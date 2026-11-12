#!/usr/bin/env python3
"""杂志大排版生成器。

用法:
  python3 gen.py example.json --out /tmp/cards --theme anthropic
  python3 gen.py example.json --out /tmp/cards --theme openai

内容用 JSON（见 example.json）。页型 type:
  cover     整页强调色底封面（大数字 + 三栏信息卡）
  compare   前后价格对比 + 双栏参数 + 反白横条
  bars_v    竖柱对比（可选 rest 同榜其他、blk 代价条、bracket 括号标注）
  ranking   横条榜单（上区大数字故事 + 反白横条榜）

主题 theme: anthropic | openai | google | crimson
渲染: 同目录上级 ../../scripts/render_html.sh（Chrome headless 1080×1440）
"""
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSS = (HERE / "magazine.css").read_text()
RENDER = HERE.parents[1] / "scripts" / "render_html.sh"
THEMES = ("anthropic", "openai", "google", "crimson")


def fmt(v):
    if isinstance(v, float):
        return f"{v:g}"
    return str(v)


def page(theme: str, body: str) -> str:
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head>"
        f"<body class='theme-{theme}'>{body}</body></html>"
    )


def mast(left: str, right: str) -> str:
    return f"<div class='mast'><span>{left}</span><span>{right}</span></div>"


def foot(source: str, pn: str) -> str:
    return f"<div class='pfoot'><span>{source}</span><span>{pn}</span></div>"


def cfoot(source: str, pn: str) -> str:
    return f"<div class='cfoot'><span>{source}</span><span>{pn}</span></div>"


def render_cover(p: dict, theme: str, pn: str) -> str:
    cards = "".join(
        f"<div><div class='no mono'>{c['no']}</div>"
        f"<div class='bn n'>{c['value']}</div>"
        f"<div class='tx'>{c['desc']}</div></div>"
        for c in p["cards"]
    )
    sub = p.get("giant_sub", "")
    sub_html = f"<div class='giant-sub'><div class='s serif'>{sub}</div></div>" if sub else ""
    body = f"""<div class='cov'>
{mast(p['mast_left'], p['mast_right'])}
<h1 class='serif'>{p['title']}</h1>
<div class='dek'>{p['dek']}</div>
<div class='giant n'>{p['giant']}</div>
{sub_html}
<div class='trio'>{cards}</div>
{cfoot(p['source'], pn)}
</div>"""
    return page(theme, body)


def render_compare(p: dict, theme: str, pn: str) -> str:
    rows = "".join(
        f"<div class='prow'><div class='k serif'>{r['label']}</div>"
        f"<div class='vv'><span class='old n'>{r['old']}</span>"
        f"<span class='arr'>→</span><span class='new n'>{r['new']}</span></div></div>"
        for r in p["rows"]
    )
    specs = "".join(
        f"<div><div class='bn n'>{s['value']}</div><div class='tx'>{s['label']}</div></div>"
        for s in p["specs"]
    )
    band = p.get("band")
    band_html = ""
    if band:
        band_html = (
            f"<div class='fastb'><div class='t'><b>{band['title']}</b>{band.get('sub','')}</div>"
            f"<div class='bn n'>{band['value']}</div>"
            f"<div class='pr'>{band.get('right_label','')}<b class='n'>{band.get('right_value','')}</b></div></div>"
        )
    note = p.get("note")
    note_html = ""
    if note:
        note_html = (
            f"<div class='myth'><span class='tag'>{note['tag']}</span>"
            f"<div class='tx'><b>{note['title']}</b><br>{note['body']}</div></div>"
        )
    lede = p.get("lede", "")
    body = f"""<div class='pg'>
{mast(p['mast_left'], p['mast_right'])}
<h2 class='serif big'>{p['title']}</h2>
<div class='lede'>{lede}</div>
<div class='px'>{rows}</div>
<div class='specs2'>{specs}</div>
{band_html}
{note_html}
{foot(p['source'], pn)}
</div>"""
    return page(theme, body)


def render_bars_v(p: dict, theme: str, pn: str) -> str:
    bars = p["bars"]
    mx = p.get("max") or max(b["value"] for b in bars)
    height = p.get("chart_height", 470)
    cls = "cb" if height >= 560 else "cols"
    gap_pad = "padding:0 10px" if cls == "cb" else ""
    cols = []
    names = []
    for b in bars:
        hl = b.get("hl") or b.get("style") in ("max", "hl")
        style = b.get("style", "hl" if hl else "")
        extra = f" {style}" if style else (" hl" if hl else "")
        h = b["value"] / mx * (height - 50)
        cols.append(
            f"<div class='col{extra}'><div class='v n'>{fmt(b['value'])}{b.get('unit','')}</div>"
            f"<div class='b' style='height:{h:.0f}px'></div></div>"
        )
        names.append(f"<div>{b['name']}<span>{b.get('tag','')}</span></div>")
    rest = p.get("rest") or []
    rest_html = ""
    if rest:
        items = "".join(
            f"<div><b class='n'>{fmt(r['value'])}{r.get('unit','')}</b>"
            f"{r['name']}{'（'+r['tag']+'）' if r.get('tag') else ''}</div>"
            for r in rest
        )
        rest_html = f"<div class='rest'><span class='k'>{p.get('rest_label','同榜其他')}</span>{items}</div>"
    blk = p.get("banner")
    blk_html = ""
    if blk:
        bn = f"<div class='bn n'>{blk['value']}</div>" if blk.get("value") else ""
        blk_html = f"<div class='blk'>{bn}<div class='tx'>{blk['text']}</div></div>"
    bracket = p.get("bracket")
    brk_html = f"<div class='brk'><div></div><div class='s'>{bracket}</div></div>" if bracket else ""
    hdr_no = p.get("header_no")
    if hdr_no:
        hdr = (
            f"<div class='hdr'><div class='no n'>{hdr_no}</div>"
            f"<div><h2 class='serif'>{p['title']}</h2>"
            f"<div class='s'>{p.get('subtitle','')}</div></div></div>"
        )
    else:
        hdr = f"<div class='hdr'><h2 class='serif'>{p['title']}</h2></div>"
        if p.get("subtitle"):
            hdr = (
                f"<div class='hdr'><div><h2 class='serif'>{p['title']}</h2>"
                f"<div class='s'>{p['subtitle']}</div></div></div>"
            )
    ncls = "cnames" if cls == "cb" else "names"
    body = f"""<div class='pg'>
{mast(p['mast_left'], p['mast_right'])}
{hdr}
<div class='{cls}' style='height:{height}px;{gap_pad}'>{''.join(cols)}</div>
<div class='{ncls}'>{''.join(names)}</div>
{brk_html}
{rest_html}
{blk_html}
{foot(p['source'], pn)}
</div>"""
    return page(theme, body)


