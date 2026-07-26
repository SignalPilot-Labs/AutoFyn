import sys, math, random
sys.path.insert(0, '/tmp/round-6')
from mt_greedy import sieve_primes, prime_factors, rad, add_set_to_MT, prune_minimal

# Theorem: under edge addition F -> F ∪ {S}, once a prime p leaves ∪MT (i.e. p in ∪MT(F_n) \ ∪MT(F_{n+1})),
# it never re-enters ∪MT(F_m) for m>n.
# Proof sketch: new_MT is built from old MT transversals (survivors + extensions T∪{q}). If p not in any
# new_MT transversal, then at the NEXT step the "old MT" has no transversal containing p, so neither
# survival nor extension can reintroduce p.

def greedy_track_drops(a1, N, sp):
    a=[0]*N; a[0]=a1
    P0=prime_factors(a1,sp); MT=prune_minimal([{p} for p in P0])
    prev_active=set(P0)
    dropped=set()  # primes that left and (by theorem) never return
    violations=[]
    for step in range(1,N):
        m=a[step-1]+1
        while True:
            Pm=prime_factors(m,sp)
            if any(t<=Pm for t in MT): break
            m+=1
        a[step]=m
        MT=add_set_to_MT(MT, prime_factors(m,sp))
        active=set()
        for t in MT: active|=set(t)
        # check theorem: any prime in 'dropped' should NOT be in active
        for p in dropped:
            if p in active:
                violations.append((step,p))
        # update dropped: primes that were active last step but not now
        new_drops = prev_active - active
        dropped |= new_drops
        prev_active = active
    return violations, dropped, active

sp=sieve_primes(2_000_000)
print("=== Verify 'once dropped never re-enters' on greedy ===")
for a1,N in [(77,120),(847,60000),(385,130000),(175,1200),(15,60),(35,200),(91,120)]:
    v,drops,final_active=greedy_track_drops(a1,N,sp)
    print(f"  a1={a1}: violations(re-entry)={len(v)} dropped_count={len(drops)} final_active={sorted(final_active)}")
    if v: print(f"    FIRST VIOLATION: {v[0]}")

# Also test on ARTIFICIAL random hypergraph sequences (not the greedy) to stress-test the theorem
print()
print("=== Stress test on random hypergraph edge additions ===")
random.seed(42)
primes_list=list(sieve_primes(50))
for trial in range(2000):
    # start with one random set
    S0=set(random.sample(primes_list, random.randint(1,4)))
    MT=prune_minimal([frozenset(S0)])
    active=set(S0); dropped=set(); v=[]
    for _ in range(40):
        S=set(random.sample(primes_list, random.randint(1,4)))
        MT=add_set_to_MT(MT, S)
        new_active=set()
        for t in MT: new_active|=set(t)
        for p in dropped:
            if p in new_active: v.append((p,))
        dropped |= (active - new_active)
        active=new_active
    if v:
        print(f"  trial {trial}: VIOLATION {v[:3]}"); break
else:
    print("  2000 random trials: 0 violations — theorem holds")
