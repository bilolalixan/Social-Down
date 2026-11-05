import {createRequire} from 'module';const require=createRequire(import.meta.url);
const {chromium}=require('playwright');
const times=process.argv.slice(2).map(Number);const out=process.env.OUT||'/tmp/stills';
import fs from 'fs';fs.mkdirSync(out,{recursive:true});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:720,height:1280},deviceScaleFactor:1});
p.on('pageerror',e=>console.log('ERR',e.message));p.on('console',m=>console.log('LOG',m.text()));
await p.goto('file://'+process.cwd()+'/index.html');await p.waitForTimeout(300);
for(const t of times){await p.evaluate(t=>render(t),t);await p.screenshot({path:`${out}/t${t.toFixed(2)}.png`});}
await b.close();
