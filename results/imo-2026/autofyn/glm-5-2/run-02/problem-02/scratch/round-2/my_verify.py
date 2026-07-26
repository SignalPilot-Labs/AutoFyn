"""
Independent from-scratch verification of the saturation identity for
imo-2026-02 (slug analytic-branch-cert), the round-1-vs-round-2 contradiction.

Goal: decide whether  Qt2*e3_line - et2*Q_line = D0*G  over the FIELD
Q(b,u,v,lx,t)[ly]  (true field division, NOT ring pseudo-remainder).

Also recompute Q at the alleged counterexample from its DEFINING formula and
check whether LHS vanishes there.
"""
import sympy as sp

# ---- coordinates ----
b, u, v, lx, ly, t = sp.symbols('b u v lx ly t')
kx, ky = sp.symbols('kx ky')

A = (0, 0)
Bpt = (b, 0)
Cpt = (u, v)
M = (b/2, 0)
Npt = (u/2, v/2)

def sub(P, d): return (P[0]-d[0], P[1]-d[1])
def cross(p, q): return p[0]*q[1] - p[1]*q[0]
def dot(p, q): return p[0]*q[0] + p[1]*q[1]

K = (kx, ky)
L = (lx, ly)

# e1: angle KBA = angle ACL  -> rays BK=K-B, BA=A-B ; CA=A-C, CL=L-C
BK = sub(K, Bpt); BA = sub(A, Bpt)
CA = sub(A, Cpt); CL = sub(L, Cpt)
e1 = sp.expand(cross(BK, BA)*dot(CA, CL) - cross(CA, CL)*dot(BK, BA))

# e2: angle LBK = angle LNC -> rays BL=L-B, BK=K-B ; NL=L-N, NC=C-N
BL = sub(L, Bpt); BK2 = sub(K, Bpt)
NL = sub(L, Npt); NC = sub(Cpt, Npt)
e2 = sp.expand(cross(BL, BK2)*dot(NL, NC) - cross(NL, NC)*dot(BL, BK2))

# e3: angle LCK = angle BMK -> rays CL=L-C, CK=K-C ; MB=B-M, MK=K-M
CL3 = sub(L, Cpt); CK = sub(K, Cpt)
MB = sub(Bpt, M); MK = sub(K, M)
e3 = sp.expand(cross(CL3, CK)*dot(MB, MK) - cross(MB, MK)*dot(CL3, CK))

# Q (cleared target): OM=ON <=> Q=0 for det(K,L) != 0
Ksq = kx**2 + ky**2
Lsq = lx**2 + ly**2
Csq = u**2 + v**2
Bsq = b**2
detKL = kx*ly - ky*lx
Q = sp.expand(2*(Ksq*ly - Lsq*ky)*(u - b) + 2*(kx*Lsq - lx*Ksq)*v - detKL*(Csq - Bsq))

print("Built e1,e2,e3,Q.")

# ---- homogeneous linearity in K-B ----
sx, sy = sp.symbols('sx sy')
e1s = sp.expand(e1.subs({kx: b+sx, ky: sy}))
e2s = sp.expand(e2.subs({kx: b+sx, ky: sy}))
c1 = sp.expand(e1s.subs({sx:0, sy:0}))
c2 = sp.expand(e2s.subs({sx:0, sy:0}))
print("c1 =", sp.simplify(c1), " c2 =", sp.simplify(c2))
assert sp.simplify(c1) == 0 and sp.simplify(c2) == 0

a1 = sp.expand(e1s.coeff(sx, 1)); b1c = sp.expand(e1s.coeff(sy, 1))
a2 = sp.expand(e2s.coeff(sx, 1)); b2c = sp.expand(e2s.coeff(sy, 1))

# D(L) = a1*b2 - b1*a2, factor
D = sp.expand(a1*b2c - b1c*a2)
D0 = sp.expand((b*lx*v - b*ly*u + 2*lx**2*ly - lx**2*v - 2*lx*ly*u
                + 2*ly**3 - 3*ly**2*v + ly*u**2 + ly*v**2))
# check D = -(b/4)|C|^2 D0
assert sp.simplify(D + (b/4)*(u**2+v**2)*D0) == 0
print("D = -(b/4)|C|^2 D0  OK")

# K = B + t*d(L), d=(b1,-a1)
kx_sub = b + t*b1c
ky_sub = t*(-a1)
e3_sub = sp.expand(e3.subs({kx: kx_sub, ky: ky_sub}))
Q_sub  = sp.expand(Q.subs({kx: kx_sub, ky: ky_sub}))

