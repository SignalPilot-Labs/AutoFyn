"""
Independent re-derivation of the §2 Direction Lemma certificate.
Goal: verify that g = C * T as a polynomial identity in the free ring
Z[sa, ca, sA, cA, tb, tg], and that it is NOT vacuous
(C not identically 0, g not identically 0, Td nonzero on locus).
"""
import sympy as sp
from sympy import symbols, together, fraction, expand, cancel, Poly

sa, ca, sA, cA = sp.symbols('sa ca sA cA')
tb, tg = sp.symbols('tb tg')

# Half-angle substitution for beta, gamma
sb = 2*tb/(1+tb**2); cb_ = (1-tb**2)/(1+tb**2)
sg = 2*tg/(1+tg**2); cg_ = (1-tg**2)/(1+tg**2)

# sin/cos of sums (free: sa,ca,sA,cA; half-angle: sb,cb,sg,cg)
def sadd(a,b,c,d): return (a*d+b*c, b*d-a*c)
saa = sa*cA + ca*sA   # sin(A+alpha)
caa = ca*cA - sa*sA   # cos(A+alpha)
sag, cag = sadd(sa, ca, sg, cg_)   # sin(alpha+gamma), cos(alpha+gamma)
sab, cab = sadd(sa, ca, sb, cb_)   # sin(alpha+beta), cos(alpha+beta)
sAag = saa*cg_ + caa*sg   # sin(A+alpha+gamma) = sin(A+2*alpha+gamma)... 
# Wait: A+alpha+gamma = A + (alpha+gamma). sin(A+alpha+gamma) = sinA*cos(alpha+gamma)+cosA*sin(alpha+gamma)
# = sA*cag + cA*sag. Let me recheck.
sAag2 = sA*cag + cA*sag  # sin(A + alpha + gamma)
cAag2 = cA*cag - sA*sag  # cos(A + alpha + gamma)
sA2ag = saa*cag + caa*sag  # sin(A + 2*alpha + gamma) = sin((A+alpha)+(alpha+gamma))
sA2ab = saa*cab + caa*sab  # sin(A + 2*alpha + beta)

# K = intersection of BK (direction pi-alpha) and MK (direction gamma)
# BK from B=(1,0): direction (cos(pi-alpha), sin(pi-alpha)) = (-ca, sa)
# MK from M=(1/2, 0): direction (cos(gamma), sin(gamma)) = (cg, sg)
# Solving: B + t*(-ca, sa) = M + u*(cg, sg)
# => 1 - t*ca = 1/2 + u*cg,  t*sa = u*sg
# From 2nd: u = t*sa/sg. Sub: 1 - t*ca = 1/2 + t*sa*cg/sg
# => 1/2 = t*(ca + sa*cg/sg) = t*(ca*sg + sa*cg)/sg = t*sag/sg
# => t = sg/(2*sag)
# K = (1 - t*ca, t*sa) = (1 - sg*ca/(2*sag), sg*sa/(2*sag))
kx = 1 - sg*ca/(2*sag); ky = sg*sa/(2*sag)

