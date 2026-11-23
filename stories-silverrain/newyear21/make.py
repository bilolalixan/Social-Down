CSS='''*{margin:0;padding:0;box-sizing:border-box}
.story{position:relative;width:1080px;height:1920px;overflow:hidden;color:#FFF;font-family:"SF Pro Display","Inter Display",sans-serif;-webkit-font-smoothing:antialiased;background-size:cover;background-position:center}
.story::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.2) 28%,rgba(0,0,0,.2) 42%,rgba(0,0,0,.72) 62%,rgba(0,0,0,.9) 100%)}
.z{position:absolute;z-index:2}
.top{top:250px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:28px;font-weight:400;letter-spacing:-.005em}
.top .d{opacity:.7;font-weight:300}
.qtop{position:absolute;z-index:2;top:350px;left:80px;right:80px}
.qtag{display:inline-block;font-size:24px;font-weight:400;letter-spacing:.04em;padding:9px 20px;border:1.5px solid rgba(255,255,255,.6);border-radius:100px;margin-bottom:30px}
.qh{font-size:84px;font-weight:400;letter-spacing:-.04em;line-height:1.05}
.txt{left:80px;right:80px;bottom:240px}
.info{font-size:34px;font-weight:300;line-height:1.38;letter-spacing:-.01em;color:rgba(255,255,255,.9)}
.info b{font-weight:400;color:#fff}.info+.info{margin-top:26px}
.dim{color:rgba(255,255,255,.65)}
.rows{list-style:none;border-top:1px solid rgba(255,255,255,.3);margin:26px 0}
.rows li{display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding:20px 0;border-bottom:1px solid rgba(255,255,255,.3);font-size:33px;font-weight:300;line-height:1.25}
.rows li b{font-weight:400;white-space:nowrap}
.rows li.l{justify-content:flex-start}
.steps{list-style:none;counter-reset:s;margin:26px 0}.steps li{counter-increment:s;display:flex;gap:26px;padding:22px 0;border-top:1px solid rgba(255,255,255,.3);font-size:36px;font-weight:300;line-height:1.3}
.steps li::before{content:counter(s);font-weight:400;width:44px;flex:none;opacity:.7}
.steps li:last-child{border-bottom:1px solid rgba(255,255,255,.3)}
.price{font-size:80px;font-weight:400;letter-spacing:-.04em;line-height:1;margin-bottom:26px}
.price small{font-size:34px;font-weight:300;letter-spacing:-.01em;margin-left:8px;color:rgba(255,255,255,.75)}
.ph{margin-top:26px;font-size:60px;font-weight:400;letter-spacing:-.03em}
'''
def li(t,p=None): return f'<li><span>{t}</span>'+(f'<b>{p}</b>' if p else '')+'</li>'
def rows(items,cls=''): return '<ul class="rows">'+''.join(li(*(i if isinstance(i,tuple) else (i,))) for i in items)+'</ul>'
S=[]
def st(bg,title,body,tag=None,tstyle=''):
    S.append(f'<section class="story" style="background-image:url({bg}-blur.jpg)"><div class="z top"><div>Silver Rain</div><div class="d">Est. 2011</div></div><div class="qtop">'+(f'<div class="qtag">{tag}</div>' if tag else '')+f'<div class="qh" style="{tstyle}">{title}</div></div><div class="z txt">{body}</div></section>')
