# social-media-skills

Agent Skills for social media content — 给写 AI / 开发者向社媒内容的 Agent 用的一组可安装 Skill。

当前包含 3 个 Skill（后续还会继续往这个仓库加社媒相关 Skill）：

| Skill | 做什么 |
|---|---|
| `content-quality-gate` | 选题过滤、七项质量门槛、九种增量、隔离环境实测与取证 |
| `social-copywriting` | 标题 / 正文 / 话题规则、禁用句式与套话、去 AI 味流程、`lint_copy.py` |
| `xhs-card-design` | 小红书 3:4 配图规划、12 种风格模板、HTML 渲染、`check_cards.py` 留白检查 |

English: Agent skills for drafting developer/AI social posts (quality gate → copy lint → Xiaohongshu 3:4 card design). Installable via the skills CLI or by copying into your agent skills directory.

## 安装

```bash
# 推荐：skills CLI
npx skills add LAwLi3tCoding/social-media-skills

# 或手动拷贝到 Agent 的 skills 目录（任选其一）
cp -R skills/* ~/.claude/skills/
cp -R skills/* ~/.agents/skills/
```

装好后按各目录下的 `SKILL.md` 使用。三个 Skill 可单独用，也可以按「门槛 → 文案 → 配图」串起来。

## 依赖（按需）

- **content-quality-gate**：无额外依赖，会用到 shell / `rg`。
- **social-copywriting**：Python 3。可选去 AI 味检测：[lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone)（**CC BY-NC 4.0，不随本仓库分发**）
  ```bash
  npx skills add larashero3-dotcom/lieflat-less-ai-tone -g -y
  ```
  账号特有禁词不要改默认列表，用：
  ```bash
  python3 skills/social-copywriting/scripts/lint_copy.py --body body.txt --extra-ban '词1,词2'
  # 或在偏好文件里写: ban: 词1,词2
  python3 skills/social-copywriting/scripts/lint_copy.py --body body.txt --profile preferences.md
  ```
- **xhs-card-design**：
  - Chrome / Chromium、Python 3 + Pillow + numpy
  - Node + playwright（Apple / 手绘模板的 `shot.mjs`）：`npm i playwright`，或设置 `PLAYWRIGHT_MJS`
  - 中文字体**不进仓库**（体积与授权）：装到 `$FONTS_DIR` 后运行 `skills/xhs-card-design/scripts/relocate.sh`
  - 可选 Swiss / Editorial 渲染：[guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)（**AGPL，不随本仓库分发**）
    ```bash
    npx skills add op7418/guizang-social-card-skill -g -y
    ```

模板体积已控制在较小范围（仓库总体约数 MB）。像素风字体 Fusion Pixel（OFL）需自行下载；说明见 `skills/xhs-card-design/templates/pixel/assets/fonts/OFL-fusion-pixel.txt`。手绘模板自带的 `rough.js` 为 MIT（见同目录 `ROUGHJS-LICENSE.txt`）。

## 仓库结构

```
skills/
  content-quality-gate/
  social-copywriting/
  xhs-card-design/
LICENSE
README.md
```

## 第三方与授权摘要

| 组件 | 授权 | 是否在本仓库 |
|---|---|---|
| 本仓库代码与模板 | MIT | 是 |
| rough.js（手绘模板） | MIT | 是（minified） |
| Fusion Pixel 等字体 | 各字体自身许可（多为 OFL） | **否**，只给下载说明 |
| guizang-social-card | AGPL | **否**，只给安装命令 |
| lieflat-less-ai-tone | CC BY-NC 4.0 | **否**，只给安装命令 |
| creator-buddy / xhs-html | 见上游 | **否**，只作可选外部工具提及 |

## 之后

欢迎提 Issue / PR。计划继续把其它**可开源**的社媒相关 Skill 放进本仓库；账号私有流程、平台操作脚本、个人偏好文件不会放进来。

Owner: [LAwLi3tCoding](https://github.com/LAwLi3tCoding)
