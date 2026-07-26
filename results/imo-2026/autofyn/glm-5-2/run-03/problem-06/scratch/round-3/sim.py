"""Simulator for the gcd-greedy sequence a_{n+1} = smallest m > a_n with gcd(m, a_i)>1 for all i<=n."""

from sympy import factorint, isprime, primefactors

def greedy_seq(a1, N):
    """Return [a_1, ..., a_N]."""
    seq = [a1]
    # Track product of all prior terms for coprimality check? Better: track lcm of each term's
    # radical? Actually simplest: gcd(m, prod) > 1 means m shares a prime with SOME prior term,
    # not ALL. We need shares with EACH. Use radical-set: the constraint is that for each i<=n,
    # gcd(m, a_i) > 1, i.e., S(m) ∩ S(a_i) != empty.
    # Equivalent: m's prime support must intersect each prior support.
    # Maintain list of supports. To test admissibility of m: factor m, check S(m) hits each support.
    supports = [set(primefactors(a1))]
    for n in range(N - 1):
        an = seq[-1]
        m = an + 1
        while True:
            # factor m once
            sm = set(primefactors(m))
            ok = all(sm & s for s in supports)
            if ok:
                break
            m += 1
        seq.append(m)
        supports.append(set(primefactors(m)))
    return seq

def detect_period(seq, min_repeats=2):
    """Detect (T, L, start) with a_{n+T} = a_n + L for ALL n in [start, start + min_repeats*T].
    i.e. a window of length min_repeats*T+1 consecutive matches starting at start."""
    N = len(seq)
    for start in range(N):
        # window must contain (min_repeats+1)*T positions: indices [start, start+T, ..., start+min_repeats*T]
        maxT = (N - start - 1) // min_repeats
        for T in range(1, maxT + 1):
            L = seq[start + T] - seq[start]
            if L <= 0:
                continue
            ok = True
            for k in range(1, min_repeats * T + 1):
                if start + T + k >= N:
                    ok = False
                    break
                if seq[start + T + k] - seq[start + k] != L:
                    ok = False
                    break
            if ok:
                return (T, L, start)
    return None

if __name__ == "__main__":
    import sys
    a1 = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    seq = greedy_seq(a1, N)
    print(f"a1={a1}, first 20 terms:", seq[:20])
    per = detect_period(seq)
    if per:
        T, L, s = per
        print(f"  Period: T={T}, L={L}, starts at index n>={s+1}")
        # verify
        bad = [k for k in range(s, N - T) if seq[k + T] - seq[k] != L]
        print(f"  verify: {len(bad)} violations out of {N - T - s} checks")
    else:
        print("  No period detected within", N, "terms")
    # show supports, distinct primes
    from collections import Counter
    allp = Counter()
    for s in [set(primefactors(x)) for x in seq]:
        for p in s:
            allp[p] += 1
    print(f"  distinct primes appearing: {len(allp)}; top: {sorted(allp.most_common(15))}")
    print(f"  P1={sorted(primefactors(a1))}, M1={sum(p for p in primefactors(a1))} (sum) / prod=", end="")
    M = 1
    for p in primefactors(a1): M *= p
    print(M)
