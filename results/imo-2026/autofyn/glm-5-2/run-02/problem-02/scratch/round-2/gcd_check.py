"""
Investigate the GCD structure of e3_line and Q_line modulo D0=0,
to determine whether the resultant closes via 'both roots shared'
(saturation) or 'one shared root' (needs root-selection).

Also: numerically sample valid configurations, find roots of e3_line
and check which are roots of Q_line.
"""
import sympy as sp
import numpy as np

b, u, v, lx, ly, t = sp.symbols('b u v lx ly t')
kx, ky = sp.symbols('kx ky')

A = (0, 0); Bpt = (b, 0); Cpt = (u, v)
M = (b/2, 0); N = (u/2, v/2)
def sub(P, d): return (P[0]-d[0], P[1]-d[1])
def cross(p, q): return p[0]*q[1] - p[1]*q[0]
def dot(p, q): return p[0]*q[0] + p[1]*q[1]
K = (kx, ky); L = (lx, ly)

# e1
BK = sub(K, Bpt); BA = sub(A, Bpt); CA = sub(A, Cpt); CL = sub(L, Cpt)
e1 = sp.expand(cross(BK, BA)*dot(CA, CL) - cross(CA, CL)*dot(BK, BA))
# e2
BL = sub(L, Bpt); NL = sub(L, N); NC = sub(Cpt, N)
e2 = sp.expand(cross(BL, BK)*dot(NL, NC) - cross(NL, NC)*dot(BL, BK))
# e3
CK = sub(K, Cpt); MB = sub(Bpt, M); MK = sub(K, M)
e3 = sp.expand(cross(CL, CK)*dot(MB, MK) - cross(MB, MK)*dot(CL, CK))
# Q
Ksq = kx**2+ky**2; Lsq = lx**2+ly**2; Csq = u**2+v**2; Bsq = b**2
detKL = kx*ly-ky*lx
Q = sp.expand(2*(Ksq*ly - Lsq*ky)*(u-b) + 2*(kx*Lsq - lx*Ksq)*v - detKL*(Csq-Bsq))

# homogeneous-linear in sx,sy
sx, sy = sp.symbols('sx sy')
e1s = sp.expand(e1.subs({kx: b+sx, ky: sy}))
e2s = sp.expand(e2.subs({kx: b+sx, ky: sy}))
a1 = sp.expand(e1s.coeff(sx, 1)); b1c = sp.expand(e1s.coeff(sy, 1))
a2 = sp.expand(e2s.coeff(sx, 1)); b2c = sp.expand(e2s.coeff(sy, 1))
D = sp.expand(a1*b2c - b1c*a2)
D0 = sp.expand(-(4*D)/(b*(u**2+v**2)))
# verify
assert sp.simplify(D + (b/4)*(u**2+v**2)*D0) == 0

# d(L) = (b1, -a1), K = B + t*d
kx_sub = b + t*b1c; ky_sub = t*(-a1)
e3_sub = sp.expand(e3.subs({kx: kx_sub, ky: ky_sub}))
Q_sub  = sp.expand(Q.subs({kx: kx_sub, ky: ky_sub}))

# field-reduce mod D0
P_e3 = sp.Poly(e3_sub, ly, domain=sp.QQ.frac_field(b, u, v, lx, t))
P_Q  = sp.Poly(Q_sub,  ly, domain=sp.QQ.frac_field(b, u, v, lx, t))
P_D0 = sp.Poly(D0, ly, domain=sp.QQ.frac_field(b, u, v, lx, t))
q3, r3 = sp.div(P_e3, P_D0); qQ, rQ = sp.div(P_Q, P_D0)
e3_line = sp.expand(r3.as_expr()); Q_line = sp.expand(rQ.as_expr())
et2 = sp.expand(sp.Poly(e3_line, t).nth(2))
Qt2 = sp.expand(sp.Poly(Q_line, t).nth(2))

print("=== SATURATION IDENTITY CHECK ===")
# Qt2*e3_line - et2*Q_line  mod D0 (field reduction in ly)  == 0 ?
LHS = sp.expand(Qt2*e3_line - et2*Q_line)
P_LHS = sp.Poly(LHS, ly, domain=sp.QQ.frac_field(b, u, v, lx, t))
qS, rS = sp.div(P_LHS, P_D0)
print("Qt2*e3_line - et2*Q_line  mod D0  remainder zero?", rS.is_zero)
if not rS.is_zero:
    print("  -> SATURATION IDENTITY IS FALSE; GCD degree 1 (one shared root)")
else:
    print("  -> SATURATION IDENTITY IS TRUE; Q_line proportional to e3_line mod D0")
    G = sp.expand(qS.as_expr())
    print("  G (quotient) degree in t:", sp.Poly(G, t).degree())
    print("  G =", G)

print("\n=== R mod D0 check (multiplicity of D0 in resultant) ===")
# R from the factorisation
Rexpr = (-b**2*u**2 - b**2*v**2 - 3*b*lx**2*u - 3*b*lx*ly*v + 4*b*lx*u**2
         + b*lx*v**2 + 3*b*ly*u*v - b*u**3 - b*u*v**2 + 9*lx**2*u**2
         + 18*lx*ly*u*v - 12*lx*u**3 - 12*lx*u*v**2 + 9*ly**2*v**2
         - 12*ly*u**2*v - 12*ly*v**3 + 4*u**4 + 8*u**2*v**2 + 4*v**4)
