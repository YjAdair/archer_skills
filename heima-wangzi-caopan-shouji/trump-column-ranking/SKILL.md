---
name: trump-column-ranking
description: |
  用户需要判断黄金柱、将军柱、元帅柱、王牌柱是否成立，以及能否作为后续支撑、攻防线或战法根基时使用。适用于“这个柱能不能授衔、软件标的黄金柱准不准、王牌柱怎么排序”等信号；不适用于没有图表数据的精确授衔或真实买卖建议。Triggers: golden column, general column, trump column, column ranking.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第1册黄金柱；第2-3册王牌授衔；第9册卧底王牌
tags: [golden-column, trump-card, signal-ranking]
related_skills:
  - slug: volume-line-balance-reading
    relation: depends-on
  - slug: key-line-anchoring
    relation: composes-with
  - slug: concave-bottom-notch-gold
    relation: composes-with
---

# 黄金柱/将军柱/王牌授衔

## R — 原文 (Reading)

> "评价一个黄金柱建构的质量有两个要点：一看基柱，二看价涨量缩。"
>
> — 黑马王子，第2册黄金柱讲解

## I — 方法论骨架 (Interpretation)

作者把关键量柱当作后续行情的战术角色，而不是只看柱子高低。
基柱要体现主力做多或控盘意愿，后三日要看价量是否配合，位置要能支撑后势。
将军柱、黄金柱、元帅柱、王牌柱的区别，在于它们能否独当一面、扭转结构、继往开来。
授衔之后，这些柱位会成为后续画线、守线、凹底淘金和过峰接力的依据。
如果只是软件自动标注、形似但没有行为确认，不能直接授衔。

## A1 — 书中的应用 (Past Application)

### 案例 1: 中卫国脉黄金柱四连板
- **问题**: 如何判断凹口/黄金线机会。
- **方法论的使用**: 作者用长阴短柱群、百日低量群、倍量黄金柱和价升量缩组合授衔。
- **结论**: 黄金柱不是单根柱，而是后续控盘质量。
- **结果**: 书中记录预报后连续四个涨停。

### 案例 2: 软件误标黄金柱
- **问题**: 软件标出多个黄金柱/将军柱。
- **方法论的使用**: 作者逐一检查位置、量价和遗漏，指出多处错标。
- **结论**: 公式标注不能替代人工辨别。
- **结果**: 该场景进入反例池。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户想判断某根量柱是否能作为关键柱。
2. 用户被软件公式或自动标注误导。
3. 用户需要为凹底、凹口、康桥或关键线寻找柱位根基。
4. 用户想比较多个关键柱谁更有支撑意义。

### 语言信号

- "这是不是黄金柱/将军柱"
- "软件标的王牌柱可信吗"
- "哪个柱才是基柱"
- "golden column / general column / trump column / rank signal"

### 与相邻 skill 的区分

- 与 `volume-line-balance-reading` 的区别: 本 skill 专门给关键量柱授衔。
- 与 `key-line-anchoring` 的区别: 本 skill 判断柱的质量；后者用柱或价位去生线。
- 与 `concave-bottom-notch-gold` 的区别: 本 skill 是柱级判断；后者是底部/凹口机会组合。

## E — 可执行步骤 (Execution)

1. **识别候选基柱**
   - 标出放量、倍量、缩量、长阴短柱、低量群中的关键柱。
   - 完成标准: 至少说明候选柱的位置和量价特征。

2. **检查后续确认**
   - 看后三日是否价涨量缩、是否不破关键底、是否能支撑后势。
   - 完成标准: 给出“可授衔/降级观察/不授衔”。

3. **赋予战术角色**
   - 判断它能否作为支撑线、攻防线、凹底/康桥/回马枪的根。
   - 完成标准: 输出角色用途和不能用的边界。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 没有图表或量价数据，却要求精确授衔。
- 用户只想知道术语定义。
- 用户想直接根据某个柱获得买卖建议。

### 作者在书中警告的失败模式

- 迷信量柱软件和公式标注。
- 只看柱高，不看位置和后续确认。
- 生搬硬套多种战法。

### 作者的盲点 / 时代局限

- 授衔规则有人工判断空间，需要图表复核。
- 书中成功案例多，不能替代完整回测。

### 容易混淆的邻近方法论

- `concave-bottom-notch-gold`: 机会筛选。
- `peak-hold-kangqiao`: 突破后接力。
- `key-line-anchoring`: 柱位转线位。

## 相关 skills

- depends-on `volume-line-balance-reading`: 先读量价，再给柱授衔。
- composes-with `key-line-anchoring`: 授衔后的柱位可生根成线。
- composes-with `concave-bottom-notch-gold`: 卧底王牌是凹底淘金的重要证据。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
