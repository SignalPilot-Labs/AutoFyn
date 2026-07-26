"""Round-7 verification for Approach 2 (parametric-recruitment-family) and
Approach 3 (p1-equals-2-direct).

Reproduce:
- A2: MT-prime set evolution for a_1=375 (stabilizes by step 6 to {2,3,5,7,19})
      and a_1=9375 (non-monotone; final {2,3,5,7,67}); cofactor-collapse 96.6%.
- A3: strengthened cofactor-P1-divisibility: 0 cofactor-fails for a_1=375,
      r in {2,7,19} (governing, not in P_1={3,5}).
"""
import math
from collections import defaultdict


def sieve_primes(limit):
    s = bytearray([1]) * (limit + 1)
    s[0] = s[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, limit + 1, i):
                s[j] = 0
    return [i for i in range(2, limit + 1) if s[i]]


def prime_factors(x, small_primes):
    fs = set()
    y = x
    for p in small_primes:
        if p * p > y:
            break
        if y % p == 0:
            fs.add(p)
            while y % p == 0:
                y //= p
    if y > 1:
        fs.add(y)
    return fs


def prune_minimal(family):
    kept = []
    for s in sorted(family, key=len):
        if not any(t <= s for t in kept):
            kept.append(s)
    out = []
    seen = set()
    for s in kept:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def add_set_to_MT(MT, S_new):
    S_new = frozenset(S_new)
    new = []
    for T in MT:
        if T & S_new:
            new.append(T)
        else:
            for p in S_new:
                new.append(T | {p})
    return prune_minimal(new)


def mt_prime_set(MT):
    s = set()
    for T in MT:
        s |= set(T)
    return s


