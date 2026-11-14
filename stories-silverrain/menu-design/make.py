import os
CSS='''
*{margin:0;padding:0;box-sizing:border-box}
.story{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:"Inter Display","SF Pro Display",sans-serif;-webkit-font-smoothing:antialiased;letter-spacing:-.02em;padding:0 80px}
.black{background:#000;color:#fff}.burg{background:#3b0402;color:#fff}.cream{background:#fffaf2;color:#0a0a0a}
.logo{position:absolute;left:80px;display:flex;flex-direction:column;align-items:flex-start;gap:14px}
.logo img{height:150px;display:block}.logo span{font-size:26px;font-weight:400;letter-spacing:.02em}
h1{font-weight:400;letter-spacing:-.05em;line-height:.98}
.ln{border-top:1.5px solid currentColor}
.t2{display:grid;grid-template-columns:1fr 1fr}
.t2>div{padding:14px 0 14px 0;font-size:28px;font-weight:300;border-bottom:1.5px solid currentColor}
.t2>div:nth-child(2n){border-left:1.5px solid currentColor;padding-left:22px}
.t2 .p{font-size:28px;font-weight:300}
.t1{display:grid;grid-template-columns:1fr 1fr;border-top:1.5px solid currentColor}
.t1>div{padding:14px 0;font-size:28px;font-weight:300;border-bottom:1.5px solid currentColor}
.t1>div:nth-child(2n){border-left:1.5px solid currentColor;padding-left:22px}
.nm{font-size:38px;font-weight:400;margin-top:34px;margin-bottom:12px;letter-spacing:-.02em}
.sub{font-size:28px;font-weight:300;opacity:.7;margin:-6px 0 18px}
ul.b{list-style:none;padding:14px 0 16px}ul.b li{font-size:27px;font-weight:300;padding:9px 0 9px 28px;position:relative;line-height:1.2}
ul.b li::before{content:"";position:absolute;left:6px;top:21px;width:5px;height:5px;border-radius:50%;background:currentColor}
.pl{font-size:25px;font-weight:300;margin-top:16px;padding-left:18px}
.pr{font-size:58px;font-weight:300;letter-spacing:-.03em;padding:6px 0 22px 18px;border-bottom:1.5px solid currentColor}
.pk{position:relative}
.hd{font-size:21px;font-weight:300;text-align:center}
'''
def fit(html,Z,top,left=80):
    return f'<div id="c" style="position:absolute;top:{top}px;left:{left}px;width:{(1080-2*left)/Z}px;transform:scale({Z});transform-origin:0 0">{html}</div>'
def logo(color,top=None,bottom=None):
    st=f'top:{top}px' if top is not None else f'bottom:{bottom}px'
    return f'<div class="logo" style="{st}"><img src="logo-{color}.png"><span>SILVER RAIN</span></div>'
def story(cls,body,css_extra=''):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{css_extra}</style></head><body><section class="story {cls}">{body}</section></body></html>'
def tbl(a,b,c,d):
    return f'<div class="t1"><div>{a}</div><div>{b}</div><div>{c}</div><div>{d}</div></div>'
def massage(name,h1,h2,p1,p2):
    return f'<div class="nm">{name}</div>'+tbl(h1,h2,p1,p2)
