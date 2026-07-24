import sympy
from sympy import primefactors, gcd, factorint
from collections import Counter

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
Q = set(primefactors(a1))
print("Q = P(a1) =", Q)

# For each sampled (n,q), find ALL blocking indices j (not just the first), and check
# what primes they share with a_n, classifying as Q / S0\Q / outside-S0
all_shared_classes = Counter()
outside_S0_events = []

for n in range(20, N+1, 11):
    an = a[n]
    primes_an = set(primefactors(an))
    candidates = [q for q in S0 if q not in primes_an]
    for q in candidates[:2]:
        c = q*(an//q)
        if c <= a[n-1]:
            continue
        blockers = [i for i in range(1,n) if gcd(c,a[i])==1]
        if not blockers: continue
        for j in blockers[:50]:  # cap
            shared = set(primefactors(an)) & set(primefactors(a[j]))
            for p in shared:
                if p in Q: all_shared_classes['Q'] += 1
                elif p in S0: all_shared_classes['S0\\Q'] += 1
                else:
                    all_shared_classes['outside_S0'] += 1
                    outside_S0_events.append((n,q,j,p))

print("shared-prime class counts (over all blockers found, all classes an index contributes):", all_shared_classes)
print("num outside-S0 shared-prime events:", len(outside_S0_events))
for ev in outside_S0_events[:10]:
    print(ev)

print("\n--- Smallest-blocker distribution ---")
from collections import Counter
smallest_j_counter = Counter()
for n in range(20, N+1, 11):
    an = a[n]
    primes_an = set(primefactors(an))
    candidates = [q for q in S0 if q not in primes_an]
    for q in candidates[:2]:
        c = q*(an//q)
        if c <= a[n-1]:
            continue
        for i in range(1,n):
            if gcd(c,a[i])==1:
                smallest_j_counter[i]+=1
                break
print(smallest_j_counter.most_common(15))
