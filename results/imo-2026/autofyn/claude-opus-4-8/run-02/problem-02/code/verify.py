"""
Exact symbolic verification for IMO 2026 P2 (imo-2026-02), approach trig-metric-identity.
General triangle B=(0,0), C=(a,0), A=(p,q), q>0.  s = tan(theta/2), theta=∠KBA=∠ACL.
K = tK*u  on the ray from B (clockwise of BA);  L = C + tL*dL on the ray from C (CCW of CA).
Everything below is an EXACT polynomial identity in Q(p,q,a,s)[tK,tL]; numerics are never
used as a proof step -- the decisive facts are the two 'assert' lines (exact zeros).
"""
import sympy as sp

p, q, a, s, tK, tL = sp.symbols('p q a s tK tL', real=True)

B = sp.Matrix([0, 0]); C = sp.Matrix([a, 0]); A = sp.Matrix([p, q])
M = (A + B)/2; N = (A + C)/2

# w*Rot(-theta) applied to BA=(p,q), and w*Rot(+theta) applied to CA=(p-a,q), w=1+s^2:
u  = sp.Matrix([ p*(1-s**2) + q*(2*s),      -p*(2*s) + q*(1-s**2)     ])   # dir of K-ray from B
dL = sp.Matrix([ (p-a)*(1-s**2) - q*(2*s),  (p-a)*(2*s) + q*(1-s**2)  ])   # dir of L-ray from C
K = tK*u
L = C + tL*dL

def cross(V, W): return sp.expand(V[0]*W[1] - V[1]*W[0])
def dot(V, W):   return sp.expand(V[0]*W[0] + V[1]*W[1])

# ---- (A) Orientation: two crosses are manifestly positive ----
print("cross(MB,MK) =", sp.factor(cross(B-M, K-M)))          # = s*tK*(p^2+q^2)
print("cross(NL,NC) =", sp.factor(cross(L-N, C-N)))          # = s*tL*((p-a)^2+q^2)

# ---- (B) The two angle-condition polynomials ----
# cond2: ∠LBK=∠LNC  -> E2 ; cond3: ∠LCK=∠BMK -> E3
E2 = cross(L-B, K-B)*dot(L-N, C-N) - cross(L-N, C-N)*dot(L-B, K-B)
E3 = cross(L-C, K-C)*dot(B-M, K-M) - cross(B-M, K-M)*dot(L-C, K-C)
H = sp.expand(sp.cancel(E2/tK))   # depends on tL only
G = sp.expand(sp.cancel(E3/tL))   # depends on tK only
assert tK not in H.free_symbols and tL not in G.free_symbols
print("H depends only on tL, G only on tK; degrees:",
      sp.degree(sp.Poly(H, tL)), sp.degree(sp.Poly(G, tK)))

# ---- (C) Target: OM=ON  <=>  O_x=(2p+a)/4  <=>  T:=4*numx-(2p+a)*D = 0 ----
Ax, Ay = A; Kx, Ky = K[0], K[1]; Lx, Ly = L[0], L[1]
D    = 2*(Ax*(Ky-Ly) + Kx*(Ly-Ay) + Lx*(Ay-Ky))
numx = (Ax**2+Ay**2)*(Ky-Ly) + (Kx**2+Ky**2)*(Ly-Ay) + (Lx**2+Ly**2)*(Ay-Ky)
T = sp.expand(4*numx - (2*p+a)*D)

# ---- (D) Exact cofactor identity  T = qG*G + qH*H  (=> T vanishes whenever G=H=0) ----
PT = sp.Poly(sp.expand(T), tK)
qG, T1 = sp.div(PT, sp.Poly(G, tK), tK)
qH, R2 = sp.div(sp.Poly(sp.expand(T1.as_expr()), tL), sp.Poly(H, tL), tL)
residual = sp.expand(qG.as_expr()*G + qH.as_expr()*H - T)
print("remainder after reducing T mod <G,H> :", sp.simplify(R2.as_expr()))
print("EXACT cofactor check  T-(qG*G+qH*H) =", sp.simplify(residual))
assert sp.simplify(residual) == 0 and sp.simplify(R2.as_expr()) == 0
print("VERIFIED: T = qG*G + qH*H identically  =>  G=H=0 forces O_x=(2p+a)/4  =>  OM=ON.")

# ---- (E) POLYNOMIAL cofactor identity: clear denominators so cofactors are polynomials.
#      The only denominator introduced by the two divisions is f (below); multiplying by f
#      yields  f*T = QG*G + QH*H  with QG,QH in Q[p,q,a,s,tK,tL] (genuine polynomials).
f = 2*s*(p**2+q**2) - 2*a*p*s + a*q*(1-s**2)
dG = sp.denom(sp.cancel(sp.together(qG.as_expr())))
dH = sp.denom(sp.cancel(sp.together(qH.as_expr())))
c  = sp.lcm(dG, dH)
print("denominator content c = lcm(denoms) factor:", sp.factor(c))
print("c - f  =", sp.simplify(c - f))                       # c equals f exactly
assert sp.simplify(c - f) == 0
QG = sp.expand(sp.cancel(c*qG.as_expr()))
QH = sp.expand(sp.cancel(c*qH.as_expr()))
assert tK in QG.free_symbols or QG.is_polynomial()          # sanity
poly_resid = sp.expand(f*T - (QG*G + QH*H))
print("EXACT polynomial identity  f*T-(QG*G+QH*H) =", sp.simplify(poly_resid))
assert sp.simplify(poly_resid) == 0
# QG,QH really are polynomials (no tK,tL,p,q,a,s in any denominator):
assert sp.denom(sp.cancel(QG)) == 1 and sp.denom(sp.cancel(QH)) == 1

# ---- (F) Geometric meaning of f:  f = (1+s^2)*AB*AC*sin(angleA + theta) > 0. ----
# AB*AC*sin(angleA) = |cross(B-A,C-A)| = q*a ;  AB*AC*cos(angleA) = dot(B-A,C-A) = p^2+q^2-a*p.
cth, sth = (1-s**2)/(1+s**2), 2*s/(1+s**2)          # cos(theta), sin(theta) with s=tan(theta/2)
f_geo = (1+s**2)*( (q*a)*cth + (p**2+q**2-a*p)*sth ) # (1+s^2)*AB*AC*sin(A+theta)
print("f - (1+s^2)*AB*AC*sin(A+theta) =", sp.simplify(f - f_geo))
assert sp.simplify(f - f_geo) == 0
print("VERIFIED: f*T=QG*G+QH*H (polynomial) and f=(1+s^2)*AB*AC*sin(A+theta)>0 => T=0 => OM=ON.")
