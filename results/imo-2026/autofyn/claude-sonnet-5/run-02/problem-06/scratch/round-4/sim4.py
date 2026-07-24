from sim import *
from sim3 import find_rogue_pairs_at_S0
from sim2 import recruit
from collections import Counter
import sys

def process(a1, length=4000, max_rounds=6, tail_frac=0.5):
    seq, Q, base_persist, canon_idx, F, S, S0init = analyze(a1, length, tail_frac, verbose=False)
    S0 = set(S0init)
    print(f"a1={a1} Q={sorted(Q)} base_persist={[sorted(t) for t in base_persist]} S0_init={sorted(S0)}")
    for round_i in range(max_rounds):
        ep, ce, viol, rogue = find_rogue_pairs_at_S0(seq, Q, S0, base_persist, tail_frac)
        print(f"  round {round_i}: |S0|={len(S0)} S0={sorted(S0)} #ext_persist={len(ep)} #violations={len(viol)} #rogue={len(rogue)}")
        if not rogue:
            print("  -> V=0, process halted (converged)")
            return round_i, True
        Ap, Bp, A, B = rogue[0]
        c, occ = recruit(seq, S0, frozenset(Ap), frozenset(Bp), tail_frac)
        if not c:
            print("  -> STUCK: no recruit candidate found")
            return round_i, False
        q = c.most_common(1)[0][0]
        frac = c[q]/occ if occ else 0
        print(f"     recruiting q={q} (matches {c[q]}/{occ} = {frac:.2f} of occurrences of {sorted(Ap)}) from rogue pair ({sorted(Ap)},{sorted(Bp)})")
        S0 = S0 | {q}
    print("  -> max rounds reached without convergence")
    return max_rounds, False

if __name__ == "__main__":
    seeds = [int(x) for x in sys.argv[1:]] if len(sys.argv)>1 else [175]
    for a1 in seeds:
        process(a1)
        print()
