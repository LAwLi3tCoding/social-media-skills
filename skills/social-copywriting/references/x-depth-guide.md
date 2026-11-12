# 深度写作准则：X 引用/回复 + 小红书笔记

依据：2026-09-20 到 11-02 之间 X 上的 86 条真实帖子，都用 X 公开接口抓取，正文逐字摘录。研究底稿路径见用户的偏好层（如已安装的 `content-profile`）。
英文账号：karpathy、simonw、swyx、theo、thsottiaux、levelsio、HamelHusain、mitchellh、badlogicgames、jxnlco、eugeneyan。
中文账号：dotey、op7418、vista8、oran_ge，另有一些中文中小号作为正反对照。
反面样本来自 "harness / claude code / codex" 话题下赞数较高的搬运帖。

---

## 0. 一句话结论

深度不在长短，而在**这条内容带来了原帖没有的东西**。可以是一个机制、一个亲手测出来的数字、一个反例或适用边界、一个新的看问题角度，或者一个对方没想到的追问。
大V的回复中位数只有 20–220 个字符。它们短，但每条都带着一个新东西。

---

## 1. 深 vs 浅：大V回复和引用的 9 种"增量"

每条引用或回复只需要做到其中一种。

### 1.1 补机制（为什么会这样）
- karpathy 引用 Land/Water eval：`The models know. From compressing the internet.`
  https://x.com/karpathy/status/2105909609487872075
- karpathy 回复"LLM 是不是真的懂图像"：`Worth emphasizing that this all comes from just reading a ton of text and then predicting text.`
  https://x.com/karpathy/status/2105912048668590090
- mitchellh 讲一次性能优化：`if you basically do any single part of this optimization wrong (change order, change buffer size, change timing size) etc then it doesn't pay off!`
  https://x.com/mitchellh/status/2116313023623401881

### 1.2 换一个框（reframe）
- swyx：`having strong opinions on effort levels is like the tabs vs spaces of our time. just tweak to taste.`
  https://x.com/swyx/status/2116773135668404286
- karpathy：`I see it as a point on the LLM pareto optimal curve in a regime that had a large revealed latent demand … that was under-invested into because of a race to higher intelligence.`
  https://x.com/karpathy/status/2102124533729955960
- simonw 把一次产品改名放进行业趋势：`everyone's racing to establish themselves as a general agent now`
  https://x.com/simonw/status/2100311378171154492

### 1.3 亲手的数据点 / 真实做法
- levelsio：`I pay $100/mo for Claude but that's for ALL my sites, so I guess it cost like $0.10`
  https://x.com/levelsio/status/2116999699865772437
- simonw：`I don't let my agents have production access to modify deployed services (except on some dedicated test accounts)`
  https://x.com/simonw/status/2113650092242850065
- badlogicgames：`did i look at any code? no. magic button + tests + benchmarks + profiling does the work.`
  https://x.com/badlogicgames/status/2116653890401886702

### 1.4 把问题往前推一步（真正难的是哪里）
- simonw：`The bigger problem is /proving/ it - I'm not sure how to get to full confidence that a model or agent harness has solved it`
  https://x.com/simonw/status/2113484950460870846
- HamelHusain：`Yeah its when you run them yourself, and look at the data - you realize the bench isn't good`
  https://x.com/HamelHusain/status/2117061899355672782

### 1.5 用激励或逻辑反驳
- theo：`Why would they only remove 5h limit on $200 plan? Hitting the limit on cheaper plans is incentive to upgrade, on $200 plan it's literally just churn`
  https://x.com/theo/status/2117156099778564258
- theo：`What you've shown me is evidence that people want 5h limits gone so bad that they're falling for honeypots in order to get there.`
  https://x.com/theo/status/2117157842679673086
- mitchellh：`Most dependencies are "done" and you never have to touch them again. … But the number of real dependencies you need is tiny`
  https://x.com/mitchellh/status/2116366705215893548

### 1.6 一针见血的追问
- swyx：`ask yourself if any of the counterfactuals have been run on the charts you see`
  https://x.com/swyx/status/2116658902083441126
