#!/usr/bin/env node

import { sign } from "node:crypto";
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const API_BASE = "https://api.appstoreconnect.apple.com";
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const SKILL_ROOT = path.resolve(__dirname, "..");
const DEFAULT_CONFIG_PATH = path.join(SKILL_ROOT, "config", "config.json");

function fail(message) {
  console.error(`[asc_request] ${message}`);
  process.exit(1);
}

function readJson(filePath) {
  return JSON.parse(readFileSync(filePath, "utf8"));
}

function base64url(input) {
  return Buffer.from(input).toString("base64url");
}

function createJwt(config) {
  const privateKeyPem = readFileSync(config.privateKeyPath, "utf8");
  const now = Math.floor(Date.now() / 1000);
  const header = {
    alg: "ES256",
    kid: config.keyId,
    typ: "JWT",
  };
  const payload = {
    iss: config.issuerId,
    iat: now,
    exp: now + 20 * 60,
    aud: "appstoreconnect-v1",
  };
  const signingInput = `${base64url(JSON.stringify(header))}.${base64url(JSON.stringify(payload))}`;
  const signature = sign("sha256", Buffer.from(signingInput), {
    key: privateKeyPem,
    dsaEncoding: "ieee-p1363",
  });
  return `${signingInput}.${signature.toString("base64url")}`;
}

function loadConfig() {
  const configPath = process.env.ASC_CONFIG_PATH || DEFAULT_CONFIG_PATH;
  if (!existsSync(configPath)) fail(`missing config: ${configPath}`);
  const config = readJson(configPath);
  for (const field of ["issuerId", "keyId", "privateKeyPath"]) {
    if (!config[field]) fail(`missing config field: ${field}`);
  }
  const privateKeyPath = resolvePrivateKeyPath(config.privateKeyPath, configPath);
  if (!existsSync(privateKeyPath)) fail(`private key not found: ${privateKeyPath}`);
  config.privateKeyPath = privateKeyPath;
  return config;
}

function resolvePrivateKeyPath(rawPath, configPath) {
  if (path.isAbsolute(rawPath)) return rawPath;
  const configDir = path.dirname(configPath);
  const baseDir = configDir === path.join(SKILL_ROOT, "config") ? SKILL_ROOT : configDir;
  return path.join(baseDir, rawPath);
}

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i += 1) {
    const value = argv[i];
    if (value.startsWith("--")) {
      const key = value.slice(2);
      const next = argv[i + 1];
      if (!next || next.startsWith("--")) {
        args[key] = true;
      } else {
        args[key] = next;
        i += 1;
      }
    } else {
      args._.push(value);
    }
  }
  return args;
}

async function request(config, method, apiPath, body) {
  const token = createJwt(config);
  const response = await fetch(`${API_BASE}${apiPath}`, {
    method,
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await response.text();
  let parsed = null;
  if (text) {
    try {
      parsed = JSON.parse(text);
    } catch {
      parsed = text;
    }
  }
  if (!response.ok) {
    fail(`${method} ${apiPath} failed: ${response.status} ${typeof parsed === "string" ? parsed : JSON.stringify(parsed, null, 2)}`);
  }
  return parsed;
}

function print(value) {
  console.log(JSON.stringify(value, null, 2));
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const [command, first, second] = args._;
  const config = loadConfig();

  if (command === "whoami") {
    const result = config.appId
      ? await request(config, "GET", `/v1/apps/${config.appId}`)
      : { ok: true, message: "JWT config loaded. Add appId to config for an app readback check." };
    print(result);
    return;
  }

  if (command === "request") {
    const method = first;
    const apiPath = second;
    if (!method || !apiPath) fail("usage: request <METHOD> <PATH> [--json-file file]");
    const body = args["json-file"] ? readJson(args["json-file"]) : undefined;
    print(await request(config, method.toUpperCase(), apiPath, body));
    return;
  }

  if (command === "patch-privacy-url") {
    const id = args["localization-id"];
    const url = args.url;
    if (!id || !url) fail("usage: patch-privacy-url --localization-id <id> --url <https_url>");
    if (!String(url).startsWith("https://")) fail("privacy policy URL must be https");
    await request(config, "PATCH", `/v1/appInfoLocalizations/${id}`, {
      data: {
        type: "appInfoLocalizations",
        id,
        attributes: { privacyPolicyUrl: url },
      },
    });
    const readback = await request(config, "GET", `/v1/appInfoLocalizations/${id}`);
    print({
      id,
      locale: readback.data?.attributes?.locale,
      privacyPolicyUrl: readback.data?.attributes?.privacyPolicyUrl,
    });
    return;
  }

  fail("commands: whoami | request | patch-privacy-url");
}

main().catch((error) => fail(error.stack || error.message));
