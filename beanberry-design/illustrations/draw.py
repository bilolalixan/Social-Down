import math,random
INK='#4b2e24';BG='#fdf3ea'
def hatch(x0,y0,x1,y1,gap=4,ang=-55,sw=.8,clip=None,jit=.6,seed=1):
    r=random.Random(seed);out=[];a=math.radians(ang);dx,dy=math.cos(a),math.sin(a)
    cx,cy=(x0+x1)/2,(y0+y1)/2;L=math.hypot(x1-x0,y1-y0)
    n=int(L/gap)
    for i in range(-n//2,n//2):
        px=cx-dy*i*gap;py=cy+dx*i*gap
        out.append(f'<line x1="{px-dx*L/2+r.uniform(-jit,jit):.1f}" y1="{py-dy*L/2:.1f}" x2="{px+dx*L/2:.1f}" y2="{py+dy*L/2+r.uniform(-jit,jit):.1f}" stroke-width="{sw}"/>')
    return ''.join(out)
def leaf(x,y,ang,s=40,w=.36,seed=0,fill=True):
    a=math.radians(ang);ca,sa=math.cos(a),math.sin(a)
    def P(u,v):return (x+u*ca-v*sa,y+u*sa+v*ca)
    p0=P(0,0);p1=P(s*.5,-s*w);p2=P(s,0);p3=P(s*.5,s*w)
    d=f'M{p0[0]:.1f},{p0[1]:.1f} Q{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} Q{p3[0]:.1f},{p3[1]:.1f} {p0[0]:.1f},{p0[1]:.1f}Z'
    o=f'<path d="{d}" fill="{BG}" stroke-width="1.4"/>'
    m=P(s*.95,0);o+=f'<line x1="{p0[0]:.1f}" y1="{p0[1]:.1f}" x2="{m[0]:.1f}" y2="{m[1]:.1f}" stroke-width="1"/>'
    for k in range(1,6):
        u=s*k/6.5;b1=P(u,0);e1=P(u+s*.14,-s*w*.78*(1-k/8));e2=P(u+s*.14,s*w*.78*(1-k/8))
        o+=f'<line x1="{b1[0]:.1f}" y1="{b1[1]:.1f}" x2="{e1[0]:.1f}" y2="{e1[1]:.1f}" stroke-width=".7"/><line x1="{b1[0]:.1f}" y1="{b1[1]:.1f}" x2="{e2[0]:.1f}" y2="{e2[1]:.1f}" stroke-width=".7"/>'
    if fill:
        for k in range(3,9):
            u=s*k/10;b=P(u,s*w*.12);e=P(u+s*.08,s*w*.62*(1-abs(k-5)/9))
            o+=f'<line x1="{b[0]:.1f}" y1="{b[1]:.1f}" x2="{e[0]:.1f}" y2="{e[1]:.1f}" stroke-width=".6"/>'
    return o
def cherry(x,y,r=11):
    o=f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*1.15}" fill="{BG}" stroke-width="1.4"/>'
    o+=f'<path d="M{x-r*.6},{y-r*.2} Q{x-r*.5},{y+r*.9} {x},{y+r*1.1}" fill="none" stroke-width=".8"/>'
    o+=hc(ell(x,y,r,r*1.15),x-r,y-r*1.2,x+r*.2,y+r*1.2,gap=2.6,ang=-60,sw=.6,seed=int(x))
    o+=f'<path d="M{x-2},{y+r*1.1} q2,3 4,0" fill="none" stroke-width="1"/>'
    return o
def svg(w,h,body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="{BG}"/><g fill="none" stroke="{INK}" stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>'
def clipped(id,d,inner):
    return f'<clipPath id="{id}"><path d="{d}"/></clipPath><g clip-path="url(#{id})">{inner}</g>'

_cid=[0]
def hc(path,x0,y0,x1,y1,**kw):
    _cid[0]+=1;i=f"hc{_cid[0]}"
    return f'<clipPath id="{i}"><path d="{path}"/></clipPath><g clip-path="url(#{i})">{hatch(x0,y0,x1,y1,**kw)}</g>'
def ell(cx,cy,rx,ry):
    return f"M{cx-rx},{cy} A{rx},{ry} 0 1,0 {cx+rx},{cy} A{rx},{ry} 0 1,0 {cx-rx},{cy}Z"
