"""
Independent from-scratch verification of the resultant-in-t certificate
for imo-2026-02 (slug analytic-resultant-cert).

We rebuild e1,e2,e3,Q from the cross/dot tangent form, perform the
2-var reduction (cubic D0 + line K = B + t*d(L)), field-reduce e3 and Q
mod D0 over QQ.frac_field(b,u,v,lx,t)[ly], obtain the quadratics
e3_line, Q_line in t, and compute res_t(e3_line, Q_line).
"""
import sympy as sp

# ---- coordinates ----
b, u, v, lx, ly, t = sp.symbols('b u v lx ly t')
kx, ky = sp.symbols('kx ky')

A = (0, 0)
B = (b, 0)
C = (u, v)
M = (b/2, 0)
N = (u/2, v/2)

def sub(P, d):
    return (P[0]-d[0], P[1]-d[1])
def add(P, d):
    return (P[0]+d[0], P[1]+d[1])
def cross(p, q):
    return p[0]*q[1] - p[1]*q[0]
def dot(p, q):
    return p[0]*q[0] + p[1]*q[1]

K = (kx, ky)
L = (lx, ly)

# ---- e1: angle KBA = angle ACL ----
# rays BK = K-B, BA = A-B;  CA = A-C, CL = L-C
BK = sub(K, B); BA = sub(A, B)
CA = sub(A, C); CL = sub(L, C)
e1 = cross(BK, BA)*dot(CA, CL) - cross(CA, CL)*dot(BK, BA)
e1 = sp.expand(e1)

# ---- e2: angle LBK = angle LNC ----
# rays BL = L-B, BK = K-B;  NL = L-N, NC = C-N
BL = sub(L, B); BK2 = sub(K, B)
NL = sub(L, N); NC = sub(C, N)
e2 = cross(BL, BK2)*dot(NL, NC) - cross(NL, NC)*dot(BL, BK2)
e2 = sp.expand(e2)

# ---- e3: angle LCK = angle BMK ----
# rays CL = L-C, CK = K-C;  MB = B-M, MK = K-M
CL3 = sub(L, C); CK = sub(K, C)
MB = sub(B, M); MK = sub(K, M)
e3 = cross(CL3, CK)*dot(MB, MK) - cross(MB, MK)*dot(CL3, CK)
e3 = sp.expand(e3)

# ---- Q (cleared target) ----
# OM=ON  <=>  Q=0  (for det(K,L) != 0)
Ksq = kx**2 + ky**2
Lsq = lx**2 + ly**2
Csq = u**2 + v**2
Bsq = b**2
detKL = kx*ly - ky*lx
Q = 2*(Ksq*ly - Lsq*ky)*(u - b) + 2*(kx*Lsq - lx*Ksq)*v - detKL*(Csq - Bsq)
Q = sp.expand(Q)

print("=== STEP 1: homogeneous linearity of e1,e2 in (sx,sy)=(K-B) ===")
# substitute kx = b + sx, ky = sy
sx, sy = sp.symbols('sx sy')
e1s = sp.expand(e1.subs({kx: b+sx, ky: sy}))
e2s = sp.expand(e2.subs({kx: b+sx, ky: sy}))
# collect in sx, sy
e1_coll = sp.collect(e1s, [sx, sy])
e2_coll = sp.collect(e2s, [sx, sy])
a1 = sp.expand(e1s.coeff(sx, 1))
b1c = sp.expand(e1s.coeff(sy, 1))
c1 = sp.expand(e1s.subs({sx:0, sy:0}))
a2 = sp.expand(e2s.coeff(sx, 1))
b2c = sp.expand(e2s.coeff(sy, 1))
c2 = sp.expand(e2s.subs({sx:0, sy:0}))
print("c1 (const of e1 in sx,sy) =", sp.simplify(c1))
print("c2 (const of e2 in sx,sy) =", sp.simplify(c2))
assert sp.simplify(c1) == 0, "e1 not homogeneous-linear!"
assert sp.simplify(c2) == 0, "e2 not homogeneous-linear!"
# verify e1 = a1*sx + b1*sy
assert sp.simplify(e1s - (a1*sx + b1c*sy)) == 0
assert sp.simplify(e2s - (a2*sx + b2c*sy)) == 0
print("e1 = a1*sx + b1*sy  (homogeneous linear)  OK")
print("e2 = a2*sx + b2*sy  (homogeneous linear)  OK")

