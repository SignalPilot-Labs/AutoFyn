"""
Check: does §2's G = (A'-B) x R_theta(C-B) = 0 prove SIGNED angle +theta
or just unsigned parallelism (±theta)?

If G uses R_{+theta} (specific rotation), then G=0 means A'-B || R_{+theta}(C-B),
which gives the SIGNED angle +theta (mod pi). If it were R_{-theta}, we'd get -theta.

Also verify: the certificate g=Td*C is the SAME regardless of using +theta or -theta?
No - if we used -theta (R_{-theta}), G would be different, and g would be different.
"""
import sympy as sp
from sympy import symbols, cancel, Poly

sa, ca, sA, cA = sp.symbols('sa ca sA cA')
tb, tg = sp.symbols('tb tg')
sb = 2*tb/(1+tb**2); cb_ = (1-tb**2)/(1+tb**2)
sg = 2*tg/(1+tg**2); cg_ = (1-tg**2)/(1+tg**2)
def sadd(a,b,c,d): return (a*d+b*c, b*d-a*c)
saa = sa*cA + ca*sA; caa = ca*cA - sa*sA
sag, cag = sadd(sa, ca, sg, cg_)
sab, cab = sadd(sa, ca, sb, cb_)
sAag = saa*cg_ + caa*sg; cAag = caa*cg_ - saa*sg

kx = 1-sg*ca/(2*sag); ky = sg*sa/(2*sag)
lxu = cA - sb*caa/(2*sab); lyu = sA - sb*saa/(2*sab)
b = sp.symbols('b')
Kx, Ky = kx, ky; Lx, Ly = b*lxu, b*lyu

dirCKx = -cAag; dirCKy = -sAag
conK = cancel((Kx - b*cA)*dirCKy - (Ky - b*sA)*dirCKx)
dirBLx = -cab; dirBLy = sab
conL = cancel((Lx - 1)*dirBLy - Ly*dirBLx)
cKp = Poly(conK, b); cLp = Poly(conL, b)
kc = list(cKp.all_coeffs()); lc = list(cLp.all_coeffs())
def pad(cs,n): cs=list(cs); return [sp.S(0)]*(n-len(cs))+cs
n=max(len(kc),len(lc)); kc=pad(kc,n); lc=pad(lc,n)
k1,k0=kc; l1,l0=lc

K2 = cancel(Kx**2+Ky**2); L2 = cancel(Lx**2+Ly**2)
detKL = cancel(Kx*Ly-Ky*Lx)
Ax = cancel((Ly*K2-Ky*L2)/detKL); Ay = cancel((Kx*L2-Lx*K2)/detKL)
CBx = b*cA-1; CBy = b*sA

# G with +theta: cos(theta)=saa, sin(theta)=caa  (theta = pi/2 - A - alpha)
Rx_pos = saa*CBx - caa*CBy; Ry_pos = caa*CBx + saa*CBy
ABx = cancel(Ax-1); ABy = cancel(Ay)
G_pos = cancel(ABx*Ry_pos - ABy*Rx_pos)

# G with -theta: cos(-theta)=caa, sin(-theta)=-saa  => R_{-theta}(v) = (caa*vx+saa*vy, -saa*vx+caa*vy)
Rx_neg = caa*CBx + saa*CBy; Ry_neg = -saa*CBx + caa*CBy
G_neg = cancel(ABx*Ry_neg - ABy*Rx_neg)

Gp_pos = Poly(G_pos, b); Gp_neg = Poly(G_neg, b)
Gc_pos = list(Gp_pos.all_coeffs()); Gc_neg = list(Gp_neg.all_coeffs())
G2p,G1p,G0p = pad(Gc_pos,3); G2n,G1n,G0n = pad(Gc_neg,3)

g_pos = cancel(G2p*k0**2 - G1p*k0*k1 + G0p*k1**2)
g_neg = cancel(G2n*k0**2 - G1n*k0*k1 + G0n*k1**2)
Ccon = cancel(k0*l1-l0*k1)

# Check: is g_pos divisible by C (certificate holds for +theta)?
from sympy import together, fraction, expand
ght=together(g_pos); ghn,ghd=fraction(ght); ghn=expand(ghn)
Cht=together(Ccon); Chn,Chd=fraction(Cht); Chn=expand(Chn)
base=sp.FractionField(sp.ZZ,[sa,ca,sA,cA,tb])
Cp=Poly(Chn,tg,domain=base); gp=Poly(ghn,tg,domain=base)
q,r=gp.div(Cp)
print(f"+theta certificate: remainder zero? {r.is_zero}")

# Check: is g_neg divisible by C (certificate holds for -theta)?
ght_n=together(g_neg); ghn_n,ghd_n=fraction(ght_n); ghn_n=expand(ghn_n)
gp_n=Poly(ghn_n,tg,domain=base)
q_n,r_n=gp_n.div(Cp)
print(f"-theta certificate: remainder zero? {r_n.is_zero}")

print()
print("If +theta cert holds but -theta cert does NOT, then §2 proves SIGNED +theta.")
print("(If both held, it would be unsigned parallelism.)")

# Numerical: check actual sign
import numpy as np
vals = {sa:0.423, ca:0.906, sA:0.819, cA:0.574, tb:0.156, tg:0.296}
# actual: A=55,al=25 => target=10deg=0.1745
target = 0.1745
# g_pos should be ~0 on locus (C=0). g_neg should NOT be ~0 on locus.
# But we need to evaluate ON the locus (C=0), not at random point.
# At the random eval, C != 0, so g_pos = C*T != 0 and g_neg != 0.
# Instead check: g_pos/C vs g_neg/C at random point
print(f"\nAt random free eval (not on locus):")
print(f"  g_pos = {float(g_pos.subs(vals)):.6e}")
print(f"  g_neg = {float(g_neg.subs(vals)):.6e}")
print(f"  C     = {float(Ccon.subs(vals)):.6e}")
print(f"  g_pos/C = {float(g_pos.subs(vals))/float(Ccon.subs(vals)):.6e}")
print(f"  g_neg/C = {float(g_neg.subs(vals))/float(Ccon.subs(vals)):.6e}")
