---
name: true-false-yin-yang
description: |
  用户需要判断一根阳线/阴线表面颜色是否可靠，识别假阴真阳、假阳真阴、阴阳胜负和右侧确认时使用。适用于“这根阳线是假阳吗、收阴是不是弱、低开高走能不能看强”等信号；不适用于没有 K 线/量价上下文的术语查询或真实买卖建议。Triggers: fake yin real yang, fake yang real yin, candle truth, yin-yang confirmation.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第3册假阴真阳/假阳真阴；第9册0413误判致歉
tags: [yin-yang, truth-detection, candle-reading]
related_skills:
  - slug: volume-line-balance-reading
    relation: depends-on
  - slug: left-proof-right-confirmation
    relation: composes-with
  - slug: double-yin-lagua-exit
    relation: composes-with
---

# 真假阴阳辨别与右确认

## R — 原文 (Reading)

> "有些量柱看起来是阴的，实质上是阳的；这种似阴实阳、似阳实阴的量柱称为阴阳柱。"
>
> — 黑马王子，第3册《伏击涨停的两个基础》

## I — 方法论骨架 (Interpretation)

K 线颜色只是表象，真实强弱要看量价结构和位置。
假阴真阳可能是主力洗盘、控盘或含蓄上攻；假阳真阴可能是反弹中继、诱多或风险警报。
判断时要看开收位置、是否过阴半/二一位、人线天线关系、量柱缩放、关键线和次日确认。
这套方法的核心，是不被红绿颜色牵着走，而是问“这根柱在攻防结构里到底站在哪边”。
没有右确认时，只能列为假设，不能直接升级为行动。

## A1 — 书中的应用 (Past Application)

### 案例 1: 2013 年 2 月假阴真阳趋势
- **问题**: 哪些涨停股具有假阴真阳基因。
- **方法论的使用**: 作者把假阴真阳和其他涨停基因组合观察。
- **结论**: 假阴真阳不是单独信号，要与位置和基因密集度结合。
- **结果**: 书中记录相关股票在涨停榜中连续出现。

### 案例 2: 2017-04-13 隐形假阳真阴致歉
- **问题**: 作者漏判大盘隐形假阳真阴。
- **方法论的使用**: 学员指出人线低于地线、价柱未过左阴实体二一位。
- **结论**: 表面阳线并不等于强。
- **结果**: 次日行情验证风险，作者公开致歉。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户看到阳线但怀疑是假强。
2. 用户看到阴线但怀疑是假弱或洗盘。
3. 用户要判断反弹是否只是下跌中继。
4. 用户需要把真假阴阳接入出货、防守或机会筛选。

### 语言信号

- "这是假阳真阴吗"
- "收阴但好像不弱"
- "低开高走是不是强"
- "fake yang real yin / fake yin real yang / candle truth"

### 与相邻 skill 的区分

- 与 `long-yin-short-volume` 的区别: 本 skill 看阴阳真假；后者专门看长阴配短量的假跌结构。
- 与 `left-proof-right-confirmation` 的区别: 本 skill 提出真假假设；后者判断是否确认。
- 与 `double-yin-lagua-exit` 的区别: 本 skill 识别风险性质；后者执行防守退出流程。

## E — 可执行步骤 (Execution)

1. **先剥离颜色**
   - 不按红/绿或阴/阳直接判断强弱，先记录开收高低和量柱。
   - 完成标准: 输出“表面颜色”和“可能真实性质”。

2. **检查结构位置**
   - 看是否过左阴二一位/阴半、是否站上关键线、人线天线是否支持。
   - 完成标准: 至少给出 2 个结构证据。

3. **等待或确认**
   - 未确认则转 `left-proof-right-confirmation`；若风险确认则转 `double-yin-lagua-exit`。
   - 完成标准: 输出“假设/确认/反证”三类结论之一。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 没有 K 线、量柱、线位或后续走势信息。
- 用户只问某个术语定义。
- 用户要求真实买卖点。

### 作者在书中警告的失败模式

- 把收阳当转强，漏判假阳真阴。
- 下降途中的假阳真阴被误作反弹。
- 一两次成功后以为一招鲜吃遍天。

### 作者的盲点 / 时代局限

- 阴阳真假高度依赖图表细节和市场制度。
- 单根 K 线不能独立证明长期趋势。

### 容易混淆的邻近方法论

- `long-yin-short-volume`: 量价背离。
- `left-proof-right-confirmation`: 右确认。
- `double-yin-lagua-exit`: 风险落地动作。

## 相关 skills

- depends-on `volume-line-balance-reading`: 真假阴阳必须回到量价动态平衡。
- composes-with `left-proof-right-confirmation`: 真假假设必须等右侧确认。
- composes-with `double-yin-lagua-exit`: 假阳真阴确认后常转入防守。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
