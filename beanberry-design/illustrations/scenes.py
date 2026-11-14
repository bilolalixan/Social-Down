from draw import *
import random
R=random.Random(7)
W,H=1536,1024
# 1 branch with cherries
def branch():
    b='<path d="M120,820 C380,700 620,640 900,520 C1100,430 1250,330 1420,180" stroke-width="3.2"/><path d="M120,832 C380,712 620,652 900,532 C1100,442 1250,342 1420,192" stroke-width="1.2"/>'
    pts=[(300,760,-35),(420,712,-80),(520,684,-20),(640,640,-70),(700,620,30),(780,590,-25),(860,545,35),(940,505,-60),(1020,470,-15),(1100,425,35),(1180,380,-55),(1260,330,-10),(1340,255,-45)]
    for i,(x,y,a) in enumerate(pts):b+=leaf(x,y,a-90 if i%2 else a+90,s=120+R.randint(-10,25),w=.34,seed=i)
    for (x,y) in [(560,700),(590,725),(610,690),(960,520),(990,548),(1010,512),(1190,400),(1215,430)]:
        b+=f'<line x1="{x}" y1="{y-30}" x2="{x}" y2="{y-6}" stroke-width="1.2"/>'+cherry(x,y+2)
    return svg(W,H,b)
# 2 cup
def cup():
    b=''
    b+='<ellipse cx="768" cy="760" rx="360" ry="64" fill="#fdf3ea" stroke-width="2"/><ellipse cx="768" cy="752" rx="270" ry="44" stroke-width="1.2"/>'
    b+=hc(ell(768,760,360,64),430,700,1110,830,gap=4,ang=-8,sw=.7,seed=2)
    d='M568,470 L568,640 Q568,745 768,745 Q968,745 968,640 L968,470 Z'
    b+=f'<path d="{d}" fill="#fdf3ea" stroke-width="2.2"/>'
    b+=clipped('c1',d,hatch(740,460,980,760,gap=4.2,ang=-65,sw=.8,seed=3)+hatch(850,460,980,760,gap=3,ang=-65,sw=.9,seed=4))
    b+='<ellipse cx="768" cy="470" rx="200" ry="40" fill="#fdf3ea" stroke-width="2.2"/><ellipse cx="768" cy="476" rx="176" ry="31" stroke-width="1"/>'
    b+=hc(ell(768,476,176,31),620,440,920,510,gap=3,ang=0,sw=.9,seed=5)
    b+='<path d="M966,520 Q1090,510 1086,590 Q1080,670 940,672" stroke-width="2.2"/><path d="M958,545 Q1050,538 1050,590 Q1048,640 950,646" stroke-width="1.2"/>'
    for i,x in enumerate([700,768,836]):
        b+=f'<path d="M{x},420 C{x-40},380 {x+40},340 {x},300 C{x-30},260 {x+30},220 {x},170" stroke-width="2.2" opacity=".85"/><path d="M{x+14},410 C{x-18},370 {x+52},330 {x+14},290 C{x-14},250 {x+40},210 {x+14},170" stroke-width="1.1" opacity=".6"/>'
    b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="8" fill="#fdf3ea" stroke-width="1.4" transform="rotate({a} {x} {y})"/><path d="M{x-8},{y} Q{x},{y-3} {x+8},{y}" stroke-width=".8" transform="rotate({a} {x} {y})"/>' for x,y,a in [(1010,785,20),(1050,805,-30),(1100,790,10)])
    return svg(W,H,b)
# 3 cafe scene
def tree(x,y,h,w,seed):
    r=random.Random(seed);o=f'<path d="M{x},{y} C{x-6},{y-h*.4} {x+10},{y-h*.6} {x},{y-h}" stroke-width="3"/><path d="M{x+8},{y} C{x+4},{y-h*.4} {x+18},{y-h*.6} {x+8},{y-h}" stroke-width="1.1"/>'
    for i in range(46):
        t=r.random();bx=x+r.uniform(-w,w)*(.4+t);by=y-h*(.45+t*.55)+r.uniform(-30,30)
        o+=f'<path d="M{x+3},{y-h*(.3+t*.6):.0f} Q{(x+bx)/2:.0f},{by+20:.0f} {bx:.0f},{by:.0f}" stroke-width="1.1"/>'
        for k in range(3):o+=leaf(bx,by,r.randint(0,360),s=26,w=.4,fill=False)
    return o
