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
N = 3000
a = gen(a1, N)
Q = P(a1)
print("Q", Q)
# find persistent base types via tail sample
from collections import defaultdict
tail_start = int(N*0.6)
counts = defaultdict(int)
tau = {}
for n in range(1, N+1):
    tau[n] = frozenset(P(a[n]) & Q)
for n in range(tail_start, N+1):
    counts[tau[n]] += 1
persistent = {t for t,c in counts.items() if c >= 5}
print("persistent base types:", persistent)
m = {}
for t in persistent:
    for n in range(1, N+1):
        if tau[n] == t:
            m[t] = n
            break
print("witnesses:", m)
S = set()
for t in persistent:
    S |= (P(a[m[t]]) - Q)
S0 = Q | S
print("S", S, "S0", S0)
rho = {n: frozenset(P(a[n]) & S0) for n in range(1, N+1)}
counts2 = defaultdict(int)
for n in range(tail_start, N+1):
    counts2[rho[n]] += 1
persistent_ext = {t for t,c in counts2.items() if c >= 5}
print("extended-persistent types:", persistent_ext)

# find disjoint base pairs & report gap statistics for one such type
# find first-occurrence witnesses for each extended type
wext = {}
for t in persistent_ext:
    for n in range(1, N+1):
        if rho[n] == t:
            wext[t] = n
            break
print("ext witnesses", wext)

for t in persistent_ext:
    occ = [n for n in range(1, N+1) if rho[n]==t]
    if len(occ) < 3: continue
    gaps = [occ[i+1]-occ[i] for i in range(len(occ)-1)]
    print(t, "count", len(occ), "gap min/max/avg", min(gaps), max(gaps), sum(gaps)/len(gaps))

# check growth of max gap with N for a sparse-ish type across truncations
import sys
target_candidates = list(persistent_ext)
