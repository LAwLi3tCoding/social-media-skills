#!/usr/bin/env python3
"""Render Xiaohongshu cards (1080x1440) from JSON content with HTML/CSS + headless Chrome.

Usage:
  python3 render.py content/deck.json --theme brief [--density dense|compact|normal] [--out out_dir] [--only 1,3] [--sheet]

Content schema (JSON, or YAML if PyYAML is installed):
  deck:  {series, total, source}
  cards: [{n, file, layout: cover|page, title, subtitle?, thesis?, blocks: [...]}]
Block types:
  text   {text}
  note   {text}
  list   {title?, items: [[term, desc], ...] or [str, ...]}
  group  {title?, items: [[name, desc], ...]}            # row of 2-4 boxes
  bars   {title?, max, unit?, items: [{label, sub?, value, kind: accent|muted}]}
  flow   {rows: [[{title, note?, kind: muted|plain|accent}]], arrows: [label per gap],
          bypass?: {from, to, label}, side?: {title, note, from, to}}
  table  {head: [...], rows: [[...]], hl?: col_index, widths?: [css width or null per column]}
  code   {text, lang?}
  stat   {items: [{value, label}]}
  quote  {en, zh?, who?, title?}                          # original-language quote + translation
  cols   {title?, cols: [[block, ...], [block, ...]]}      # side-by-side columns of blocks
  timeline {title?, items: [{time ('11-05\\n07:37'), title, tag?, desc?, kind: accent|solid|muted}]}
Themes: templates/themes/<theme>.css on top of templates/base.css.
"""
import argparse, html, json, os, re, subprocess, sys, tempfile, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TPL = ROOT / 'templates'
CHROME = shutil.which('google-chrome') or '/usr/bin/google-chrome'
W, H = 1080, 1440

def e(s):
    """escape + light inline markup: `code`, **strong**"""
    s = html.escape(str(s))
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'((?:https?://)?(?:github\.com|mp\.weixin\.qq\.com|x\.com)/[\w./%?=&-]+)', r'<span class="url">\1</span>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    return s

def b_text(b):  return f'<p class="b-text">{e(b["text"])}</p>'
def b_note(b):  return f'<p class="b-note">{e(b["text"])}</p>'
def b_title(b): return f'<h2 class="b-title">{e(b["title"])}</h2>' if b.get('title') else ''

def b_list(b):
    rows = []
    for it in b['items']:
        if isinstance(it, (list, tuple)):
            rows.append(f'<li><span class="term">{e(it[0])}</span><span class="desc">{e(it[1])}</span></li>')
        else:
            rows.append(f'<li class="plain"><span class="desc">{e(it)}</span></li>')
    return f'<section class="b-list">{b_title(b)}<ul>{"".join(rows)}</ul></section>'

def b_group(b):
    cells = ''.join(f'<div class="g-cell"><div class="g-name">{e(n)}</div><div class="g-desc">{e(d)}</div></div>' for n, d in b['items'])
    return f'<section class="b-group">{b_title(b)}<div class="g-row" style="--n:{len(b["items"])}">{cells}</div></section>'

def b_bars(b):
    mx = b.get('max') or max(i['value'] for i in b['items'])
    unit = b.get('unit', '')
    rows = []
    for i in b['items']:
        pct = i['value'] / mx * 100
        sub = f'<span class="bar-sub">{e(i["sub"])}</span>' if i.get('sub') else ''
        rows.append(f'<div class="bar-row k-{i.get("kind","accent")}"><div class="bar-label">{e(i["label"])}{sub}</div>'
                    f'<div class="bar-track"><div class="bar-fill" style="width:{pct:.1f}%"></div></div>'
                    f'<div class="bar-val">{i["value"]}{e(unit)}</div></div>')
    return f'<section class="b-bars">{b_title(b)}<div class="bars">{"".join(rows)}</div></section>'

def b_table(b):
    hl = b.get('hl'); ws = b.get('widths')
    cg = '<colgroup>' + ''.join(f'<col style="width:{w}">' if w else '<col>' for w in ws) + '</colgroup>' if ws else ''
    th = ''.join(f'<th{" class=hl" if j==hl else ""}>{e(h)}</th>' for j, h in enumerate(b['head']))
    trs = ''.join('<tr>' + ''.join(f'<td{" class=hl" if j==hl else ""}>{e(c)}</td>' for j, c in enumerate(r)) + '</tr>' for r in b['rows'])
    return f'<section class="b-table">{b_title(b)}<table>{cg}<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></section>'

