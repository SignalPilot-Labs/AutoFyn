import random
from sim import gen_sequence
from sympy import primefactors

def rad_prod(C):
    p=1
    for x in C: p*=x
    return p

def T_C(a1, C):
    prod = rad_prod(C)
    x = prod
    while True:
        if x > a1 and set(primefactors(x)) == set(C):
            return x
        x += prod

random.seed(42)
candidates = []
# a mix of semiprimes and 3-factor composites, various sizes
for _ in range(20):
    p = random.choice([2,3,5,7,11,13,17,19,23,29,31,37,41,43])
    q = random.choice([53,59,61,67,71,73,79,83,89,97,101,103,107,109,113])
    if p==q: continue
    candidates.append(p*q)
for _ in range(10):
    p,q,r = random.sample([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53],3)
    candidates.append(p*q*r)

total_mismatch_beyond_n1 = 0
tested = 0
for a1 in sorted(set(candidates)):
    if a1 < 4: continue
    try:
        a, history = gen_sequence(a1, 300)
    except Exception as e:
        print(f"a1={a1}: ERROR {e}")
        continue
    seen=set()
    mism=0
    for n in range(1,301):
        rad = frozenset(primefactors(a[n]))
        if rad in seen: continue
        seen.add(rad)
        Tc = T_C(a1, rad)
        if Tc != a[n]:
            if n==1:
                continue  # expected boundary artifact
            mism+=1
            print(f"  VIOLATION a1={a1} n={n} a_n={a[n]} rad={sorted(rad)} T_C={Tc}")
    tested += 1
    total_mismatch_beyond_n1 += mism
    print(f"a1={a1}: distinct radicals(first 300 terms)={len(seen)}, mismatches(excl n=1)={mism}")

print(f"\nTOTAL: tested {tested} a1 values, total mismatches beyond n=1: {total_mismatch_beyond_n1}")
