import numpy as np
import sys, time

def sieve_spf(limit):
    spf = np.zeros(limit+1, dtype=np.int32)
    for i in range(2, limit+1):
        if spf[i] == 0:
            spf[i::i] = np.where(spf[i::i]==0, i, spf[i::i])
    return spf

LIMIT = 6_000_000
t0=time.time()
spf = sieve_spf(LIMIT)
print("sieve time", time.time()-t0)

def primefactors(x, spf):
    s=set()
    while x>1:
        p=spf[x]
        if p==0:
            # x itself is prime > LIMIT sqrt guess; shouldn't happen if LIMIT big enough
            s.add(x)
            break
        s.add(int(p))
        while x % p==0:
            x//=p
    return s

a1 = 255255
target_n = 140000

a = [a1]
prime_bitmask = {}  # prime -> int bitmask of indices (bit i-1 for term i) divisible by prime
fullmask = 0  # bits for all indices so far
n = 1
bit = 1  # bit for index 1
# set bitmask for a1's primes
f0 = primefactors(a1, spf)
for p in f0:
    prime_bitmask[p] = prime_bitmask.get(p,0) | bit
fullmask |= bit

types_first = {}
types_all = {}
Q = frozenset({3,5,7,11,13,17})
t0=time.time()
c = a1+1
while n < target_n:
    fc = primefactors(c, spf)
    union = 0
    for p in fc:
        union |= prime_bitmask.get(p, 0)
    if union == fullmask:
        # legal
        n += 1
        bit = 1 << (n-1)
        for p in fc:
            prime_bitmask[p] = prime_bitmask.get(p,0) | bit
        fullmask |= bit
        a.append(c)
        typ = frozenset(fc) & Q
        types_all.setdefault(typ, []).append(n)
        if n % 20000 == 0:
            print("n=",n,"a_n=",c,"elapsed",time.time()-t0)
        c += 1
    else:
        c += 1

print("final n", n, "a_n", a[-1], "elapsed", time.time()-t0)
typ = frozenset({5,7,11,13,17})
print("occurrences of {5,7,11,13,17}:", types_all.get(typ))

