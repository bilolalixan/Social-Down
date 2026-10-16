# Generates carousel.html: 14 slides, 1080x1350, pure black background, Uzbek text.
# [g]...[/g] marks the grey (secondary) part of a sentence.
USER = "@bilolalixan"
S = [
 "Hech qachon [g]ish necha soat vaqt olishini[/g] tushuntirmang.",
 "Bu katta xato, u [g]ekspertligingizni arzonroq ko‘rsatadi.[/g]",
 "Mijoz so‘raydi: “Nega bu 8&nbsp;000 dollar turadi?” Siz esa javob berasiz: “Xo‘sh, bunga taxminan 40 soatlik ish ketadi…”",
 "Siz narxni tushuntiryapman deb o‘ylaysiz. [g]Aslida esa unga kalkulyator berib qo‘yyapsiz.[/g]",
 "Chunki endi u o‘ylaydi: “8&nbsp;000 dollarni 40 soatga bo‘lsak…”",
 "Va birdan ekspertligingiz boshqasi bilan solishtirsa bo‘ladigan soatbay narxga aylanib qoladi.",
 "Premium mijozlar ish qancha vaqt olgani uchun pul to‘lamaydi. [g]Ular nima qilishni, qachon qilishni va nima uchun qilishni bilganingiz uchun to‘laydi.[/g]",
 "Aslida… qanchalik yaxshi mutaxassis bo‘lsangiz, muammoni shunchalik tez hal qila olasiz. [g]Yaxshiroq bo‘lish sizni arzonroq qilishi kerakmi?[/g]",
 "Tasavvur qiling: ekspertga muammoni bir kunda hal qilgani uchun 10&nbsp;000 dollar to‘layapsiz. Uning uch hafta ovora bo‘lishini afzal ko‘rarmidingiz?",
 "Albatta, yo‘q. Siz o‘sha bir kunni sotib olmayapsiz. Siz o‘sha kunni mumkin qilish uchun u bilishi kerak bo‘lgan hamma narsani sotib olyapsiz.",
 "Shuning uchun soatlaringizni tushuntirish ekspertlikni jazolashi mumkin. [g]Mijoz qiymatni emas, sarflangan kuchni baholay boshlaydi.[/g]",
 "Yaxshiroq yo‘l mana bu:",
 "Premium brendlar mukammallikni oldindan aniq ko‘rsatadi: aniq jarayon, aniq muddat, aniq natija. [g]Hamma qanchalik qattiq ishlagani haqida to‘xtovsiz izoh bermaydi.[/g]",
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
for i, t in enumerate(S, 1):
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
.h{margin-top:56px;font-size:46px;font-weight:600;letter-spacing:-.02em}
.sub{margin-top:18px;font-size:32px;font-weight:400;letter-spacing:-.01em;color:#7A7A7A}
.u,.n{position:absolute;bottom:72px;font-size:26px;font-weight:500;letter-spacing:-.005em}
.u{left:80px;color:#FFF}.n{right:80px;color:#5E5E5E;font-weight:400}
</style></head><body>
''' + '\n'.join(out) + '\n</body></html>\n'
open(__file__.replace('slides.py', 'carousel.html'), 'w').write(html)
