# Orbit Formula for Affine Functional Equations

**Statement:** If f: R+ -> R+ satisfies f(f(y)) = 2f(y) - y for all y > 0, then defining g = f - id:
1. g(f(y)) = g(y) for all y > 0 (orbit invariance)
2. f^n(y) = y + n * g(y) for all y > 0 and n >= 0 (orbit formula)

**Proof:**

Part 1: g(f(y)) = f(f(y)) - f(y) = (2f(y) - y) - f(y) = f(y) - y = g(y).

Part 2: By induction on n.
- Base case n = 0: f^0(y) = y = y + 0 * g(y).
- Inductive step: f^{k+1}(y) = f(f^k(y)) = f^k(y) + g(f^k(y)) = (y + kg(y)) + g(y) = y + (k+1)g(y).

**Source:** orbit-invariance approach for IMO 2026 P5.

**Certification:** Proof-reviewed and certified Round 2.
