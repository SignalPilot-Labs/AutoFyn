"""
Round-6 verification for the pairing-partner direct sum-level Hall injection.

Conjecture (H1 + H2 + general e_M <= o_R): for the level-(n+1) [here: level-N]
dyadic config, for every real Xiang response (<= N marks), the merged-sort
inequality  e_M <= o_R  holds, where
  e_M = sum of M-sub-pieces at global EVEN ranks,
  o_R = sum of R'-pieces at global ODD ranks.
Equivalence L(n+1) <=> e_M <= o_R is CERTIFIED (lemma-em-or-reduction).

We verify three things with exact-rational arithmetic (fractions.Fraction):

(A) GENERAL  e_M <= o_R  for arbitrary Xiang play (any k), N = 2..6.
    Record min slack (o_R - e_M) in units of alpha(N) = 1/D(N).  The explorer
    signature is: slack GROWS with N  (0, 0, ~0.10, ~0.64, ~1.15 at N=3..7).

(B) UNREFINED-R  (k = N, all marks in M, R' = R intact, superincreasing).
    Branch 1 (m_1 >= a_1): verify (H1)  s_3 + s_5 + ... + s_{2N-1} <= total(R)-a_1.
    Branch 2 (m_1 <  a_1): verify (H2)  oddsum(rest) <= total(R).
    Both in units of alpha(N).

(C) Branch-population census: fraction of unrefined-R configs in Branch 1 vs 2.

All computations exact (Fraction).  No floats anywhere.
"""

import random
from fractions import Fraction

def D(N):
    return (1 << (N + 1)) - 1   # 2^{N+1} - 1  (Mersenne)

def liu_marks(N):
    # Liu marks at cumulative sums of (1,2,4,...,2^N)/D(N): mark j at (2^j-1)/D(N), j=1..N
    d = D(N)
    return [Fraction((1 << j) - 1, d) for j in range(1, N + 1)]

def dyadic_pieces(N):
    # pieces (1,2,4,...,2^N)/D(N), N+1 pieces
    d = D(N)
    return [Fraction(1 << i, d) for i in range(N + 1)]   # i=0..N  => 1,2,...,2^N

def M_interval(N):
    # M is the largest piece 2^N/D(N); it is the LAST interval [ (2^N - 1)/D(N), 1 ]
    d = D(N)
    left = Fraction((1 << N) - 1, d)
    return (left, Fraction(1, 1))

def random_marks(N, rng, tries=50):
    # generate N distinct marks in (0,1) not equal to any Liu mark; exact rational
    liu = set(liu_marks(N))
    out = set()
    while len(out) < N:
        # random rational with small numerator/denominator for exactness & speed
        num = rng.randint(1, 9999)
        den = rng.randint(num + 1, 10000)   # ensure < 1
        x = Fraction(num, den)
        if x in liu or x in out or x <= 0 or x >= 1:
            continue
        out.add(x)
    return sorted(out)

def partition_with_origins(N, xiang_marks):
    # Combine Liu + Xiang marks, sort, take diffs; label each piece by 'M' or 'R'.
    lmarks = liu_marks(N)
    all_marks = sorted(set(lmarks) | set(xiang_marks))
    pts = [Fraction(0)] + all_marks + [Fraction(1)]
    m_left, m_right = M_interval(N)
    pieces = []   # (length, origin)
    for i in range(len(pts) - 1):
        L = pts[i + 1] - pts[i]
        if L <= 0:
            continue
        mid = (pts[i] + pts[i + 1]) / 2
        if m_left < mid < m_right:
            origin = 'M'
        elif mid <= m_left or mid >= m_right:
            origin = 'R'
        else:
            origin = 'R'   # boundary
        pieces.append((L, origin))
    return pieces

