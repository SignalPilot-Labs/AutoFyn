import sympy
from sympy import primefactors, gcd, factorint, divisors
import random

def gen_sequence(a1, N):
    a = [None, a1]
    while len(a) <= N:
        n = len(a)-1
        prev = a[-1]
        c = prev+1
        while True:
            ok = True
            for i in range(1, n+1):
                if gcd(c, a[i]) == 1:
                    ok = False
                    break
            if ok:
                a.append(c)
                break
            c += 1
    return a

a1 = 4807
N = 1500
a = gen_sequence(a1, N)
S0 = {2,3,5,7,11,19,23,73,127}

random.seed(0)
results = []
for n in range(20, N+1, 7):  # sample every 7th index
    an = a[n]
    primes_an = set(primefactors(an))
    # pick primes q in S0 not dividing a_n (outside-type primes), and also a generic non-S0 small prime
    candidates = [q for q in S0 if q not in primes_an]
    for q in candidates[:2]:
        c = q*(an//q)
        if c <= a[n-1]:
            branch = 'a'
            j = None
        else:
            branch = 'b'
            j = None
            for i in range(1,n):
                if gcd(c,a[i])==1:
                    j = i
                    break
        results.append((n,q,branch,j))

from collections import Counter
branch_counts = Counter(r[2] for r in results)
print("branch counts:", branch_counts)

# for branch b, look at distribution of (n-j) i.e how far back is blocking index
gaps = [(n-j) for (n,q,br,j) in results if br=='b']
print("num branch-b samples:", len(gaps))
print("min gap", min(gaps) if gaps else None, "max gap", max(gaps) if gaps else None)
import statistics
if gaps:
    print("mean gap", statistics.mean(gaps), "median", statistics.median(gaps))

# check how often j is "small" (<=20) vs scales with n
small_j = sum(1 for (n,q,br,j) in results if br=='b' and j<=20)
print("branch-b with j<=20:", small_j, "/", len(gaps))

# print a handful of examples with shared-prime info
print("\nExamples:")
cnt=0
for (n,q,br,j) in results:
    if br=='b' and cnt<15:
        an=a[n]; aj=a[j]
        shared = set(primefactors(an)) & set(primefactors(aj))
        c = q*(an//q)
        print(f"n={n} q={q} c={c} j={j} a_j={aj} shared(a_n,a_j)={shared} P(c)={primefactors(c)}")
        cnt+=1
