# 卡片风格库

模板都在 `../templates/`。`classic/` 用 `../scripts/render_html.sh name.html out.png` 截图；`overview.html` 为六款总览。

| 风格 | 视觉要点 | 配色 | 字体 | 适合 | 模板 |
|---|---|---|---|---|---|
| Apple 产品页（开发者工具首选之一） | 纯白页、居中超粗紧排大标题、关键词蓝紫粉渐变字、通栏浅灰底带上放 28px 圆角白图卡、细线参数格、大数字参数区、渐变大编号纵向列表 | 白 #FFF，底带 #F5F5F7，主字 #1D1D1F，正文 #6E6E73，渐变 #0A84FF→#5E5CE6→#BF5AF2→#FF375F | Inter + 思源黑体（Noto Sans CJK SC），代码 JetBrains Mono | 开发者工具、开源项目、示例合集、截图或架构图当主角的产品介绍；纯概念科普偏冷不适合 | `apple/`（apple.css、gen.py、shot.mjs、shoot_diagram.mjs、trim.py、README.md） |
| 像素游戏 | 深色游戏画面、像素标题、像素机器人 / CRT 电脑、RPG 对话框、1P vs 2P、道具格、存档框、NEXT ▶ | 底 #1B1F3B，黄 #FFD23F、绿 #7CF29C、红 #E4572E、蓝 #2E5EAA，外框米格纸 | Fusion Pixel 只用于标题 / 标签，正文用常规黑体 | 系列科普、记忆点强的固定合集（适合记忆点强的固定合集） | `pixel/`（README、`SERIES=合集名 ./new_post.sh 02`、render.sh 自带检查、PROMPTS.md 统一蓝色小机器人）；原样张 `classic/s4.html` |
| 黑板粉笔 | 黑板质感、粉笔字、彩色粉笔圈和箭头、木框 | 粉笔白 #f4f1e8，黄 #FFE566、蓝 #66B3FF、粉 #FF9999、绿 #90EE90 | 站酷快乐体 + 霞鹜文楷 | 上课感强的概念讲解；白底截图贴在黑板上很跳 | `classic/s2.html` |
| 3D 黏土 | 黏土机器人、软糯圆角卡片、奶油底 | #FFFDF8，紫 #CDBEF0、薄荷 #BDEBDD、深紫字 #4B3B7A | Noto Sans CJK + 站酷快乐体 | 面向怕技术的普通读者 | `classic/s3.html` |
| 新粗野撞色 | 粗黑边框、硬投影、贴纸、撞色块 | #FF4757、#FECA57、#00D2D3、#A29BFE、黑 | 得意黑 + Noto Sans CJK | 抢眼的对比 / 观点类（偏花哨） | `classic/s1.html` |
| 复古报纸 | 报头、双线栏线、网点插图、引文框 | #EDE5D3、墨黑 #1d1a16、红 #B3261E | Noto Serif/Sans CJK | 讲定义、澄清误解、新闻解读 | `classic/s5.html` |
| 马卡龙手账 | 方格纸、和纸胶带、荧光笔标题、便利贴 | #C9EEDD、#FFD3DC、#BFD9EE、棕字 #8a6a50 | 站酷快乐体 + 霞鹜文楷 | 清单、方法、学习笔记 | `classic/s6.html` |
| 手绘·视觉笔记（手绘首选） | 奶油点阵纸、马卡龙色块故意不填满、rough.js 抖动线框与箭头、色块横幅标题、马克笔风插画小人 | 蓝 / 桃 / 薄荷 / 薰衣草色块，珊瑚红强调 | 站酷快乐体 + 霞鹜文楷 | 概念讲解、流程、对照，最像爆款知识卡 | `doodle/d_sketchnote.html`（gen.py 生成、shot.mjs 截图） |
| 手绘·蜡笔彩铅 | 牛皮纸底加纸纹噪点、蜡笔斜线填色、彩铅绘本插画 | 红黄蓝绿蜡笔色 | 站酷快乐体 + 霞鹜文楷 | 温暖、亲子 / 入门向；斜线别压在大段文字下 | `doodle/d_crayon.html` |
| 手绘·白板（Excalidraw） | 白底浅网格、手写字、rough.js 斜线淡彩填充、Excalidraw 风图标 | 白底，蓝强调，淡彩 | 小赖 Xiaolai | 干净的结构图、流程；多页全用会显花哨 | `doodle/d_excalidraw.html` |
| Swiss / Editorial（guizang 外部包） | 网格、粗无衬线、单一强调色 | 按题材选强调色 | 包内自带 | 新闻截图、引文类；普通科普嫌朴素时不要首选 | guizang-social-card |
| 研究简报（brief） | 白底、衬线标题、单一强调色 | 按题材选强调色 | Noto Serif/Sans CJK | 新闻截图类备用 | `brief_renderer/` |
| 杂志简报（偏朴素） | 米色纸、衬线大标题、细线网格 | #f3eee4 / #1d1b18 / #9a3d22 | Noto Serif SC | 深度长文；不要主动选 | 未随本仓库（可自建模板） |
| 现代科技卡片（偏朴素） | 浅灰蓝底、白圆角卡、紫色编号 | #f5f6fb / #5b4ddb | Inter + Noto Sans SC | 工具 / 产品功能介绍 | 未随本仓库（可自建模板） |

