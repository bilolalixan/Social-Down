const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:2});
await p.goto('file://'+process.cwd()+'/qs.html');await p.waitForTimeout(600);
await (await p.$('.s')).screenshot({path:'quote-glass-story.png'});await b.close()})();
