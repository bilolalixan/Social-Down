import {createRequire} from 'module';const require=createRequire(import.meta.url);
const {chromium}=require('playwright');import fs from 'fs';
const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+process.cwd()+'/index.html');
const s=await p.evaluate(()=>window.__SFX);fs.writeFileSync(process.argv[2],JSON.stringify(s));console.log(s.length);await b.close();