已淘汰：手绘涂鸦·橙黑旧版（被上面三款手绘取代）。

## 手绘细则
线条统一用 rough.js，比 SVG 滤镜扭曲稳；VS 圆圈和两侧文字留足间距；注意行末孤字。

## Apple 产品页细则
- 字号（1080×1440）：封面标题 104px/900/字距 -0.045em/行高 1.08；内页标题 86–100px 同字重字距；眉题 28px/700 渐变；副标题 28px/500 灰；小标题 30–40px/800/-0.02em；正文 25–30px 行高 1.6 灰；参数大数字 52px/800/-0.04em 配 21px 灰小注；角标 22px/700。
- 标题居中，不用中文句号收尾。渐变只用在封面关键词、眉题、大编号这类少量字上（`-webkit-background-clip:text`），渐变字要细，不铺大色块；链接色 #0066CC，提醒色 #BF4800。
- 圆角：图卡 28px，提示框 24px，代码块 20px。阴影只一层极淡：`0 1px 2px rgba(0,0,0,.04), 0 24px 48px -28px rgba(0,0,0,.16)`。
- 分区从上到下：顶栏（左角标「合集 · 0N」，右页码）→ 居中标题区 → #F5F5F7 通栏示例图带 → 细线参数格（两行：粗名称＋灰小注）→ 两栏说明或渐变大编号纵向列表（行间 1px 细线）→ 页脚（左来源、右蓝色仓库链接）。左右边距 60px，区块间 20–28px。
- 示例图：带网格的先去网格转白底再 2x 截图（stack-diagram 注入 `.canvas{background-image:none;background:#fff}`），裁掉外框和白边；横图铺满底带宽，方图收到 72–76% 宽。图注一行「FIG.N　图上看什么」，署名只在页脚写一次。
- 不用 emoji、贴纸、手绘元素；内容少的页放大行距 / 字号 / 参数格补满，不留空。

## 参考来源
- https://github.com/JimLiu/baoyu-skills （baoyu-xhs-images 的 chalkboard、sketch-notes 预设；只借规范，不让生图模型写中文）
- https://github.com/comeonzhj/Auto-Redbook-Skills （主题配色）
- https://github.com/BboTTM/xiaohongshu-card-skill （mode-sketchnote、mode-whiteboard）
- https://roughjs.com 、https://excalidraw.com
- 字体：smiley-sans、fusion-pixel-font、kose-font（小赖）、霞鹜文楷、站酷快乐体
