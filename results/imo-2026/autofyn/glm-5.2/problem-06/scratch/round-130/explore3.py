import math
from itertools import combinations
from collections import defaultdict, Counter

def factor(m):
    f=set(); n=m; d=2
    while d*d<=n:
        while n%d==0: f.add(d); n//=d
        d+=1
    if n>1: f.add(n)
    return f

def minimal_transversals(Mn):
    # all minimal hitting sets of family Mn (list of frozensets)
    # transversal = set hitting every member; minimal under inclusion
    # brute force over subsets of ground set
    ground=sorted(set().union(*Mn))
    if len(ground)>16: return None
    mins=[]
    for r in range(1,len(ground)+1):
        for S in combinations(ground,r):
            Ss=set(S)
            if all(Ss & M for M in Mn):
                # minimal?
                if not any(set(T)<Ss for T in mins):
                    # remove supersets
                    mins=[T for T in mins if not (Ss < set(T))]
                    mins.append(Ss)
    return [set(s) for s in mins]

def gen(a1, max_terms=2000, cap=10**8):
    a=[a1]; Mn=[frozenset(factor(a1))]
    promo=[]
    while len(a)<max_terms:
        an=a[-1]; cur=Mn
        m=an+1
        while m<=cap:
            Pm=frozenset(factor(m))
            if all(Pm & M for M in cur): break
            m+=1
        if m>cap: break
        Pm=frozenset(factor(m))
        if not any(M<=Pm for M in cur):
            refines=[M for M in cur if Pm<M]
            newM=[M for M in cur if not (Pm<M)]+[Pm]
            Mn=newM
            promo.append((len(a)+1,m,set(Pm),'r' if refines else 'i'))
        a.append(m)
    return a,Mn,promo

if __name__=='__main__':
    # Examine the large transient family of 46189 and others
    for a1 in [46189, 37961, 96577, 62491, 25025]:
        a,Mn,promo=gen(a1,1500)
        # size distribution of minimals in final Mn
        sz=Counter(len(m) for m in Mn)
        # how many minimals contain 2?
        with2=sum(1 for m in Mn if 2 in m)
        Pa1=factor(a1)
        # {2,p} members for p in Pa1
        covey=[m for m in Mn if len(m)==2 and 2 in m and (m-{2})<=set(Pa1)]
        # distinct primes in final Mn
        primes_in_M=set().union(*Mn) if Mn else set()
        entering_final=primes_in_M-set(Pa1)
        print(f"a1={a1} |P(a1)|={len(Pa1)} Pa1={sorted(Pa1)}")
        print(f"  terms={len(a)} #promo={len(promo)} final|M|={len(Mn)} maxtransient|M|={max(len(p) for p in [Mn])}")
        print(f"  minimal size dist: {dict(sorted(sz.items()))}")
        print(f"  minimals-with-2: {with2}/{len(Mn)}  Cov{{2,p}},p in Pa1: {len(covey)}")
        print(f"  distinct primes in final Mn: {len(primes_in_M)} entering_final: {len(entering_final)} (max {max(entering_final) if entering_final else 0})")
        # show a few minimals
        print(f"  sample minimals: {sorted([tuple(sorted(s)) for s in Mn])[:8]}")
        # track |P_ess_n| over evolution (does it decrease? refueling)
        # sample promotion types
        types=''.join(p[3] for p in promo)
        print(f"  promo types: {types[:80]}...")
        print()