def b_code(b):
    return f'<section class="b-code">{b_title(b)}<pre><code>{html.escape(b["text"])}</code></pre></section>'

def b_stat(b):
    cells = ''.join(f'<div class="stat"><div class="stat-v">{e(i["value"])}</div><div class="stat-l">{e(i["label"])}</div></div>' for i in b['items'])
    return f'<section class="b-stat">{b_title(b)}<div class="stats">{cells}</div></section>'

def b_flow(b):
    rows = b['rows']; arrows = b.get('arrows', [''] * (len(rows) - 1))
    parts = []
    for i, row in enumerate(rows):
        nodes = ''.join(
            f'<div class="node k-{n.get("kind","plain")}"><div class="node-t">{e(n["title"])}</div>'
            + (f'<div class="node-n">{e(n["note"])}</div>' if n.get('note') else '') + '</div>' for n in row)
        parts.append(f'<div class="f-row" data-row="{i}" style="grid-row:{2*i+1}">{nodes}</div>')
        if i < len(rows) - 1:
            lab = arrows[i] if i < len(arrows) else ''
            parts.append(f'<div class="f-arrow" style="grid-row:{2*i+2}"><i></i>{f"<span>{e(lab)}</span>" if lab else ""}</div>')
    side = b.get('side')
    if side:
        parts.append(f'<div class="f-side" style="grid-row:{2*side["from"]+1}/{2*side["to"]+2}">'
                     f'<div class="node-t">{e(side["title"])}</div><div class="node-n">{e(side["note"])}</div></div>')
    bp = b.get('bypass')
    data = f' data-bypass="{bp["from"]},{bp["to"]}" data-bypass-label="{html.escape(bp["label"])}"' if bp else ''
    cls = 'b-flow' + (' has-side' if side else '') + (' has-bypass' if bp else '')
    return f'<section class="{cls}"{data}><div class="f-grid">{"".join(parts)}</div><svg class="f-svg"></svg></section>'

def b_quote(b):
    who = f'<span class="q-who">{e(b["who"])}</span>' if b.get('who') else ''
    zh = f'<p class="q-zh">{e(b["zh"])}</p>' if b.get('zh') else ''
    return f'<section class="b-quote">{b_title(b)}<blockquote><p class="q-en">{e(b["en"])}{who}</p>{zh}</blockquote></section>'

def b_cols(b):
    cols = ''.join('<div class="c-col">' + ''.join(BLOCKS[x['type']](x) for x in col) + '</div>' for col in b['cols'])
    return f'<section class="b-cols">{b_title(b)}<div class="c-row" style="--n:{len(b["cols"])}">{cols}</div></section>'

TL_CSS = """<style>
.b-tl{margin-top:6px;font-size:25px}
.b-tl .tl-item{display:grid;grid-template-columns:150px 1fr;column-gap:22px}
.b-tl .tl-time{font-weight:700;color:#222;text-align:right;line-height:1.3;padding-top:2px}
.b-tl .tl-time small{display:block;font-size:.8em;font-weight:400;color:#8a9096}
.b-tl .tl-body{position:relative;border-left:3px solid #d5dadd;padding:0 0 .85em 30px}
.b-tl .tl-item:last-child .tl-body{border-left-color:transparent}
.b-tl .tl-dot{position:absolute;left:-11px;top:.35em;width:19px;height:19px;border-radius:50%;background:#fff;border:4px solid var(--accent);box-sizing:border-box}
.b-tl .k-muted .tl-dot{border-color:#b9bfc4}
.b-tl .k-solid .tl-dot{background:var(--accent)}
.b-tl .tl-head{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.b-tl .tl-t{font-size:1.1em;font-weight:700;color:#1a1a1a;line-height:1.35}
.b-tl .tl-tag{font-size:.72em;padding:3px 11px;border-radius:999px;background:var(--accent-soft);color:var(--accent);font-weight:600;white-space:nowrap}
.b-tl .k-muted .tl-tag{background:#f0f1f2;color:#80868b}
.b-tl .tl-d{font-size:.9em;color:#555;line-height:1.55;margin-top:6px}
.card.small-title .title{font-size:54px !important;line-height:1.2 !important}.card.small-title .subtitle{font-size:30px !important;margin-top:12px !important}.card.small-title .thesis{font-size:28px !important;margin-top:20px !important}
</style>"""
def b_timeline(b):
    items=[]
    for it in b['items']:
        t=e(it['time']).replace(chr(10),'<small>',1)+('</small>' if chr(10) in it['time'] else '')
        tag=f'<span class="tl-tag">{e(it["tag"])}</span>' if it.get('tag') else ''
        d=f'<div class="tl-d">{e(it["desc"])}</div>' if it.get('desc') else ''
        items.append(f'<div class="tl-item k-{it.get("kind","accent")}"><div class="tl-time">{t}</div><div class="tl-body"><span class="tl-dot"></span><div class="tl-head"><span class="tl-t">{e(it["title"])}</span>{tag}</div>{d}</div></div>')
    return f'{TL_CSS}<section class="b-tl">{b_title(b)}{"".join(items)}</section>'

