"""
Verify the superincreasing-R Hall matching conjecture on rank indices
for the unrefined-R sub-case (k = n+1, all Xiang marks in M) at n=1..5.

Conjecture: for level-(n+1) dyadic with k = n+1 marks all in M
(M = 2^{n+1}/D(n+1), R = (1,2,4,...,2^n)/D(n+1) superincreasing),
let s_1 >= ... >= s_{2n+2} be sorted-desc merge of
  small M-sub-pieces {m_2,...,m_{n+2}} (sum sigma <= a_1 = M/2)
  with R-pieces {a_1=2^n/D, a_2=2^{n-1}/D, ..., a_{n+1}=1/D}.
Then s_1 = a_1, and
  s_3 + s_5 + ... + s_{2n+1}  <=  a_2 + a_3 + ... + a_{n+1}.

Also verify the FULL (Match): the full odd-position sum bound which is what
closes L(n+1): A = M - a_1 + (s_2+s_4+...+s_{2n+2}) - (s_3+s_5+...+s_{2n+1})
         = (M - a_1) + (sigma+total_R - a_1) - 2*(s_3+s_5+...)
... actually use direct A computation.
Target: A >= 1/D(n+1) = alpha(n+1).
"""
import random
from fractions import Fraction

def D(n): return (1 << (n+1)) - 1  # 2^{n+1} - 1

def check_n(n, samples=200000):
    """n here is the level index: level-(n+1) dyadic, so n+1 marks, M=2^{n+1}/D(n+1)."""
    d = D(n+1)  # using level = n+1
    # Actually let's be careful: 'n' in the conjecture is such that level = n+1.
    # Let n_param = n. level = n+1. D(level) = 2^{level+1}-1 = 2^{n+2}-1.
    # To match the pairing-partner notation: conjecture stated for level-(n+1) dyadic,
    # so let's parameterize by level = n+1 directly.
    pass

