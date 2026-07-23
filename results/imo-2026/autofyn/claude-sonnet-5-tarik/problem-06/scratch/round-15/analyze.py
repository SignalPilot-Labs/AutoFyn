import sys, math, itertools
from gen import gen_sequence

def analyze(a1, N):
    terms, radicals = gen_sequence(a1, N)
    P1 = radicals[0]  # rad(a1)
    # per-core index lists (1-indexed positions -> use 0-indexed here, report n=i+1)
    core_members = {}  # core (frozenset subset of P1) -> list of (n, comp_frozenset)
    for idx, rs in enumerate(radicals):
        n = idx+1
        S = rs & P1
        comp = rs - P1
        core_members.setdefault(S, []).append((n, comp))
    return P1, core_members, terms

def report(a1, N):
    P1, core_members, terms = analyze(a1, N)
    print(f"=== a_1={a1}  P_1={sorted(P1)}  (|P_1|={len(P1)})  N={N}  last={terms[-1]} ===")
    proper_cores = [S for S in core_members if S and S != P1]
    # stats per proper core
    stats = {}
    for S in sorted(proper_cores, key=lambda s: sorted(s)):
        members = core_members[S]
        sizes = [len(c) for (n,c) in members]
        singles = [ (n, next(iter(c))) for (n,c) in members if len(c)==1 ]
        distinct_singleton_primes = sorted(set(q for _,q in singles))
        stats[S] = dict(count=len(members), minsize=min(sizes) if sizes else None,
                         n_le2=sum(1 for s in sizes if s<=2),
                         n_singles=len(singles),
                         distinct_singleton_primes=distinct_singleton_primes,
                         first_idx = members[0][0], first_comp = members[0][1])
        print(f"  core {sorted(S)!s:12} count={len(members):6d} minsize={min(sizes) if sizes else None} "
              f"#(<=2)={stats[S]['n_le2']:5d} #singles={len(singles):5d} distinct_single_primes={distinct_singleton_primes} "
              f"first_idx={stats[S]['first_idx']} first_comp={sorted(stats[S]['first_comp'])}")
    # now test FWSM-style conjecture for every disjoint pair
    print("  -- disjoint pair FWSM test --")
    all_cores = list(proper_cores)
    results = []
    for S in all_cores:
        for Sp in all_cores:
            if S==Sp or (S & Sp): continue
            # try direction: j0 in S (first occurrence), singleton match search in Sp
            j0_n, Q = stats[S]['first_idx'], stats[S]['first_comp']
            avail = stats[Sp]['distinct_singleton_primes']
            covered = Q.issubset(set(avail))
            results.append((tuple(sorted(S)), tuple(sorted(Sp)), 'S->Sp(fixed j0 in S, singles in Sp)', sorted(Q), avail, covered))
    for r in results:
        tag = "OK" if r[-1] else "no"
        print(f"    [{tag}] S={r[0]} S'={r[1]}  j0.comp(Q)={r[3]}  singleton-primes-avail-in-S'={r[4]}")
    ok_pairs = set()
    for S in all_cores:
        for Sp in all_cores:
            if S==Sp or (S&Sp): continue
            # unordered pair check: succeeds if EITHER direction covered
            j0_n, Q = stats[S]['first_idx'], stats[S]['first_comp']
            avail = set(stats[Sp]['distinct_singleton_primes'])
            dir1 = Q.issubset(avail)
            j0_n2, Q2 = stats[Sp]['first_idx'], stats[Sp]['first_comp']
            avail2 = set(stats[S]['distinct_singleton_primes'])
            dir2 = Q2.issubset(avail2)
            pair = frozenset([S,Sp])
            if dir1 or dir2:
                ok_pairs.add(pair)
    total_pairs = set()
    for S in all_cores:
        for Sp in all_cores:
            if S==Sp or (S&Sp): continue
            total_pairs.add(frozenset([S,Sp]))
    print(f"  SUMMARY: {len(ok_pairs)}/{len(total_pairs)} disjoint pairs closed by first-witness-singleton-match (either direction)")
    return stats, ok_pairs, total_pairs

if __name__=="__main__":
    a1 = int(sys.argv[1]); N = int(sys.argv[2])
    report(a1, N)
