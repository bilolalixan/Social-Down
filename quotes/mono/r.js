const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:3});
await p.goto('file://'+process.cwd()+'/m.html');await p.waitForTimeout(500);
await (await p.$('.s')).screenshot({path:'quote-mono-story.png'});await b.close()})();
