import sys, time
from sim import gen_sequence
from sympy import primefactors, nextprime, primerange

def rad_prod(C):
    p=1
    for x in C: p*=x
    return p

def T_C(a1, C):
    """smallest x > a1 with rad(x) == C, via brute search over multiples of prod(C)
    scaling up powers of the largest prime, cheap for small |C|."""
    prod = rad_prod(C)
    # search multiples of prod, of the form prod * m where every prime factor of m is in C
    # simplistic: iterate k=1,2,... test prod*k, check rad==C, until prod*k>a1
    x = prod
    while True:
        if x > a1 and set(primefactors(x)) == set(C):
            return x
        x += prod

a1 = int(sys.argv[1])
N = int(sys.argv[2])
a, history = gen_sequence(a1, N)
P1 = frozenset(primefactors(a1))
print(f"a1={a1}  P1={sorted(P1)}  N={N}")

# find all "collapse events": times n where antichain shrinks (size decreases)
prev_size = None
prev_set = None
collapses = []
for n in range(1, N+1):
    cur = history[n]
    if prev_set is not None and len(cur) < len(prev_set):
        removed = prev_set - cur
        added = cur - prev_set
        collapses.append((n, removed, added))
    prev_set = cur

print(f"# collapse events (size decreases): {len(collapses)}")
for n, removed, added in collapses:
    print(f"n={n}: added {[sorted(x) for x in added]}   removed {len(removed)} elts: {[sorted(x) for x in sorted(removed,key=lambda s:(len(s),sorted(s)))]}")
    for newc in added:
        Tc = T_C(a1, newc)
        print(f"    T_C for {sorted(newc)} = {Tc},  a_n={a[n]}  (match: {Tc==a[n]})")
        # bound check: for each removed r with newc < r, check r's "extra primes" q = r - newc
        prodc = rad_prod(newc)
        bound_primes = [p for p in primerange(2, Tc//prodc + 2) if p not in newc]
        print(f"    extremal bound (#primes q with q*prod({sorted(newc)})<T_C, q not in C): {len(bound_primes)}  (primes: {bound_primes[:30]}{'...' if len(bound_primes)>30 else ''})")
        fan_qs = []
        for r in removed:
            if newc < r:
                extra = r - newc
                fan_qs.append(sorted(extra))
        print(f"    observed removed supersets' extra-prime-sets: {fan_qs}")
