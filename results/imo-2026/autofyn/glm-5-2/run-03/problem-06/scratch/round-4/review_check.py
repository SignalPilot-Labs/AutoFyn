import sympy as sp

def greedy(a1, N):
    a=[a1]; primes_seen=set(sp.factorint(a1).keys())
    for _ in range(N-1):
        x=a[-1]+1
        while True:
            ok=True
            for p in primes_seen:
                if (x % p)==0:
                    ok=True; break
            # need gcd(x, a_i)>1 for every i; since every a_i has a prime in primes_seen,
            # and primes_seen accumulates, checking against primes_seen of PAST terms is right
            # but primes_seen must be the set at the TIME of selecting x (past only)
            ok=False
            for p in primes_seen:
                if x % p ==0:
                    ok=True; break
            if ok: break
            x+=1
        a.append(x)
        for p in sp.factorint(x).keys():
            primes_seen.add(p)
    return a

# 1. Schur premise: a1=15, q=3 governing (<= M_1=15). Cofactors k_i = a_n/3, prime factors?
a=greedy(15, 600)
kprimes=set()
for v in a:
    if v % 3 ==0:
        for p in sp.factorint(v//3).keys():
            kprimes.add(p)
print("a1=15 q=3: distinct primes in cofactors k_i = a_n/3:", sorted(kprimes))
print("  max prime in k_i:", max(kprimes) if kprimes else None, " M_1=15")
# how many k_i have a prime > 15
cnt_large=0
for v in a:
    if v%3==0:
        if any(p>15 for p in sp.factorint(v//3).keys()):
            cnt_large+=1
print("  # q-multiples with a cofactor-prime > 15:", cnt_large, " out of", sum(1 for v in a if v%3==0))

# 2. Primal minimal-support antichain size for a few a_1
def minimal_supports(supports):
    # supports: list of frozensets; return inclusion-minimal ones
    ms=[]
    for s in supports:
        if any(s2 <= s for s2 in supports if s2 is not s and s2 != s):
            # s is non-minimal if some s2 strict subset exists
            pass
    # proper: minimal = no strict subset in the family
    out=[]
    for i,s in enumerate(supports):
        minimal=True
        for j,s2 in enumerate(supports):
            if i!=j and s2 < s:
                minimal=False; break
        if minimal: out.append(s)
    return out

for a1 in [15,35,65,77,91,143,175,385,847]:
    a=greedy(a1, 1500)
    supports=[frozenset(sp.factorint(v).keys()) for v in a]
    ms=minimal_supports(supports)
    allprimes=set()
    for s in ms: allprimes|=set(s)
    M1=1
    for p in sp.factorint(a1).keys(): M1*=p
    print(f"a1={a1}: #minimal_supports={len(ms)}, primes in MS={sorted(allprimes)}, M1={M1}, all<=M1? {all(p<=M1 for p in allprimes)}")
