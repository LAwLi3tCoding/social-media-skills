"""Apple 产品页风小红书卡片生成器。改 PAGES 内容 → python3 gen.py → node shot.mjs <outdir>"""
import json,os
CSS=open(os.path.join(os.path.dirname(__file__),'apple.css')).read()
TAG="示例合集 · 02"; TOTAL=7; SRC="github.com/caru-ini/stack-diagram"
EXTRA={}
def page(n,body,credit):
    return f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS}{EXTRA.get(n,'')}</style></head><body><div id=p>
<div class=top><span class=tag>{TAG}</span><span class=pn>{n:02d} / {TOTAL:02d}</span></div>
<div class=main>{body}</div>
<div class=foot><span>{credit}</span><span class=link>{SRC}</span></div></div></body></html>'''
def head(eb,title,sub='',cls=''): return f'<header class="hd {cls}"><div class=eb>{eb}</div><h1>{title}</h1>'+(f'<p class=sub>{sub}</p>' if sub else '')+'</header>'
def stage(img,cap,w=''): return f'<section class=stage><div class=shot style="{w}"><img src="assets/{img}"></div><div class=cap>{cap}</div></section>'
def specs(items,cols=4,big=False): return f'<div class="specs{" big" if big else ""}" style="grid-template-columns:repeat({cols},1fr)">'+''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in items)+'</div>'
def cols(items): return '<div class=cols>'+''.join(f'<div><h4>{a}</h4><p>{b}</p></div>' for a,b in items)+'</div>'
def rows(items): return '<ol class=rows>'+''.join(f'<li><span class=no>{i+1:02d}</span><div><h4>{a}</h4><p>{b}</p></div></li>' for i,(a,b) in enumerate(items))+'</ol>'
CAP="图：stack-diagram 自带脚本 + 模板生成"
P={}
P[1]=(head('开源 Agent Skill　stack-diagram','一句话，画出<br><span class=g>带官方 Logo</span><br>的架构图','跟 Claude Code、Codex 或 Cursor 说一句你的技术栈，它画出一张带官方 Logo 的架构图。','cover')
 +stage('java.png','示例　Java 后端')
 +'<p class=line>本期 3 张示例图：Java 后端 · Python 后端 · AI Agent 开发栈</p>'
 +specs([('MIT','开源协议'),('2000+','GitHub star'),('0','API Key'),('HTML','也能出 PNG')],big=True),CAP)
P[2]=(head('工作原理','它的流程','从拉 Logo 到看图返修，一共五步。')
 +rows([('拉 Logo','<code>fetch_icons.py</code> 依次查 svgl → devicon → gilbarbara/logos，查不到就去项目仓库找官方文件。'),
  ('Agent 算坐标','按 <code>geometry.md</code> 的间距规则，算好每个节点、分组框和箭头的位置，填进自带 HTML 模板。'),
  ('build 打包','<code>build.py</code> 把图标和字体内联，得到一个离线可用的 HTML。'),
  ('Playwright 截图','<code>render_png.py</code> 用无头 Chromium 截成 PNG，浅色、深色各一张。'),
  ('看图返修','Agent 检查截图：箭头压字、图标看不清，就改坐标重画。')])
 +specs([('HTML','默认输出'),('PNG','浅色 / 深色'),('离线','图标字体内联')],cols=3),'来源：skills/stack-diagram/SKILL.md')
P[3]=(head('示例 1','Java 后端','Spring Boot + MySQL + Redis + Kafka + Nginx + Docker + Kubernetes')
 +stage('java.png','FIG.1　7 个官方 Logo 全部自动拉到')
 +specs([('Nginx','反向代理'),('Spring Boot','API 服务'),('Kafka','事件流'),('Spring Boot','消费服务'),('MySQL','主库'),('Redis','缓存'),('Docker','镜像构建'),('Kubernetes','编排集群')])
 +cols([('画的是','用户经 Nginx 到 Spring Boot API，写 MySQL、读写 Redis 缓存，事件经 Kafka 交给消费服务；整组跑在 Kubernetes 里，Docker 负责打镜像。'),('怎么读','蓝色实线是主请求链路，灰线是内部调用，虚线是构建/部署。')]),CAP)
P[4]=(head('示例 2','Python 后端','FastAPI + PostgreSQL + Celery + Redis + Nginx + Docker Compose')
 +stage('python.png','FIG.2　Docker Compose 编排的异步任务栈','width:88%')
 +specs([('Nginx','反向代理'),('FastAPI','异步 API'),('Redis','消息代理'),('Celery','任务 worker'),('PostgreSQL','主库'),('Compose','编排')],cols=3)
 +cols([('画的是','请求经 Nginx 到 FastAPI，任务通过 Redis 投给 Celery worker，FastAPI 和 Celery 都写 PostgreSQL，整体用 Docker Compose 编排。'),('Logo 怎么来','Celery 三个图标源都查不到，按它的规则改用 Celery 仓库里的官方图片。每张图还会同时出一张深色版。')]),CAP)
P[5]=(head('示例 3','AI Agent 开发栈')
 +cols([('上半部分 · 开发时','Claude Code、Codex 两个 coding agent，通过 MCP 连 GitHub 和 PostgreSQL。'),('下半部分 · 上线后','LangGraph Agent 应用，调 Claude / OpenAI API，Qdrant 检索，Langfuse 追踪。')])
 +stage('agent.png','FIG.3　开发时与上线后画在同一张图里','width:72%')
 +'<p class=warn><b>Logo 不全</b>　LangGraph 用的是 LangChain 的标；Codex 和 OpenAI API 是同一个 Logo。</p>',CAP)
P[6]=(head('安装与使用','怎么装，怎么用')
 +rows([('安装','Claude Code、Codex、Cursor 等支持 Skill 的 Agent：<pre>npx skills add caru-ini/stack-diagram</pre>'),
  ('使用','直接说一句技术栈，比如 README 里的例子：<pre class=lt>Diagram our stack: Next.js and a Hono API on Vercel. Postgres on Neon, auth with Clerk, payments with Stripe.</pre>'),
  ('环境','Python 3.9+；拉 Logo 要联网；出 PNG 要 Playwright + Chromium。不需要 API Key。')])
 +specs([('HTML','默认'),('PNG','浅色 / 深色'),('TSX','React 组件'),('云图标','AWS / GCP / Azure')]),'来源：README / SKILL.md')
P[7]=(head('写在最后','适合谁，要注意什么')
 +'<div class=pair><div><div class=eb2>适合</div><p>写技术方案<br>做分享 PPT<br>给 README 配架构图</p></div><div class=muted><div class=eb2>不太需要</div><p>随手画草图<br>白板工具更快</p></div></div>'
 +rows([('不是一句话秒出图','坐标是 Agent 一个个算的，第一版可能标签压线，要截图检查后返修。'),('图越大越费 token','节点和箭头越多，Agent 要算、要改的就越多。'),('新 AI 工具 Logo 不全','后端常见组件基本齐；Celery 要手动指定图片，LangGraph 借 LangChain 的标，Codex 和 OpenAI 撞标。')]),'来源：README / SKILL.md')
EXTRA[2]='.rows p{font-size:25px}.rows li{padding:26px 0}'
EXTRA[6]='h1{font-size:100px}.hd{margin-bottom:14px}.rows li{padding:36px 0}.rows h4{font-size:40px;margin-bottom:12px}.rows p{font-size:30px}pre{font-size:30px;padding:24px 28px}pre.lt{font-size:25px}.specs b{font-size:34px}.specs span{font-size:23px}.specs div{padding:22px 8px}'
EXTRA[7]='h1{font-size:96px}.pair>div{padding:36px 38px}.pair p{font-size:38px}.eb2{font-size:28px}.rows li{padding:38px 0}.rows h4{font-size:40px}.rows p{font-size:30px}'
os.makedirs('build',exist_ok=True)
for n,(b,c) in P.items(): open(f'build/p{n}.html','w').write(page(n,b,c).replace('src="assets/','src="../assets/'))
