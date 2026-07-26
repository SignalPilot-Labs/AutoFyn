"""Round-7 proof-reviewer independent verification.

Reproduce the load-bearing computational claims of the three approaches using
the NAIVE O(N^2) gcd-greedy (gold standard; NEVER /tmp/round-4/fast_greedy.py).
"""
import math
from collections import defaultdict


def prime_set(x):
    fs = set()
    y = x
    d = 2
    while d * d <= y:
        if y % d == 0:
            fs.add(d)
            while y % d == 0:
                y //= d
        d += 1
    if y > 1:
        fs.add(y)
    return fs


def rad(a1):
    return 1
    r = 1
    for p in prime_set(a1):
        r *= p
    return r


def naive_greedy(a1, N):
    """Gold-standard O(N^2) gcd-greedy. Returns list a[0..N-1]."""
    a = [0] * N
    a[0] = a1
    M1 = 1
    for p in prime_set(a1):
        M1 *= p
    for step in range(1, N):
        prev = a[step - 1]
        m = prev + 1
        while True:
            ok = True
            for i in range(step):
                if math.gcd(m, a[i]) == 1:
                    ok = False
                    break
            if ok:
                break
            m += 1
        a[step] = m
    return a


def Dn(a, n, M1):
    """Admissible-increment set at step n: {d in 1..M1 : gcd(a_n+d, a_i)>1 for all i<=n}."""
    an = a[n]
    out = []
    for d in range(1, M1 + 1):
        m = an + d
        ok = True
        for i in range(n + 1):
            if math.gcd(m, a[i]) == 1:
                ok = False
                break
        if ok:
            out.append(d)
    return tuple(out)


def detect_period(d, min_run=200):
    n = len(d)
    for T in range(1, n // 2):
        start = n - min_run
        ok = True
        for k in range(start, n - T):
            if d[k + T] != d[k]:
                ok = False
                break
        if ok:
            return T, sum(d[n - T:n])
    return None, None


# ===== Approach 1: f-of-a1-bounded-nonresidue-statistic =====

def check_tautology_and_set_to_set(a1, N, kmax, label):
    """For the D_n-window statistic, verify:
    (a) sigma_n -> d_{n+1} trivially single-valued at k=1 (tautology).
    (b) set-to-set sigma_n -> sigma_{n+1} minimal single-valued window k_*,
        realized state count at k_*.
    """
    a = naive_greedy(a1, N)
    M1 = 1
    for p in prime_set(a1):
        M1 *= p
    d = [a[i + 1] - a[i] for i in range(N - 1)]
    T, L = detect_period(d, min_run=max(50, T_known.get(a1, 8)))
    print(f"[{label}] a_1={a1} M1={M1} N={N} detected T={T} L={L}")

    # Compute D_n for n in [0, N-2] (need n+1 <= N-1 for d_{n+1})
    D = [None] * (N - 1)
    for n in range(N - 1):
        D[n] = Dn(a, n, M1)
    # Verify greedy: d_{n+1} = a[n+1]-a[n] = min D_n
    bad = 0
    for n in range(N - 1):
        if not D[n] or min(D[n]) != d[n]:
            bad += 1
    print(f"  greedy check: d_{n+1}=min(D_n) violations = {bad} (expect 0)")

    # (a) tautology: sigma_n -> d_{n+1} at k=1: D_n -> min(D_n) trivially single-valued
    # group by D_n, check d_{n+1} (=min D_n) consistent
    conflicts_inc = 0
    groups = defaultdict(set)
    for n in range(N - 2):
        groups[D[n]].add(d[n + 1])  # d[n+1] = a[n+1]-a[n] = min(D_n)
    for key, vals in groups.items():
        if len(vals) > 1:
            conflicts_inc += sum(1 for _ in vals)
    print(f"  (a) sigma->d_{n+1} at k=1: distinct-D_n groups with >1 d-value = {conflicts_inc} (expect 0 = TAUTOLOGY)")

    # (b) set-to-set sigma_n -> sigma_{n+1}: minimal k with 0 conflicts, realized count
    # sigma_n = (D[n-k+1],...,D[n]). Forward map single-valued at window k iff
    # for all n,n' with sigma_n=sigma_{n'}, we have D[n+1]=D[n'+1].
    # We need n in [k-1, N-3] so sigma_n and D[n+1] both defined.
    best_k = None
    best_realized = None
    for k in [1, 2, 4, 8, 16, 24, 32, 64, 65, 100, 128, 256, 512]:
        if k > N - 3:
            continue
        # build sigma_n for n in [k-1, N-3]
        sig_list = []
        sig_to_Dnext = defaultdict(set)
        sig_count = defaultdict(int)
        for n in range(k - 1, N - 2):
            sig = tuple(D[n - k + 1: n + 1])
            sig_list.append((n, sig))
            sig_to_Dnext[sig].add(D[n + 1])
            sig_count[sig] += 1
        conflicts = sum(1 for s, vals in sig_to_Dnext.items() if len(vals) > 1)
        realized = len(sig_to_Dnext)
        print(f"  (b) k={k}: conflicts={conflicts}, realized_states={realized}")
        if conflicts == 0 and best_k is None:
            best_k = k
            best_realized = realized
    if best_k:
        print(f"  => k_* (first 0-conflict) = {best_k}, realized @ k_* = {best_realized}, ratio realized/T = {best_realized/T:.3f}, k_*/T = {best_k/T:.4f}")
    return T, L


T_known = {15: 8, 35: 34, 77: 18, 91: 20, 175: 274, 375: 852, 847: 1744, 9375: 3108}

print("=" * 70)
print("APPROACH 1: f-of-a1-bounded-nonresidue-statistic")
print("=" * 70)
# small case first (hand-enumerate per round-6 rule)
check_tautology_and_set_to_set(15, 60, 8, "a1=15 hand-check")
print()
check_tautology_and_set_to_set(77, 200, 16, "rad-77 pair small")
print()
check_tautology_and_set_to_set(375, 2000, 128, "refutation witness")
