from sim import *
from collections import Counter

def find_rogue_pairs_at_S0(seq, Q, S0, base_persist, tail_frac=0.5, min_count=3):
    ext_persist, ext_counts = extended_types(seq, S0, tail_frac, min_count)
    N0 = int(len(seq)*tail_frac)
    canon_ext = {}
    for i in range(N0, len(seq)):
        t = P(seq[i]) & Q
        if t in base_persist and t not in canon_ext:
            canon_ext[t] = P(seq[i]) & S0
    violations = []
    rogue = []
    for Ap in ext_persist:
        for Bp in ext_persist:
            if Ap == Bp: continue
            A = Ap & Q
            B = Bp & Q
            if A not in base_persist or B not in base_persist: continue
            if A == B: continue
            if len(A & B) != 0: continue
            if len(Ap & Bp) == 0:
                violations.append((Ap,Bp,A,B))
                Acan = canon_ext.get(A); Bcan = canon_ext.get(B)
                if Ap != Acan and Bp != Bcan:
                    rogue.append((Ap,Bp,A,B))
    return ext_persist, canon_ext, violations, rogue

seq, Q, base_persist, canon_idx, F, S, S0 = analyze(175, 6000)
print("=== Stage 0 (S0) ===")
ep0, ce0, v0, r0 = find_rogue_pairs_at_S0(seq, Q, S0, base_persist)
print("ext_persist count:", len(ep0))
print("violations:", len(v0), "rogue:", len(r0))
for r in r0: print("  ROGUE0:", sorted(r[0]), sorted(r[1]))

S0p = S0 | {13}
print("\n=== Stage 1 (S0 U {13}) ===")
ep1, ce1, v1, r1 = find_rogue_pairs_at_S0(seq, Q, S0p, base_persist)
print("ext_persist count:", len(ep1))
print("violations:", len(v1), "rogue:", len(r1))
for v in v1: print("  VIOL1:", sorted(v[0]), sorted(v[1]))
for r in r1: print("  ROGUE1:", sorted(r[0]), sorted(r[1]))
print("ext_persist types at stage1:")
for t in sorted(ep1, key=lambda x: sorted(x)):
    print("  ", sorted(t))
