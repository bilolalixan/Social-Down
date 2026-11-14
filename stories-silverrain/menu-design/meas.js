const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const i of [1,2,3,4,5,6,7]){await p.goto('file://'+process.cwd()+`/m${i}.html`);const h=await p.evaluate(()=>{const c=document.getElementById('c');if(c){const r=c.getBoundingClientRect();return [r.top,r.bottom]}
 const w=[...document.querySelectorAll('.story>div')].filter(d=>!d.classList.contains('logo')).map(d=>d.getBoundingClientRect().bottom);return ['abs',Math.max(...w)]});console.log(i,h)}
await b.close()})();
