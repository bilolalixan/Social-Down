CSS='''
*{margin:0;padding:0;box-sizing:border-box}
.story{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:"Inter Display","SF Pro Display",sans-serif;-webkit-font-smoothing:antialiased;letter-spacing:-.02em}
.black{background:#000;color:#fff}.burg{background:#3b0402;color:#fff}.cream{background:#fffaf2;color:#0a0a0a}
.wrap{position:absolute;left:96px;right:96px;top:250px;bottom:260px;display:flex;flex-direction:column;justify-content:center}
.head{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:70px}
.head .lg{display:flex;flex-direction:column;gap:12px;align-items:flex-start}.head img{height:104px}.head span{font-size:24px;font-weight:400;letter-spacing:.03em}
.sec{font-size:104px;font-weight:400;letter-spacing:-.05em;line-height:.95;text-align:right}
.sec.l{text-align:left;font-size:92px}
.ln{border-top:1.5px solid currentColor}
.nm{font-size:56px;font-weight:400;letter-spacing:-.03em;margin:38px 0 14px}
.t{display:grid;grid-template-columns:1fr 1fr;border-top:1.5px solid currentColor}
.t>div{padding:18px 0;font-size:38px;font-weight:300;border-bottom:1.5px solid currentColor}
.t>div:nth-child(2n){border-left:1.5px solid currentColor;padding-left:30px}
.t.c>div{text-align:center;padding-left:0!important}
ul.b.sm li{font-size:37px;padding:10px 0 10px 44px}ul.b.sm li::before{top:28px}ul.b{list-style:none;padding:22px 0 26px}ul.b li{font-size:42px;font-weight:300;padding:14px 0 14px 44px;position:relative;line-height:1.22}
ul.b li::before{content:"";position:absolute;left:8px;top:36px;width:8px;height:8px;border-radius:50%;background:currentColor}
.big{font-size:108px;font-weight:300;letter-spacing:-.04em;line-height:1}
.hd{font-size:28px;font-weight:300;opacity:.75;margin-top:34px;margin-bottom:12px}
.sub{font-size:38px;font-weight:300;opacity:.7;margin-bottom:34px}
.rn{font-size:100px;font-weight:400;letter-spacing:-.045em;line-height:1;margin-bottom:14px}
'''
def head(color,title,left=False):
    return f'<div class="head"><div class="lg"><img src="logo-{color}.png"><span>SILVER RAIN</span></div><div class="sec{" l" if left else ""}">{title}</div></div>'
def S(cls,color,title,body,left=False):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="story {cls}"><div class="wrap">{head(color,title,left)}{body}</div></section></body></html>'
def mas(name,h1,h2,p1,p2):
    return f'<div class="nm">{name}</div><div class="t"><div>{h1}</div><div>{h2}</div><div>{p1}</div><div>{p2}</div></div>'
pages=[]
# packages
def pack(name,bul,pr,add):
    li=''.join(f'<li>{x}</li>' for x in bul)
    return f'<div class="rn" style="margin-top:6px">{name}</div><div class="ln"></div><ul class="b">{li}</ul><div class="ln"></div><div class="t c" style="border-top:none"><div style="border-bottom:none;padding-bottom:0;font-size:30px;opacity:.75">3 гостя / 3 часа</div><div style="border-bottom:none;padding-bottom:0;font-size:30px;opacity:.75">3 гостя / 4 часа</div><div style="font-size:46px">{pr[0]}</div><div style="font-size:46px">{pr[1]}</div></div><div class="t c" style="border-top:none"><div style="border-bottom:none;padding-bottom:0;font-size:30px;opacity:.75;padding-top:34px">Доп. гость / 3 часа</div><div style="border-bottom:none;padding-bottom:0;font-size:30px;opacity:.75;padding-top:34px">Доп. гость / 4 часа</div><div style="font-size:46px">{add[0]}</div><div style="font-size:46px">{add[1]}</div></div>'
