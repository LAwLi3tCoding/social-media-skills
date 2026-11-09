# 像素游戏风模板（固定合集用；合集名通过 SERIES 环境变量传入）

每篇 4 张，尺寸 1080×1440。文字全部由 HTML 加字体渲染，插画用 GenerateImage 生成，图里不能有字。样板是 `example_post01/`，成品输出到你指定的目录（见 `render.sh`）。

## 目录
| 路径 | 作用 |
|---|---|
| `base.css` | 共用样式：配色变量、像素硬边框 `.px`、顶栏、游戏画面 `.screen`、对话框 `.dlg`、对战栏 `.vs`、道具格 `.slots`、小卡 `.pair/.it`、页脚 |
| `example_post01/p1–p4.html` | 4 种页型的样板（每页自带少量页内样式），新篇复制后改文字 |
| `example_post01/img/` | 本篇专用插图（封面、场景、存档点等） |
| `assets/` | 全系列共用素材：像素字体需自行下载 Fusion Pixel（OFL，见 `assets/fonts/OFL-fusion-pixel.txt`），放到 `$FONTS_DIR` 后运行 `scripts/relocate.sh`、像素机器人和电脑 `px_robot.png / px_pc.png`、心和星 `px_heart.png / px_star.png`、道具图标 `items/` |
| `render.sh` | 渲染并检查：`./render.sh <稿件目录> <输出目录>`，把 p1.html… 输出为 01.png…，然后自动跑 check.py |
| `../../scripts/check_cards.py` | 合并后的出图检查（尺寸、空白横带 ≤8%、8×6 网格留白）；render.sh 自动调用 |
| `new_post.sh` | `SERIES=合集名 ./new_post.sh 02`：复制样板为 `post02/`，角标改成「合集名 · 02」 |
| `tools/cutout.py` | 纯色底插图抠图、切图 |
| `PROMPTS.md` | 各类插画的 GenerateImage 提示词 |

依赖：google-chrome（无头截图）、Python 3 + Pillow + numpy、系统字体 Noto Sans CJK SC（正文）。

## 4 种页型（样板对应 post01）
1. **p1 封面加定义**：`.screen.cover` 用封面主视觉做背景，左上放大像素标题（132px，`<span class="g">` 为绿色第二色），旁边是副标题加「▶ PRESS START」；下面是定义对话框 `.dlg`（小节标题 `.sec`、重点句加 `.hl`），再下面是 5 格道具 `.slots`。
2. **p2 对照页**：短游戏画面（像素标题加机器人和电脑）→「提示」对话框和三步 `.flow` → 两张小卡 `.pair` → `.sec` 小节标题 → 1P/2P 对战 `.vs` → 「新词」框 `.ml`。
3. **p3 场景页**：场景大图 `.scene`（标题叠在上方夜空，带渐变底）→ 两栏「能做到 / 会出错」`.col`（底部各放一条从场景图裁下来的细条）→ 「提示」对话框 → 红色警告框 `.warn`。
4. **p4 收尾页**：存档大对话框 `.save`（黄色双线框、「已存档」标签、存档点插图、整句定义、满格进度条）→ `.sec` → 聊天气泡对话框 → 道具图标横条 → 深色「NEXT ▶」条。

每篇按内容挑页型，可以重复用同一种，也可以合并。页序固定为封面在前、存档收尾页在后。

## 给第 N 篇出图（以 02 为例）
1. `cd <skill>/templates/pixel && ./new_post.sh 02`
2. 改 `post02/p1–p4.html` 里的文字：
   - 只用 `postNN.md` 里的原句；短标签可以拆用原句片段，例如道具格、对照格、聊天气泡。
   - 不预告具体的后续篇目。
   - 页码写「1 / 4」…，页脚进度格写「■ □ □ □」…，来源写这一页用到的 S 编号对应的机构名。
   - 像素字体（class `pix` / `.sec` / `h1` / `.who` / `.h`）只用在标题和标签上，正文保持 Noto Sans。
   - 像素 UI 标签每页最多一两个（提示、1P/2P、PRESS START、已存档、NEXT、注意），不要堆砌。
3. 换插图：按 `PROMPTS.md` 用 GenerateImage 出封面主视觉和场景图，放进 `post02/img/`，同名覆盖或改 html 里的路径。存档点图可以直接复用。
4. 渲染：`./render.sh post02 ../post02_pixel`
5. 逐张看图，重点检查：
   - 底部有没有被裁切；
   - 有没有单字孤行（用 `<br>` 断句）；
   - 标题有没有压到插图主体；
   - 各模块之间是不是挤在一起（挤了就减插图高度或字号）；
   - check.py 是否全部 OK。
   排版是 flex 列纵向等分（`justify-content:space-between`）：内容少时间距自动拉开，内容多时会贴在一起甚至溢出。

## 规格速记
- 正文 32–34px，辅助文字 26–30px，来源 22px；像素标题 78–132px，像素标签 30–48px。
- 颜色：墨蓝 `--ink`、夜空 `--night`、纸底 `--paper`，强调色是黄、绿、红、蓝、淡蓝，粉、薄荷、奶油三种浅色作卡片底。
- 留白：check.py 的阈值是 8%；样板实测最大 2.7%。

## 注意
- Chrome 截图会读最新文件；用 Read 工具看图时，同一路径可能显示缓存旧图，复查时换个文件名再看。
- 生成的插图偶尔自带小装饰（例如爱心）；和内容冲突时要抠掉，可参考 `px_pc.png` 的处理。
