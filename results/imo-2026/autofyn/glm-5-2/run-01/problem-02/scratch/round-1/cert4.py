import sympy as sp, sys, time
from sympy import symbols,together,fraction,Poly,div,cancel,expand

v = sp.Symbol('v')
sa,ca,sb,cb,sA,cA = sp.symbols('sa ca sb cb sA cA')
# compound (no v) as addition formulas in atomic symbols
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
log("pieces t",round(time.time()-t0,2),"ops",sp.count_ops(K2),sp.count_ops(L2),sp.count_ops(kxl))
P = sp.cancel(2*sag**2); Q = sp.cancel(-(2*sAag*sag - sg*sA2ag))
R = sp.cancel(2*sab*sAab - sb*sA2ab); Sg = sp.cancel(-2*sab**2)
numH = 2*Q**2*L2*kxcA - 2*P*Q*(L2*ky - K2*lxcA) - 2*P**2*K2*ly
H = numH/kxl + (P**2 - Q**2); C = sp.cancel(P*Sg - Q*R)
log("H,C assembled t",round(time.time()-t0,2))
t1=time.time()
Ht=together(H); Hn,Hd=fraction(Ht)
log("H frac t",round(time.time()-t1,2),"Hn ops",sp.count_ops(Hn),"Hd ops",sp.count_ops(Hd))
Ct=together(C); Cn,Cd=fraction(Ct)
log("C frac t",round(time.time()-t1,2),"Cn ops",sp.count_ops(Cn),"Cd ops",sp.count_ops(Cd))
tgt=Hn*Cd; dvsr=Cn*Hd
t2=time.time()
pT=sp.Poly(tgt,v,domain='EX'); log("Poly tgt t",round(time.time()-t2,2),"deg",pT.degree())
pD=sp.Poly(dvsr,v,domain='EX'); log("Poly dvsr t",round(time.time()-t2,2),"deg",pD.degree())
q,r=div(pT,pD); log("div t",round(time.time()-t2,2),"rem deg",r.degree())
Rr=r.as_expr(); log("rem==0:",Rr==0)
if Rr!=0:
    # reduce remainder modulo Pythagoreans: sa^2+ca^2-1, sb^2+cb^2-1, sA^2+cA^2-1
    pyth=[sa**2+ca**2-1, sb**2+cb**2-1, sA**2+cA**2-1]
    Rr_exp=expand(Rr)
    log("Rr expanded ops",sp.count_ops(Rr_exp))
    # substitute ca^2 = 1-sa^2 etc. (reduce powers)
    Rr_sub = Rr_exp.subs({ca**2:1-sa**2, cb**2:1-sb**2, cA**2:1-sA**2})
    Rr_sub=expand(Rr_sub)
    # also reduce cAa etc? they are linear combos; their squares reduce via the above. just expand.
    log("after ca2->1-sa2 etc, ops",sp.count_ops(Rr_sub)," iszero?",Rr_sub==0)
    if Rr_sub!=0:
        Rr_sub2=sp.cancel(Rr_sub); log("cancel iszero?",Rr_sub2==0,"ops",sp.count_ops(Rr_sub2))
