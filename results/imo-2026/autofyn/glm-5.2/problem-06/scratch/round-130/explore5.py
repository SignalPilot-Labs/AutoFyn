import math
from itertools import combinations

def factor(m):
    f=set(); n=m; d=2
    while d*d<=n:
        while n%d==0: f.add(d); n//=d
        d+=1
    if n>1: f.add(n)
    return f

def gen(a1, max_terms=1500, cap=10**8):
    a=[a1]; Mn=[frozenset(factor(a1))]
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
            Mn=[M for M in cur if not (Pm<M)]+[Pm]
        a.append(m)
    return a,Mn

def minimal_transversals(S):  # S = list of frozensets (straggler family)
    if not S: return [frozenset()]
    ground=sorted(set().union(*S))
    if len(ground)>18: return None
    res=[]
    for r in range(1,len(ground)+1):
        for Ss in combinations(ground,r):
            Ss=frozenset(Ss)
            if all(Ss & M for M in S):
                if not any(T<Ss for T in res):
                    res=[T for T in res if not (Ss<T)]
                    res.append(Ss)
    return res

def is_self_blocking(Mn):
    # every transversal contains a member
    ground=sorted(set().union(*Mn))
    if len(ground)>18: return None
    # check: exists a transversal avoiding all members (i.e. T hits all but no member subset of T)
    for r in range(1,len(ground)+1):
        for Ss in combinations(ground,r):
            Ss=frozenset(Ss)
            if all(Ss & M for M in Mn):
                if not any(M<=Ss for M in Mn):
                    return False  # avoiding transversal exists -> not self-blocking
    return True

if __name__=='__main__':
    for a1 in [15,35,77,91,105,143,175,195,323,385,429,1001,96577,25025,37961,62491,4199,46189]:
        a,Mn=gen(a1,1500)
        strag=[s for s in Mn if 2 not in s]
        star=[s for s in Mn if 2 in s]
        mt = minimal_transversals(strag) if strag else [frozenset()]
        # predicted clean star = {2} u T for T minimal transversal of strag
        predicted_star = set(frozenset({2}|set(T)) for T in mt) if mt is not None else None
        actual_star = set(star)
        # also: is star+straggler self-blocking?
        sb = is_self_blocking(Mn) if len(set().union(*Mn))<=18 else None
        Pa1=factor(a1)
        strag_primes=set().union(*strag) if strag else set()
        # is every actual star member a superset of some {2}uT?
        covers = all(any(({2}|set(T)) <= s for T in mt) for s in star) if mt else None
        print(f"a1={a1}: |Mn|={len(Mn)} |strag|={len(strag)} |star|={len(star)} #minTrans(strag)={len(mt) if mt else '?'} self_blocking={sb}")
        print(f"   strag_primes={sorted(strag_primes)} (entering: {sorted(strag_primes-set(Pa1))})")
        print(f"   predicted_clean_star({len(predicted_star) if predicted_star else '?'}) = {sorted([tuple(sorted(s)) for s in predicted_star])[:6] if predicted_star else '?'}")
        print(f"   actual_star (sample) = {sorted([tuple(sorted(s)) for s in actual_star])[:6]}")
        print(f"   every star member covers a clean {2}uT: {covers}")
        # equality: actual star == predicted? (only if no free-rider star members)
        eq = (predicted_star == actual_star) if predicted_star else None
        print(f"   star == predicted_clean (no free-rider star members): {eq}")
        print()
