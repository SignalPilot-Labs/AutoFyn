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
    W = set()
    for c in R_S_comps: W |= c
    for c in R_Sp_comps: W |= c
    W = sorted(W)
    if len(W) > 18:
        return None
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

def dedup_pool(members, max_pool):
    comps = [c for n,c in members]
    seen = []
    seenset = set()
    for c in sorted(comps, key=len):
        if c not in seenset:
            seenset.add(c)
            seen.append(c)
        if len(seen) >= max_pool:
            break
    return seen

def find_witness_collection(membersS, membersSp, max_pool=15, max_size=4):
    poolS = dedup_pool(membersS, max_pool)
    poolSp = dedup_pool(membersSp, max_pool)
    for r1 in range(1, max_size+1):
        for r2 in range(1, max_size+1):
            for combo1 in itertools.combinations(range(len(poolS)), r1):
                RS = [poolS[i] for i in combo1]
                for combo2 in itertools.combinations(range(len(poolSp)), r2):
                    RSp = [poolSp[i] for i in combo2]
                    res = succeeds(RS, RSp)
                    if res:
                        return (r1, r2, [sorted(x) for x in RS], [sorted(x) for x in RSp])
    return None

def test_a1(a1, N, max_pool=15, max_size=4, verbose=True):
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
        print(f"a_1={a1} P_1={sorted(P1)} N={N}: {closed}/{total} pairs closed (dedup pool<={max_pool}, |R|<={max_size}/side)")
        for S,Sp,ok,r in results:
            tag = "OK" if ok else "FAIL"
            print(f"   [{tag}] {S} vs {Sp}  {r}")
    return results

if __name__=="__main__":
    a1=int(sys.argv[1]); N=int(sys.argv[2])
    mp = int(sys.argv[3]) if len(sys.argv)>3 else 15
    ms = int(sys.argv[4]) if len(sys.argv)>4 else 4
    test_a1(a1,N,mp,ms)
