import re,base64,io
from PIL import Image
import numpy as np
F=open('front.svg').read().split('\n')
def d(i):return re.search(r' d="([^"]*)"',F[i-1]).group(1)
leaf=d(219);house=d(254);recycle=d(325);border=d(286)
# flame raster -> white png w/ alpha
im=Image.open('flame-1.png').convert('L');a=np.asarray(im)
rgba=np.zeros(a.shape+(4,),dtype='uint8');rgba[...,:3]=255;rgba[...,3]=a
buf=io.BytesIO();Image.fromarray(rgba).save(buf,'PNG');flame=base64.b64encode(buf.getvalue()).decode()
FONT='font-family="Inter Display, Inter, sans-serif"'
def T(x,y,s,txt,anchor='start',ls=0,w=400):
    return f'<text x="{x}" y="{y}" font-size="{s}" font-weight="{w}" letter-spacing="{ls}" text-anchor="{anchor}" fill="#fff" {FONT}>{txt}</text>'
def car_office(cx,base):
    s=1.08
    car=f'<g transform="translate({cx-22.5:.2f},{base-14*s:.2f}) scale({s})"><path fill="#fff" fill-rule="evenodd" d="M2 9 L3.2 5.6 C3.5 4.8 4.2 4.3 5 4.3 H15 C15.8 4.3 16.4 4.7 16.9 5.3 L19.2 7.6 L21.6 8.2 C22.4 8.4 23 9.1 23 9.9 V11.2 H21.2 C20.9 12.6 19.7 13.6 18.2 13.6 C16.7 13.6 15.5 12.6 15.2 11.2 H8.8 C8.5 12.6 7.3 13.6 5.9 13.6 C4.4 13.6 3.2 12.6 2.9 11.2 H1 V10.4 C1 9.8 1.4 9.3 2 9 Z"/><path fill="#000" d="M5 5.7 H10.2 V8.4 H4.1 Z M11.4 5.7 H15 C15.3 5.7 15.6 5.8 15.8 6 L17.9 8.4 H11.4 Z"/><circle cx="5.9" cy="11.6" r="2.1" fill="#000"/><circle cx="5.9" cy="11.6" r="1" fill="#fff"/><circle cx="18.2" cy="11.6" r="2.1" fill="#000"/><circle cx="18.2" cy="11.6" r="1" fill="#fff"/></g>'
    ox=cx-22.5+23*s+3
    off=f'<g transform="translate({ox:.2f},{base-20*s:.2f}) scale({s})"><path fill="#fff" fill-rule="evenodd" d="M1 20 V2.6 C1 2.2 1.2 2 1.6 2 H10.4 C10.8 2 11 2.2 11 2.6 V8 H14.4 C14.8 8 15 8.2 15 8.6 V20 H12.5 V17 H3.5 V20 Z"/><path fill="#000" d="M3 4 H5 V6 H3 Z M6 4 H8 V6 H6 Z M3 7.4 H5 V9.4 H3 Z M6 7.4 H8 V9.4 H6 Z M3 10.8 H5 V12.8 H3 Z M6 10.8 H8 V12.8 H6 Z M3 14 H5 V16 H3 Z M6 14 H8 V16 H6 Z M11.8 10.5 H13 V12 H11.8 Z M11.8 13.4 H13 V14.9 H11.8 Z M11.8 16 H13 V17 H11.8 Z"/></g>'
    return car+off

def car_icon(cx,cy):
    s=1.15
    return f'<g transform="translate({cx-11.5*s:.2f},{cy-7*s:.2f}) scale({s})"><path fill="#fff" fill-rule="evenodd" d="M2 9 L3.2 5.6 C3.5 4.8 4.2 4.3 5 4.3 H15 C15.8 4.3 16.4 4.7 16.9 5.3 L19.2 7.6 L21.6 8.2 C22.4 8.4 23 9.1 23 9.9 V11.2 H21.2 C20.9 12.6 19.7 13.6 18.2 13.6 C16.7 13.6 15.5 12.6 15.2 11.2 H8.8 C8.5 12.6 7.3 13.6 5.9 13.6 C4.4 13.6 3.2 12.6 2.9 11.2 H1 V10.4 C1 9.8 1.4 9.3 2 9 Z"/><path fill="#000" d="M5 5.7 H10.2 V8.4 H4.1 Z M11.4 5.7 H15 C15.3 5.7 15.6 5.8 15.8 6 L17.9 8.4 H11.4 Z"/><circle cx="5.9" cy="11.6" r="2.1" fill="#000"/><circle cx="5.9" cy="11.6" r="1" fill="#fff"/><circle cx="18.2" cy="11.6" r="2.1" fill="#000"/><circle cx="18.2" cy="11.6" r="1" fill="#fff"/></g>'
