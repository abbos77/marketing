// Генерация OG-картинок: node tools/make-og.js  (нужен Playwright)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const lang of ['ru', 'uz']) {
    const file = path.join(__dirname, `og-${lang}.html`);
    if (!require('fs').existsSync(file)) continue;
    const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
    await p.goto('file://' + file, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    await p.screenshot({ path: path.join(__dirname, `../assets/img/og-${lang}.jpg`), type: 'jpeg', quality: 86 });
    console.log('og-' + lang + '.jpg');
    await p.close();
  }
  await b.close();
})();
