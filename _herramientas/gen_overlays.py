import numpy as np, subprocess, sys, os
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
FPS=24

def encode(name, frames_iter, w, h, n, crf=20, extra=None):
    vf=f"scale=1920:1080:flags=bicubic,format=yuv420p" if (w,h)!=(1920,1080) else "format=yuv420p"
    cmd=['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{w}x{h}','-r',str(FPS),'-i','-',
         '-vf',vf,'-c:v','libx264','-preset','slow','-crf',str(crf),'-movflags','+faststart',os.path.join(out,name)]
    p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    for f in frames_iter: p.stdin.write(np.clip(f,0,255).astype(np.uint8).tobytes())
    p.stdin.close(); p.wait()

# --- light leaks: soft coloured blobs drifting on black, seamless loop ---
def light_leak(seed, palette, secs=8, w=640, h=360):
    rng=np.random.default_rng(seed); n=secs*FPS
    yy,xx=np.mgrid[0:h,0:w]; xx=xx/w; yy=yy/h
    blobs=[dict(c=np.array(palette[i%len(palette)],float), cx=rng.uniform(-.1,1.1), cy=rng.uniform(-.1,1.1),
                ax=rng.uniform(.1,.35), ay=rng.uniform(.1,.3), r=rng.uniform(.18,.45), ph=rng.uniform(0,6.28),
                k=int(rng.integers(1,3))) for i in range(5)]
    def gen():
        for t in range(n):
            a=2*np.pi*t/n; img=np.zeros((h,w,3))
            for b in blobs:
                cx=b['cx']+b['ax']*np.sin(b['k']*a+b['ph']); cy=b['cy']+b['ay']*np.cos(b['k']*a+b['ph'])
                inten=0.65+0.35*np.sin(2*b['k']*a+b['ph']*2)
                g=np.exp(-(((xx-cx)*1.6)**2+(yy-cy)**2)/(2*b['r']**2))*inten
                img=1-(1-img)*(1-g[...,None]*b['c']/255)   # screen
            yield img*255
    return gen(), w, h, n

palettes={
 'calido-naranja':[(255,120,30),(255,190,90),(255,70,40)],
 'dorado':[(255,200,80),(255,230,150),(240,150,40)],
 'rosa-magenta':[(255,90,140),(255,150,190),(200,60,200)],
 'verde-botanico':[(120,220,90),(200,255,140),(60,170,90)],
 'azul-frio':[(80,150,255),(140,210,255),(90,90,230)],
 'arcoiris':[(255,80,60),(255,210,70),(80,220,140),(90,140,255)],
}
for i,(k,pal) in enumerate(palettes.items()):
    g,w,h,n=light_leak(i+1,pal); encode(f'light-leak-{k}.mp4',g,w,h,n,crf=20)

# --- bokeh: soft discs drifting, seamless loop ---
def bokeh(seed, cols, secs=8, w=960, h=540, count=45):
    rng=np.random.default_rng(seed); n=secs*FPS
    yy,xx=np.mgrid[0:h,0:w].astype(float)
    P=[dict(x=rng.uniform(0,w), y=rng.uniform(0,h), r=rng.uniform(8,60), a=rng.uniform(.15,.6),
            c=np.array(cols[rng.integers(len(cols))],float)/255, vx=int(rng.integers(-1,2)) or 1, amp=rng.uniform(5,40), ph=rng.uniform(0,6.28)) for _ in range(count)]
    def gen():
        for t in range(n):
            s=t/n; img=np.zeros((h,w,3))
            for p in P:
                x=(p['x']+p['vx']*s*w)%w; y=p['y']+p['amp']*np.sin(2*np.pi*s+p['ph'])
                for ox in (-w,0,w):
                    d=np.sqrt((xx-x-ox)**2+(yy-y)**2)
                    m=np.clip((p['r']-d)/2.5,0,1)*(0.75+0.25*np.clip(d/p['r'],0,1))*p['a']
                    if m.max()>0: img=1-(1-img)*(1-m[...,None]*p['c'])
            yield img*255
    return gen(), w, h, n
encode('bokeh-dorado.mp4',*bokeh(11,[(255,210,120),(255,180,90),(255,240,200)]),crf=20)
encode('bokeh-verde.mp4',*bokeh(12,[(170,240,140),(220,255,170),(110,200,120)]),crf=20)
encode('bokeh-blanco.mp4',*bokeh(13,[(255,255,255),(230,240,255)]),crf=20)

# --- dust & scratches on black (use Screen/Add blend) ---
def dust(seed, secs=6, w=1920, h=1080):
    rng=np.random.default_rng(seed); n=secs*FPS
    def gen():
        for t in range(n):
            img=np.zeros((h,w),float)
            for _ in range(rng.integers(8,30)):
                x,y=rng.integers(0,w),rng.integers(0,h); r=rng.integers(1,4); v=rng.uniform(.4,1)
                img[max(0,y-r):y+r,max(0,x-r):x+r]=np.maximum(img[max(0,y-r):y+r,max(0,x-r):x+r],v)
            for _ in range(rng.integers(0,3)):   # hairs
                x0,y0=rng.integers(0,w),rng.integers(0,h); L=rng.integers(15,70); ang=rng.uniform(0,6.28)
                for k in range(L):
                    xi=int(x0+k*np.cos(ang+0.03*k)); yi=int(y0+k*np.sin(ang+0.03*k))
                    if 0<=xi<w and 0<=yi<h: img[yi,xi]=0.8
            if rng.random()<0.6:                   # vertical scratch
                x=rng.integers(0,w); img[:,x]=np.maximum(img[:,x],rng.uniform(.2,.6))
            yield np.repeat((img*255)[...,None],3,2)
    return gen(), w, h, n
encode('polvo-y-rayas.mp4',*dust(21),crf=22)
