import sympy as sp, sys, time
from sympy import symbols,together,fraction,expand,cancel
def flush(): sys.stdout.flush()
log=print
sa,ca,sA,cA = sp.symbols('sa ca sA cA')
tb,tg = sp.symbols('tb tg')
sb=2*tb/(1+tb**2); cb=(1-tb**2)/(1+tb**2)
sg=2*tg/(1+tg**2); cg=(1-tg**2)/(1+tg**2)
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
K2=sp.cancel(Kx**2+Ky**2); L2=sp.cancel(Lx**2+Ly**2)
detKL=sp.cancel(Kx*Ly-Ky*Lx)
Ax=sp.cancel((Ly*K2-Ky*L2)/detKL); Ay=sp.cancel((Kx*L2-Lx*K2)/detKL)
CBx=b*cA-1; CBy=b*sA
Rx=saa*CBx - caa*CBy; Ry=caa*CBx + saa*CBy
ABx=sp.cancel(Ax-1); ABy=sp.cancel(Ay)
G=sp.cancel(ABx*Ry - ABy*Rx)
Gp=sp.Poly(G,b); Gc=list(Gp.all_coeffs()); G2,G1,G0=pad(Gc,3)
g=sp.cancel(G2*k0**2 - G1*k0*k1 + G0*k1**2)
Ccon=sp.cancel(k0*l1-l0*k1)
# Tn, Td, Phi
Phi = sA*sa**2*(tb**2-1)*(1-tg**2) + sa*(ca*sA-cA*sa)*(tb+tg)*(tb*tg-1) + (2*cA*ca*sa+sA*(sa**2-ca**2))*tb*tg
Tn = sa*tg*(sA**2+cA**2)**2*(ca-sa*tg)*(tb**2+1)*(ca*tg+sa)
Td = (tg**2+1)*Phi
# Verify g*Td - Ccon*Tn == 0 as rational function
diff=sp.cancel(g*Td - Ccon*Tn)
log("g*Td - C*Tn (rational) == 0 ?", diff==0); flush()
# Also clear denominators fully and check numerator polynomial is zero
dt=together(g*Td - Ccon*Tn); dn,dd=fraction(dt); dn=expand(dn)
log("cleared numerator == 0 ?", dn==0, " ops",sp.count_ops(dn)); flush()
# Random free-indeterminate evaluation (NOT trig values)
import random
random.seed(7)
vals={sa:0.37,ca:0.91,sA:0.52,cA:-0.83,tb:0.6,tg:1.4}
gv=float(g.subs(vals)); Cv=float(Ccon.subs(vals)); Tv=float((Tn/Td).subs(vals))
log(f"random free eval: g={gv:.6e} C*T={(Cv*Tv):.6e} diff={gv-Cv*Tv:.3e}"); flush()
# Also: does the certificate hold if we DO NOT use pyth for A,alpha? Already does (free ring).
# Confirm with a second random set
vals2={sa:0.13,ca:-0.99,sA:0.71,cA:0.31,tb:-0.4,tg:2.1}
gv2=float(g.subs(vals2)); Cv2=float(Ccon.subs(vals2)); Tv2=float((Tn/Td).subs(vals2))
log(f"random2: g={gv2:.6e} C*T={(Cv2*Tv2):.6e} diff={gv2-Cv2*Tv2:.3e}"); flush()
