import pickle, sympy as sp
from sympy import symbols, expand, Poly, factor, simplify, N
with open('/tmp/geom/poly.pkl','rb') as f: d=pickle.load(f)
A,P,G,p,q = symbols('A P G p q')
for k in d: d[k]=d[k].subs({str(s):s for s in [A,P,G,p,q]})
TGT=d['TGT']; fA=d['fA']; fB=d['fB']

# Use the numerical config from rays.py: A=(0,0),B=(1,0),C=(0.25,0.75) so p=0.25,q=0.75.
# alpha=10.14deg -> A=tan(alpha/2)=tan(5.07deg). beta=21.08 -> P=tan((alpha+beta)/2)=tan(15.6deg). gamma=35.58-> G=tan((alpha+gamma)/2)=tan(22.86deg)
import math
alpha=math.radians(10.140977272332982); beta=math.radians(21.08047146055647); gamma=math.radians(35.582220333404194)
Av=math.tan(alpha/2); Pv=math.tan((alpha+beta)/2); Gv=math.tan((alpha+gamma)/2)
pv=0.25; qv=0.75
subs={A:Av,P:Pv,G:Gv,p:pv,q:qv}
print("TGT at valid config:", float(TGT.subs(subs)))
print("fA at valid config:", float(fA.subs(subs)))
print("fB at valid config:", float(fB.subs(subs)))
