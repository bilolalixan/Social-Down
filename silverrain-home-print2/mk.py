import re
BL=8.504;SL=28.35;W=412;H=489
off=BL+SL;TW=W+2*off;TH=H+2*off
def wrap(n):
    s=open(n+'.svg').read();s=re.sub(r'^<\?xml[^>]*>','',s)
    s=s.replace('width="412" height="489" viewBox="0 0 412 489"',f'x="{off}" y="{off}" width="{W}" height="{H}" viewBox="0 0 412 489" overflow="visible"',1)
    marks=[];L=14;G=BL+3
    for x in (off,off+W):
        for y0,y1 in ((off-G-L,off-G),(off+H+G,off+H+G+L)):marks.append(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y1}"/>')
    for y in (off,off+H):
        for x0,x1 in ((off-G-L,off-G),(off+W+G,off+W+G+L)):marks.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}"/>')
    out=f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{TW}pt" height="{TH}pt" viewBox="0 0 {TW} {TH}"><rect width="{TW}" height="{TH}" fill="#fff"/><rect x="{off-BL}" y="{off-BL}" width="{W+2*BL}" height="{H+2*BL}" fill="#000"/>{s}<g stroke="#000" stroke-width="0.5">{"".join(marks)}</g></svg>'
    open(n+'-print.svg','w').write(out)
for n in ('front','back'):wrap(n)
