"""
Check the certified superincreasing-R lemma's corollary:
  "m_1 >= M/2 (largest of k+1 >= 2 pieces summing to M)"
  => sigma = M - m_1 <= M/2 = a_1.
This claim is TRUE only when k+1 = 2 (k=1). For k >= 2 (k+1 >= 3 sub-pieces),
m_1 is just the max, so m_1 >= M/(k+1), NOT m_1 >= M/2.

Test: level-3 dyadic, k=3 marks in M=8, R=(4,2,1).
Find configurations where sigma > 4 = M/2 = a_1 (contradicting the corollary),
and check whether A >= 1 still holds (conjecture) AND whether the
L(3) unrefined-R proof's formula A = 7 - 2(s_3+s_5) (derived assuming m_1 = global rank 1)
is even applicable.

The proof treats m_1 separately and merges {m_2,m_3,m_4} with R = {4,2,1}.
Formula A = m_1 - s_1 + s_2 - s_3 + s_4 - s_5 + s_6 requires m_1 = global rank 1
i.e. m_1 >= a_1 = 4 = M/2.
"""
import random
from fractions import Fraction

def test():
    # level-3: M=8, R=(4,2,1), stick total 15, alpha=1/15 (target A_int >= 1)
    M_int = 8
    R_int = [4, 2, 1]
    a1 = 4
    target_A = 1
    samples = 500000
    sigma_violations = 0  # sigma > M/2 = a1 (contradicts corollary)
    formula_violations = 0  # m_1 < a1 (formula A = m_1 - ... inapplicable)
    A_violations = 0  # actual A < 1
    min_A = None
    formula_min_diff = None  # |actual A - formula A|
    formula_examples = []
    for _ in range(samples):
        # generate 3 marks in (0, 8), distinct
        cuts = sorted(random.uniform(0, 8) for _ in range(3))
        mp = [cuts[0]] + [cuts[i]-cuts[i-1] for i in range(1,3)] + [8 - cuts[-1]]
        mp = [Fraction(x).limit_denominator(10**9) for x in mp]
        if any(p <= 0 for p in mp):
            continue
        mp.sort(reverse=True)
        m1 = mp[0]
        sigma = sum(mp[1:])
        # check corollary
        if sigma > a1:
            sigma_violations += 1
        # check formula applicability
        formula_applicable = (m1 >= a1)
        if not formula_applicable:
            formula_violations += 1
        # compute actual A (merged sort of all 7 pieces)
        merged = sorted(mp + R_int, reverse=True)
        A = Fraction(0)
        for i, v in enumerate(merged):
            if i % 2 == 0:
                A += v
            else:
                A -= v
        if A < target_A:
            A_violations += 1
            if A_violations <= 5:
                print(f"  A VIOLATION: A={A}, m={mp}, merged={merged}")
        if min_A is None or A < min_A:
            min_A = A
        # check formula's predicted A
        if formula_applicable and m1 == max(merged):
            # formula: merge {m_2,m_3,m_4} with R, s = sorted desc (6 pieces)
            small = sorted(mp[1:], reverse=True)
            s = sorted(small + R_int, reverse=True)
            # s_1 should = a1 if m1>=a1
            # formula A_formula = m1 - s[0] + s[1] - s[2] + s[3] - s[4] + s[5]
            A_formula = m1 - s[0] + s[1] - s[2] + s[3] - s[4] + s[5]
            # the proof's closed form: 7 - 2*(s[2]+s[4])  (s_3+s_5 = s[2]+s[4] in 0-based)
            A_closed = 7 - 2*(s[2]+s[4])
            if A_formula != A_closed and len(formula_examples) < 3:
                formula_examples.append((mp, s, A_formula, A_closed))
            if A_formula != A and len(formula_examples) < 5:
                formula_examples.append((mp, s, A_formula, A, "MISMATCH"))
    print(f"=== level-3 unrefined-R sub-case (k=3 marks in M=8), samples={samples} ===")
    print(f"  corollary sigma <= a1=4 violations: {sigma_violations} (FALSE corollary)")
    print(f"  formula inapplicable (m1 < a1=4): {formula_violations}")
    print(f"  actual A >= 1 violations: {A_violations}")
    print(f"  min actual A: {min_A}")
    print(f"  formula example mismatches: {formula_examples[:3]}")

if __name__ == "__main__":
    test()