BLOCKS = dict(timeline=b_timeline, quote=b_quote, cols=b_cols, text=b_text, note=b_note, list=b_list, group=b_group, bars=b_bars, table=b_table, code=b_code, stat=b_stat, flow=b_flow)

JS = r"""
<script>
document.fonts.ready.then(()=>{
 document.querySelectorAll('.b-flow.has-bypass').forEach(f=>{
  const [a,b]=f.dataset.bypass.split(',').map(Number);
  const svg=f.querySelector('.f-svg'), fr=f.getBoundingClientRect();
  const ra=f.querySelector(`.f-row[data-row="${a}"]`).getBoundingClientRect();
  const rb=f.querySelector(`.f-row[data-row="${b}"]`).getBoundingClientRect();
  const x0=ra.right-fr.left, x1=rb.right-fr.left, ya=ra.top+ra.height/2-fr.top, yb=rb.top+rb.height/2-fr.top;
  const rail=Math.max(x0,x1)+ (parseFloat(getComputedStyle(f).getPropertyValue('--rail'))||40);
  svg.setAttribute('width',fr.width);svg.setAttribute('height',fr.height);
  const ns='http://www.w3.org/2000/svg';
  const p=document.createElementNS(ns,'path');
  p.setAttribute('d',`M${x0} ${ya} H${rail} V${yb} H${x1+10}`);p.setAttribute('class','bp-line');svg.appendChild(p);
  const t=document.createElementNS(ns,'path');
  t.setAttribute('d',`M${x1+2} ${yb} l14 -9 v18 z`);t.setAttribute('class','bp-head');svg.appendChild(t);
  const lab=document.createElement('div');lab.className='bp-label';lab.textContent=f.dataset.bypassLabel;
  lab.style.left=(rail+14)+'px';lab.style.top=ya+'px';f.appendChild(lab);
 });
 const c=document.querySelector('.card'), m=document.querySelector('.blocks'), ft=document.querySelector('.src');
 const over = c.scrollHeight>c.clientHeight+1 || m.getBoundingClientRect().bottom > ft.getBoundingClientRect().top+1;
 let wide=[];document.querySelectorAll('.card *').forEach(el=>{if(el.scrollWidth>el.clientWidth+1&&getComputedStyle(el).overflow!=='visible')wide.push(el.className)});
 document.body.setAttribute('data-check', JSON.stringify({overflow:over, over_px:c.scrollHeight-c.clientHeight, gap: Math.round(ft.getBoundingClientRect().top-m.getBoundingClientRect().bottom)}));
 document.body.classList.add('ready');
});
</script>"""

