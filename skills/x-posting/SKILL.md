---
name: x-posting
description: >-
  写 X（Twitter）原创、引用或回复时用：回复与引用怎么带增量、可用句式模板、发前自检、中文短帖写法，以及一键发布 intent
  链接的拼法。共用语言规则见 social-copywriting。
---
# X 原创、引用与回复

共用禁用词、去 AI 味流程见 `social-copywriting`；账号与代发约定见用户的偏好层（如已安装的 `content-profile`）。

## 回复与引用

- 不复述原帖内容或数字；写自己的观点、感想或真实体感。
- 一条只用一种增量（九种见 `content-quality-gate` §3），写完删到一两句。
- 必须有一个具体名词或数字：模型、档位、时长、钱、命令。
- 小写随意口吻可以保留；像人写的关键是观点和具体细节。
- 不写编号列表，不写总结腔；不要把长帖的列表结构套给一两句回复。
- 中文释义只给用户看，不进帖子。

可用模板（一次只用一个，填完再删字）：

- `ran this on (task) for (time), the real win was (specific), not (hyped thing)`
- `the hard part isn't (x), it's (proving/maintaining/paying for) it once (condition)`
- `makes sense if you look at the incentives: (who) gets (what) when (x), so (prediction)`
- `works great for (scenario). falls apart the moment you (condition)`
- `this is basically (old thing) again, and last time the winner was whoever (lesson)`
- `curious what (metric) looks like here. did anyone run it without (new thing)?`
- `(x) and (y) are different problems. this fixes (x), most people's pain is (y)`
- `give it (timeframe) and (specific outcome). (one-clause reason)`

## 原创

- 中文短帖：3–5 行，一行一个意思，最后一行是判断（参考 orange、歸藏的短句分行）。
- 首行写对象、动作或具体问题；有完成物先给结果；没亲测不装亲历。
- 只有多项独立动作才列点；有可核对的结果才配图或视频。
- 若偏好层写明账号是 Premium，长内容合成一条长帖，不拆 thread。
- 原创前同样对照已发清单查重（见 `content-quality-gate`）。

## 发前自检

- 带事实、数字或机制描述的原创和引用，交付前同样过第三方事实核查（流程见 `xhs-publish`「发布前」第 0 条，核查人见偏好层）。

- 删掉原帖，这条还成立吗？不成立就重写。
- 有没有 huge / wild / game changer / great post / totally agree / 🤯 / 👇 / bookmark / here's why？有就重写（大 V 对 AI 式回复零容忍，会拉黑）。

```bash
rg -n -i "huge|wild|game changer|great post|totally agree|🤯|👇|bookmark|here's why" x_draft.txt   # 应为 0 行
```

## 交付

- 每条都附 URL 编码的一键链接：`https://x.com/intent/post?text=<urlencoded>`；回复加 `&in_reply_to=<status_id>`。
- 不替用户直接发帖。

```bash
python3 -c "import urllib.parse,sys;t=open(sys.argv[1]).read().strip();print('https://x.com/intent/post?text='+urllib.parse.quote(t))" x_draft.txt
```
