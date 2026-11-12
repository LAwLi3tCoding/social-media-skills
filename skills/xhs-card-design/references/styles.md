# 卡片风格库

模板都在 `../templates/`。`classic/` 用 `../scripts/render_html.sh name.html out.png` 截图；`overview.html` 为六款总览。

| 风格 | 视觉要点 | 配色 | 字体 | 适合 | 模板 |
|---|---|---|---|---|---|
| Apple 产品页（开发者工具首选之一） | 纯白页、居中超粗紧排大标题、关键词蓝紫粉渐变字、通栏浅灰底带上放 28px 圆角白图卡、细线参数格、大数字参数区、渐变大编号纵向列表 | 白 #FFF，底带 #F5F5F7，主字 #1D1D1F，正文 #6E6E73，渐变 #0A84FF→#5E5CE6→#BF5AF2→#FF375F | Inter + 思源黑体（Noto Sans CJK SC），代码 JetBrains Mono | 开发者工具、开源项目、工具或 Skill 介绍、截图或架构图当主角的产品介绍；纯概念科普偏冷不适合 | `apple/`（apple.css、gen.py、shot.mjs、shoot_diagram.mjs、trim.py、README.md） |
| 像素游戏 | 深色游戏画面、像素标题、像素机器人 / CRT 电脑、RPG 对话框、1P vs 2P、道具格、存档框、NEXT ▶ | 底 #1B1F3B，黄 #FFD23F、绿 #7CF29C、红 #E4572E、蓝 #2E5EAA，外框米格纸 | Fusion Pixel 只用于标题 / 标签，正文用常规黑体 | 系列科普、记忆点强的固定合集（哪一套合集专用见偏好层） | `pixel/`（README、`SERIES=合集名 ./new_post.sh 02`、render.sh 自带检查、PROMPTS.md 统一蓝色小机器人）；原样张 `classic/s4.html` |
| 黑板粉笔 | 黑板质感、粉笔字、彩色粉笔圈和箭头、木框 | 粉笔白 #f4f1e8，黄 #FFE566、蓝 #66B3FF、粉 #FF9999、绿 #90EE90 | 站酷快乐体 + 霞鹜文楷 | 上课感强的概念讲解；白底截图贴在黑板上很跳 | `classic/s2.html` |
| 3D 黏土 | 黏土机器人、软糯圆角卡片、奶油底 | #FFFDF8，紫 #CDBEF0、薄荷 #BDEBDD、深紫字 #4B3B7A | Noto Sans CJK + 站酷快乐体 | 面向怕技术的普通读者 | `classic/s3.html` |
| 新粗野撞色 | 粗黑边框、硬投影、贴纸、撞色块 | #FF4757、#FECA57、#00D2D3、#A29BFE、黑 | 得意黑 + Noto Sans CJK | 抢眼的对比 / 观点类（偏花哨） | `classic/s1.html` |
| 复古报纸 | 报头、双线栏线、网点插图、引文框 | #EDE5D3、墨黑 #1d1a16、红 #B3261E | Noto Serif/Sans CJK | 讲定义、澄清误解、新闻解读 | `classic/s5.html` |
| 便签墙（便签首选） | 浅格纸底、便签纸轻微旋转、柔和投影、半透明和纸胶带、彩色便签分区，排版有层次、排满不互相压字 | 奶黄 / 浅蓝 / 薄荷 / 浅粉 / 薰衣草便签，深墨字 | 小赖 + 霞鹜文楷，英文名用 Inter | Skill / 工具介绍、方法清单、流程；轮换合集可用 | `sticky/01–06.html`（示例 06 全套：封面、四步流程、刹车、配套方法、代价、安装）；`scripts/render_html.sh` 截图，预览 `sticky/preview.png` |
| 手绘·真手绘（手绘首选，2026-11-11 替换旧视觉笔记） | rough.js 手画线框和箭头、手写体大标题、手绘图标和编号圆圈、斜线淡彩填充，整版铺满，不用规整方框网格和大块空白 | 白格纸底，蓝强调，黄 / 粉 / 绿 / 蓝淡彩 | 小赖 + 霞鹜文楷，英文名用 Inter | 概念讲解、流程、对照 | `handdrawn/01.html`（封面）、`02.html`（流程页），`shot.mjs` 截图 |
| 卡片编号（classic 卡片） | 大字标题、深色强调条、编号格、带阴影小卡，一主一辅两色 | 墨色 + 青绿 #1F6F6B | Noto Sans CJK，英文 Inter | 轮换合集的干净默认，信息密的介绍 / 测评 | `cards/01.html`、`02.html`，`scripts/render_html.sh` |
| 手绘·蜡笔彩铅 | 牛皮纸底加纸纹噪点、蜡笔斜线填色、彩铅绘本插画 | 红黄蓝绿蜡笔色 | 站酷快乐体 + 霞鹜文楷 | 温暖、亲子 / 入门向；斜线别压在大段文字下 | `doodle/d_crayon.html` |
| 手绘·白板（Excalidraw） | 白底浅网格、手写字、rough.js 斜线淡彩填充、Excalidraw 风图标 | 白底，蓝强调，淡彩 | 小赖 Xiaolai | 干净的结构图、流程；多页全用会显花哨 | `doodle/d_excalidraw.html` |
| Swiss / Editorial（guizang 外部包） | 网格、粗无衬线、单一强调色 | 按题材选强调色 | 包内自带 | 新闻截图、引文类；普通科普嫌朴素时不要首选 | guizang-social-card |
| 研究简报（brief） | 白底、衬线标题、单一强调色 | 按题材选强调色 | Noto Serif/Sans CJK | 新闻截图类备用 | `brief_renderer/` |
| 杂志大排版 | 整页强调色封面、顶栏粗黑线、衬线大标题、超大数字主视觉、01/02/03 白底阴影编号信息卡；内页米色纸、前后价格大字对比（旧值划掉）、双栏大数字参数、通栏黑色反白横条带阴影、竖柱/横条榜单 |配色按主题（`--ac` 一主 + `--ink` 一辅）；预设 anthropic 陶土橙 / openai 墨绿 / google 蓝 / crimson 中性红；纸色 `--paper` 米色系 |Noto Serif CJK SC（标题）+ Inter / Inter Tight（数字）+ Noto Sans CJK SC + JetBrains Mono |新闻资讯、模型发布、跑分和价格对比等数字主导的帖子 |`magazine/`（magazine.css、gen.py、example.json、README.md） |
| 杂志简报（偏朴素） | 米色纸、衬线大标题、细线网格 | #f3eee4 / #1d1b18 / #9a3d22 | Noto Serif SC | 深度长文；不要主动选 | 未随包（可自建模板） |
| 现代科技卡片（偏朴素） | 浅灰蓝底、白圆角卡、紫色编号 | #f5f6fb / #5b4ddb | Inter + Noto Sans SC | 工具 / 产品功能介绍 | 未随包（可自建模板） |

