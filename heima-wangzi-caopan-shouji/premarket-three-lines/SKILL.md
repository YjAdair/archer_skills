---
name: premarket-three-lines
description: |
  用户要把大盘或个股分析转成盘前预案，设置上线/中线/下线、确认条件和失效动作时使用。适用于“明天三线怎么设、跌破下线怎么办、中线是什么、盘中怎么按预案执行”等信号；不适用于没有线位证据的猜涨跌或真实交易指令。Triggers: premarket plan, three lines, upper middle lower line, invalidation.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第2册盘前三线；第9册0516-0524连续收评
tags: [premarket-plan, three-lines, execution-boundary]
related_skills:
  - slug: key-line-anchoring
    relation: depends-on
  - slug: left-proof-right-confirmation
    relation: composes-with
  - slug: double-yin-lagua-exit
    relation: composes-with
---

# 盘前三线预案与失效条件

## R — 原文 (Reading)

> "上线、中线、下线都是关键平衡线；中线是操盘的行为中枢。"
>
> — 黑马王子，第3册《量波的三线建构》

## I — 方法论骨架 (Interpretation)

盘前三线不是猜明天涨跌，而是把临盘行为提前写成条件化预案。
上线表示上攻观察边界，下线表示防守或失效边界，中线是多空行为中枢。
盘中价格在三线内运行时，按预案执行；有效越线或破线时，切换到对应方案。
三线的价值在于限制情绪临时反应，让用户知道什么时候观察、什么时候确认、什么时候退出或等待。
它依赖关键线生根，不能随意填三个数字。

## A1 — 书中的应用 (Past Application)

### 案例 1: 2017 年 5 月 3090 平衡点
- **问题**: 大盘连续弱势后，如何判断反弹与风险边界。
- **方法论的使用**: 作者围绕 3090、3071、3054 等关键穴位滚动设盘前三线。
- **结论**: 线位成为每天观察主力是否守住平衡的依据。
- **结果**: 0523 大盘低点和收盘与预案高度接近。

### 案例 2: 2017-06-08 三线精准
- **问题**: 过峰保顶第一天，如何判断是否接力。
- **方法论的使用**: 前日预设 3130、3140、3154 三线。
- **结论**: 最高和最低贴近三线后，继续观察凹口/凹底接力。
- **结果**: 作者同时提醒突破不力要高抛。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户有若干关键线，想组织成第二天预案。
2. 用户不知道盘中跌破/突破某线后该如何切换。
3. 用户被消息影响，想检查预案是否漂移。
4. 用户想把历史收评按上中下线做训练。

### 语言信号

- "明天盘前三线怎么设"
- "中线破了怎么办"
- "上线/下线分别代表什么"
- "premarket three lines / upper middle lower / invalidation"

### 与相邻 skill 的区分

- 与 `key-line-anchoring` 的区别: 本 skill 假设线已有依据，负责组织成预案。
- 与 `left-proof-right-confirmation` 的区别: 本 skill 设边界；后者判断信号是否已经确认。
- 与 `double-yin-lagua-exit` 的区别: 本 skill 是事前预案；后者是风险触发后的出货流程。

## E — 可执行步骤 (Execution)

1. **选择三条线**
   - 从关键线池中选上线、中线、下线，并说明每条线的来源。
   - 完成标准: 三线均有生根证据，不是拍脑袋数字。

2. **写三种情景**
   - 上破如何观察，中线附近如何判断，跌破下线如何失效。
   - 完成标准: 每条线至少有一个触发动作和一个失效动作。

3. **盘中只按条件切换**
   - 若走势不符合预案，先标记“预案失效/需重建”，不临时找理由硬扛。
   - 完成标准: 输出条件化语言，如“若 A 则 B；否则 C”。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 线位没有来源，只有用户想猜涨跌。
- 用户要求真实下单、仓位比例或收益预测。
- 当前问题只是判断某个信号是否确认，应转 `left-proof-right-confirmation`。

### 作者在书中警告的失败模式

- 被重大消息带偏盘前三线。
- 不等确认就抄底或建仓。
- 未设止损就下单。

### 作者的盲点 / 时代局限

- 三线精准案例来自特定 A 股环境，不能等同于普适预测能力。
- 线位需要图表和行情数据校验。

### 容易混淆的邻近方法论

- `key-line-anchoring`: 线位来源。
- `left-proof-right-confirmation`: 确认门禁。
- `two-dragon-positioning`: 变盘节点。

## 相关 skills

- depends-on `key-line-anchoring`: 三线必须来自有根的关键线。
- composes-with `left-proof-right-confirmation`: 到线后还要等确认。
- composes-with `double-yin-lagua-exit`: 三线失效可触发防守流程。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