# L = intersection of CL (direction A+pi+alpha) and NL (direction A-beta)
# CL from C=b*(cosA, sinA): direction (-cos(A+alpha), -sin(A+alpha)) = (-caa, -saa)
# NL from N=C/2: direction (cos(A-beta), sin(A-beta)) = (cosA*cos(beta)+sinA*sin(beta), sinA*cos(beta)-cosA*sin(beta))
#   = (cA*cb_ + sA*sb, sA*cb_ - cA*sb)
# Let me denote NL direction as (nlx, nly)
nlx = cA*cb_ + sA*sb; nly = sA*cb_ - cA*sb
# C + t*(-caa, -saa) = N + u*(nlx, nly)
# C = b*(cA, sA), N = C/2 = b*(cA/2, sA/2)
# b*cA - t*caa = b*cA/2 + u*nlx,  b*sA - t*saa = b*sA/2 + u*nly
# => b*cA/2 - t*caa = u*nlx,  b*sA/2 - t*saa = u*nly
# From 1st: u = (b*cA/2 - t*caa)/nlx
# Sub into 2nd: b*sA/2 - t*saa = (b*cA/2 - t*caa)*nly/nlx
# => (b*sA/2 - t*saa)*nlx = (b*cA/2 - t*caa)*nly
# => b*sA/2*nlx - t*saa*nlx = b*cA/2*nly - t*caa*nly
# => b*(sA*nlx - cA*nly)/2 = t*(saa*nlx - caa*nly)
# Note: sA*nlx - cA*nly = sA*(cA*cb_+sA*sb) - cA*(sA*cb_-cA*sb) = sA*cA*cb_+sA^2*sb - cA*sA*cb_+cA^2*sb = (sA^2+cA^2)*sb = sb
# And: saa*nlx - caa*nly = (sa*cA+ca*sA)*(cA*cb_+sA*sb) - (ca*cA-sa*sA)*(sA*cb_-cA*sb)
#   = saa*(cA*cb_+sA*sb) - caa*(sA*cb_-cA*sb)
#   = saa*cA*cb_ + saa*sA*sb - caa*sA*cb_ + caa*cA*sb
#   = cb_*(saa*cA - caa*sA) + sb*(saa*sA + caa*cA)
#   = cb_*(sa*cA^2+ca*sA*cA - ca*cA*sA+sa*sA^2) + sb*(sa*cA*sA+ca*sA^2+ca*cA^2-sa*sA*cA)
#   = cb_*(sa*cA^2+sa*sA^2) + sb*(ca*sA^2+ca*cA^2)
#   = cb_*sa*(cA^2+sA^2) + sb*ca*(sA^2+cA^2)
#   = cb_*sa + sb*ca = sin(alpha+beta) = sab  ... wait: sin(a+b) = sa*cb_+ca*sb. Hmm, but I got cb_*sa+sb*ca = same thing! = sab.
# Hmm wait: cb_*sa + sb*ca = sa*cb_ + ca*sb = sab. Yes! = sab.
# So t = b*sb/(2*sab)
# L = C + t*(-caa, -saa) = b*(cA, sA) + b*sb/(2*sab)*(-caa, -saa)
# = b*(cA - sb*caa/(2*sab), sA - sb*saa/(2*sab))
lxu = cA - sb*caa/(2*sab); lyu = sA - sb*saa/(2*sab)

# b is the free parameter (|AC|/|AB|)
b = sp.symbols('b')
Kx, Ky = kx, ky
Lx, Ly = b*lxu, b*lyu

# conK = (K - C) x dir(CK) = 0
# dir(CK) = (-cos(A+alpha+gamma), -sin(A+alpha+gamma)) = (-cAag2, -sAag2)
dirCKx = -cAag2; dirCKy = -sAag2
conK = sp.cancel((Kx - b*cA)*dirCKy - (Ky - b*sA)*dirCKx)

# conL = (L - B) x dir(BL) = 0
# dir(BL) = (-cos(alpha+beta), sin(alpha+beta)) = (-cab, sab)
dirBLx = -cab; dirBLy = sab
conL = sp.cancel((Lx - 1)*dirBLy - (Ly - 0)*dirBLx)

# Check linearity in b
cKp = sp.Poly(conK, b); cLp = sp.Poly(conL, b)
print(f"deg_b conK = {cKp.degree()}, deg_b conL = {cLp.degree()}")
kc = list(cKp.all_coeffs()); lc = list(cLp.all_coeffs())
def pad(cs,n): cs=list(cs); return [sp.S(0)]*(n-len(cs))+cs
n=max(len(kc),len(lc)); kc=pad(kc,n); lc=pad(lc,n)
k1,k0 = kc; l1,l0 = lc
Ccon = sp.cancel(k0*l1 - l0*k1)

