#!/bin/bash
# 用法: render_html.sh <page.html> <out.png> [WxH]   headless Chrome 截 3:4 卡片（默认 1080x1440）
set -e; WH=${3:-1080x1440}; W=${WH%x*}; H=${WH#*x}
CHROME=${CHROME:-$(command -v google-chrome || command -v chromium || command -v chromium-browser)}
"$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --allow-file-access-from-files --virtual-time-budget=4000 --window-size=$W,$H \
  --screenshot="$2" "file://$(cd "$(dirname "$1")" && pwd)/$(basename "$1")" 2>/dev/null
echo "rendered $2"
