"""
Check the discriminant of e3_line (in t) modulo D0, and whether the
splitting field of e3_line over K = Q(b,u,v,lx,ly)/(D0) is a field (non-split)
or split.  This determines whether the resultant + Galois argument can
derive 'both roots shared' (saturation) WITHOUT the explicit saturation identity.

Also: numerically check, at valid configs, whether BOTH roots of e3_line are
Q-roots (which would confirm saturation holds on the real locus).
"""
import sympy as sp
import numpy as np

b, u, v, lx, ly, t = sp.symbols('b u v lx ly t')
kx, ky = sp.symbols('kx ky')
A = (0,0); Bpt = (b,0); Cpt = (u,v); M = (b/2,0); Npt = (u/2,v/2)
def sub(P,d): return (P[0]-d[0], P[1]-d[1])
def cross(p,q): return p[0]*q[1]-p[1]*q[0]
def dot(p,q): return p[0]*q[0]+p[1]*q[1]
K = (kx,ky); L = (lx,ly)
BK=sub(K,Bpt); BA=sub(A,Bpt); CA=sub(A,Cpt); CL=sub(L,Cpt)
e1 = sp.expand(cross(BK,BA)*dot(CA,CL) - cross(CA,CL)*dot(BK,BA))
BL=sub(L,Bpt); NL=sub(L,Npt); NC=sub(Cpt,Npt)
e2 = sp.expand(cross(BL,BK)*dot(NL,NC) - cross(NL,NC)*dot(BL,BK))
CK=sub(K,Cpt); MB=sub(Bpt,M); MK=sub(K,M)
e3 = sp.expand(cross(CL,CK)*dot(MB,MK) - cross(MB,MK)*dot(CL,CK))
Ksq=kx**2+ky**2; Lsq=lx**2+ly**2; Csq=u**2+v**2; Bsq=b**2
detKL=kx*ly-ky*lx
Q = sp.expand(2*(Ksq*ly-Lsq*ky)*(u-b) + 2*(kx*Lsq-lx*Ksq)*v - detKL*(Csq-Bsq))
sx, sy = sp.symbols('sx sy')
e1s=sp.expand(e1.subs({kx:b+sx,ky:sy})); e2s=sp.expand(e2.subs({kx:b+sx,ky:sy}))
a1=sp.expand(e1s.coeff(sx,1)); b1c=sp.expand(e1s.coeff(sy,1))
a2=sp.expand(e2s.coeff(sx,1)); b2c=sp.expand(e2s.coeff(sy,1))
D=sp.expand(a1*b2c-b1c*a2); D0=sp.expand(-(4*D)/(b*(u**2+v**2)))
assert sp.simplify(D + (b/4)*(u**2+v**2)*D0)==0
kx_sub=b+t*b1c; ky_sub=t*(-a1)
e3_sub=sp.expand(e3.subs({kx:kx_sub,ky:ky_sub}))
Q_sub =sp.expand(Q.subs({kx:kx_sub,ky:ky_sub}))
P_e3=sp.Poly(e3_sub,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
P_Q =sp.Poly(Q_sub ,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
P_D0=sp.Poly(D0,ly,domain=sp.QQ.frac_field(b,u,v,lx,t))
_,r3=sp.div(P_e3,P_D0); _,rQ=sp.div(P_Q,P_D0)
e3_line=sp.expand(r3.as_expr()); Q_line=sp.expand(rQ.as_expr())
et2=sp.expand(sp.Poly(e3_line,t).nth(2))
et1=sp.expand(sp.Poly(e3_line,t).nth(1))
et0=sp.expand(sp.Poly(e3_line,t).nth(0))
Qt2=sp.expand(sp.Poly(Q_line,t).nth(2))

print("=== discriminant of e3_line in t: Delta = et1^2 - 4*et2*et0 ===")
Delta = sp.expand(et1**2 - 4*et2*et0)
print("Delta degree in ly:", sp.Poly(Delta, ly).degree())
# reduce Delta mod D0
P_Delta=sp.Poly(Delta, ly, domain=sp.QQ.frac_field(b,u,v,lx,t))
_, rDelta = sp.div(P_Delta, P_D0)
Delta_red = sp.expand(rDelta.as_expr())
print("Delta mod D0 (remainder) zero?", rDelta.is_zero)
if not rDelta.is_zero:
    print("  -> e3_line has DISTINCT roots generically on D0=0 (Delta not divisible by D0)")
    # Try to factor Delta_red as a square in Q(b,u,v,lx,ly)/(D0).
    # Heuristic: factor Delta_red as polynomial in lx over Q(b,u,v)[ly] (keep ly symbolic).
    # If Delta_red is a perfect square (up to scalar) in the function field, it's split.
    fD = sp.factor(Delta_red)
    print("Delta mod D0 factored:")
    print(fD)
    # also try factor as poly in lx
    P_Dlx = sp.Poly(Delta_red, lx, domain=sp.QQ.frac_field(b,u,v,ly,t))
    print("Delta mod D0 as poly in lx, degree:", P_Dlx.degree())
else:
    print("  -> D0 DIVIDES Delta; e3_line has a double root on D0=0 generically")

print("\n=== check: is Delta mod D0 a square in K = Q(b,u,v,lx,ly)/(D0)? ===")
# A polynomial in the quotient is a square iff (after pulling out content) it
# is a perfect square as a polynomial. Hard in general; do a NUMERIC test:
# at several random specialisations of (b,u,v) and points on D0=0, check
# whether Delta_red evaluates to a square in Q (i.e., is a perfect square rational).
# This is only a necessary condition (sampling), not a proof.
rng = np.random.default_rng(7)
square_count = 0; nonsquare_count = 0
for _ in range(20):
    bn=float(rng.uniform(3,7)); un=float(rng.uniform(-3,5)); vn=float(rng.uniform(3,7))
    # pick lx, solve D0=0 cubic in ly for a real root, evaluate Delta_red
    lxs=float(rng.uniform(-2,6))
    c3=2.0; c2=-3*vn
    c1=-bn*un + 2*lxs**2 - 2*lxs*un + un**2 + vn**2
    c0=bn*lxs*vn - lxs**2*vn
    roots=np.roots([c3,c2,c1,c0])
    for r in roots:
        if abs(r.imag)<1e-6:
            lyn=r.real
            val = float(Delta_red.subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
            # is val a perfect square rational? (as float, check sqrt is rational-ish)
            if abs(val) < 1e-6: continue
            sv = np.sqrt(abs(val))
            # check if sv is close to a rational with small denominator
            frac = sp.nsimplify(sv, rational=False, tolerance=1e-4)
            # check square: val ~ (p/q)^2 ?
            is_sq = abs(sv - round(sv))**2 < 1e-3 or abs(sv - float(sp.Rational(round(sv*100),100)))**2<1e-3
            # simpler: just record sign and whether near a perfect square
            break
    # We won't rigorously decide square-ness from sampling; just record.
# (Sampling for square-ness is unreliable; skip counts.)

print("(square-ness decision requires algebraic methods; sampling unreliable -- skipped)")

print("\n=== NUMERIC: at valid configs, are BOTH roots of e3_line Q-roots? ===")
e3_line_fn = sp.lambdify((b,u,v,lx,ly,t), e3_line, 'numpy')
Q_line_fn  = sp.lambdify((b,u,v,lx,ly,t), Q_line, 'numpy')
et2_fn     = sp.lambdify((b,u,v,lx,ly), et2, 'numpy')
et1_fn     = sp.lambdify((b,u,v,lx,ly), sp.Poly(e3_line,t).nth(1), 'numpy')
et0_fn     = sp.lambdify((b,u,v,lx,ly), sp.Poly(e3_line,t).nth(0), 'numpy')
b1c_fn = sp.lambdify((b,u,v,lx,ly), b1c, 'numpy')
a1_fn  = sp.lambdify((b,u,v,lx,ly), (-a1), 'numpy')  # d_y = -a1; ky = t*d_y

def in_tri(P,V1,V2,V3):
    def s(p,q,r): return (p[0]-r[0])*(q[1]-r[1])-(q[0]-r[0])*(p[1]-r[1])
    d1=s(P,V1,V2);d2=s(P,V2,V3);d3=s(P,V3,V1)
    neg=(d1<0)|(d2<0)|(d3<0); pos=(d1>0)|(d2>0)|(d3>0)
    return not(neg and pos)

configs=[]
att=0
while len(configs)<40 and att<80000:
    att+=1
    bn=float(rng.uniform(3,7)); un=float(rng.uniform(-3,5)); vn=float(rng.uniform(3,7))
    Bn=(bn,0); Nn=(un/2,vn/2); Cn=(un,vn); Mn=(bn/2,0)
    lxs=float(rng.uniform(min(Bn[0],Nn[0],Cn[0])-0.5, max(Bn[0],Nn[0],Cn[0])+0.5))
    c3=2.0;c2=-3*vn
    c1=-bn*un+2*lxs**2-2*lxs*un+un**2+vn**2
    c0=bn*lxs*vn-lxs**2*vn
    roots=np.roots([c3,c2,c1,c0])
    for r in roots:
        if abs(r.imag)<1e-6:
            lyn=r.real
            if not in_tri((lxs,lyn),Bn,Nn,Cn): continue
            e2c=float(et2_fn(bn,un,vn,lxs,lyn))
            e1c=float(et1_fn(bn,un,vn,lxs,lyn))
            e0c=float(et0_fn(bn,un,vn,lxs,lyn))
            if abs(e2c)<1e-9: continue
            disc=e1c**2-4*e2c*e0c
            if disc<0: continue
            for tr in [(-e1c+np.sqrt(disc))/(2*e2c),(-e1c-np.sqrt(disc))/(2*e2c)]:
                dy=float(a1_fn(bn,un,vn,lxs,lyn))
                dbx=float(b1c_fn(bn,un,vn,lxs,lyn))
                Kxn=bn+tr*dbx; Kyn=tr*dy
                if not in_tri((Kxn,Kyn),Bn,Mn,Cn): continue
                if abs(Kxn-bn)<1e-9 and abs(Kyn)<1e-9: continue
                if abs(Kxn*lyn-Kyn*lxs)<1e-9: continue
                Qv=float(Q_line_fn(bn,un,vn,lxs,lyn,tr))
                configs.append((bn,un,vn,lxs,lyn,tr,Qv,e2c,e1c,e0c))
                if len(configs)>=40: break
    if len(configs)>=40: break

print(f"Found {len(configs)} valid configs.")
both=0; one=0; neither=0
for cfg in configs:
    bn,un,vn,lxs,lyn,tr,Qv,e2c,e1c,e0c=cfg
    r1=tr; r2=(-e1c/e2c)-r1
    Qr1=float(Q_line_fn(bn,un,vn,lxs,lyn,r1))
    Qr2=float(Q_line_fn(bn,un,vn,lxs,lyn,r2))
    z1=abs(Qr1)<1e-5; z2=abs(Qr2)<1e-5
    if z1 and z2: both+=1
    elif z1 or z2: one+=1
    else: neither+=1
print(f"Both roots Q-zero: {both}; exactly one: {one}; neither: {neither}")
print("-> if 'both' dominates, saturation (Q_line vanishes at ALL roots of e3_line) holds on real locus")
