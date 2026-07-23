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

def test_pair(a1, N, verbose=True):
    P1, core_members = analyze(a1, N)
    proper_cores = [S for S in core_members if S and S != P1]
    stats = {}
    for S in proper_cores:
        members = core_members[S]
        comps = [c for (n,c) in members]
        singleton_primes = set(next(iter(c)) for c in comps if len(c)==1)
        min_size = min(len(c) for c in comps)
        stats[S] = dict(comps=comps, singleton_primes=singleton_primes, min_size=min_size, count=len(members))
    pairs = []
    for S in proper_cores:
        for Sp in proper_cores:
            if S == Sp or (S & Sp): pairs.append(None)
    total_pairs=set()
    ok_msf=set()
    ok_msf_detail = {}
    for S in proper_cores:
        for Sp in proper_cores:
            if S==Sp or (S&Sp): continue
            pair = frozenset([S,Sp])
            if pair in total_pairs: continue
            total_pairs.add(pair)
            # direction 1: singletons from Sp cover some comp c in S
            avail_sp = stats[Sp]['singleton_primes']
            best1 = None
            for c in stats[S]['comps']:
                if c.issubset(avail_sp):
                    if best1 is None or len(c) < len(best1): best1 = c
            avail_s = stats[S]['singleton_primes']
            best2 = None
            for c in stats[Sp]['comps']:
                if c.issubset(avail_s):
                    if best2 is None or len(c) < len(best2): best2 = c
            if best1 is not None or best2 is not None:
                ok_msf.add(pair)
                ok_msf_detail[pair] = (best1, best2)
    if verbose:
        print(f"a_1={a1} P_1={sorted(P1)} N={N}")
        for S in proper_cores:
            print(f"   core {sorted(S)} count={stats[S]['count']} minsize={stats[S]['min_size']} singleton_primes={sorted(stats[S]['singleton_primes'])}")
        print(f"   MSF-closable pairs: {len(ok_msf)}/{len(total_pairs)}")
        for pair in total_pairs:
            tag = "OK" if pair in ok_msf else "NO"
            Slist = [sorted(x) for x in pair]
            print(f"     [{tag}] pair={Slist}  detail={ok_msf_detail.get(pair)}")
    return stats, ok_msf, total_pairs

if __name__=="__main__":
    a1=int(sys.argv[1]); N=int(sys.argv[2])
    test_pair(a1,N)
