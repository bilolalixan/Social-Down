import subprocess, wave, math, numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont
W,H,FPS,DUR=1080,1920,30,10.0
N=int(FPS*DUR); SR=48000
rng=np.random.default_rng(7)
BROWN=np.array([90,36,22],np.float32); CREAM=np.array([243,233,220],np.float32)
def ease(x): x=np.clip(x,0,1); return x*x*(3-2*x)
def eout(x): x=np.clip(x,0,1); return 1-(1-x)**3
def place(m,cx,cy):
    a=np.zeros((H,W),np.float32); h,w=m.shape; y=int(cy-h/2); x=int(cx-w/2); a[y:y+h,x:x+w]=m; return a
# ---- logos
o=np.asarray(Image.open('/root/.claude/uploads/43c41a0e-1397-56a9-ae81-7fcc7bd40cc6/a104092d-image.png').convert('L')).astype(np.float32)
oa=np.clip((o-40)/180,0,1); ys,xs=np.where(oa>.2); oa=oa[ys.min()-6:ys.max()+6,xs.min()-6:xs.max()+6]
oi=Image.fromarray((oa*255).astype(np.uint8)); oi=oi.resize((840,int(oi.height*840/oi.width)),Image.LANCZOS)
OLD=place(np.asarray(oi)/255.,W/2,H/2)
ni=Image.open('../profile/beanberry-wordmark-white-transparent.png').split()[3]
ni=ni.resize((800,int(ni.height*800/ni.width)),Image.LANCZOS)
NEW=place(np.asarray(ni)/255.,W/2,H/2-30)
# tagline
f=ImageFont.truetype('/usr/share/fonts/opentype/inter/InterDisplay-Light.otf',30)
tg=Image.new('L',(800,60),0); d=ImageDraw.Draw(tg); txt='THE FIFTH TASTE'; x=0
widths=[]
for ch in txt: widths.append(d.textlength(ch,font=f)+12)
tot=sum(widths)-12; x=(800-tot)/2
for ch,wd in zip(txt,widths): d.text((x,10),ch,font=f,fill=255); x+=wd
TAG=place(np.asarray(tg)/255.,W/2,H/2+75)
# ---- new logo letters (column segmentation) + outlines
nb=NEW>0.35; cols=nb.any(0); segs=[]; inside=False
for xi,v in enumerate(cols):
    if v and not inside: s=xi; inside=True
    if not v and inside: segs.append((s,xi)); inside=False
er=np.asarray(Image.fromarray((nb*255).astype(np.uint8)).filter(ImageFilter.MinFilter(5)))>127
edge=nb&~er
edge=np.asarray(Image.fromarray((edge*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)))/255.
YY,XX=np.mgrid[0:H,0:W]
ang=np.zeros((H,W),np.float32); lid=np.full((H,W),-1)
for i,(a,b) in enumerate(segs):
    sl=(slice(None),slice(a-3,b+3)); m=nb[sl]
    yy,xx=np.where(m); cy,cx=yy.mean(),xx.mean()+a-3
    A=(np.arctan2(YY[sl]-cy,XX[sl]-cx)+np.pi*0.5)%(2*np.pi)/(2*np.pi)
    ang[sl]=np.where(lid[sl]<0,A,ang[sl]); lid[sl]=np.where(lid[sl]<0,i,lid[sl])
NL=len(segs)
# ---- old logo particles
py,px=np.where(OLD>0.4); sel=rng.choice(len(py),min(26000,len(py)),replace=False); py=py[sel].astype(np.float32); px=px[sel].astype(np.float32)
vx=rng.normal(140,60,len(px)); vy=rng.normal(-260,120,len(px)); delay=(px-px.min())/(px.max()-px.min())*0.35+rng.uniform(0,.1,len(px))
# old logo column ink & pen y
ocol=OLD.sum(0); obx=np.where(ocol>0)[0]; ox0,ox1=obx.min(),obx.max()
def penY(xc):
    c=OLD[:,int(xc)]; 
    if c.sum()<1e-3: return None
    return (np.arange(H)*c).sum()/c.sum()
