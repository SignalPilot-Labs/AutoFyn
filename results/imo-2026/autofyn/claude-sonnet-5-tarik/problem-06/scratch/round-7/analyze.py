import sys, itertools
from gen import generate

def analyze(a1, N, min_IS=1, verbose=True):
    a, radset0 = generate(a1, N)
    radset = [None] + [frozenset(s) for s in radset0[1:]]
    P1 = radset[1]
    k = len(P1)
    print(f"a_1={a1}, P_1={sorted(P1)}, k={k}, N={N}")
    results = {}
    subsets = []
    Plist = sorted(P1)
    for r in range(1, k):  # proper nonempty subsets
        for combo in itertools.combinations(Plist, r):
            subsets.append(frozenset(combo))
    for S in subsets:
        I_S = [i for i in range(1, N+1) if (radset[i] & P1) == S]
        if len(I_S) < min_IS:
            continue
        J_S = [j for j in range(1, N+1) if (radset[j] & S) == frozenset()]
        if not J_S:
            continue
        # D_S = intersection of radset[j] for j in J_S  (predicted bound for single companions)
        D_S = None
        for j in J_S:
            D_S = radset[j] if D_S is None else (D_S & radset[j])
        # fresh / ever-minimal values within I_S (restricted antichain dynamics)
        antichain = []  # list of frozensets
        ever_minimal = set()
        for i in I_S:
            C = radset[i]
            # is C dominated by (i.e. superset of) something already in antichain? then not minimal (not added fresh)
            dominated = any(m <= C for m in antichain)  # existing m subset-or-equal of C
            if not dominated:
                ever_minimal.add(C)
                # remove existing antichain elements that are strict supersets of C
                antichain = [m for m in antichain if not (C < m)]
                antichain.append(C)
        results[S] = dict(I_S=I_S, J_S=J_S, D_S=D_S, ever_minimal=ever_minimal, final_antichain=set(antichain))
    return a, radset, P1, results

def report(a1, N, min_IS=1, show_all=False, max_print=30):
    a, radset, P1, results = analyze(a1, N, min_IS)
    for S, d in results.items():
        bundles = []
        for C in d['ever_minimal']:
            Q = C - S
            bundles.append((len(Q), sorted(Q), C in d['final_antichain']))
        bundles.sort()
        multi = [b for b in bundles if b[0] >= 2]
        if not multi:
            continue
        DminusP1 = d['D_S'] - P1
        print(f"\n=== S={sorted(S)}  |I_S|={len(d['I_S'])}  |J_S|={len(d['J_S'])}  D_S\\P1={sorted(DminusP1)} ===")
        print(f"  total ever-minimal values: {len(bundles)}, of which multi-companion (|Q|>=2): {len(multi)}")
        with_d = [b for b in multi if any(q in DminusP1 for q in b[1])]
        without_d = [b for b in multi if not any(q in DminusP1 for q in b[1])]
        alive_multi = [b for b in multi if b[2]]
        alive_multi_without_d = [b for b in alive_multi if not any(q in DminusP1 for q in b[1])]
        print(f"  multi-bundles containing a D_S prime: {len(with_d)} / {len(multi)}")
        print(f"  multi-bundles WITHOUT any D_S prime:  {len(without_d)} / {len(multi)}")
        print(f"  multi-bundles ALIVE in final antichain: {len(alive_multi)} (of which WITHOUT D_S prime: {len(alive_multi_without_d)})")
        if without_d:
            print(f"  sample of multi-bundles without D_S prime (up to {max_print}):")
            for sz, Q, alive in without_d[:max_print]:
                tag = "ALIVE(final)" if alive else "dominated-later"
                print(f"    size {sz}: {Q} [{tag}]")
        if show_all:
            for sz, Q, alive in bundles[:max_print]:
                tag = "ALIVE(final)" if alive else "dominated-later"
                marker = "  <-- has D_S prime" if any(q in DminusP1 for q in Q) else ""
                print(f"    bundle size {sz}: companions={Q}  [{tag}]{marker}")
    return a, radset, P1, results

if __name__ == "__main__":
    a1 = int(sys.argv[1])
    N = int(sys.argv[2])
    min_IS = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    report(a1, N, min_IS)
