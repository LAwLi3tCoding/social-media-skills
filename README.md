# social-media-skills

Agent Skills for social media content — 给写 AI / 开发者向社媒内容的 Agent 用的一组可安装 Skill。

当前包含 7 个 Skill：

| Skill | 做什么 |
|---|---|
| `social-content-router` | 跨环节时的顺序与分工（选题 → 文案 → 配图 → 发布） |
| `content-quality-gate` | 选题过滤、已发查重、七项质量门槛、九种增量、隔离环境实测与取证 |
| `xhs-series-formats` | 七种内容类型（常青技巧、测评、扫盲、新闻、功能介绍、解读、周报）的结构 |
| `social-copywriting` | 标题 / 正文 / 话题规则、禁用句式与套话、去 AI 味流程、`lint_copy.py` |
| `x-posting` | X 原创、引用与回复的增量写法，以及一键发布 intent 链接 |
| `xhs-card-design` | 小红书 3:4 配图规划、本包十余种风格模板、HTML 渲染、`check_cards.py` 留白检查 |
| `xhs-publish` | 小红书创作服务平台发布步骤、发布前自查与发布后回写 |

English: Agent skills for drafting developer/AI social posts (route → quality gate → series format → copy lint → Xiaohongshu 3:4 cards / X post → publish). Installable via the skills CLI or by copying into your agent skills directory.

可选的账号偏好空白模板见 `profile-template/TEMPLATE.md`（填写后放在你自己的 skill 目录，例如 `content-profile`；填好的个人偏好不要提交回本仓库）。

## 安装

```bash
# 推荐：skills CLI
npx skills add LAwLi3tCoding/social-media-skills

# 或手动拷贝到 Agent 的 skills 目录（任选其一）
cp -R skills/* ~/.claude/skills/
cp -R skills/* ~/.agents/skills/
```

装好后按各目录下的 `SKILL.md` 使用。各 Skill 可单独用，也可以按 `social-content-router` 的流水线串起来。

## 依赖（按需）

- **social-content-router**、**content-quality-gate**、**xhs-series-formats**、**x-posting**、**xhs-publish**：无额外依赖（发布步骤在浏览器里操作；查重和自查会用到 shell / `rg`）。
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

本包模板包括 Apple 产品页、像素游戏、黑板、黏土、粗野撞色、复古报纸、便签墙、手绘、卡片编号、杂志大排版、研究简报，以及蜡笔 / 白板等手绘变体；并保留马卡龙手账与视觉笔记样张。模板体积已控制在较小范围。像素风字体 Fusion Pixel（OFL）需自行下载；说明见 `skills/xhs-card-design/templates/pixel/assets/fonts/OFL-fusion-pixel.txt`。手绘模板自带的 `rough.js` 为 MIT（见 `doodle/`、`handdrawn/` 目录下的 `ROUGHJS-LICENSE.txt`）。

## 仓库结构

```
skills/
  social-content-router/
  content-quality-gate/
  xhs-series-formats/
  social-copywriting/
  x-posting/
  xhs-card-design/
  xhs-publish/
profile-template/
  TEMPLATE.md
LICENSE
README.md
```

## 第三方与授权摘要

| 组件 | 授权 | 是否在本仓库 |
|---|---|---|
| 本仓库代码与模板 | MIT | 是 |
| rough.js（手绘 / 便签手绘模板） | MIT | 是（minified，附许可证） |
| Fusion Pixel 等字体 | 各字体自身许可（多为 OFL / SIL） | **否**，只给下载说明，用 `__FONTS_DIR__` 占位 |
| guizang-social-card | AGPL | **否**，只给安装命令 |
| lieflat-less-ai-tone | CC BY-NC 4.0 | **否**，只给安装命令 |
| creator-buddy / xhs-html | 见上游 | **否**，只作可选外部工具提及 |

## 之后

欢迎提 Issue / PR。账号私有流程和个人偏好文件不会放进本仓库。

Owner: [LAwLi3tCoding](https://github.com/LAwLi3tCoding)