def scene():
    b=''
    b+='<path d="M470,430 L650,380 L820,430" stroke-width="1.5"/><path d="M460,540 L640,500 L760,540" stroke-width="1" opacity=".7"/>'
        # building
    b+='<rect x="860" y="430" width="470" height="380" fill="#fdf3ea" stroke-width="2.2"/><rect x="900" y="470" width="390" height="340" stroke-width="1.2"/>'
    b+='<path d="M960,810 L960,600 Q960,520 1050,520 Q1140,520 1140,600 L1140,810" fill="#fdf3ea" stroke-width="2.2"/><path d="M985,810 L985,610 Q985,548 1050,548 Q1115,548 1115,610 L1115,810" stroke-width="1.2"/>'
    b+=hc('M985,810 L985,610 Q985,548 1050,548 Q1115,548 1115,610 L1115,810Z',980,540,1120,810,gap=4,ang=-70,sw=.7,seed=6)
    for x in range(905,1290,34):b+=f'<path d="M{x},470 l17,-22 l17,22" stroke-width=".9"/>'
    b+='<rect x="1180" y="560" width="90" height="140" rx="6" stroke-width="1.4"/><line x1="1225" y1="560" x2="1225" y2="700" stroke-width=".9"/><line x1="1180" y1="630" x2="1270" y2="630" stroke-width=".9"/>'
    for x in (860,1330):b+=f'<rect x="{x-24}" y="260" width="48" height="540" fill="#fdf3ea" stroke-width="2"/><path d="M{x-24},260 Q{x},230 {x+24},260" stroke-width="2"/>'+hc(f'M{x-24},260 h48 v540 h-48Z',x-24,260,x+24,800,gap=6,ang=75,sw=.6,seed=x)
    b+='<ellipse cx="1050" cy="520" rx="0" ry="0"/>'
    # awning
    b+='<path d="M230,610 L520,520 L760,640 L480,700 Z" fill="#fdf3ea" stroke-width="2.2"/>'+clipped('aw','M230,610 L520,520 L760,640 L480,700 Z',hatch(230,520,760,700,gap=22,ang=55,sw=1,seed=9))
    for i in range(9):
        x=240+i*58;y=616+(i*7);b+=f'<path d="M{x},{y+80-i*4} q29,26 58,0" stroke-width="1.2"/>'
    b+='<line x1="300" y1="650" x2="300" y2="880" stroke-width="2.4"/><line x1="480" y1="700" x2="480" y2="880" stroke-width="2.4"/><line x1="740" y1="640" x2="740" y2="880" stroke-width="2"/>'
    for x,y in [(300,690),(480,740)]:b+=f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+22}" stroke-width="1.2"/><path d="M{x-10},{y+22} h20 l-3,26 h-14 Z" fill="#fdf3ea" stroke-width="1.4"/>'
    # table & chairs
    b+='<ellipse cx="420" cy="800" rx="58" ry="10" fill="#fdf3ea" stroke-width="2"/><line x1="420" y1="808" x2="420" y2="880" stroke-width="2.4"/><path d="M388,884 Q420,874 452,884" stroke-width="2"/>'
    b+='<ellipse cx="410" cy="792" rx="11" ry="3" stroke-width="1.2"/><path d="M399,792 v-8 h22 v8" stroke-width="1.2"/>'
    for x,s in [(340,-1),(500,1)]:
        b+=f'<path d="M{x-18},{800} h36" stroke-width="2"/><line x1="{x-16}" y1="800" x2="{x-18}" y2="880" stroke-width="2"/><line x1="{x+16}" y1="800" x2="{x+18}" y2="880" stroke-width="2"/><path d="M{x-16},{800} v-70 q16,-14 32,0 v70" fill="#fdf3ea" stroke-width="2"/>'+''.join(f'<line x1="{x-12+i*8}" y1="742" x2="{x-12+i*8}" y2="796" stroke-width=".9"/>' for i in range(4))
    # trees, ground
    b+=tree(150,890,560,200,1)+tree(1440,890,380,150,2)+tree(700,900,230,120,3)
    b+='<path d="M20,930 Q300,880 600,920 Q900,950 1200,900 Q1400,880 1520,920" stroke-width="2.2"/><path d="M60,960 Q400,930 800,965 Q1100,985 1480,950" stroke-width="1.2"/>'
    b+=hc('M20,930 Q300,880 600,920 Q900,950 1200,900 Q1400,880 1520,920 L1520,1000 L20,1000Z',20,880,1520,1000,gap=7,ang=-4,sw=.5,seed=11)
    # branch top right
    b+='<path d="M1000,40 C1150,70 1300,50 1500,0" stroke-width="2.6"/>'
    for i,(x,y,a) in enumerate([(1060,60,100),(1140,76,-100),(1220,70,95),(1300,50,-95),(1380,30,100),(1100,66,110)]):b+=leaf(x,y,a,s=80,w=.35,seed=i)
    for (x,y) in [(1250,100),(1290,112)]:b+=cherry(x,y,10)
    return svg(W,H,b)