# field reduce mod D0 over Q(b,u,v,lx,t)[ly]
F = sp.QQ.frac_field(b, u, v, lx, t)
P_e3 = sp.Poly(e3_sub, ly, domain=F)
P_Q  = sp.Poly(Q_sub,  ly, domain=F)
P_D0 = sp.Poly(D0,     ly, domain=F)
q3, r3 = sp.div(P_e3, P_D0)
qQ, rQ = sp.div(P_Q,  P_D0)
e3_line = sp.expand(r3.as_expr())
Q_line  = sp.expand(rQ.as_expr())
print("e3_line deg in t:", sp.Poly(e3_line, t).degree(),
      " Q_line deg in t:", sp.Poly(Q_line, t).degree())

et2 = sp.expand(sp.Poly(e3_line, t).nth(2))
Qt2 = sp.expand(sp.Poly(Q_line,  t).nth(2))

# Lemma 3 relation: et2 = (b^3/2)|C|^2 (v-ly)|L-C|^2 - b^2 D
LmC = (lx-u)**2 + (ly-v)**2
claim_et2 = (b**3/2)*(u**2+v**2)*(v-ly)*LmC - b**2 * D
assert sp.simplify(et2 - claim_et2) == 0
print("Lemma 3 (et2 = (b^3/2)|C|^2(v-ly)|L-C|^2 - b^2 D)  OK")

# === THE CRITICAL SATURATION IDENTITY ===
# Qt2 * e3_line - et2 * Q_line  divisible by D0 in Q(b,u,v,lx,t)[ly] ?
LHS = sp.expand(Qt2 * e3_line - et2 * Q_line)
P_LHS = sp.Poly(LHS, ly, domain=F)
q_sat, r_sat = sp.div(P_LHS, P_D0)
print("=== SATURATION IDENTITY (true field division over Q(b,u,v,lx,t)[ly]) ===")
print("remainder identically zero?", r_sat.is_zero)
G = q_sat.as_expr()
print("G degree in t:", sp.Poly(sp.expand(G), t).degree() if not r_sat.is_zero else "N/A")

# also verify the proposed explicit G from the builder
G_prop = (b**4 * v * (u**2+v**2) / 4) * (
    t * ( (u**2+v**2)*(3*b**2 + b*lx - b*u) - 3*b**2*(lx*u + ly*v) )
    + ( b**2 + b*lx - b*u - 3*lx*u - 3*ly*v + 2*(u**2+v**2) ) )
check = sp.simplify(LHS - D0 * G_prop)
print("LHS - D0*G_prop == 0 (builder's explicit G)?", check == 0)

# === RECOMPUTE THE ALLEGED COUNTEREXAMPLE FROM DEFINING FORMULA ===
print("\n=== ALLEGED COUNTEREXAMPLE b=4,u=1,v=3,lx=1/2,ly=7/2 ===")
subs_pt = {b:4, u:1, v:3, lx:sp.Rational(1,2), ly:sp.Rational(7,2)}
# Check D0 = 0 there
D0_at = sp.expand(D0.subs(subs_pt))
print("D0 at pt =", D0_at, " (zero? ", D0_at == 0, ")")

# K = B + t*d(L). At this point, compute d(L) = (b1, -a1) symbolically then substitute.
# But the builder claims K=(8/3,8/3) at t=1/3. Verify that.
d_x = b1c
d_y = -a1
dx_at = sp.expand(d_x.subs(subs_pt))
dy_at = sp.expand(d_y.subs(subs_pt))
print("d(L) at pt =", (dx_at, dy_at))
t_val = sp.Rational(1,3)
Kx_at = 4 + t_val * dx_at
Ky_at = t_val * dy_at
print("K at t=1/3 (from d(L)) =", (sp.simplify(Kx_at), sp.simplify(Ky_at)), " (builder says (8/3,8/3))")

# Q from DEFINING formula
Q_at = sp.expand(Q.subs({b:4,u:1,v:3,kx:sp.Rational(8,3),ky:sp.Rational(8,3),
                          lx:sp.Rational(1,2),ly:sp.Rational(7,2)}))
print("Q from defining formula at K=(8/3,8/3),L=(1/2,7/2) =", Q_at, " = ", float(Q_at))
print(" (builder says 320/3; round-1 said 256)")

