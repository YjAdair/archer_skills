---
name: app-store-connect-api
description: 安全配置和操作 App Store Connect API，包含 skill 目录内 config/keys 检查、必填参数检测、API Key 证书检测、JWT 鉴权、元数据更新、隐私政策 URL 更新、年龄分级更新、截图或资源状态检查，以及变更后的读回验证。当用户要求通过 API 配置或操作 App Store Connect、上传或更新 App 元数据、检查 ASC 资源、验证 ASC 凭证，或准备可复用的 App Store Connect 自动化流程时使用。
---

# App Store Connect API

使用这个 skill 通过官方 App Store Connect API 执行操作，同时避免泄露凭证、跳过确认门禁或误改线上数据。命令中的路径都以当前 skill 目录为基准，不写死某台机器的安装路径。

## SOP 流程

1. 先确认当前 skill 目录下是否存在 `config/` 和 `keys/`。
2. 运行配置检测：
   ```bash
   python3 scripts/asc_config.py check
   ```
3. 如果 `config/config.json` 不存在，或字段/证书不符合要求，先提醒用户提供参数和 `.p8` 证书，或按“手动配置格式”自行填写并导入到 `keys/`。
4. 配置齐全后，再确认用户要执行的 App Store Connect 操作，并判断是否会修改线上数据。
5. 对任何会修改 ASC 的操作，必须先取得用户明确批准，再执行变更，最后读回资源确认结果。

## 目录约定

当前 skill 默认使用自身目录下的配置和证书目录：

```text
app-store-connect-api/
├── config/
│   └── config.json
├── keys/
│   └── AuthKey_<KEY_ID>.p8
├── scripts/
└── references/
```

用户也可以通过 `ASC_CONFIG_PATH` 或 `--config` 指定自己的配置文件。若使用默认目录，`privateKeyPath` 推荐写相对路径，例如 `keys/AuthKey_ABC123DEFG.p8`。

## 需要用户提供的参数

- `issuerId`：App Store Connect API 的 Issuer ID。获取方式：App Store Connect -> Users and Access -> Integrations -> App Store Connect API。
- `keyId`：API Key ID。获取方式：同一 API Keys 页面中对应 key 的 Key ID。
- `.p8` 私钥文件：创建 API Key 时下载的 `AuthKey_<KEY_ID>.p8`。Apple 只允许下载一次，丢失后需要重新创建 key。
- `appId`：App Store Connect 中 App 的资源 ID。可通过 API 列表、已知 ASC 链接或现有项目记录获取。
- `bundleId`：应用 Bundle ID，例如 `com.example.app`。
- 可选资源 ID：`appInfoId`、`appInfoLocalizationId`、`appStoreVersionId`、`ageRatingDeclarationId`、截图集 ID 等。执行对应 API 操作前必须确认，不能靠名称猜。

## 初始化配置

从用户提供的 `.p8` 路径初始化，并把证书复制到当前 skill 的 `keys/`：

```bash
python3 scripts/asc_config.py init \
  --issuer-id <issuer_uuid> \
  --key-id <key_id> \
  --private-key-path <path/to/AuthKey_KEYID.p8> \
  --app-id <app_store_connect_app_id> \
  --bundle-id <bundle_id> \
  --copy-key
```

查看脱敏后的配置：

```bash
python3 scripts/asc_config.py show
```

## API 操作命令

检查 JWT 和 App 读回：

```bash
node scripts/asc_request.mjs whoami
```

更新某个本地化的隐私政策 URL：

```bash
node scripts/asc_request.mjs patch-privacy-url \
  --localization-id <appInfoLocalizationId> \
  --url <https_url>
```

发起通用 API 请求：

```bash
node scripts/asc_request.mjs request GET /v1/apps/<app_id>
node scripts/asc_request.mjs request PATCH /v1/appInfoLocalizations/<id> --json-file /tmp/body.json
```

## 安全规则

- 不要打印 `.p8` 内容、JWT、密码、token 或完整密钥 JSON。
- 不要把证书或配置保存到代码仓库、日志或临时对话输出里。
- 如果按本 skill 的默认方式保存证书，只放在当前 skill 的 `keys/` 目录，并设置为 `600` 权限。
- 将 App Store Connect 的生产变更视为外部/公开变更。若用户没有明确批准本次具体变更，先停下来确认。
- 优先使用官方 App Store Connect API。若公开 API 不支持某项操作，要明确说明；只有在用户批准后，才使用人工或浏览器方案。
- 每次 `PATCH`、`POST`、`DELETE` 后都要读回对应资源，并向用户报告读回字段。

## 引用资料

- 当需要把用户需求映射到 App Store Connect API 资源，或判断公开 API 是否支持某项操作时，读取 `references/api-operations.md`。
- 修改配置检测逻辑前，先读取 `scripts/asc_config.py`。
- 新增 API helper 命令前，先读取 `scripts/asc_request.mjs`。