已淘汰：手绘涂鸦·橙黑旧版（被上面三款手绘取代）。

本仓库仍保留 `classic/s6.html`（马卡龙手账）和 `doodle/d_sketchnote.html`（手绘视觉笔记）作为备选样张。

## 手绘细则
线条统一用 rough.js，比 SVG 滤镜扭曲稳；VS 圆圈和两侧文字留足间距；注意行末孤字。

## Apple 产品页细则
- 字号（1080×1440）：封面标题 104px/900/字距 -0.045em/行高 1.08；内页标题 86–100px 同字重字距；眉题 28px/700 渐变；副标题 28px/500 灰；小标题 30–40px/800/-0.02em；正文 25–30px 行高 1.6 灰；参数大数字 52px/800/-0.04em 配 21px 灰小注；角标 22px/700。
- 标题居中，不用中文句号收尾。渐变只用在封面关键词、眉题、大编号这类少量字上（`-webkit-background-clip:text`），渐变字要细，不铺大色块；链接色 #0066CC，提醒色 #BF4800。
- 圆角：图卡 28px，提示框 24px，代码块 20px。阴影只一层极淡：`0 1px 2px rgba(0,0,0,.04), 0 24px 48px -28px rgba(0,0,0,.16)`。
- 分区从上到下：顶栏（左角标「合集 · 0N」，右页码）→ 居中标题区 → #F5F5F7 通栏示例图带 → 细线参数格（两行：粗名称＋灰小注）→ 两栏说明或渐变大编号纵向列表（行间 1px 细线）→ 页脚（左来源、右蓝色仓库链接）。左右边距 60px，区块间 20–28px。
- 示例图：带网格的先去网格转白底再 2x 截图（stack-diagram 注入 `.canvas{background-image:none;background:#fff}`），裁掉外框和白边；横图铺满底带宽，方图收到 72–76% 宽。图注一行「FIG.N　图上看什么」，署名只在页脚写一次。
- 不用 emoji、贴纸、手绘元素；内容少的页放大行距 / 字号 / 参数格补满，不留空。

