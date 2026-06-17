#!/usr/bin/env python3
"""Configure and validate App Store Connect API credentials for this skill.

This script never prints private key contents.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import stat
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_DIR = SKILL_ROOT / "config"
DEFAULT_CONFIG_PATH = DEFAULT_CONFIG_DIR / "config.json"
REQUIRED_FIELDS = ("issuerId", "keyId", "privateKeyPath")


def config_path(value: str | None = None) -> Path:
    raw = value or os.environ.get("ASC_CONFIG_PATH")
    return Path(raw).expanduser() if raw else DEFAULT_CONFIG_PATH


def key_base_dir(target_config: Path) -> Path:
    if target_config.parent == DEFAULT_CONFIG_DIR:
        return SKILL_ROOT
    return target_config.parent


def resolve_private_key_path(raw_path: str, target_config: Path) -> Path:
    path = Path(raw_path).expanduser()
    if path.is_absolute():
        return path
    return key_base_dir(target_config) / path


def secure_write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.parent.chmod(0o700)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    path.chmod(0o600)


def load_config(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"missing config: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def masked(value: str | None, keep: int = 4) -> str | None:
    if not value:
        return value
    if len(value) <= keep * 2:
        return "*" * len(value)
    return f"{value[:keep]}...{value[-keep:]}"


def validate_private_key(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        errors.append(f"private key not found: {path}")
        return errors
    if not path.is_file():
        errors.append(f"private key path is not a file: {path}")
        return errors
    text = path.read_text(encoding="utf-8", errors="replace")
    if "BEGIN PRIVATE KEY" not in text or "END PRIVATE KEY" not in text:
        errors.append("private key does not look like an Apple .p8 private key")
    mode = stat.S_IMODE(path.stat().st_mode)
    if mode & 0o077:
        errors.append(f"private key permissions are too open: {oct(mode)}; use chmod 600")
    return errors


def command_init(args: argparse.Namespace) -> None:
    target_config = config_path(args.config)
    source_key = Path(args.private_key_path).expanduser().resolve()
    private_key_path = source_key
    private_key_config_value = str(source_key)

    if args.copy_key:
        keys_dir = key_base_dir(target_config) / "keys"
        keys_dir.mkdir(parents=True, exist_ok=True)
        keys_dir.chmod(0o700)
        private_key_path = keys_dir / f"AuthKey_{args.key_id}.p8"
        if source_key != private_key_path:
            shutil.copy2(source_key, private_key_path)
        private_key_path.chmod(0o600)
        private_key_config_value = f"keys/AuthKey_{args.key_id}.p8"

    config = {
        "issuerId": args.issuer_id,
        "keyId": args.key_id,
        "privateKeyPath": private_key_config_value,
    }
    for key, value in {
        "appId": args.app_id,
        "bundleId": args.bundle_id,
        "appInfoId": args.app_info_id,
        "ageRatingDeclarationId": args.age_rating_declaration_id,
        "appStoreVersionId": args.app_store_version_id,
    }.items():
        if value:
            config[key] = value

    secure_write_json(target_config, config)
    print(json.dumps({
        "configPath": str(target_config),
        "issuerId": masked(args.issuer_id),
        "keyId": args.key_id,
        "privateKeyPath": private_key_config_value,
        "resolvedPrivateKeyPath": str(private_key_path),
        "copiedKey": bool(args.copy_key),
    }, indent=2, ensure_ascii=False))


def command_check(args: argparse.Namespace) -> None:
    target_config = config_path(args.config)
    config = load_config(target_config)
    errors: list[str] = []

    for field in REQUIRED_FIELDS:
        if not str(config.get(field, "")).strip():
            errors.append(f"missing required field: {field}")

    key_path_raw = config.get("privateKeyPath")
    if key_path_raw:
        errors.extend(validate_private_key(resolve_private_key_path(key_path_raw, target_config)))

    mode = stat.S_IMODE(target_config.stat().st_mode)
    if mode & 0o077:
        errors.append(f"config permissions are too open: {oct(mode)}; use chmod 600")

    result = {
        "ok": not errors,
        "configPath": str(target_config),
        "issuerId": masked(config.get("issuerId")),
        "keyId": config.get("keyId"),
        "privateKeyPath": config.get("privateKeyPath"),
        "resolvedPrivateKeyPath": str(resolve_private_key_path(key_path_raw, target_config)) if key_path_raw else None,
        "appId": config.get("appId"),
        "bundleId": config.get("bundleId"),
        "errors": errors,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if errors:
        raise SystemExit(1)


def command_show(args: argparse.Namespace) -> None:
    target_config = config_path(args.config)
    config = load_config(target_config)
    safe = dict(config)
    safe["issuerId"] = masked(safe.get("issuerId"))
    safe["privateKeyLoaded"] = bool(
        safe.get("privateKeyPath") and resolve_private_key_path(safe["privateKeyPath"], target_config).exists()
    )
    print(json.dumps(safe, indent=2, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(description="Configure App Store Connect API credentials")
    parser.add_argument("--config", help="Config path. Defaults to ASC_CONFIG_PATH or this skill's config/config.json.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="Create or replace a local ASC config")
    init.add_argument("--issuer-id", required=True)
    init.add_argument("--key-id", required=True)
    init.add_argument("--private-key-path", required=True)
    init.add_argument("--app-id")
    init.add_argument("--bundle-id")
    init.add_argument("--app-info-id")
    init.add_argument("--age-rating-declaration-id")
    init.add_argument("--app-store-version-id")
    init.add_argument("--copy-key", action="store_true", help="Copy .p8 into this skill's keys directory")
    init.set_defaults(func=command_init)

    check = subparsers.add_parser("check", help="Validate local config and key file")
    check.set_defaults(func=command_check)

    show = subparsers.add_parser("show", help="Print sanitized config")
    show.set_defaults(func=command_show)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