def card_html(deck, card, theme, density='dense'):
    base = (TPL / 'base.css').read_text(); th = (TPL / 'themes' / f'{theme}.css').read_text()
    dens = TPL / 'density' / f'{density}.css'
    if density != 'normal' and dens.exists(): th += '\n' + dens.read_text()
    acc = deck.get('accent'); soft = deck.get('accent_soft')
    if acc:
        if not soft:
            h = acc.lstrip('#'); r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
            soft = '#%02x%02x%02x' % tuple(int(c + (255 - c) * 0.92) for c in (r, g, b))
        th += '\n:root{--accent:%s;--accent-soft:%s}\n' % (acc, soft)
    pg = f'{card["n"]:02d} / {deck["total"]:02d}'
    head = f'<h1 class="title">{e(card["title"]).replace(chr(10), "<br>")}</h1>'
    if card.get('subtitle'): head += f'<p class="subtitle">{e(card["subtitle"])}</p>'
    if card.get('thesis'):   head += f'<p class="thesis">{e(card["thesis"]).replace(chr(10), "<br>")}</p>'
    blocks = ''.join(BLOCKS[b['type']](b) for b in card.get('blocks', []))
    return f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><style>{base}\n{th}</style></head>
<body><div class="card layout-{card.get('layout','page')} theme-{theme} {card.get('cls','')}">
<div class="bg"></div>
<header class="run"><span class="series">{e(card.get('series', deck['series']))}</span><span class="pg">{pg}</span></header>
<div class="head">{head}</div>
<main class="blocks">{blocks}</main>
<footer class="src">{e(card.get('source', deck['source']))}</footer>
</div>{JS}</body></html>"""

def chrome(args):
    return subprocess.run([CHROME, '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                           '--force-device-scale-factor=1', f'--window-size={W},{H}', '--virtual-time-budget=3000', *args],
                          capture_output=True, text=True, timeout=90)

def render(deck, card, theme, out, density='dense'):
    out.mkdir(parents=True, exist_ok=True)
    hp = out / f'{card["file"]}.html'; hp.write_text(card_html(deck, card, theme, density))
    png = out / f'{card["file"]}.png'
    chrome([f'--screenshot={png}', hp.as_uri()])
    dom = chrome(['--dump-dom', hp.as_uri()]).stdout
    m = re.search(r"data-check=\"([^\"]*)\"", dom)
    chk = json.loads(html.unescape(m.group(1))) if m else {'overflow': None}
    flag = 'OVERFLOW!' if chk.get('overflow') else 'ok'
    print(f'{png}  [{flag}] free space above footer: {chk.get("gap")}px, overflow by {chk.get("over_px")}px')
    return png, chk

def sheet(pngs, path, label=None):
    from PIL import Image, ImageDraw, ImageFont
    s = 0.5; w, h = int(W*s), int(H*s); g = 40; top = 90 if label else g
    im = Image.new('RGB', (g + len(pngs)*(w+g), top + h + g), (228, 229, 233))
    for i, p in enumerate(pngs):
        im.paste(Image.open(p).convert('RGB').resize((w, h), Image.LANCZOS), (g + i*(w+g), top))
    if label:
        d = ImageDraw.Draw(im)
        try: f = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc', 34, index=2)
        except Exception: f = ImageFont.load_default()
        d.text((g, 26), label, font=f, fill=(30, 32, 38))
    im.save(path); print('sheet ->', path)

def load(p):
    t = Path(p).read_text()
    if p.endswith(('.yml', '.yaml')):
        import yaml; return yaml.safe_load(t)
    return json.loads(t)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('content'); ap.add_argument('--theme', default='brief'); ap.add_argument('--out')
    ap.add_argument('--only', help='comma-separated card numbers'); ap.add_argument('--sheet', action='store_true')
    ap.add_argument('--label'); ap.add_argument('--density', default='dense', help='dense (default) | compact (~70%% type, for info-heavy cards) | normal'); ap.add_argument('--accent', help='hex accent colour, overrides deck.accent')
    a = ap.parse_args()
    data = load(a.content)
    if a.accent: data['deck']['accent'] = a.accent
    out = Path(a.out or ROOT / a.theme)
    cards = data['cards']
    if a.only: keep = {int(x) for x in a.only.split(',')}; cards = [c for c in cards if c['n'] in keep]
    res = [render(data['deck'], c, a.theme, out, a.density) for c in cards]
    if a.sheet: sheet([p for p, _ in res], out / f'contact_sheet_{a.theme}.png', a.label)
    if any(c.get('overflow') for _, c in res): sys.exit(2)
