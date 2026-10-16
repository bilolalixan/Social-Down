# Generates carousel.html: 14 slides, 1080x1350, pure black background, Uzbek text.
# [g]...[/g] marks the grey (secondary) part of a sentence.
USER = "@bilolalixan"
S = [
 "Hech qachon [g]hozirgi mijozlaringizdan[/g] shikoyat qilmang.",
 "Chunki hayotingizdagi hozirgi mijozlar tasodif emas. [g]Ular sizning aksingiz.[/g]",
 "Brendingiz yuborgan har bir signal ma’lum turdagi odamni jalb qiladi. [g]Kelayotgan odamlar esa aynan shu signalga javob beryapti.[/g]",
 "Vaqtingizni hurmat qilmaydigan mijoz [g]brendingizdagi nimadir vaqtingiz moslashuvchan ekanini aytgani uchun keldi.[/g]",
 "Har bir hisob&#8209;faktura uchun savdolashadigan mijoz [g]narxlaringizdagi nimadir ular shunchaki taklif ekanini aytgani uchun keldi.[/g]",
 "Maslahatingizni e’tiborsiz qoldiradigan mijoz [g]pozitsiyangizdagi nimadir ekspertligingiz ixtiyoriy ekanini aytgani uchun keldi.[/g]",
 "Qiyin mijozlarni omadingiz kelmagani uchun jalb qilmadingiz. [g]Ularni o‘zingizni aniq ko‘rsatmagansiz, shuning uchun jalb qildingiz.[/g]",
 "Saytingizdagi har bir so‘z. Siz rozi bo‘lgan har bir narx. Siz saqlab qolgan yoki saqlay olmagan har bir chegara.",
 "Bularning hammasi kuzatayotgan har bir kishiga jimgina uzatiladi. Ular sizga birinchi xabarni yozmasidan oldinoq sizga qanday munosabatda bo‘lish kerakligini aytib turadi.",
 "Darhol hurmat qozonadigan mutaxassisga yaxshi mijozlar shunchaki omad bilan kelmagan.",
 "U shunday brend qurganki, [g]unda hurmatsizlik o‘rinsiz tuyuladi.[/g]",
 "Chunki premium signallar premium xulq&#8209;atvorni jalb qiladi. Chegirma signallari esa chegirma xulq&#8209;atvorini jalb qiladi. Har doim.",
 "Yaxshiroq yo‘l mana bu:",
 "Mijozlaringizni o‘zgartirishdan oldin signallaringizni o‘zgartiring. [g]Narxlaringizni, bandligingizni, tilingizni va chegaralaringizni tekshirib chiqing.[/g]",
 "Chunki signallaringiz o‘zgargan zahoti [g]ularga javob beradiganlarning sifati ham o‘zgaradi.[/g]",
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
