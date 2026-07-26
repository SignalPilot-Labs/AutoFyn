"""Check cofactor-P1-divisibility for a_1=375, r=19 (actual governing prime > M_1)."""
import sys
sys.path.insert(0, '/tmp/round-6')
from mt_greedy import greedy_mt, rad, sieve_primes

a1 = 375
N = 3000
M1 = rad(a1)  # 15
maxval = a1 + (N+5)*M1 + 50
sp = sieve_primes(min(maxval, 4_000_000))
a = greedy_mt(a1, N, sp)

p, q = 3, 5
r = 19
# For every term a_n divisible by r, check cofactor k = a_n / r divisible by p or q
fails = []
total = 0
for i, x in enumerate(a):
    if x % r == 0:
        k = x // r
        total += 1
        if k % p != 0 and k % q != 0:
            fails.append((i, x, k))
print(f"a1={a1}, r={r}, M1={M1}")
print(f"total r-multiple terms in first {N}: {total}")
print(f"cofactor NOT divisible by {p} or {q}: {len(fails)}")
if fails[:10]:
    print("first fails:", fails[:10])
# also check r=2,3,5,7 (other governing primes <= M_1)
for r2 in [2,3,5,7,19]:
    fs = []
    tot = 0
    for x in a:
        if x % r2 == 0:
            k = x // r2
            tot += 1
            if k % p != 0 and k % q != 0:
                fs.append((x,k))
    print(f"  r={r2}: {tot} multiples, {len(fs)} cofactor-fails (not div by 3 or 5)")