## 杂志大排版细则

与「杂志简报」（米色细线网格、偏朴素）不是同一套。本套来自 Claude Fable 5.2 等模型发布帖的定稿版式，强调数字层级和杂志感分区。

- **字号层级（1080×1440）**：最小 28px（顶栏、页脚、effort 小注）；标题衬线不低于 84px（封面 h1 / 内页 h2）；封面超大数字约 390px；内页价格新值约 170px、旧值划掉约 110px；三栏信息卡大数字约 90px；反白横条大数字 96–120px；竖柱顶数字 56–96px。
- **分区顺序**
  - 封面：顶栏（左合集 / 右品牌）粗黑底线 → 衬线大标题 + dek 细线 → 超大数字主视觉 + 副句 → 白底带阴影三栏编号卡（01/02/03）→ 页脚来源 + 页码。
  - 对比页：顶栏 → 衬线大标题 + lede → 粗黑线上的前后价格行（旧值划掉、箭头、新值强调色）→ 双栏大数字参数 → 通栏黑色反白横条（可带右侧价格）→ 底部强调色标签 + 说明 → 页脚。
  - 竖柱页：顶栏 → 超大编号 + 标题（或仅标题）→ 底边粗黑线的柱群 + 柱名 → 可选括号标注 / 同榜其他 / 反白代价条 → 页脚。
  - 横条榜：顶栏 → 标题 → 上区故事（编号 + 大数字 + 主张 + 网格其他）→ 反白出血横条榜 → 可选底部说明 → 页脚。
- **阴影与反白横条**：三栏卡 `0 30px 70px` 暖色阴影；`.blk` / `.fastb` / `.inv` 黑底反白，左右负 margin 出血，阴影 `0 26px 60px rgba(0,0,0,.25)`；高亮柱用强调色 + 轻阴影。
- **配色按主题换**：只换 `body.theme-*`（或 `gen.py --theme`）。变量：`--ac` 强调、`--ink` 墨、`--paper` 纸、`--tan` 浅辅、`--mu` 次要字。预设见 `templates/magazine/README.md`。版式规则不随主题改。
- **用法**：`python3 templates/magazine/gen.py example.json --out <稿目录>/cards --theme anthropic`，再 `scripts/check_cards.py`。

## 参考来源
- https://github.com/JimLiu/baoyu-skills （baoyu-xhs-images 的 chalkboard、sketch-notes 预设；只借规范，不让生图模型写中文）
- https://github.com/comeonzhj/Auto-Redbook-Skills （主题配色）
- https://github.com/BboTTM/xiaohongshu-card-skill （mode-sketchnote、mode-whiteboard）
- https://roughjs.com 、https://excalidraw.com
- 字体：smiley-sans、fusion-pixel-font、kose-font（小赖）、霞鹜文楷、站酷快乐体
