// 用法: node shoot_diagram.mjs in.html out.png  —— 把 stack-diagram 的 HTML 去网格、白底、2x 截 .canvas
import { createRequire } from 'module'
const require = createRequire(import.meta.url)
async function loadChromium() {
  if (process.env.PLAYWRIGHT_MJS) {
    return (await import(process.env.PLAYWRIGHT_MJS)).chromium
  }
  return require('playwright').chromium
}

const [,,inp,out]=process.argv
const chromium=await loadChromium()
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1400,height:1400},deviceScaleFactor:2})
await p.goto('file://'+inp);await p.addStyleTag({content:'.canvas{background-image:none!important;background:#fff!important}:root{--color-paper:#fff;--color-veil:rgba(255,255,255,.9)}'})
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500)
await (await p.$('.canvas')).screenshot({path:out});await b.close()
