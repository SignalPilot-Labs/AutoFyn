import sympy as sp, sys, time, math
from sympy import symbols,together,fraction,expand,cancel
log=print
def flush(): sys.stdout.flush()
sa,ca,sA,cA = sp.symbols('sa ca sA cA')
tb,tg = sp.symbols('tb tg')
# half-angle for beta, gamma
sb=2*tb/(1+tb**2); cb=(1-tb**2)/(1+tb**2)
sg=2*tg/(1+tg**2); cg=(1-tg**2)/(1+tg**2)
# build atoms via sum formulas (keep as rational functions)
def sadd(sa_,ca_,sb_,cb_): return (sa_*cb_+ca_*sb_, ca_*cb_-sa_*sb_)
# sin(al+A), cos(al+A)
saa=sa*cA+ca*sA; caa=ca*cA-sa*sA
# sin(al+ga), cos(al+ga)  -> sag,cag
sag,cag=sadd(sa,ca,sg,cg)
# sin(al+be),cos(al+be) -> sab,cab
sab,cab=sadd(sa,ca,sb,cb)
# sin(A+2al+ga)=sin((A+al)+(al+ga))
sA2ag=saa*cag+caa*sag
# sin(A+2al+be)=sin((A+al)+(al+be))
sA2ab=saa*cab+caa*sab
kx=1-sg*ca/(2*sag); ky=sg*sa/(2*sag)
lxu=cA - sb*caa/(2*sab); lyu=sA - sb*saa/(2*sab)
b = sp.symbols('b')
Kx,Ky=kx,ky
Lx,Ly=b*lxu,b*lyu
K2=sp.cancel(Kx**2+Ky**2); L2=sp.cancel(Lx**2+Ly**2)
detKL=sp.cancel(Kx*Ly-Ky*Lx)
Ax=sp.cancel((Ly*K2-Ky*L2)/detKL); Ay=sp.cancel((Kx*L2-Lx*K2)/detKL)
log("A' ops",sp.count_ops(Ax),sp.count_ops(Ay)); flush()
CBx=b*cA-1; CBy=b*sA
Rx=saa*CBx - caa*CBy
Ry=caa*CBx + saa*CBy
ABx=sp.cancel(Ax-1); ABy=sp.cancel(Ay)
G=sp.cancel(ABx*Ry - ABy*Rx)
Gp=sp.Poly(G,b)
G2,G1,G0=[sp.cancel(c) for c in Gp.all_coeffs()]
log("Gi ops",sp.count_ops(G2),sp.count_ops(G1),sp.count_ops(G0)); flush()
P=2*sag**2
Q=sg*sA2ag - 2*sag**2
R=2*sab**2 - sb*sA2ab
S=-2*sab**2
C=sp.cancel(P*S-Q*R)
log("C ops",sp.count_ops(C)); flush()
g=sp.cancel(G2*Q**2 - G1*Q*P + G0*P**2)
log("g ops",sp.count_ops(g)); flush()
# numeric sanity (scalene A=55,al=25,be=17.191,ga=32.923)
import numpy as np
def numev2(e):
    f=sp.lambdify((sa,ca,sA,cA,tb,tg),e,'numpy')
    Ad,ald,bed,gad=55,25,17.191,32.923
    vals=[np.sin(np.radians(ald)),np.cos(np.radians(ald)),np.sin(np.radians(Ad)),np.cos(np.radians(Ad)),np.tan(np.radians(bed)/2),np.tan(np.radians(gad)/2)]
    return float(f(*vals))
log("g on locus:",numev2(g)," C on locus:",numev2(C)); flush()
# clear denominators in tb,tg
t0=time.time()
ght=together(g); ghn,ghd=fraction(ght); ghn=expand(ghn)
Cht=together(C); Chn,Chd=fraction(Cht); Chn=expand(Chn)
log("cleared t",round(time.time()-t0,2),"ghn ops",sp.count_ops(ghn),"Chn ops",sp.count_ops(Chn)); flush()
# polys in tg over ZZ(sa,ca,sA,cA,tb)
base=sp.FractionField(sp.ZZ,sa,ca,sA,cA,tb)
t1=time.time()
Cp=sp.Poly(Chn,tg,domain=base); gp=sp.Poly(ghn,tg,domain=base)
log("deg tg Chn",Cp.degree(),"deg tg ghn",gp.degree(),"t",round(time.time()-t1,2)); flush()
q,r=gp.div(Cp)
log("div done t",round(time.time()-t1,2)," r zero?",r.is_zero," r ops",sp.count_ops(r.as_expr())); flush()
if not r.is_zero:
    # also try adding pyth relations for sa,ca,sA,cA via extending base? Hard. Print remainder degree.
    re=sp.cancel(r.as_expr())
    log("rem on locus:",numev2(re)); flush()
    log("rem deg tg:",sp.Poly(sp.together(re),tg).degree() if re!=0 else 0)