- HamelHusain：`would love to hear more detail behind that (i.e. what earned that trust, etc)?`
  https://x.com/HamelHusain/status/2115554957256704266
- simonw：`What's in your prompt?`
  https://x.com/simonw/status/2112549568395288756

### 1.7 给出带适用边界的立场
- swyx：`low effort + critique loop > superultramaxhighwhatever` 后面跟着 `(for the throughput-constrained; …)`
  https://x.com/swyx/status/2116642586387730593
- simonw：`cautiously starting to suspect it may not be a problem with today's strongest models … but it's still a real concern for cheaper, weaker models`
  https://x.com/simonw/status/2113484746999411051

### 1.8 预测（敢和主流相反）
- theo，回应"$200 无限 token 迟早没了"：`I have a feeling it will last way longer than people seem to think`
  https://x.com/theo/status/2117155146065195166
- HamelHusain：`Enough people haven't caught onto 4 yet, but they will.`
  https://x.com/HamelHusain/status/2116987667716223160

### 1.9 精确区分 / 命名一个现象
- jxnlco，引用"Opus 用代码复刻宣传片"：`Reciting a book and writing a book are different things.`
  https://x.com/jxnlco/status/2117215971748311523
- levelsio：`Because AI is actually good at photos, it sucks at writing useful replies`
  https://x.com/levelsio/status/2115818017569353977
- simonw：`I've been using "AI mania" for when you get carried away building things that you don't even need … but your thing here sounds like something different to that`
  https://x.com/simonw/status/2115850302863946038

**夸也要具体。** simonw 不说 "amazing"，说 `my eyebrows raised at least a dozen times while reading this`（https://x.com/simonw/status/2115821668350435645）。
同一个意思，他还交代了程度和读的过程。

---

## 2. 语言和语气

**长度**（本次样本的中位数，去掉 @ 和链接后统计）：

| 账号 | 回复 | 引用 | 原创 |
|---|---|---|---|
| karpathy | ~219 字符 | ~1.7k | ~1.5k（长文） |
| simonw | ~110 | ~97 | ~181 |
| swyx | ~29 | ~207 | — |
| theo | ~52 | ~83 | — |
| HamelHusain | ~36 | ~213 | ~258 |
| mitchellh | ~152 | — | ~190 |
| jxnl | ~22 | ~94 | — |
| Tibo | ~19 | — | — |

**结论**：回复以一两句为主。真正有料时才写长段，比如 mitchellh 的战报、Hamel 的失败清单。

**大小写**：
- 全小写只有 swyx（21/23 条以小写开头）和 badlogicgames。
- karpathy、simonw、levelsio、Hamel 基本都是正常大小写。
- 你坚持的"随意的小写 dev 口吻"，在 swyx 和 badlogic 身上有先例，可以保留。
- 重点不在小写，在于句子像人随手打出来的：可以省主语、可以有 lol 和 ngl，但不能有"总结腔"。

**怎么开头**：
- 直接下判断：`Close, but wrong direction.`（https://x.com/mitchellh/status/2116309253845832094）
- 交代自己的模型：`My mental model for what is happening is…`（https://x.com/karpathy/status/2106806571321966793）
- 讲"我做了什么"：`Inspired me to try out … on my phone.`（https://x.com/simonw/status/2115822698341519520）
- 不用 "Great post!"、"This is huge"、"Totally agree" 开头。

**数字**：
- 数字是"自己测的 / 算的"，不是从发布稿里抄的。例如 `43M comments … to 6,454 videos … ~2 hours`（https://x.com/karpathy/status/2116957135661945283）、`$0.10`、`I tried some form of it like once a year going back to 2023`。

**hedge（留余地）**：
- simonw 的 `cautiously`、`I'm not sure`、`I dunno about that`，用来表示诚实。
- 不要用 "might potentially" 这种空泛的 hedge。

**反讽 / 幽默**：
- 只用来加一层观点，比如 swyx 的 `altho mine is definitely superior to yours`，karpathy 的 `Don't make any mistakes.`。
- Tibo 那种纯梗回复（https://x.com/thsottiaux/status/2116256600436641887）能爆，是因为他是 Codex 负责人。普通账号照抄只会显得空。

