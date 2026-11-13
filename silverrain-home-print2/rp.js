const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();
for(const n of ['front','back']){
 const svg=fs.readFileSync(n+'-print.svg','utf8');
 const m=svg.match(/width="([\d.]+)pt" height="([\d.]+)pt"/);const w=m[1]/72,h=m[2]/72;
 const html=`<!doctype html><html><head><style>@page{size:${w}in ${h}in;margin:0}html,body{margin:0}svg{display:block}</style></head><body>${svg}</body></html>`;
 const p=await b.newPage({viewport:{width:Math.ceil(m[1]*1.34),height:Math.ceil(m[2]*1.34)},deviceScaleFactor:3});
 await p.setContent(html);await p.waitForTimeout(400);
 await p.pdf({path:n+'-print.pdf',width:w+'in',height:h+'in',printBackground:true});
 await p.screenshot({path:n+'-print.png',clip:{x:0,y:0,width:m[1]*96/72,height:m[2]*96/72}});
}
await b.close()})();
