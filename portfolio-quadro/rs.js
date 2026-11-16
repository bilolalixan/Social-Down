const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});
for(let i=1;i<=7;i++){await p.goto('file://'+process.cwd()+`/slides/s${i}.html`);await p.waitForTimeout(500);await (await p.$('.s')).screenshot({path:`slides/quadro-${i}.png`})}
await b.close()})();
