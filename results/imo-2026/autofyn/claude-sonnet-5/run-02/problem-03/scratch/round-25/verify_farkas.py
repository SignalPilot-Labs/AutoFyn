from fractions import Fraction as F
from sympy import symbols, Rational, simplify, Poly

p1,p2,p3 = symbols('p1 p2 p3')

def check(name, terms):
    # terms: list of (lhs_expr, rhs_value, weight, strict_bool)
    lhs_sum = 0
    rhs_sum = 0
    any_strict=False
    for lhs, rhs, w, strict in terms:
        lhs_sum += w*lhs
        rhs_sum += w*rhs
        if strict and w>0: any_strict=True
    lhs_sum = simplify(lhs_sum)
    rhs_sum = simplify(rhs_sum)
    print(name, "LHS sum simplified:", lhs_sum, " RHS sum:", rhs_sum, " any_strict:", any_strict)
    assert lhs_sum == 0, f"{name} LHS doesn't vanish: {lhs_sum}"
    assert rhs_sum == 0, f"{name} RHS doesn't vanish: {rhs_sum}"
    assert any_strict, f"{name} no strict inequality used"
    print(name, "OK: certifies 0<0 -> infeasible")

R = Rational

# constraints as (expr, bound) meaning expr < bound (strict) unless noted
# p2 < 4/15  [strict]
c_p2 = (p2, R(4,15), True)
# p3-p2 < -1/15 (g14<0) strict
c_g14 = (p3-p2, R(-1,15), True)
# -p1-p2-2p3 < -16/15 (g12<0) strict
c_g12 = (-p1-p2-2*p3, R(-16,15), True)
# p1-2p3 <0 (P1: R22.1.1 infeasible via p1<2p3) strict
c_P1 = (p1-2*p3, R(0), True)
# p1-p2-p3 <=0 (X: DSA/TP infeasible) non-strict
c_X = (p1-p2-p3, R(0), False)
# -p1-2p2 < -1 (P2: p2>p3+p4 i.e. p1+2p2>1) strict
c_P2 = (-p1-2*p2, R(-1), True)
# -p1+p2+p3 <0 (Y: DSA/TP feasible) strict
c_Y = (-p1+p2+p3, R(0), True)
# p1/2+p2 < 7/15 (g_R22<0, Q) strict
c_Q = (p1/2+p2, R(7,15), True)
# -p1+p2+p3 < -1/15 (g_DSA<0)
c_gDSA = (-p1+p2+p3, R(-1,15), True)
# p1<7/15 (g_TP<0)
c_gTP = (p1, R(7,15), True)
# p3-p2<=0 (sort order p3<=p2)
c_sort = (p3-p2, R(0), False)

def make(l): 
    return [(lhs-bound, F(0), w, strict) for (lhs,bound,strict),w in l]

# Branch (X,P1): p2<4/15 [5]; g14<0 [4]; g12<0 [1]; P1 [1]
check("(X,P1)", make([(c_p2,5),(c_g14,4),(c_g12,1),(c_P1,1)]))

# Branch (X,P2): p2<4/15 [4]; g14<0 [1]; X [1]; P2 [1]
check("(X,P2)", make([(c_p2,4),(c_g14,1),(c_X,1),(c_P2,1)]))

# Branch (X,Q): p2<4/15 [1/2]; g14<0 [1]; g12<0 [1/2]; Q [1]
check("(X,Q)", make([(c_p2,R(1,2)),(c_g14,1),(c_g12,R(1,2)),(c_Q,1)]))

# Branch (Y,P1): sort p3<=p2 [1]; Y feasible [1]; P1 [1]
check("(Y,P1)", make([(c_sort,1),(c_Y,1),(c_P1,1)]))

# Branch (Y,P2): p2<4/15 [2]; gTP<0 [1]; P2 [1]
check("(Y,P2)", make([(c_p2,2),(c_gTP,1),(c_P2,1)]))

# Branch (Y,Q): p2<4/15 [1]; g14<0[1]; g12<0[1]; gDSA<0[1]; gTP<0[2]
check("(Y,Q)", make([(c_p2,1),(c_g14,1),(c_g12,1),(c_gDSA,1),(c_gTP,2)]))

print("ALL 6 CERTIFICATES VERIFIED")
