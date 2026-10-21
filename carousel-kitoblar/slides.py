# Generates carousel.html: 8 slides, 1080x1350, black background, Uzbek text.
# Slide 1 and the CTA use the big-headline style; list slides use a compact layout.
USER = "@bilolalixan"
SECTIONS = [
 ("Startap asoslari", "1–20",
  "G‘oyani tekshirish, mahsulot yaratish, mijozlarni tushunish va barqaror biznes qurishni o‘rganing.",
  ["The Lean Startup|Eric Ries","Zero to One|Peter Thiel","The Mom Test|Rob Fitzpatrick",
   "The Startup Owner's Manual|Steve Blank & Bob Dorf","Business Model Generation|Alexander Osterwalder & Yves Pigneur",
   "Disciplined Entrepreneurship|Bill Aulet","Rework|Jason Fried & David Heinemeier Hansson","The $100 Startup|Chris Guillebeau",
   "Crossing the Chasm|Geoffrey A. Moore","The Innovator's Dilemma|Clayton M. Christensen","Blue Ocean Strategy|W. Chan Kim & Renée Mauborgne",
   "Running Lean|Ash Maurya","Value Proposition Design|Alexander Osterwalder et al.","Founders at Work|Jessica Livingston",
   "Inspired|Marty Cagan","Start Small, Stay Small|Rob Walling","The Startup Playbook|David S. Kidder","Little Bets|Peter Sims",
   "The Innovator's Solution|Clayton Christensen & Michael Raynor","Sprint|Jake Knapp et al."],
  "Muvaffaqiyatli biznes siz hal qilayotgan muammoni tushunishdan, talabni tekshirishdan va mijozlar chin dildan qadrlaydigan narsani yaratishdan boshlanadi."),
 ("Sotuv va marketing", "21–40",
  "Mijozlarni jalb qilish, qadringizni yetkazish, mijozlar oqimini yaratish va taniqli brend qurishni o‘rganing.",
  ["Building a StoryBrand|Donald Miller","Contagious|Jonah Berger","Influence|Robert Cialdini","Purple Cow|Seth Godin",
   "This Is Marketing|Seth Godin","Traction|Gabriel Weinberg & Justin Mares","Hooked|Nir Eyal","$100M Offers|Alex Hormozi",
   "$100M Leads|Alex Hormozi","Obviously Awesome|April Dunford","The Challenger Sale|Matthew Dixon & Brent Adamson",
   "SPIN Selling|Neil Rackham","Fanatical Prospecting|Jeb Blount","Pitch Anything|Oren Klaff","To Sell Is Human|Daniel H. Pink",
   "Positioning|Al Ries & Jack Trout","Made to Stick|Chip Heath & Dan Heath","Ogilvy on Advertising|David Ogilvy",
   "Hacking Growth|Sean Ellis & Morgan Brown","Predictable Revenue|Aaron Ross & Marylou Tyler"],
  "Ajoyib mahsulotning o‘zi yetarli emas. Uning qadrini yetkazish, to‘g‘ri mijozlarga yetib borish va e’tiborni barqaror daromadga aylantirishni bilish kerak."),
 ("Pul va moliyaviy boshqaruv", "41–60",
  "Pul oqimi, rentabellik, investitsiya, biznesni baholash va uzoq muddatli o‘sishga ta’sir qiladigan qarorlarni tushuning.",
  ["Profit First|Mike Michalowicz","Venture Deals|Brad Feld & Jason Mendelson","Secrets of Sand Hill Road|Scott Kupor",
   "The Psychology of Money|Morgan Housel","Financial Intelligence|Karen Berman & Joe Knight","Financial Statements|Thomas Ittelson",
   "The Art of Startup Fundraising|Alejandro Cremades","The Power Law|Sebastian Mallaby","The Intelligent Investor|Benjamin Graham",
   "The Essays of Warren Buffett|Lawrence A. Cunningham","The Little Book of Common Sense Investing|John C. Bogle",
   "Rich Dad Poor Dad|Robert Kiyosaki","The Simple Path to Wealth|JL Collins","The Millionaire Fastlane|MJ DeMarco",
   "Unscripted|MJ DeMarco","Money: Master the Game|Tony Robbins","Monetizing Innovation|Madhavan Ramanujam & Georg Tacke",
   "The Richest Man in Babylon|George S. Clason","The Millionaire Next Door|Thomas J. Stanley & William D. Danko","Die With Zero|Bill Perkins"],
  "Muvaffaqiyatni faqat daromad belgilamaydi. Pul oqimini tushunish, xarajatlarni boshqarish, rentabellikni saqlash va asosli qarorlar qabul qilish muhim."),
 ("Liderlik va jamoa qurish", "61–80",
  "Samarali ishga olish, kuchli jamoa rivojlantirish, qiyin qarorlar qabul qilish va o‘sish uchun tizimlar qurishni o‘rganing.",
  ["The Hard Thing About Hard Things|Ben Horowitz","High Output Management|Andrew S. Grove","Good to Great|Jim Collins",
   "Built to Last|Jim Collins & Jerry I. Porras","Radical Candor|Kim Scott","The Five Dysfunctions of a Team|Patrick Lencioni",
   "Start with Why|Simon Sinek","Leaders Eat Last|Simon Sinek","Measure What Matters|John Doerr","Scaling Up|Verne Harnish",
   "The E-Myth Revisited|Michael E. Gerber","Blitzscaling|Reid Hoffman & Chris Yeh","The Founder's Dilemmas|Noam Wasserman",
   "Powerful|Patty McCord","No Rules Rules|Reed Hastings & Erin Meyer","Team of Teams|Stanley McChrystal et al.",
   "Extreme Ownership|Jocko Willink & Leif Babin","Crucial Conversations|Kerry Patterson et al.","Who|Geoff Smart & Randy Street",
   "Built to Sell|John Warrillow"],
  "Biznes o‘sgani sari liderlik muhimroq bo‘ladi. Kuchli kompaniyaga malakali odamlar, aniq muloqot, samarali tizimlar va mas’uliyat madaniyati kerak."),
 ("Tadbirkorlik tafakkuri", "81–100",
  "Tadbirkorlik qiyinchiliklaridan o‘tish uchun intizom, chidamlilik, diqqat va qaror qabul qilish ko‘nikmalarini rivojlantiring.",
  ["Shoe Dog|Phil Knight","Steve Jobs|Walter Isaacson","The Almanack of Naval Ravikant|Eric Jorgenson","Atomic Habits|James Clear",
   "Deep Work|Cal Newport","Mindset|Carol S. Dweck","Grit|Angela Duckworth","The Obstacle Is the Way|Ryan Holiday",
   "Ego Is the Enemy|Ryan Holiday","Essentialism|Greg McKeown","The War of Art|Steven Pressfield","Man's Search for Meaning|Viktor E. Frankl",
   "Think and Grow Rich|Napoleon Hill","The Compound Effect|Darren Hardy","Principles|Ray Dalio","Antifragile|Nassim Nicholas Taleb",
   "Mastery|Robert Greene","The 4-Hour Workweek|Tim Ferriss","Tools of Titans|Tim Ferriss","Creativity, Inc.|Ed Catmull & Amy Wallace"],
  "Tadbirkorlik bilimdan ko‘proq narsani talab qiladi. Chidamlilik, moslashuvchanlik va barqaror odatlar noaniqlikdan o‘tishga va yaxshiroq qaror qabul qilishga yordam beradi."),
]
N = 2 + len(SECTIONS) + 1

