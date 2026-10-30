import sys
img,out,num,title,desc,yes,no=sys.argv[1:8]
s=open('story43.html').read().replace('peel1-blur.jpg',img)
s=s.replace('</style>','''.pre{font-size:28px;font-weight:300;color:rgba(255,255,255,.75);margin-bottom:20px}
.pd{margin-top:28px;font-size:34px;font-weight:300;line-height:1.38;color:rgba(255,255,255,.9);letter-spacing:-.01em}
.yn{margin-top:32px;border-top:1px solid rgba(255,255,255,.3)}
.yn div{display:flex;gap:22px;padding:20px 0;border-bottom:1px solid rgba(255,255,255,.3);font-size:30px;font-weight:300;line-height:1.32;color:rgba(255,255,255,.9)}
.yn b{flex:0 0 190px;font-weight:400;color:#fff}
.pr{margin-top:28px;font-size:34px;font-weight:400}
.pr span{color:rgba(255,255,255,.65);font-weight:300}
</style>''')
a=s.index('<div class="z txt">'); b=s.index('</section>')
s=s[:a]+f'''<div class="z txt">
    <div class="pre">Пилинг {num} / 04</div>
    <h1><b>{title}</b></h1>
    <div class="pd">{desc}</div>
    <div class="yn"><div><b>Подойдёт</b><span>{yes}</span></div><div><b>Не&nbsp;подойдёт</b><span>{no}</span></div></div>
    <div class="pr"><span>40 мин ·</span> 650 000 сум</div>
  </div>
'''+s[b:]
open(out,'w').write(s)
