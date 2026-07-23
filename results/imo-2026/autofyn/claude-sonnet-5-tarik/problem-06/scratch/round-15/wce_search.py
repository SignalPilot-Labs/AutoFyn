import sys, itertools
from gen import gen_sequence

def analyze(a1, N):
    terms, radicals = gen_sequence(a1, N)
    P1 = radicals[0]
    core_members = {}
    for idx, rs in enumerate(radicals):
        n = idx+1
        S = rs & P1
        comp = rs - P1
        core_members.setdefault(S, []).append((n, comp))
    return P1, core_members

def succeeds(R_S_comps, R_Sp_comps):
    # R_S_comps: list of comp-sets for chosen S-side witnesses
    # R_Sp_comps: list of comp-sets for chosen S'-side witnesses
    W = set()
    for c in R_S_comps: W |= c
    for c in R_Sp_comps: W |= c
    W = sorted(W)
    if len(W) > 20:
        return None  # too big to brute force safely
    all_subsets = []
    for r in range(len(W)+1):
        for combo in itertools.combinations(W, r):
            all_subsets.append(frozenset(combo))
    def in_TS(tau):
        return all(tau & rho for rho in R_Sp_comps)
    def in_TSp(taup):
        return all(taup & rho for rho in R_S_comps)
    TS = [t for t in all_subsets if in_TS(t)]
    TSp = [t for t in all_subsets if in_TSp(t)]
    for t in TS:
        for tp in TSp:
            if not (t & tp):
                return False
    return True

def find_witness_collection(compsS, compsSp, max_pool=12, max_size=3):
    # compsS, compsSp: lists of (n, comp) for the two classes, already sorted by n (low index first)
    poolS = [c for n,c in compsS[:max_pool]]
    poolSp = [c for n,c in compsSp[:max_pool]]
    # dedupe identical comp sets, keep small pool distinct
    for r1 in range(1, max_size+1):
        for r2 in range(1, max_size+1):
            for combo1 in itertools.combinations(range(len(poolS)), r1):
                RS = [poolS[i] for i in combo1]
                for combo2 in itertools.combinations(range(len(poolSp)), r2):
                    RSp = [poolSp[i] for i in combo2]
                    res = succeeds(RS, RSp)
                    if res:
                        return (r1, r2, RS, RSp)
    return None

def test_a1(a1, N, max_pool=12, max_size=3, verbose=True):
    P1, core_members = analyze(a1, N)
    proper_cores = [S for S in core_members if S and S != P1]
    total = 0
    closed = 0
    results = []
    seen_pairs = set()
    for S in proper_cores:
        for Sp in proper_cores:
            if S==Sp or (S&Sp): continue
            pair = frozenset([S,Sp])
            if pair in seen_pairs: continue
            seen_pairs.add(pair)
            total += 1
            r = find_witness_collection(core_members[S], core_members[Sp], max_pool, max_size)
            if r:
                closed += 1
            results.append((sorted(S), sorted(Sp), r is not None, r))
    if verbose:
        print(f"a_1={a1} P_1={sorted(P1)} N={N}: {closed}/{total} pairs closed by search (pool<= {max_pool}, |R|<= {max_size} per side)")
        for S,Sp,ok,r in results:
            tag = "OK" if ok else "FAIL"
            detail = f"r1={r[0]},r2={r[1]}" if r else ""
            print(f"   [{tag}] {S} vs {Sp}  {detail}")
    return results

if __name__=="__main__":
    a1=int(sys.argv[1]); N=int(sys.argv[2])
    mp = int(sys.argv[3]) if len(sys.argv)>3 else 12
    ms = int(sys.argv[4]) if len(sys.argv)>4 else 3
    test_a1(a1,N,mp,ms)
