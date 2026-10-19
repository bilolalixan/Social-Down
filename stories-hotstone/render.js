const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [,, html, outDir, prefix] = process.argv;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + require('path').resolve(html));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const els = await p.$$('.story');
  for (let i = 0; i < els.length; i++) {
    await els[i].screenshot({ path: `${outDir}/${prefix}-${String(i + 1).padStart(2, '0')}.png` });
  }
  await b.close();
  console.log('rendered', els.length);
})();
