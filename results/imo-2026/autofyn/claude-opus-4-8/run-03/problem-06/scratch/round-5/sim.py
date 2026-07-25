import sympy
from math import gcd

def run(a1, N=6000):
    a = [a1]
    def admissible(c, terms):
        for t in terms:
            if gcd(c,t)==1:
                return False
        return True
    c = a1+1
    terms = [a1]
    while len(terms) < N:
        while not admissible(c, terms):
            c += 1
        terms.append(c)
        c += 1
    return terms

def supports(terms):
    return [set(sympy.primefactors(t)) for t in terms]

def minimal_supports(F):
    # global minimal among the list (approx via full list, assume stabilized)
    mins = []
    Fs = [frozenset(f) for f in F]
    uniq = []
    seen=set()
    for f in Fs:
        if f not in seen:
            seen.add(f); uniq.append(f)
    for f in uniq:
        if not any(g < f for g in uniq):
            mins.append(f)
    return mins

import itertools
results=[]
seeds = [15,35,105,375,385,867,1155,2025,9375,507,899,1875,2145,2310,255255]
import random
random.seed(1)
for _ in range(60):
    seeds.append(random.randint(4,5000))

for a1 in sorted(set(seeds)):
    if a1<4: continue
    try:
        terms = run(a1, N=4000)
    except Exception as e:
        print(a1, "ERR", e); continue
    F = supports(terms)
    mins = minimal_supports(F)
    M = 1
    for p in sympy.primefactors(a1):
        M*=p
    worst_ratio=0
    worst_G=None
    worst_redmax=0
    maxprime=0
    for G in mins:
        prod = 1
        for p in G: prod*=p
        ratio = prod/a1
        if ratio>worst_ratio:
            worst_ratio=ratio; worst_G=G
        if G:
            pmax=max(G)
            redmax = prod//pmax
            if redmax/a1 > worst_redmax:
                worst_redmax = redmax/a1
            if pmax>maxprime:
                maxprime=pmax
    results.append((a1,M,len(mins),max(len(G) for G in mins),worst_ratio,worst_G,worst_redmax,maxprime))

for r in results:
    print(r)
print("MAX ratio overall:", max(r[4] for r in results))
print("MAX redmax ratio overall:", max(r[6] for r in results))

print("---- extra structured seeds ----")
import sympy
extra = [2*3*5*7, 2*3*5*7*11, 2*3*5*7*11*13, 3*5*7*11, 3*5*7*11*13, 2*3*5, 2*3*5*11, 3*5*7, 5*7*11, 5*7*11*13, 7*11*13, 2*3*7*11, 899*2, 899*3, 3*899, 5*899]
random.seed(2)
for _ in range(20):
    # products of 3-4 random small primes
    ps = random.sample([2,3,5,7,11,13,17,19,23],random.randint(2,4))
    v=1
    for p in ps: v*=p
    extra.append(v)

results2=[]
for a1 in sorted(set(extra)):
    if a1<4: continue
    try:
        terms = run(a1, N=4000)
    except Exception as e:
        print(a1,"ERR",e); continue
    F = supports(terms)
    mins = minimal_supports(F)
    worst_ratio=0; worst_G=None; worst_redmax=0
    for G in mins:
        prod=1
        for p in G: prod*=p
        ratio=prod/a1
        if ratio>worst_ratio:
            worst_ratio=ratio; worst_G=G
        if G:
            pmax=max(G)
            redmax=(prod//pmax)/a1
            if redmax>worst_redmax: worst_redmax=redmax
    results2.append((a1,len(mins),max(len(G) for G in mins),worst_ratio,worst_G,worst_redmax))
for r in results2: print(r)
print("MAX ratio2:", max(r[3] for r in results2))
print("MAX redmax2:", max(r[5] for r in results2))