print("\n=== STEP 2: D(L) = a1*b2 - b1*a2, factor D = -(b/4)|C|^2 * D0 ===")
D = sp.expand(a1*b2c - b1c*a2)
Dfact = sp.factor(D)
print("D (factored) =", Dfact)
# expected D0
D0 = (b*lx*v - b*ly*u + 2*lx**2*ly - lx**2*v - 2*lx*ly*u
      + 2*ly**3 - 3*ly**2*v + ly*u**2 + ly*v**2)
D0 = sp.expand(D0)
quot = sp.simplify(D / (-(b/4)*(u**2+v**2)*D0))
print("D / (-(b/4)|C|^2 D0) =", quot)
assert sp.simplify(D + (b/4)*(u**2+v**2)*D0) == 0, "D factorisation FAILS"
print("D = -(b/4)|C|^2 * D0  OK")

print("\n=== STEP 3: d(L) = (b1, -a1); K = B + t*d(L) ===")
d_x = b1c
d_y = -a1
# substitute into e1, e2, e3, Q
kx_sub = b + t*d_x
ky_sub = t*d_y
e1_sub = sp.expand(e1.subs({kx: kx_sub, ky: ky_sub}))
e2_sub = sp.expand(e2.subs({kx: kx_sub, ky: ky_sub}))
e3_sub = sp.expand(e3.subs({kx: kx_sub, ky: ky_sub}))
Q_sub  = sp.expand(Q.subs({kx: kx_sub, ky: ky_sub}))
# on D0=0, e1_sub should be identically 0, e2_sub = -t*D
# verify e1_sub is divisible by D (up to the |C|^2,b factor)
print("e1_sub / D0  remainder (check e1_sub vanishes on D0=0)")
# Build Poly in ly with domain QQ(b,u,v,lx,t)
P_e1 = sp.Poly(e1_sub, ly, domain=sp.QQ.frac_field(b, u, v, lx, t))
P_D0 = sp.Poly(D0, ly, domain=sp.QQ.frac_field(b, u, v, lx, t))
q_e1, r_e1 = sp.div(P_e1, P_D0)
print("e1_sub mod D0 (remainder) identically zero?", r_e1.is_zero)
# e2_sub should be -t*D + 0 on D0=0, i.e. e2_sub + t*D is divisible by D0
P_e2 = sp.Poly(e2_sub + t*( -(b/4)*(u**2+v**2)*D0 ), ly, domain=sp.QQ.frac_field(b, u, v, lx, t))
# Actually let's just reduce e2_sub mod D0 and check remainder = -t*D reduced
q_e2, r_e2 = sp.div(sp.Poly(e2_sub, ly, domain=sp.QQ.frac_field(b, u, v, lx, t)), P_D0)
print("e2_sub mod D0 (remainder) =", sp.factor(r_e2.as_expr()))
# We expect remainder to be -t*D reduced mod D0 = -t*D since D is multiple of D0
# Actually -t*D = -t * (-(b/4)|C|^2 D0) = (t*b/4)|C|^2 D0 which reduces to 0 mod D0.
# Hmm so e2_sub mod D0 should be 0 if e2_sub = -t*D exactly. Let me check directly.
print("e2_sub + t*D == 0 identically?", sp.simplify(e2_sub + t*D) == 0)

