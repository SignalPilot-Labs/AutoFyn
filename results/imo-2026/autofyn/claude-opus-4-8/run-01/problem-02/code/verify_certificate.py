"""Reproduce and check the (T)-reduction certificate for IMO 2026 P2 (Opus 4.8 run).

Rebuilds TN, P, Q via gb2_build.py, then verifies the exact identity

    lc(P,t) * lc(Q,s) * TN = f*P + g*Q   (modulo the Pythagorean relations)

by two one-step pseudo-divisions, and materializes the cofactors f and g,
which the original run asserted but never emitted.

Run: python3 verify_certificate.py
"""
import sympy as sp

cA, sA, cC, sC, cth, sth = sp.symbols('cA sA cC sC cth sth')
RHO = [sA**2 + cA**2 - 1, sC**2 + cC**2 - 1, sth**2 + cth**2 - 1]
PYTHAG_GENS = (sA, cA, sC, cC, sth, cth)
EXPECTED_DEG = 4
EXPECTED_R2_DEG = (3, 3)


def build() -> dict[str, sp.Expr]:
    """Construct TN, P, Q from the geometry (verbatim builder from the run)."""
    ns: dict[str, sp.Expr] = {}
    with open('gb2_build.py') as fh:
        exec(fh.read(), ns)
    return ns


def check() -> bool:
    """Verify the certificate and print the cofactors. Returns True if certified."""
    ns = build()
    TN, P, Q, t, s = ns['TN'], ns['P'], ns['Q'], ns['t'], ns['s']

    lcP = sp.Poly(P, t).LC()
    lcQ = sp.Poly(Q, s).LC()
    print(f"deg_t P = {sp.degree(sp.Poly(P, t))}, deg_s Q = {sp.degree(sp.Poly(Q, s))}")

    # Step 1: lc(P)*TN = f1*P + R1
    R1 = sp.expand(sp.prem(TN, P, t))
    f1, rem1 = sp.div(sp.expand(lcP * TN - R1), P, t)
    assert sp.expand(rem1) == 0, "identity (6.2) failed"

    # Step 2: lc(Q)*R1 = g*Q + R2
    R2 = sp.expand(sp.prem(R1, Q, s))
    g, rem2 = sp.div(sp.expand(lcQ * R1 - R2), Q, s)
    assert sp.expand(rem2) == 0, "identity (6.3) failed"
    assert (sp.degree(sp.Poly(R2, t)), sp.degree(sp.Poly(R2, s))) == EXPECTED_R2_DEG

    # R2 must vanish modulo the Pythagorean relations
    G = sp.groebner(RHO, *PYTHAG_GENS, order='grevlex')
    if not all(G.reduce(c)[1] == 0 for c in sp.Poly(R2, t, s).coeffs()):
        print("R2 does NOT reduce to 0 mod rho — certificate INVALID")
        return False

    # Combining: lc(P)*lc(Q)*TN = (lc(Q)*f1)*P + g*Q
    f = sp.expand(lcQ * f1)
    lhs = sp.expand(lcP * lcQ * TN)
    residual = sp.expand(lhs - sp.expand(f * P + g * Q))
    certified = all(G.reduce(c)[1] == 0 for c in sp.Poly(residual, t, s).coeffs()) \
        if residual != 0 else True

    print(f"f terms: {len(sp.Add.make_args(f))}, g terms: {len(sp.Add.make_args(g))}")
    print(f"certificate lc(P)*lc(Q)*TN = f*P + g*Q (mod rho): {certified}")
    with open('certificate_cofactors.txt', 'w') as fh:
        fh.write(f"f = {f}\n\ng = {g}\n")
    print("cofactors written to certificate_cofactors.txt")
    return certified


if __name__ == '__main__':
    raise SystemExit(0 if check() else 1)
