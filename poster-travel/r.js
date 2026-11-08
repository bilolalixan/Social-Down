const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1200,height:1700}});
await pg.goto('file://'+process.cwd()+'/p.html');await pg.waitForTimeout(500);
for(const [id,n] of [['a','poster-1'],['b','poster-2']]){await (await pg.$('#'+id)).screenshot({path:n+'.jpg',type:'jpeg',quality:95});}
await b.close()})();
