CSS='''
*{margin:0;padding:0;box-sizing:border-box}
.story{position:relative;width:1080px;height:1920px;overflow:hidden;color:#fff;font-family:"SF Pro Display","Inter Display",sans-serif;-webkit-font-smoothing:antialiased;letter-spacing:-.02em;background:url(IMG) center/cover}
.story::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.6) 0%,rgba(0,0,0,.5) 25%,rgba(0,0,0,.66) 50%,rgba(0,0,0,.72) 75%,rgba(0,0,0,.85) 100%)}
.z{position:absolute;z-index:2}
.top{top:250px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:28px;font-weight:400;letter-spacing:-.005em}
.top .d{opacity:.7;font-weight:300}
.wrap{position:absolute;z-index:2;left:80px;right:80px;top:330px;bottom:250px;display:flex;flex-direction:column;justify-content:center}
.sec{font-size:100px;font-weight:300;letter-spacing:-.045em;line-height:1;margin-bottom:46px}
.ln{border-top:1px solid rgba(255,255,255,.35)}
.nm{font-size:52px;font-weight:400;letter-spacing:-.03em;margin:30px 0 10px}
.t{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid rgba(255,255,255,.35)}
.t>div{padding:18px 0;font-size:37px;font-weight:300;border-bottom:1px solid rgba(255,255,255,.35)}
.t>div:nth-child(2n){border-left:1px solid rgba(255,255,255,.35);padding-left:28px}
.t.c>div{text-align:center;padding-left:0!important}
ul.b.sm li{font-size:34px;padding:9px 0 9px 40px}ul.b.sm li::before{top:26px}
ul.b{list-style:none;padding:16px 0 20px}ul.b li{font-size:39px;font-weight:300;padding:12px 0 12px 40px;position:relative;line-height:1.22;color:rgba(255,255,255,.92)}
ul.b li::before{content:"";position:absolute;left:6px;top:32px;width:6px;height:6px;border-radius:50%;background:#fff;opacity:.8}
.big{font-size:96px;font-weight:300;letter-spacing:-.04em;line-height:1}
.hd{font-size:24px;font-weight:300;opacity:.75}
.sub{font-size:36px;font-weight:300;opacity:.7;margin-bottom:26px}
.rn{font-size:88px;font-weight:300;letter-spacing:-.045em;line-height:1.02;margin-bottom:12px}
.pl{font-size:30px;opacity:.75}
'''
def head(color,title,left=False):
    return f'<div class="sec">{title}</div>'
def S(cls,color,title,body,left=False):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="story"><div class="z top"><div>Silver Rain</div><div class="d">Est. 2011</div></div><div class="wrap">{head(color,title,left)}{body}</div></section></body></html>'
def mas(name,h1,h2,p1,p2):
    return f'<div class="nm">{name}</div><div class="t"><div>{h1}</div><div>{h2}</div><div>{p1}</div><div>{p2}</div></div>'
pages=[]
# packages
def pack(name,bul,pr,add):
    li=''.join(f'<li>{x}</li>' for x in bul)
    return f'<div class="rn" style="margin-top:6px">{name}</div><div class="ln"></div><ul class="b">{li}</ul><div class="ln"></div><div class="t c" style="border-top:none"><div style="border-bottom:none;padding-bottom:0;font-size:27px;opacity:.75">3 гостя / 3 часа</div><div style="border-bottom:none;padding-bottom:0;font-size:27px;opacity:.75">3 гостя / 4 часа</div><div style="font-size:42px">{pr[0]}</div><div style="font-size:42px">{pr[1]}</div></div><div class="t c" style="border-top:none"><div style="border-bottom:none;padding-bottom:0;font-size:27px;opacity:.75;padding-top:34px">Доп. гость / 3 часа</div><div style="border-bottom:none;padding-bottom:0;font-size:27px;opacity:.75;padding-top:34px">Доп. гость / 4 часа</div><div style="font-size:42px">{add[0]}</div><div style="font-size:42px">{add[1]}</div></div>'
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
        pr=f'<div class="t"><div><div style="font-size:27px;opacity:.75">{two[0][0]}</div><div style="font-size:48px;margin-top:8px;font-weight:300">{two[0][1]}</div></div><div><div style="font-size:27px;opacity:.75">{two[1][0]}</div><div style="font-size:48px;margin-top:8px;font-weight:300">{two[1][1]}</div></div></div>'
    else:
        pr=f'<div style="font-size:30px;opacity:.75;margin-top:8px">{label}</div><div class="big" style="margin-top:10px">{price}</div>'
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
IM=['couple','couple2','couple3','massage','peel1','oil','bday5','bday','baliqa1','bday3','forest','aroma','qa1','peel3','asian2']
for i,p in enumerate(pages,1):open(f'q{i:02d}.html','w').write(p.replace('IMG',IM[i-1]+'-blur.jpg'))
print(len(pages))
