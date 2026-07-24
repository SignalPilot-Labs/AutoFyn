import math
from sympy import factorint, primerange

def gen_sequence_fast(a1, N):
    a = [a1]
    while len(a) < N:
        an = a[-1]
        cand = an + 1
        while True:
            ok = True
            for x in a:
                if math.gcd(cand, x) == 1:
                    ok = False
                    break
            if ok:
                a.append(cand)
                break
            cand += 1
    return a

def scan(a1, N=2500):
    a = gen_sequence_fast(a1, N)
    Q = set(factorint(a1).keys())
    types = {}
    outside = {}
    for i,val in enumerate(a):
        n=i+1
        f = set(factorint(val).keys())
        rho = f & Q
        types[n] = frozenset(rho)
        outside[n] = f - Q
    from collections import defaultdict
    occ = defaultdict(list)
    for n,t in types.items():
        occ[t].append(n)
    # persistent-ish: appears many times in window, and recent occurrence near end
    persistent_types = [t for t,ns in occ.items() if len(ns)>=8 and ns[-1] > N*0.7 and t]
    # find disjoint pairs with |F'|,|F''|>=2 at EARLIEST occurrence
    results = []
    for i in range(len(persistent_types)):
        for j in range(i+1,len(persistent_types)):
            A,B = persistent_types[i], persistent_types[j]
            if A & B: continue
            nA = occ[A][0]; nB = occ[B][0]
            fA = outside[nA]; fB = outside[nB]
            if len(fA)>=2 and len(fB)>=2:
                results.append((A,B,nA,nB,fA,fB,len(occ[A]),len(occ[B])))
    return results

# candidate seeds: products of 2 or 3 small odd primes (avoid 2, since even seeds solved separately)
primes = list(primerange(3,60))
seeds = []
for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        seeds.append(primes[i]*primes[j])
        for k in range(j+1,min(j+4,len(primes))):
            seeds.append(primes[i]*primes[j]*primes[k])

seeds = sorted(set(seeds))
print("num seeds to test:", len(seeds))
found = []
tested=0
import time
t0=time.time()
for s in seeds:
    if s > 6000: continue
    tested+=1
    try:
        res = scan(s, N=2200)
    except Exception as e:
        continue
    if res:
        found.append((s,res))
        print("FOUND", s, res)
    if tested%20==0:
        print("tested",tested,"time",time.time()-t0)
print("total tested", tested, "found", len(found))
