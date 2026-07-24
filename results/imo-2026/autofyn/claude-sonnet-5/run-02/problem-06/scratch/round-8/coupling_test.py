import math
from sympy import primefactors

def greedy_seq(a1, n_terms):
    seq = [a1]
    while len(seq) < n_terms:
        n = seq[-1] + 1
        while True:
            ok = all(math.gcd(n, x) > 1 for x in seq)
            if ok:
                seq.append(n)
                break
            n += 1
    return seq

def Qset(a1):
    return set(primefactors(a1))

def test_pair(a1, pk, n_terms=4000, sub_n=200):
    Q = Qset(a1)
    assert pk in Q
    a1p = a1
    while a1p % pk == 0:
        a1p //= pk
    seq = greedy_seq(a1, n_terms)
    seqp = greedy_seq(a1p, n_terms)
    Qp = Qset(a1p)
    # types wrt Qp
    def type_(x, primes):
        return frozenset(p for p in primes if x % p == 0)
    types = [type_(x, Qp) for x in seq]
    typesp = [type_(x, Qp) for x in seqp]
    return seq, seqp, types, typesp, Qp

if __name__ == "__main__":
    for a1, pk in [(15,5),(15,3),(35,5),(35,7),(105,7),(105,5),(105,3)]:
        seq, seqp, types, typesp, Qp = test_pair(a1, pk, n_terms=60)
        print(f"a1={a1} pk={pk} Qp={Qp}")
        print("orig types (Qp-level):", types[:40])
        print("reduced types        :", typesp[:40])
        print()

def test_match(a1, pk, n_terms=3000):
    seq, seqp, types, typesp, Qp = test_pair(a1, pk, n_terms=n_terms)
    stripped = [t for t in types if t != frozenset()]
    L = min(len(stripped), len(typesp))
    stripped = stripped[:L]
    red = typesp[:L]
    mismatches = [i for i in range(L) if stripped[i] != red[i]]
    return L, mismatches[:10], len(mismatches)

for a1, pk in [(15,5),(15,3),(35,5),(35,7),(105,7),(105,5),(105,3),(1155,11),(1155,7),(1155,5),(1155,3)]:
    L, mism, nmis = test_match(a1, pk, n_terms=500)
    print(a1, pk, "L=",L, "mismatches=",nmis, mism)

print("=== detail 105,7 ===")
seq, seqp, types, typesp, Qp = test_pair(105,7, n_terms=40)
for i,(x,t) in enumerate(zip(seq,types)):
    print(i+1, x, sorted(t))
print("---reduced---")
for i,(x,t) in enumerate(zip(seqp,typesp)):
    print(i+1, x, sorted(t))

print("=== growth check 105,7 ===")
for N in [100,300,1000,3000,8000]:
    L, mism, nmis = test_match(105,7, n_terms=N)
    print("N=",N,"L=",L,"nmis=",nmis,"density=",nmis/L if L else None)

print("=== distributional check 105,7 over N=3000 ===")
seq, seqp, types, typesp, Qp = test_pair(105,7, n_terms=3000)
from collections import Counter
stripped = [t for t in types if t != frozenset()]
c1 = Counter(stripped)
c2 = Counter(typesp)
print("orig-stripped freq (normalized):", {str(sorted(k)):v/len(stripped) for k,v in c1.items()})
print("reduced freq (normalized):", {str(sorted(k)):v/len(typesp) for k,v in c2.items()})
print("orig total incl empty terms:", len(types), "empty count:", len(types)-len(stripped))

print("=== more |Q|=3 seeds, all removals ===")
for a1 in [30, 70, 42, 165, 385]:
    Q = Qset(a1)
    if len(Q) != 3:
        continue
    for pk in Q:
        L, mism, nmis = test_match(a1, pk, n_terms=600)
        print(f"a1={a1} Q={Q} pk={pk} L={L} density={nmis/L if L else None:.3f}")

print("=== check 30,pk=3 with larger N (contains prime 2 kept) ===")
for N in [600,3000,8000]:
    L, mism, nmis = test_match(30,3,n_terms=N)
    print("N=",N,"L=",L,"nmis=",nmis)
