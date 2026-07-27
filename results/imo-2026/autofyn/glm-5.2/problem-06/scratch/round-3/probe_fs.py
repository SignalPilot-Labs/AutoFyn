"""
Finite-state lens probe for IMO 2026 P6.

Questions:
  Q1. Is the gap a_{n+1}-a_n unconditionally bounded by G(a1) across ALL seeds?
        Track max_gap vs a1.
  Q2. Is mtp(M_n) bounded by a function of a1 (mtp_final vs a1)? What function?
        Is mtp_final <= a1? <= pmax(a1)^2? Extremal seeds.
  Q3. Does a_n mod rad(a1) (or mod small M) stabilize BEFORE M stabilizes?
        Track residue evolution.
  Q4. Is there a seed where the gap GROWS unboundedly (no finite-state win)?
        Search products of 2/3 primes with various spacings.

Correct transversal enumeration: full 2^|Pess| subset check (NOT min-cardinality).
Verify fast method vs brute force on 3 small seeds first.
"""
import math, sys
from itertools import combinations

def spf_table(N):
    spf = list(range(N+1))
    for i in range(2, int(N**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, N+1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def factor(m, spf):
    s = set()
    while m > 1:
        p = spf[m]
        s.add(p)
        while m % p == 0:
            m //= p
    return frozenset(s)

def minimal_family_inc(old_M, new_P):
    """old_M: list of frozensets (current minimals). new_P: frozenset.
    Return new minimal family after adding new_P."""
    new_M = []
    is_new_min = True
    for S in old_M:
        if new_P < S:  # new_P proper subset of S -> S removed
            continue
        if S < new_P or S == new_P:  # S subset of new_P -> new_P not minimal
            is_new_min = False
            new_M.append(S)
            continue
        new_M.append(S)
    if is_new_min and not any(S == new_P for S in new_M):
        new_M.append(new_P)
    return new_M

def all_transversals(Pess_list, M):
    """Full subset enumeration of transversals of M using primes in Pess_list."""
    n = len(Pess_list)
    res = []
    for k in range(1, n+1):
        for combo in combinations(range(n), k):
            T = frozenset(Pess_list[i] for i in combo)
            if all(T & Mm for Mm in M):
                res.append(T)
    return res

def mtp_of(Pess_list, M):
    best = None
    n = len(Pess_list)
    for k in range(1, n+1):
        for combo in combinations(range(n), k):
            T = frozenset(Pess_list[i] for i in combo)
            if all(T & Mm for Mm in M):
                prod = 1
                for p in T: prod *= p
                if best is None or prod < best:
                    best = prod
        if best is not None and k >= 1:
            pass
    return best

def common(M):
    if not M: return set()
    c = set(M[0])
    for s in M[1:]: c &= s
    return c

def run(a1, Nmax, spf, track_residues=False, rad_a1=None, stable_window=300):
    """Greedy with incremental M tracking and mtp gap bound for candidate search."""
    a = [a1]
    P1 = factor(a1, spf)
    M = [P1]
    Pess = set(P1)
    gaps = []
    mtp_trace = []
    Pess_size_trace = []
    common_trace = []
    entering_log = []
    entering_total = set()
    promo_steps = []
    M_repr = tuple(sorted([tuple(sorted(s)) for s in M]))
    last_repr = M_repr
    stable = 0
    residue_traces = {rad_a1: []} if (track_residues and rad_a1) else {}
    residue_traces[2] = []
    residue_traces[6] = []
    residue_traces[30] = []
    mtp_cached = None
    for n in range(1, Nmax):
        an = a[-1]
        # compute mtp (only recompute when M changed)
        if mtp_cached is None:
            Pess_list = sorted(Pess)
            mtp_cached = mtp_of(Pess_list, M)
        mtp = mtp_cached
        mtp_trace.append(mtp)
        Pess_size_trace.append(len(Pess))
        common_trace.append(sorted(common(M)))
        # record residues
        for mod in residue_traces:
            residue_traces[mod].append(an % mod)
        # candidate search bounded by an + mtp
        m = an + 1
        bound = an + (mtp if mtp else an)
        while m <= bound:
            Pm = factor(m, spf)
            if all(Pm & Mm for Mm in M):
                break
            m += 1
        a.append(m)
        gaps.append(m - an)
        # update M
        new_P = factor(m, spf)
        new_M = minimal_family_inc(M, new_P)
        if set(new_M) != set(M):
            # promotion occurred
            promo_steps.append(n)
            entered = set(new_P) - Pess
            if entered:
                entering_log.append((n, frozenset(new_P), frozenset(entered)))
                entering_total |= entered
            Pess = set()
            for S in new_M: Pess |= set(S)
            mtp_cached = None  # invalidate
        M = new_M
        reprM = tuple(sorted([tuple(sorted(s)) for s in M]))
        if reprM == last_repr:
            stable += 1
        else:
            stable = 0; last_repr = reprM
        if stable >= stable_window:
            break
    return {
        'a1': a1, 'a': a, 'gaps': gaps, 'M_final': M,
        'Pess_final': set().union(*M) if M else set(),
        'entering_log': entering_log, 'entering_total': entering_total,
        'C_final': common(M), 'n_terms': len(a),
        'mtp_trace': mtp_trace, 'promo_steps': promo_steps,
        'residue_traces': residue_traces,
    }

def brute(a1, Nmax, spf):
    a = [a1]
    for _ in range(Nmax-1):
        an = a[-1]
        m = an+1
        while True:
            if all(math.gcd(m, x) > 1 for x in a):
                break
            m += 1
        a.append(m)
    return a

if __name__ == '__main__':
    N = 2000000
    spf = spf_table(N)
    # VERIFY fast vs brute on 3 small seeds
    print("=== VERIFY fast vs brute ===")
    for a1 in [15, 21, 105]:
        r = run(a1, 60, spf)
        b = brute(a1, 60, spf)
        print(f"a1={a1}: fast==brrite? {r['a']==b}")
        if r['a'] != b:
            print(" fast:", r['a'][:25])
            print(" brute:", b[:25])