# ---------- 1: Пакеты (cream)
def pack(name,bul,pr,add):
    li=''.join(f'<li>{x}</li>' for x in bul)
    return f'''<div style="margin-top:38px;border-top:1.5px solid #0a0a0a;padding-top:6px;position:relative">
<div style="font-size:50px;font-weight:400;letter-spacing:-.03em;margin:8px 0 8px">{name}</div>
<div style="display:grid;grid-template-columns:430px 1fr;column-gap:24px;align-items:start;margin-top:-4px">
<ul class="b" style="padding-top:18px">{li}</ul>
<div>
<div style="display:grid;grid-template-columns:1fr 1fr;text-align:center">
<div class="hd" style="padding:2px 0 10px">3 гостя / 3 часа</div><div class="hd" style="padding:2px 0 10px">3 гостя / 4 часа</div></div>
<div class="t3"><div>{pr[0]}</div><div>{pr[1]}</div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;text-align:center">
<div class="hd" style="padding:10px 0 8px">Доп. гость / 3 часа</div><div class="hd" style="padding:10px 0 8px">Доп. гость / 4 часа</div></div>
<div class="t3"><div>{add[0]}</div><div>{add[1]}</div></div></div></div></div>'''
extra1='.t3{display:grid;grid-template-columns:1fr 1fr;border-top:1.5px solid #0a0a0a;border-bottom:1.5px solid #0a0a0a}.t3>div{padding:18px 0;font-size:27px;font-weight:300;text-align:center}.t3>div:nth-child(2){border-left:1.5px solid #0a0a0a}.story{padding:0 70px}'
S1=story('cream',f'''<div class="logo" style="top:150px;left:70px"><img src="logo-black.png" style="height:130px"><span>SILVER RAIN</span></div>
<h1 style="position:absolute;top:190px;left:560px;font-size:118px">Пакеты</h1>
<div id="c" style="position:absolute;top:410px;left:70px;width:{940/1.08}px;transform:scale(1.08);transform-origin:0 0">
{pack('Signature Package',['Фирменный приветственный ритуал','Приватная VIP-зона','Изысканный выбор чая и кофе','Фирменные угощения'],['2 200 000 uzs','2 750 000 uzs'],['650 000 uzs','850 000 uzs'])}
{pack('Prestige Package',['Фирменный приветственный ритуал','Приватная VIP-зона','Аутентичный массаж','Изысканный выбор чая и кофе','Фирменные угощения'],['4 100 000 uzs','5 200 000 uzs'],['1 250 000 uzs','1 600 000 uzs'])}
{pack('Imperial Package',['Фирменный приветственный ритуал','Эксклюзивный выбор SPA-процедур','Изысканный выбор чая и кофе','Фирменные угощения','Премиальный мини-бар'],['5 700 000 uzs','7 200 000 uzs'],['1 800 000 uzs','2 200 000 uzs'])}
</div>''',extra1)
# ---------- 2: Массажи + хаммам (black)
def tm(n):return massage(n,'40 min','60 min','600 000 uzs','750 000 uzs')
def th(n):return f'<div class="nm">{n}</div><div class="t1"><div>40 min</div><div>650 000 uzs</div></div>'
S2=story('black',fit(f'''<h1 style="font-size:120px">Массажи</h1><div style="margin-top:20px">{tm('Массаж плеч')}{tm('Рефлексинг массаж')}<div class="nm">Курсовые массажи</div><div class="t1"><div>10 сеансов</div><div>6 750 000 uzs</div></div></div>
<h1 style="font-size:120px;margin-top:70px">Процедуры<br>хаммама</h1><div style="margin-top:6px">{th('Кофейный пилинг')}{th('Цитрусовый пилинг')}{th('Пена пилинг')}{th('Медовый пилинг')}</div>''',0.9,120)+logo('white',bottom=100))
# ---------- 3: Массажи (black, 8)
def m2(n,a,b):return massage(n,'60 min','90 min',a,b)
S3=story('black',f'''<h1 style="position:absolute;top:140px;font-size:112px">Массажи</h1>
<div style="position:absolute;top:310px;left:80px;right:80px">
{m2('Балийский массаж','750 000 uzs','1 000 000 uzs')}{m2('Классический массаж','750 000 uzs','1 000 000 uzs')}{m2('Ароматерапия','800 000 uzs','1 050 000 uzs')}{m2('Кокосовый массаж','800 000 uzs','1 050 000 uzs')}{m2('Аутентичный массаж','750 000 uzs','1 000 000 uzs')}{m2('Горячими камнями','850 000 uzs','1 100 000 uzs')}{m2('Шиацу','800 000 uzs','1 050 000 uzs')}{m2('Тайский массаж','800 000 uzs','1 050 000 uzs')}</div>''','.nm{margin-top:24px;margin-bottom:8px;font-size:36px}.t1>div{padding:11px 0;font-size:26px}')
# ---------- SPA pages
def ritual(name,sub,bul,label,price,two=None):
    li=''.join(f'<li>{x}</li>' for x in bul)
    if two:
        pr=f'<div class="t1" style="border-top:1.5px solid currentColor;margin-top:6px"><div style="border-bottom:1.5px solid currentColor;padding-left:0"><div style="font-size:24px;font-weight:300">{two[0][0]}</div><div style="font-size:42px;font-weight:300;margin-top:6px">{two[0][1]}</div></div><div style="border-bottom:1.5px solid currentColor"><div style="font-size:24px;font-weight:300">{two[1][0]}</div><div style="font-size:42px;font-weight:300;margin-top:6px">{two[1][1]}</div></div></div>'
    else:
        pr=f'<div class="ln" style="margin-top:6px"></div><div class="pl">{label}</div><div class="pr">{price}</div>'
    return f'<div class="nm" style="font-size:54px;margin-top:0;margin-bottom:8px;letter-spacing:-.03em">{name}</div><div class="sub">{sub}</div><div class="ln"></div><ul class="b">{li}</ul>{pr}'
