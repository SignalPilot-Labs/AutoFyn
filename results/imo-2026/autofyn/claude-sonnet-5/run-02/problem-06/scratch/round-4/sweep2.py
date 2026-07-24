from sim import *
from sim3 import find_rogue_pairs_at_S0
import itertools

def test_seed(a1, length=3500, tail_frac=0.5):
    try:
        seq, Q, base_persist, canon_idx, F, S, S0 = analyze(a1, length, tail_frac, verbose=False)
        ep, ce, viol, rogue = find_rogue_pairs_at_S0(seq, Q, S0, base_persist, tail_frac)
    except Exception as e:
        return
    if not rogue:
        return
    multi_found=False
    for (Ap,Bp,A,B) in rogue:
        m = None
        for i in range(len(seq)):
            if (P(seq[i]) & S0) == Bp:
                m = i; break
        if m is None: continue
        Fprime = P(seq[m]) - S0
        if len(Fprime)>=2:
            multi_found=True
            print(f"a1={a1} MULTI FOUND: A'={sorted(Ap)} B'={sorted(Bp)} F'={sorted(Fprime)}")
    if multi_found:
        print(f"  -> a1={a1} Q={sorted(Q)} S0={sorted(S0)}")

primes = [2,3,5,7,11,13,17,19,23,29]
seeds = set()
for k in range(2,5):
    for combo in itertools.combinations(primes, k):
        prod=1
        for p in combo: prod*=p
        if prod < 20000:
            seeds.add(prod)
print(f"testing {len(seeds)} seeds")
for a1 in sorted(seeds):
    test_seed(a1)
print("done")
