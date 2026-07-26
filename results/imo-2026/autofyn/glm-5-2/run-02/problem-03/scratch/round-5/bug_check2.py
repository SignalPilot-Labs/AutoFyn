"""
Redo the bug check with EXACT rational arithmetic (integer grid cuts),
so sum of m_i = M_int = 8 exactly.
"""
import random
from fractions import Fraction

def test():
    M_int = 8
    R_int = [4, 2, 1]
    a1 = 4
    target_A = 1  # alpha(3)*D(3) = 1/15 * 15
    samples = 2000000
    GRID = 10**6  # cuts at integer multiples of 1/GRID
    sigma_violations = 0
    formula_violations = 0
    A_violations = 0
    A_violation_examples = []
    min_A = None
    for _ in range(samples):
        # 3 distinct integer cut positions in (0, 8*GRID)
        positions = sorted(random.sample(range(1, 8*GRID), 3))
        cuts = [Fraction(p, GRID) for p in positions]
        mp = [cuts[0]] + [cuts[i]-cuts[i-1] for i in range(1,3)] + [Fraction(8) - cuts[-1]]
        # all positive, sum = 8 exactly
        assert sum(mp) == 8
        mp.sort(reverse=True)
        m1 = mp[0]
        sigma = sum(mp[1:])
        if sigma > a1:
            sigma_violations += 1
        if m1 < a1:
            formula_violations += 1
        merged = sorted(mp + R_int, reverse=True)
        A = Fraction(0)
        for i, v in enumerate(merged):
            if i % 2 == 0:
                A += v
            else:
                A -= v
        if A < target_A:
            A_violations += 1
            if len(A_violation_examples) < 5:
                A_violation_examples.append((mp, merged, A))
        if min_A is None or A < min_A:
            min_A = A
    print(f"=== level-3 unrefined-R (k=3 in M=8), EXACT, samples={samples} ===")
    print(f"  corollary 'sigma <= a1=4' violations: {sigma_violations}")
    print(f"  formula inapplicable (m1 < a1=4): {formula_violations}")
    print(f"  actual A >= 1 violations: {A_violations}")
    print(f"  min actual A: {min_A} = {float(min_A):.6f}")
    print(f"  examples:")
    for mp, merged, A in A_violation_examples:
        print(f"    m={[float(x) for x in mp]}, merged={[float(x) for x in merged]}, A={float(A):.6f}")

if __name__ == "__main__":
    test()
