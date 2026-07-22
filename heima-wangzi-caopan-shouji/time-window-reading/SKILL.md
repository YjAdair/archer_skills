---
name: time-window-reading
description: |
  用户在读历史盘前预报、收评、交易案例或课程材料，想训练判断而不是抄答案时使用。适用于“怎么看这篇旧收评、怎么复盘历史行情、怎么练盘前三线”等信号；不适用于实时行情预测、真实买卖建议或只查术语。Triggers: time window, historical review, backtest reading, forecast training.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第1册导读；第6册《通过时间窗口采撷操盘绝活》
tags: [reading-method, backtest, forecast-training]
related_skills:
  - slug: heima-risk-discipline
    relation: composes-with
  - slug: premarket-three-lines
    relation: composes-with
  - slug: failure-case-review
    relation: composes-with
---

# 时间窗口三步阅读法

## R — 原文 (Reading)

> "以这个时间为起点，先用你自己的眼光预判未来的行情，并记下你的预判结论。"
>
> — 黑马王子，第1册导读

## I — 方法论骨架 (Interpretation)

这套读法把书从“答案集”变成“训练场”。
读者不能先看作者结论，也不能拿已经发生的结果倒推自己很懂。
第一步，把自己放回文章发表的那个时间点，只看当时能看到的信息。
第二步，先写下自己的方向、点位、条件和风险预判。
第三步，再对照作者当时的判断、后续真实走势和自己的差距。
它训练的是独立判断、预案表达和错误校正，而不是背诵股票名。

## A1 — 书中的应用 (Past Application)

### 案例 1: 读盘前预报而不是偷看答案
- **问题**: 读者容易只看作者预报准不准，忽略自己当时能否看出来。
- **方法论的使用**: 作者要求以发表时间为窗口，先独立预判再看后续行情。
- **结论**: 自己的预判差距才是真训练材料。
- **结果**: 后几册大量盘前/收评都按这种方式构成连续训练样本。

### 案例 2: 断章取义反例
- **问题**: 很多读者只摘收评中的某句话或股票名。
- **方法论的使用**: 作者反复要求看前提、条件、位置和失效边界。
- **结论**: 只抄结论会把训练材料变成错误指令。
- **结果**: 断章取义被列入反例池。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户拿到旧收评、盘前预报、交易手记，想知道怎么学。
2. 用户想把历史行情做成训练，而不是让 agent 总结结论。
3. 用户要复盘自己和作者判断差在哪里。
4. 用户说自己看了很多战法但不会用。

### 语言信号

- "这篇旧收评应该怎么读"
- "帮我按时间窗口复盘"
- "我不要抄答案，想训练判断"
- "先别告诉我结果，帮我做预测练习"
- "historical trading review / backtest reading / forecast drill"

### 与相邻 skill 的区分

- 与 `premarket-three-lines` 的区别: 本 skill 管学习和复盘流程；后者管具体盘前三线如何设预案。
- 与 `failure-case-review` 的区别: 本 skill 可用于成功和失败样本；后者专门处理已经犯错的交易。
- 与 `heima-risk-discipline` 的区别: 本 skill 是训练法，不判断能不能实盘。

## E — 可执行步骤 (Execution)

1. **冻结时间窗口**
   - 明确文章发表日、当时可见信息、不能看的未来结果。
   - 完成标准: 输出“当时可见/不可见信息”两栏。

2. **先写用户预判**
   - 要求用户或 agent 先写方向、关键线、触发条件、失效条件。
   - 完成标准: 至少包含方向、上/中/下或风险线、确认条件。

3. **对照作者和真实走势**
   - 再看作者原文、后续走势、误差和原因。
   - 完成标准: 输出“我错在哪里/作者强在哪里/下次如何改”的三点复盘。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 用户要求实时买卖建议。
- 用户只是要术语解释或书摘摘要。
- 用户没有历史文本、时间点或行情材料。

### 作者在书中警告的失败模式

- 只关注王子收评中的某一句话，忘记前提和条件。
- 看太多战法没有消化，生搬硬套。
- 迷信作者，不自己独立判断。

### 作者的盲点 / 时代局限

- 历史训练不能直接证明当前市场可交易。
- 旧行情中的涨停生态、监管和参与者结构可能已经变化。

### 容易混淆的邻近方法论

- `premarket-three-lines`: 具体预案。
- `failure-case-review`: 失败审计。
- `heima-risk-discipline`: 实盘门禁。

## 相关 skills

- composes-with `premarket-three-lines`: 时间窗口训练常以三线预案作为答题格式。
- composes-with `failure-case-review`: 训练结果偏差较大时，进入失败复盘。
- composes-with `heima-risk-discipline`: 防止把历史训练直接当作实盘能力。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