# Verify the (coeffs) expressions in the proof
# k1 should = sin(alpha+gamma) = sag
print(f"k1 == sag? {sp.simplify(k1 - sag) == 0}")
# l0 should = -sin(alpha+beta) = -sab
print(f"l0 == -sab? {sp.simplify(l0 + sab) == 0}")

# A' = intersection of perp-through-K (P.K = |K|^2) and perp-through-L (P.L = |L|^2)
K2 = sp.cancel(Kx**2+Ky**2); L2 = sp.cancel(Lx**2+Ly**2)
detKL = sp.cancel(Kx*Ly - Ky*Lx)
Ax = sp.cancel((Ly*K2 - Ky*L2)/detKL); Ay = sp.cancel((Kx*L2 - Lx*K2)/detKL)

# G = (A' - B) x R_theta(C - B), theta = pi/2 - A - alpha
# cos(theta) = sin(A+alpha) = saa, sin(theta) = cos(A+alpha) = caa
# R_theta(C-B) = (saa*(CBx) - caa*(CBy), caa*(CBx) + saa*(CBy))
CBx = b*cA - 1; CBy = b*sA
Rx = saa*CBx - caa*CBy; Ry = caa*CBx + saa*CBy
ABx = sp.cancel(Ax - 1); ABy = sp.cancel(Ay)
G = sp.cancel(ABx*Ry - ABy*Rx)
Gp = sp.Poly(G, b)
Gc = list(Gp.all_coeffs()); G2,G1,G0 = pad(Gc, 3)

# g = G2*k0^2 - G1*k0*k1 + G0*k1^2  (substituting b=-k0/k1, clearing k1^2)
g = sp.cancel(G2*k0**2 - G1*k0*k1 + G0*k1**2)

# Check: is g identically 0?
import random
random.seed(42)
vals = {sa:0.37, ca:0.91, sA:0.52, cA:-0.83, tb:0.6, tg:1.4}
gv = float(g.subs(vals))
print(f"g at random free eval = {gv:.6e} (should be nonzero => not vacuous)")
Cv = float(Ccon.subs(vals))
print(f"C at random free eval = {Cv:.6e} (should be nonzero => locus is proper)")

# Verify g = C * T via cleared-denominator pseudodivision
ght = together(g); ghn, ghd = fraction(ght); ghn = expand(ghn)
Cht = together(Ccon); Chn, Chd = fraction(Cht); Chn = expand(Chn)
base = sp.FractionField(sp.ZZ, [sa,ca,sA,cA,tb])
Cp = Poly(Chn, tg, domain=base); gp = Poly(ghn, tg, domain=base)
q, r = gp.div(Cp)
print(f"Pseudodivision remainder zero? {r.is_zero}")
print(f"deg_tg(Chn)={Cp.degree()}, deg_tg(ghn)={gp.degree()}")

# Also verify the specific T from the proof
Phi = sA*sa**2*(tb**2-1)*(1-tg**2) + sa*(ca*sA-cA*sa)*(tb+tg)*(tb*tg-1) + (2*cA*ca*sa+sA*(sa**2-ca**2))*tb*tg
Tn = sa*tg*(sA**2+cA**2)**2*(ca-sa*tg)*(tb**2+1)*(ca*tg+sa)
Td = (tg**2+1)*Phi
diff = cancel(g*Td - Ccon*Tn)
print(f"g*Td - C*Tn == 0 (rational)? {diff == 0}")

# Check Td nonzero on actual configs
import numpy as np
def numev(e):
    f = sp.lambdify((sa,ca,sA,cA,tb,tg), e, 'numpy')
    return float(f(0.423, 0.906, 0.819, 0.574, 0.156, 0.296))  # A=55,al=25,be~17.8,ga~33
print(f"Phi on actual config: {numev(Phi):.6e} (should be nonzero)")
print(f"Td on actual config: {numev(Td):.6e} (should be nonzero)")
