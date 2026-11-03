import sys
from PIL import Image, ImageFilter
import numpy as np
SIG=float(sys.argv[1]) if len(sys.argv)>1 else 1.0
im=Image.open('/root/.claude/uploads/43c41a0e-1397-56a9-ae81-7fcc7bd40cc6/4f93dcae-image.jpg').convert('RGB')
a=np.asarray(im).astype(np.float32)/255
dark=1-a.min(2)
ys,xs=np.where(dark>0.15); pad=8
y0,y1,x0,x1=ys.min()-pad,ys.max()+pad,xs.min()-pad,xs.max()+pad
crop=a[y0:y1,x0:x1]; d=dark[y0:y1,x0:x1]
strong=d>0.45; rows=np.where(strong.any(1))[0]; k=max(1,len(rows)//5)
top=crop[rows[:k]][strong[rows[:k]]].mean(0); bot=crop[rows[-k:]][strong[rows[-k:]]].mean(0)
lev=d[strong].mean()
S=24
m=Image.fromarray((np.clip(d/lev,0,1)*255).astype(np.uint8)).resize(((x1-x0)*S,(y1-y0)*S),Image.BICUBIC)
m=m.filter(ImageFilter.GaussianBlur(S*SIG))
arr=np.asarray(m).astype(np.float32)/255
hard=(arr>0.42).astype(np.float32)
# second smoothing pass (curvature smoothing)
for r in (S*0.6,S*0.4):
    h2=np.asarray(Image.fromarray((hard*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r))).astype(np.float32)/255
    hard=(h2>0.5).astype(np.float32)
mask=Image.fromarray((hard*255).astype(np.uint8))
W=4000; H=int(mask.height*W/mask.width); mask=mask.resize((W,H),Image.LANCZOS)
al=np.asarray(mask).astype(np.float32)/255
yy=np.linspace(0,1,H)[:,None,None]; gold=np.broadcast_to(top*(1-yy)+bot*yy,(H,W,3))
def out(name,fg,bg=None):
    f=np.broadcast_to(np.array(fg,np.float32),(H,W,3)) if fg.ndim==1 else fg
    if bg is None:
        Image.fromarray(np.dstack([f*255,al*255]).astype(np.uint8),'RGBA').save(name+'.png'); return
    CW,CH=int(W*1.4),int(H*2.4)
    cv=np.ones((CH,CW,3),np.float32)*np.array(bg); oy,ox=(CH-H)//2,(CW-W)//2
    cv[oy:oy+H,ox:ox+W]=cv[oy:oy+H,ox:ox+W]*(1-al[...,None])+f*al[...,None]
    img=Image.fromarray((cv*255+.5).astype(np.uint8)); img.save(name+'.jpg',quality=97); img.save(name+'-bg.png')
B=np.array([0.,0,0]);Wt=np.array([1.,1,1])
out('issi-white-on-black',Wt,B); out('issi-black-on-white',B,Wt)
out('issi-gold-on-white',gold,Wt); out('issi-gold-on-black',gold,np.array([.04,.04,.04]))
out('issi-white-transparent',Wt); out('issi-black-transparent',B); out('issi-gold-transparent',gold)
