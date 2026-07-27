import sympy as sp, sys, time, math
from sympy import symbols,together,fraction,Poly,div,cancel,expand
from numpy import sin,cos

v = sp.Symbol('v')
sa,ca,sb,cb,sA,cA = sp.symbols('sa ca sb cb sA cA')
sAa = sA*ca + cA*sa;   cAa = cA*ca - sA*sa
sA2a = sAa*ca + cAa*sa; cA2a = cAa*ca - sAa*sa
sab = sa*cb + ca*sb;    cab = ca*cb - sa*sb
sAab = sAa*cb + cAa*sb
sA2ab = sA2a*cb + cA2a*sb

sg = 2*v/(1+v**2); cg = (1-v**2)/(1+v**2)
sag = sa*cg + ca*sg
sAag = sAa*cg + cAa*sg
sA2ag = sA2a*cg + cA2a*sg

def log(*a): print(*a); sys.stdout.flush()
t0=time.time()
kx = 1 - sg*ca/(2*sag); ky = sg*sa/(2*sag)
lx = cA - sb*cAa/(2*sab); ly = sA - sb*sAa/(2*sab)
K2 = sp.cancel(kx**2+ky**2); L2 = sp.cancel(lx**2+ly**2)
kxl = sp.cancel(kx*ly-ky*lx); kxcA = sp.cancel(kx*sA-ky*cA); lxcA = sp.cancel(lx*sA-ly*cA)
log("pieces t",round(time.time()-t0,2))
P = sp.cancel(2*sag**2); Q = sp.cancel(-(2*sAag*sag - sg*sA2ag))
R = sp.cancel(2*sab*sAab - sb*sA2ab); Sg = sp.cancel(-2*sab**2)
# H' = QS F1 - PS F2 + RP F3  with F1=2L2 kxcA/kxl -1, F2=2(L2 ky - K2 lxcA)/kxl, F3=-2K2 ly/kxl +1
numHp = sp.cancel(2*Q*Sg*L2*kxcA - 2*P*Sg*(L2*ky - K2*lxcA) - 2*R*P*K2*ly)
Hp = numHp/kxl + (R*P - Q*Sg)
C = sp.cancel(P*Sg - Q*R)
log("H',C assembled t",round(time.time()-t0,2))
# numeric sanity
def ev(e,vals):
    f=sp.lambdify((sa,ca,sb,cb,sA,cA,v),e,'numpy'); return float(f(*vals))
# alpha=20,beta=35.241,gamma=17.963,A=60
ad=math.radians(20);bd=math.radians(35.2414494241406);gd=math.radians(17.963453537582254);Ad=math.radians(60)
vals=(sin(ad),cos(ad),sin(bd),cos(bd),sin(Ad),cos(Ad),math.tan(gd/2))
log("Hp(on locus)=",ev(Hp,vals)," C=",ev(C,vals))
vals2=(vals[0],vals[1],sin(math.radians(10)),cos(math.radians(10)),vals[4],vals[5],vals[6])
log("Hp(off locus)=",ev(Hp,vals2)," C=",ev(C,vals2))
t1=time.time()
Ht=together(Hp); Hn,Hd=fraction(Ht)
log("H' frac t",round(time.time()-t1,2),"Hn ops",sp.count_ops(Hn),"Hd ops",sp.count_ops(Hd))
Ct=together(C); Cn,Cd=fraction(Ct)
log("C frac t",round(time.time()-t1,2),"Cn ops",sp.count_ops(Cn),"Cd ops",sp.count_ops(Cd))
tgt=Hn*Cd; dvsr=Cn*Hd
t2=time.time()
pT=sp.Poly(tgt,v,domain='EX'); log("Poly tgt t",round(time.time()-t2,2),"deg",pT.degree())
pD=sp.Poly(dvsr,v,domain='EX'); log("Poly dvsr t",round(time.time()-t2,2),"deg",pD.degree())
q,r=div(pT,pD); log("div t",round(time.time()-t2,2),"rem deg",r.degree())
Rr=r.as_expr(); log("rem==0:",Rr==0,"ops",sp.count_ops(Rr))
if Rr!=0:
    Rr_exp=expand(Rr)
    Rr_sub=Rr_exp.subs({ca**2:1-sa**2,cb**2:1-sb**2,cA**2:1-sA**2})
    Rr_sub=expand(Rr_sub)
    log("after pyth-subst ops",sp.count_ops(Rr_sub),"iszero?",Rr_sub==0)
    if Rr_sub!=0:
        Rs=cancel(Rr_sub); log("cancel iszero?",Rs==0,"ops",sp.count_ops(Rs))
