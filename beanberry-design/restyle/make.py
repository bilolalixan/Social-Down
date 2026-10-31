import sys, subprocess, numpy as np
from PIL import Image, ImageFilter
W,H,FPS,DUR=1080,1920,30,8.0
# old logo mask
o=np.asarray(Image.open('/root/.claude/uploads/43c41a0e-1397-56a9-ae81-7fcc7bd40cc6/a104092d-image.png').convert('L')).astype(np.float32)
oa=np.clip((o-40)/180,0,1); ys,xs=np.where(oa>.2)
oa=oa[ys.min()-8:ys.max()+8, xs.min()-8:xs.max()+8]
old=Image.fromarray((oa*255).astype(np.uint8)); s=820/old.width; old=old.resize((820,int(old.height*s)),Image.LANCZOS)
new=Image.open('../profile/beanberry-wordmark-white-transparent.png').split()[3]
s=780/new.width; new=new.resize((780,int(new.height*s)),Image.LANCZOS)
def ease(x): x=min(max(x,0),1); return x*x*(3-2*x)
def place(canvas,m,alpha,blur,scale,dx=0):
    if alpha<=0: return
    mm=m.resize((max(1,int(m.width*scale)),max(1,int(m.height*scale))),Image.LANCZOS)
    pad=80; big=Image.new('L',(mm.width+2*pad,mm.height+2*pad),0); big.paste(mm,(pad,pad))
    if blur>0.3:
        # motion (horizontal) + soft blur, like brand story blur
        big=big.filter(ImageFilter.BoxBlur(0)).resize(big.size)
        arr=np.asarray(big).astype(np.float32); k=int(blur*2)+1
        c=np.cumsum(np.pad(arr,((0,0),(k,k))),axis=1); arr=(c[:,2*k:]-c[:,:-2*k])/(2*k)
        big=Image.fromarray(arr[:, :big.width].clip(0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(blur/3))
    big=big.point(lambda v:int(v*alpha))
    x=(W-big.width)//2+int(dx); y=(H-big.height)//2
    canvas.paste(Image.new('L',big.size,255),(x,y),big)
p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','gray','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
  '-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-preset','slow','-movflags','+faststart','beanberry-restyle.mp4'],stdin=subprocess.PIPE)
rng=np.random.default_rng(1)
for f in range(int(DUR*FPS)):
    t=f/FPS; c=Image.new('L',(W,H),0)
    # old: in 0.4-1.4, out 2.9-3.7
    if t<3.8:
        a=ease((t-0.4)/1.0)*(1-ease((t-2.9)/0.8))
        b=40*(1-ease((t-0.4)/1.0))+45*ease((t-2.9)/0.8)
        sc=0.96+0.04*ease((t-0.4)/1.0)+0.05*ease((t-2.9)/0.8)
        place(c,old,a,b,sc,dx=-60*ease((t-2.9)/0.8))
    # new: in 3.5-4.7
    if t>3.4:
        e=ease((t-3.5)/1.2)
        place(c,new,e,45*(1-e),1.05-0.05*e,dx=60*(1-e))
    arr=np.asarray(c).astype(np.float32)+rng.normal(0,1.5,(H,W))  # subtle grain
    p.stdin.write(arr.clip(0,255).astype(np.uint8).tobytes())
p.stdin.close(); p.wait(); print('done')