print("\n=== STEP 4: field-reduce e3_sub and Q_sub mod D0 -> quadratics in t ===")
P_e3 = sp.Poly(e3_sub, ly, domain=sp.QQ.frac_field(b, u, v, lx, t))
P_Q  = sp.Poly(Q_sub,  ly, domain=sp.QQ.frac_field(b, u, v, lx, t))
q3, r3 = sp.div(P_e3, P_D0)
qQ, rQ = sp.div(P_Q,  P_D0)
e3_line = sp.expand(r3.as_expr())
Q_line  = sp.expand(rQ.as_expr())
print("e3_line degree in t:", sp.Poly(e3_line, t).degree())
print("Q_line  degree in t:", sp.Poly(Q_line, t).degree())
# confirm both quadratic in t
assert sp.Poly(e3_line, t).degree() <= 2
assert sp.Poly(Q_line, t).degree() <= 2

# leading coeffs
et2 = sp.expand(sp.Poly(e3_line, t).nth(2))
et1 = sp.expand(sp.Poly(e3_line, t).nth(1))
et0 = sp.expand(sp.Poly(e3_line, t).nth(0))
Qt2 = sp.expand(sp.Poly(Q_line, t).nth(2))
Qt1 = sp.expand(sp.Poly(Q_line, t).nth(1))
Qt0 = sp.expand(sp.Poly(Q_line, t).nth(0))
print("et2 =", et2)
print("Qt2 =", Qt2)

print("\n=== STEP 5: verify et2-on-D0 relation ===")
# et2 = (b^3/2)|C|^2 (v-ly)|L-C|^2 - b^2 * D
LmC = (lx-u)**2 + (ly-v)**2
claim_et2 = (b**3/2)*(u**2+v**2)*(v-ly)*LmC - b**2 * D
diff = sp.expand(et2 - claim_et2)
print("et2 - (claim - b^2 D) == 0?", sp.simplify(diff) == 0)
assert sp.simplify(diff) == 0, "et2-on-D relation FAILS"
print("et2 = (b^3/2)|C|^2 (v-ly)|L-C|^2 - b^2 D  (polynomial identity) OK")

print("\n=== STEP 6: compute resultant res_t(e3_line, Q_line) ===")
# Use Poly in t over the fraction field QQ(b,u,v,lx,ly)
P_e3_t = sp.Poly(e3_line, t, domain=sp.QQ.frac_field(b, u, v, lx, ly))
P_Q_t  = sp.Poly(Q_line,  t, domain=sp.QQ.frac_field(b, u, v, lx, ly))
res = sp.resultant(P_e3_t, P_Q_t)
res = sp.simplify(res)
print("res computed; attempting factorisation...")
res_fact = sp.factor(res)
print("res_t(e3_line, Q_line) factored =")
print(res_fact)

print("\n=== STEP 7: check divisibility by D0^2 and the claimed cofactors ===")
# D0 is in lx,ly; check res / D0^2
P_D0_ly = sp.Poly(D0, ly, domain=sp.QQ.frac_field(b, u, v, lx))
# We work in QQ(b,u,v,lx,ly); divide res by D0^2 as a poly in ly
res_poly = sp.Poly(sp.together(res), ly, domain=sp.QQ.frac_field(b, u, v, lx))
D0sq_poly = sp.Poly(sp.expand(D0**2), ly, domain=sp.QQ.frac_field(b, u, v, lx))
q_res, r_res = sp.div(res_poly, D0sq_poly)
print("res mod D0^2 (remainder) zero?", r_res.is_zero)
if r_res.is_zero:
    R = sp.simplify(q_res.as_expr())
    print("R = res / D0^2 =")
    print(sp.factor(R))
    # check the claimed prefactor (b^8/16) v^2 |C|^2 (|C|^2 - b^2)
    pref = (b**8/16) * v**2 * (u**2+v**2) * (u**2+v**2 - b**2)
    ratio = sp.simplify(R / pref)
    print("R / [(b^8/16) v^2 |C|^2 (|C|^2-b^2)] =")
    print(sp.factor(ratio))
else:
    print("D0^2 does NOT divide res! remainder:")
    print(sp.factor(r_res.as_expr()))
