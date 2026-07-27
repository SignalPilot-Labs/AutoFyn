import sympy
from sympy import factorint
from itertools import combinations

def P(m): return frozenset(factorint(m).keys())

def minimal_family_dedup(Fn):
    mins=[]
    for S in Fn:
        if any((T<S) for T in Fn if T!=S): continue
        mins.append(S)
    out=[]
    for S in mins:
        if S not in out: out.append(S)
    return out

def greedy_seq(a1,max_terms=200):
    a=[a1];F=[P(a1)];recs=[];n=1
    while n<max_terms:
        Mn=minimal_family_dedup(F)
        recs.append({'n':n,'M_n':[frozenset(s) for s in Mn]})
        m=a[-1]+1
        while True:
            pm=P(m)
            if all(pm&Pa for Pa in F): break
            m+=1
        a.append(m);F.append(P(m));n+=1
    return a,recs

# Are minimals pairwise-intersecting? (pstar §5.3 relies on this)
print("=== are M_n minimals pairwise-intersecting? ===")
for s in [15,35,175,429,273,323,385,4199]:
    a,r=greedy_seq(s,150)
    viol=0
    for x in r:
        Mn=x['M_n']
        for i in range(len(Mn)):
            for j in range(i+1,len(Mn)):
                if not (Mn[i]&Mn[j]):
                    viol+=1
                    if viol<=2: print(f"  seed {s} n={x['n']}: disjoint minimals {set(Mn[i])},{set(Mn[j])}")
    print(f"  seed {s}: pairwise-intersecting violations={viol}")

# Verify pstar §5.3 claim: every straggler contains all of Cov
print("\n=== straggler contains all of Cov? ===")
for s in [15,35,175,429,323,385,4199]:
    a,r=greedy_seq(s,150)
    P1=P(s)
    viol=0
    for x in r:
        Mn=x['M_n']
        cov=set()
        for M in Mn:
            if 2 in M and len(M)==2:
                q=list(M-{2})
                if q[0] in P1: cov.add(q[0])
        # stragglers: minimals not containing 2
        stragglers=[M for M in Mn if 2 not in M]
        for Sg in stragglers:
            if not cov <= Sg:
                viol+=1
                if viol<=2: print(f"  seed {s} n={x['n']}: straggler {set(Sg)} does NOT contain Cov={cov}")
    print(f"  seed {s}: straggler⊇Cov violations={viol}")
