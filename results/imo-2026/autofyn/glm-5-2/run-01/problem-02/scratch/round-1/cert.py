import sympy as sp
from sympy import sin,cos,symbols,expand,together,fraction,Poly,div,cancel, Rational
import time, math

alpha,beta,gamma,A=symbols('alpha beta gamma A')
v = symbols('v')  # tan(gamma/2)

# field symbols for all gamma-independent trig quantities (free-ring move:
# treat them as independent; if H vanishes in the free ring modulo C, then
# a fortiori it vanishes as a genuine trig identity).
sa = sp.Symbol('sa')   # sin alpha
ca = sp.Symbol('ca')   # cos alpha
sA = sp.Symbol('sA')   # sin A
cA = sp.Symbol('cA')   # cos A
sAa = sp.Symbol('sAa') # sin(A+alpha)
cAa = sp.Symbol('cAa') # cos(A+alpha)
sA2a = sp.Symbol('sA2a') # sin(A+2alpha)
cA2a = sp.Symbol('cA2a') # cos(A+2alpha)
# beta-side (all gamma-independent): lhat components and derived scalars as TRUE formulas? No--
# to keep the l-structure, we keep lhat in terms of sA,cA,sAa,cAa,sb,cb,sab,cab.
sb = sp.Symbol('sb')   # sin beta
cb = sp.Symbol('cb')   # cos beta
sab = sp.Symbol('sab') # sin(alpha+beta)
cab = sp.Symbol('cab') # cos(alpha+beta)
sAab = sp.Symbol('sAab') # sin(A+alpha+beta)
cAab = sp.Symbol('cAab') # cos(A+alpha+beta)  -- not needed actually
sA2ab = sp.Symbol('sA2ab') # sin(A+2alpha+beta)
cA2ab = sp.Symbol('cA2ab') # cos(A+2alpha+beta) -- not needed

# gamma-dependent quantities expressed in v: sin g = 2v/(1+v^2), cos g=(1-v^2)/(1+v^2)
sg = 2*v/(1+v**2)
cg = (1-v**2)/(1+v**2)
# sin(alpha+gamma) = sa*cg + ca*sg ; sin(A+alpha+gamma)=sAa*cg+cAa*sg ; sin(A+2alpha+gamma)=sA2a*cg+cA2a*sg
sag = sa*cg + ca*sg
sAag = sAa*cg + cAa*sg
sA2ag = sA2a*cg + cA2a*sg

# khat (depends on alpha,gamma): K = c*khat
kx = 1 - sg*ca/(2*sag)
ky = sg*sa/(2*sag)
# lhat (depends on alpha,beta,A, NO gamma): L = b*lhat. Keep as TRUE formula in field symbols:
lx = cA - sb*cAa/(2*sab)
ly = sA - sb*sAa/(2*sab)

t0=time.time()
K2 = expand(kx**2+ky**2)
L2 = expand(lx**2+ly**2)
kxl = expand(kx*ly - ky*lx)
kxcA = expand(kx*sA - ky*cA)
lxcA = expand(lx*sA - ly*cA)
# P,Q,R,S
P = 2*sag**2
Q = -(2*sAag*sag - sg*sA2ag)
R = 2*sab*sAab - sb*sA2ab
S = -2*sab**2
numH = expand(2*Q**2*L2*kxcA - 2*P*Q*(L2*ky - K2*lxcA) - 2*P**2*K2*ly)
H = numH/kxl + (P**2 - Q**2)
C = expand(P*S - Q*R)
print("built trig-in-v. ops H(raw):",sp.count_ops(H),"C:",sp.count_ops(C),"t",round(time.time()-t0,2))

# Clear denominators: combine into single fraction and clear (1+v^2) powers.
# H is rational in v (denominators are powers of (1+v^2) and sag = (sa*cg+ca*sg) which also has (1+v^2)).
# Use together to get single fraction, then take numerator -> polynomial in v with field-symbol coeffs.
t1=time.time()
Ht = together(H)
Hn,Hd = fraction(Ht)
Hn = expand(Hn); Hd = expand(Hd)
print("together/fraction. Hn ops:",sp.count_ops(Hn),"Hd ops:",sp.count_ops(Hd),"t",round(time.time()-t1,2))
Ct = together(C)
Cn,Cd = fraction(Ct)
Cn = expand(Cn); Cd = expand(Cd)
print("Cn ops:",sp.count_ops(Cn),"Cd ops:",sp.count_ops(Cd))

# H = Hn/Hd, C = Cn/Cd. We want H = C*T => Hn/Hd = (Cn/Cd) T => Hn*Cd = Cn*Hd*T.
# So check divisibility of (Hn*Cd) by (Cn*Hd): remainder 0 => certificate.
tgt = expand(Hn*Cd)
dvsr = expand(Cn*Hd)
print("tgt ops:",sp.count_ops(tgt),"dvsr ops:",sp.count_ops(dvsr),"t",round(time.time()-t1,2))
print("deg tgt in v:", sp.Poly(tgt, v).degree(), "deg dvsr in v:", sp.Poly(dvsr, v).degree())

# Pseudodivision as univariate polynomials in v over the EX (expression) domain.
t2=time.time()
pT = sp.Poly(tgt, v, domain='EX')
pD = sp.Poly(dvsr, v, domain='EX')
q,r = div(pT, pD)
print("pseudodivision done. t",round(time.time()-t2,2))
print("remainder degree in v:", r.degree())
Rr = r.as_expr()
print("remainder == 0:", Rr==0, " remainder ops:", sp.count_ops(Rr))
if Rr!=0:
    Rr2 = cancel(Rr)
    print("remainder(cancel) ==0:", Rr2==0, "ops:",sp.count_ops(Rr2))
