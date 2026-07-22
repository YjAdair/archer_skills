---
name: volume-line-balance-reading
description: |
  用户需要按量学框架阅读盘面、区分价格表象和量价真实力量时使用。适用于“不要看消息，怎么看量柱量线、这个涨跌是真强还是假强、怎么判断主力行为痕迹”等信号；不适用于纯基本面分析、实时荐股或精确画线。Triggers: volume-price, volume column, volume line, dynamic balance, market reading.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第1册《股市量学ABC》；第3册《掌握量学，股市可测》
tags: [volume-price, dynamic-balance, market-reading]
related_skills:
  - slug: key-line-anchoring
    relation: depends-on
  - slug: true-false-yin-yang
    relation: composes-with
  - slug: sector-rotation-strong-following
    relation: composes-with
---

# 量柱量线动态平衡读盘框架

## R — 原文 (Reading)

> "量柱是基础，量线是灵魂，量波是抓手；量柱是量学的音符。"
>
> — 黑马王子，第3册《掌握量学，股市可测》

## I — 方法论骨架 (Interpretation)

这套框架要求先看盘面证据，而不是先听消息、指标或他人判断。
量柱表达参与力度，价柱表达价格动作，量线提供攻防边界，量波提供临盘节奏。
作者把这些信号放在“动态平衡”里看：平衡是暂时稳定，失衡说明力量正在转移。
读盘的核心不是判断涨跌颜色，而是问：量价组合背后的力量是否真实、是否可持续、是否已经失效。
它是后续关键线、真假阴阳、回马枪、凹底淘金等 skill 的基础语言。

## A1 — 书中的应用 (Past Application)

### 案例 1: 华工科技视角之争
- **问题**: 有人按均线跌破看坏华工科技。
- **方法论的使用**: 作者用黄金柱确认日、量柱量线角度重新解释。
- **结论**: 不同读盘入口会得出相反判断，量学优先看量柱量线。
- **结果**: 书中记载该股后续继续上行，成为量学视角案例。

### 案例 2: 追消息股反例
- **问题**: 利好消息公布后，散户容易追消息股。
- **方法论的使用**: 作者要求回到形态，看量柱量线是否支持。
- **结论**: 消息热不等于盘面强。
- **结果**: 追消息股被列入失败模式。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户给出一段行情描述，想按量学做第一层读盘。
2. 用户被消息、指标、K 线颜色干扰，不知道该信什么。
3. 用户想判断表面上涨/下跌背后的力量是否真实。
4. 用户准备使用真假阴阳、关键线、回马枪等具体战法前，需要统一读盘语言。

### 语言信号

- "按量柱量线怎么看"
- "这个上涨是真强还是假强"
- "不看消息，只看盘面怎么判断"
- "volume-price reading / dynamic balance / volume line first"

### 与相邻 skill 的区分

- 与 `key-line-anchoring` 的区别: 本 skill 是总读盘框架；后者专门处理线如何生根和验证。
- 与 `true-false-yin-yang` 的区别: 本 skill 看整体量价平衡；后者专门辨别 K 线阴阳真假。
- 与 `sector-rotation-strong-following` 的区别: 本 skill 看单个对象或市场状态；后者看板块和强者切换。

## E — 可执行步骤 (Execution)

1. **拆成四类证据**
   - 分别列出量柱、价柱、量线、量波信息。
   - 完成标准: 不把消息、观点、指标混进第一层证据。

2. **判断平衡或失衡**
   - 看量价是否同步、背离、缩放、阴阳胜负和线位得失。
   - 完成标准: 给出“平衡/上行失衡/下行失衡/不确定”之一。

3. **转入具体 skill**
   - 若问题是取线，转 `key-line-anchoring`；若是阴阳真假，转 `true-false-yin-yang`；若是进退预案，转 `premarket-three-lines`。
   - 完成标准: 输出下一步应该使用的具体方法，而不是直接给买卖建议。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 用户只问财报、公司基本面、宏观政策细节。
- 用户要求具体股票买卖建议或收益预测。
- 用户需要精确画线但没有图表或行情数据。

### 作者在书中警告的失败模式

- 追消息股而不看形态。
- 今天看价柱、明天看均线、后天又回量柱，标准漂移。
- 迷信软件公式标注，不解释量价结构。

### 作者的盲点 / 时代局限

- 把量价变化解释为主力行为有启发性，但可能高估“有计划操盘”的解释力。
- 该体系主要来自 A 股历史样本，不应直接套到其他市场。

### 容易混淆的邻近方法论

- `key-line-anchoring`: 画线和线位。
- `true-false-yin-yang`: 阴阳真假。
- `premarket-three-lines`: 预案执行。

## 相关 skills

- depends-on `key-line-anchoring`: 量线必须有根，不能随手画。
- composes-with `true-false-yin-yang`: 表面阴阳要回到量价结构确认。
- composes-with `sector-rotation-strong-following`: 板块也可当作一只股票读量价。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