# scribble path
sx=np.linspace(ox0-30,ox1+30,400); sy=H/2+np.sin(sx/26)*38+np.sin(sx/7.3)*9+rng.normal(0,2,400)
# sound event log
ev=[]
frames_audio_scratch=np.zeros(N)
def tsec(f): return f/FPS
p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
 '-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','slow','video.mp4'],stdin=subprocess.PIPE)
boil=None
for fi in range(N):
    t=tsec(fi); ink=np.zeros((H,W),np.float32); bg_mix=np.zeros((H,W),np.float32)
    # A: write old logo 0.3-2.1
    if t<2.4:
        pr=eout((t-0.3)/1.8); xr=ox0+(ox1-ox0+20)*pr
        wob=np.sin(YY[:,:1]/9+t*20)*6
        mask=(XX<xr+wob).astype(np.float32)
        ink=np.maximum(ink,OLD*mask*(1-np.clip((XX-xr)/12,0,1)*0))
        if 0.3<t<2.15:
            y=penY(min(xr,ox1)); 
            if y is not None:
                d2=(XX-xr)**2+(YY-y)**2; ink=np.maximum(ink,np.exp(-d2/60)*1.0)
                frames_audio_scratch[fi]=min(1,OLD[:,int(min(xr,ox1))].sum()/40)
    elif t<4.3:
        # B scribble 2.4-3.1, then dissolve 3.2-4.3
        if t<3.25:
            ink=OLD.copy()
            k=int(np.clip((t-2.4)/0.65,0,1)*len(sx))
            if k>1:
                im=Image.new('L',(W,H),0); d=ImageDraw.Draw(im)
                d.line(list(zip(sx[:k],sy[:k])),fill=255,width=14,joint='curve')
                ink=np.maximum(ink,np.asarray(im)/255.)
            if 2.4<t<3.05: ev.append(('squeak',t))
            # shake at end
        else:
            tt=t-3.25; ink=np.zeros((H,W),np.float32)
            loc=np.clip(tt-delay,0,None); xx=(px+vx*loc+np.sin(py/20+loc*6)*20*loc).astype(int); yy=(py+vy*loc*1.2+120*loc*loc).astype(int)
            al=np.clip(1-loc/0.75,0,1); ok=(xx>=0)&(xx<W)&(yy>=0)&(yy<H)&(al>0)
            np.maximum.at(ink,(yy[ok],xx[ok]),al[ok])
            still=(loc<=0)&ok; 
            ink=np.asarray(Image.fromarray((ink*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)))/255.
            # remaining static (not yet released) old pixels
            rel=np.clip((XX-px.min())/(px.max()-px.min())*0.35 - tt,0,1)>0
            ink=np.maximum(ink,OLD*rel)
    # D: new outlines 4.4-6.6 per letter, boil
    if t>=4.3:
        if fi%3==0 or boil is None: boil=(rng.integers(-2,3),rng.integers(-2,3))
        ed=np.roll(np.roll(edge,boil[0],0),boil[1],1)
        out=np.zeros((H,W),np.float32); fill=np.zeros((H,W),np.float32)
        for i in range(NL):
            st=4.4+i*0.2; pr=np.clip((t-st)/0.55,0,1)
            if pr<=0: continue
            mk=(lid==i)
            out=np.maximum(out,ed*mk*(ang<pr))
            fs=6.4+i*0.06; fp=ease((t-fs)/0.35)
            fill=np.maximum(fill,NEW*mk*fp)
            if 0<pr<1: frames_audio_scratch[fi]=max(frames_audio_scratch[fi],0.6)
            if abs(t-fs)<1/FPS/2+1e-6: ev.append(('pop',t))
        ink=np.maximum(np.maximum(ink,out*(1-ease((t-7.2)/0.5)*0.0)),fill)
        # tagline drawn 7.9-8.6 with underline
        tp=ease((t-7.9)/0.8)
        tag=TAG*((XX-(W/2-300))/600<tp)
        ink=np.maximum(ink,tag*0.9)
        ux=W/2-300+600*ease((t-8.0)/0.9)
        if t>8.0:
            ul=((YY>H/2+112)&(YY<H/2+115)&(XX>W/2-300)&(XX<ux)).astype(np.float32)*0.7
            ink=np.maximum(ink,ul)
    # F: circle reveal brown 7.2-7.9
    r=eout((t-7.2)/0.75)*1300
    bg_mix=((XX-W/2)**2+(YY-(H/2-30))**2<r*r).astype(np.float32) if t>7.2 else bg_mix
    if t>7.2 and abs(t-7.2)<1/FPS: ev.append(('thump',t))
    if t>4.3 and abs(t-4.3)<1/FPS: ev.append(('whoosh_end',t))
    bgc=bg_mix[...,None]*BROWN
    fg=CREAM*bg_mix[...,None]+np.array([255,255,255],np.float32)*(1-bg_mix[...,None])
    img=bgc*(1-ink[...,None])+fg*ink[...,None]
    img+=rng.normal(0,2.2,(H,W,1))
    # vignette
    p.stdin.write(img.clip(0,255).astype(np.uint8).tobytes())