# Now check saturation identity at this point (as polynomial in t)
e3_at_t = sp.Poly(sp.expand(e3_sub.subs(subs_pt)), t)
Q_at_t  = sp.Poly(sp.expand(Q_sub.subs(subs_pt)),  t)
print("e3_sub at pt, poly in t:", e3_at_t.as_expr())
print("Q_sub  at pt, poly in t:", Q_at_t.as_expr())
et2_at = sp.expand(et2.subs(subs_pt))
Qt2_at = sp.expand(Qt2.subs(subs_pt))
print("et2 at pt =", et2_at)
print("Qt2 at pt =", Qt2_at)
LHS_at = sp.expand( (Qt2_at * sp.expand(e3_at_t.as_expr()) - et2_at * sp.expand(Q_at_t.as_expr())) )
print("Qt2*e3_sub - et2*Q_sub at pt (poly in t) =", sp.expand(LHS_at))
print("  is zero poly in t?", sp.simplify(LHS_at) == 0)

# === positivity check on inside arc: et2 = (b^3/2)|C|^2 (v-ly)|L-C|^2 on D0=0
# === sample a valid configuration and confirm et2 > 0, Q=0
print("\n=== positivity + theorem check on inside arc ===")
import numpy as np
rng = np.random.default_rng(12345)
found = 0
maxQ = 0.0; min_et2 = 1e9
b1_fn = sp.lambdify((b,u,v,lx,ly), b1c, 'numpy')
a1_fn = sp.lambdify((b,u,v,lx,ly), (-a1), 'numpy')
e3_line_fn = sp.lambdify((b,u,v,lx,ly,t), e3_line, 'numpy')
Q_line_fn = sp.lambdify((b,u,v,lx,ly,t), Q_line, 'numpy')
et2_fn = sp.lambdify((b,u,v,lx,ly), et2, 'numpy')

def in_tri(P,V1,V2,V3):
    def s(p,q,r): return (p[0]-r[0])*(q[1]-r[1])-(q[0]-r[0])*(p[1]-r[1])
    d1=s(P,V1,V2);d2=s(P,V2,V3);d3=s(P,V3,V1)
    neg=(d1<0)|(d2<0)|(d3<0); pos=(d1>0)|(d2>0)|(d3>0)
    return not(neg and pos)

att=0
while found < 25 and att < 60000:
    att += 1
    bn=float(rng.uniform(3,7)); un=float(rng.uniform(-3,5)); vn=float(rng.uniform(3,7))
    Bn=(bn,0); Nn=(un/2,vn/2); Cn=(un,vn); Mn=(bn/2,0)
    lxs=float(rng.uniform(min(Bn[0],Nn[0],Cn[0])-0.3, max(Bn[0],Nn[0],Cn[0])+0.3))
    c3=2.0;c2=-3*vn
    c1=-bn*un+2*lxs**2-2*lxs*un+un**2+vn**2
    c0=bn*lxs*vn-lxs**2*vn
    rts=np.roots([c3,c2,c1,c0])
    for r in rts:
        if abs(r.imag)<1e-6:
            lyn=r.real
            if not in_tri((lxs,lyn),Bn,Nn,Cn): continue
            e2c=float(et2_fn(bn,un,vn,lxs,lyn))
            if abs(e2c)<1e-9: continue
            e1c=float(sp.lambdify((b,u,v,lx,ly),sp.Poly(e3_line,t).nth(1),'numpy')(bn,un,vn,lxs,lyn))
            e0c=float(sp.lambdify((b,u,v,lx,ly),sp.Poly(e3_line,t).nth(0),'numpy')(bn,un,vn,lxs,lyn))
            disc=e1c**2-4*e2c*e0c
            if disc<0: continue
            for tr in [(-e1c+np.sqrt(disc))/(2*e2c),(-e1c-np.sqrt(disc))/(2*e2c)]:
                dy=float(a1_fn(bn,un,vn,lxs,lyn)); dbx=float(b1_fn(bn,un,vn,lxs,lyn))
                Kxn=bn+tr*dbx; Kyn=tr*dy
                if not in_tri((Kxn,Kyn),Bn,Mn,Cn): continue
                if abs(Kxn*lyn-Kyn*lxs)<1e-9: continue
                Qv=float(Q_line_fn(bn,un,vn,lxs,lyn,tr))
                found += 1
                maxQ=max(maxQ,abs(Qv))
                min_et2=min(min_et2,e2c)
                if found>=25: break
    if found>=25: break
print(f"valid configs: {found}; max|Q_line|={maxQ:.2e}; min et2={min_et2:.4f}")
