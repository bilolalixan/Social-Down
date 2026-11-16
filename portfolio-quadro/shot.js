const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();
const pages=['','events','menu','bar','gallery','about','contact'];
for(const [tag,vp,dsf,mobile] of [['d',{width:1440,height:900},2,false],['m',{width:390,height:844},3,true]]){
 const ctx=await b.newContext({viewport:vp,deviceScaleFactor:dsf,isMobile:mobile,hasTouch:mobile});const p=await ctx.newPage();
 for(const pg of pages){
  try{await p.goto('https://quadro-website-lime.vercel.app/'+pg,{waitUntil:'networkidle',timeout:45000});}catch(e){console.log('goto',pg,e.message.slice(0,60))}
  await p.waitForTimeout(1500);
  // scroll to trigger lazy/animations
  const h=await p.evaluate(async()=>{let y=0;const H=document.body.scrollHeight;while(y<H){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,250));y+=innerHeight*.7}window.scrollTo(0,0);return document.body.scrollHeight});
  await p.waitForTimeout(800);
  await p.screenshot({path:`${tag}-${pg||'home'}-top.png`});
  await p.screenshot({path:`${tag}-${pg||'home'}-full.png`,fullPage:true});
  console.log(tag,pg||'home',h)
 }
 await ctx.close()}
await b.close()})();
