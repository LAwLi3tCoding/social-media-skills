# 杂志大排版 · 小红书卡片模板

参数与细则见 `../../references/styles.md`「杂志大排版细则」。

与「杂志简报」（米色细线、偏朴素、作者嫌丑）不是同一套。本套是整页强调色封面、超大数字、编号信息卡、前后价格对比、反白横条、竖柱 / 横条榜单。

## 文件

- `magazine.css`：版式规则；配色全部走 `:root` / `body.theme-*` 变量（`--ac` `--ink` `--paper` `--tan` `--mu`）
- `gen.py`：读 JSON → 写 `html/0N.html` → 调 `../../scripts/render_html.sh` 出 1080×1440 PNG
- `example.json`：示例内容（标注为示例；数字可替换）

## 配色预设

| 参数 | 主强调 `--ac` | 适用题材 |
|---|---|---|
| `anthropic` | `#D97757` 陶土橙 | Claude / Anthropic |
| `openai` | `#0D7A5F` 墨绿 | OpenAI / ChatGPT |
| `google` | `#1A73E8` 蓝 | Gemini / Google |
| `crimson` | `#C44536` 中性红 | 通用新闻、中性题材 |

一主一辅：强调色 `--ac`，墨色 `--ink` 兼辅。换主题只改 `--theme`，版式不变。

## 页型

| `type` | 画面 | 关键字段 |
|---|---|---|
| `cover` | 整页强调色底；顶栏；衬线大标题；超大数字；三栏白底阴影信息卡 | `title` `dek` `giant` `giant_sub` `cards[]` |
| `compare` | 米色纸；前后价格（旧值划掉、新值大号强调色）；双栏参数；反白横条；底部标签 | `rows[]` `specs[]` `band` `note` |
| `bars_v` | 竖柱对比；可选 header 超大编号、rest 同榜其他、banner 代价条、bracket | `bars[]` `header_no` `rest` `banner` `bracket` |
| `ranking` | 上区大数字故事 + 网格其他；下区反白横条榜 | `top` `inv` `bars[]` `note` |

## 用法

```bash
# 示例：Anthropic 橙
python3 gen.py example.json --out /tmp/mag-anthropic --theme anthropic

# 换配色（同一内容）
python3 gen.py example.json --out /tmp/mag-openai --theme openai

# 只出 HTML、不截图
python3 gen.py example.json --out /tmp/mag-html --theme google --html-only
```

产物写到 `--out`，不要写进本 skill 目录。出图后跑：

```bash
python3 ../../scripts/check_cards.py /tmp/mag-anthropic/*.png
```

再逐张看溢出、截断、重叠、大片空白。

## 硬约束（本风格）

- 最小字号 28px；标题不低于 84px
- 数字用等宽特征（`.n`）；标题衬线（`.serif`）；代码 / ID 用 `.mono`
- 反白横条（`.blk` / `.fastb` / `.inv`）带阴影，左右可出血（负 margin）
- 内容字典不要写死某一家产品的数字；示例放 `example.json`
