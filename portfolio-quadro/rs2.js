const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});
for(const f of fs.readdirSync('w').filter(x=>x.endsWith('.html')).sort()){await p.goto('file://'+process.cwd()+'/w/'+f);await p.waitForTimeout(400);await (await p.$('.s')).screenshot({path:'w/'+f.replace('.html','.png')})}
await b.close()})();