**列表 vs 段落**：
- 回复里几乎没有列表。
- 列表只出现在长原创里，比如 karpathy 的漏斗、Hamel 的失败类型，而且每一项都是具体观察。
- 你的规则"回复/引用不用编号列表"与此一致。

**术语密度**：
- 术语用得准、用得少，一条一般只有一两个（harness、counterfactual、pareto、churn）。
- 不堆砌 "agentic workflow paradigm" 之类的词。

**各人差异**：
- karpathy：长文 + 心智模型 + 量级数字。
- simonw：谨慎、经验驱动、爱追问细节。
- swyx：公式化立场 + 类比 + 自嘲。
- theo：用激励逻辑辩论，嘴硬但讲理。
- Hamel：反 benchmark，强调"自己跑、看数据"。
- mitchellh：工程战报，乐意纠偏。
- levelsio：亲历拆解 + 算账 + 强立场。

---

## 3. 有效的原创结构

**"我试了 X，结果是这样"**（最适合你）：
- 动机 → 结果加数字 → 过程里人工做了哪几步 → 一个开放问题。
- 例：karpathy HackerTube（https://x.com/karpathy/status/2116957135661945283），结尾是 `What else are we not thinking of.`
- 例：levelsio 的 vlog（https://x.com/levelsio/status/2116959423117857026），把每一步用的工具列清楚，再用 P.S. 反转：`I didn't ask for any of this`。

**心智模型 / 框架**：
- 一个结构，配量级数字，再说驱动因素和机制。
- 例：karpathy 的漏斗（https://x.com/karpathy/status/2109361546505966046）。

**递进技巧帖**：
- 每段末尾用 `But even better:` 把读者往上一层带。
- 例：https://x.com/karpathy/status/2105819303471976479

**反共识类比**：
- 把新事物放进一个大家熟悉的旧谱系。
- 例：Hamel 把 AI benchmark 公司和 Gartner、评级机构放在一起（https://x.com/HamelHusain/status/2116987667716223160）。

**带约束的真问题**：
- 交代硬件、目标和自己的猜测，再提问。
- 例：simonw 问 <60GB、>12 tok/s 的 MoE（https://x.com/simonw/status/2108608482442449261）。

**先立反方，再反驳**：
- 例：Hamel 先列三条 pushback，再说利益机制（https://x.com/HamelHusain/status/2114935968604299552）。

---

## 4. 反面模式（读起来像 bot）

来自真实反面样本，见 examples.md 的 E、G 两节：

1. **复述原帖**：把发布稿改写一遍。例：`wow, Asymptote Labs just dropped Beacon 🤯 …`（https://x.com/AIDropDaily/status/2112640235536523373）
2. **搬运钩子**：`this paper should be required reading` 加 `here are the 7 parts`。两个账号用几乎一模一样的模板，同一账号还发了两次（https://x.com/Arindam_1729/status/2114026631941574741 、https://x.com/AnnatarXBT/status/2113634548378374458 、https://x.com/AnnatarXBT/status/2117267486621962721）。
3. **收藏 / 箭头 / emoji 指令**：`(bookmark this)`、`Bookmark this ↓`、`go show it some love 👇`。
4. **空形容词**：`is wild`、`🤯`、`insane`、`game changer`、`this is huge`，后面不跟任何理由。
5. **空问题收尾**：`anyone else … yet? 👀`。真问题会带约束，空问题只是在要互动。
6. **万能夸赞**：比如"这个比喻很贴切，期待你讲细一点"（https://x.com/_ExploreAI/status/2115794714376953963）。
7. **模板化"我的判断"**：同一句"我的判断是工具会继续分层……"被贴到三条不同的帖子下（https://x.com/ChenChaim42853/status/2109870208030855477 等）。"我的判断"四个字本身不是深度，判断要专门针对这一条。
8. **好内容被营销尾巴毁掉**：https://x.com/ReignSwords/status/2116340346418495982 的数据很好（`23 份说明书只用 3 份`、`第 6 次起省钱`），但"尖锐版"、"敢查账吗 👇"、"蓝V互关"让整条掉价。
9. levelsio 和 simonw 都公开表示讨厌 AI 回复，原话是 `X should have a zero tolerance policy for AI replies`（https://x.com/levelsio/status/2115805396753383750）。所以像 bot 不只是"浅"，还会被拉黑。