def merged_sort_eM_oR(N, xiang_marks):
    pieces = partition_with_origins(N, xiang_marks)
    # sort desc by length; stable on origin doesn't matter for sums
    pieces.sort(key=lambda t: t[0], reverse=True)
    eM = Fraction(0); oR = Fraction(0)
    for idx, (L, org) in enumerate(pieces):
        rank = idx + 1
        if rank % 2 == 0:  # even rank
            if org == 'M':
                eM += L
        else:              # odd rank
            if org == 'R':
                oR += L
    return eM, oR

def unrefined_R_branches(N, msubs):
    # msubs: sorted desc list of N+1 M-sub-pieces summing to M = 2^N/D(N).
    # R intact = (1,2,...,2^{N-1})/D(N) = pieces a_1=2^{N-1}/D, ..., a_N=1/D
    d = D(N)
    R = [Fraction(1 << (N - 1 - i), d) for i in range(N)]  # a_1..a_N
    a1 = R[0]
    M = Fraction(1 << N, d)
    totalR = sum(R)
    alpha = Fraction(1, d)
    m1 = msubs[0]
    branch1 = (m1 >= a1)
    if branch1:
        # Branch 1: m_1 is rank 1. Rest = {m_2..m_{N+1}} U R, 2N pieces.
        rest = sorted(msubs[1:] + R, reverse=True)
        # s_1..s_{2N}; s_1 should be a_1. odd-position sum (excl s_1) <= total(R)-a_1
        # (H1): s_3+s_5+...+s_{2N-1} <= totalR - a1
        lhs = sum(rest[i] for i in range(2, 2 * N, 2))   # indices 2,4,...,2N-2 => s_3,s_5,...
        rhs = totalR - a1
        H1_ok = lhs <= rhs
        # equivalent: A >= alpha.  A = M + totalR - 2*(s_1+s_3+...)
        O = sum(rest[i] for i in range(0, 2 * N, 2))  # s_1,s_3,...,s_{2N-1}
        A = m1 + (sum(rest) ) - 2 * O   # = M + totalR - 2*O  since m1+sum(rest)= M+totalR
        return branch1, (H1_ok, lhs, rhs, A, alpha)
    else:
        # Branch 2: a_1 is rank 1. Rest = {m_1..m_{N+1}} U {a_2..a_N}, 2N pieces.
        rest = sorted(msubs + R[1:], reverse=True)
        # (H2): oddsum(rest) <= totalR
        oddsum = sum(rest[i] for i in range(0, 2 * N, 2))  # rest positions 0,2,... = ranks 2,4,...
        # wait: rest occupies ranks 2..2N+1; oddsum(rest) = pieces at global ODD ranks = positions 1,3,.. (0-indexed 0,2,...)
        H2_ok = oddsum <= totalR
        A = a1 - (sum(rest[0:2*N:2]) - sum(rest[1:2*N:2]))  # a1 - A_rest; A_rest = odd-even of rest
        return branch1, (H2_ok, oddsum, totalR, A, alpha)

def random_msplit(N, rng):
    # split M = 2^N/D(N) into N+1 sub-pieces (exact rational), sorted desc
    d = D(N)
    M = Fraction(1 << N, d)
    # generate N cut points in (0, M), distinct, rational
    cuts = set()
    while len(cuts) < N:
        num = rng.randint(1, (1 << N) * 1000 - 1)
        x = Fraction(num, 1000 * d)   # rational in (0, M) roughly
        if x <= 0 or x >= M or x in cuts:
            continue
        cuts.add(x)
    cuts = sorted(cuts)
    pts = [Fraction(0)] + cuts + [M]
    subs = sorted((pts[i + 1] - pts[i] for i in range(len(pts) - 1)), reverse=True)
    return subs

