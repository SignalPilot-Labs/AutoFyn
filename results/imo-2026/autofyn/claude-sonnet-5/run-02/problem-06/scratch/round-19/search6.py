from sim2 import simulate, factorize
import collections, sys

def check(a1, N, S0, min_occ=200):
    seq = simulate(a1, N)
    Q = factorize(a1)
    types = collections.defaultdict(list)
    outsig = {}
    for i,a in enumerate(seq):
        n=i+1
        f = factorize(a)
        rho = frozenset(f & S0)
        out = frozenset(f - S0)
        types[rho].append(n)
        outsig[n] = out
    persistent = {t:v for t,v in types.items() if len(v)>=min_occ and (t & Q)}
    keys = list(persistent.keys())
    nomatch=[]
    anymatch=0
    total=0
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            A,B = keys[i], keys[j]
            if (A&Q) & (B&Q): continue
            occA, occB = persistent[A], persistent[B]
            sigsA=[outsig[n] for n in occA]; sigsB=[outsig[n] for n in occB]
            singA=collections.Counter(next(iter(s)) for s in sigsA if len(s)==1)
            singB=collections.Counter(next(iter(s)) for s in sigsB if len(s)==1)
            if not singA or not singB: continue
            total+=1
            shared = set(singA)&set(singB)
            if shared:
                anymatch+=1
            else:
                nomatch.append((sorted(A),sorted(B),dict(singA),dict(singB)))
    return total, anymatch, nomatch

if __name__=="__main__":
    a1=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 15000
    Q = factorize(a1)
    S0 = set(Q) | {2,3,5,7,11,13}
    total, anymatch, nomatch = check(a1,N,S0)
    print(f"a1={a1}: {anymatch}/{total} pairs have SOME shared singleton prime (any, not just top)")
    for A,B,singA,singB in nomatch[:5]:
        print(f"  NOMATCH A={A} singA={singA} B={B} singB={singB}")