# 4 beans & sack
def bean(x,y,a,s=1):
    return f'<g transform="translate({x},{y}) rotate({a}) scale({s})"><ellipse rx="40" ry="26" fill="#fdf3ea" stroke-width="2"/><path d="M-38,2 C-14,-14 14,16 38,-2" stroke-width="1.6"/>'+hc(ell(0,0,40,26),-40,-26,40,26,gap=4,ang=-60,sw=.5,seed=int(x+y))+'</g>'
def beans():
    b=''
    d='M470,330 Q520,260 640,250 L900,250 Q1020,260 1070,330 L1130,800 Q1000,860 770,860 Q540,860 410,800 Z'
    b+=f'<path d="{d}" fill="#fdf3ea" stroke-width="2.4"/>'
    b+=clipped('sk',d,hatch(900,240,1140,880,gap=5,ang=-70,sw=.7,seed=1)+hatch(1000,240,1140,880,gap=3,ang=-70,sw=.8,seed=2)+hatch(400,640,1140,880,gap=9,ang=10,sw=.5,seed=8))
    b+='<path d="M470,330 Q620,370 770,350 Q920,370 1070,330" stroke-width="1.8"/><path d="M480,352 Q620,390 770,370 Q920,390 1060,352" stroke-width="1"/>'
    for x in range(520,1030,60):b+=f'<line x1="{x}" y1="362" x2="{x+4}" y2="395" stroke-width="1"/>'
    b+='<path d="M560,520 q210,-70 420,0 v160 q-210,70 -420,0 Z" fill="#fdf3ea" stroke-width="1.6"/>'
    b+=f'<text x="770" y="620" text-anchor="middle" font-family="Georgia,serif" font-size="64" fill="{INK}" stroke="none" letter-spacing="6">COFFEE</text><line x1="640" y1="640" x2="900" y2="640" stroke-width="1.4"/>'
    R2=random.Random(5)
    for i in range(34):
        x=R2.uniform(300,1230);y=R2.uniform(830,940)
        b+=bean(x,y,R2.randint(0,180),R2.uniform(.55,.85))
    for x,y,a in [(1180,720,30),(1250,760,-50),(1310,800,10)]:b+=bean(x,y,a,.8)
    return svg(W,H,b)