p.stdin.close(); p.wait()
# ---- audio
L=int(SR*DUR); au=np.zeros(L)
noise=rng.normal(0,1,L)
def bp(x,a): # simple one-pole highpass-ish
    y=np.empty_like(x); prev=0; 
    y=x-np.concatenate([[0],x[:-1]])*a; return y
scr=bp(noise,0.6)
env=np.interp(np.arange(L)/SR,np.arange(N)/FPS,frames_audio_scratch)
grain=(rng.random(L)<0.004)*rng.normal(0,1,L)
env*= (0.6+0.4*np.abs(np.sin(np.arange(L)/SR*2*np.pi*13)))
au+=scr*env*0.12+grain*env*0.5
def add(st,sig):
    i=int(st*SR); j=min(L,i+len(sig)); au[i:j]+=sig[:j-i]
# typewriter-ish clicks not used; squeak (marker) 2.4-3.05
ts=np.arange(int(0.65*SR))/SR
sq=np.sin(2*np.pi*(1800+400*np.sin(ts*9))*ts)*0.05+bp(rng.normal(0,1,len(ts)),0.95)*0.08
sq*=np.minimum(1,ts*20)*np.minimum(1,(0.65-ts)*15)
add(2.4,sq)
# whoosh 3.2-4.3
tw=np.arange(int(1.1*SR))/SR; wn=rng.normal(0,1,len(tw))
k=np.ones(40)/40; wl=np.convolve(wn,k,'same'); wh=wn-wl
mix=np.clip(tw/1.1,0,1); wsh=(wl*(1-mix)+wh*mix*0.4)*np.sin(np.pi*tw/1.1)**2*0.5
add(3.2,wsh)
# pops per letter fill
for i in range(NL):
    tp=np.arange(int(0.09*SR))/SR; fr=900-500*tp/0.09
    s=np.sin(2*np.pi*np.cumsum(fr)/SR)*np.exp(-tp*45)*0.22
    add(6.4+i*0.06,s)
# thump + shimmer at 7.2
tt=np.arange(int(1.2*SR))/SR
th=np.sin(2*np.pi*(55+30*np.exp(-tt*8))*tt)*np.exp(-tt*3.2)*0.7+bp(rng.normal(0,1,len(tt)),0.5)*np.exp(-tt*20)*0.15
add(7.2,th)
ts2=np.arange(int(2.2*SR))/SR
sh=sum(np.sin(2*np.pi*f0*ts2+ph) for f0,ph in [(1760,0),(2637,1),(3520,2),(2217,.5)])*0.025*np.exp(-ts2*1.6)*np.minimum(1,ts2*10)
add(7.25,sh)
# soft tick for underline
ttk=np.arange(int(0.9*SR))/SR; add(8.0,bp(rng.normal(0,1,len(ttk)),0.8)*0.04*np.sin(np.pi*ttk/0.9))
# ambient room tone
au+=np.convolve(rng.normal(0,1,L),np.ones(200)/200,'same')*0.02
au=au/max(1e-6,np.abs(au).max())*0.9
fade=np.ones(L); fade[-int(0.6*SR):]=np.linspace(1,0,int(0.6*SR)); au*=fade
with wave.open('audio.wav','wb') as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((au*32767).astype(np.int16).tobytes())
subprocess.run(['ffmpeg','-y','-loglevel','error','-i','video.mp4','-i','audio.wav','-c:v','copy','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart','beanberry-restyle-motion.mp4'],check=True)
print('ok',NL)
