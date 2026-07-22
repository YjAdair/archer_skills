---
name: huimaqiang-three-step
description: |
  用户需要判断强势趋势或超跌反弹中的“回马枪”是否成立，避免把普通下跌误作回踩机会时使用。适用于“连续下杀第三天回升、回踩后能不能反攻、这是回马枪还是反转失败”等信号；不适用于无趋势背景的抄底或真实买卖建议。Triggers: huimaqiang, pullback attack, third-day rebound, reversal setup.
source_book: 《黑马王子操盘手记系列》 黑马王子
source_chapter: 第1册《看准大方向，破解回马枪》；第9册0524/0605回马枪实盘
tags: [huimaqiang, pullback, confirmation]
related_skills:
  - slug: left-proof-right-confirmation
    relation: depends-on
  - slug: long-yin-short-volume
    relation: composes-with
  - slug: concave-bottom-notch-gold
    relation: contrasts-with
---

# 回马枪三步破解

## R — 原文 (Reading)

> "破解回马枪，第一要趋势不变；第二要预测它最多在什么位置回马；第三要随时盯住回马的一瞬间。"
>
> — 黑马王子，第1册《看准大方向，破解回马枪》

## I — 方法论骨架 (Interpretation)

回马枪不是普通回调买入，而是趋势中的反杀和再攻击。
第一步先确认大方向没有坏，避免把下跌延续误判为回马。
第二步测算回踩极限，看它最多回到哪条关键线、黄金线或二一位附近。
第三步等回马瞬间：量波、次阳、关键线站回或圆角波确认。
如果连续三天下杀不回升，或者关键线失守，就不能再按回马枪处理。

## A1 — 书中的应用 (Past Application)

### 案例 1: 2010 年开年五日
- **问题**: 利好后大盘局部下杀，如何避免误判。
- **方法论的使用**: 作者判断大势向好、局部可能回马，连续做盘前预报。
- **结论**: 大势和局部节奏要分开。
- **结果**: 书中称五天预报基本兑现，同时记录局部失误。

### 案例 2: 2017-05-24 回马枪批量涨停
- **问题**: 大盘下跌时出现一批回马枪候选。
- **方法论的使用**: 作者围绕 3036、3050 和圆角波确认，实时点评回马枪票。
- **结论**: 回马枪要在关键位和量波确认中触发。
- **结果**: 当日出现多只回马枪涨停。

## A2 — 触发场景 (Future Trigger)

### 用户会在什么情境下需要这个 skill?

1. 用户看到连续一两天下杀后第三天回升。
2. 用户想区分回调机会和趋势破坏。
3. 用户已经用长阴短柱、极阴次阳筛出候选，需要判断是否能反攻。
4. 用户想做历史案例复盘中的回马枪训练。

### 语言信号

- "这是不是回马枪"
- "连续两天下杀第三天拉起"
- "回踩到哪里算正常"
- "huimaqiang / pullback attack / third-day rebound"

### 与相邻 skill 的区分

- 与 `long-yin-short-volume` 的区别: 长阴短柱判断下跌真假；回马枪判断趋势中反杀机会。
- 与 `concave-bottom-notch-gold` 的区别: 回马枪偏趋势回踩；凹底/凹口偏底部或突破后的组合筛选。
- 与 `left-proof-right-confirmation` 的区别: 回马枪包含确认步骤，但还需要趋势和回踩极限。

## E — 可执行步骤 (Execution)

1. **确认大方向**
   - 检查趋势、关键线和前置量价结构是否仍支持回马而非反转失败。
   - 完成标准: 明确“大方向未坏/已坏/不确定”。

2. **测回踩极限**
   - 找出可能的支撑线、黄金线、二一位、谷底线。
   - 完成标准: 输出一个或多个条件边界，不给精确买点。

3. **等触发瞬间**
   - 看第三天回升、圆角波、次阳确认或站回关键线。
   - 完成标准: 输出“未触发/触发候选/失效”的判断。

## B — 边界 (Boundary)

### 不要在以下情况使用此 skill

- 没有原趋势，仅仅是下跌后想抄底。
- 连续三天下杀且关键线失守。
- 用户要求实盘买入卖出点。

### 作者在书中警告的失败模式

- 急躁追涨杀跌。
- 不等确认就抢反弹。
- 一招鲜吃遍天。

### 作者的盲点 / 时代局限

- 回马枪案例多来自涨跌停制度下的 A 股。
- 批量涨停验证不等于个体实盘收益稳定。

### 容易混淆的邻近方法论

- `concave-bottom-notch-gold`: 底部/凹口组合。
- `long-yin-short-volume`: 假跌识别。
- `left-proof-right-confirmation`: 确认门禁。

## 相关 skills

- depends-on `left-proof-right-confirmation`: 回马枪必须等待触发确认。
- composes-with `long-yin-short-volume`: 缩量下杀可成为回马枪候选证据。
- contrasts-with `concave-bottom-notch-gold`: 趋势回踩与底部淘金触发不同。

## 审计信息

- **验证通过**: V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**: 100%（主流程静态自测 fallback；详见 test-results.md）
- **蒸馏时间**: 2026-07-22
