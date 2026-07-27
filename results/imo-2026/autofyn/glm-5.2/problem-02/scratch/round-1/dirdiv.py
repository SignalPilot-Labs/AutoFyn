import sympy as sp, sys, time, math
from sympy import symbols,together,fraction,expand,cancel,prem,Poly
log=print
def flush(): sys.stdout.flush()
sa,ca,sb,cb,sg,cg,sA,cA = sp.symbols('sa ca sb cb sg cg sA cA')
saa=sa*cA+ca*sA; caa=ca*cA-sa*sA
salag=sa*cg+ca*sg; calag=ca*cg-sa*sg
sag=salag; cag=calag
sab=saa*cb+caa*sb; cab=caa*cb-saa*sb
sA2ag=saa*calag+caa*salag
sA2ab=saa*(ca*cb-sa*sb)+caa*(sa*cb+ca*sb)
kx=1-sg*ca/(2*sag); ky=sg*sa/(2*sag)
lxu=cA - sb*caa/(2*sab); lyu=sA - sb*saa/(2*sab)
b = sp.symbols('b')
Kx,Ky=kx,ky
Lx,Ly=b*lxu,b*lyu
K2=sp.cancel(Kx**2+Ky**2); L2=sp.cancel(Lx**2+Ly**2)
detKL=sp.cancel(Kx*Ly-Ky*Lx)
Ax=sp.cancel((Ly*K2-Ky*L2)/detKL); Ay=sp.cancel((Kx*L2-Lx*K2)/detKL)
CBx=b*cA-1; CBy=b*sA
Rx=saa*CBx - caa*CBy
Ry=caa*CBx + saa*CBy
ABx=sp.cancel(Ax-1); ABy=sp.cancel(Ay)
G=sp.cancel(ABx*Ry - ABy*Rx)
Gp=sp.Poly(G,b)
G2,G1,G0=[sp.cancel(c) for c in Gp.all_coeffs()]
log("G2,G1,G0 ops",sp.count_ops(G2),sp.count_ops(G1),sp.count_ops(G0)); flush()
# P,Q,R,S and rho=-Q/P, C=PS-QR
P=2*sag**2
Q=sg*sA2ag - 2*sag**2
R=2*sab**2 - sb*sA2ab
S=-2*sab**2
C=sp.expand(P*S-Q*R)
log("C ops",sp.count_ops(C)); flush()
# g = G2*Q^2 - G1*Q*P + G0*P^2  ( = P^2 * G(-Q/P) )
g=sp.cancel(G2*Q**2 - G1*Q*P + G0*P**2)
log("g ops",sp.count_ops(g)); flush()
g=sp.expand(g)
log("g expand ops",sp.count_ops(g)); flush()
# sanity: evaluate numerically on a valid config
import numpy as np
def numev(e):
    f=sp.lambdify((sa,ca,sb,cb,sg,cg,sA,cA),e,'numpy')
    Ad,ald,bed,gad=60,20,25.752096,25.752096  # symmetric-ish interior (equilateral) -- use a scalene instead
    return float(f(*[np.sin(np.radians(x)) if i%2==0 else np.cos(np.radians(x)) for i,x in enumerate([ald,ald,bed,bed,gad,gad,Ad,Ad])]))
# use scalene: A=55,al=25,be=17.191,ga=32.923
def numev2(e):
    f=sp.lambdify((sa,ca,sb,cb,sg,cg,sA,cA),e,'numpy')
    Ad,ald,bed,gad=55,25,17.191,32.923
    vals=[np.sin(np.radians(ald)),np.cos(np.radians(ald)),np.sin(np.radians(bed)),np.cos(np.radians(bed)),np.sin(np.radians(gad)),np.cos(np.radians(gad)),np.sin(np.radians(Ad)),np.cos(np.radians(Ad))]
    return float(f(*vals))
log("g on locus (should be ~0):",numev2(g)); flush()
log("C on locus (should be ~0):",numev2(C)); flush()
# Now half-angle substitute sb,cb,sg,cg -> functions of tb,tg ; keep sa,ca,sA,cA as symbols (+pyth later)
tb,tg=symbols('tb tg')
sb2=2*tb/(1+tb**2); cb2=(1-tb**2)/(1+tb**2); sg2=2*tg/(1+tg**2); cg2=(1-tg**2)/(1+tg**2)
log("half-angle substituting..."); flush()
t0=time.time()
gh=sp.cancel(g.subs({sb:sb2,cb:cb2,sg:sg2,cg:cg2}))
Ch=sp.cancel(C.subs({sb:sb2,cb:cb2,sg:sg2,cg:cg2}))
log("half-angle done t",round(time.time()-t0,2),"gh ops",sp.count_ops(gh),"Ch ops",sp.count_ops(Ch)); flush()
# clear denominators: multiply by (1+tb^2)^k (1+tg^2)^m
ght=together(gh); ghn,ghd=fraction(ght); ghn=expand(ghn)
Cht=together(Ch); Chn,Chd=fraction(Cht); Chn=expand(Chn)
log("cleared. ghn ops",sp.count_ops(ghn),"Chn ops",sp.count_ops(Chn)); flush()
# pseudodivide ghn by Chn in tg, over ZZ(sa,ca,sA,cA)[tb][tg]
base=sp.FractionField(sp.ZZ,sa,ca,sA,cA,tb)
log("making polys over",base); flush()
t1=time.time()
try:
    Cp=sp.Poly(Chn,tg,domain=base)
    gp=sp.Poly(ghn,tg,domain=base)
    log("deg tg Chn",Cp.degree(),"deg tg ghn",gp.degree(),"t",round(time.time()-t1,2)); flush()
    q,r=gp.div(Cp)
    log("division done. r ops",sp.count_ops(r.as_expr()),"t",round(time.time()-t1,2)); flush()
    log("remainder zero?",r.is_zero); flush()
    if not r.is_zero:
        re=r.as_expr()
        log("remainder (lambdized) on locus:",numev2(sp.cancel(re.subs({tb:sp.tan(sp.Symbol('be')/2),tg:sp.tan(sp.Symbol('ga')/2)}))))
except Exception as e:
    log("ERROR:",repr(e)); flush()