def office_icon(cx,cy):
    s=1.05
    return f'<g transform="translate({cx-7.5*s:.2f},{cy-11*s:.2f}) scale({s})"><path fill="#fff" fill-rule="evenodd" d="M1 20 V2.6 C1 2.2 1.2 2 1.6 2 H10.4 C10.8 2 11 2.2 11 2.6 V8 H14.4 C14.8 8 15 8.2 15 8.6 V20 H12.5 V17 H3.5 V20 Z"/><path fill="#000" d="M3 4 H5 V6 H3 Z M6 4 H8 V6 H6 Z M3 7.4 H5 V9.4 H3 Z M6 7.4 H8 V9.4 H6 Z M3 10.8 H5 V12.8 H3 Z M6 10.8 H8 V12.8 H6 Z M3 14 H5 V16 H3 Z M6 14 H8 V16 H6 Z M11.8 10.5 H13 V12 H11.8 Z M11.8 13.4 H13 V14.9 H11.8 Z M11.8 16 H13 V17 H11.8 Z"/></g>'
cy=362
def ring(cx):return f'<circle cx="{cx}" cy="{cy}" r="25" fill="none" stroke="#fff" stroke-width="1"/>'
def front():
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="412pt" height="591pt" viewBox="0 0 412 591"><rect width="412" height="591" fill="#000"/>',
     f'<path fill="#fff" fill-rule="nonzero" d="{border}"/>']
    para=['Изысканный аромат для дома, дарящий','ощущение спокойствия и гармонии','в вашем пространстве. Идеально подходит','для белья, подушек, штор и жилых','помещений.']
    for k,t in enumerate(para):out.append(T(46,68+17*k,14.5,t))
    out.append('<rect x="42" y="152" width="328" height="1" fill="#fff"/>')
    out.append(T(46,190,14.5,'СПОСОБ ПРИМЕНЕНИЯ'))
    for k,t in enumerate(['Распылите 2–3 раза на текстиль или','в воздух по мере необходимости.']):out.append(T(46,216+19*k,14.5,t))
    out.append('<rect x="42" y="262" width="328" height="1" fill="#fff"/>')
    X=[67,159.7,252.3,345]
    for cx in X:out.append(ring(cx))
    out.append(f'<g transform="translate({X[0]-75.9:.2f},{cy-402.6:.2f})"><path fill="#fff" d="{leaf}"/></g>')
    out.append(f'<g transform="translate({X[3]-335:.2f},{cy-402:.2f})"><path fill="#fff" d="{house}"/></g>')
    out.append(car_icon(X[1],cy));out.append(office_icon(X[2],cy))
    labs={X[0]:['ДЛЯ БЕЛЬЯ И','ПОМЕЩЕНИЙ'],X[1]:['ДЛЯ','АВТО'],X[2]:['ДЛЯ','ОФИСА'],X[3]:['ГАРМОНИЯ В','ВАШЕМ ДОМЕ']}
    for cx,l in labs.items():
        for k,t in enumerate(l):out.append(T(cx,cy+25+19+k*13,10,t,'middle',.2))
    out.append(T(46,501,14.5,'SILVER RAIN HOME',w=500))
    out.append(T(46,524,11.5,'Ташкент, Узбекистан'))
    out.append(T(46,542,11.5,'www.silverrain.asia'))
    out.append(T(294,501,14.5,'30 мл',w=500))
    out.append(f'<image x="294" y="513" width="38" height="38" href="data:image/png;base64,{flame}"/>')
    out.append(f'<path fill="#fff" d="{recycle}"/>')
    out.append('</svg>');return '\n'.join(out)
def back():
    B=open('back.svg').read().split('\n')
    keep=[l for i,l in enumerate(B,1) if i not in (118,119)]
    s='\n'.join(keep)
    extra=T(211,475,15,'СПРЕЙ ДЛЯ БЕЛЬЯ И ПОМЕЩЕНИЙ','middle',.6)+T(211,549,17,'30 мл','middle',.3)
    s=s.replace('width="412" height="591"','width="412pt" height="591pt"',1)
    return s.replace('</svg>',extra+'\n</svg>')
open('front-ru.svg','w').write(front());open('back-ru.svg','w').write(back())
