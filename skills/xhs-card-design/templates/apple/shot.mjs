// 用法: node shot.mjs <outdir>  —— 截 build/p*.html 为 0N.png，并打印溢出像素
import { createRequire } from 'module'
const require = createRequire(import.meta.url)
async function loadChromium() {
  if (process.env.PLAYWRIGHT_MJS) {
    return (await import(process.env.PLAYWRIGHT_MJS)).chromium
  }
  return require('playwright').chromium
}

import fs from 'fs'
const out=process.argv[2]||'out';fs.mkdirSync(out,{recursive:true})
const dir=new URL('build/',import.meta.url).pathname
const files=fs.readdirSync(dir).filter(f=>/^p\d+\.html$/.test(f)).sort()
const chromium=await loadChromium()
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1440}})
for(const f of files){await p.goto('file://'+dir+f);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300)
 const ov=await p.evaluate(()=>{const m=document.querySelector('.main');return [m.scrollHeight-m.clientHeight,document.getElementById('p').scrollHeight-1440]})
 const n=f.match(/\d+/)[0].padStart(2,'0');await (await p.$('#p')).screenshot({path:`${out}/${n}.png`});console.log(n,'overflow',ov)}
await b.close()
