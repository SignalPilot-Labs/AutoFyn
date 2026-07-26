import math
from itertools import count

def greedy_seq(a1, N):
    a = [a1]
    # keep set of prior terms for gcd check
    while len(a) < N:
        m = a[-1] + 1
        while True:
            if all(math.gcd(m, x) > 1 for x in a):
                a.append(m)
                break
            m += 1
    return a

# a1 = 15 case
a = greedy_seq(15, 200)
print("a1=15 first 20:", a[:20])
# check periodicity T=8, L=30
T, L = 8, 30
ok = all(a[n+T] == a[n]+L for n in range(len(a)-T))
print(f"T={T},L={L} periodic from n=0 over {len(a)} terms:", ok)

# cofactor AP for q=3
q = 3
# find indices where q | a_n
idx = [n for n in range(len(a)) if a[n] % q == 0]
print("q=3 multiple indices (first 20):", idx[:20])
cof = [a[n]//q for n in idx]
print("cofactors (first 20):", cof[:20])
# check k_{i+s} = k_i + L/q where s = number of q-multiples per period
Lq = L // q
print(f"L/q = {Lq}")
# find s: count q-multiples in first T indices
s = sum(1 for n in range(T) if a[n] % q == 0)
print(f"s (q-multiples per period) = {s}")
# verify k_{i+s} = k_i + Lq
ap_ok = all(cof[i+s] == cof[i] + Lq for i in range(len(cof)-s))
print(f"k_{{i+s}} = k_i + L/q holds:", ap_ok)

# check distinct big primes in cofactors
big_primes = set()
for k in cof:
    for p in range(16, k+1):
        if k % p == 0:
            # check primality
            if all(p % d for d in range(2, int(p**0.5)+1) if p>2):
                big_primes.add(p)
print(f"distinct primes >M_1=15 in cofactors over {len(a)} terms:", len(big_primes))
print("max such prime:", max(big_primes) if big_primes else None)
