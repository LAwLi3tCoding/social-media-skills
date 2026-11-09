#!/bin/bash
# 换机安装后运行一次：把模板里的字体占位符改成本机路径。
# 用法: FONTS_DIR=~/fonts ./relocate.sh
set -e
D=$(cd "$(dirname "$0")/.." && pwd)
FONTS_DIR=${FONTS_DIR:-${HOME}/.local/share/fonts/xhs-card-design}
PLACEHOLDER='__FONTS_DIR__'
grep -rl --include='*.html' --include='*.css' --include='*.py' --include='*.mjs' "$PLACEHOLDER" "$D/templates" \
  | xargs -r sed -i "s#${PLACEHOLDER}#${FONTS_DIR}#g"
echo "fonts -> $FONTS_DIR"
echo "Playwright: npm i playwright 后直接 node templates/*/shot.mjs；或 export PLAYWRIGHT_MJS=/path/to/playwright/index.mjs"
ls "$FONTS_DIR" >/dev/null 2>&1 || echo "WARN: $FONTS_DIR 不存在，按 SKILL.md「依赖」下载字体"
