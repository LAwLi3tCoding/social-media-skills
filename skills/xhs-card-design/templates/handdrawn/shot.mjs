import { createRequire } from 'module'
import { fileURLToPath } from 'node:url'
import { dirname, join } from 'node:path'
const require = createRequire(import.meta.url)
async function loadChromium() {
  if (process.env.PLAYWRIGHT_MJS) {
    return (await import(process.env.PLAYWRIGHT_MJS)).chromium
  }
  return require('playwright').chromium
}
const dir = dirname(fileURLToPath(import.meta.url))
const out = process.argv[2] || dir
const chromium = await loadChromium()
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1080, height: 1440 } })
for (const name of ['01', '02']) {
  await p.goto(`file://${join(dir, name + '.html')}`)
  await p.evaluate(() => document.fonts.ready)
  await p.waitForFunction(() => document.body.dataset.done === '1', { timeout: 8000 })
  await p.waitForTimeout(200)
  const ov = await p.evaluate(() => {
    const P = document.getElementById('p').getBoundingClientRect()
    return [...document.querySelectorAll('.pad *')].filter(x => {
      const q = x.getBoundingClientRect()
      return q.width && (q.right > P.right + 1 || q.bottom > P.bottom + 1)
    }).length
  })
  await (await p.$('#p')).screenshot({ path: join(out, name + '.png') })
  console.log(name, 'overflow', ov)
}
await b.close()
