# Generates carousel.html: 14 slides (strategic thinking), 1080x1350, pure black background, Uzbek text.
# [g]...[/g] marks the grey (secondary) part of a sentence.
USER = "@bilolalixan"
S = [
 "Strategik fikrlash. [g]Murakkab muammolarni hal qilish, ishonarli gapirish va qat’iy harakat qilish uchun 7 bosqichli metod.[/g]",
 "1–4-bosqichlar — fikrlash. [g]O‘z nuqtai nazaringiz va strategik qadamingizni qurasiz.[/g]",
 ("Muammoni aniqlang", "Biz hal qilayotgan <i>haqiqiy</i> muammoni toping.",
  ["Ziddiyatni toping: nima ishlamayapti va nega bu muhim", "Kerak bo‘lsa, muammoni qayta shakllantiring"], "Fikrlash"),
 ("Kichik qismlarga bo‘ling", "Murakkab muammoni boshqariladigan qiling.",
  ["Muammoni bo‘laklash uchun “muammolar daraxti”dan foydalaning", "Asl sababga yetish uchun “5 marta nega?” usulini qo‘llang"], "Fikrlash"),
 ("Har bir qismni tahlil qiling", "Muammoni o‘rganing va dalil toping.",
  ["80/20, trend tahlili, benchmark kabi vositalardan foydalaning", "Natijaga eng ko‘p ta’sir qiladigan narsani toping"], "Fikrlash"),
 ("Insayt yarating", "Ma’lumotlaringizdan chuqurroq ma’no toping.",
  ["“Xo‘sh, bundan nima?” degan savolga javob bering", "Nimasi kutilmagan va boshqacha ekanini toping", "O‘z nuqtai nazaringizni shakllantiring"], "Fikrlash"),
 "5–7-bosqichlar — ta’sir qilish. [g]Ishonarli hikoya qilasiz va strategiyani hayotga tatbiq etasiz.[/g]",
 ("Hikoya tuzing", "Javobni ishonarli hikoyaga aylantiring.",
  ["Yaxshi hikoya muammo, katta g‘oya va harakatni tushuntiradi", "Sodda til va vizuallardan foydalaning"], "Ta’sir qilish"),
 ("Qaror qabul qiling", "Nimadan voz kechayotganingizni bilib, tanlov qiling.",
  ["Variantlarni aniq belgilang: har biri boshqasidan farq qilsin", "Baholash usulidan foydalaning"], "Ta’sir qilish"),
 ("Dadil harakat qiling", "Aniq fikrlash faqat harakatga olib kelsa qadrli.",
  ["Mukammallikdan ko‘ra tezlikni ustun qo‘ying", "Kichik tajribalardan boshlang", "O‘rganing va takomillashtiring"], "Ta’sir qilish"),
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
        ti, sub, bl, grp = t
        lis = ''.join(f'<li>{x}</li>' for x in bl)
        out.append(f'<section class="s" id="s{i}"><div><div class="no">{step:02d} / 07 · {grp}</div><div class="t" style="font-size:92px">{ti}</div><div class="st">{sub}</div><ul>{lis}</ul></div>{foot(i)}</section>')
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