def render_ranking(p: dict, theme: str, pn: str) -> str:
    """上区：大数字故事；下区：反白横条榜。"""
    top = p.get("top")
    top_html = ""
    if top:
        others = "".join(
            f"<div>{o['name']}<b class='n'>{fmt(o['value'])}{o.get('unit','')}</b></div>"
            for o in top.get("others", [])
        )
        top_html = f"""<div class='story'>
<div class='hd'><span class='no mono'>{top.get('no','01')}</span>
<span class='t'>{top['title']}</span><span class='m'>{top.get('meta','')}</span></div>
<div class='valsrow'><div class='bn n'>{fmt(top['value'])}{top.get('unit','')}</div>
<div class='tx'><b>{top['claim']}</b>{top.get('note','')}</div></div>
<div class='vg'>{others}</div></div>"""

    bars = p.get("bars") or []
    mx = p.get("max") or (max(b["value"] for b in bars) if bars else 1)
    hb = "".join(
        f"<div class='hb{' hl' if b.get('hl') else ''}'><span>{b['name']}</span>"
        f"<div class='tr'><div class='f' style='width:{b['value']/mx*100:.1f}%'></div></div>"
        f"<span class='v n'>{fmt(b['value'])}{b.get('unit','')}</span></div>"
        for b in bars
    )
    inv = p.get("inv")
    inv_html = ""
    if inv:
        inv_html = f"""<div class='inv story'>
<div class='hd'><span class='no mono'>{inv.get('no','02')}</span>
<span class='t'>{inv['title']}</span><span class='m'>{inv.get('meta','')}</span></div>
{hb}</div>"""
    elif hb:
        inv_html = f"<div class='inv story'>{hb}</div>"

    note = p.get("note")
    note_html = f"<div class='bnote' style='margin-top:28px'><b>{note['title']}</b><br>{note['body']}</div>" if note else ""

    title = p.get("title")
    title_html = f"<div class='hdr'><h2 class='serif' style='white-space:nowrap'>{title}</h2></div>" if title else ""

    body = f"""<div class='pg'>
{mast(p['mast_left'], p['mast_right'])}
{title_html}
{top_html}
{inv_html}
{note_html}
{foot(p['source'], pn)}
</div>"""
    return page(theme, body)


RENDERERS = {
    "cover": render_cover,
    "compare": render_compare,
    "bars_v": render_bars_v,
    "ranking": render_ranking,
}


def build(deck: dict, theme: str) -> dict[str, str]:
    pages = deck["pages"]
    total = len(pages)
    out = {}
    for i, p in enumerate(pages, 1):
        t = p["type"]
        if t not in RENDERERS:
            raise SystemExit(f"unknown page type: {t}")
        pn = p.get("page") or f"{i:02d}/{total:02d}"
        out[f"{i:02d}"] = RENDERERS[t](p, theme, pn)
    return out


def main():
    ap = argparse.ArgumentParser(description="杂志大排版卡片生成")
    ap.add_argument("json", help="内容 JSON（见 example.json）")
    ap.add_argument("--out", required=True, help="输出目录（写 01.png… 与 html/）")
    ap.add_argument("--theme", default="anthropic", choices=THEMES)
    ap.add_argument("--html-only", action="store_true")
    a = ap.parse_args()

    deck = json.loads(Path(a.json).read_text())
    theme = a.theme or deck.get("theme", "anthropic")
    if theme not in THEMES:
        raise SystemExit(f"theme must be one of {THEMES}")

    out = Path(a.out)
    ht = out / "html"
    ht.mkdir(parents=True, exist_ok=True)

    pages = build(deck, theme)
    for k, html in pages.items():
        hp = ht / f"{k}.html"
        hp.write_text(html)
        if a.html_only:
            print(f"wrote {hp}")
            continue
        if not RENDER.exists():
            raise SystemExit(f"render script missing: {RENDER}")
        subprocess.run(
            ["bash", str(RENDER), str(hp), str(out / f"{k}.png")],
            check=True,
        )
    print(f"done {len(pages)} pages → {out} (theme={theme})")


if __name__ == "__main__":
    main()
