import sympy as sp, sys, time
from sympy import sin,cos,symbols,together,fraction,Poly,div,cancel

v = sp.Symbol('v')
sa,ca,sA,cA = sp.symbols('sa ca sA cA')
sAa,cAa,sA2a,cA2a = sp.symbols('sAa cAa sA2a cA2a')
sb,cb,sab,cab,sAab,cA2ab = sp.symbols('sb cb sab cab sAab cA2ab')
sA2ab = sp.Symbol('sA2ab')

sg = 2*v/(1+v**2)
cg = (1-v**2)/(1+v**2)
sag = sa*cg + ca*sg
sAag = sAa*cg + cAa*sg
sA2ag = sA2a*cg + cA2a*sg

kx = 1 - sg*ca/(2*sag)
ky = sg*sa/(2*sag)
lx = cA - sb*cAa/(2*sab)
ly = sA - sb*sAa/(2*sab)

def log(*a):
    print(*a); sys.stdout.flush()

t0=time.time()
# Build without expand; use cancel on sub-pieces to keep small.
K2 = sp.cancel(kx**2+ky**2)
L2 = sp.cancel(lx**2+ly**2)
kxl = sp.cancel(kx*ly-ky*lx)
kxcA = sp.cancel(kx*sA-ky*cA)
lxcA = sp.cancel(lx*sA-ly*cA)
log("pieces built t",round(time.time()-t0,2),"ops:",sp.count_ops(K2),sp.count_ops(L2),sp.count_ops(kxl))
P = sp.cancel(2*sag**2)
Q = sp.cancel(-(2*sAag*sag - sg*sA2ag))
R = sp.cancel(2*sab*sAab - sb*sA2ab)
S = sp.cancel(-2*sab**2)
log("PQ built t",round(time.time()-t0,2))
numH = 2*Q**2*L2*kxcA - 2*P*Q*(L2*ky - K2*lxcA) - 2*P**2*K2*ly
log("numH unexpanded ops",sp.count_ops(numH),"t",round(time.time()-t0,2))
H = numH/kxl + (P**2 - Q**2)
C = sp.cancel(P*S - Q*R)
log("H,C assembled. t",round(time.time()-t0,2))

# Clear v-denominators manually: multiply by (1+v^2)^K. Find max power needed via together.
t1=time.time()
Ht = together(H)
log("together(H) t",round(time.time()-t1,2),"ops",sp.count_ops(Ht))
Hn,Hd = fraction(Ht)
log("fraction t",round(time.time()-t1,2),"Hn ops",sp.count_ops(Hn),"Hd ops",sp.count_ops(Hd))
# Do NOT fully expand; feed to Poly directly (EX domain collects by v).
Ct = together(C); Cn,Cd = fraction(Ct)
log("C fraction t",round(time.time()-t1,2),"Cn ops",sp.count_ops(Cn),"Cd ops",sp.count_ops(Cd))

tgt = Hn*Cd
dvsr = Cn*Hd
log("tgt,dvsr assembled (unexpanded) t",round(time.time()-t1,2))
# Build Poly in v with EX domain (collects by v without expanding coeffs)
t2=time.time()
pT = sp.Poly(tgt, v, domain='EX')
log("Poly tgt built t",round(time.time()-t2,2),"deg",pT.degree())
pD = sp.Poly(dvsr, v, domain='EX')
log("Poly dvsr built t",round(time.time()-t2,2),"deg",pD.degree())
q,r = div(pT,pD)
log("div done t",round(time.time()-t2,2),"rem deg",r.degree())
Rr = r.as_expr()
log("rem==0:",Rr==0)
if Rr!=0:
    Rr2=cancel(Rr); log("rem cancel==0:",Rr2==0,"ops",sp.count_ops(Rr2))
