const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:2});const p=await ctx.newPage();
const pages=[['home',''],['about','about'],['services','services'],['packages','packages'],['prestige','packages/prestige'],['booking','booking'],['contact','contact'],['blog','blog'],['bali','services/bali-massage'],['sacura','services/ritual-sacura']];
const out={};
for(const [n,u] of pages){
 await p.goto('https://www.silverrain.asia/'+u,{waitUntil:'networkidle',timeout:45000}).catch(()=>{});
 await p.waitForTimeout(1200);
 await p.evaluate(async()=>{let y=0;const H=document.body.scrollHeight;while(y<H){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,250));y+=innerHeight*.6}await new Promise(r=>setTimeout(r,1500));window.scrollTo(0,0)});
 await p.addStyleTag({content:'[class*=fixed],[style*="position: fixed"]{display:none!important}header{position:absolute!important}'});
 await p.waitForTimeout(800);
 const secs=await p.evaluate(()=>[...document.querySelectorAll('main > section, main > div > section, section')].filter(s=>s.offsetHeight>250&&!s.closest('section section')).map(s=>({y:Math.round(s.getBoundingClientRect().top+scrollY),h:s.offsetHeight,t:(s.innerText||'').slice(0,50).replace(/\n/g,' | ')})));
 out[n]=secs;
 await p.screenshot({path:`${n}-clean.png`,fullPage:true});
 console.log(n,secs.length);secs.forEach((s,i)=>console.log(' ',i,s.y,s.h,s.t));
}
require('fs').writeFileSync('secs.json',JSON.stringify(out));
await b.close()})();