P_R = sp.Poly(sp.expand(Rexpr), ly, domain=sp.QQ.frac_field(b, u, v, lx))
qR, rR = sp.div(P_R, P_D0)
print("R mod D0 remainder zero?", rR.is_zero)
print("  -> if False, D0 multiplicity in resultant is EXACTLY 2")

print("\n=== GCD of e3_line, Q_line over field Q(b,u,v,lx)[ly]/(D0) as polys in t ===")
# Work over the quotient: substitute ly-reduction. Build GCD via Euclidean algorithm
# over QQ.frac_field(b,u,v,lx,ly) but reduce each remainder mod D0.
# Use Poly in t with domain QQ.frac_field(b,u,v,lx,ly), and reduce mod D0 in ly after each step.
def reduce_mod_D0(expr):
    P = sp.Poly(sp.expand(expr), ly, domain=sp.QQ.frac_field(b, u, v, lx, t))
    _, r = sp.div(P, P_D0)
    return sp.expand(r.as_expr())

# GCD via Euclidean algorithm (pseudo-gcd over the field with D0-reduction)
f = sp.Poly(e3_line, t, domain=sp.QQ.frac_field(b, u, v, lx, ly))
g = sp.Poly(Q_line, t, domain=sp.QQ.frac_field(b, u, v, lx, ly))
print("deg e3_line in t:", f.degree(), " deg Q_line in t:", g.degree())
# do one step: f = q*g + r, then reduce r mod D0
if f.degree() >= g.degree() and g.degree() > 0:
    # divide f by g in t
    q_step, r_step = sp.div(f, g)
    r_red = reduce_mod_D0(sp.expand(r_step.as_expr()))
    print("after 1 Euclidean step, remainder (mod D0) degree in t:",
          sp.Poly(r_red, t).degree() if r_red != 0 else "zero")
    if r_red == 0:
        print("  -> g divides f mod D0; GCD = g (degree 2); SATURATION confirmed")
    else:
        # next step: g mod r_red
        g2 = sp.Poly(Q_line, t, domain=sp.QQ.frac_field(b, u, v, lx, ly))
        r2_poly = sp.Poly(r_red, t, domain=sp.QQ.frac_field(b, u, v, lx, ly))
        if r2_poly.degree() > 0:
            q2, r2 = sp.div(g2, r2_poly)
            r2_red = reduce_mod_D0(sp.expand(r2.as_expr()))
            print("after 2nd step, remainder (mod D0):", "zero" if r2_red==0 else "nonzero")
            if r2_red == 0:
                print("  -> GCD = r_red (degree", sp.Poly(r_red,t).degree(), "); ONE shared root")
            else:
                print("  -> GCD trivial?? unexpected")
        else:
            print("  r_red is constant nonzero -> GCD trivial, but resultant says shared root...")
else:
    print("unexpected degree")

print("\n=== NUMERICAL: roots of e3_line and Q_line at valid configurations ===")
# Generate valid configurations numerically.
# Strategy: pick b,u,v; pick L on D0=0 inside △BNC; solve e3_line(t)=0 for t;
# check which roots give K inside △BMC and Q≈0.
rng = np.random.default_rng(12345)

def D0num(bn,un,vn,lxn,lyn):
    return (bn*lxn*vn - bn*lyn*un + 2*lxn**2*lyn - lxn**2*vn - 2*lxn*lyn*un
            + 2*lyn**3 - 3*lyn**2*vn + lyn*un**2 + lyn*vn**2)

def in_triangle(P, V1, V2, V3):
    def s(p,q,r): return (p[0]-r[0])*(q[1]-r[1]) - (q[0]-r[0])*(p[1]-r[1])
    d1=s(P,V1,V2); d2=s(P,V2,V3); d3=s(P,V3,V1)
    neg = (d1<0)|(d2<0)|(d3<0); pos = (d1>0)|(d2>0)|(d3>0)
    return not (neg and pos)

# symbolic e3_line, Q_line, et2 as functions for numeric eval
e3_line_fn = sp.lambdify((b,u,v,lx,ly,t), e3_line, 'numpy')
Q_line_fn  = sp.lambdify((b,u,v,lx,ly,t), Q_line, 'numpy')
et2_fn     = sp.lambdify((b,u,v,lx,ly), et2, 'numpy')
# also full e3, Q (not reduced) for cross-check
e3_full_fn = sp.lambdify((b,u,v,lx,ly,t), e3_sub, 'numpy')
Q_full_fn  = sp.lambdify((b,u,v,lx,ly,t), Q_sub, 'numpy')

