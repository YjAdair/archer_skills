---
name: peak-hold-kangqiao
description: |
  用户需要判断突破左峰、高量实顶或康桥后是否能保顶、接力、继续持有观察，还是假突破转防守时使用。适用于“过峰保顶是否成功、燕归来康桥怎么看、突破后回踩能不能接力、康量过康桥”等信号；不适用于底部凹底筛选、无图表线位或真实买卖建议。Triggers: peak hold, kangqiao, bridge line, breakout hold, yan guilai.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第6册燕归来康桥；第9册过峰保顶/康桥接力
tags: [breakout, peak-hold, kangqiao]
related_skills:
  - slug: key-line-anchoring
    relation: depends-on
  - slug: trump-column-ranking
    relation: composes-with
  - slug: two-dragon-positioning
    relation: composes-with
---

# 过峰保顶与康桥接力

## R — 原文 (Reading)

> "过左侧最近的高量实顶，同时价升量缩，符合燕归来战法。"
>
> — 黑马王子，第6册《燕归来康桥战法》

## I — 方法论骨架 (Interpretation)

突破左峰不是结束，而是新的验证开始。
过峰之后，要看能否在左峰实顶、高量实顶、康桥线或关键平衡线附近守住。
康桥强调“过桥”后的量价质量：价升量缩、康量上攻、顶底互换、王牌支撑。
如果突破后回踩不破、缩量接力、关键柱支撑，就可能进入接力观察。
如果保顶失败、攻击上线乏力或关键线失守，就不能把突破当安全。

## A1 — 书中的应用 (Past Application)

### 案例 1: 燕归来康桥战法
- **问题**: 如何判断过高量实顶后的接力机会。
- **方法论的使用**: 作者用过左侧高量实顶、价升量缩、康量上攻识别康桥。
- **结论**: 过桥后仍要看控盘质量。
- **结果**: 第6册列出多只康桥案例作为预报样本。

### 案例 2: 2017-06 过峰保顶
- **问题**: 大盘突破后是否能守住峰顶。
- **方法论的使用**: 作者用 3164、3154、3112 等关键线连续跟踪保顶区间。
- **结论**: 过峰后要等待主力确认，不能急于重仓。
- **结果**: 后续凹底淘金、康桥、二级王牌接力被纳入预案。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户看到突破左峰或高量实顶，想判断是否有效。
2. 用户问康桥、燕归来、康量过康桥如何用。
3. 用户想判断突破后回踩是保顶还是失败。
4. 用户需要和凹底/凹口、二龙定位组合做接力判断。

### 语言信号

- "过峰保顶成功了吗"
- "康桥线怎么判断"
- "突破后回踩还能不能接力"
- "peak hold / kangqiao / breakout hold / yan guilai"

### 与相邻 skill 的区分

- 与 `concave-bottom-notch-gold` 的区别: 凹底/凹口偏低位或凹口筛选；本 skill 偏突破后保顶接力。
- 与 `key-line-anchoring` 的区别: 本 skill 使用左峰/康桥线判断接力；关键线 skill 验证线位来源。
- 与 `two-dragon-positioning` 的区别: 二龙定位看交叉变盘；本 skill 看突破后是否守住。

## E — 可执行步骤 (Execution)

1. **确认突破对象**
   - 标出左峰、高量实顶、康桥线或关键平衡线。
   - 完成标准: 说明突破的到底是哪一类峰/桥。

2. **检查保顶质量**
   - 看回踩是否不破、价升量缩、王牌支撑、康量过桥。
   - 完成标准: 给出“保顶候选/保顶失败/证据不足”。

3. **设接力与防守条件**
   - 写明继续观察、减仓防守、等待再确认的条件。
   - 完成标准: 输出条件化接力预案，不给买卖指令。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 还没有突破左峰或高量实顶。
- 没有图表，无法定位康桥线。
- 用户只因题材热就想追突破。

### 作者在书中警告的失败模式

- 跟风作者点评股票导致惊庄被套。
- 画线人工雕饰。
- 追高杀低，不等确认。

### 作者的盲点 / 时代局限

- 康桥和过峰保顶高度依赖图表、涨跌停生态和 A 股题材环境。
- 书中战法案例有教学选择偏差。

### 容易混淆的邻近方法论

- `concave-bottom-notch-gold`: 底部/凹口机会。
- `two-dragon-positioning`: 交叉变盘。
- `sector-rotation-strong-following`: 板块强者筛选。

## 相关 skills

- depends-on `key-line-anchoring`: 左峰和康桥线必须有根。
- composes-with `trump-column-ranking`: 王牌柱支撑提高保顶质量。
- composes-with `two-dragon-positioning`: 过峰保顶中常遇到二龙交叉节点。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
