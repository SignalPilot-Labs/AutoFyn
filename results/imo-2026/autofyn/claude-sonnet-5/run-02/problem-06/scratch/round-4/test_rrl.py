from sim import *
from sim3 import find_rogue_pairs_at_S0
from collections import Counter
import sys

def test_seed(a1, length=4000, tail_frac=0.5):
    seq, Q, base_persist, canon_idx, F, S, S0 = analyze(a1, length, tail_frac, verbose=False)
    ep, ce, viol, rogue = find_rogue_pairs_at_S0(seq, Q, S0, base_persist, tail_frac)
    print(f"a1={a1} Q={sorted(Q)} S0={sorted(S0)} #rogue={len(rogue)}")
    for (Ap,Bp,A,B) in rogue:
        # find earliest witness with ext type Bp (over WHOLE sequence, not just tail)
        m = None
        for i in range(len(seq)):
            if (P(seq[i]) & S0) == Bp:
                m = i
                break
        if m is None:
            continue
        Fprime = P(seq[m]) - S0
        print(f"  rogue pair A'={sorted(Ap)} B'={sorted(Bp)}  witness m={m+1} a_m={seq[m]} F'={sorted(Fprime)}")
        if len(Fprime) < 2:
            print("    (|F'|=1, uniform is forced trivially by Bounded Witness Lemma disjunction over singleton)")
        # check each candidate prime in F' against ALL occurrences of Ap and Bp (whole sequence, from m onward, and also from first occurrence of Ap/Bp)
        for q in sorted(Fprime):
            a_occ = [i for i in range(len(seq)) if (P(seq[i]) & S0)==Ap]
            b_occ = [i for i in range(len(seq)) if (P(seq[i]) & S0)==Bp]
            a_hit = sum(1 for i in a_occ if q in P(seq[i]))
            b_hit = sum(1 for i in b_occ if q in P(seq[i]))
            a_after_m = [i for i in a_occ if i> m]
            a_hit_after = sum(1 for i in a_after_m if q in P(seq[i]))
            print(f"    q={q}: A' occurrences total={len(a_occ)} hit={a_hit} (after witness: total={len(a_after_m)} hit={a_hit_after});  B' occurrences total={len(b_occ)} hit={b_hit}")

if __name__ == "__main__":
    seeds = [int(x) for x in sys.argv[1:]] if len(sys.argv)>1 else [175,35]
    for a1 in seeds:
        test_seed(a1)
        print()
