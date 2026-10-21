import sys
from PIL import Image, ImageFilter
import numpy as np
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB')
im=im.resize((int(im.width*1.6),int(im.height*1.6)),Image.LANCZOS)
ang=-28
big=im.rotate(ang,expand=True,resample=Image.BICUBIC)
a=np.asarray(big).astype(np.float32); k=80
c=np.cumsum(np.pad(a,((0,0),(k,k),(0,0)),mode='edge'),axis=1)
a=(c[:,2*k:]-c[:,:-2*k])/(2*k)
big=Image.fromarray(a.clip(0,255).astype(np.uint8)).rotate(-ang,resample=Image.BICUBIC)
W,H=big.size; cw,ch=im.size
big=big.crop(((W-cw)//2,(H-ch)//2,(W+cw)//2,(H+ch)//2)).filter(ImageFilter.GaussianBlur(6))
n=np.random.normal(0,7,(big.height,big.width,1))
Image.fromarray((np.asarray(big)+n).clip(0,255).astype(np.uint8)).save(out,quality=92)
