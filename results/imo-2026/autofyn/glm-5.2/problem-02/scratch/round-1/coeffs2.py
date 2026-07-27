import sympy as sp, sys, time
from sympy import symbols,together,fraction,expand,cancel,factor
def flush(): sys.stdout.flush()
log=print
sa,ca,sb,cb,sg,cg,sA,cA = sp.symbols('sa ca sb cb sg cg sA cA')
def sadd(a,b,c,d): return (a*d+b*c, b*d-a*c)
saa=sa*cA+ca*sA; caa=ca*cA-sa*sA
sag,cag=sadd(sa,ca,sg,cg); sab,cab=sadd(sa,ca,sb,cb)
sA2ag=saa*cag+caa*sag; sA2ab=saa*cab+caa*sab
sAag=saa*cg+caa*sg; cAag=caa*cg-saa*sg
kx=1-sg*ca/(2*sag); ky=sg*sa/(2*sag)
lxu=cA - sb*caa/(2*sab); lyu=sA - sb*saa/(2*sab)
b=symbols('b')
Kx,Ky=kx,ky; Lx,Ly=b*lxu,b*lyu
dirCKx=-cAag; dirCKy=-sAag
conK=sp.cancel((Kx-b*cA)*dirCKy - (Ky-b*sA)*dirCKx)
dirBLx=-cab; dirBLy=sab
conL=sp.cancel((Lx-1)*dirBLy - Ly*dirBLx)
cKp=sp.Poly(conK,b); cLp=sp.Poly(conL,b)
kc=list(cKp.all_coeffs()); lc=list(cLp.all_coeffs())
def pad(cs,n): cs=list(cs); return [sp.S(0)]*(n-len(cs))+cs
n=max(len(kc),len(lc)); kc=pad(kc,n); lc=pad(lc,n)
k1,k0=kc; l1,l0=lc
log("k1-(cA2+sA2)*sag =",sp.cancel(k1-(cA**2+sA**2)*sag))
log("l0+sab =",sp.cancel(l0+sab))
log("k0+(cA*sag2+sA*cg*sA2ag)/(2*sag) =",sp.cancel(k0+(cA*sag**2+sA*cg*sA2ag)/(2*sag)))
log("l1-(cA*sab2+sA*cb*sA2ab)/(2*sab) =",sp.cancel(l1-(cA*sab**2+sA*cb*sA2ab)/(2*sab)))
flush()
