// 用法: node shot.mjs [outdir]  截 d_sketchnote / d_crayon / d_excalidraw 样张并打印溢出元素数
import { createRequire } from 'module'
const require = createRequire(import.meta.url)
async function loadChromium() {
  if (process.env.PLAYWRIGHT_MJS) {
    return (await import(process.env.PLAYWRIGHT_MJS)).chromium
  }
  return require('playwright').chromium
}

const dir=new URL('./',import.meta.url).pathname;const out=process.argv[2]||dir
const chromium=await loadChromium()
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1440}})
const L=[['sketchnote',1],['crayon',2],['excalidraw',3]]
for(const [k,n] of L){await p.goto(`file://${dir}d_${k}.html`);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(700)
 const ov=await p.evaluate(()=>{const P=document.getElementById('p').getBoundingClientRect();return [...document.querySelectorAll('.pad *')].filter(x=>{const q=x.getBoundingClientRect();return q.width&&(q.right>P.right+1||q.bottom>P.bottom+1)}).length})
 await (await p.$('#p')).screenshot({path:`${out}/d${n}_${k}.png`});console.log(k,'overflow',ov)}
await b.close()
