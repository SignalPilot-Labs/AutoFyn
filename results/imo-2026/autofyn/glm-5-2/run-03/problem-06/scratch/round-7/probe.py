"""Round-7 outline-reviewer probes:
1. D_n-window forward-determinism for a_1 in {15, 35, 77, 91, 175, 847}.
   - For each k, check if (D_{n-k+1},...,D_n) determines d_{n+1}.
2. Hole-set / skeleton-closure sanity for a_1=375 (the refutation witness).
   - Verify governing set = {2,3,5,7,19}, L=3990, T=852.
"""
import math
from collections import defaultdict


def prime_factors(x, primes):
    fs = set()
    y = x
    for p in primes:
        if p * p > y:
            break
        if y % p == 0:
            fs.add(p)
            while y % p == 0:
                y //= p
    if y > 1:
        fs.add(y)
    return fs


def sieve(limit):
    s = bytearray([1]) * (limit + 1)
    s[0] = s[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, limit + 1, i):
                s[j] = 0
    return [i for i in range(2, limit + 1) if s[i]]


def naive_greedy(a1, N, primes):
    """O(N^2) gcd-greedy. Returns list a[0..N-1] and d[0..N-2]."""
    a = [a1]
    for n in range(N - 1):
        m = a[n] + 1
        while True:
            ok = True
            for ai in a:
                if math.gcd(m, ai) == 1:
                    ok = False
                    break
            if ok:
                break
            m += 1
        a.append(m)
    d = [a[i + 1] - a[i] for i in range(len(a) - 1)]
    return a, d


def compute_Dn(a, n, M1, primes):
    """D_n = {d in [1,M1] : gcd(a[n]+d, a_i)>1 for all i<=n}."""
    an = a[n]
    Dn = []
    for d in range(1, M1 + 1):
        m = an + d
        ok = True
        for ai in a[:n + 1]:
            if math.gcd(m, ai) == 1:
                ok = False
                break
        if ok:
            Dn.append(d)
    return frozenset(Dn)


def find_period(d):
    """Find minimal period T of d (periodic tail)."""
    N = len(d)
    for T in range(1, N // 2):
        ok = True
        for i in range(N - T):
            if d[i] != d[i + T]:
                ok = False
                break
        if ok:
            # verify it's actually periodic for a long stretch
            tail_ok = all(d[i] == d[i + T] for i in range(N - 2 * T, N - T))
            if tail_ok:
                return T
    return None


def dn_window_fwd_det(a, d, M1, primes, N_check, kmax=8):
    """For each k in 1..kmax, check if (D_{n-k+1},...,D_n) determines d_{n+1}.
    Returns dict k -> (forward_deterministic: bool, realized_states, conflict_states)."""
    # Compute D_n for n in [0, N_check)
    Ds = {}
    for n in range(0, N_check):
        Ds[n] = compute_Dn(a, n, M1, primes)

    results = {}
    for k in range(1, kmax + 1):
        # state at step n (need n>=k-1): sigma_n = (D_{n-k+1},...,D_n)
        # CHECK: does sigma_n determine d_{n+1}? d_{n+1} = d[n+1] = a[n+2]-a[n+1] = min D_{n+1}.
        # (NOT d_n = min D_n, which is tautologically determined by D_n.)
        state_to_dnext = defaultdict(list)
        realized = 0
        conflict = 0
        for n in range(k - 1, N_check - 2):
            state = tuple(Ds[n - j] for j in range(k - 1, -1, -1))  # (D_{n-k+1},...,D_n)
            dnext = d[n + 1]  # the NEXT increment d_{n+1}
            if dnext in state_to_dnext[state]:
                pass
            elif state_to_dnext[state]:
                conflict += 1
                state_to_dnext[state].append(dnext)
            else:
                state_to_dnext[state].append(dnext)
            realized = len(state_to_dnext)
        results[k] = {
            "fwd_det": conflict == 0,
            "realized_states": realized,
            "conflict_states": conflict,
        }
    return results


def test_a1(a1, N, label=""):
    primes = sieve(int(a1 ** 0.5) + 50)
    # need primes up to sqrt(max a) ~ sqrt(a1 + N*M1). M1=rad(a1).
    a, d = naive_greedy(a1, N, primes)
    # compute M1 = rad(a1)
    M1 = 1
    x = a1
    for p in primes:
        if x % p == 0:
            M1 *= p
            while x % p == 0:
                x //= p
    if x > 1:
        M1 *= x
    T = find_period(d)
    print(f"=== a1={a1} (M1={M1}, T={T}, label={label}) ===")
    # check gap bound d_n <= M1
    maxd = max(d)
    print(f"  max d = {maxd}, M1 = {M1}, gap bound holds: {maxd <= M1}")
    res = dn_window_fwd_det(a, d, M1, primes, N_check=min(N - 1, 200), kmax=6)
    for k in range(1, 7):
        r = res[k]
        print(f"  k={k}: fwd_det={r['fwd_det']}, realized={r['realized_states']}, conflicts={r['conflict_states']}")


# Small cases for D_n-window forward-determinism
for a1, N in [(15, 200), (35, 400), (77, 200), (91, 300), (175, 1500), (847, 5000)]:
    test_a1(a1, N)
