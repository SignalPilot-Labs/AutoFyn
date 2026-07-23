import sys
from sim import gen

def test(a1, M):
    terms, rads = gen(a1, M)
    P1 = rads[0]
    k = len(P1)
    imprint_classes = {}  # S(frozenset) -> list of indices
    for i in range(M):
        Gi = frozenset(rads[i] & P1)
        imprint_classes.setdefault(Gi, []).append(i)
    print(f"a1={a1} (P1={sorted(P1)}, k={k}), M={M}: #imprint classes used={len(imprint_classes)}")
    ext = {}
    for S, idxs in imprint_classes.items():
        if len(idxs) < 5:
            continue
        # compute stabilized intersection C_infty^S over these indices (within window)
        C = set(rads[idxs[0]])
        for i in idxs[1:]:
            C &= rads[i]
        ext[S] = C
        print(f"  class S={sorted(S)}: #members(in window)={len(idxs)}, extended C_infty^S (approx, window-limited)={sorted(C)}")
    # check pairwise overlaps of extended imprints for disjoint S,S'
    keys = list(ext.keys())
    for a in range(len(keys)):
        for b in range(a+1, len(keys)):
            S, Sp = keys[a], keys[b]
            if S & Sp:
                continue  # not disjoint imprints, skip (Lemma FX only concerns disjoint)
            overlap = ext[S] & ext[Sp]
            print(f"    disjoint pair S={sorted(S)}, S'={sorted(Sp)}: extended overlap = {sorted(overlap)}")

if __name__ == "__main__":
    for a1, M in [(247,4000, ), (4199,4000), (375,1500), (221,1500), (65,1500)]:
        test(a1, M)
