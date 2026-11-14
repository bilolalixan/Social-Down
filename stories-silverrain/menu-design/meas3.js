const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(let i=1;i<=15;i++){const f=String(i).padStart(2,'0');await p.goto('file://'+process.cwd()+`/n${f}.html`);
const h=await p.evaluate(()=>{const w=document.querySelector('.wrap');let t=1e9,bm=0;[...w.children].forEach(c=>{const r=c.getBoundingClientRect();t=Math.min(t,r.top);bm=Math.max(bm,r.bottom)});return [Math.round(t),Math.round(bm)]});console.log(f,h.join('-'))}
await b.close()})();