---

## 5. X 引用/回复：写作清单 + 模板

### 发前 6 问
1. 删掉原帖，这条还成立吗？如果它只是在复述原帖，就重写。
2. 有没有带来一个新东西：机制、我的数据或做法、反例或边界、新框、追问、预测？
3. 有没有一个具体名词或数字（模型 / 档位 / 时长 / 钱 / 文件 / 命令）？
4. 能不能删到一两句？
5. 有没有 bot 词？包括 huge / wild / game changer / great post / totally agree / 🤯 / 👇 / bookmark / "here's why"。
6. 有没有偏好层额外禁用的项目名或称呼？有就按偏好层处理。

### 模板（小写 dev 口吻，括号里是要填的内容）
1. **经验数据**：`ran this on (task) for (time/n runs), the real win was (specific), not (the thing everyone's hyping)`
2. **把问题往前推**：`the hard part isn't (what the post solves), it's (proving/maintaining/paying for) it once (condition)`
3. **激励逻辑**：`makes sense if you look at the incentives: (who) gets (what) when (x), so (prediction)`
4. **适用边界**：`works great for (scenario). falls apart the moment you (condition), learned that the hard way with (concrete thing)`
5. **换框**：`this is basically (familiar old thing) again, and last time the winner was whoever (lesson)`
6. **追问**：`curious what (metric/counterfactual) looks like here. did anyone run it without (the new thing)?`
7. **精确区分**：`(x) and (y) are different problems. this fixes (x), most people's pain is (y)`
8. **预测**：`give it (timeframe) and (specific outcome). (one-clause reason)`

用法：一次只用一个模板，填完再删一半字。
中文释义照旧写在下方给用户看，不随帖发出。

---

## 6. 中文大V：深度和语言（新增）

### 6.1 他们做得好的地方
- **亲自核验，并说清核验边界**（宝玉）：`我查了 Hugging Face 上的文件列表……卖家的截图我没能看到，没法自己逐字节比对。`
  他还自己算了一笔账：`640 片乘以 7.39GB 约等于 4.73TB，离卖家说的 8TB 差了三千多 GB。`
  https://x.com/dotey/status/2116366460939386990
- **术语就地解释，不另起"科普段"**：`遗留代码指公司几十年攒下来、还在运行、但越来越难改的老程序。`、`Token 是 AI 模型的计费单位，可以理解成 AI 干活的"工时"`
  https://x.com/dotey/status/2116218545906319826
- **【】小标题分节，结尾列来源**（宝玉的长文结构）。
- **替中文读者判断相关性**（歸藏）：`不过跟我们关系不大。……估计是为了防止蒸馏之类的东西`
  https://x.com/op7418/status/2116351174253359293
- **预期管理**（歸藏）：`Siri 这部分应该是之前的版本……最主要的不是 Siri，……实时翻译呀之类的其他设备的 AI 功能挺有用的。`
  https://x.com/op7418/status/2116348058254647552
- **自测对比，批评时留一个真实用途**（向阳乔木）：`同样一个 Computer Use 任务在 Project 的 Session 就能顺利完成，而 Dots 就搞不定。……不过，每天让它查下 Github PR 和 Obsidian 插件下载量还挺方便的。`
  https://x.com/vista8/status/2116215180900331783
- **三行压缩一个判断，回复用反问**（orange）：`你用一小时干完老板给你安排了8小时的活儿 / 你的老板会给你涨工资吗？`（https://x.com/oran_ge/status/2116463419129999786 ）、`强大和泡沫并不冲突`（https://x.com/oran_ge/status/2116399550491734066 ）
- **观点帖有转折**（宝玉）：先承认`技术已经没啥护城河了`，再落到`用户选一个产品一个重要因素是对品牌的信任`，最后一句判断：`永远慢半拍`。
  https://x.com/dotey/status/2117306470727336321
