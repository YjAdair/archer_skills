---
name: project-knowledge-manager
description: 项目经验沉淀与管理工具。用于初始化项目知识库结构（cloudy.md），基于文档或代码自动设计项目规范和架构模式，以及记录团队术语和业务逻辑。当用户需要“初始化项目知识库”、“制定项目规范”、“设计架构模式”或“记录团队黑话”时使用此技能。
---

# Project Knowledge Manager

## 1. 项目初始化 (Project Initialization)

当用户请求初始化项目知识库、生成 `cloudy.md` 或开始项目经验沉淀时：

1.  运行初始化脚本：
    ```bash
    python3 scripts/init_project.py
    ```
2.  脚本会在当前目录下生成 `cloudy.md`，包含预设的结构（项目规范、架构模式、团队黑话、错误记录）。
3.  告知用户初始化完成，并简要介绍 `cloudy.md` 的结构。

## 2. 项目规范和架构模式设计 (Design Specifications & Architecture)

当用户请求设计项目规范、架构模式，或填充 `cloudy.md` 的相关章节时：

### 步骤 1: 获取上下文 (Gather Context)

*   **如果是新项目**（用户提供了文档路径）：
    *   使用 `LS` 列出文档目录。
    *   使用 `Read` 读取相关的产品文档或需求文档。
*   **如果是老项目**（默认情况）：
    *   使用 `LS` 查看项目根目录结构。
    *   读取关键配置文件（如 `package.json`, `requirements.txt`, `pom.xml`, `go.mod` 等）以识别技术栈。
    *   读取 `README.md`（如果存在）。
    *   浏览核心源代码目录（如 `src`, `lib`, `app` 等）以理解现有架构。

### 步骤 2: 设计与生成 (Design & Generate)

基于获取的上下文，运用你的专业知识设计以下内容：
1.  **项目规范**：代码风格、命名约定、提交规范、依赖管理等。
2.  **架构模式**：分层架构、设计模式（MVC/MVVM/DDD等）、状态管理、UI/业务分离策略等。

### 步骤 3: 更新知识库 (Update Knowledge Base)

将设计好的内容写入 `cloudy.md`。你可以使用 `scripts/update_cloudy.py` 脚本，或者直接使用 `SearchReplace` / `Write` 工具（如果修改较多）。

使用脚本更新示例：
```bash
python3 scripts/update_cloudy.py --section "项目规范" --content "- 所有的接口必须返回 JSON 格式\n- 变量命名使用驼峰式"
python3 scripts/update_cloudy.py --section "架构模式" --content "- 采用 Clean Architecture\n- 领域层不依赖外部库"
```

## 3. 更新团队黑话与业务逻辑 (Update Jargon & Business Logic)

当用户提供新的团队术语、黑话或特定的业务逻辑解释时：

1.  整理用户提供的信息，使其清晰易懂。
2.  使用脚本更新到 `cloudy.md` 的“团队黑话与业务逻辑”章节：
    ```bash
    python3 scripts/update_cloudy.py --section "团队黑话与业务逻辑" --content "- **[术语名]**: [解释]\n- **[逻辑名]**: [逻辑描述]"
    ```

## 4. 错误转化记录 (Error Transformation)

当用户分享一个错误修复经验或教训时：

1.  总结错误原因和解决方案。
2.  提取为一条可预防的教训。
3.  更新到 `cloudy.md` 的“错误转化记录”章节：
    ```bash
    python3 scripts/update_cloudy.py --section "错误转化记录" --content "- [日期] [错误描述] -> [教训/预防措施]"
    ```
