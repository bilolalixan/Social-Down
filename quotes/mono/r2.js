const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:3});
await p.goto('file://'+process.cwd()+'/m2.html');await p.waitForTimeout(500);
await (await p.$('.s')).screenshot({path:'quote-mono-small.png'});await b.close()})();
