import pickle, sympy as sp, math
from sympy import symbols, expand, N as Ne
with open('/tmp/geom/conds.pkl','rb') as f: d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
Kx=d['Kx'];Ky=d['Ky'];Kden=d['Kden'];Lx=d['Lx'];Ly=d['Ly'];Lden=d['Lden']
alpha=math.radians(10.140977272332982);beta=math.radians(21.08047146055647);gamma=math.radians(35.582220333404194)
Av=math.tan(alpha/2);Pv=math.tan((alpha+beta)/2);Gv=math.tan((alpha+gamma)/2)
pv=0.25;qv=0.75
subs={A:Av,P:Pv,G:Gv,p:pv,q:qv}
Kxn=float(Kx.subs(subs));Kyn=float(Ky.subs(subs));Kdn=float(Kden.subs(subs))
Lxn=float(Lx.subs(subs));Lyn=float(Ly.subs(subs));Ldn=float(Lden.subs(subs))
print(f"K=({Kxn/Kdn:.6f},{Kyn/Kdn:.6f})  expect (0.6,0.071546)")
print(f"L=({Lxn/Ldn:.6f},{Lyn/Ldn:.6f})  expect (0.210434,0.478582)")
