import sympy as sp, sys, time
from sympy import symbols,together,fraction,expand,cancel,factor,simplify,trigsimp
log=print
def flush(): sys.stdout.flush()
# raw sin/cos ring, all independent
sa,ca,sb,cb,sg,cg,sA,cA = sp.symbols('sa ca sb cb sg cg sA cA')
def sadd(sa_,ca_,sb_,cb_): return (sa_*cb_+ca_*sb_, ca_*cb_-sa_*sb_)
saa=sa*cA+ca*sA; caa=ca*cA-sa*sA
sag,cag=sadd(sa,ca,sg,cg)
sab,cab=sadd(sa,ca,sb,cb)
sA2ag=saa*cag+caa*sag
sA2ab=saa*cab+caa*sab
sAag=saa*cg+caa*sg; cAag=caa*cg-saa*sg
kx=1-sg*ca/(2*sag); ky=sg*sa/(2*sag)
lxu=cA - sb*caa/(2*sab); lyu=sA - sb*saa/(2*sab)
b=symbols('b')
Kx,Ky=kx,ky
Lx,Ly=b*lxu,b*lyu
dirCKx=-cAag; dirCKy=-sAag
conK=sp.cancel((Kx-b*cA)*dirCKy - (Ky-b*sA)*dirCKx)
dirBLx=-cab; dirBLy=sab
conL=sp.cancel((Lx-1)*dirBLy - Ly*dirBLx)
cKp=sp.Poly(conK,b); cLp=sp.Poly(conL,b)
kc=list(cKp.all_coeffs()); lc=list(cLp.all_coeffs())
def pad(cs,n): cs=list(cs); return [sp.S(0)]*(n-len(cs))+cs
n=max(len(kc),len(lc)); kc=pad(kc,n); lc=pad(lc,n)
k1,k0=kc; l1,l0=lc
log("=== conK coeffs (k1*b+k0) ===")
log("k1 =",sp.cancel(k1)); log("k0 =",sp.cancel(k0))
log("=== conL coeffs (l1*b+l0) ===")
log("l1 =",sp.cancel(l1)); log("l0 =",sp.cancel(l0))
Ccon=sp.cancel(k0*l1-l0*k1)
log("\nCcon =",Ccon)
flush()
