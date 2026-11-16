import os
from PIL import Image
P=os.getcwd()
# (id, page, y0, h, label, title, sub)
SEC=[
('home-hero','home',0,2300,'Bosh sahifa · 01','Birinchi ekran','To\'liq ekranli rasm, katta sarlavha va tugmalar: restoran muhiti birinchi soniyadan ko\'rinadi.'),
('home-menu','home',1570,2300,'Bosh sahifa · 02','Menyu bo\'limi','Rangli blok va rasm: ta\'m va hikoya bir ekranda, "Menyuni ko\'rish" tugmasi bilan.'),
('home-atm','home',3500,2300,'Bosh sahifa · 03','Atmosfera','Katta foto ustidagi shior va keyingi bo\'limga o\'tish.'),
('home-cards','home',7300,2300,'Bosh sahifa · 04','Fotokartochkalar','Bo\'limlar bo\'yicha gorizontal slayder: menyu, bar, tadbirlar.'),
('home-about','home',9300,2300,'Bosh sahifa · 05','Biz haqimizda','Yorug\' fonda foto va matn: mehmondo\'stlik haqida qisqa hikoya.'),
('home-booking','home',12550,2300,'Bosh sahifa · 06','Stolni bron qilish','Ism, telefon, sana va mehmonlar soni: forma sodda va tushunarli.'),
('menu-hero','menu',0,2300,'Menyu · 01','Menyu sahifasi','Foto-sarlavha, qisqa kirish va toifa filtri: Antipasti, Sovuq, Issiq, Paelya va boshqalar.'),
('menu-list','menu',2900,2300,'Menyu · 02','Menyu ro\'yxati','Toifalar ikki ustunda, narxlar o\'ng tomonda: kitobdek o\'qiladi.'),
('bar-lists','bar',0,2300,'Bar · 01','Bar kartasi','Kokteyllar, vino va alkogolsiz ichimliklar uch ustunda.'),
('bar-cta','bar',1850,2300,'Bar · 02','Bar atmosferasi','Vino va taom surati ustida shior: vecher kayfiyati.'),
('events-1','events',1750,2300,'Tadbirlar · 01','"Ikki kishiga kechki ovqat"','Bordo fonli blok: alohida taklif uchun maxsus dizayn.'),
('events-form','events',5300,2300,'Tadbirlar · 02','So\'rov formasi','Tadbir uchun ariza: forma foto bilan yonma-yon.'),
('gallery','gallery',1700,2300,'Galereya','Fotogalereya','Notekis to\'r: taomlar va interyer bir-biriga aralashadi.'),
('about-story','about',2700,2300,'Biz haqimizda · 01','Quadro tarixi','Sarlavha, matn va vertikal foto: "kitob sahifasi" uslubida.'),
('about-photo','about',4600,2300,'Biz haqimizda · 02','Katta fotolavha','Foto ustida manifest matni: katta kompaniyalar va oilalar uchun.'),
('contact-hero','contact',0,2300,'Aloqa · 01','Aloqa va manzil','Bordo blok: ish vaqti, manzil, telefon va elektron pochta.'),
('contact-find','contact',1800,2300,'Aloqa · 02','Xarita va yo\'l','"Bizni qanday topasiz": xarita bloki va fotolavha.'),
]
os.makedirs('sec',exist_ok=True)
for sid,pg,y0,h,*_ in SEC:
    f=Image.open(f'd-{pg}-full.png');y1=min(f.height,y0+h);f.crop((0,y0,2880,y1)).save(f'sec/{sid}.png')
