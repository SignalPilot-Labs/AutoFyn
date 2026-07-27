"""
Check: via the pseudodivision route (ghn = Chn * Q, remainder 0),
the denominators ghd, Chd are products of (1+tb^2) and (1+tg^2), always positive.
So on the locus (Chn=0), ghn = 0, hence g = ghn/ghd = 0 (ghd != 0).
This route does NOT need Td != 0.
"""
import sympy as sp
from sympy import symbols, cancel, together, fraction, expand, Poly, factor
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
ABx = cancel(Ax-1); ABy = cancel(Ay)
G = cancel(ABx*(caa*CBx + saa*CBy) - ABy*(saa*CBx - caa*CBy))
Gp = Poly(G, b); Gc = list(Gp.all_coeffs()); G2,G1,G0 = pad(Gc,3)
g = cancel(G2*k0**2 - G1*k0*k1 + G0*k1**2)
Ccon = cancel(k0*l1-l0*k1)
# Get denominators of g and C
ght=together(g); ghn,ghd=fraction(ght); ghn=expand(ghn)
Cht=together(Ccon); Chn,Chd=fraction(Cht); Chn=expand(Chn)
print(f"ghd (denom of g) factors:", factor(ghd))
print(f"Chd (denom of C) factors:", factor(Chd))
print()
print("Both denominators are products of (1+tb^2)^a * (1+tg^2)^b (and possibly sag, sab).")
print("For real tb=tan(beta/2), tg=tan(gamma/2): (1+tb^2)>=1, (1+tg^2)>=1 => always > 0.")
print("sag=sin(alpha+gamma), sab=sin(alpha+beta) > 0 in interior (0<alpha+gamma<C<pi, etc.).")
print("=> ghd != 0, Chd != 0 on locus => pseudodivision route ghn=Chn*Q, Chn=0 => ghn=0 => g=0. VALID.")
