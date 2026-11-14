const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});let o=[];
for(let i=1;i<=15;i++){const f=String(i).padStart(2,'0');await p.goto('file://'+process.cwd()+`/q${f}.html`);
o.push(f+':'+await p.evaluate(()=>{const w=document.querySelector('.wrap');return w.scrollHeight+'/'+w.clientHeight}))}console.log(o.join(' '));await b.close()})();
