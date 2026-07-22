---
name: long-yin-short-volume
description: |
  用户看到大阴线、急跌或超跌，但量柱明显缩小，需要判断是真跌、假跌、洗盘、诱空还是等待次阳确认时使用。适用于“长阴短柱怎么看、缩量大跌能不能算假跌、极阴次阳是否确认”等信号；不适用于无量价数据的猜底或真实买卖建议。Triggers: long yin short volume, shrink volume drop, extreme yin next yang.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第1册长阴短柱；第3册极阴次阳；第9册回马枪案例
tags: [volume-price-divergence, false-drop, extreme-yin]
related_skills:
  - slug: true-false-yin-yang
    relation: composes-with
  - slug: left-proof-right-confirmation
    relation: composes-with
  - slug: concave-bottom-notch-gold
    relation: composes-with
---

# 长阴短柱与极阴次阳

## R — 原文 (Reading)

> "所谓长阴短柱，就是长长的阴价柱对应着短短的小量柱。"
>
> — 黑马王子，第1册《长阴短柱再展雄风》

## I — 方法论骨架 (Interpretation)

长阴短柱把“跌得狠”和“卖得真不真”拆开看。
如果价格大跌但量柱短，作者认为可能不是主力真实出货，而是洗盘、诱空或借势打压。
但长阴短柱不能直接等于买点，它只能提出“假跌可能”。
后续必须看是否踩住关键线、是否出现次阳过阴半、缩量确认或右侧反攻。
极阴次阳则是急跌后的修复质量测试，用次日阳线的位置和量价结构确认反弹是否成立。

## A1 — 书中的应用 (Past Application)

### 案例 1: 新潮实业长阴短柱涨停基因
- **问题**: 大盘低迷时，如何看大阴后的机会。
- **方法论的使用**: 作者用长阴短柱、回踩精准线、阻力位组合判断。
- **结论**: 大阴不必然是真弱，量缩和踩线可能隐藏机会。
- **结果**: 书中记录新潮实业午后封死涨停。

### 案例 2: 2017-06-05 极阴回马枪
- **问题**: 急跌后的反弹是否有批量机会。
- **方法论的使用**: 作者用极阴回马枪和次阳确认观察中小盘反弹。
- **结论**: 极阴后需要右侧量价确认。
- **结果**: 书中记录大量极阴回马枪形态涨停，同时复盘误差。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户看到大阴下跌但成交量缩小。
2. 用户想判断超跌后是风险延续还是假跌机会。
3. 用户需要筛选凹底、回马枪、极阴次阳候选。
4. 用户把跌幅大误认为一定弱，或把缩量误认为一定安全。

### 语言信号

- "长阴短柱是不是假跌"
- "大跌缩量怎么看"
- "极阴次阳确认了吗"
- "long yin short volume / shrink volume drop / extreme-yin reversal"

### 与相邻 skill 的区分

- 与 `true-false-yin-yang` 的区别: 本 skill 专门处理价跌量缩和极阴次阳；真假阴阳更宽。
- 与 `concave-bottom-notch-gold` 的区别: 本 skill 是单个结构证据；后者要求多证据组合。
- 与 `huimaqiang-three-step` 的区别: 本 skill 判断急跌性质；后者判断趋势回马机会。

## E — 可执行步骤 (Execution)

1. **确认背离**
   - 判断是否为“长阴价柱 + 短量柱/缩量”。
   - 完成标准: 说明价跌幅度与量柱变化是否背离。

2. **检查位置**
   - 看是否踩关键线、低量群、谷底线、黄金线或前期实顶实底。
   - 完成标准: 至少有一个位置证据，否则仅观察。

3. **等待次阳确认**
   - 看次日是否过阴半、盖阴、缩量上攻或量波转强。
   - 完成标准: 输出“假跌候选/确认不足/风险延续”。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 只有价格下跌，没有成交量数据。
- 放量长阴或连续破位，不应硬解释为假跌。
- 用户要求直接抄底。

### 作者在书中警告的失败模式

- 不等确认就抄底。
- 把第一次翘头当反转。
- 一招鲜式套用长阴短柱。

### 作者的盲点 / 时代局限

- 缩量可能来自流动性枯竭，不一定代表主力控盘。
- 需要结合市场阶段和图表证据。

### 容易混淆的邻近方法论

- `true-false-yin-yang`: 阴阳真假。
- `left-proof-right-confirmation`: 确认门禁。
- `concave-bottom-notch-gold`: 组合选股。

## 相关 skills

- composes-with `true-false-yin-yang`: 长阴短柱常是假阴/假跌候选。
- composes-with `left-proof-right-confirmation`: 大跌缩量后必须等右确认。
- composes-with `concave-bottom-notch-gold`: 长阴短柱可作为凹底淘金证据之一。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