def check_level(L, samples=200000):
    """L = level of the dyadic (pieces (1,2,...,2^L)/D(L), D(L)=2^{L+1}-1).
    conjecture: with L marks all in M (so k = L = n+1 with n = L-1),
    M = 2^L / D(L), R = (1,2,...,2^L)/D(L) with L+1 pieces? No.
    Actually for level-(n+1) dyadic: pieces = (1,2,4,...,2^{n+1})/D(n+1), n+2 pieces.
    M = 2^{n+1}/D(n+1) (largest), R = (1,2,...,2^n)/D(n+1), n+1 pieces.
    Marks all in M: k = n+1 marks -> n+2 sub-pieces of M.
    Let n_param = n. So L = n+1, n = L-1, marks = L, R has L pieces (1,2,...,2^{L-1})/D(L) -- wait
    R = (1,2,...,2^n)/D(n+1) where n = L-1, so R = (1,2,...,2^{L-1})/D(L), L pieces.
    """
    dval = D(L)  # 2^{L+1} - 1
    # pieces of level-L dyadic: (1, 2, 4, ..., 2^L)/D(L), total L+1 pieces
    M = Fraction(2**L, dval)
    R = [Fraction(2**j, dval) for j in range(L)]  # 1, 2, ..., 2^{L-1}
    # R has L pieces, superincreasing
    # k = L marks all in M -> L+1 sub-pieces of M (m_1 >= ... >= m_{L+1})
    a1 = R[0]  # = 2^{L-1}/D(L) = M/2
    total_R = sum(R)
    assert M - total_R == Fraction(1, dval), f"M-total_R={M-total_R}, expected 1/{dval}"
    assert a1 == M/2
    target_A = Fraction(1, dval)
    # conjecture bound: sum of a_2..a_{L} (smaller R pieces) = total_R - a1
    bound_rhs = total_R - a1
    n_param = L - 1  # for labeling
    violations_match = 0
    violations_A = 0
    min_slack = None
    min_A = None
    for _ in range(samples):
        # generate L marks in (0, M) interior, distinct, sorted
        # easier: generate L+1 sub-pieces m_1>=...>=m_{L+1} summing to M
        # by drawing L cut points uniformly in (0,M), sort, take diffs
        cuts = sorted(random.uniform(0, float(M)) for _ in range(L))
        mp = [Fraction(cuts[0])] + [Fraction(cuts[i]-cuts[i-1]) for i in range(1,L)] + [Fraction(float(M)-cuts[-1])]
        # filter distinct cuts -> nonzero pieces (skip degenerate for cleanliness, but allow)
        if any(p <= 0 for p in mp):
            continue
        mp.sort(reverse=True)
        m1 = mp[0]
        if m1 < M/2:
            continue  # m1 must be largest; if not, re-sort: actually mp[0] is max
        # actually m1 >= M/2 is forced by m1 being max of L+1 pieces summing to M only when L+1>=2
        # but for L>=2 not necessarily; check anyway
        sigma = sum(mp[1:])
        if sigma > a1 + Fraction(1,1000000):  # tiny tolerance
            # m1 < M/2 means sigma > M/2 = a1; should not happen if m1 is the max
            # m1 is max so m1 >= M/(L+1) but not necessarily >= M/2
            # WAIT - the lemma uses m1>=M/2 because m1 is the LARGEST of (k+1) pieces summing to M,
            # so m1 >= M/(k+1). It is NOT >= M/2 unless k+1 = 2. So sigma can exceed a1.
            # Hmm. Let me re-read the superincreasing-R corollary.
            pass
        # the obstruction bound corollary says sigma <= M/2. That's FALSE if m1 < M/2.
        # But m1 IS the largest of k+1 pieces summing to M; m1 >= M/(k+1) not M/2.
        # The corollary "m1 >= M/2" is WRONG as stated!
        # Let me re-check: in the lemma-superincreasing-R.md, it says
        #   "m1 >= M/2 (largest of k+1 >= 2 pieces summing to M)"
        # That is FALSE: e.g. M=8, k+1=4 pieces (2,2,2,2), m1=2 < 4=M/2.
        # The claim m1 >= M/2 needs k+1 <= 2 i.e. k<=1.
        # So the obstruction bound sigma <= M/2 is FALSE for k>=2.
        # ... but wait: the obstruction bound is on sigma = sum of MM smaller halves, not all.
        # Actually the corollary says sigma = M - m1 <= M/2. This requires m1>=M/2. For k+1>=2 pieces
        # summing to M, m1 is just the max, m1>=M/(k+1), NOT m1>=M/2.
        # So the certified corollary has a BUG?? Let me check at n=2 (level-3).
        # Actually wait - let me re-read more carefully.
        pass
        # Compute the merged sort and A directly
        merged = sorted(mp + R, reverse=True)
        A = Fraction(0)
        for i, v in enumerate(merged):
            if i % 2 == 0:
                A += v
            else:
                A -= v
        if A < target_A:
            violations_A += 1
        # conjecture bound: s_3 + s_5 + ... + s_{2L+1} <= bound_rhs
        # (merged has 2L+1 pieces total: L+1 from M + L from R)
        # s_1 = a1 (since m1 <= ... wait, m1 may exceed a1!)
        # Hmm. Actually the conjecture is for "k = n+1 marks all in M" with level-(n+1),
        # and it claims s_1 = a_1. But m_1 can exceed a_1 = M/2 (if m_1 close to M).
        # That contradicts s_1 = a_1. So the conjecture as stated only works when m_1 <= a_1?
        # let me just compute the sum of odd-position pieces (excluding s_1)
        # actually conjecture: s_3+s_5+...+s_{2n+1} <= a_2+...+a_{n+1}
        # for level-(n+1), n+1 marks, merged has 2n+3 pieces? Let me recompute.
        # level-(n+1) dyadic: n+2 Liu pieces. M = 2^{n+1}/D(n+1), R = (1,...,2^n)/D(n+1) -> n+1 pieces.
        # k = n+1 marks in M -> n+2 sub-pieces of M. merged has n+2 + n+1 = 2n+3 pieces.
        # conjecture: s_3 + s_5 + ... + s_{2n+1} <= a_2 + ... + a_{n+1}
        # indices 3,5,...,2n+1 -> n terms. RHS has n terms (a_2..a_{n+1}).
        # 2n+3 pieces, last odd index is 2n+3. So conjecture sums odd indices 3..2n+1 (n terms),
        # SKIPPING the last odd index 2n+3. Interesting.
        n = L - 1
        odd_sum = sum(merged[i] for i in range(2, 2*n+1, 2))  # indices 3,5,...,2n+1 -> 0-based 2,4,...,2n
        slack = odd_sum - bound_rhs
        if slack > Fraction(1, 1000000):  # tolerance
            violations_match += 1
        if min_slack is None or slack < min_slack:
            min_slack = slack
        if min_A is None or A < min_A:
            min_A = A
    print(f"level L={L} (n={L-1}, D={dval}, samples~{samples}):")
    print(f"  conjecture (s_3+...+s_{{2n+1}}) <= (a_2+...+a_{{n+1}})={bound_rhs}: violations={violations_match}")
    print(f"  min slack = {min_slack}")
    print(f"  full L(n+1) target A>={target_A}: violations_A={violations_A}, min_A={min_A}")

if __name__ == "__main__":
    for L in [2, 3, 4, 5]:
        check_level(L, samples=200000)