extraS='.nm{}'
def spa(a,b,Z=1.2,tt=150):
    return story('burg',f'''<h1 style="position:absolute;top:{tt}px;font-size:112px;left:80px">SPA &amp; Beauty<br>Collection</h1><div class="logo" style="top:{tt+6}px;left:auto;right:80px;align-items:center"><img src="logo-white.png" style="height:118px"><span style="font-size:22px">SILVER RAIN</span></div>'''+fit(f'{a}<div style="height:56px"></div>{b}',Z,tt+270))
S4=spa(ritual('Rituals of Sacura','Косметика Ритуалы (для женщин)',['Акватермальная зона','Пенный массаж','Массаж тела','Уход за лицом','Зона отдыха и чайный сет'],'3 чел | VIP-зона','6 950 000 UZS'),
       ritual('Rituals of Bali','Bali tangi',['Акватермальная зона','Фруктовый пилинг','Балийский массаж','Зона отдыха и чайный сет'],'1 чел | общая зона','1 600 000 UZS'))
S5=spa(ritual('Swiss Chocolate','Косметика Ритуалы (для двоих)',['Акватермальная зона','Шоколадный скраб','Массаж','Зона отдыха и чайный сет'],'2 чел | VIP-зона','4 800 000 UZS'),
       ritual('Amazonian Discovery','Germaine de Capuccini',['Акватермальная зона','Уход за лицом','Скраб-суфле для тела','Массаж тела на нектаре','Зона отдыха и чайный сет'],'2 чел | VIP-зона','4 300 000 UZS'))
S6=spa(ritual('Ritual Provence','Germaine de Capuccini',['Акватермальная зона','Лавандовый скраб','Лавандовое обертывание','Массаж лаванда','Зона отдыха и чайный сет'],'2 чел | VIP-зона','4 300 000 UZS'),
       ritual('He &amp; She','Germaine de Capuccini',['Акватермальная зона (для мужчин)','Приветственный ритуал (для мужчин и женщин)','Скраб-эксфолиант для тела (для мужчин и женщин)','Массаж (для мужчин)','Золотое обертывание (для женщин)','Массаж на золотом нектаре (для мужчин и женщин)','Уход за лицом (для мужчин и женщин)','Зона отдыха и чайный сет'],'2 чел | 3 часа','5 600 000 UZS'),Z=1.08,tt=110)
S7=spa(ritual('Rituals of Pomegranate','Germaine de Capuccini',['Акватермальная зона','Гранатовый скраб','Гранатовое обертывание','Массаж на креме','Зона отдыха и чайный сет'],'2 чел | VIP-зона','4 400 000 UZS'),
       ritual('Asian Journey','Germaine de Capuccini',['Акватермальная зона','Гель-скраб на основе масел','Массаж тела на молочке','Зона отдыха и чайный сет'],'', '',two=[('1 чел | VIP-зона','1 850 000 UZS'),('2 чел | VIP-зона','3 330 000 UZS')]))
for i,s in enumerate([S1,S2,S3,S4,S5,S6,S7],1):open(f'm{i}.html','w').write(s)
