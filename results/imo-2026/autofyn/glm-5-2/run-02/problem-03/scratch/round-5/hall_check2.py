"""
Corrected Hall-matching conjecture check, EXACT rational arithmetic.
Level-(n+1) dyadic (param n), k = n+1 marks all in M.
SPLIT by whether m_1 >= a_1 (= M/2 = R_largest) or m_1 < a_1.

The pairing-partner conjecture as stated (s_1=a_1, then s_3+s_5+...<=a_2+...+a_{n+1})
only applies when m_1 >= a_1 (so m_1 is global rank 1, removed from the merge).
When m_1 < a_1, the setup differs: a_1 is global rank 1, and ALL of m_1..m_{n+2}
plus a_2..a_{n+1} form the "rest". We check A >= alpha directly in both branches.

Reports: violation counts and min A in each branch, for n=1..5.
"""
import random
from fractions import Fraction

def D(m): return (1 << (m+1)) - 1

def check(n, samples=300000, GRID=10**6):
    """n = parameter in conjecture; level = n+1. M = 2^{n+1}/D(n+1), R has n+1 pieces."""
    level = n+1
    dval = D(level)  # 2^{level+1}-1 = 2^{n+2}-1
    M = Fraction(2**level, dval)
    # R = (1, 2, ..., 2^{level-1})/dval, level pieces. Sorted DESC: a_1 = 2^{level-1}/D = M/2
    R_desc = [Fraction(2**(level-1-j), dval) for j in range(level)]  # [2^{level-1}, ..., 1]/D
    R = R_desc
    a1 = R[0]  # = 2^{level-1}/D = M/2
    total_R = sum(R)
    assert M - total_R == Fraction(1, dval), f"M-total_R={M-total_R}"
    assert a1 == M/2, f"a1={a1}, M/2={M/2}"
    target_A = Fraction(1, dval)
    # k = n+1 = level marks in M -> level+1 = n+2 sub-pieces
    n_marks = level
    # branch counters
    b1_total = b2_total = 0
    b1_Aviol = b2_Aviol = 0
    b1_minA = None; b2_minA = None
    b1_conj_viol = 0; b1_min_slack = None
    for _ in range(samples):
        # generate n_marks distinct integer cuts in (0, M*GRID)
        Mgrid = int(M * GRID)
        positions = sorted(random.sample(range(1, Mgrid), n_marks))
        cuts = [Fraction(p, GRID) for p in positions]
        mp = [cuts[0]] + [cuts[i]-cuts[i-1] for i in range(1,n_marks)] + [M - cuts[-1]]
        assert sum(mp) == M
        mp.sort(reverse=True)
        m1 = mp[0]
        merged = sorted(mp + R, reverse=True)
        A = Fraction(0)
        for i, v in enumerate(merged):
            if i % 2 == 0: A += v
            else: A -= v
        if m1 >= a1:
            b1_total += 1
            if A < target_A: b1_Aviol += 1
            if b1_minA is None or A < b1_minA: b1_minA = A
            # conjecture: merge {m_2..m_{n+2}} with R, s_1=a_1, s_3+...+s_{2n+1} <= a_2+...+a_{n+1}
            small = sorted(mp[1:], reverse=True)
            s = sorted(small + R, reverse=True)
            # s has (n+1) + (n+1) = 2n+2 pieces
            # odd indices (1-based) 3,5,...,2n+1 -> 0-based 2,4,...,2n
            odd_sum = sum(s[i] for i in range(2, 2*n+1, 2))
            rhs = sum(R[1:])  # a_2 + ... + a_{n+1}
            slack = rhs - odd_sum  # >= 0 if conjecture holds
            if slack < 0: b1_conj_viol += 1
            if b1_min_slack is None or slack < b1_min_slack: b1_min_slack = slack
        else:
            b2_total += 1
            if A < target_A: b2_Aviol += 1
            if b2_minA is None or A < b2_minA: b2_minA = A
    print(f"=== n={n} (level={level}, D={dval}, M={float(M):.4f}, a_1={float(a1):.4f}), samples={samples} ===")
    print(f"  branch 1 (m_1 >= a_1): {b1_total} configs ({100*b1_total/samples:.1f}%)")
    print(f"    A >= alpha violations: {b1_Aviol}, min A: {float(b1_minA) if b1_minA else 'n/a'}")
    print(f"    conjecture (s_3+..+s_2n+1 <= a_2+..+a_n+1) violations: {b1_conj_viol}")
    print(f"    min slack (rhs - odd_sum): {float(b1_min_slack) if b1_min_slack is not None else 'n/a'}")
    print(f"  branch 2 (m_1 < a_1): {b2_total} configs ({100*b2_total/samples:.1f}%)")
    print(f"    A >= alpha violations: {b2_Aviol}, min A: {float(b2_minA) if b2_minA else 'n/a'}")

if __name__ == "__main__":
    for n in [1,2,3,4,5]:
        check(n, samples=200000)
