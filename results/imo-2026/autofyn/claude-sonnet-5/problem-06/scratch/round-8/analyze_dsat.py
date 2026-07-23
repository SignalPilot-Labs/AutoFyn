import json, sys
from sympy import factorint

def rad(x, cache={}):
    r = cache.get(x)
    if r is None:
        r = frozenset(factorint(x).keys())
        cache[x] = r
    return r

def analyze_core(a1, seq, S):
    P1 = rad(a1)
    n = len(seq)
    RAD = [None] + [rad(x) for x in seq]
    G = [None] + [RAD[i] & P1 for i in range(1, n+1)]
    COMP = [None] + [RAD[i] - P1 for i in range(1, n+1)]
    I_S = [i for i in range(1, n+1) if G[i] == S]
    J_S = [i for i in range(1, n+1) if RAD[i] & S == frozenset()]
    if not I_S or not J_S:
        return {"S": sorted(S), "error": "empty I_S or J_S", "I_S": len(I_S), "J_S": len(J_S)}
    # D_S = intersection of RAD[j] over j in J_S (stabilized proxy using all available data)
    D = None
    for j in J_S:
        D = RAD[j] if D is None else (D & RAD[j])
    D_minus_P1 = D - P1
    # find witnesses (any index disjoint from S, i.e. in J_S) with nonempty comp, for coarsening
    witnesses = [j for j in J_S if len(COMP[j]) > 0]
    pair = None
    for a_ in range(len(witnesses)):
        for b_ in range(a_+1, len(witnesses)):
            j1, j2 = witnesses[a_], witnesses[b_]
            if COMP[j1] & COMP[j2] == frozenset():
                pair = (j1, j2)
                break
        if pair:
            break
    realized_radicals = set(RAD[i] for i in I_S)
    result = {"S": sorted(S), "I_S_count": len(I_S), "J_S_count": len(J_S),
              "D_minus_P1": sorted(D_minus_P1)}
    if pair is None:
        result["error"] = "no disjoint witness pair found"
        return result
    j1, j2 = pair
    c1, c2 = COMP[j1], COMP[j2]
    buckets = [frozenset({p, q}) for p in c1 for q in c2]
    result["j1"] = j1; result["j2"] = j2
    result["comp_j1"] = sorted(c1); result["comp_j2"] = sorted(c2)
    bucket_results = []
    for b in buckets:
        kappa = S | b
        exact_realized = kappa in realized_radicals
        first_block = None
        for j3 in range(1, n+1):
            if RAD[j3] & kappa == frozenset():
                first_block = j3
                break
        supersets = [r for r in realized_radicals if kappa <= r]
        min_extra = None; min_dominator = None
        if supersets:
            best = min(supersets, key=lambda r: len(r))
            min_extra = len(best) - len(kappa)
            min_dominator = best
        predicted = kappa | D_minus_P1
        match = None
        if min_dominator is not None:
            match = (frozenset(min_dominator) == frozenset(predicted))
        bucket_results.append({
            "bucket": sorted(b), "kappa": sorted(kappa),
            "exact_realized": exact_realized,
            "first_block_witness": first_block,
            "min_extra_primes": min_extra,
            "min_dominator": sorted(min_dominator) if min_dominator else None,
            "predicted_dominator_via_DS": sorted(predicted),
            "DS_saturation_matches": match,
            "predicted_extra": len(predicted - kappa),
        })
    result["buckets"] = bucket_results
    return result

if __name__ == "__main__":
    a1 = int(sys.argv[1])
    path = sys.argv[2]
    S = frozenset(int(x) for x in sys.argv[3].split(","))
    seq = json.load(open(path))
    out = analyze_core(a1, seq, S)
    print(json.dumps(out, indent=1, default=str))
