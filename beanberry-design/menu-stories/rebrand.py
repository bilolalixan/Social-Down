# Replaces the old script logo on menu pages 1-2 with the new BEANBERRY wordmark (black), then rebuilds stories.
import os,sys
from PIL import Image,ImageFilter
D='/tmp/claude-0/-home-user-Social-Down/43c41a0e-1397-56a9-ae81-7fcc7bd40cc6/scratchpad/menu/'
mk0=Image.open(D+'wordmark-brown.png')
mark=Image.new('RGBA',mk0.size,(24,20,18,0));mark.putalpha(mk0.getchannel('A'))
mark.save(D+'wordmark-brown.png')   # file name kept, colour is now black
def clean(p,reg,patch,ins_x,ins_t,ins_b):
    im=Image.open(D+f'hi/p-{p:02d}.png').convert('RGB')
    x0,y0,x1,y1=reg;w,h=x1-x0,y1-y0
    pt=im.crop(patch);t=Image.new('RGB',(w,h));x=0;fl=False
    while x<w:
        t.paste(pt.transpose(Image.FLIP_LEFT_RIGHT) if fl else pt,(x,0));x+=pt.width;fl=not fl
    m=Image.new('L',(w,h),0);m.paste(255,(ins_x,ins_t,w-ins_x,h-ins_b));m=m.filter(ImageFilter.GaussianBlur(10))
    im.paste(t,(x0,y0),m);return im
def put(im,cx,cy,w):
    k=w/mark.width;m=mark.resize((w,round(mark.height*k)),Image.LANCZOS);im.paste(m,(cx-w//2,cy-m.height//2),m)
os.makedirs(D+'hi2',exist_ok=True)
im=clean(1,(460,2050,1200,2340),(80,2050,520,2340),45,45,45);put(im,827,2200,430);im.save(D+'hi2/p-01.png')
im=clean(2,(420,168,1240,540),(80,168,500,540),45,30,45);put(im,827,345,520);im.save(D+'hi2/p-02.png')
for p in range(3,28):
    Image.open(D+f'hi/p-{p:02d}.png').save(D+f'hi2/p-{p:02d}.png')
