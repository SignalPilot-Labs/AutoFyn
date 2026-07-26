"""Round-7: (a) verify governing set for a_1=375 = 3*5^3; (b) D_n-window k_* for a_1=175 (higher k)."""
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


def naive_greedy(a1, N, primes):
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


# (a) governing set for a_1=375
a1 = 375
N = 3000
primes = sieve(200000)
a = naive_greedy(a1, N, primes)
# collect all prime factors appearing in a (these include transient + governing)
allpf = set()
for ai in a:
    allpf |= prime_factors(ai, primes)
# M1 = rad(375) = 15
M1 = 15
gov_candidates = sorted(p for p in allpf)
print(f"a1={a1}, N={N}, M1=rad(a1)={M1}")
print(f"distinct primes appearing in a[0..{N-1}]: {gov_candidates[:30]} ... total={len(allpf)}")
# period & L: a_{n+T}=a_n+L => L=a[n+T]-a[n]
# find T by checking a_{n+T}-a_n constant
for T in range(100, 1200):
    if a[T] - a[0] == a[T+1] - a[1] == a[T+2] - a[2]:
        L = a[T] - a[0]
        # verify over a stretch
        ok = all(a[i+T] - a[i] == L for i in range(max(0, N - T - 50), N - T))
        if ok:
            print(f"  T={T}, L={L}, L factorization: {prime_factors(L, primes)}")
            break
else:
    print("  T not found in [100,1200)")

# (b) a_1=175 higher-k D_n-window
print()
a1b = 175
Nb = 1200
primesb = sieve(20000)
ab = naive_greedy(a1b, Nb, primesb)
M1b = 35
db = [ab[i+1]-ab[i] for i in range(len(ab)-1)]
Ncb = 600
Dsb = {n: compute_Dn(ab, n, M1b) for n in range(Ncb)}
print(f"a1={a1b}, M1={M1b}, N_check={Ncb}")
for k in range(1, 9):
    fd, real, conf = window_fwd_det(Dsb, db, k, Ncb)
    print(f"  D_n-window k={k}: fwd_det={fd}, realized={real}, conflicts={conf}")