- **经验规则，每条都有真实来由**（中小号里的好例子）：`我遇到过它写着「任务完成」，实际是额度中断了。`，以及 `事实、我的判断、AI 的推断，分开标。`
  https://x.com/Chengzhaoran/status/2113483552868143405
- **只挑机制讲，再接上自己的做法**：`我最想抄的是两个设计。……第二点我在 MuseMVP 里也是这么做的`
  https://x.com/wztlink1013/status/2111800466913087777
- **"我的判断"用对的样子**：`单价不吓人，怕的是 agent 搜起来没上限。` / `一个任务到底搜了几次，多数人没数过。`
  https://x.com/sisiliu517/status/2111751048188567903

### 6.2 借鉴 vs 避免

| 借鉴 | 避免 |
|---|---|
| 亲测，并写明"我没能验证的部分" | 吓人开头钩子："你装的那些 Skill，四个里可能就有一个有漏洞。"（https://x.com/vkdefi/status/2117084978026627291） |
| 术语一句话就地解释 | 生活化比喻硬套："就像把家门钥匙交给一个陌生人" |
| 【】分节，结尾列来源 | "关注我少踩坑"、"蓝V互关"、"敢查账吗👇" |
| 相关性判断："跟我们关系不大 / 国内用不了" | 没有对象的"我的判断"套话，或者一句话到处贴 |
| 代价、反例写得老实（`Pass@1 四组涨、一组掉 1 分`） | "尖锐版"、"炸裂"、"封神"、"必看" |
| 短句、口语，但信息密 | 转述原帖加一串话题标签 |

---

## 7. 迁移到小红书（中文、专业、克制）

### 7.1 笔记骨架（替换"罗列功能"式写法）
1. **一句话说清楚**：谁用什么做了什么，给出最关键的一个数字。
2. **我实际怎么用 / 测了什么**：环境、档位、时长、花了多少。没测过就写"没实测"，不要假装测过。
3. **机制**：为什么有效，一两句讲原理。原理靠术语就地解释，不另写科普段。
4. **边界与反例**：什么情况下没用；代价是什么（额度 / 时间 / 安全）。
5. **和你有什么关系**：国内能不能用、要不要现在就装、适合什么人。
6. **原帖 / 来源**。

### 7.2 句子级规则
- 每段只写一个判断，判断后面紧跟证据，可以是数字、截图里能看到的事实，或者自己的操作。
- 用"我这边……"、"实测……"、"没验证……"，不用"大家都知道 / 不得不说 / 值得一提的是"。
- 禁止用词：总而言之、综上所述、赋能、颠覆、炸裂、封神、必看、建议收藏、干货满满、保姆级、一文读懂、关注我。
- "我的判断"可以作为小标题，但下面必须是只适用于这一条的判断，并带一个理由。如果同一句话换到别的笔记也成立，就是套话，要重写。
- 结尾不用"你怎么看？评论区聊聊"。可以留一个具体的问题，例如"有人在 Max 档测过长任务的掉线率吗"，或者直接结束。
- 引用外国大V的观点时，给出原句的中文意思，并说明**为什么他这么说**（他是谁、站在什么利益位置）。例：Tibo 是 Codex 负责人，theo 做 T3 Code。

### 7.3 图卡对应
- 每张卡最多一个"机制图"或"对比表"。表里的每一格都要来自原文或实测，自己补充的解释要标注"我的理解"。
- 加一张"适用边界 / 不适合谁"卡，比"功能清单"卡更显专业。

### 7.4 中文 X 帖（如果要发）
- 参考 orange、歸藏 的短句分行：三到五行，一行一个意思，最后一行是判断。
- 回复中文大V时也照第 1 节的 9 种增量来写，最好用的是"追问"和"边界"。

---

## 8. 附：数据来源说明
- 原始抓取存放在作者本机 `x_depth_study/raw/`（未随包），分析脚本是 `parse.py`、`build_examples.py`，样本清单是 `spec.txt`。
- 所有引文都是接口返回的原文。长帖用 note_tweet 取全文，examples.md 只把 HTML 转义还原（`&amp;`→`&`）。
- 本 guide 里的引文是节选，节选处用"……"标出。
