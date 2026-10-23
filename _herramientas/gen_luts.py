import numpy as np, os, sys
out=sys.argv[1]; os.makedirs(out,exist_ok=True); N=33
g=np.linspace(0,1,N); b,gg,r=np.meshgrid(g,g,g,indexing='ij')   # cube order: R fastest
rgb=np.stack([r,gg,b],-1).reshape(-1,3)
lum=lambda c:(c@np.array([.2126,.7152,.0722]))[:,None]
def sat(c,s): L=lum(c); return L+(c-L)*s
def curve(c,lift=0,gamma=1,gain=1): return np.clip(lift+(gain-lift)*np.clip(c,0,1)**gamma,0,1)
def scurve(c,k): return np.clip(c+k*(c-0.5)*(1-np.abs(2*c-1)),0,1)
def split(c,sh,hi,amt=.12):
    L=lum(c); return c+amt*((1-L)*(np.array(sh)-.5)+L*(np.array(hi)-.5))
looks={
 'botanico-verde-suave': lambda c: sat(curve(split(c,(.4,.6,.5),(.6,.62,.45),.18),lift=.04,gamma=.95),.92),
 'calido-dorado':        lambda c: sat(scurve(c*np.array([1.06,1.0,.88]),.15),1.05),
 'frio-azulado':         lambda c: sat(scurve(c*np.array([.92,1.0,1.08]),.12),.95),
 'pelicula-desvanecida': lambda c: sat(curve(scurve(c,.2),lift=.08,gain=.94),.8),
 'teal-naranja':         lambda c: sat(scurve(split(c,(.3,.55,.6),(.7,.55,.4),.3),.18),1.1),
 'pastel-mate':          lambda c: sat(curve(c,lift=.12,gamma=.9,gain=.97),.75),
 'blanco-y-negro-contraste': lambda c: np.repeat(scurve(lum(c),.35),3,1),
 'sepia-vintage':        lambda c: curve(lum(c)*np.array([1.07,.95,.78])+.03,lift=.05,gain=.95),
 'verano-vibrante':      lambda c: sat(scurve(c*np.array([1.04,1.02,.95]),.2),1.25),
 'bosque-oscuro':        lambda c: sat(curve(split(c,(.35,.55,.5),(.55,.6,.45),.2),gamma=1.15,gain=.95),.85),
}
for name,f in looks.items():
    o=np.clip(f(rgb.copy()),0,1)
    with open(os.path.join(out,f'{name}.cube'),'w') as fh:
        fh.write(f'TITLE "{name}"\nLUT_3D_SIZE {N}\nDOMAIN_MIN 0.0 0.0 0.0\nDOMAIN_MAX 1.0 1.0 1.0\n')
        fh.writelines(f'{x:.6f} {y:.6f} {z:.6f}\n' for x,y,z in o)
print(len(looks))
