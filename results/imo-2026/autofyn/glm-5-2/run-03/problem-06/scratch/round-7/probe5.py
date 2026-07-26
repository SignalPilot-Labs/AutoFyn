"""Find k_* for a_1=175 (check k=14..20) and re-confirm k_*=1 for a_1=847,375 with larger N."""
import math
from collections import defaultdict


def sieve(limit):
    s = bytearray([1]) * (limit + 1)
    s[0] = s[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, limit + 1, i):
                s[j] = 0
    return [i for i in range(2, limit + 1) if s[i]]


def naive_greedy(a1, N):
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
    return a


def compute_Dn(a, n, M1):
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


def window_fwd_det(Ds, d, k, N_check):
    state_to_dnext = defaultdict(set)
    conflict = 0
    for n in range(k - 1, N_check - 2):
        state = tuple(Ds[n - j] for j in range(k - 1, -1, -1))
        dnext = d[n + 1]
        if state in state_to_dnext:
            if dnext not in state_to_dnext[state]:
                conflict += 1
                state_to_dnext[state].add(dnext)
        else:
            state_to_dnext[state] = {dnext}
    return (conflict == 0, len(state_to_dnext), conflict)


a1 = 175
N = 1200
M1 = 35
a = naive_greedy(a1, N)
d = [a[i+1]-a[i] for i in range(N-1)]
Nc = 600
Ds = {n: compute_Dn(a, n, M1) for n in range(Nc)}
print(f"a1={a1}, M1={M1}, N_check={Nc}")
for k in [10, 12, 14, 15, 16, 18, 20, 25, 30]:
    fd, real, conf = window_fwd_det(Ds, d, k, Nc)
    print(f"  D_n-window k={k}: fwd_det={fd}, realized={real}, conflicts={conf}")
