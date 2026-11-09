#!/bin/bash
# 用法：./render.sh <稿件目录> <输出目录>
#   把 <稿件目录>/p1.html p2.html … 渲染成 <输出目录>/01.png 02.png …（1080×1440），然后跑留白检查
set -e
SRC=$(cd "$1" && pwd); OUT=$(mkdir -p "$2" && cd "$2" && pwd)
for f in "$SRC"/p*.html; do
  n=$(basename "$f" .html); n=${n#p}; out=$(printf "%s/%02d.png" "$OUT" "$n")
  google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
    --allow-file-access-from-files --virtual-time-budget=4000 --window-size=1080,1440 \
    --screenshot="$out" "file://$f" 2>/dev/null
  echo "rendered $out"
done
python3 "$(dirname "$0")/../../scripts/check_cards.py" "$OUT"/[0-9][0-9].png
