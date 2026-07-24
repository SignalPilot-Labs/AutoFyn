import sys
from math import gcd

def factorize(x):
    f = set()
    d = 2
    while d*d <= x:
        if x % d == 0:
            f.add(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        f.add(x)
    return f

def gen(a1, N):
    a = [None, a1]
    while len(a) <= N:
        prev = a[-1]
        c = prev + 1
        while True:
            ok = True
            for x in a[1:]:
                if gcd(c, x) == 1:
                    ok = False
                    break
            if ok:
                a.append(c)
                break
            c += 1
    return a

def P(x, cache={}):
    if x not in cache:
        cache[x] = factorize(x)
    return cache[x]

a1 = 4807
N = 6000
a = gen(a1, N)
Q = P(a1)
S0 = {2,3,5,7,11,19,23,73,127}
rho = {n: frozenset(P(a[n]) & S0) for n in range(1, N+1)}

target = frozenset({19, 2, 11, 7})  # a sparser type from earlier run
for cutoff in [1500,2000,3000,4000,5000,6000]:
    occ = [n for n in range(1, cutoff+1) if rho[n]==target]
    if len(occ) < 3: 
        print(cutoff, "too few", len(occ))
        continue
    gaps = [occ[i+1]-occ[i] for i in range(len(occ)-1)]
    print(cutoff, "count", len(occ), "max gap", max(gaps), "last occ", occ[-1])
