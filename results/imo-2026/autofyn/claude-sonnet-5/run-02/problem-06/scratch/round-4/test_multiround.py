from sim import *
from sim3 import find_rogue_pairs_at_S0
from sim2 import recruit
from collections import Counter

a1 = 247
seq, Q, base_persist, canon_idx, F, S, S0init = analyze(a1, 4000, 0.5, verbose=False)
S0 = set(S0init)
print("S0 init:", sorted(S0))

for round_i in range(3):
    ep, ce, viol, rogue = find_rogue_pairs_at_S0(seq, Q, S0, base_persist, 0.5)
    print(f"round {round_i}: S0={sorted(S0)} #rogue={len(rogue)}")
    if not rogue:
        break
    Ap, Bp, A, B = rogue[0]
    # earliest witness of Bp over WHOLE sequence
    m = None
    for i in range(len(seq)):
        if (P(seq[i]) & S0) == Bp:
            m = i; break
    Fprime = P(seq[m]) - S0
    print(f"  rogue A'={sorted(Ap)} B'={sorted(Bp)} witness m={m+1} a_m={seq[m]} F'={sorted(Fprime)}")
    for q in sorted(Fprime):
        a_occ = [i for i in range(len(seq)) if (P(seq[i]) & S0)==Ap]
        b_occ = [i for i in range(len(seq)) if (P(seq[i]) & S0)==Bp]
        a_hit = sum(1 for i in a_occ if q in P(seq[i]))
        b_hit = sum(1 for i in b_occ if q in P(seq[i]))
        print(f"    q={q}: A' hit {a_hit}/{len(a_occ)}   B' hit {b_hit}/{len(b_occ)}")
    S0 = S0 | {sorted(Fprime)[0]}