def main():
    rng = random.Random(12345)
    print("=== (A) GENERAL e_M <= o_R, arbitrary Xiang play (exact rational) ===")
    for N in range(2, 7):
        d = D(N)
        alpha = Fraction(1, d)
        nbad = 0
        minslack = None
        nsamp = 30000 if N <= 5 else 12000
        for _ in range(nsamp):
            xm = random_marks(N, rng)
            eM, oR = merged_sort_eM_oR(N, xm)
            slack = oR - eM
            if slack < 0:
                nbad += 1
                if minslack is None or slack < minslack:
                    minslack = slack
            else:
                if minslack is None or slack < minslack:
                    minslack = slack
        # report slack in units of alpha
        if minslack is not None:
            slack_units = minslack / alpha
        else:
            slack_units = None
        print(f"  N={N} (c({N}), D={d}, alpha=1/{d}): samples={nsamp}, violations={nbad}, "
              f"min slack (o_R-e_M) = {minslack} = {float(minslack):.6f} = {float(slack_units):.4f} * alpha")

    print()
    print("=== (B) UNREFINED-R (k=N, all marks in M, R intact), Branch 1 & 2 ===")
    for N in range(2, 7):
        d = D(N)
        alpha = Fraction(1, d)
        b1_bad = 0; b2_bad = 0
        b1_minA = None; b2_minA = None
        b1_cnt = 0; b2_cnt = 0
        nsamp = 40000 if N <= 5 else 15000
        for _ in range(nsamp):
            subs = random_msplit(N, rng)
            is_b1, res = unrefined_R_branches(N, subs)
            ok, lhs, rhs, A, al = res
            if is_b1:
                b1_cnt += 1
                if not ok:
                    b1_bad += 1
                if b1_minA is None or A < b1_minA:
                    b1_minA = A
            else:
                b2_cnt += 1
                if not ok:
                    b2_bad += 1
                if b2_minA is None or A < b2_minA:
                    b2_minA = A
        b1_minA_u = (b1_minA / alpha) if b1_minA is not None else None
        b2_minA_u = (b2_minA / alpha) if b2_minA is not None else None
        print(f"  N={N}: samples={nsamp}, B1={b1_cnt} (bad={b1_bad}, min A={float(b1_minA):.6f}={float(b1_minA_u):.3f}*alpha), "
              f"B2={b2_cnt} (bad={b2_bad}, min A={float(b2_minA):.6f}={float(b2_minA_u):.3f}*alpha)")

    print()
    print("=== (C) sanity: staircase equality config for unrefined-R, Branch 1 ===")
    # staircase: m_1=a_1, m_2=a_2, ..., m_{N+1}=a_N  => all b's at even positions, e_M=o_R=0
    for N in range(2, 7):
        d = D(N)
        a = [Fraction(1 << (N - 1 - i), d) for i in range(N)]  # a_1..a_N
        subs = sorted([a[0]] + list(a), reverse=True)  # m_1=a_1, m_2..m_{N+1}=a_1..a_N
        # actually staircase: m_1=a_1, then m_2=a_2? need sum = M = 2*a_1.
        # a_1+ a_1 + a_2 + ... ?  M = 2^N/d, a_1 = 2^{N-1}/d = M/2. sum of a's = (2^N-1)/d = (M*d - 1)/d? sum a_i = (2^N-1)/d.
        # m_1 + m_2+...+m_{N+1} = M. if m_1 = a_1 = M/2, rest sum = M/2 = a_1.
        # rest = a_1 = a_2+...+a_N + a_1 - (a_2+..+a_N)? sum a_2..a_N = a_1 - alpha. so to get a_1 we add alpha.
        # staircase equality: {m_2..m_{N+1}} = {a_2,...,a_N, alpha}? but alpha=1/d = a_N. so {a_2,...,a_N,a_N}? a_N appears twice?
        # Known n=3 equality: {m_2,m_3,m_4}={2,1,1}/15 = {a_2, a_3, a_3}. so pattern: {a_2,a_3,...,a_N,a_N}.
        rest = list(a[1:]) + [a[-1]]   # a_2..a_N, then a_N again
        subs = sorted([a[0]] + rest, reverse=True)
        is_b1, res = unrefined_R_branches(N, subs)
        ok, lhs, rhs, A, al = res
        print(f"  N={N} staircase: branch1={is_b1}, (H) ok={ok}, A={A} = {float(A/al):.3f}*alpha (expect 1.000)")

if __name__ == "__main__":
    main()