def rad(a1):
    fs = set()
    x = a1
    d = 2
    while d * d <= x:
        if x % d == 0:
            fs.add(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        fs.add(x)
    r = 1
    for p in fs:
        r *= p
    return r


def run_mt_greedy(a1, N):
    M1 = rad(a1)
    maxval = a1 + (N + 5) * M1 + 50
    small_limit = min(maxval + 1000, 2_000_000)
    sp = sieve_primes(small_limit)
    a = [0] * N
    a[0] = a1
    P0 = prime_factors(a1, sp)
    MT = prune_minimal([frozenset([p]) for p in P0])
    # track MT-prime set evolution
    mt_prime_evol = [None] * N
    mt_prime_evol[0] = frozenset(mt_prime_set(MT))
    grow_events = 0
    shrink_events = 0
    prev_primes = set(mt_prime_evol[0])
    flush_steps = []
    for step in range(1, N):
        prev = a[step - 1]
        m = prev + 1
        while True:
            Pm = prime_factors(m, sp)
            if any(t <= Pm for t in MT):
                break
            m += 1
        a[step] = m
        S_new = prime_factors(m, sp)
        MT = add_set_to_MT(MT, S_new)
        cur = set(mt_prime_set(MT))
        mt_prime_evol[step] = frozenset(cur)
        if cur != prev_primes:
            added = cur - prev_primes
            removed = prev_primes - cur
            if added:
                grow_events += 1
            if removed:
                shrink_events += 1
                if len(removed) >= 10:
                    flush_steps.append((step, len(removed), len(added)))
            prev_primes = cur
    return a, MT, mt_prime_evol, (grow_events, shrink_events, flush_steps)


def detect_period(a, N):
    d = [a[i + 1] - a[i] for i in range(N - 1)]
    n = len(d)
    for T in range(1, n // 2):
        start = n - min(200, n // 3)
        ok = True
        for k in range(start, n - T):
            if d[k + T] != d[k]:
                ok = False
                break
        if ok:
            return T, sum(d[n - T:n])
    return None, None


# ===== A2: a_1=375 =====
print("=" * 70)
print("A2: a_1=375 (refutation witness, expect MT stabilizes by step 6)")
print("=" * 70)
N = 1500
a375, MT375, evol375, (ge, se, fs375) = run_mt_greedy(375, N)
T375, L375 = detect_period(a375, N)
print(f"T={T375} L={L375}")
print(f"final MT-prime set: {sorted(mt_prime_set(MT375))}")
print(f"final MT: {sorted([sorted(t) for t in MT375])}")
print(f"grow_events={ge} shrink_events={se}")
# print evolution for first 15 steps
print("MT-prime set evolution (first 15 steps):")
for i in range(15):
    print(f"  step {i}: {sorted(evol375[i])}")
# when does it stabilize?
stable_from = None
for i in range(1, N):
    if all(evol375[i] == evol375[i - 1] for i2 in range(i, min(i + 50, N)) for _ in [0]):
        pass
# simpler: find first i such that evol is constant from i to N-1
target = evol375[N - 1]
for i in range(N - 1, -1, -1):
    if evol375[i] != target:
        stable_from = i + 1
        break
else:
    stable_from = 0
print(f"MT-prime set stable from step {stable_from} to N={N}: {sorted(evol375[stable_from])}")

# ===== A2: a_1=9375 =====
print()
print("=" * 70)
print("A2: a_1=9375 (expect non-monotone; final {2,3,5,7,67})")
print("=" * 70)
N2 = 4000
a9375, MT9375, evol9375, (ge2, se2, fs9375) = run_mt_greedy(9375, N2)
T9375, L9375 = detect_period(a9375, N2)
print(f"T={T9375} L={L9375}")
print(f"final MT-prime set: {sorted(mt_prime_set(MT9375))}")
print(f"grow_events={ge2} shrink_events={se2}")
print(f"flush steps (>=10 primes removed at once): {fs9375[:10]}")
# count distinct transient primes ever seen
ever = set()
for i in range(N2):
    ever |= set(evol9375[i])
print(f"distinct MT-primes ever seen: {len(ever)}")
print(f"governing (final): {sorted(mt_prime_set(MT9375))}")
print(f"transient ever: {len(ever - set(mt_prime_set(MT9375)))}")

# cofactor-collapse: % of terms carrying a prime outside governing set {2,3,5,7,67}
gov = set(mt_prime_set(MT9375))
sp = sieve_primes(min(9375 + (N2 + 5) * 15 + 1000, 2_000_000))
out_count = 0
for i in range(N2):
    Pf = prime_factors(a9375[i], sp)
    if Pf - gov:
        out_count += 1
print(f"terms carrying a prime outside governing skeleton: {out_count}/{N2} = {100*out_count/N2:.1f}%")

# ===== A3: cofactor-P1-divisibility for a_1=375 =====
print()
print("=" * 70)
print("A3: strengthened cofactor-P1-divisibility, a_1=375")
print("=" * 70)
# P1={3,5}, p=3,q=5. governing G = primes of L = {2,3,5,7,19}. r notin P1: {2,7,19}
P1 = {3, 5}
G = set(prime_factors(L375, sp)) if L375 else {2, 3, 5, 7, 19}
print(f"P1={sorted(P1)} L={L375} G={sorted(G)}")
for r in sorted(G - P1):
    mults = 0
    fails = 0
    for i in range(N):
        if a375[i] % r == 0:
            mults += 1
            k = a375[i] // r
            if k % 3 != 0 and k % 5 != 0:
                fails += 1
    print(f"  r={r}: r-multiples={mults}, cofactor-fails (k not div by 3 or 5)={fails}")

# also check a_1=15 (small, hand-checkable)
print()
print("A3 small-check a_1=15:")
a15, MT15, _, _ = run_mt_greedy(15, 200)
T15, L15 = detect_period(a15, 200)
print(f"T={T15} L={L15} G={sorted(set(prime_factors(L15, sieve_primes(1000))))}")
P1_15 = {3, 5}
sp15 = sieve_primes(1000)
G15 = set(prime_factors(L15, sp15))
for r in sorted(G15 - P1_15):
    mults = 0; fails = 0
    for i in range(200):
        if a15[i] % r == 0:
            mults += 1
            k = a15[i] // r
            if k % 3 != 0 and k % 5 != 0:
                fails += 1
    print(f"  r={r}: r-multiples={mults}, fails={fails}")
