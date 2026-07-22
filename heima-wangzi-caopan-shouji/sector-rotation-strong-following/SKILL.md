---
name: sector-rotation-strong-following
description: |
  用户需要按量学思路判断市场热点、板块轮动、龙头/强者、权重领衔和股池替换时使用。适用于“哪个板块是真强者、要不要跟热点、白马30/雄安20怎么替换、大金融是否领衔”等信号；不适用于追新闻热度、荐股或真实买卖建议。Triggers: sector rotation, strong leader, hot theme, leading sector, stock pool.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第1册《看透主力手法，盯住市场热点》；第9册白马/雄安/大金融轮动
tags: [sector-rotation, leadership, stock-pool]
related_skills:
  - slug: volume-line-balance-reading
    relation: depends-on
  - slug: premarket-three-lines
    relation: composes-with
  - slug: peak-hold-kangqiao
    relation: composes-with
---

# 热点轮动与强者跟随

## R — 原文 (Reading)

> "任何一个板块都可以当作一只股票来看。"
>
> — 黑马王子，第3册《股海明灯，照亮乾坤》

## I — 方法论骨架 (Interpretation)

作者不是让读者追新闻热点，而是把板块当作一只整体股票来读。
板块也有量柱、价柱、强弱、领衔者、接力者和失效边界。
真正的强者不是“大家都在谈”，而是有资金动作、量价结构、龙头示范和持续轮动。
当原热点上攻乏力，新热点有量学证据时，可以准备调仓或替换股池。
当关键阻力位前缺少大金融、大建设等主攻力量时，不宜简单放大乐观预期。

## A1 — 书中的应用 (Past Application)

### 案例 1: 银行板块四小龙
- **问题**: 大盘双向阴胜后，作者为何敢预报银行领衔大涨。
- **方法论的使用**: 把银行板块当作一只股票，看次阳过半阴与四小龙领衔。
- **结论**: 板块整体结构和龙头强度可用于判断主攻力量。
- **结果**: 书中记录四小龙带动银行板块反击。

### 案例 2: 白马30与雄安20替换
- **问题**: 雄安之后行情可能向白马转移。
- **方法论的使用**: 作者要求建立白马30、大消费、大金融、大军工等股池，并随趋势替换。
- **结论**: 股池要体现当前大趋势，不是固定名单。
- **结果**: 后续白马行情和大金融领衔被多次收评跟踪。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户想判断当前市场热点是真启动还是消息噪声。
2. 用户需要比较多个板块谁是强者、谁只是跟风。
3. 用户想建立或替换主题股池。
4. 用户问权重、大金融、大建设是否领衔冲关。

### 语言信号

- "哪个板块是真强者"
- "热点轮动怎么看"
- "要不要追这个题材"
- "sector rotation / leading sector / strong leader / stock pool"

### 与相邻 skill 的区分

- 与 `volume-line-balance-reading` 的区别: 本 skill 把板块当整体对象；读盘框架看基础量价。
- 与 `premarket-three-lines` 的区别: 本 skill 判断主攻力量和股池；三线管理当日指数/个股边界。
- 与 `peak-hold-kangqiao` 的区别: 强者筛选可进入过峰/康桥接力，但不是同一个问题。

## E — 可执行步骤 (Execution)

1. **把板块当股票读**
   - 观察板块量价、龙头、涨停梯队、领衔权重和持续性。
   - 完成标准: 不用新闻热度替代量价证据。

2. **比较强弱和轮动阶段**
   - 判断当前是主升、接力、补涨、退潮还是切换。
   - 完成标准: 输出板块相对强弱排序和证据。

3. **生成股池/观察池规则**
   - 建立候选池标准，如量柱健康、价柱登台阶、康量过康桥。
   - 完成标准: 输出筛选条件，不输出具体荐股。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 用户只是追新闻或问某题材会不会爆。
- 用户要求推荐具体股票。
- 没有板块、量价或龙头数据。

### 作者在书中警告的失败模式

- 追消息股而不看形态。
- 盲目跟风追高杀低。
- 一两次成功后以为一招鲜吃遍天。

### 作者的盲点 / 时代局限

- 热点轮动与 A 股题材生态强相关，跨市场不能直接套。
- 公开点评可能引发跟风和惊庄风险。

### 容易混淆的邻近方法论

- `volume-line-balance-reading`: 基础读盘。
- `peak-hold-kangqiao`: 具体突破接力。
- `heima-risk-discipline`: 防止荐股和跟风。

## 相关 skills

- depends-on `volume-line-balance-reading`: 板块也要按量价读。
- composes-with `premarket-three-lines`: 板块领衔影响指数三线预案。
- composes-with `peak-hold-kangqiao`: 强者突破后可用康桥/保顶验证。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