def foot(i):
    return f'<div class="u">{USER}</div><div class="n">{i:02d} / {N}</div>'

out = ['<section class="s big" id="s1"><div class="t" style="font-size:112px">Har bir biznes egasi o‘qishi kerak bo‘lgan <span class="g">100 ta kitob</span></div>' + foot(1) + '</section>']
start = 1
for k, (title, rng, desc, books, lesson) in enumerate(SECTIONS, 2):
    items = ''.join(
        f'<li><span class="no">{start+j}</span><span class="bk">{b.split("|")[0]}</span> <span class="au">— {b.split("|")[1]}</span></li>'
        for j, b in enumerate(books))
    start += len(books)
    out.append(f'<section class="s list" id="s{k}"><div class="w">'
               f'<div class="h"><span>{title}</span><span class="rng">{rng}</span></div>'
               f'<div class="d">{desc}</div><ol>{items}</ol>'
               f'<div class="l"><b>Asosiy saboq:</b> {lesson}</div></div>{foot(k)}</section>')
k = len(SECTIONS) + 2
tips = ''.join(f'<li><b>{q}</b> {a}</li>' for q, a in [
    ("Biznes boshlayapsizmi?", "Startap asoslariga e’tibor bering."),
    ("Mijoz jalb qilish qiyinmi?", "Sotuv va marketingni o‘rganing."),
    ("Pulni boshqarish qiyinmi?", "Moliyaviy boshqaruvni o‘rganing."),
    ("Jamoa quryapsizmi?", "Liderlik ko‘nikmalaringizni oshiring."),
    ("Diqqatingiz tarqoqmi?", "Tafakkur va kundalik odatlaringiz ustida ishlang.")])
