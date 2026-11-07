import sys,numpy as np
from PIL import Image,ImageDraw,ImageFont
S='/tmp/claude-0/-home-user-Social-Down/43c41a0e-1397-56a9-ae81-7fcc7bd40cc6/scratchpad/menu/hi/p-%02d.png'
OUT='beanberry-design/menu-stories/'
BG=(228,218,207);INK=(52,46,42)
F=ImageFont.truetype('/usr/share/fonts/opentype/inter/InterDisplay-Regular.otf',26)
def story(crop,name,label):
    k=min(1080/crop.width,1620/crop.height)
    w=round(crop.width*k);h=round(crop.height*k)
    c=crop.resize((w,h),Image.LANCZOS)
    cv=Image.new('RGB',(1080,1920),BG)
    cv.paste(c,((1080-w)//2,(1920-h)//2))
    d=ImageDraw.Draw(cv)
    d.text((60,90),'BEANBERRY',font=F,fill=INK)
    d.text((1020,90),'MENU',font=F,fill=INK,anchor='ra')
    d.text((540,1810),label,font=F,fill=INK,anchor='ma')
    cv.save(OUT+name+'.png')
n=0
for p in range(1,28):
    im=Image.open(S%p).convert('RGB');W,H=im.size
    x0,x1=30,W-30;y0,y1=30,H-30
    if p==1:
        story(im.crop((0,0,W,H)),'menu-01',f'1 / 27');n+=1;continue
    a=np.asarray(im.convert('L'),dtype=float)[:,x0:x1]
    ca=np.asarray(im.convert('L'),dtype=float)
    cm=W//2;best2=min(range(cm-40,cm+40),key=lambda x:ca[int(H*.2):int(H*.9),x-2:x+3].std(axis=0).mean())
    v=ca[int(H*.2):int(H*.9),best2-2:best2+3].std(axis=0).mean()
    if False:
        story(im.crop((x0,y0,best2,y1)),f'menu-{p:02d}a',f'{p} / 27  ·  1/2')
        story(im.crop((best2,y0,x1,y1)),f'menu-{p:02d}b',f'{p} / 27  ·  2/2');n+=2;print(p,'cols',round(v,1));continue
    print(p,'rows',round(v,1))
    mid=H//2;best=None
    for y in range(mid-150,mid+150):
        s=a[y-3:y+3].std(axis=1).mean()
        if best is None or s<best[0]:best=(s,y)
    cut=best[1]
    story(im.crop((x0,y0,x1,cut+50)),f'menu-{p:02d}a',f'{p} / 27  ·  1/2');
    story(im.crop((x0,cut-50,x1,y1)),f'menu-{p:02d}b',f'{p} / 27  ·  2/2');n+=2
print(n)
