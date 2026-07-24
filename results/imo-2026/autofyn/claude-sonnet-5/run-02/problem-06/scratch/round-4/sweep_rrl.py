from sim import *
from sim3 import find_rogue_pairs_at_S0
from collections import Counter
import sys

def test_seed(a1, length=4000, tail_frac=0.5):
    try:
        seq, Q, base_persist, canon_idx, F, S, S0 = analyze(a1, length, tail_frac, verbose=False)
        ep, ce, viol, rogue = find_rogue_pairs_at_S0(seq, Q, S0, base_persist, tail_frac)
    except Exception as e:
        print(f"a1={a1}: ERROR {e}")
        return
    if not rogue:
        return
    print(f"a1={a1} Q={sorted(Q)} S0={sorted(S0)} #rogue={len(rogue)}")
    seen = set()
    for (Ap,Bp,A,B) in rogue:
        key = (Ap,Bp)
        if key in seen: continue
        seen.add(key)
        m = None
        for i in range(len(seq)):
            if (P(seq[i]) & S0) == Bp:
                m = i
                break
        if m is None:
            continue
        Fprime = P(seq[m]) - S0
        flag = "MULTI" if len(Fprime)>=2 else "single"
        print(f"  [{flag}] A'={sorted(Ap)} B'={sorted(Bp)}  witness m={m+1} F'={sorted(Fprime)}")
        if len(Fprime)>=2:
            a_occ = [i for i in range(len(seq)) if (P(seq[i]) & S0)==Ap]
            b_occ = [i for i in range(len(seq)) if (P(seq[i]) & S0)==Bp]
            for q in sorted(Fprime):
                a_hit = sum(1 for i in a_occ if q in P(seq[i]))
                b_hit = sum(1 for i in b_occ if q in P(seq[i]))
                print(f"     q={q}: A' hit {a_hit}/{len(a_occ)}  B' hit {b_hit}/{len(b_occ)}")

if __name__ == "__main__":
    import itertools
    primes = [2,3,5,7,11,13,17,19,23]
    seeds = set()
    for k in range(2,5):
        for combo in itertools.combinations(primes, k):
            prod = 1
            for p in combo: prod*=p
            if prod < 5000:
                seeds.add(prod)
    # also some prime power / mixed
    for a1 in sorted(seeds):
        test_seed(a1, length=3000)
