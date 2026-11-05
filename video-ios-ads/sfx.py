import json,sys,wave,numpy as np
SR=44100
src,out=sys.argv[1],sys.argv[2]
ev=json.load(open(src));TOTAL=43.5
buf=np.zeros(int(SR*TOTAL)+SR)
rng=np.random.default_rng(7)
def tt(d):return np.arange(int(SR*d))/SR
def bell(f,d=.4,dec=9,h=(1,.4,.15)):
    t=tt(d);y=sum(a*np.sin(2*np.pi*f*(i+1)*t) for i,a in enumerate(h));return y*np.exp(-dec*t)*np.minimum(1,t/.004)
def pop(p=1):
    t=tt(.14);f=(820*p)*(1-.45*np.minimum(1,t/.06));ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t/.028)*.9
def tick(p=1):
    t=tt(.03);return (np.sin(2*np.pi*3400*p*t)*np.exp(-t/.004)+.3*rng.standard_normal(len(t))*np.exp(-t/.002))*.6
def thud(f=95):
    t=tt(.16);return np.sin(2*np.pi*f*t*(1-.3*t/.16))*np.exp(-t/.05)
def whoosh(d=.4,up=True):
    n=int(SR*d);x=rng.standard_normal(n);t=np.arange(n)/n
    fc=(300+3800*t**1.5) if up else (4000-3500*t)
    out=np.zeros(n);lp=0;bp=0
    for i in range(n):  # state-variable band-pass
        f=2*np.sin(np.pi*min(fc[i],9000)/SR);q=.35
        hp=x[i]-lp-q*bp;bp+=f*hp;lp+=f*bp;out[i]=bp
    env=np.sin(np.pi*t)**2
    return out*env*.55/max(1e-9,np.abs(out).max())
def seq(notes,gap,**k):
    L=int(SR*(gap*len(notes)+.6));y=np.zeros(L)
    for i,f in enumerate(notes):
        b=bell(f,**k);s=int(SR*gap*i);y[s:s+len(b)]+=b[:L-s]
    return y
def fit(y,n=int(SR*.5)):
    return np.pad(y,(0,max(0,n-len(y))))[:n]
S={
 'pop':lambda e:pop(e.get('p',1)),
 'tick':lambda e:tick(e.get('p',1)),
 'tap':lambda e:fit(thud(90))+fit(tick(.7))*.6,
 'sent':lambda e:fit(whoosh(.28,True)*.9)+fit(np.pad(pop(1.5),(int(SR*.18),0)))*.5,
 'whoosh':lambda e:whoosh(e.get('d',.4),True),
 'chime':lambda e:seq([1046,1319,1568],.11,d=.5,dec=7)*.8,
 'recv':lambda e:seq([1175,1568],.09,d=.4,dec=10)*.8,
 'success':lambda e:seq([1319,1760],.12,d=.6,dec=6)*.9,
 'alert':lambda e:fit(thud(70))*1.1+fit(np.pad(bell(520,.4,7,(1,.3)),(int(SR*.08),0)))*.6,
}
for e in ev:
    y=S[e['n']](e)*e.get('v',.6)
    s=int(e['t']*SR);buf[s:s+len(y)]+=y[:len(buf)-s]
buf=np.tanh(buf*1.1)
buf/=max(1e-9,np.abs(buf).max());buf*=.8
pcm=(buf*32767).astype('<i2')
with wave.open(out,'wb') as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes(pcm.tobytes())
print('ok',len(ev))