I=lambda t:f'<div class="info">{t}</div>'
st('anniv1','Что подарить<br>на Новый год?',I('Если вы всё ещё не нашли подарок, в этой серии расскажем, что подойдёт каждому.'))
st('curtain','Как это работает',I('Подарить очень просто:')+'<ol class="steps"><li>Выбираете</li><li>Оплачиваете</li><li>Мы доставляем красивую коробку с сертификатом</li></ol>'+I('<b>Сертификат от 750 000 сум.</b>'))
st('massage','Массаж',f'<div class="price">от 750 000<small>сум</small></div>'+I('<b>Сертификат на массаж.</b> Самый простой и доступный подарок.')+I('Какой массаж выбрать, зависит от того, кому вы дарите.'),tag='Подарок')
st('ayol','Жене, сестре, любимой',I('<b>Балийский массаж:</b> мягкий и расслабляющий')+rows([('60 мин','750 000 сум'),('90 мин','1 000 000 сум')])+I('Если дни состоят из работы, детей и домашних дел, один час будет только её.'),tag='Балийский массаж')
st('baliqa1','Маме и свекрови',I('<b>Балийский или классический массаж.</b>')+I('Спокойно, мягко, без спешки. Массаж проводят специалисты-женщины с Бали.')+I('Свекрови или тёще трудно выбрать подарок? Отдых лишним не бывает.'))
st('dark','Тем, кто мёрзнет',I('<b>Массаж горячими камнями.</b> Тёплые камни прогревают тело.')+rows([('60 мин','850 000 сум'),('90 мин','1 100 000 сум')])+I('Очень уместный зимний подарок.'),tag='Hot stones')
st('bamboo','Мужу, папе, брату',I('<b>Классический, тайский массаж или горячие камни.</b>')+I('Мужчины тоже к нам приходят. Массаж проводят специалисты-женщины.')+I('В этом году вместо галстука подарите отдых.'))
st('reading','Коллегам и руководителю',I('<b>Скромный и запоминающийся подарок.</b>')+rows([('Массаж плеч, 40 мин','600 000 сум')])+I('Понравится тем, кто много сидит за компьютером.'))
st('pool','Rituals of Bali',f'<div class="price">1 600 000<small>сум</small></div>'+I('Самый частый выбор. Всё в одной программе:')+rows(['Хаммам, сауна и бассейн','Фруктовый пилинг','Балийский массаж 60 минут','Чай'])+I('<b>2,5 часа только для себя.</b>'),tag='Программа')
st('lounge','Кому подарить',rows(['Маме','Свекрови','Подруге','Сестре','Любимому человеку'])+I('Подарок, с которым сложно ошибиться.'),tag='Rituals of Bali')
st('asian1','Asian Journey',f'<div class="price">1 850 000<small>сум</small></div>'+I('В отдельной VIP-зоне: хаммам, сауна, бассейн, гель-скраб на основе масел и массаж тела на молочке.')+I('Любимой, жене или близкой подруге: на шаг выше обычного подарка.'),tag='VIP-зона')
st('skin','Курс массажей',f'<div class="price">6 750 000<small>сум</small></div>'+I('<b>10 сеансов.</b> Не разовый, а долгий подарок.')+I('Маме, папе или себе: тем, кто любит регулярно выделять время на массаж.')+I('<span class="dim">Один сеанс выходит примерно 675 000 сум.</span>'),tag='Курс')
st('couple','Для вас двоих',f'<div class="price">3 700 000<small>сум</small></div>'+I('<b>3 часа в приватной VIP-зоне.</b> Хаммам, финская сауна и бассейн только для вас.')+I('Массаж 60 минут каждому, чай, кофе и угощения.'),tag='Для двоих')
st('couple2','Кому подарить',rows(['Мужу или жене, на годовщину','Любимому человеку','Маме и дочке вместе','Двум близким подругам'])+I('Рядом никого, телефоны можно отложить.'),tag='Для двоих')
st('couple3','He & She',f'<div class="price">5 600 000<small>сум, 3 часа</small></div>'+I('Только для пары. Самый красивый подарок:')+rows(['Скраб-эксфолиант','Массаж для мужчины','Золотое обёртывание и массаж на золотом нектаре для женщины','Уход за лицом']),tag='Для двоих')
st('anniv2','Кому подарить',rows(['На свадьбу или годовщину','Любимому человеку','Мужу, чтобы пойти вместе'])+I('Подарок, который запомнится.'),tag='He & She')
st('bday2','Для троих',I('Цена за всю компанию:')+rows([('Signature','2 200 000'),('Prestige (массаж каждому)','4 100 000'),('Imperial (скраб, массаж, мини-бар)','5 700 000')])+I('<b>Цена не за человека, а за всех троих.</b>'),tag='Для троих')
st('bday3','Кому подарить',rows(['Трём подругам','Маме и двум дочкам','Сёстрам','День рождения с подругами'])+I('Всё в отдельной зоне, только для вас.'),tag='Для троих')
st('peel1','Rituals of Sacura',f'<div class="price">6 950 000<small>сум</small></div>'+I('Для трёх женщин, на косметике Rituals.')+I('Акватермальная зона, пенный массаж, массаж тела, уход за лицом.'),tag='Для троих')
st('room','К Новому году открыто предварительное бронирование',rows([('Для одного','Массаж или Rituals of Bali'),('Для двоих','VIP-зона с массажем или He & She'),('Для троих','Prestige или Imperial')]),tstyle='font-size:70px')
st('tea','Не знаете,<br>что выбрать?',I('Напишите в Direct, кому дарите, и мы подберём.')+'<div class="ph">+998 55 518 00 77</div>')
html=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'+''.join(S)+'</body></html>'
open('ny21.html','w').write(html)
print(len(S))
