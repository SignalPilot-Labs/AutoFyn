"""Confirm: dropout cases lock; no |P1|>=3 no-lock dropouts; verify a few long runs."""
import math
from sympy import factorint


def support(m):
    return frozenset(factorint(m).keys())

def is_prime_power(m):
    return len(factorint(m)) <= 1

def gen_until_lock(a1, K=2000):
    a = [a1]
    if is_prime_power(a1):
        return a, True, list(support(a1))[0], 1
    for n in range(1, K):
        an = a[-1]; m = an + 1
        while True:
            if all(math.gcd(m, ai) > 1 for ai in a):
                break
            m += 1
        a.append(m)
        if is_prime_power(m):
            return a, True, list(support(m))[0], len(a)
    return a, False, None, None

# 1. Confirm dropout cases lock (run longer)
print("=== Confirm dropout cases eventually lock ===")
for a1 in [514, 753, 771, 1042]:
    seq, locked, lp, li = gen_until_lock(a1, K=3000)
    P1 = support(a1)
    print(f"  a1={a1} P1={set(P1)}: locked={locked} lock_prime={lp} at term#{li} (first 8 terms: {seq[:8]})")

# 2. Check |P1|>=3 no-lock cases: any dropout?
print("\n=== |P1|>=3 no-lock cases (K=250): dropouts? ===")
count_nolock_ge3 = 0
dropouts_ge3 = []
for a1 in range(6, 3001):
    f = factorint(a1)
    if len(f) < 3 or len(f) <= 1:
        continue
    P1 = frozenset(f.keys())
    seq, locked, _, _ = gen_until_lock(a1, 250)
    if locked:
        continue
    count_nolock_ge3 += 1
    n = len(seq); start = n//2
    dropped = [p for p in P1 if not any(p in support(seq[i]) for i in range(start, n))]
    if dropped:
        dropouts_ge3.append((a1, P1, dropped))
print(f"  no-lock |P1|>=3 cases: {count_nolock_ge3}")
print(f"  with a P1-prime dropped in 2nd half: {len(dropouts_ge3)}")
for d in dropouts_ge3[:10]:
    print(f"    {d}")

# 3. Verify 385 / 1309 / 2431 / 77 are truly no-lock (no prime power in 2000 terms)
print("\n=== Are the 'no-lock' test cases truly no-lock? (K=2000) ===")
for a1 in [385, 77, 1309, 2431, 715, 105, 165]:
    seq, locked, lp, li = gen_until_lock(a1, 2000)
    print(f"  a1={a1}: locked_within_2000={locked} lock_prime={lp} at #{li}")
