#!/usr/bin/env python3
"""小红书卡片出图检查（合并旧 pixel_template/check.py 横带检查 + patrol1108 cards_v2_src/check.py 8×6 网格检查）。
用法: python3 check_cards.py <png...> [--size 1080x1440] [--mode both|band|grid]
深色大底的风格（如像素风大块夜空）网格检查易误报：先看图确认是插画/画面而非空白，再用 --mode band 复核。
判定（任一不过 → FAIL，退出码 1）:
  1. 尺寸等于 --size（默认 1080×1440，3:4）。
  2. 空白横带：整行几乎无内容的最长连续带 ≤ 画面高 8%。
  3. 8×6 网格：低信息格（灰度 std<12 且边缘密度<0.6%）的连通区，若横向连续≥2 格且面积>6% → 不合格。
另打印 16×12 细格结果作参考（不参与判定）。"""
import sys, argparse
import numpy as np
from PIL import Image

def band(im):
    med = np.median(im, axis=1, keepdims=True)
    busy = (np.abs(im - med).sum(axis=2) > 45).mean(axis=1) > 0.004
    run = best = at = 0
    for y, b in enumerate(busy):
        run = 0 if b else run + 1
        if run > best: best, at = run, y - run + 1
    return best, at

def cells(g, R, C):
    H, W = g.shape; h, w = H // R, W // C
    gy = np.abs(np.diff(g, axis=0, append=g[-1:])); gx = np.abs(np.diff(g, axis=1, append=g[:, -1:]))
    e = np.maximum(gx, gy) > 40
    low = np.zeros((R, C), bool)
    for r in range(R):
        for c in range(C):
            blk = g[r*h:(r+1)*h, c*w:(c+1)*w]
            low[r, c] = blk.std() < 12 and e[r*h:(r+1)*h, c*w:(c+1)*w].mean()*100 < 0.6
    return low

def regions(low):
    R, C = low.shape; seen = np.zeros_like(low); out = []
    for r in range(R):
        for c in range(C):
            if low[r, c] and not seen[r, c]:
                st = [(r, c)]; seen[r, c] = 1; cl = []
                while st:
                    a, b = st.pop(); cl.append((a, b))
                    for da, db in ((1,0),(-1,0),(0,1),(0,-1)):
                        x, y = a+da, b+db
                        if 0 <= x < R and 0 <= y < C and low[x, y] and not seen[x, y]:
                            seen[x, y] = 1; st.append((x, y))
                rows = {}
                for a, b in cl: rows.setdefault(a, []).append(b)
                mr = 0
                for bs in rows.values():
                    bs = sorted(bs); run = best = 1
                    for i in range(1, len(bs)):
                        run = run + 1 if bs[i] == bs[i-1] + 1 else 1; best = max(best, run)
                    mr = max(mr, best)
                out.append((len(cl), mr))
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('files', nargs='+'); ap.add_argument('--size', default='1080x1440'); ap.add_argument('--mode', choices=['both','band','grid'], default='both')
    a = ap.parse_args(); W, H = map(int, a.size.split('x')); bad = 0
    for f in sorted(a.files):
        img = Image.open(f); rgb = np.asarray(img.convert('RGB')).astype(int); g = np.asarray(img.convert('L'), dtype=np.float32)
        h, w = rgb.shape[:2]; size_ok = (w, h) == (W, H)
        b, at = band(rgb); band_ok = b / h <= 0.08
        grid = [(n, mr) for n, mr in regions(cells(g, 8, 6)) if mr >= 2 and n / 48 > 0.06]
        fine = max([n for n, _ in regions(cells(g, 16, 12))], default=0)
        ok = size_ok and (band_ok or a.mode == 'grid') and (not grid or a.mode == 'band'); bad += not ok
        print(f"{'OK  ' if ok else 'FAIL'} {f} size={w}x{h}{'' if size_ok else '(!)'} 最长空白带={b}px({b/h:.1%})@y={at}"
              f" 8x6不合格区={grid or '无'} 16x12最大低信息连通={fine}/192")
    print('PASS' if not bad else f'FAIL {bad}')
    sys.exit(1 if bad else 0)

if __name__ == '__main__': main()
