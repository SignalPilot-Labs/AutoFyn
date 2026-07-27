import sympy as sp, sys, time, math
from sympy import symbols,together,fraction,expand,cancel,factor
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
sAag=saa*cg+caa*sg; cAag=caa*cg-saa*sg
dirCKx=-cAag; dirCKy=-sAag
conK=sp.cancel((Kx-b*cA)*dirCKy - (Ky-b*sA)*dirCKx)
dirBLx=-cab; dirBLy=sab
conL=sp.cancel((Lx-1)*dirBLy - (Ly-0)*dirBLx)
cKp=sp.Poly(conK,b); cLp=sp.Poly(conL,b)
kcoeffs=list(cKp.all_coeffs()); lcoeffs=list(cLp.all_coeffs())
def pad(cs,n): cs=list(cs); return [sp.S(0)]*(n-len(cs))+cs
n=max(len(kcoeffs),len(lcoeffs)); kcoeffs=pad(kcoeffs,n); lcoeffs=pad(lcoeffs,n)
k1,k0=kcoeffs; l1,l0=lcoeffs
Ccon=sp.cancel(k0*l1-l0*k1)
K2=sp.cancel(Kx**2+Ky**2); L2=sp.cancel(Lx**2+Ly**2)
detKL=sp.cancel(Kx*Ly-Ky*Lx)
Ax=sp.cancel((Ly*K2-Ky*L2)/detKL); Ay=sp.cancel((Kx*L2-Lx*K2)/detKL)
CBx=b*cA-1; CBy=b*sA
Rx=saa*CBx - caa*CBy; Ry=caa*CBx + saa*CBy
ABx=sp.cancel(Ax-1); ABy=sp.cancel(Ay)
G=sp.cancel(ABx*Ry - ABy*Rx)
Gp=sp.Poly(G,b); Gcoeffs=list(Gp.all_coeffs()); G2,G1,G0=pad(Gcoeffs,3)
g=sp.cancel(G2*k0**2 - G1*k0*k1 + G0*k1**2)
T=sp.cancel(g/Ccon)
log("T ops",sp.count_ops(T)); flush()
# verify
diff=sp.cancel(g-Ccon*T)
log("g-Ccon*T == 0?",diff==0); flush()
# Try to factor T or see structure. T is rational in tb,tg with coeffs in sa,ca,sA,cA.
# print T as a fraction
Tt=together(T); Tn,Td=fraction(Tt); Tn=expand(Tn); Td=expand(Td)
log("Tn ops",sp.count_ops(Tn),"Td ops",sp.count_ops(Td)); flush()
# degrees
for v,nm in [(tb,'tb'),(tg,'tg')]:
    try: log(f"deg_{nm} Tn",sp.Poly(Tn,v).degree()," deg_{nm} Td",sp.Poly(Td,v).degree())
    except: pass
flush()
# Does Td factor nicely? Tn?
log("factoring Td..."); flush()
t0=time.time()
try:
    Tdf=factor(Td); log("Td factored ops",sp.count_ops(Tdf),"t",round(time.time()-t0,2)); flush()
    log("Td factored =",Tdf)
except Exception as e: log("Td factor fail",e)
log("factoring Tn..."); flush()
t0=time.time()
try:
    Tnf=factor(Tn); log("Tn factored ops",sp.count_ops(Tnf),"t",round(time.time()-t0,2)); flush()
    log("Tn factored =",Tnf)
except Exception as e: log("Tn factor fail",e)
# Also print the big Td factor and try factor it over the trig interpretation
log("\n-- Td inner factor --")
inner=Td/((tg**2+1))
inner=sp.cancel(inner)
log("inner ops",sp.count_ops(inner))
log("inner factored:",factor(inner))
# Print T fully (cancelled)
log("\n-- T = Tn/Td --")
log("Tn =",Tn)
log("Td =",Td)
