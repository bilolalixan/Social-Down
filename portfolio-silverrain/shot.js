const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();
const pages=process.argv.slice(2);const fails=new Set();
for(const [tag,vp,dsf,mob] of [['d',{width:1440,height:900},2,false],['m',{width:390,height:844},3,true]]){
 const ctx=await b.newContext({viewport:vp,deviceScaleFactor:dsf,isMobile:mob,hasTouch:mob});const p=await ctx.newPage();
 p.on('requestfailed',r=>{try{fails.add(new URL(r.url()).host)}catch(e){}});
 for(const pg of pages){
  const name=pg===''?'home':pg.replace(/\//g,'_');
  try{await p.goto('https://www.silverrain.asia/'+pg,{waitUntil:'networkidle',timeout:45000})}catch(e){console.log('goto',pg,e.message.slice(0,50))}
  await p.waitForTimeout(1500);
  const h=await p.evaluate(async()=>{let y=0;const H=document.body.scrollHeight;while(y<H){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,300));y+=innerHeight*.6}await new Promise(r=>setTimeout(r,1500));window.scrollTo(0,0);return document.body.scrollHeight});
  await p.waitForTimeout(1000);
  await p.screenshot({path:`${tag}-${name}-top.png`});
  await p.screenshot({path:`${tag}-${name}-full.png`,fullPage:true});
  console.log(tag,name,h)}
 await ctx.close()}
console.log('failed:',[...fails].join(' '));
await b.close()})();