# Parametrise L by lx, solve cubic D0(lx,ly)=0 for ly, pick a real root inside △BNC.
import numpy as np
configs = []
att = 0
while len(configs) < 30 and att < 50000:
    att += 1
    bn = float(rng.uniform(3,7))
    un = float(rng.uniform(-3,5))
    vn = float(rng.uniform(3,7))
    Bn=(bn,0); Nn=(un/2,vn/2); Cn=(un,vn)
    # lx range inside triangle BNC horizontally
    lxs = rng.uniform(min(bn,un,un/2)-0.5, max(bn,un,un/2)+0.5)
    # D0 as cubic in ly: 2 ly^3 + (-3v) ly^2 + (b lx - b ... wait D0 = b*lx*v - b*ly*u + 2 lx^2 ly - lx^2 v - 2 lx ly u + 2 ly^3 - 3 ly^2 v + ly u^2 + ly v^2
    # collect in ly:
    # ly^3: 2
    # ly^2: -3v
    # ly^1: (-b*u) + (2 lx^2) (-2 lx u) + (u^2) + (v^2)  -> wait term by term:
    #   -b*ly*u  -> -b*u
    #   +2*lx^2*ly -> 2 lx^2
    #   -2*lx*ly*u -> -2 lx u
    #   +ly*u^2 -> u^2
    #   +ly*v^2 -> v^2
    # ly^0: b*lx*v - lx^2 v
    c3 = 2.0
    c2 = -3*vn
    c1 = -bn*un + 2*lxs**2 - 2*lxs*un + un**2 + vn**2
    c0 = bn*lxs*vn - lxs**2*vn
    roots = np.roots([c3,c2,c1,c0])
    for r in roots:
        if abs(r.imag) < 1e-6:
            lyn = r.real
            Lptn = (lxs, lyn)
            if in_triangle(Lptn, Bn, Nn, Cn):
                # solve e3_line(t)=0
                e2_c = float(et2_fn(bn,un,vn,lxs,lyn))
                e1_c = float(sp.Poly(e3_line,t).nth(1).subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
                e0_c = float(sp.Poly(e3_line,t).nth(0).subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
                if abs(e2_c) < 1e-9: continue
                disc = e1_c**2 - 4*e2_c*e0_c
                if disc < 0: continue
                for tr in [(-e1_c+np.sqrt(disc))/(2*e2_c), (-e1_c-np.sqrt(disc))/(2*e2_c)]:
                    Kxn = bn + tr*b1c.subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn})
                    Kyn = tr*(-a1.subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
                    Kxn=float(Kxn); Kyn=float(Kyn)
                    Mn=(bn/2,0)
                    if not in_triangle((Kxn,Kyn), Bn, Mn, Cn): continue
                    # K != B
                    if abs(Kxn-bn)<1e-9 and abs(Kyn)<1e-9: continue
                    # check det(K,L)!=0
                    if abs(Kxn*lyn - Kyn*lxs) < 1e-9: continue
                    Qv = float(Q_line_fn(bn,un,vn,lxs,lyn,tr))
                    Qfv = float(Q_full_fn(bn,un,vn,lxs,lyn,tr))
                    e3v = float(e3_line_fn(bn,un,vn,lxs,lyn,tr))
                    e3fv = float(e3_full_fn(bn,un,vn,lxs,lyn,tr))
                    configs.append((bn,un,vn,lxs,lyn,tr,Qv,Qfv,e3v,e3fv))
                    if len(configs)>=30: break
        if len(configs)>=30: break

print(f"Found {len(configs)} valid configurations.")
both_Q_zero_count = 0
one_Q_zero_count = 0
for cfg in configs:
    bn,un,vn,lxs,lyn,tr,Qv,Qfv,e3v,e3fv = cfg
    # find the OTHER root of e3_line
    e2_c = float(et2_fn(bn,un,vn,lxs,lyn))
    e1_c = float(sp.Poly(e3_line,t).nth(1).subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
    e0_c = float(sp.Poly(e3_line,t).nth(0).subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
    # roots r1,r2: sum = -e1/e2, product = e0/e2
    r1 = tr
    r2 = (-e1_c/e2_c) - r1
    Q_r1 = float(Q_line_fn(bn,un,vn,lxs,lyn,r1))
    Q_r2 = float(Q_line_fn(bn,un,vn,lxs,lyn,r2))
    # also check if r2 gives K inside triangle
    K2x = bn + r2*float(b1c.subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
    K2y = r2*float(-a1.subs({b:bn,u:un,v:vn,lx:lxs,ly:lyn}))
    Mn=(bn/2,0); Bn=(bn,0); Cn=(un,vn)
    r2_inside = in_triangle((K2x,K2y), Bn, Mn, Cn) and (abs(K2x-bn)>1e-9 or abs(K2y)>1e-9)
    if abs(Q_r1)<1e-6 and abs(Q_r2)<1e-6:
        both_Q_zero_count += 1
    elif abs(Q_r1)<1e-6 or abs(Q_r2)<1e-6:
        one_Q_zero_count += 1
    print(f"  b={bn:.2f} L=({lxs:.2f},{lyn:.2f}) t_cfg={tr:.4f}: Q(t1)={Q_r1:.2e} Q(t2)={Q_r2:.2e} t2_inside={r2_inside}")

print(f"\nBoth roots Q-zero: {both_Q_zero_count}; exactly one: {one_Q_zero_count}; total {len(configs)}")
