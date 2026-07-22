---
name: left-proof-right-confirmation
description: |
  用户看到某个反弹、假阴真阳、回踩、抄底或回马枪迹象，但不确定是否已经能行动时使用。适用于“这是左证明还是右确认、第一次翘头能不能做、需要等什么确认”等信号；不适用于纯画线、纯术语解释或真实买卖建议。Triggers: confirmation, left proof, right confirmation, wait signal.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第3册《九阴真经逃命法宝》；第4册假阴真阳确认
tags: [confirmation, right-side, signal-gate]
related_skills:
  - slug: premarket-three-lines
    relation: composes-with
  - slug: true-false-yin-yang
    relation: composes-with
  - slug: huimaqiang-three-step
    relation: composes-with
---

# 左证明右确认

## R — 原文 (Reading)

> "别急，这时的迹象，不过是左证明而已，能不能有效反弹，必须等待右边走势的确认。"
>
> — 黑马王子，第3册《九阴真经逃命法宝》

## I — 方法论骨架 (Interpretation)

左侧证据只说明“可能”，右侧确认才说明“可以进入下一步”。
一个支撑、缩量、假阴、第一次翘头、极阴后的阳线，都可能只是左证明。
右确认要看后续走势是否站回关键线、过阴半、次阳过半阴、量波转强或三线条件成立。
这套方法把“看到机会”与“可以行动”分开，防止把观察信号误当操作信号。
它是抄底、回马枪、真假阴阳、凹底淘金的共同门禁。

## A1 — 书中的应用 (Past Application)

### 案例 1: 假阴真阳右确认
- **问题**: 看到假阴真阳迹象，是否可以直接乐观。
- **方法论的使用**: 作者要求按左证明、右确认原则，次日跳空向上才确认反弹成功。
- **结论**: 左侧结构不足以单独行动。
- **结果**: 后续真假阴阳案例都把右确认作为关键步骤。

### 案例 2: 超跌反弹等二次确认
- **问题**: 第一次翘头后读者容易抢入。
- **方法论的使用**: 作者建议等第二次探底回升或次阳过阴半。
- **结论**: 先备战，不急于参战。
- **结果**: 不等确认抄底被列为反例。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户看到某个形态像机会，但不知道是否已经确认。
2. 用户想区分“观察名单”和“可执行预案”。
3. 用户问是否可以抄底、追击、补仓、做回马枪。
4. 用户需要为其他战法增加确认门槛。

### 语言信号

- "这算确认了吗"
- "第一次反弹能不能做"
- "还只是左证明吗"
- "wait for confirmation / right-side confirmation / signal gate"

### 与相邻 skill 的区分

- 与 `premarket-three-lines` 的区别: 三线给边界；本 skill 判断触线后的信号是否确认。
- 与 `true-false-yin-yang` 的区别: 真假阴阳是具体对象；本 skill 是所有形态的确认门禁。
- 与 `huimaqiang-three-step` 的区别: 回马枪需要本 skill，但还要趋势和回踩极限。

## E — 可执行步骤 (Execution)

1. **标记左侧证据**
   - 列出当前支持机会的证据，如踩线、缩量、假阴、首次翘头。
   - 完成标准: 明确这些证据只能说明“可能”。

2. **定义右侧确认**
   - 为当前场景写出必须满足的确认条件。
   - 完成标准: 至少包含一条线位条件和一条量价/量波条件。

3. **输出等待或确认结论**
   - 若未确认，输出等待清单；若确认，转入对应战法的执行步骤。
   - 完成标准: 不把“看起来像”写成行动建议。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 用户没有任何左侧证据，只是在猜底猜顶。
- 用户要求具体买卖点或仓位。
- 用户需要先画线，此时先用 `key-line-anchoring`。

### 作者在书中警告的失败模式

- 第一次翘头就参与。
- 不见信号就挂弦。
- 追涨杀跌、急躁下单。

### 作者的盲点 / 时代局限

- 右确认也不能保证后续盈利，只能提高证据质量。
- 书中确认标准依赖 A 股日线/分时结构，跨市场需重建口径。

### 容易混淆的邻近方法论

- `true-false-yin-yang`: 判断 K 线真假。
- `huimaqiang-three-step`: 反杀机会。
- `concave-bottom-notch-gold`: 底部/凹口机会。

## 相关 skills

- composes-with `premarket-three-lines`: 三线触发后用确认门禁。
- composes-with `true-false-yin-yang`: 假阴假阳都需要右确认。
- composes-with `huimaqiang-three-step`: 回马枪第三步就是等待触发确认。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
