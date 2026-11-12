#!/usr/bin/env python3
"""社媒成稿硬规则自查。用法:
  python3 lint_copy.py --title title.txt --body body.txt --tags tags.txt [--extra-ban 词1,词2] [--profile <偏好SKILL.md>]
  python3 lint_copy.py --text any.md            # 只扫禁用词/句式（图卡 HTML 也可传 --text）
检查: 禁用句式、自我削弱措辞、营销/AI 套话、标题 ≤20 字、正文+话题 ≤1000 字（目标 ≈900）。
字数按小红书算法: 半角字符（英文字母、数字、空格、半角标点）两个算一个字，向上取整。
--profile: 读取偏好文件里 `ban:` 开头的行（逗号分隔）追加为禁用词。全部通过退出码 0。"""
import re, sys, argparse, pathlib, math
def xlen(t): return math.ceil(sum(0.5 if ord(c) < 128 else 1 for c in t))
BANS = {
  '禁用句式(不等于/不意味着/不代表)': r'不等于|不意味着|不代表',
  '禁用句式(不是…)': r'不是',
  '禁用句式(他的思路是/他的做法是)': r'他的(思路|做法)是',
  '自我削弱措辞': r'未实测|未复现|没实测|没跑过|未验证|本机未|没验证|没测过|我们没',
  '格式化小标题/标注': r'我的判断|适用边界|^\s*边界[:：]|推断[:：]|文档没写',
  'AI/营销套话': r'总而言之|综上所述|不得不说|赋能|颠覆|炸裂|封神|必看|建议收藏|干货满满|保姆级|一文读懂|关注我|救命|破防了|绝绝子|姐妹们|宝宝们|扣1|评论区聊聊|你怎么看',
  '口语俗语': r'挺香|甩开一截|压着打',
  '第一人称过程交代': r'我读了一下|我看了下|我看了一下|这篇是我读完|这句很关键|我把.{0,12}读了一遍',
  '公文序号': r'[①②③④⑤]',
}
def scan(name, text, bans):
    bad = 0
    for k, pat in bans.items():
        for m in re.finditer(pat, text, re.M | re.I):
            line = text.count('\n', 0, m.start()) + 1
            print(f'FAIL {name}:{line} [{k}] …{text[max(0,m.start()-12):m.end()+12]}…'.replace('\n', ' ')); bad += 1
    return bad
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--title'); ap.add_argument('--body'); ap.add_argument('--tags'); ap.add_argument('--text', nargs='*', default=[])
    ap.add_argument('--extra-ban', default=''); ap.add_argument('--profile')
    ap.add_argument('--title-max', type=int, default=20); ap.add_argument('--total-max', type=int, default=1000)
    a = ap.parse_args(); bans = dict(BANS)
    extra = [w for w in a.extra_ban.split(',') if w]
    if a.profile:
        for l in pathlib.Path(a.profile).read_text().splitlines():
            if l.strip().lower().startswith('ban:'): extra += [w.strip() for w in l.split(':', 1)[1].split(',') if w.strip()]
    if extra: bans['自定义禁用'] = '|'.join(map(re.escape, extra))
    rd = lambda p: pathlib.Path(p).read_text().strip() if p else ''
    bad = 0; title, body, tags = rd(a.title), rd(a.body), rd(a.tags)
    for n, t in (('title', title), ('body', body), ('tags', tags)): bad += scan(n, t, bans)
    for p in a.text: bad += scan(p, pathlib.Path(p).read_text(), bans)
    if a.title:
        if xlen(title) > a.title_max: print(f'FAIL 标题 {xlen(title)} 字 > {a.title_max}'); bad += 1
        if title.rstrip().endswith('。'): print('FAIL 标题以中文句号结尾'); bad += 1
    if a.body:
        total = xlen(body) + (xlen(tags) + 1 if tags else 0)
        print(f'INFO 标题 {xlen(title)} 字；正文 {xlen(body)} + 话题 {xlen(tags)} = {total} 字（上限 {a.total_max}，目标 ≈900）')
        if total > a.total_max: print('FAIL 超出字数上限'); bad += 1
    print('PASS' if not bad else f'FAIL {bad}'); sys.exit(1 if bad else 0)
if __name__ == '__main__': main()
