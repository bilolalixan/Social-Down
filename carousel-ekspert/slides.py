# Generates carousel.html: 16 slides, 1080x1350, black background, Uzbek text.
# [g]...[/g] marks the grey (secondary) part of a sentence.
S = [
 "Hech qachon mijozni [g]ekspert ekaningizga ishontirishga urinmang.[/g]",
 "Buni havaskorlar qiladi.",
 "Ko‘pchilik kouchlar, konsultantlar va xizmat brendlari [g]vaqtini o‘zini isbotlashga sarflaydi.[/g]",
 "Ko‘proq sharhlar.<br>Ko‘proq sertifikatlar.<br>Ko‘proq unvonlar.",
 "Ularga ishonish uchun yana ko‘proq sabablar.",
 "Mijoz esa shunday o‘ylab qoladi: [g]“Shunchalik yaxshi bo‘lsa… nega meni ishontirishga buncha urinyapti?”[/g]",
 "Chunki ishonch tasdiq so‘rab yalinmaydi.",
 "U malakani namoyon qiladi.",
 "Eng yaxshi jarrohlar konsultatsiyani jarroh ekanini isbotlashga sarflamaydi.",
 "Eng yaxshi advokatlar uchrashuvni advokat ekanini isbotlashga sarflamaydi.",
 "Ular savol beradi.<br>Muammoni aniqlaydi.<br>Va tavsiya beradi.",
 "Ularning ekspertligi ko‘rinib turadi. [g]Reklama qilinmaydi.[/g]",
 "Yaxshiroq yo‘l mana bu:",
 "Ekspert ekaningizni isbotlashni bas qiling. [g]Ekspertdek harakat qiling. Agar bu rost bo‘lsa, mijoz buni sezadi.[/g]",
 "Chunki obro‘ da’vo qilinmaydi. U seziladi. [g]Premium mijozlar esa farqni ajrata oladi.[/g]",
]
CTA = ('<div class="t" style="font-size:92px">Shu kabi foydali ma’lumotlar uchun</div>'
       '<div class="t w" style="font-size:92px;margin-top:6px">sahifamga obuna bo‘ling.</div>'
       '<div class="sub">Saqlab qo‘ying va kerakli odamga ulashing.</div>')

def size(t):
    n = len(t.replace('[g]', '').replace('[/g]', ''))
    return 104 if n < 60 else 92 if n < 95 else 84

out = []
for i, t in enumerate(S, 1):
    body = t.replace('[g]', '<span class="g">').replace('[/g]', '</span>')
    out.append(f'<section class="s" id="s{i}"><div class="t" style="font-size:{size(t)}px">{body}</div>'
               f'<div class="n">{i:02d} / 16</div></section>')
out.append(f'<section class="s" id="s16"><div>{CTA}</div><div class="n">16 / 16</div></section>')

html = '''<!doctype html><html lang="uz"><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
.s{position:relative;width:1080px;height:1350px;background:#0B0B0B;color:#F2F2F2;overflow:hidden;
  display:flex;align-items:center;padding:0 80px 60px;
  font-family:"SF Pro Display","Inter Display",-apple-system,sans-serif;-webkit-font-smoothing:antialiased}
.t{font-weight:500;letter-spacing:-.045em;line-height:1.04}
.g{color:#7C7C7C}.w{color:#F2F2F2}
#s16 .t:first-child{color:#7C7C7C}
.sub{margin-top:64px;font-size:34px;font-weight:400;letter-spacing:-.01em;color:#7C7C7C}
.n{position:absolute;left:80px;bottom:72px;font-size:24px;font-weight:400;color:#6A6A6A;letter-spacing:.02em}
</style></head><body>
''' + '\n'.join(out) + '\n</body></html>\n'
open(__file__.replace('slides.py', 'carousel.html'), 'w').write(html)
