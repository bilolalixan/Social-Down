# Generates carousel.html: 14 slides (strategic thinking), 1080x1350, pure black background, Uzbek text.
# [g]...[/g] marks the grey (secondary) part of a sentence.
USER = "@bilolalixan"
S = [
 "Fikringiz tumanli bo‘lsa, [g]strategiyangiz ham tumanli bo‘ladi.[/g]",
 "Aniqlik — [g]sizning eng katta ustunligingiz.[/g]",
 "Muhim qarorlarda asosiy muammo — “tuman”: [g]noaniq maqsadlar, bir&#8209;biriga zid fikrlar, cheksiz yig‘ilishlar va hech qanday natija yo‘q.[/g]",
 "Aniq fikrlaydiganlar bu tumanni yorib o‘tadi. [g]Ular tartibsizlikka tartib beradi va ishni oldinga siljitadigan qarorlar qabul qiladi.[/g]",
 "Mana buni 7 bosqichda qanday qilish mumkin:",
 ("Muammoni aniqlang", "Aniq belgilanmagan muammoni hal qilib bo‘lmaydi.",
  ["So‘rang: biz aynan qanday muammoga duch kelyapmiz?", "Noaniq maqsadlarni aniq ziddiyatlarga aylantiring", "Muammoni boshqalar bilan sinovdan o‘tkazing"]),
 ("Kichik qismlarga bo‘ling", "Katta muammolar murakkablik ichida yashirinadi.",
  ["“Muammolar daraxti” yoki “5 marta nega?” usulidan foydalaning", "Eng muhim qismlarni birinchi o‘ringa qo‘ying", "Asl sabablarni yuzaki belgilardan ajrating"]),
 ("Har bir qismni tahlil qiling", "Taxmin qilmang, dalilga tayaning.",
  ["Ma’lumotlar, trendlar va xatti&#8209;harakatlarga qarang", "To‘siqlar, bo‘shliqlar va g‘ayrioddiy holatlarni toping", "So‘rang: buni nima harakatlantiryapti va nima o‘zgardi?"]),
 ("Insayt yarating", "Umumlashtirish faktlarni ma’noga aylantiradi.",
  ["Har bir topilmadan keyin “Xo‘sh, bundan nima?” deb so‘rang", "Ko‘rinmaydigan cheklovlarni yuzaga chiqaring", "Nima qilish kerakligi haqida aniq nuqtai nazar shakllantiring"]),
 ("Hikoya tuzing", "Strategiya boshqalar tushunsagina foydali.",
  ["Uni “muammo → katta g‘oya → harakat” ko‘rinishida tuzing", "Auditoriyangizga moslashtiring", "Sodda, tartibli va esda qoladigan qiling"]),
 ("Qaror qabul qiling", "Mukammal vaqtni kutmang.",
  ["Nimadan voz kechayotganingizni aniq belgilang", "O‘zingiz uchun mantiqli mezonlar asosida tanlang", "Ishonch bilan qaror qiling"]),
 ("Dadil harakat qiling", "Ijrosiz fikrlash hech narsa emas.",
  ["Tez va aniq yo‘naltirilgan tajribalardan boshlang", "Silliqlikdan ko‘ra o‘rganishni ustun qo‘ying", "Ishonch uyg‘otadigan, ko‘zga ko‘rinadigan g‘alabalar yarating", "O‘rganing va takomillashtiring"]),
 "Aniq fikrlash — bu super kuch. [g]Fikringizni tartibga soling, aniq gapiring va odamlarni harakatga undang.[/g]",
]
CTA = ('<div class="t g" style="font-size:92px">Shu kabi foydali ma’lumotlar uchun</div>'
       '<div class="t" style="font-size:92px;margin-top:6px">sahifamga obuna bo‘ling.</div>'
       f'<div class="h">{USER}</div>'
       '<div class="sub">Saqlab qo‘ying va kerakli odamga ulashing.</div>')
N = len(S) + 1

def size(t):
    n = len(t.replace('[g]', '').replace('[/g]', ''))
    return 104 if n < 60 else 92 if n < 100 else 82

def foot(i):
    return f'<div class="u">{USER}</div><div class="n">{i:02d} / {N}</div>'

out = []
step = 0
for i, t in enumerate(S, 1):
    if isinstance(t, tuple):
        step += 1
        ti, sub, bl = t
        lis = ''.join(f'<li>{x}</li>' for x in bl)
        out.append(f'<section class="s" id="s{i}"><div><div class="no">{step:02d} / 07</div><div class="t" style="font-size:92px">{ti}</div><div class="st">{sub}</div><ul>{lis}</ul></div>{foot(i)}</section>')
        continue
    body = t.replace('[g]', '<span class="g">').replace('[/g]', '</span>')
    out.append(f'<section class="s" id="s{i}"><div class="t" style="font-size:{size(t)}px">{body}</div>{foot(i)}</section>')
out.append(f'<section class="s" id="s{N}"><div>{CTA}</div>{foot(N)}</section>')

html = '''<!doctype html><html lang="uz"><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
.s{position:relative;width:1080px;height:1350px;background:#000;color:#FFF;overflow:hidden;
  display:flex;align-items:center;padding:0 80px 60px;
  font-family:"SF Pro Display","Inter Display",-apple-system,sans-serif,"Noto Color Emoji";-webkit-font-smoothing:antialiased}
.t{font-weight:500;letter-spacing:-.045em;line-height:1.04}
.g{color:#7A7A7A}
.no{font-size:30px;font-weight:500;color:#7A7A7A;letter-spacing:-.005em;margin-bottom:28px}
.st{margin-top:24px;font-size:46px;font-weight:500;letter-spacing:-.03em;line-height:1.12;color:#7A7A7A}
ul{list-style:none;margin-top:64px;border-top:1px solid #2A2A2A}
li{font-size:36px;font-weight:400;letter-spacing:-.015em;line-height:1.25;padding:26px 0 26px 44px;border-bottom:1px solid #2A2A2A;position:relative}
li::before{content:"—";position:absolute;left:0;color:#5E5E5E}
.h{margin-top:56px;font-size:46px;font-weight:600;letter-spacing:-.02em}
.sub{margin-top:18px;font-size:32px;font-weight:400;letter-spacing:-.01em;color:#7A7A7A}
.u,.n{position:absolute;bottom:72px;font-size:26px;font-weight:500;letter-spacing:-.005em}
.u{left:80px;color:#FFF}.n{right:80px;color:#5E5E5E;font-weight:400}
</style></head><body>
''' + '\n'.join(out) + '\n</body></html>\n'
open(__file__.replace('slides.py', 'carousel.html'), 'w').write(html)
