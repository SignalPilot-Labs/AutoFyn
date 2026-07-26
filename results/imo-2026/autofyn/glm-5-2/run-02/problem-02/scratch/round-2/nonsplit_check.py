"""
Prove Delta_red (= discriminant of e3_line in t, reduced mod D0) is NOT a
square in K = Q(b,u,v,lx,ly)/(D0), by specializing to a concrete triangle
and finding a real point of D0=0 where Delta_red < 0.

A real-valued square rational function is >= 0 wherever defined, so a
negative value proves non-square (hence the splitting field L=K(sqrt(Delta))
is a FIELD, non-split -> the resultant+Galois argument closes).
"""
import sympy as sp
import numpy as np

b, u, v, lx, ly, t = sp.symbols('b u v lx ly t')
kx, ky = sp.symbols('kx ky')
A=(0,0); Bpt=(b,0); Cpt=(u,v); M=(b/2,0); Npt=(u/2,v/2)
def sub(P,d): return (P[0]-d[0], P[1]-d[1])
def cross(p,q): return p[0]*q[1]-p[1]*q[0]
def dot(p,q): return p[0]*q[0]+p[1]*q[1]
Kp=(kx,ky); Lp=(lx,ly)
BK=sub(Kp,Bpt); BA=sub(A,Bpt); CA=sub(A,Cpt); CL=sub(Lp,Cpt)
e1=sp.expand(cross(BK,BA)*dot(CA,CL)-cross(CA,CL)*dot(BK,BA))
BL=sub(Lp,Bpt); NL=sub(Lp,Npt); NC=sub(Cpt,Npt)
e2=sp.expand(cross(BL,BK)*dot(NL,NC)-cross(NL,NC)*dot(BL,BK))
CK=sub(Kp,Cpt); MB=sub(Bpt,M); MK=sub(Kp,M)
e3=sp.expand(cross(CL,CK)*dot(MB,MK)-cross(MB,MK)*dot(CL,CK))
Ksq=kx**2+ky**2; Lsq=lx**2+ly**2; Csq=u**2+v**2; Bsq=b**2
detKL=kx*ly-ky*lx
Q=sp.expand(2*(Ksq*ly-Lsq*ky)*(u-b)+2*(kx*Lsq-lx*Ksq)*v-detKL*(Csq-Bsq))
sx,sy=sp.symbols('sx sy')
e1s=sp.expand(e1.subs({kx:b+sx,ky:sy})); e2s=sp.expand(e2.subs({kx:b+sx,ky:sy}))
a1=sp.expand(e1s.coeff(sx,1)); b1c=sp.expand(e1s.coeff(sy,1))
a2=sp.expand(e2s.coeff(sx,1)); b2c=sp.expand(e2s.coeff(sy,1))
D=sp.expand(a1*b2c-b1c*a2); D0=sp.expand(-(4*D)/(b*(u**2+v**2)))
kx_sub=b+t*b1c; ky_sub=t*(-a1)
e3_sub=sp.expand(e3.subs({kx:kx_sub,ky:ky_sub}))
P_e3=sp.Poly(e3_sub,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
P_D0=sp.Poly(D0,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
_,r3=sp.div(P_e3,P_D0)
e3_line=sp.expand(r3.as_expr())
et2=sp.expand(sp.Poly(e3_line,t).nth(2))
et1=sp.expand(sp.Poly(e3_line,t).nth(1))
et0=sp.expand(sp.Poly(e3_line,t).nth(0))
Delta=sp.expand(et1**2-4*et2*et0)
P_Delta=sp.Poly(Delta,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
_,rD=sp.div(P_Delta,P_D0)
Delta_red=sp.expand(rD.as_expr())
print("Delta_red computed (mod D0).")

# Specialize to concrete triangle b=1, u=0, v=2
spec = {b:sp.Rational(1), u:sp.Rational(0), v:sp.Rational(2)}
D0_spec = sp.expand(D0.subs(spec))
Delta_red_spec = sp.expand(Delta_red.subs(spec))
print("D0 (b=1,u=0,v=2) =", D0_spec)
print("Delta_red (b=1,u=0,v=2) (mod D0) =")
print(sp.factor(Delta_red_spec))

# Check: is Delta_red_spec negative at some real point of D0_spec=0?
# Parametrize: solve D0_spec=0 cubic in ly for given lx, evaluate Delta_red_spec.
rng = np.random.default_rng(99)
found_neg = None
for _ in range(2000):
    lxs = float(rng.uniform(-2, 4))
    # D0_spec as cubic in ly: collect coeffs
    # D0_spec = 2*lx + 2*lx^2*ly - 2*lx^2 + 2*ly^3 - 6*ly^2 + 4*ly  (for b=1,u=0,v=2)
    P = sp.Poly(D0_spec, ly)
    coeffs = [float(c) for c in P.all_coeffs()]
    roots = np.roots(coeffs)
    for r in roots:
        if abs(r.imag) < 1e-6:
            lyn = r.real
            val = float(Delta_red_spec.subs({lx: lxs, ly: lyn}))
            if val < -1e-6:
                found_neg = (lxs, lyn, val)
                break
    if found_neg: break

if found_neg:
    lxs, lyn, val = found_neg
    print(f"\n*** FOUND negative Delta_red at real point of D0=0 ***")
    print(f"  lx = {lxs}, ly = {lyn}")
    print(f"  D0_spec(lx,ly) = {float(D0_spec.subs({lx:lxs, ly:lyn}))}  (should be ~0)")
    print(f"  Delta_red_spec(lx,ly) = {val}  (NEGATIVE)")
    # Verify D0 is ~0
    # Verify with EXACT rational approximations to make it rigorous
    # Use rational lx, ly near this point on D0=0.
    # Find a rational point on D0_spec=0 near (lxs, lyn) with Delta_red < 0.
    # Use lx = rational, solve cubic for rational ly (hard). Instead use
    # a rational parametrization: pick rational lx, solve cubic, check if a
    # real root is rational (unlikely). So we use a continuity + density argument:
    # Delta_red_spec is continuous, negative at (lxs,lyn), and D0_spec=0 there.
    # Rationals are dense in R, and D0_spec=0 is a real curve; near (lxs,lyn)
    # there are real points of D0=0 with Delta_red<0. To make it FULLY rigorous
    # we exhibit a rational point. Let's search for rational lx with the cubic
    # having a rational root.
    print("\nSearching for a RATIONAL point on D0_spec=0 with Delta_red<0 (for rigor)...")
    found_rat = None
    for lx_num in range(-40, 81):
        for lx_den in range(1, 21):
            lx_r = sp.Rational(lx_num, lx_den)
            P2 = sp.Poly(D0_spec.subs({lx: lx_r}), ly)
            rats = sp.polys.polytools.Poly(P2.all_coeffs(), ly)
            # rational roots via rational-root theorem
            lc = P2.LC(); cc = P2.TC()
            # candidate rational roots: divisors of cc / divisors of lc
            if lc == 0: continue
            cc_divs = [sp.Rational(i,1) for i in range(1, abs(int(cc))+1) if cc % i == 0] if cc != 0 else []
            # too slow for big; use a direct eval over a grid of rationals
            for ly_num in range(-80, 81):
                for ly_den in range(1, 21):
                    ly_r = sp.Rational(ly_num, ly_den)
                    if D0_spec.subs({lx: lx_r, ly: ly_r}) == 0:
                        dval = int(Delta_red_spec.subs({lx: lx_r, ly: ly_r}))
                        if dval < 0:
                            found_rat = (lx_r, ly_r, dval)
                            break
                if found_rat: break
            if found_rat: break
        if found_rat: break
    if found_rat:
        lx_r, ly_r, dval = found_rat
        print(f"  RATIONAL point: lx={lx_r}, ly={ly_r}")
        print(f"  D0_spec = {D0_spec.subs({lx:lx_r, ly:ly_r})}  (=0)")
        print(f"  Delta_red_spec = {dval}  (<0)")
        print("  -> Delta_red is NOT a square in K (specialization argument).")
    else:
        print("  No rational point found in grid; using the real point + density argument.")
else:
    print("No negative Delta_red found in sampling. Need different specialization.")
