# Apple 产品页风 小红书卡片模板

参数说明见 ../../references/styles.md「Apple 产品页细则」。

## 文件
- `apple.css`：全部样式，即 design tokens 与组件（.hd 标题区、.stage 图带、.specs 参数格、.cols 两栏、.rows 编号列表、pre/code、.warn、.pair）。
- `gen.py`：页面内容，生成 `build/pN.html`。改 TAG / TOTAL / SRC 和 `P[n]`；单页微调写在 `EXTRA[n]`。
- `shot.mjs`：`node shot.mjs <输出目录>`，截出 01.png… 并打印溢出像素，要求 [0,0]。
- `shoot_diagram.mjs`：`node shoot_diagram.mjs in.html out.png`，把 stack-diagram 的 HTML 去网格、转白底并以 2x 截图。
- `trim.py`：`python3 trim.py assets/*.png`，裁掉外框和多余白边，四周留 36px。
- `assets/`：示例图（java / python / agent）。

## 流程
1. 用 `shoot_diagram.mjs` 截图，再用 `trim.py` 裁边，放进 assets/。
2. 改 `gen.py` 内容，执行 `python3 gen.py && node shot.mjs out`。
3. 逐张检查溢出、孤字和空白带（不超过约 8%）。不够满就在 `EXTRA[n]` 里加大行距或字号。

需要本机已安装 playwright（npm i playwright），或设置 PLAYWRIGHT_MJS。
