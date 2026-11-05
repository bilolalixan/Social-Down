import {createRequire} from 'module';const require=createRequire(import.meta.url);
const {chromium}=require('playwright');import fs from 'fs';
const [,, outDir, from, to, fps=30, dsf=1.5]=process.argv;fs.mkdirSync(outDir,{recursive:true});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:720,height:1280},deviceScaleFactor:+dsf});
p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file://'+process.cwd()+'/index.html');await p.waitForTimeout(500);
for(let i=+from;i<+to;i++){await p.evaluate(t=>render(t),i/+fps);await p.screenshot({path:`${outDir}/f${String(i).padStart(5,'0')}.jpg`,type:'jpeg',quality:95});}
await b.close();
