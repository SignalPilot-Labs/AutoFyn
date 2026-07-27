import sympy as sp, sys, time, math
from sympy import symbols,together,fraction,expand,cancel
log=print
def flush(): sys.stdout.flush()
sa,ca,sA,cA = sp.symbols('sa ca sA cA')
tb,tg = sp.symbols('tb tg')
sb=2*tb/(1+tb**2); cb=(1-tb**2)/(1+tb**2)
sg=2*tg/(1+tg**2); cg=(1-tg**2)/(1+tg**2)
def sadd(sa_,ca_,sb_,cb_): return (sa_*cb_+ca_*sb_, ca_*cb_-sa_*sb_)
saa=sa*cA+ca*sA; caa=ca*cA-sa*sA
sag,cag=sadd(sa,ca,sg,cg)
sab,cab=sadd(sa,ca,sb,cb)
sA2ag=saa*cag+caa*sag
sA2ab=saa*cab+caa*sab
kx=1-sg*ca/(2*sag); ky=sg*sa/(2*sag)
lxu=cA - sb*caa/(2*sab); lyu=sA - sb*saa/(2*sab)
b = sp.symbols('b')
Kx,Ky=kx,ky
Lx,Ly=b*lxu,b*lyu
# incidences directly
# dir CK = (cos(A+pi+al+ga), sin(...)) = (-cos(A+al+ga), -sin(A+al+ga))
# sin(A+al+ga)=saa*cg+caa*sg ; cos=caa*cg-saa*sg
sAag=saa*cg+caa*sg; cAag=caa*cg-saa*sg
dirCKx=-cAag; dirCKy=-sAag
conK=sp.cancel((Kx-b*cA)*dirCKy - (Ky-b*sA)*dirCKx)   # (K-C) x dirCK
# dir BL = (cos(pi-al-be), sin(pi-al-be)) = (-cos(al+be), sin(al+be)) = (-cab, sab)
dirBLx=-cab; dirBLy=sab
conL=sp.cancel((Lx-1)*dirBLy - (Ly-0)*dirBLx)         # (L-B) x dirBL  (B=(1,0))
log("conK ops",sp.count_ops(conK),"conL ops",sp.count_ops(conL)); flush()
# collect in b
cKp=sp.Poly(conK,b); cLp=sp.Poly(conL,b)
log("deg b conK",cKp.degree(),"deg b conL",cLp.degree()); flush()
# conK = k0 + k1*b ; conL = l0 + l1*b
kcoeffs=cKp.all_coeffs(); lcoeffs=cLp.all_coeffs()
# pad
def pad(cs,n):
    cs=list(cs); return [sp.S(0)]*(n-len(cs))+cs
n=max(len(kcoeffs),len(lcoeffs))
kcoeffs=pad(kcoeffs,n); lcoeffs=pad(lcoeffs,n)
log("kcoeffs deg",len(kcoeffs),"lcoeffs deg",len(lcoeffs)); flush()
# if degree 1: conK=k1*b+k0, conL=l1*b+l0. consistency: k0*l1-l0*k1=0 (b=-k0/k1=-l0/l1)
if len(kcoeffs)==2:
    k1,k0=kcoeffs; l1,l0=lcoeffs
else:
    k1,k0=kcoeffs[-1],kcoeffs[-2]; l1,l0=lcoeffs[-1],lcoeffs[-2]
Ccon=sp.cancel(k0*l1-l0*k1)
log("Ccon (consistency) ops",sp.count_ops(Ccon)); flush()
# numeric check
import numpy as np
def numev2(e):
    f=sp.lambdify((sa,ca,sA,cA,tb,tg),e,'numpy')
    Ad,ald,bed,gad=55,25,17.191,32.923
    vals=[np.sin(np.radians(ald)),np.cos(np.radians(ald)),np.sin(np.radians(Ad)),np.cos(np.radians(Ad)),np.tan(np.radians(bed)/2),np.tan(np.radians(gad)/2)]
    return float(f(*vals))
log("Ccon on locus (want 0):",numev2(Ccon)); flush()
flush()
# Now compute G (direction cross product) and substitute b=-k0/k1, clear k1^2
K2=sp.cancel(Kx**2+Ky**2); L2=sp.cancel(Lx**2+Ly**2)
detKL=sp.cancel(Kx*Ly-Ky*Lx)
Ax=sp.cancel((Ly*K2-Ky*L2)/detKL); Ay=sp.cancel((Kx*L2-Lx*K2)/detKL)
CBx=b*cA-1; CBy=b*sA
Rx=saa*CBx - caa*CBy
Ry=caa*CBx + saa*CBy
ABx=sp.cancel(Ax-1); ABy=sp.cancel(Ay)
G=sp.cancel(ABx*Ry - ABy*Rx)
Gp=sp.Poly(G,b)
Gcoeffs=Gp.all_coeffs()
log("G deg b",Gp.degree()); flush()
# G = G2*b^2+G1*b+G0 (deg 2). b=-k0/k1. G(-k0/k1)*k1^2 = G2*k0^2 - G1*k0*k1 + G0*k1^2
G2,G1,G0=pad(Gcoeffs,3)
g=sp.cancel(G2*k0**2 - G1*k0*k1 + G0*k1**2)
log("g ops",sp.count_ops(g)); flush()
log("g on locus (want 0):",numev2(g)); flush()
# clear denoms
t0=time.time()
ght=together(g); ghn,ghd=fraction(ght); ghn=expand(ghn)
Cht=together(Ccon); Chn,Chd=fraction(Cht); Chn=expand(Chn)
log("cleared t",round(time.time()-t0,2),"ghn ops",sp.count_ops(ghn),"Chn ops",sp.count_ops(Chn)); flush()
# polys in tg over QQ(sa,ca,sA,cA,tb)
gens=[sa,ca,sA,cA,tb]
base=sp.FractionField(sp.ZZ, gens)
t1=time.time()
Cp=sp.Poly(Chn,tg,domain=base); gp=sp.Poly(ghn,tg,domain=base)
log("deg tg Chn",Cp.degree(),"deg tg ghn",gp.degree(),"t",round(time.time()-t1,2)); flush()
q,r=gp.div(Cp)
log("div done t",round(time.time()-t1,2)," r zero?",r.is_zero," r ops",sp.count_ops(r.as_expr()) if not r.is_zero else 0); flush()
if not r.is_zero:
    re=sp.cancel(r.as_expr())
    log("rem on locus:",numev2(re)); flush()
