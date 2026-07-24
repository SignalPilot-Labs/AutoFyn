import sympy

def gen(a1, N):
    a = [a1]
    while len(a) < N:
        c = a[-1] + 1
        while True:
            ok = all(__import__('math').gcd(c, x) > 1 for x in a)
            if ok:
                a.append(c)
                break
            c += 1
    return a

import math

def primes(x):
    return set(sympy.primefactors(x))

N = 8000
a1 = 4807
seq = gen(a1, N)
S0 = {2,3,5,11,19,23}
rho = [primes(x) & S0 for x in seq]

# find occurrences of type A'={3,5,19}, B'={2,11}
A = frozenset({3,5,19})
B = frozenset({2,11})
Aidx = [i+1 for i,t in enumerate(rho) if frozenset(t)==A]
Bidx = [i+1 for i,t in enumerate(rho) if frozenset(t)==B]
print("num A occ:", len(Aidx), "first few:", Aidx[:15])
print("num B occ:", len(Bidx), "first few:", Bidx[:15])

# canonical witness n_A=6
print("a_6 =", seq[5], "factors:", primes(seq[5]), "F'_6 (out of core):", primes(seq[5])-S0)

# check B occurrences singleton out-of-core signatures
sig_counts = {}
for i in Bidx:
    outcore = primes(seq[i-1]) - S0
    sig_counts.setdefault(frozenset(outcore), []).append(i)

for sig, idxs in sig_counts.items():
    if len(sig)==1:
        print("singleton B sig:", set(sig), "count:", len(idxs), "first idx:", idxs[0])

# check x_1=72
if 72 <= N:
    print("a_72=", seq[71], "outcore:", primes(seq[71])-S0)

# check q=17 divides ALL A occurrences with n>72 and all B occurrences with n>6
q = 17
badA = [n for n in Aidx if n>72 and seq[n-1] % q != 0]
badB = [n for n in Bidx if n>6 and seq[n-1] % q != 0]
print("bad A (should be empty):", badA[:10], len(badA))
print("bad B (should be empty):", badB[:10], len(badB))
