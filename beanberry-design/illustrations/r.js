const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1536,height:1024},deviceScaleFactor:2});
for(const f of fs.readdirSync('.').filter(x=>x.endsWith('.svg'))){await p.setContent(`<body style="margin:0">${fs.readFileSync(f,'utf8')}</body>`);await p.screenshot({path:f.replace('.svg','.png')})}
await b.close()})();