pages.append(S('cream','black','Пакеты',pack('Signature Package',['Фирменный приветственный ритуал','Приватная VIP-зона','Изысканный выбор чая и кофе','Фирменные угощения'],['2 200 000 uzs','2 750 000 uzs'],['650 000 uzs','850 000 uzs'])))
pages.append(S('cream','black','Пакеты',pack('Prestige Package',['Фирменный приветственный ритуал','Приватная VIP-зона','Аутентичный массаж','Изысканный выбор чая и кофе','Фирменные угощения'],['4 100 000 uzs','5 200 000 uzs'],['1 250 000 uzs','1 600 000 uzs'])))
pages.append(S('cream','black','Пакеты',pack('Imperial Package',['Фирменный приветственный ритуал','Эксклюзивный выбор SPA-процедур','Изысканный выбор чая и кофе','Фирменные угощения','Премиальный мини-бар'],['5 700 000 uzs','7 200 000 uzs'],['1 800 000 uzs','2 200 000 uzs'])))
# massages short + course
m40=lambda n:mas(n,'40 min','60 min','600 000 uzs','750 000 uzs')
pages.append(S('black','white','Массажи',m40('Массаж плеч')+m40('Рефлексинг массаж')+'<div class="nm">Курсовые массажи</div><div class="t"><div>10 сеансов</div><div>6 750 000 uzs</div></div>'))
th=lambda n:f'<div class="nm">{n}</div><div class="t"><div>40 min</div><div>650 000 uzs</div></div>'
pages.append(S('black','white','Процедуры<br>хаммама',th('Кофейный пилинг')+th('Цитрусовый пилинг')+th('Пена пилинг')+th('Медовый пилинг')))
# massages 8 → 2 stories
m60=lambda n,a,b:mas(n,'60 min','90 min',a,b)
pages.append(S('black','white','Массажи',m60('Балийский массаж','750 000 uzs','1 000 000 uzs')+m60('Классический массаж','750 000 uzs','1 000 000 uzs')+m60('Ароматерапия','800 000 uzs','1 050 000 uzs')+m60('Кокосовый массаж','800 000 uzs','1 050 000 uzs')))
pages.append(S('black','white','Массажи',m60('Аутентичный массаж','750 000 uzs','1 000 000 uzs')+m60('Горячими камнями','850 000 uzs','1 100 000 uzs')+m60('Шиацу','800 000 uzs','1 050 000 uzs')+m60('Тайский массаж','800 000 uzs','1 050 000 uzs')))
# rituals
def rit(name,sub,bul,label,price,two=None):
    li=''.join(f'<li>{x}</li>' for x in bul)
    if two:
        pr=f'<div class="t"><div><div style="font-size:30px;opacity:.75">{two[0][0]}</div><div style="font-size:56px;margin-top:8px;font-weight:300">{two[0][1]}</div></div><div><div style="font-size:30px;opacity:.75">{two[1][0]}</div><div style="font-size:56px;margin-top:8px;font-weight:300">{two[1][1]}</div></div></div>'
    else:
        pr=f'<div style="font-size:32px;opacity:.75;margin-top:8px">{label}</div><div class="big" style="margin-top:10px">{price}</div>'
    return f'<div class="rn" style="margin-top:0">{name}</div><div class="sub">{sub}</div><div class="ln"></div><ul class="b{' sm' if len(bul)>6 else ''}">{li}</ul><div class="ln"></div>{pr}'
SP='SPA &amp; Beauty<br>Collection'
R=[('Rituals of Sacura','Косметика Ритуалы (для женщин)',['Акватермальная зона','Пенный массаж','Массаж тела','Уход за лицом','Зона отдыха и чайный сет'],'3 чел | VIP-зона','6 950 000 UZS'),
('Rituals of Bali','Bali tangi',['Акватермальная зона','Фруктовый пилинг','Балийский массаж','Зона отдыха и чайный сет'],'1 чел | общая зона','1 600 000 UZS'),
('Swiss Chocolate','Косметика Ритуалы (для двоих)',['Акватермальная зона','Шоколадный скраб','Массаж','Зона отдыха и чайный сет'],'2 чел | VIP-зона','4 800 000 UZS'),
('Amazonian Discovery','Germaine de Capuccini',['Акватермальная зона','Уход за лицом','Скраб-суфле для тела','Массаж тела на нектаре','Зона отдыха и чайный сет'],'2 чел | VIP-зона','4 300 000 UZS'),
('Ritual Provence','Germaine de Capuccini',['Акватермальная зона','Лавандовый скраб','Лавандовое обертывание','Массаж лаванда','Зона отдыха и чайный сет'],'2 чел | VIP-зона','4 300 000 UZS'),
('He &amp; She','Germaine de Capuccini',['Акватермальная зона (для мужчин)','Приветственный ритуал (для мужчин и женщин)','Скраб-эксфолиант для тела (для мужчин и женщин)','Массаж (для мужчин)','Золотое обертывание (для женщин)','Массаж на золотом нектаре (для мужчин и женщин)','Уход за лицом (для мужчин и женщин)','Зона отдыха и чайный сет'],'2 чел | 3 часа','5 600 000 UZS'),
('Rituals of Pomegranate','Germaine de Capuccini',['Акватермальная зона','Гранатовый скраб','Гранатовое обертывание','Массаж на креме','Зона отдыха и чайный сет'],'2 чел | VIP-зона','4 400 000 UZS'),
('Asian Journey','Germaine de Capuccini',['Акватермальная зона','Гель-скраб на основе масел','Массаж тела на молочке','Зона отдыха и чайный сет'],'','')]
for r in R:
    two=[('1 чел | VIP-зона','1 850 000 UZS'),('2 чел | VIP-зона','3 330 000 UZS')] if r[0]=='Asian Journey' else None
    pages.append(S('burg','white',SP,rit(*r,two=two),left=False))
for i,p in enumerate(pages,1):open(f'n{i:02d}.html','w').write(p)
print(len(pages))
