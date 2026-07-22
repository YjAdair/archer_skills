# Stage 1.5 Verified Methodology Units

- project: heima-wangzi-caopan-shouji
- generated_at: 2026-07-22
- criteria: V1 跨域验证 + V2 预测力测试 + V3 独特性检验
- decision_summary: 17 个单元进入阶段 2；其余候选降级为案例、术语或边界。
- safety_note: 后续 skill 只用于读书训练、复盘辅助和方法论提取，不输出真实买卖建议，不替代投资顾问、账户风控或合规判断。

---

```yaml
- id: v01
  title: 四不得四不要风险纪律
  type: verified-skill-candidate
  merged_from: [p02, p03, p04, p05, ce01, ce02, ce03, ce04, ce05, ce06, ce07, ce10, ce11, ce18, ce19, ce20, g26]
  V1_cross_domain:
    passed: true
    evidence:
      - 第1册《炒股的金钥匙》: 代客理财、借钱炒股、收费荐股、不要迷信作者。
      - 第3册《黑马王子为师之道》: 四不得与训练门槛被正式写成教学纪律。
      - 第6-9册连续收评: 反复警告跟风、追高、心态乱、训练不足。
  V2_predictive_power:
    passed: true
    novel_question: "一个读者模拟盘刚抓到两个涨停，朋友想出钱让他代操，他该不该接？"
    derived_answer: "不能接。按该纪律，代客资金会把训练问题变成金钱压力和责任压力，优先破坏判断独立性；正确动作是继续模拟、复盘、写规则，不承诺收益。"
  V3_exclusivity:
    passed: true
    why_not_common: "常识只说控制风险；书中把代客、借钱、收费荐股、训练门槛、成绩下降和神化权威合成一套交易前置禁令。"
  stage2_decision: enter

- id: v02
  title: 时间窗口三步阅读法
  type: verified-skill-candidate
  merged_from: [f01, p01, ce06, ce18, ce20]
  V1_cross_domain:
    passed: true
    evidence:
      - 第1册导读: 要用发表日作为时间窗口，先自己预判，再看作者和后续行情。
      - 第6册方法提示: 读连续盘前/收评时必须回到当时，不许直接偷看答案。
      - 反例系统: 断章取义、跟风结论、生搬硬套都被归为失败根源。
  V2_predictive_power:
    passed: true
    novel_question: "如果拿到一篇 2017 年收评，怎样判断自己是在学习方法还是背结论？"
    derived_answer: "先遮住次日结果和作者最终建议，写出自己的三线、方向、触发条件和失效条件；再对照作者与真实走势，差距才是训练材料。"
  V3_exclusivity:
    passed: true
    why_not_common: "它不是普通读书笔记，而是把历史文本变成预测训练场，强制先下注自己的判断再看答案。"
  stage2_decision: enter

- id: v03
  title: 量柱量线动态平衡读盘框架
  type: verified-skill-candidate
  merged_from: [f02, p05, p06, ce12, ce13, ce14, ce16, g01, g02, g03, g04, g05]
  V1_cross_domain:
    passed: true
    evidence:
      - 第1册《股市量学 ABC》: 量柱、价柱、阴阳虚实的搭配决定后续走势。
      - 第3册《掌握量学，股市可测》: 量柱是基础，量线是灵魂，量波是抓手。
      - 第5册和第9册: 反复警告不要追消息、不要漂移标准，要回到量柱量线。
  V2_predictive_power:
    passed: true
    novel_question: "一只股票利好后高开，但量柱异常放大、价柱上攻无力，应该怎么读？"
    derived_answer: "不能只按利好看多，应回到量价阴阳真假：若价涨但量价关系失衡、上攻乏力或出现假阳真阴迹象，应先列为风险场景而非机会场景。"
  V3_exclusivity:
    passed: true
    why_not_common: "常识会看价格或消息；该框架把量柱、价柱、量线、量波和真假阴阳视为同一套行为证据系统。"
  stage2_decision: enter

- id: v04
  title: 关键线生根与攻防
  type: verified-skill-candidate
  merged_from: [f03, f05, p08, p09, p11, p12, ce15, ce17, g04, g06, g07, g08, g09]
  V1_cross_domain:
    passed: true
    evidence:
      - 第1册平衡线取点答疑: 上行找实顶，下行找实底，取点要天然，不要人工雕饰。
      - 第1册灯塔线与误差复盘: 用关键线解释大盘高低点和误差来源。
      - 第9册太极线/盘前三线: 反复用穴位、平衡点、精准线作为攻防边界。
  V2_predictive_power:
    passed: true
    novel_question: "如果两条线都能贴合历史走势，该用哪条做次日预案？"
    derived_answer: "优先选有明确生根证据的线：关键量柱/价柱、实顶实底、焦点拐点、被后续走势验证的线；纯视觉贴合降级为参考，不能当操作边界。"
  V3_exclusivity:
    passed: true
    why_not_common: "它不是普通支撑阻力线，而是要求线位必须从量柱价柱穴位生根，并能转化为攻、防、破位和复盘动作。"
  stage2_decision: enter
  boundary: "涉及具体图形取点时，必须回看页图或行情数据；OCR 文本不足以单独确认精确线位。"

- id: v05
  title: 盘前三线预案与失效条件
  type: verified-skill-candidate
  merged_from: [f04, p12, p16, p17, p18, p20, ce09, ce11, ce14, ce17, c11, c19, c22, g21]
  V1_cross_domain:
    passed: true
    evidence:
      - 第2-3册: 盘前三线被定义为上线、中线、下线，中线是行为中枢。
      - 第9册 0516-0524 连续收评: 围绕 3090、3071、3054 等线位滚动验证。
      - 反例系统: 被消息带偏三线、不等确认抄底、未设止损都导致预案失效。
  V2_predictive_power:
    passed: true
    novel_question: "盘前判断可能反弹，但开盘直接跌破下线，应该如何更新？"
    derived_answer: "下线失守说明原预案的反弹场景失效，应先切到防守/等待，而不是用盘前观点硬扛；只有重新站回中线或出现右侧确认，才重建计划。"
  V3_exclusivity:
    passed: true
    why_not_common: "它把预测拆成上中下三条行为边界，并规定盘中按中线中枢和失效条件执行，不是简单猜涨跌。"
  stage2_decision: enter

- id: v06
  title: 左证明右确认
  type: verified-skill-candidate
  merged_from: [p07, p15, p16, p20, ce08, ce09, f07, f09]
  V1_cross_domain:
    passed: true
    evidence:
      - 第3册《九阴真经逃命法宝》: 反弹迹象只是左证明，必须等右边走势确认。
      - 第4册假阴真阳: 真假阴阳判断要求左侧证据与右侧确认组合。
      - 第6-9册超跌反弹和回马枪场景: 多次要求二次探底、次阳过阴半或量波确认。
  V2_predictive_power:
    passed: true
    novel_question: "一个形态已经到达预设支撑，但只有第一次翘头，能否视为买入信号？"
    derived_answer: "不能。支撑和翘头只是左证明，必须等二次探底、次阳过阴半、有效反弹或量波确认，才从观察转为行动。"
  V3_exclusivity:
    passed: true
    why_not_common: "常识只说等确认；书中把左侧证据和右侧确认作为真假阴阳、回马枪、凹底、抄底和逃顶的统一门禁。"
  stage2_decision: enter

- id: v07
  title: 黄金柱/将军柱/王牌授衔
  type: verified-skill-candidate
  merged_from: [f06, c04, c10, c23, ce12, g10, g11, g12, g13]
  V1_cross_domain:
    passed: true
    evidence:
      - 第1册黄金柱/黄金线: 用中卫国脉解释倍量柱后确认与四连板。
      - 第2-3册王牌授衔: 讨论黄金柱、将军柱、元帅柱的质量、角色和后续支撑。
      - 第9册凹底淘金: 二级卧底王牌被用于批量筛选涨停趋势。
  V2_predictive_power:
    passed: true
    novel_question: "软件标了一个黄金柱，但后三天没有价涨量缩，能否直接作为支撑基准？"
    derived_answer: "不能。授衔要看基柱质量、后三日确认、位置和后续角色；软件形式命中但行为证据不足，应降级观察。"
  V3_exclusivity:
    passed: true
    why_not_common: "它不是一般‘放量阳线’，而是把关键量柱按战术角色授衔，并让授衔结果成为后续线位和战法的根。"
  stage2_decision: enter
  boundary: "具体授衔高度依赖图表和数据口径，阶段 2 必须写明回看图表/行情数据要求。"

- id: v08
  title: 真假阴阳辨别与右确认
  type: verified-skill-candidate
  merged_from: [f09, p13, p14, p15, c14, c15, c16, c17, ce13, ce19, g14, g15]
  V1_cross_domain:
    passed: true
    evidence:
      - 第3册假阴真阳/假阳真阴: 从基础概念、五要素和盘中警报展开。
      - 第4册假阴真阳批量涨停: 用化名预报验证战法组合。
      - 第9册 0413 误判致歉: 作者承认漏判隐形假阳真阴，并以失败修正规则。
  V2_predictive_power:
    passed: true
    novel_question: "一根阳线低开高走但未过左阴关键位置，是否能直接看作转强？"
    derived_answer: "不能。要检查它是真阳还是假阳：开收位置、阴半/二一位、人线天线关系、量波和次日确认都不足时，应按风险而非转强处理。"
  V3_exclusivity:
    passed: true
    why_not_common: "常识按红绿 K 线看强弱；该框架专门反转表面颜色，以量价结构和右确认判断真实阴阳。"
  stage2_decision: enter

- id: v09
  title: 长阴短柱与极阴次阳
  type: verified-skill-candidate
  merged_from: [f08, p13, p15, c03, c07, c10, c20, c21, ce09, g16, g17]
  V1_cross_domain:
    passed: true
    evidence:
      - 第1册长阴短柱案例: 新潮实业、金鹰股份等被用于解释假跌和精准线机会。
      - 第3册极阴次阳结构: 用次阳过半阴等方式判断急跌后的确认。
      - 第9册回马枪批量涨停: 极阴回马枪与次日确认反复出现。
  V2_predictive_power:
    passed: true
    novel_question: "一只股票大阴下跌但明显缩量，是否应立即按破位处理？"
    derived_answer: "不立即定性。先判是否长阴短柱，再看是否踩关键线、次日是否次阳过阴半；没有右确认时只能列入观察，不能提前重仓。"
  V3_exclusivity:
    passed: true
    why_not_common: "常识把长阴当弱；该框架把价跌与量缩背离作为识别假跌、洗盘和反弹确认的线索。"
  stage2_decision: enter

- id: v10
  title: 回马枪三步破解
  type: verified-skill-candidate
  merged_from: [f07, c02, c20, c21, ce08, ce09, g18]
  V1_cross_domain:
    passed: true
    evidence:
      - 第1册 2010 年开年五日: 用大势向好、局部回马和三日节奏破解大盘回马枪。
      - 第9册 0524 实盘: 围绕圆角波和关键点位确认回马枪批量涨停。
      - 第9册 0605 实盘: 极阴回马枪全面开花，同时复盘预测误差。
  V2_predictive_power:
    passed: true
    novel_question: "连续两天下杀后第三天盘中拉起，是否就是回马枪机会？"
    derived_answer: "还不能只凭三天形态下结论；要先确认大方向未坏，再测回踩极限位置，最后等量波/关键线触发。第三天下杀不回升则风险升级。"
  V3_exclusivity:
    passed: true
    why_not_common: "它不是普通回调买入，而是把趋势、极限位置和触发瞬间组合成一套反杀识别流程。"
  stage2_decision: enter

- id: v11
  title: 凹底/凹口淘金组合筛选
  type: verified-skill-candidate
  merged_from: [f10, c10, c19, c22, c23, ce08, ce09, g19, g20, g23, g24]
  V1_cross_domain:
    passed: true
    evidence:
      - 第1册中卫国脉: 凹口、黄金柱、长阴短柱群和百日低量群共同出现。
      - 第3册凹底淘金战法: 强调有主力卧底、有底、有线、有确认。
      - 第9册 0612-0615 连续收评: 凹底淘金和二级卧底王牌被用于批量验证。
  V2_predictive_power:
    passed: true
    novel_question: "一只股票超跌后横盘，是否可以按凹底淘金处理？"
    derived_answer: "不能只因超跌横盘就处理为机会；要检查是否有底部证据、低量群、关键线、王牌柱组合和右侧触发，没有两组以上证据时不进入。"
  V3_exclusivity:
    passed: true
    why_not_common: "常识说低位找反弹；该框架要求底部/凹口、卧底王牌、低量群、精准线和阶段触发共同成立。"
  stage2_decision: enter

- id: v12
  title: 双阴/大阴/拉拐出货防守
  type: verified-skill-candidate
  merged_from: [f11, p08, p09, p10, p13, p14, p17, p18, c01, c05, c06, c09, c13, c15, c24, ce05, ce10, ce11, g25]
  V1_cross_domain:
    passed: true
    evidence:
      - 第1册双阴出货: 对上证指数 13 个点位和白云山失误进行规则验证。
      - 第3册九阴真经: 阳胜进、阴胜出、跳空阴出干净构成急跌逃命逻辑。
      - 第9册拉拐替领: 用上线乏力、拉拐替领处理午后跳水。
  V2_predictive_power:
    passed: true
    novel_question: "如果一只股票突破上线失败，随后出现连续两根阴线，但卖出后可能反包，怎么办？"
    derived_answer: "按该防守框架，先出或减，不追求卖在最高点；保留再进入权比赌反包重要。若次日重新阳胜阴并有效过线，再按新证据重建动作。"
  V3_exclusivity:
    passed: true
    why_not_common: "常识说止损；该框架把双阴、大阴、跳空阴、上线乏力、拉拐替领和再进入权组合成防守流程。"
  stage2_decision: enter

- id: v13
  title: 失败案例三步复盘
  type: verified-skill-candidate
  merged_from: [f12, f16, c08, c12, c17, c18, c21, ce05, ce16, ce18, ce20]
  V1_cross_domain:
    passed: true
    evidence:
      - 第1册乐通股份: 作者复盘自己因心态不稳和视角不广痛失涨停。
      - 第1册 8月27日误差复盘: 从 3 点误差中继续追问灯塔线依据。
      - 第9册山东矿机与 0413 致歉: 用定位当时、放眼全局、抓住重点修正误判。
  V2_predictive_power:
    passed: true
    novel_question: "一个读者买入后亏 15%，复盘时应该先看今天走势还是回到买入当天？"
    derived_answer: "先定位当时，回到买入日向左分析买入依据；再放眼全局判断位置和阶段；最后抓关键证据，区分方法失效、执行错误还是情绪追入。"
  V3_exclusivity:
    passed: true
    why_not_common: "常识说复盘失败；该框架规定复盘顺序：定位当时、放眼全局、抓住重点，并要求正视错误而非事后找理由。"
  stage2_decision: enter

- id: v14
  title: 3121 时空节律与分级动作
  type: verified-skill-candidate
  merged_from: [f14, p19, g22, ce09, ce11]
  V1_cross_domain:
    passed: true
    evidence:
      - 第3册《九阴真经逃命法宝》: 跳空阴后用时间 3121 给一小时确认窗口，不能收上即跑。
      - 第5册《用顶部3121战法享受牛市盛宴》: 一个见顶标准减三一、两个再减二一、三个到齐全减。
      - 第9册 0413/0328/0612 等收评: 用阴柱二一位、缩量三一二一、量波 3121 判断真假阴阳、回踩和节奏。
  V2_predictive_power:
    passed: true
    novel_question: "跳空低开后盘中快速回拉，但一个小时内不能站回关键位，该怎么处理？"
    derived_answer: "按时间 3121 先给有限确认窗口；若窗口内不能回到关键线或阴柱二一位上方，按风险处理，不再把希望延长到全天。"
  V3_exclusivity:
    passed: true
    why_not_common: "常识只说分批减仓或等确认；3121 把时间、空间、量能和仓位动作压成书内特有的节律语言。"
  stage2_decision: enter
  boundary: "具体二一/三一位计算必须依赖可靠行情数据和图表，不凭 OCR 中的孤立数字下结论。"

- id: v15
  title: 平斜二龙定位
  type: verified-skill-candidate
  merged_from: [f13, g08, g23, ce15, ce17]
  V1_cross_domain:
    passed: true
    evidence:
      - 第3册《股市结构力学》: 平斜交叉以平为准，叉上看涨，叉下看跌。
      - 第4-5册连续收评: 多次用平斜交叉判断中到大阳/中到大阴和“该上不上必下”。
      - 第9册 0612-0630 收评: 用横龙、斜龙、二龙交叉判断变盘节点和过峰保顶。
  V2_predictive_power:
    passed: true
    novel_question: "两条趋势线交叉日临近，价格在交叉线下方但没有明显放量，如何设预案？"
    derived_answer: "先把交叉点当变盘节点，而不是直接看涨；以平线为准设上下方案，叉上才进入进攻预案，叉下或该上不上则切换防守。"
  V3_exclusivity:
    passed: true
    why_not_common: "它不是普通趋势线交叉，而是把横向平衡线与斜向太极线称为二龙，以交叉点决定变盘与攻防。"
  stage2_decision: enter
  boundary: "该 skill 高度依赖准确画线，缺图表时只能输出分析框架和需补证据清单。"

- id: v16
  title: 热点轮动与强者跟随
  type: verified-skill-candidate
  merged_from: [f15, p16, p21, p22, ce13, ce19]
  V1_cross_domain:
    passed: true
    evidence:
      - 第1册《看透主力手法，盯住市场热点》: 用资源、能源、金融、地产等板块轮动解释行情扩散。
      - 第3册《牛股是怎样选出来的》: 选股要看量柱、热点叠加和涨停趋势。
      - 第9册 0524-0630 收评: 大金融、大消费、大军工、雄安、环保、白马股轮动被纳入预案和股池替换。
  V2_predictive_power:
    passed: true
    novel_question: "题材股已经涨了一段，另一个板块刚有资金启动，是否该换过去？"
    derived_answer: "先把板块当作一只股票看，比较量柱建构、领涨龙头、持续性和主攻力量；若原板块上攻乏力且新板块有主力动作，再做调仓预案。"
  V3_exclusivity:
    passed: true
    why_not_common: "常识说追热点；书中要求把板块当作股票，用量柱量线和主力领衔判断强者，而不是追新闻热度。"
  stage2_decision: enter

- id: v17
  title: 过峰保顶与康桥接力
  type: verified-skill-candidate
  merged_from: [g23, g24, c22, c23, ce07, ce15]
  V1_cross_domain:
    passed: true
    evidence:
      - 第6册《燕归来康桥战法》: 过左侧高量实顶且价升量缩，形成燕归来康桥。
      - 第9册 0608-0619 连续收评: 过峰保顶第一天、第二天和保顶区间被反复设线跟踪。
      - 第9册 0614-0621 收评: 康桥、3S、凹底淘金和二级王牌在接力涨停潮中组合出现。
  V2_predictive_power:
    passed: true
    novel_question: "一只股票突破左峰后回踩，是继续看接力还是当假突破处理？"
    derived_answer: "先看是否守住峰顶/康桥线，再看价升量缩、王牌支撑和回踩不破；若保顶失败或攻击上线乏力，应从接力预案切到防守。"
  V3_exclusivity:
    passed: true
    why_not_common: "常识把突破视为买点；该框架强调突破后还要保顶、过桥、缩量和接力确认。"
  stage2_decision: enter
  boundary: "康桥与过峰保顶都依赖左峰实顶、高量实顶和回踩线位，需图表验证。"
```

## 下一步确认点

以上 17 个单元会进入阶段 2，被分别构造成可调用 skill。用户已要求“做完整，不要遗落”，据此进入阶段 2。
