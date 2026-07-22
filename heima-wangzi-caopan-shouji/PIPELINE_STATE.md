# PIPELINE_STATE

- project: heima-wangzi-caopan-shouji
- title: 黑马王子操盘手记系列
- current_stage: cangjie-stage-5-installed
- latest_note: full 17-skill package installed at /Users/yadmin/.codex/skills/heima-wangzi-caopan-shouji on 2026-07-22; nested skill directories are used directly; top-level symlink entries removed; stage 4 static fallback tests generated and validated; independent blind testing not yet run

## Directory Rules

- `source-text/`: 只放可被 cangjie 阶段 0 读取的正文文本。
- `source-text/pdf-ocr/<volume>/pages/`: 每页 OCR 原始文本，用于断点续跑和抽样复核。
- `source-text/combined/`: 全套合并语料，供后续整套蒸馏使用。
- `logs/`: 每册抽取质量日志和统计。
- `tmp/ocr-images/`: OCR 中间图片，可清理，不作为交付依据。
- `<skill-slug>/`: 阶段 2 生成的单个 skill，每个目录包含 `SKILL.md`、`test-prompts.json`、`test-results.md`。
- `INDEX.md` / `GLOSSARY.md` / `DIGEST.md`: 阶段 3/5 的整包导航、术语表和精华长文。

## Source Status

- [x] volume-01: 黑马王子操盘手记 1 (pdf)
- [x] volume-02: 黑马王子操盘手记 2 (pdf)
- [x] volume-03: 黑马王子操盘手记 3 (pdf)
- [x] volume-04: 黑马王子操盘手记 4 (pdf)
- [x] volume-05: 黑马王子操盘手记 5 (pdf)
- [x] volume-06-09: 黑马王子操盘手记 6-9 套装 (epub)

## Next

- [x] 完成全套文本质量报告。
- [x] 基于 `source-text/combined/all-source-text.md` 进入 cangjie 阶段 0。
- [x] 用户确认 `BOOK_OVERVIEW.md` 的整套方法论骨架。
- [x] 进入 cangjie 阶段 1: 5 个 extractor 提取候选方法论单元。
- [x] 完成 cangjie 阶段 1.5: 三重验证筛选。
- [x] 用户要求“做完整，不要遗落”，恢复可验证的候选，不放宽质量门槛。
- [x] 进入 cangjie 阶段 2: 为 17 个通过/恢复候选构造 RIA++ skill。
- [x] 完成 cangjie 阶段 3: 生成 `INDEX.md` 和 `GLOSSARY.md`。
- [x] 完成 cangjie 阶段 4: 为 17 个 skill 生成 `test-prompts.json` 与 `test-results.md`。
- [x] 完成 cangjie 阶段 5 交付草案: 生成 `DIGEST.md`。
- [x] 用户确认安装位置: `/Users/yadmin/.codex/skills`。
- [x] 按 cangjie 输出结构安装完整包到 `/Users/yadmin/.codex/skills/heima-wangzi-caopan-shouji`。
- [x] 已移除顶层 symlink 引用；17 个 skill 通过包内嵌套目录直接加载。
