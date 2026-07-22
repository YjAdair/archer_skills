---
name: double-yin-lagua-exit
description: |
  用户需要把盘面风险转成防守、减仓、出货或等待再进入流程时使用。适用于“双阴出货、跳空阴、攻击上线乏力、拉拐替领、阴胜阳、破线后怎么办”等信号；不适用于交易前风险伦理门禁、纯学习复盘或真实买卖指令。Triggers: double yin, gap down, lagua, exit defense, sell signal.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第1册双阴出货；第3册九阴真经；第9册拉拐替领
tags: [exit, defense, risk-control]
related_skills:
  - slug: premarket-three-lines
    relation: depends-on
  - slug: true-false-yin-yang
    relation: composes-with
  - slug: heima-risk-discipline
    relation: composes-with
---

# 双阴/大阴/拉拐出货防守

## R — 原文 (Reading)

> "攻击上线乏力的，果断出货，即使出错了也要出。只有出了才有机会进。"
>
> — 黑马王子，第9册《金融三胖突飙升，拉拐替领一身轻》

## I — 方法论骨架 (Interpretation)

作者把出货看作交易系统的一部分，不是失败后的补救。
双阴、大阴、跳空阴、阴胜阳、攻击上线乏力、拉拐不过位，都可能触发防守。
这套方法的目标不是卖在最高点，而是保存再行动权。
如果先出来，后续阳胜阴、重新站线、右确认成立，还可以重建计划。
如果不出来，被套住后再有机会也无法行动。

## A1 — 书中的应用 (Past Application)

### 案例 1: 上证指数双阴出货 13 点位
- **问题**: 如何检验双阴出货规则。
- **方法论的使用**: 作者把历史区间按同一标准标出双阴出货点。
- **结论**: 第二阴有效跌破第一阴收盘价时优先防守。
- **结果**: 书中统计 13 个出货点中大多数有效。

### 案例 2: 2017-06-22 拉拐替领
- **问题**: 午后跳水前如何保护收益。
- **方法论的使用**: 特训班学员用拉拐替领和三线出货处理盘中风险。
- **结论**: 上攻乏力时先退出或调仓，保留主动权。
- **结果**: 多名学员规避午后大跌。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户看到连续阴线、跳空阴、大阴破线。
2. 用户持有对象攻击上线乏力，不知道该守还是退。
3. 用户想区分减仓、清仓、等待再进入。
4. 用户需要给盘前三线补充失效后的防守动作。

### 语言信号

- "双阴出货了吗"
- "跳空阴怎么处理"
- "攻击上线乏力要不要出"
- "拉拐替领怎么用"
- "double yin / gap down / lagua / exit signal"

### 与相邻 skill 的区分

- 与 `heima-risk-discipline` 的区别: 风险纪律是交易前门禁；本 skill 是盘面风险触发后的动作。
- 与 `premarket-three-lines` 的区别: 三线设预案；本 skill 处理破线、乏力、双阴后的防守。
- 与 `true-false-yin-yang` 的区别: 真假阴阳识别风险；本 skill 执行防守流程。

## E — 可执行步骤 (Execution)

1. **识别防守信号**
   - 查双阴、大阴、跳空阴、阴胜阳、破线、上线乏力、拉拐不过位。
   - 完成标准: 标出具体触发信号和对应线位。

2. **选择防守等级**
   - 根据信号强度输出观察、减仓、清仓、等待再进入四类动作。
   - 完成标准: 用条件化描述，不给真实交易指令。

3. **保留再进入条件**
   - 写明阳胜阴、站回关键线、右确认成立后如何重建预案。
   - 完成标准: 防守后有“再判断入口”，不是情绪化离场。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 用户没有持仓或风险触发，只是在交易前问能不能做，应先用 `heima-risk-discipline`。
- 用户只是想复盘为什么错了，应转 `failure-case-review`。
- 用户要求你替他下卖出指令。

### 作者在书中警告的失败模式

- 实盘成绩下降仍继续操作。
- 情绪冲动时下单或不设止损。
- 看到跳空阴仍感情用事。

### 作者的盲点 / 时代局限

- 出货规则来自历史 A 股样本，不能保证当前市场表现。
- 具体拉拐点依赖分时图和量波数据。

### 容易混淆的邻近方法论

- `heima-risk-discipline`: 风险底线。
- `premarket-three-lines`: 预案边界。
- `failure-case-review`: 事后审计。

## 相关 skills

- depends-on `premarket-three-lines`: 出货动作常依赖上线/中线/下线。
- composes-with `true-false-yin-yang`: 假阳真阴可触发防守。
- composes-with `heima-risk-discipline`: 连续亏损或情绪乱时升级为纪律门禁。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