CSS='''
*{margin:0;padding:0;box-sizing:border-box}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff;color:#111;font-family:"Inter Display","SF Pro Display",sans-serif;-webkit-font-smoothing:antialiased;letter-spacing:-.02em}
.dk{background:#111;color:#fff}
.tag{position:absolute;left:72px;top:64px;right:72px;display:flex;justify-content:space-between;font-size:24px;font-weight:400}
.tag span:last-child{color:#9a9a9a}.dk .tag span:last-child{color:#888}
.lbl{font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:#8a8a8a}
h1{font-weight:300;letter-spacing:-.05em;line-height:.98}
.sub{font-size:28px;font-weight:300;color:#666;line-height:1.35;margin-top:22px;max-width:860px}
.br{position:absolute;left:72px;width:936px;border-radius:20px;overflow:hidden;background:#fff;border:1px solid #d9d9d9;box-shadow:0 30px 80px rgba(0,0,0,.18)}
.br .bar{height:46px;background:#f1f1f1;display:flex;align-items:center;gap:9px;padding:0 20px;border-bottom:1px solid #e2e2e2}
.br .bar i{width:12px;height:12px;border-radius:50%;background:#c9c9c9;display:block}
.br img{display:block;width:100%}
.ph{position:absolute;width:300px;height:650px;border-radius:46px;background:#000;border:9px solid #1a1a1a;box-shadow:0 30px 70px rgba(0,0,0,.28);overflow:hidden}
.ph img{display:block;width:100%;height:100%;object-fit:cover;object-position:top}
.ph::before{content:"";position:absolute;top:10px;left:50%;transform:translateX(-50%);width:84px;height:22px;border-radius:12px;background:#000;z-index:2}
'''
def doc(body,cls=''):return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="s {cls}">{body}</section></body></html>'
N=len(SEC)+3
slides=[]
# cover
slides.append(doc(f'''<div class="tag"><span>Portfolio</span><span>01 / {N}</span></div>
<div style="position:absolute;left:72px;top:210px;right:72px"><div class="lbl">Veb-sayt · Restoran</div><h1 style="font-size:210px;margin-top:26px">Quadro</h1><div class="sub" style="font-size:40px;color:#444">Toshkentdagi ispan restorani uchun veb-sayt. Har bir bo'lim o'z uslubida.</div></div>
<div class="br" style="top:760px"><div class="bar"><i></i><i></i><i></i></div><img src="{P}/d-home-top.png"></div>'''))
for k,(sid,pg,y0,h,lb,t,sb) in enumerate(SEC,2):
    slides.append(doc(f'''<div class="tag"><span>Quadro</span><span>{k:02d} / {N}</span></div>
<div style="position:absolute;left:72px;top:140px;right:72px"><div class="lbl">{lb}</div><h1 style="font-size:96px;margin-top:20px">{t}</h1><div class="sub">{sb}</div></div>
<div class="br" style="top:520px"><div class="bar"><i></i><i></i><i></i></div><img src="{P}/sec/{sid}.png"></div>'''))
# mobile
slides.append(doc(f'''<div class="tag"><span>Quadro</span><span>{N-1:02d} / {N}</span></div>
<div style="position:absolute;left:72px;top:140px;right:72px"><div class="lbl">Mobil versiya</div><h1 style="font-size:96px;margin-top:20px">Telefonda ham o'z uslubida</h1><div class="sub">Bo'limlar telefon ekraniga moslab qayta joylashtirilgan.</div></div>
<div class="ph" style="left:46px;top:560px;transform:rotate(-4deg)"><img src="{P}/m-menu-top.png"></div><div class="ph" style="left:390px;top:520px;z-index:3"><img src="{P}/m-home-top.png"></div><div class="ph" style="left:734px;top:560px;transform:rotate(4deg)"><img src="{P}/m-contact-top.png"></div>'''))
# cta (black)
slides.append(doc(f'''<div class="tag"><span>Quadro</span><span>{N:02d} / {N}</span></div>
<div style="position:absolute;left:72px;top:330px;right:72px"><div class="lbl" style="color:#888">Sizga ham kerakmi?</div><h1 style="font-size:150px;margin-top:26px;color:#fff">Sizning biznesingizga ham shunday sayt</h1><div class="sub" style="color:#aaa;font-size:36px;margin-top:50px">Har bir bo'lim uchun alohida dizayn, mobil versiya va bron formasi.</div><div style="margin-top:60px;display:inline-block;border:2px solid #fff;border-radius:100px;padding:26px 46px;font-size:34px">@bilolalixan</div></div>''','dk'))
for i,s in enumerate(slides,1):open(f'w/s{i:02d}.html','w').write(s)
print(len(slides))
