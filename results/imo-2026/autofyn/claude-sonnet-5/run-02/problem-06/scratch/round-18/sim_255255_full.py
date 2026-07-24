import numpy as np
import time

def sieve_spf(limit):
    spf = np.zeros(limit+1, dtype=np.int32)
    for i in range(2, limit+1):
        if spf[i] == 0:
            spf[i::i] = np.where(spf[i::i]==0, i, spf[i::i])
    return spf

LIMIT = 30_000_000
t0=time.time()
spf = sieve_spf(LIMIT)
print("sieve time", time.time()-t0)

def primefactors(x, spf):
    s=set()
    while x>1:
        p=spf[x]
        if p==0:
            s.add(x); break
        s.add(int(p))
        while x % p==0:
            x//=p
    return s

a1 = 255255
target_n = 500000

a_last = a1
prime_bitmask = {}
fullmask = 0
n = 1
bit = 1
f0 = primefactors(a1, spf)
for p in f0:
    prime_bitmask[p] = prime_bitmask.get(p,0) | bit
fullmask |= bit

Q = frozenset({3,5,7,11,13,17})
types_all = {}
t0=time.time()
c = a1+1
while n < target_n:
    fc = primefactors(c, spf)
    union = 0
    for p in fc:
        union |= prime_bitmask.get(p, 0)
    if union == fullmask:
        n += 1
        bit = 1 << (n-1)
        for p in fc:
            prime_bitmask[p] = prime_bitmask.get(p,0) | bit
        fullmask |= bit
        typ = frozenset(fc) & Q
        types_all.setdefault(typ, []).append(n)
        if n % 50000 == 0:
            print("n=",n,"a_n=",c,"elapsed",time.time()-t0)
        a_last = c
        c += 1
    else:
        c += 1

print("final n", n, "a_n", a_last, "elapsed", time.time()-t0)
fullQ = frozenset(Q)
print("full-Q occurrences:", types_all.get(fullQ))
target = frozenset({5,7,11,13,17})
print("{5,7,11,13,17} occurrences:", types_all.get(target))
# count distinct types and min occurrences
counts = {k: len(v) for k,v in types_all.items()}
mincount = min(counts.values())
print("num distinct types:", len(counts), "min occurrence count:", mincount)
