#!/bin/bash
# 用法：SERIES="合集名" ./new_post.sh 02   → 复制 example_post01 为 post02/，角标改成「合集名 · 02」
set -e
cd "$(dirname "$0")"
N=$1
[ -z "$N" ] && { echo "用法: SERIES=合集名 $0 <两位篇号>"; exit 1; }
SERIES=${SERIES:-示例合集}
[ -e "post$N" ] && { echo "post$N 已存在"; exit 1; }
cp -r example_post01 "post$N"
sed -i "s/示例合集 · 01/${SERIES} · $N/g" post$N/p*.html
echo "已建 post$N/：改 p1–p4.html 的文字，换 img/ 里的插图，然后 ./render.sh post$N ../post${N}_pixel"
