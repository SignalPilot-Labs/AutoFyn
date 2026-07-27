"""Quick check: does the certificate hold for -theta (unsigned)? 
If not, §2 proves SIGNED +theta."""
import sympy as sp
from sympy import symbols, cancel, Poly, together, fraction, expand
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
Ccon = cancel(k0*l1-l0*k1)
# +theta: R_theta(v) = (saa*vx - caa*vy, caa*vx + saa*vy)
G_pos = cancel(ABx*(caa*CBx + saa*CBy) - ABy*(saa*CBx - caa*CBy))
Gp = Poly(G_pos, b); Gc = list(Gp.all_coeffs()); G2,G1,G0 = pad(Gc,3)
g_pos = cancel(G2*k0**2 - G1*k0*k1 + G0*k1**2)
ght=together(g_pos); ghn,ghd=fraction(ght); ghn=expand(ghn)
Cht=together(Ccon); Chn,Chd=fraction(Cht); Chn=expand(Chn)
base=sp.FractionField(sp.ZZ,[sa,ca,sA,cA,tb])
Cp=Poly(Chn,tg,domain=base); gp=Poly(ghn,tg,domain=base)
q,r=gp.div(Cp)
print(f"+theta certificate: remainder zero? {r.is_zero}")
# Now -theta: R_{-theta}(v) = (caa*vx + saa*vy, -saa*vx + caa*vy)
G_neg = cancel(ABx*(-saa*CBx + caa*CBy) - ABy*(caa*CBx + saa*CBy))
Gpn = Poly(G_neg, b); Gcn = list(Gpn.all_coeffs()); G2n,G1n,G0n = pad(Gcn,3)
g_neg = cancel(G2n*k0**2 - G1n*k0*k1 + G0n*k1**2)
ghtn=together(g_neg); ghnn,ghdn=fraction(ghtn); ghnn=expand(ghnn)
gpn=Poly(ghnn,tg,domain=base)
qn,rn=gpn.div(Cp)
print(f"-theta certificate: remainder zero? {rn.is_zero}")