# 5 moka pot
def moka():
    b=''
    top='M650,300 Q660,240 770,230 Q880,240 890,300 L900,420 L640,420 Z'
    base='M620,620 L920,620 L960,880 L580,880 Z'
    mid='M640,420 L900,420 L920,620 L620,620 Z'
    for d,i in ((top,'a'),(mid,'b'),(base,'c')):
        b+=f'<path d="{d}" fill="#fdf3ea" stroke-width="2.4"/>'
    b+=clipped('ma','M640,420 L900,420 L920,620 L620,620 Z',hatch(620,420,930,620,gap=6,ang=-85,sw=.8,seed=3))
    b+=clipped('mc','M620,620 L920,620 L960,880 L580,880 Z',hatch(620,620,960,880,gap=6,ang=-85,sw=.8,seed=4))
    b+=clipped('mt',top,hatch(650,230,900,420,gap=5,ang=-70,sw=.7,seed=5))
    for x in (690,730,770,810,850):b+=f'<line x1="{x}" y1="430" x2="{x-4}" y2="610" stroke-width="1" opacity=".8"/>'
    b+='<path d="M730,238 Q770,205 810,238" stroke-width="2"/><circle cx="770" cy="215" r="14" fill="#fdf3ea" stroke-width="2"/>'
    b+='<path d="M890,290 Q1010,280 1010,370 Q1000,450 900,420" stroke-width="2.4"/><path d="M890,310 Q980,310 980,370 Q975,425 898,402" stroke-width="1.2"/>'
    b+='<path d="M650,300 L610,285 Q585,280 590,300 L650,330" fill="#fdf3ea" stroke-width="2.2"/>'
    b+='<ellipse cx="770" cy="882" rx="190" ry="14" stroke-width="1.6"/>'
    for i,x in enumerate((700,770,840)):b+=f'<path d="M{x},190 C{x-30},160 {x+30},130 {x},95" stroke-width="1.8" opacity=".7"/>'
    b+='<path d="M120,940 Q500,915 800,938 Q1100,960 1420,935" stroke-width="1.6"/>'
    # branch left
    b+='<path d="M80,700 C180,640 300,560 420,470" stroke-width="2.6"/>'
    for i,(x,y,a) in enumerate([(160,670,-60),(220,630,-110),(280,590,-50),(340,540,-100),(400,490,-40)]):b+=leaf(x,y,a,s=90,w=.34,seed=i)
    for (x,y) in [(250,650),(300,625)]:b+=cherry(x,y,10)
    return svg(W,H,b)
# 6 croissant + cup
def croissant():
    import math
    b=''
    cx,cy,Rr=768,930,350
    order=[0,6,1,5,2,4,3]
    for j,i in enumerate(order):
        th=math.radians(205+i*(130/6));x=cx+Rr*math.cos(th);y=cy+Rr*math.sin(th)*.62
        k=1-abs(i-3)/3.2;rx=70+80*k;ry=55+75*k;a=math.degrees(th)+90
        d=ell(0,0,rx,ry)
        b+=f'<g transform="translate({x:.0f},{y:.0f}) rotate({a:.0f})"><path d="{d}" fill="#fdf3ea" stroke-width="2.4"/>'
        b+=hc(d,-rx,-ry,rx,ry,gap=5,ang=-60,sw=.7,seed=i)
        for q in range(1,5):b+=f'<path d="M{-rx*.85:.0f},{-ry+q*ry*.4:.0f} Q0,{-ry*.8+q*ry*.4-18:.0f} {rx*.85:.0f},{-ry+q*ry*.4:.0f}" stroke-width=".9"/>'
        b+='</g>'
    b+='<ellipse cx="768" cy="965" rx="470" ry="40" fill="none" stroke-width="2"/><ellipse cx="768" cy="955" rx="380" ry="28" fill="none" stroke-width="1"/>'
    b+=hc('M298,965 A470,40 0 1,0 1238,965 A470,40 0 1,0 298,965Z',298,935,1238,1005,gap=4,ang=-6,sw=.6,seed=3)
    for i,(x,y,a) in enumerate([(250,340,-30),(330,290,-70),(1290,340,200),(1210,290,240)]):b+=leaf(x,y,a,s=90,w=.34,seed=i)
    return svg(W,H,b)
for n,f in [('1-branch',branch),('2-cup',cup),('3-cafe',scene),('4-beans',beans),('5-moka',moka),('6-croissant',croissant)]:
    open(f'{n}.svg','w').write(f())
