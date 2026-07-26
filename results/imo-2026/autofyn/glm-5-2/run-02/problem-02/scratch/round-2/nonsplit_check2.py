"""
Prove Delta_red is NOT a square in K by finding a rational point on D0=0
(for a concrete triangle) where Delta_red < 0.
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

# Try several concrete triangles; find rational point on D0=0 with Delta_red<0.
def rational_roots_of_cubic(coeffs):
    # coeffs = [c3, c2, c1, c0] for c3*ly^3 + c2*ly^2 + c1*ly + c0
    c3, c2, c1, c0 = [sp.Rational(c) for c in coeffs]
    if c3 == 0: return []
    # multiply through to clear; use rational_root theorem on integer version
    from fractions import Fraction
    # find a common denominator to get integer coeffs
    den = 1
    for c in [c3,c2,c1,c0]:
        den = sp.ilcm(den, c.q)
    ic3 = int((c3*den).p); ic2=int((c2*den).p); ic1=int((c1*den).p); ic0=int((c0*den).p)
    g = sp.gcd(sp.gcd(abs(ic3),abs(ic2)),sp.gcd(abs(ic1),abs(ic0)))
    ic3//=g; ic2//=g; ic1//=g; ic0//=g
    # leading: ic3, constant: ic0. rational roots p/q with p|ic0, q|ic3
    p_divs = [d for d in range(1, abs(ic0)+1) if ic0 % d == 0] if ic0!=0 else [1]
    p_divs = p_divs + [-d for d in p_divs]
    q_divs = [d for d in range(1, abs(ic3)+1) if ic3 % d == 0]
    roots = set()
    for p in p_divs:
        for q in q_divs:
            r = sp.Rational(p, q)
            if ic3*r**3 + ic2*r**2 + ic1*r + ic0 == 0:
                roots.add(r)
    return sorted(roots)

triangles = [
    {b:sp.Rational(1), u:sp.Rational(0), v:sp.Rational(2)},
    {b:sp.Rational(2), u:sp.Rational(1), v:sp.Rational(3)},
    {b:sp.Rational(3), u:sp.Rational(0), v:sp.Rational(4)},
    {b:sp.Rational(1), u:sp.Rational(0), v:sp.Rational(3)},
    {b:sp.Rational(2), u:sp.Rational(0), v:sp.Rational(3)},
    {b:sp.Rational(3), u:sp.Rational(1), v:sp.Rational(2)},
]
found = None
for spec in triangles:
    D0s = sp.expand(D0.subs(spec))
    Ds = sp.expand(Delta_red.subs(spec))
    # D0s as cubic in ly with coeffs depending on lx. For rational lx, get cubic in ly.
    for lx_num in range(-12, 25):
        for lx_den in [1,2,3,4,5,6,8]:
            lx_r = sp.Rational(lx_num, lx_den)
            P = sp.Poly(D0s.subs({lx:lx_r}), ly)
            coeffs = [int(c) if c.is_integer else float(c) for c in P.all_coeffs()]
            # need degree 3 in ly
            try:
                rr = rational_roots_of_cubic(coeffs)
            except Exception:
                continue
            for ly_r in rr:
                dv = Ds.subs({lx: lx_r, ly: ly_r})
                if dv < 0:
                    found = (spec, lx_r, ly_r, sp.Rational(dv), D0s.subs({lx:lx_r,ly:ly_r}))
                    break
            if found: break
        if found: break
    if found: break

if found:
    spec, lx_r, ly_r, dv, d0val = found
    print("*** NON-SPLIT CONFIRMED ***")
    print(f"Triangle specialization: b={spec[b]}, u={spec[u]}, v={spec[v]}")
    print(f"Rational point on D0=0: lx={lx_r}, ly={ly_r}")
    print(f"  D0(lx,ly) = {d0val}  (exactly 0)")
    print(f"  Delta_red(lx,ly) = {dv}  (NEGATIVE)")
    print("Since a real square rational function is >=0 wherever defined,")
    print("Delta_red is NOT a square in K = Q(b,u,v,lx,ly)/(D0).")
    print("=> The splitting field L = K(sqrt(Delta_red)) is a FIELD (non-split),")
    print("   Gal(L/K) = Z/2 swaps the two roots t1<->t2 of e3_line.")
    print("This is the key structural fact for the resultant+Galois closing.")
    # also print the specialized D0 and Delta_red for the record
    print("\nD0(lx,ly) at this specialization:", sp.expand(D0.subs(spec)))
else:
    print("No rational point with negative Delta found in the grid tried.")
    print("Trying numerical (real) points to at least confirm negativity...")
    spec = triangles[0]
    D0s = sp.expand(D0.subs(spec))
    Ds = sp.expand(Delta_red.subs(spec))
    rng = np.random.default_rng(1)
    neg = None
    for _ in range(5000):
        lxs = float(rng.uniform(-3,5))
        P = sp.Poly(D0s.subs({lx:lxs}), ly)
        cc = [float(c) for c in P.all_coeffs()]
        if len(cc)<4: continue
        if abs(cc[0])<1e-12: continue
        roots = np.roots(cc)
        for r in roots:
            if abs(r.imag)<1e-6:
                lyn=r.real
                dv = float(Ds.subs({lx:lxs, ly:lyn}))
                if dv < -1e-6:
                    neg=(lxs,lyn,dv,float(D0s.subs({lx:lxs,ly:lyn})))
                    break
        if neg: break
    if neg:
        print("Real (non-rational) point with Delta<0:", neg)
