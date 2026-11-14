---
name: xhs-card-design
description: >-
  给小红书笔记做 3:4 配图时用：先规划每张放什么，再挑视觉风格、用 HTML 模板或 guizang / xhs-html 渲染
  1080×1440，最后跑尺寸与留白检查。也管封面选型和截图处理。
---
# 小红书配图：规划、风格、渲染、检查

只在文字稿被用户确认后做图。各合集固定用哪种风格见用户的偏好层（如有）。本 skill 的脚本、模板和参考文件都在它自己目录下的 `scripts/`、`templates/`、`references/`。

## 1. 规划（每张放什么）

详见 `references/card-planning.md`。要点：

- 先定主阅读面：概念、原理、科普类把定义、机制、例子、前提写在图卡上，读者只翻图也能懂；新闻、工具类图放截图、对比、关系，正文补版本、权限、额度、条件。
- 封面写对象 + 主张，信息本身当钩子。工具 / Skill 封面要让人一眼看出它是干嘛的，不只写实测数字。排名表、流程图、模块图优先；新闻或引文用原帖截图铺满。
- 一页推进一步：现象命名 → 对照或机制 → 例子 → 方法或检查；内容少就少做几页。
- 每张最多一个机制图或对比表；表格每格来自原文或实测；自补解释和原文分层（可标「我的理解」）。
- 主卡像一条编辑过的长帖：以文字和高亮引文为主，不为表格而表格。
- 官方原文（prompt、原句）放最后几张作附录。

## 2. 硬规则（所有风格）

- 尺寸 1080×1440（3:4）。所有文字（尤其中文）用 HTML + 字体渲染；生图模型只出插画或背景，图里不许有字。
- 每张排满，不留大块空白：空了就补真实细节、插画或调版式（检查见 §5）。
- 字小、密度高：正文约 25–38px（随模板），标题 56–100px，小字不低于 20px。
- 配图标题直接写信息，不用聊天口吻；中英文断行别挤在一起；标题不以中文句号收尾。
- 文字用稿件原句；为版式加的短标签（VS、STAGE 0N 等）要少，并告诉用户加了哪些。
- 截图放大铺满，裁掉上下白边。
- 不用 emoji 当图标；用 SVG 或同风格插画。插画风格和版面统一，不像拼贴。
- 配色按题材选，干净克制；强调色参考：Claude 陶土橙、OpenAI 绿、DeepSeek 蓝、开源项目 GitHub 深灰或项目品牌色。
- 合集帖：角标写「合集名 · 0N」，页码另放右上角。
- 不用粗糙的 Python / PIL 直接画图。

## 3. 选风格

风格表、配色、字体、模板位置见 `references/styles.md`。挑法：

- 固定合集：选定一种做成模板目录，之后每篇只换内容；用户点名换风格时按用户说的来。
- 轮换合集：每篇可以不同，按内容挑；避开太花哨和太朴素，偏美观克制、有层次（大字标题、强调色块、编号、带阴影图卡，一主一辅两色；手绘和便签只用模板里的 `handdrawn/`、`sticky/`，做不到那个水准就换风格）。
- 开发者新闻、截图类：guizang Swiss 或 `brief_renderer`；模型发布、跑分、价格对比这类数字主导的新闻：杂志大排版（`templates/magazine/`，配色按主题换）；工具 / Skill 介绍：Apple 产品页、报纸、白板手绘。
- 普通读者科普：黑板、黏土、手账、手绘三款、像素。
- 用户没指定：同一页（封面 + 一张内页）出 3–5 种风格样张，拼成对比图让用户挑，再做全套。

## 4. 渲染

| 方式 | 何时用 | 怎么跑 |
|---|---|---|
| 本包 HTML 模板 | 风格表里的样式 | `scripts/render_html.sh page.html out.png`；Apple 和手绘模板用各自的 `shot.mjs`；像素用 `templates/pixel/render.sh` |
| `templates/magazine/gen.py` | 杂志大排版（新闻、跑分、价格对比） | `python3 templates/magazine/gen.py content.json --out <稿目录>/cards --theme anthropic`（主题有 anthropic / openai / google / crimson，内部调 `scripts/render_html.sh`；页型和 JSON 格式见该目录 README） |
| guizang-social-card（外部包） | Swiss / Editorial、公众号封面、Live Photo | 安装 `npx skills add op7418/guizang-social-card-skill -g -y`；按其 SKILL.md 用 `node scripts/render.mjs`；默认 Swiss + `.poster.xhs`；不改包内模板源文件 |
| xhs-html（外部包，creator-buddy） | 备选排版，62 种风格 | 选偏研究简报 / 瑞士信息图的风格，避开少女可爱风 |
| `templates/brief_renderer/render.py` | 研究简报风备用 | `python3 render.py deck.json --theme brief --density compact` |

外部作图工具不必是小红书专用，能出 3:4 1080×1440 并接进本流程即可。
产物写到 `<稿目录>/cards/`，不写进 skill 目录。换机首次使用先设 `FONTS_DIR` 并跑 `scripts/relocate.sh`。
与本 skill 冲突时：口吻、禁用词、信息密度以 `social-copywriting` 和本 skill 为准，版式可以跟外部包。

## 5. 检查（每次出图后）

```bash
python3 scripts/check_cards.py <稿目录>/cards/*.png      # 尺寸 + 空白横带 ≤8% + 8×6 网格留白，须 PASS
python3 ../social-copywriting/scripts/lint_copy.py --text <稿目录>/cards_src/*.html
```

再逐张看：溢出、重叠、截断、孤字折行、发糊、底部被裁。深色大底（像素风夜空、黑板）网格检查易误报：看图确认那是画面不是空白，再用 `--mode band` 复核并告诉用户。

## 依赖

- Chrome / Chromium（headless 截图）；Python 3 + Pillow + numpy；Node + playwright（Apple、手绘模板的 `shot.mjs`：`npm i playwright`，或设环境变量 `PLAYWRIGHT_MJS`）。
- 字体（不随包分发，放到 `$FONTS_DIR` 后跑 `scripts/relocate.sh`）：Noto Sans/Serif CJK SC（系统包 `fonts-noto-cjk`）、Inter、JetBrains Mono、得意黑 Smiley Sans（atelier-anchor/smiley-sans）、Fusion Pixel（TakWolf/fusion-pixel-font）、霞鹜文楷 LXGW WenKai（lxgw/LxgwWenKai）、小赖 Xiaolai（lxgw/kose-font）、站酷快乐体（Google Fonts: ZCOOL KuaiLe）、青柯 / 马善政 / 小薇（Google Fonts: ZCOOL QingKe HuangYou、Ma Shan Zheng、ZCOOL XiaoWei）。

用户确认新风格或纠正视觉偏好：风格写进 `references/styles.md`，个人选择写进偏好层。
