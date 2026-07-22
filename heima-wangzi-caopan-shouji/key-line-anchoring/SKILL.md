---
name: key-line-anchoring
description: |
  用户需要判断灯塔线、平衡线、太极线、精准线、谷底线等关键线是否有根、能不能作为攻防边界时使用。适用于“这条线怎么画、取点是否自然、破线怎么办、线位是否有效”等信号；不适用于缺图却要求精确点位或真实买卖建议。Triggers: key line, anchor point, balance line, precise line, line validation.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第1册平衡线取点答疑；第2册量线生根；第9册太极线案例
tags: [key-line, anchor, attack-defense]
related_skills:
  - slug: volume-line-balance-reading
    relation: depends-on
  - slug: premarket-three-lines
    relation: composes-with
  - slug: two-dragon-positioning
    relation: composes-with
---

# 关键线生根与攻防

## R — 原文 (Reading)

> "平衡线的取点必须遵循天然法则，要求取点自然而然，不要人工雕饰。"
>
> — 黑马王子，第1册平衡线取点答疑

## I — 方法论骨架 (Interpretation)

作者的线不是为了让图好看，而是为了找到市场已经留下的攻防边界。
一条线要能使用，必须有根：关键量柱、实顶实底、极点、焦点、拐点或被后续走势验证的位置。
上行找实顶，下行找实底；没有实点再找密点；取点标准要先于结论。
线的作用是把复杂走势压缩成攻、防、破位、确认四类动作。
如果线是为了配合观点临时移动出来的，它就不能作为决策依据。

## A1 — 书中的应用 (Past Application)

### 案例 1: 2010-07-23 平衡线移植
- **问题**: 如何把日线平衡线用于分时预报。
- **方法论的使用**: 作者用自然平衡点和人工修正设定 2550、2578 等边界。
- **结论**: 线位用于构造当天上下预案。
- **结果**: 书中记录当天高低点与预报相差 1 点。

### 案例 2: 8 月 27 日灯塔线误差复盘
- **问题**: 盘前最低点预报与实际差 3 点。
- **方法论的使用**: 作者没有放过误差，而是回看灯塔线、通道和浮线。
- **结论**: 线的误差也能反推支撑和修正值。
- **结果**: 误差被转化为后续复盘材料。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户需要判断某条线是否能作为支撑、阻力、攻防线。
2. 用户在多个可能取点之间犹豫。
3. 用户怀疑自己画线是在事后贴合。
4. 用户需要把关键线转化成盘前三线或二龙定位。

### 语言信号

- "这条线该怎么取点"
- "是不是人工雕饰"
- "破了这条线意味着什么"
- "anchor point / balance line / precise line / line validation"

### 与相邻 skill 的区分

- 与 `premarket-three-lines` 的区别: 本 skill 先验证线是否有根；后者把线组织成当天上中下预案。
- 与 `two-dragon-positioning` 的区别: 本 skill 处理单条或一组关键线；后者专门处理横线与斜线交叉变盘。
- 与 `volume-line-balance-reading` 的区别: 本 skill 是线位专项，不做整体读盘总判断。

## E — 可执行步骤 (Execution)

1. **找根**
   - 标出线的来源：量柱、价柱、实顶、实底、虚顶、虚底、极点、焦点、拐点。
   - 完成标准: 每条线都能说清“从哪里来”。

2. **查自然性**
   - 检查是否为了贴合结论反复移动取点；同类场景标准是否一致。
   - 完成标准: 能说明取点规则，而不是只说“看起来像”。

3. **定攻防动作**
   - 把线位转成触线、咬线、破线、站上线后的观察动作。
   - 完成标准: 输出条件化预案，不输出直接买卖指令。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 没有图表、行情数据，却要求精确点位。
- 用户只需要读术语，不需要建立线位。
- 用户要求用线位直接给出买卖建议。

### 作者在书中警告的失败模式

- 画线取点人工雕饰。
- 图片缩放造成看线误判。
- 软件公式标注错漏关键量柱。

### 作者的盲点 / 时代局限

- 很多线位判断依赖图形和坐标，OCR 文本不能完整保留。
- 线位的可复现性需要独立行情数据检验。

### 容易混淆的邻近方法论

- `premarket-three-lines`: 三线预案。
- `two-dragon-positioning`: 平斜交叉。
- `peak-hold-kangqiao`: 突破后的保顶/康桥线。

## 相关 skills

- depends-on `volume-line-balance-reading`: 线位必须服务量价平衡判断。
- composes-with `premarket-three-lines`: 经过验证的关键线可进入三线预案。
- composes-with `two-dragon-positioning`: 横线和斜线交叉需要先各自有根。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
