# App Store Connect API 操作参考

## 能力检查清单

真实 API 操作前先检查：

1. Node.js 可用。`asc_request.mjs` 使用内置 `crypto` 和 `fetch`。
2. 当前 skill 目录下存在 `config/config.json`，或 `ASC_CONFIG_PATH` 指向用户自定义配置文件。
3. 配置包含 `issuerId`、`keyId`、`privateKeyPath`。
4. `.p8` 文件存在、可读、格式像 Apple 私钥，并已放入 `keys/` 或由配置明确指向。
5. 当前操作所需资源 ID 已确认。API 要求资源 ID 时，不要用名称猜。
6. 网络调用可能需要 sandbox escalation。

## 配置字段

必填：

- `issuerId`: App Store Connect API 的 Issuer UUID。
- `keyId`: App Store Connect API Key ID。
- `privateKeyPath`: `.p8` 私钥路径。默认配置中推荐使用相对路径，例如 `keys/AuthKey_ABC123DEFG.p8`。

可选但常用：

- `appId`: App Store Connect 的 App 资源 ID。
- `bundleId`: Bundle Identifier，例如 `com.openclaw.desktop`。
- `appInfoId`: App Information 资源 ID。
- `ageRatingDeclarationId`: 年龄分级声明资源 ID。
- `appStoreVersionId`: App Store 版本资源 ID。
- `localizations`: 按 locale 保存的本地化资源 ID，例如 `{ "en-US": { "appInfoLocalizationId": "..." } }`。

## 变更类操作

执行前必须取得用户明确批准：

- PATCH 元数据、隐私政策 URL、年龄分级、价格、可用地区、截图、App 版本、构建版本分配、审核提交信息。
- 上传、删除、重排或替换截图。
- 创建、删除或修改 App 内购买项目/订阅。

变更后：

1. 读回被修改的准确资源。
2. 只输出非密钥字段。
3. 说明未更新成功的字段，或公开 API 不支持的字段。

## 公开 API 支持边界

公开 API 通常支持：

- 读取 apps、app infos、versions、builds、localizations、screenshot sets 和 screenshots。
- 当 Apple 在资源上暴露字段时，PATCH `appInfoLocalizations` 的 `privacyPolicyUrl` 等字段。
- 当资源存在且账号有权限时，PATCH 年龄分级声明字段。

已知限制：

- App Privacy 问卷/隐私营养标签的数据收集表单，在公开 App Store Connect API 中没有稳定可写资源。除非 Apple 当前官方文档已经公开对应端点，否则应准备填写方案，让用户在后台手动填写。

## 资源 ID 纪律

优先使用读回结果、现有配置或官方 API 列表中的资源 ID。不要从 locale 或可见名称推断 ID。

常用资源 ID 包括：

- App ID
- App Info ID
- 每个 locale 对应的 App Info Localization ID
- App Store Version ID
- Age Rating Declaration ID
- 每个 locale/display type 对应的 Screenshot Set ID

## 手动配置

用户可以不运行 `asc_config.py`，直接创建 `config/config.json`：

```json
{
  "issuerId": "00000000-0000-0000-0000-000000000000",
  "keyId": "ABC123DEFG",
  "privateKeyPath": "keys/AuthKey_ABC123DEFG.p8",
  "appId": "1234567890",
  "bundleId": "com.example.app",
  "localizations": {
    "en-US": {
      "appInfoLocalizationId": "..."
    },
    "zh-Hans": {
      "appInfoLocalizationId": "..."
    }
  }
}
```

导入证书到 `keys/` 后设置权限：

```bash
chmod 700 config keys
chmod 600 config/config.json
chmod 600 keys/*.p8
```