out.append(f'<section class="s list" id="s{k}"><div class="w">'
           f'<div class="t" style="font-size:72px">Barcha 100 ta kitobni o‘qish shart emas.</div>'
           f'<div class="d2">Duch kelayotgan muammongizga mos kitobni o‘qing.</div><ul class="tips">{tips}</ul>'
           f'<div class="d2">O‘qish qimmatli, lekin o‘rganganingizni qo‘llash undan ham muhimroq.</div>'
           f'<div class="t" style="font-size:52px;margin-top:40px">O‘qing. O‘rganing. Qo‘llang.<br><span class="g">Yaxshilang. Takrorlang.</span></div>'
           f'</div>{foot(k)}</section>')
out.append(f'<section class="s big" id="s{N}"><div><div class="t g" style="font-size:92px">Ro‘yxatni saqlab qo‘ying va</div>'
           f'<div class="t" style="font-size:92px;margin-top:6px">sahifamga obuna bo‘ling.</div>'
           f'<div class="hh">{USER}</div><div class="sub">Shu kabi foydali ma’lumotlar har kuni.</div></div>{foot(N)}</section>')

html = '''<!doctype html><html lang="uz"><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
.s{position:relative;width:1080px;height:1350px;background:#000;color:#FFF;overflow:hidden;
  font-family:"SF Pro Display","Inter Display",-apple-system,sans-serif;-webkit-font-smoothing:antialiased}
.big{display:flex;align-items:center;padding:0 80px 60px}
.list .w{position:absolute;left:80px;right:80px;top:96px}
.t{font-weight:500;letter-spacing:-.045em;line-height:1.04}
.g{color:#7A7A7A}
.h{display:flex;justify-content:space-between;align-items:baseline;font-size:52px;font-weight:600;letter-spacing:-.03em}
.rng{font-size:30px;font-weight:400;color:#7A7A7A;letter-spacing:0}
.d{margin-top:16px;font-size:26px;line-height:1.35;color:#8C8C8C}
ol{list-style:none;margin-top:34px}
ol li{font-size:27px;line-height:1.36;letter-spacing:-.012em;white-space:nowrap}
.no{display:inline-block;width:62px;color:#5E5E5E;font-variant-numeric:tabular-nums}
.bk{font-weight:500}.au{color:#7A7A7A}
.l{margin-top:34px;font-size:25px;line-height:1.4;color:#BDBDBD}.l b{color:#FFF;font-weight:600}
.d2{margin-top:36px;font-size:34px;line-height:1.35;color:#8C8C8C}
.tips{list-style:none;margin-top:24px}.tips li{font-size:34px;line-height:1.35;margin-top:14px;color:#8C8C8C}.tips b{color:#FFF;font-weight:500}
.hh{margin-top:56px;font-size:46px;font-weight:600;letter-spacing:-.02em}
.sub{margin-top:18px;font-size:32px;color:#7A7A7A}
.u,.n{position:absolute;bottom:72px;font-size:26px;font-weight:500}
.u{left:80px}.n{right:80px;color:#5E5E5E;font-weight:400}
</style></head><body>
''' + '\n'.join(out) + '\n</body></html>\n'
open(__file__.replace('slides.py', 'carousel.html'), 'w').write(html)
