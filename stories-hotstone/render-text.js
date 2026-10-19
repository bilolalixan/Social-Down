const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + require('path').resolve('photo/stories.html'));
  await p.addStyleTag({ content: 'html,body{background:transparent!important}.story{background:none!important}.story::after{display:none!important}' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const els = await p.$$('.story');
  for (let i = 0; i < els.length; i++)
    await els[i].screenshot({ path: `photo/text-only/text-0${i + 1}.png`, omitBackground: true });
  await b.close();
})();
