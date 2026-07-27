import math
from itertools import combinations
from collections import defaultdict
from functools import lru_cache

def primes(n):
    sieve=[True]*(n+1); sieve[0]=sieve[1]=False
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i,n+1,i): sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]]

PSET=set(primes(10**6))
def factor(m):
    f=set(); n=m; d=2
    while d*d<=n:
        while n%d==0: f.add(d); n//=d
        d+=1
    if n>1: f.add(n)
    return f

def minimal_supports(F):  # F = list of frozensets
    F=[s for s in F if s]
    mins=[]
    for i,s in enumerate(F):
        dominated=False
        for j,t in enumerate(F):
            if i!=j and t<=s and t<s: # proper subset => s not minimal
                # s dominated by t if t subset s and (t<s or t==s with j<i)
                dominated=True;break
        if not dominated:
            mins.append(s)
    # proper minimals: no other is a proper subset
    res=[]
    for i,s in enumerate(F):
        if not any(F[j]<s for j in range(len(F)) if j!=i):
            res.append(s)
    return res

def gen_sequence(a1, max_terms=400, cap=10**7):
    a=[a1]; F=[frozenset(factor(a1))]
    Mn=[F[0]]
    promo_log=[]
    while len(a)<max_terms:
        an=a[-1]; Mn_cur=Mn
        # find smallest m>an whose prime set hits every M in Mn_cur
        m=an+1
        while m<=cap:
            Pm=frozenset(factor(m))
            if all(Pm & M for M in Mn_cur):
                break
            m+=1
        if m>cap: break
        # promotion?
        Pm=frozenset(factor(m))
        # is Pm dominated by some member?
        dominated = any(M <= Pm for M in Mn_cur)
        new_Mn = Mn_cur[:]
        if not dominated:
            # add Pm, remove supersets
            new_Mn=[M for M in Mn_cur if not (Pm < M)]
            new_Mn.append(Pm)
            # classify
            refines = [M for M in Mn_cur if Pm < M]  # Pm proper subset of M
            incomparable = (len(refines)==0)
            promo_log.append((len(a)+1, m, set(Pm), 'refine' if refines else 'incomp', len(new_Mn)))
        a.append(m); Mn=new_Mn
    return a, Mn, promo_log

if __name__=='__main__':
    for a1 in [15,35,77,105,143,175,323,385,429,1001,1155,1365,2145,5005,91,195,4199]:
        a,Mn,pl=gen_sequence(a1,300)
        if not pl:
            print(f"a1={a1}: no promotions (freeze?) terms={len(a)} finalM={Mn}")
            continue
        # sizes of minimals ever
        sizes=[len(s) for (_,_,s,_,_) in pl]
        maxsz=max(sizes) if sizes else 0
        # refinement vs incomparable counts
        nref=sum(1 for p in pl if p[3]=='refine')
        ninc=sum(1 for p in pl if p[3]=='incomp')
        # primes entering
        allprimes=set()
        for _,_,s,_,_ in pl: allprimes|=s
        Pa1=factor(a1)
        entering=allprimes-set(Pa1)
        print(f"a1={a1}: terms={len(a)} #promo={len(pl)} ref={nref} inc={ninc} maxminsz={maxsz} Pa1={sorted(Pa1)} entering={sorted(entering)} final|M|={len(Mn)}")
        # show promotion sequence types
        types=[p[3][0] for p in pl]
        print("   types:", "".join(types))
