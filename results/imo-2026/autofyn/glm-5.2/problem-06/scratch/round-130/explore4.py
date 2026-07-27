import math
from itertools import combinations
from collections import Counter

def factor(m):
    f=set(); n=m; d=2
    while d*d<=n:
        while n%d==0: f.add(d); n//=d
        d+=1
    if n>1: f.add(n)
    return f

def gen(a1, max_terms=1500, cap=10**8):
    a=[a1]; Mn=[frozenset(factor(a1))]
    promo=[]; straggler_history=[]; star_history=[]
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
            is_straggler = 2 not in Pm
            promo.append((len(a)+1,m,set(Pm),is_straggler, len(refines)))
            straggler_family=sorted([tuple(sorted(s)) for s in Mn if 2 not in s])
            straggler_history.append((len(a)+1, straggler_family))
        a.append(m)
    return a,Mn,promo,straggler_history

if __name__=='__main__':
    seeds=[15,35,77,91,105,143,175,195,323,385,429,1001,96577,25025,37961,62491,46189]
    for a1 in seeds:
        a,Mn,promo,sh=gen(a1,1500)
        # straggler family evolution: when does it stabilize?
        strag_steps=[p[0] for p in promo if p[3]]  # straggler promotions
        # straggler sizes ever
        strag_sizes=[]
        for _,sf in sh:
            for s in sf: strag_sizes.append(len(s))
        # final straggler family
        final_strag=sorted([tuple(sorted(s)) for s in Mn if 2 not in s])
        # when did straggler family last change?
        last_change=None
        prev=None
        for step,sf in sh:
            if sf!=prev:
                last_change=step; prev=sf
        Pa1=factor(a1)
        # is straggler subset of P(a1) in final?
        final_strag_primes=set().union(*[set(s) for s in final_strag]) if final_strag else set()
        print(f"a1={a1} |P(a1)|={len(Pa1)} #promo={len(promo)} #strag-promo={len(strag_steps)} strag_last_change_step={last_change}")
        print(f"  final straggler family ({len(final_strag)} members): {final_strag[:5]}{'...' if len(final_strag)>5 else ''}")
        print(f"  straggler size range: {min(strag_sizes) if strag_sizes else 0}-{max(strag_sizes) if strag_sizes else 0}")
        print(f"  final straggler primes: {sorted(final_strag_primes)}  entering_in_straggler: {sorted(final_strag_primes-set(Pa1))}")
        # verify: every straggler promotion refines a straggler (closed under refinement)
        closed=True
        # check at each straggler promo: does Pm refine only stragglers?
        # rebuild Mn tracking
        Mn2=[frozenset(factor(a1))]
        for p in promo:
            step,m,Pm,is_strag,refn=p
            Pm=frozenset(Pm)
            refines=[M for M in Mn2 if Pm<M]
            if refines:
                # check all refined are stragglers if Pm is straggler, etc.
                if is_strag:
                    # refined members should be stragglers (no 2)
                    for M in refines:
                        if 2 in M: closed=False
        print(f"  straggler-closed-under-refinement: {closed}")
        print()
