const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});
await p.goto('file://'+process.cwd()+'/q.html');await p.waitForTimeout(600);
await (await p.$('.s')).screenshot({path:'quote-glass.png'});await b.close()})();
