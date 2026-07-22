---
name: concave-bottom-notch-gold
description: |
  用户需要从超跌、底部、凹口、缩量、卧底王牌等条件中筛选“凹底淘金/凹口淘金”机会时使用。适用于“超跌后能不能淘金、凹底/凹口是否成立、需要几组王牌证据”等信号；不适用于单纯低位抄底、无图表数据或真实买卖建议。Triggers: concave bottom, notch gold, bottom setup, aodi, aokou.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第1册凹口淘金；第3册凹底淘金；第9册0612-0615连续收评
tags: [bottom-setup, notch, composite-signal]
related_skills:
  - slug: trump-column-ranking
    relation: depends-on
  - slug: long-yin-short-volume
    relation: composes-with
  - slug: huimaqiang-three-step
    relation: contrasts-with
---

# 凹底/凹口淘金组合筛选

## R — 原文 (Reading)

> "值得淘金的凹底是有主力卧底的凹底。"
>
> — 黑马王子，第3册《凹底淘金战法》

## I — 方法论骨架 (Interpretation)

凹底淘金不是“跌得多就买”，凹口淘金也不是“形状像凹就买”。
作者要求底部或凹口里有主力卧底证据：长阴短柱、百日低量群、精准谷底线、卧底王牌、二级黄金梯等。
单一超跌不够，最好至少有两组以上关键证据形成组合。
凹底偏底部发现，凹口偏突破或接力位置。
真正的动作要等右侧确认和关键线触发，不能用“低位”替代“有底”。

## A1 — 书中的应用 (Past Application)

### 案例 1: 中卫国脉凹口淘金
- **问题**: 如何从凹口中发现黄金柱接力。
- **方法论的使用**: 作者用长阴短柱群、百日低量群、倍量黄金柱和价升量缩组合判断。
- **结论**: 凹口需要有柱、有线、有接力。
- **结果**: 书中记录预报后连续四个涨停。

### 案例 2: 2017-06-12 至 0614 涨停潮
- **问题**: 过峰保顶期间如何筛选个股机会。
- **方法论的使用**: 作者用超跌有底、二级黄金梯、卧底王牌组合筛选。
- **结论**: 凹底淘金要靠组合证据，不靠单一跌幅。
- **结果**: 书中记录特训班大量学员伏击涨停。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户看到超跌股、底部横盘、凹口结构，想筛选是否有机会。
2. 用户想判断“有底”还是只是下跌坑。
3. 用户需要把长阴短柱、王牌柱、关键线组合成机会筛选。
4. 用户想复盘凹底/凹口案例而不是追涨。

### 语言信号

- "这是不是凹底淘金"
- "凹口能不能接力"
- "超跌有底怎么判断"
- "concave bottom / notch gold / bottom setup / aodi / aokou"

### 与相邻 skill 的区分

- 与 `huimaqiang-three-step` 的区别: 本 skill 偏底部/凹口组合；回马枪偏趋势回踩反杀。
- 与 `trump-column-ranking` 的区别: 本 skill 用王牌柱组合筛机会；授衔 skill 判断柱本身。
- 与 `peak-hold-kangqiao` 的区别: 本 skill 偏低位或凹口；后者偏突破左峰后的保顶接力。

## E — 可执行步骤 (Execution)

1. **判底或凹口**
   - 标出凹底、凹口、左峰、谷底线或关键凹间峰。
   - 完成标准: 能说明当前属于底部凹陷、凹口接力或不属于。

2. **收集组合证据**
   - 检查长阴短柱、低量群、卧底王牌、黄金梯、精准线、缩量二一/三一。
   - 完成标准: 至少两组独立证据才进入候选。

3. **等待触发和失效**
   - 写明过线、踩线、次阳确认、跌破底线等条件。
   - 完成标准: 输出“候选/等待/淘汰”而非直接买入建议。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 只有跌幅，没有底部结构和量价证据。
- 无图表但要求具体凹口线位。
- 用户想把所有低位股都当机会。

### 作者在书中警告的失败模式

- 第一次翘头就抄底。
- 急躁追涨杀跌。
- 生搬硬套战法。

### 作者的盲点 / 时代局限

- 批量涨停案例不等于每个候选都可实盘盈利。
- 需要行情数据校验低量群、黄金梯和凹口线。

### 容易混淆的邻近方法论

- `huimaqiang-three-step`: 趋势回马。
- `peak-hold-kangqiao`: 突破后保顶。
- `trump-column-ranking`: 王牌柱质量。

## 相关 skills

- depends-on `trump-column-ranking`: 卧底王牌需要先授衔。
- composes-with `long-yin-short-volume`: 长阴短柱常是凹底证据。
- contrasts-with `huimaqiang-three-step`: 低位组合与趋势回踩不同。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
