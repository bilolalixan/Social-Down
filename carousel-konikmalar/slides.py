# Generates carousel.html: 14 slides (5 skills for the AI era), 1080x1350, pure black background, Uzbek text.
# [g]...[/g] marks the grey (secondary) part of a sentence.
USER = "@bilolalixan"
S = [
 "Sun’iy intellekt davrida muvaffaqiyat uchun kerak bo‘ladigan [g]5 ta asosiy ko‘nikma[/g]",
 "Forbes Future of Work sammitida rahbarlar shu ko‘nikmalarni qayta&#8209;qayta tilga olishdi. [g]Qaysi yo‘nalishda rivojlanish kerakligini ko‘ring.[/g]",
 ("Mulohaza qilish", "Nimaga ustuvorlik berishni bilish javobni bilishdan muhimroq.",
  "Sun’iy intellekt ma’lumot olishni osonlashtirgani sari, avvalo nima ustida ishlashni hal qila olish insonni ajratib turadigan asosiy farqqa aylanmoqda."),
 ("Tanqidiy fikrlash", "Sun’iy intellekt ko‘proq narsa yaratib bera oladi. Qaysi biri qilishga arzishini baribir siz hal qilasiz.",
  "Indeed va BetterUp kompaniyalari tanqidiy fikrlashsiz unumdorlik shunchaki ko‘proq sifatsiz ish chiqarishga olib kelishini ta’kidlashdi."),
 ("Ijodkorlik", "Hammada bir xil vositalar bo‘lganda, original fikrlash yanada qimmatli bo‘ladi.",
  "Sun’iy intellekt oddiy aqliy ishlarni ommalashtirgani sari ijodkorlik eng qadrli qobiliyatlardan biriga aylanmoqda."),
 ("Moslashuvchanlik", "Bugungi ishingiz ikki yildan keyin boshqacha bo‘lishi mumkin.",
  "Lavozimlar va vazifalar tez o‘zgarib borar ekan, tez o‘rganish, chaqqonlik va doimiy rivojlanish muhim ahamiyatga ega."),
 ("Odamlar bilan ishlash", "Vazifalar qanchalik ko‘p avtomatlashtirilsa, insoniy muloqot shunchalik muhim bo‘ladi.",
  "Muloqot, hamkorlik, yetakchilik va munosabatlar qurish — texnologiya osonlikcha o‘rnini bosa olmaydigan ko‘nikmalar."),
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
        ti, q, ex = t
        out.append(f'<section class="s" id="s{i}"><div class="big">{step}</div><div style="position:relative"><div class="no">{step:02d} / 05</div><div class="t" style="font-size:92px">{ti}</div><div class="q">{q}</div><div class="ex">{ex}</div></div>{foot(i)}</section>')
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
.q{margin-top:40px;font-size:56px;font-weight:500;letter-spacing:-.035em;line-height:1.1;color:#FFF}
.ex{margin-top:48px;padding-top:36px;border-top:1px solid #2A2A2A;font-size:34px;font-weight:400;letter-spacing:-.015em;line-height:1.35;color:#7A7A7A}
.big{position:absolute;right:40px;top:-60px;font-size:720px;font-weight:600;letter-spacing:-.06em;line-height:1;color:#121212}
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
