const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();
for(const n of ['front-ru','back-ru']){
 const svg=fs.readFileSync(n+'.svg','utf8').replace(/^<\?xml[^>]*>/,'');
 const html=`<!doctype html><html><head><style>@page{size:412pt 591pt;margin:0}html,body{margin:0;background:#000}svg{display:block}</style></head><body>${svg}</body></html>`;
 const p=await b.newPage({viewport:{width:550,height:788},deviceScaleFactor:4});
 await p.setContent(html);await p.waitForTimeout(400);
 await p.pdf({path:n+'.pdf',width:'5.72222in',height:'8.20833in',printBackground:true});
 await p.screenshot({path:n+'.png',clip:{x:0,y:0,width:549.33,height:788}});
}
await b.close()})();
