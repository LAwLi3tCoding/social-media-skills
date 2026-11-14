---
name: social-content-router
description: >-
  做 X 或小红书内容要跨多个环节时先读：从选题、实测、写作、去 AI 味、配图到交付发布的顺序，以及每一步该读哪个 skill。只做单一环节时直接读对应
  skill。
---
# 社媒内容总控

本 skill 只管顺序和分工，不重复各环节规则。个人偏好（账号、合集、口吻、禁用词扩展）一律以用户的偏好层为准（如有）；与通用 skill 冲突时偏好层胜出。

## 流水线

| 步 | 做什么 | 读哪个 skill | 出口条件（可自查） |
|---|---|---|---|
| 1 | 选题、查重、过质量门槛、实测取证 | `content-quality-gate` | 已对照已发清单；`<稿目录>/sources.md` 列出原始链接与日期；可实测项的日志在 `<稿目录>/verify/` |
| 2 | 定内容类型（常青技巧 / 工具或 Skill 测评 / 概念扫盲 / 新闻速报 / 文章解读） | `xhs-series-formats` | 稿件头部写明类型 |
| 3 | 写标题、正文、话题（X 版另写） | `social-copywriting`；X 另读 `x-posting` | `lint_copy.py` 输出 PASS |
| 4 | 去 AI 味 | `social-copywriting` §去 AI 味 | 跑过 `detect.py` 和 unslop，交付的是润色后的稿 |
| 5 | 交付文字稿给用户确认（**此时不做图**） | — | 用户明确点头 |
| 6 | 配图 | `xhs-card-design` | `check_cards.py` 输出 PASS，且逐张看过 |
| 7 | 发布小红书 / 给 X 一键链接（转述 Tips 用引用转发） | `xhs-publish`、`x-posting` | 发布后核对页面；回写合集进度文件和已发清单 |
| 8 | 盯官宣类监控（可选） | 用户自己的监控流程（如有） | 建监控前报过每天检查次数 |

## 硬规则

- 未经用户确认不发布、不代发 X；登录页、二维码、验证码、短信码一出现就停，交给用户。
- 每一步只读自己需要的 skill；任何规则只在一个 skill 里定义，其他地方只引用。
- 用户新的纠正：通用方法写进对应环节 skill，个人口味写进偏好层；不只记在记忆里。

## 可选外部包（非必需）

本机若装了 creator-buddy（`npx skills add SpaceZephyr/creator-buddy -g -y`），可借用：`space-xhs-title` 批量出标题候选、`space-xhs-writer` 正文骨架、`space-xhs-hotspot` / `xiaohongshu-search` 查热度。外部包的口吻（种草、emoji、煽情钩子）一律被 `social-copywriting` 和偏好层覆盖。`space-xhs-buddy` 的路由职责由本 skill 取代，不再单独使用。

## 自查

```bash
ls <稿目录>/sources.md <稿目录>/verify/ 2>/dev/null   # 第 1 步产物
python3 <social-copywriting>/scripts/lint_copy.py --title t.txt --body b.txt --tags g.txt --profile <偏好层>/SKILL.md
python3 <xhs-card-design>/scripts/check_cards.py cards/*.png
```
