import os
P=os.getcwd()
CSS='''
*{margin:0;padding:0;box-sizing:border-box}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;background:#140c0a;color:#f4ead9;font-family:"Inter Display","SF Pro Display",sans-serif;-webkit-font-smoothing:antialiased;letter-spacing:-.02em}
.cream{background:#f4ead9;color:#2a120e}.burg{background:#4a0f12;color:#f4ead9}
.tag{position:absolute;left:72px;top:68px;right:72px;display:flex;justify-content:space-between;font-size:24px;font-weight:400;letter-spacing:.02em}
.tag span:last-child{opacity:.6}
h1{font-weight:300;letter-spacing:-.05em;line-height:.96}
.br{position:absolute;border-radius:22px;overflow:hidden;background:#000;box-shadow:0 40px 90px rgba(0,0,0,.55);border:1px solid rgba(255,255,255,.14)}
.br .bar{height:50px;background:#201512;display:flex;align-items:center;gap:9px;padding:0 20px}
.br .bar i{width:13px;height:13px;border-radius:50%;background:#5a4540;display:block}
.br .bar u{margin-left:18px;flex:1;height:28px;border-radius:14px;background:#2e201b;font-size:15px;color:#bfa99a;text-decoration:none;line-height:28px;padding-left:16px}
.br img{display:block;width:100%}
.ph{position:absolute;width:300px;height:650px;border-radius:46px;background:#000;border:9px solid #241915;box-shadow:0 40px 80px rgba(0,0,0,.6);overflow:hidden}
.ph img{display:block;width:100%;height:100%;object-fit:cover;object-position:top}
.ph::before{content:"";position:absolute;top:10px;left:50%;transform:translateX(-50%);width:84px;height:22px;border-radius:12px;background:#000;z-index:2}
.cap{position:absolute;left:72px;right:72px;bottom:70px;font-size:28px;font-weight:300;line-height:1.35}
.cap b{font-weight:500}
.num{font-size:22px;letter-spacing:.14em;opacity:.7;text-transform:uppercase}
'''
def doc(body,cls=''):return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="s {cls}">{body}</section></body></html>'
def tag(a,b):return f'<div class="tag"><span>{a}</span><span>{b}</span></div>'
def br(img,x,y,w,h=None):
    return f'<div class="br" style="left:{x}px;top:{y}px;width:{w}px"><div class="bar"><i></i><i></i><i></i><u>quadro-website-lime.vercel.app</u></div><img src="{P}/{img}"></div>'
def ph(img,x,y,rot=0,z=1):return f'<div class="ph" style="left:{x}px;top:{y}px;transform:rotate({rot}deg);z-index:{z}"><img src="{P}/{img}"></div>'
S=[]
# 1 cover
S.append(doc(tag('PORTFOLIO','Web design')+f'''
<div style="position:absolute;left:72px;top:150px;right:72px"><div class="num">Veb-sayt · Restoran</div><h1 style="font-size:190px;margin-top:22px;color:#f4ead9">Quadro</h1><div style="font-size:38px;font-weight:300;margin-top:20px;opacity:.85;max-width:760px;line-height:1.25">Toshkentdagi ispan restorani uchun veb-sayt</div></div>
{br('d-home-top.png',-60,760,1200)}
<div style="position:absolute;right:72px;bottom:60px;font-size:24px;opacity:.7">01 / 07</div>'''))
# 2 desktop hero
S.append(doc(tag('Quadro','Bosh sahifa')+f'''
<div style="position:absolute;left:72px;top:150px;right:72px"><div class="num">Birinchi taassurot</div><h1 style="font-size:92px;margin-top:18px">Birinchi ekran: restoran muhitining o'zi</h1></div>
{br('d-home-top.png',72,560,936)}
<div class="cap" style="bottom:56px">To'liq ekranli rasm, aniq sarlavha va <b>"Stolni bron qilish"</b> tugmasi.</div>'''))
# 3 mobile trio
S.append(doc(tag('Quadro','Telefon')+f'''
<div style="position:absolute;left:72px;top:150px;right:72px"><div class="num">Mobil versiya</div><h1 style="font-size:92px;margin-top:18px">Telefonda ham qulay</h1></div>
{ph('m-home-top.png',46,470,-4,1)}{ph('m-menu-top.png',390,430,0,3)}{ph('m-bar-top.png',734,470,4,1)}
<div class="cap" style="bottom:56px">Bosh sahifa · Menyu · Bar. Hammasi telefon ekraniga moslashgan.</div>'''))
# 4 home sections
S.append(doc(tag('Quadro','Bosh sahifa')+f'''
<div style="position:absolute;left:72px;top:150px;right:72px"><div class="num">Sahifa tuzilishi</div><h1 style="font-size:92px;margin-top:18px">Muhit, ta'm va hikoya</h1></div>
{br('c-home-mid.png',72,440,936)}{br('c-home-atm.png',150,900,860)}''','burg'))
# 5 pages grid
S.append(doc(tag('Quadro','Sahifalar')+f'''
<div style="position:absolute;left:72px;top:150px;right:72px"><div class="num">7 ta sahifa</div><h1 style="font-size:92px;margin-top:18px">Har bir sahifa bir uslubda</h1></div>
{br('d-events-top.png',72,470,440)}{br('d-gallery-top.png',568,470,440)}{br('d-about-top.png',72,800,440)}{br('d-contact-top.png',568,800,440)}
<div class="cap" style="bottom:56px;font-size:26px">Tadbirlar · Galereya · Biz haqimizda · Aloqa</div>'''))
# 6 menu + bar
S.append(doc(tag('Quadro','Menyu va bar')+f'''
<div style="position:absolute;left:72px;top:150px;right:72px"><div class="num">Menyu</div><h1 style="font-size:92px;margin-top:18px">Toifalar bo'yicha menyu</h1></div>
{br('d-menu-top.png',72,440,936)}{br('d-bar-top.png',150,900,860)}''','cream'))
# 7 CTA
S.append(doc(f'''<div style="position:absolute;left:72px;top:300px;right:72px"><div class="num">Sizga ham kerakmi?</div><h1 style="font-size:150px;margin-top:26px">Sizning biznesingizga ham shunday sayt</h1>
<div style="font-size:36px;font-weight:300;margin-top:50px;opacity:.85;line-height:1.3">Dizayn, mobil versiya va bron formasi bilan.</div>
<div style="margin-top:60px;display:inline-block;border:2px solid #f4ead9;border-radius:100px;padding:26px 46px;font-size:34px">@bilolalixan</div></div>
<div style="position:absolute;left:72px;bottom:70px;font-size:26px;opacity:.7">quadro-website-lime.vercel.app</div>''','burg'))
for i,s in enumerate(S,1):open(f'slides/s{i}.html','w').write(s)
