---
name: twitter-article-scraper
description: 抓取指定博主的长文章，保存为Markdown。具备模拟真人行为、自动去重、持久化登录等高级特性。
---

# Twitter Article Scraper Skill

## Overview
本 Skill 是一个高度拟人化的 Twitter (X) 文章抓取工具。它专为长期稳定运行设计，能够模拟真实用户的阅读习惯，自动抓取指定博主的最新长文章（Articles），并将其转换为 Markdown 格式（保留图片和视频链接）归档。

核心优势：
- **高度隐蔽 (Stealth)**：注入反检测脚本，隐藏 Webdriver 特征，降低被识别风险。
- **真人模拟 (Human-Like)**：
    - **Click-to-Open**：模拟点击文章卡片进入详情页，而非直接请求链接。
    - **智能阅读**：根据文章字数计算合理的阅读停留时间（基于 250 wpm 阅读速度）。
    - **随机行为**：在操作间隙加入随机等待和鼠标滚动。
- **持久化登录**：使用本地 Chrome Profile 保存登录状态，一次登录，长期有效。
- **智能调度**：支持配置多个允许运行的时间窗口（如晨读、午休、晚间），模拟正常作息。

## Workflow (工作流)

1.  **环境初始化**：
    *   脚本启动，自动识别脚本所在目录。
    *   加载 `chrome_profile`（如果不存在则创建），启动配置了反检测参数的 Chrome 浏览器。

2.  **全局登录检查**：
    *   访问 Twitter 主页。
    *   **智能检测**：使用高效的 `wait_for_selector` 检查登录状态。
    *   **交互式登录**：如果未登录，脚本会静默等待用户在浏览器窗口中手动登录。登录成功后自动继续。

3.  **博主遍历**：
    *   根据 `CONFIG` 中的 `usernames` 列表，依次访问每个博主的 Articles 页面。
    *   **时间窗口检查**：如果当前时间不在 `schedule_windows` 定义的范围内（如深夜），脚本会自动停止。

4.  **文章抓取循环**：
    *   **列表加载**：等待博主文章列表加载，并执行随机滚动。
    *   **随机篇数**：根据 `articles_per_session_range` 配置，随机决定本轮抓取 1-N 篇文章。
    *   **点击进入**：模拟用户按住修饰键（Meta/Ctrl）点击文章时间戳或卡片，进入文章详情页。
    *   **模拟阅读**：根据文章长度计算阅读时间，并进行随机滚动，停留 15-180 秒不等。
    *   **内容提取**：解析 DOM，提取标题、日期、正文、图片和视频，转换为 Markdown。
    *   **增量保存**：检查本地是否已存在同名/同日期文件。如果遇到比本地最新文章更旧的文章，智能判断停止该博主的抓取（假设列表按时间倒序）。

5.  **休眠与结束**：
    *   在抓取每篇文章和切换每个博主之间，执行符合人类习惯的随机等待。
    *   所有任务完成后，关闭浏览器上下文（保留 Profile 数据）。

## Configuration (配置)

所有配置均位于 `scripts/scrape_twitter.py` 顶部的 `CONFIG` 字典中：

```python
CONFIG = {
    # 1. 博主列表
    "usernames": ["dotey", "elonmusk"],

    # 2. 运行时间窗口 (模拟作息)
    "schedule_windows": [
        {"start": "07:30", "end": "09:00"},
        {"start": "12:00", "end": "14:00"},
        {"start": "19:00", "end": "23:00"}
    ],

    # 3. 阅读行为模拟
    "articles_per_session_range": (1, 4), # 每次随机抓取 1-4 篇
    "reading_speed_wpm": 250,             # 阅读速度 (词/分)
    "min_reading_time": 15,               # 最短停留 (秒)
    "max_reading_time": 180,              # 最长停留 (秒)

    # 4. 随机间隔 (秒)
    "scrape_interval_range": (5, 15),     # 文章间过渡时间
    "blogger_interval_range": (30, 90),   # 博主切换时间
    
    # 5. 路径配置 (自动生成，通常无需修改)
    "output_dir": "...",   # 文章保存路径 (默认: scripts/articles)
    "user_data_dir": "..." # Profile 路径 (默认: scripts/chrome_profile)
}
```

## Usage

### 1. 安装依赖
```bash
cd twitter-article-scraper/scripts
pip3 install -r requirements.txt
python3 -m playwright install chromium
```

### 2. 运行
```bash
python3 scripts/scrape_twitter.py
```

### 3. 输出结构
```
scripts/articles/
├── dotey/
│   ├── 2024-03-20_关于AI的思考.md
│   └── ...
└── elonmusk/
    └── 2024-03-21_Mars_Colonization.md
```

## 多任务操作指南 (Multitasking Guide)
脚本运行时，**您可以进行其他工作**，无需一直盯着浏览器。

*   **后台运行**：您可以将脚本打开的 Chrome 窗口**最小化**，或者拖动到另一个桌面 (Space)。脚本会在后台静默运行，不会被暂停。
*   **互不干扰**：脚本的点击和滚动操作是直接发送给浏览器进程的，**不会**抢占您的鼠标光标或键盘焦点。
*   **注意事项**：
    *   请勿关闭该浏览器窗口。
    *   请勿在同一个浏览器窗口中手动操作 Twitter，以免干扰脚本的自动化流程。
    *   建议让脚本在一个独立的桌面空间运行，这样既能随时监控进度，又不会干扰您的主屏幕工作。

## Troubleshooting
- **无法找到文章**：请确认提供的URL是否为博主的 "Articles" 页面（例如 `https://x.com/username/articles`），并且该博主确实发布过长文章。
