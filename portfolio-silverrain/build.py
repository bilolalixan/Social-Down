import os,json
from PIL import Image
P=os.getcwd()
SC=2
# (id, file, y0, y1, label, title, sub)
SEC=[
('hero','home-clean.png',0,830,'Bosh sahifa · 01','Birinchi ekran','Aksiya va "Onlayn yozilish" tugmasi: mehmon birinchi soniyadayoq harakatga chaqiriladi.'),
('services','home-clean.png',830,1509,'Bosh sahifa · 02','Xizmatlar ro\'yxati','Toifa filtri va uch ustunli ro\'yxat: massaj, ritual va paketlar bir joyda.'),
('cert','home-clean.png',1509,2561,'Bosh sahifa · 03','Sovg\'a sertifikati','To\'q bordo blok: sertifikat uchun alohida dizayn va tayyor takliflar kartalari.'),
('why','home-clean.png',2561,3851,'Bosh sahifa · 04','Nega aynan biz','Foto va raqamlardan iborat bento-to\'r: tajriba, reyting, atmosfera.'),
('offer','home-clean.png',4848,5484,'Bosh sahifa · 05','Maxsus taklif','Bordo fonda bitta aniq taklif: bepul birinchi konsultatsiya.'),
('reviews','home-clean.png',5484,6177,'Bosh sahifa · 06','Mijozlar fikri','Reyting 4.9 va haqiqiy sharhlar slayderi.'),
('faq','home-clean.png',6177,6814,'Bosh sahifa · 07','Savol-javoblar','Ochiladigan savollar va yonida rasm: ishonch uchun.'),
('about1','about-clean.png',68,860,'Biz haqimizda · 01','Brend hikoyasi','Foto ustida sarlavha va "Yozilish" tugmasi.'),
('about2','about-clean.png',1021,2053,'Biz haqimizda · 02','Yillar va raqamlar','Tarix: 2011-yildan beri, 20 000+ mehmon, vaqt chizig\'i.'),
('about3','about-clean.png',2053,3207,'Biz haqimizda · 03','Missiya va jamoa','Tamoyillar va mutaxassislar bo\'limi.'),
('about4','about-clean.png',3207,4134,'Biz haqimizda · 04','Makon galereyasi','Filial bo\'yicha filtr bilan interyer fotolari.'),
('svc','services-clean.png',68,1000,'Xizmatlar','Xizmatlar katalogi','Filial va toifa bo\'yicha filtrlar, narxli ro\'yxat.'),
('pack','packages-clean.png',68,1371,'Paketlar','SPA-paketlar','Filial tanlash, kartochkalar va "Prestige" paketi ajratib ko\'rsatilgan.'),
('book','booking-clean.png',68,1270,'Bron qilish','Onlayn yozilish','Protsedura yoki sertifikat, filial, ism va telefon: bitta sahifada.'),
('contact','contact-clean.png',72,1633,'Aloqa','Filiallar va xarita','Har bir filial uchun manzil, telefon, ish vaqti va xarita.'),
('detail','bali-clean.png',140,1214,'Xizmat sahifasi','Alohida xizmat sahifasi','Tavsif, afzalliklar va tegishli boshqa xizmatlar.'),
]
os.makedirs('sec',exist_ok=True)
from PIL import Image
for sid,fn,a,b,*_ in SEC:
    im=Image.open(fn);im.crop((0,int(a*SC),2880,min(im.height,int(b*SC)))).save(f'sec/{sid}.png')
Image.MAX_IMAGE_PIXELS=None
CSS='''
*{margin:0;padding:0;box-sizing:border-box}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff;color:#111;font-family:"Inter Display","SF Pro Display",sans-serif;-webkit-font-smoothing:antialiased;letter-spacing:-.02em}
.dk{background:#111;color:#fff}
.tag{position:absolute;left:72px;top:64px;right:72px;display:flex;justify-content:space-between;font-size:24px}
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
N=len(SEC)+4
sl=[]
sl.append(doc(f'''<div class="tag"><span>Portfolio</span><span>01 / {N}</span></div>
<div style="position:absolute;left:72px;top:210px;right:72px"><div class="lbl">Veb-sayt · Spa-markaz</div><h1 style="font-size:190px;margin-top:26px">Silver Rain</h1><div class="sub" style="font-size:40px;color:#444">Toshkentdagi premium spa-markaz uchun veb-sayt. Har bir bo'lim o'z uslubida.</div></div>
<div class="br" style="top:780px"><div class="bar"><i></i><i></i><i></i></div><img src="{P}/sec/hero.png"></div>'''))
for k,(sid,fn,a,b,lb,t,sb) in enumerate(SEC,2):
    sl.append(doc(f'''<div class="tag"><span>Silver Rain</span><span>{k:02d} / {N}</span></div>
<div style="position:absolute;left:72px;top:140px;right:72px"><div class="lbl">{lb}</div><h1 style="font-size:96px;margin-top:20px">{t}</h1><div class="sub">{sb}</div></div>
<div class="br" style="top:520px"><div class="bar"><i></i><i></i><i></i></div><img src="{P}/sec/{sid}.png"></div>'''))
k=len(SEC)+2
sl.append(doc(f'''<div class="tag"><span>Silver Rain</span><span>{k:02d} / {N}</span></div>
<div style="position:absolute;left:72px;top:140px;right:72px"><div class="lbl">Mobil versiya</div><h1 style="font-size:96px;margin-top:20px">Telefonda ham o'z uslubida</h1><div class="sub">Bo'limlar telefon ekraniga moslab qayta joylashtirilgan.</div></div>
<div class="ph" style="left:46px;top:560px;transform:rotate(-4deg)"><img src="{P}/mc-services.png"></div><div class="ph" style="left:390px;top:520px;z-index:3"><img src="{P}/mc-home.png"></div><div class="ph" style="left:734px;top:560px;transform:rotate(4deg)"><img src="{P}/mc-booking.png"></div>'''))
sl.append(doc(f'''<div class="tag"><span>Silver Rain</span><span>{N-1:02d} / {N}</span></div>
<div style="position:absolute;left:72px;top:140px;right:72px"><div class="lbl">Ritual sahifasi</div><h1 style="font-size:96px;margin-top:20px">Har bir ritual uchun alohida sahifa</h1><div class="sub">Rituals of Sacura: tarkib, afzalliklar va narx bir ekranda.</div></div>
<div class="br" style="top:560px"><div class="bar"><i></i><i></i><i></i></div><img src="{P}/sec/ritual.png"></div>'''))
sl.append(doc(f'''<div class="tag"><span>Silver Rain</span><span>{N:02d} / {N}</span></div>
<div style="position:absolute;left:72px;top:330px;right:72px"><div class="lbl" style="color:#888">Sizga ham kerakmi?</div><h1 style="font-size:150px;margin-top:26px;color:#fff">Sizning biznesingizga ham shunday sayt</h1><div class="sub" style="color:#aaa;font-size:36px;margin-top:50px">Har bir bo'lim uchun alohida dizayn, mobil versiya va onlayn bron. Murojaat uchun Direct'ga yozing.</div><div style="margin-top:60px;display:inline-block;border:2px solid #fff;border-radius:100px;padding:26px 46px;font-size:38px"><span style="opacity:.6;font-size:26px;margin-right:16px">Direct</span>@odex.asia</div></div>''','dk'))
os.makedirs('w',exist_ok=True)
for i,s in enumerate(sl,1):open(f'w/s{i:02d}.html','w').write(s)
print(len(sl))
