import sympy
from sympy import factorint
from itertools import combinations

def P(m):
    return frozenset(factorint(m).keys())

def minimal_family_dedup(Fn):
    mins=[]
    for S in Fn:
        if any((T<S) for T in Fn if T!=S): continue
        mins.append(S)
    out=[]
    for S in mins:
        if S not in out: out.append(S)
    return out

def compute_mtp(Mn,Pess):
    plist=sorted(Pess); n=len(plist)
    if n>18: return (None,None)
    best=None;bestT=None
    for k in range(1,n+1):
        for combo in combinations(range(n),k):
            T=frozenset(plist[i] for i in combo)
            if all(T&Mm for Mm in Mn):
                prod=1
                for p in T: prod*=p
                if best is None or prod<best: best=prod;bestT=T
    return (best,bestT)

def greedy_seq(a1,max_terms=200):
    a=[a1];F=[P(a1)];recs=[];n=1
    while n<max_terms:
        Mn=minimal_family_dedup(F)
        Pess=set()
        for S in Mn: Pess|=set(S)
        Pess=sorted(Pess)
        mtp,wit=compute_mtp(Mn,Pess)
        m=a[-1]+1
        while True:
            pm=P(m)
            if all(pm&Pa for Pa in F): break
            m+=1
        Fn2=F+[P(m)];Mn2=minimal_family_dedup(Fn2)
        is_promo=(frozenset(P(m)) in Mn2) and (frozenset(P(m)) not in Mn)
        if mtp:
            mu=((a[-1]//mtp)+1)*mtp
            eq=(m==mu)
        else: eq=None
        recs.append({'n':n,'a_n':a[-1],'M_n':[frozenset(s) for s in Mn],'witness':frozenset(wit) if wit else None,'mtp':mtp,'a_next':m,'Pnext':frozenset(P(m)),'is_promo':is_promo,'eq':eq})
        a.append(m);F.append(P(m));n+=1
    return a,recs

# Verify: at an equality-promotion, witness T* is a transversal of M_n but NOT a member of M_n
# (so P(a_{n+1}) ⊇ T* does NOT dominate => genuine new minimal)
print("=== equality-promotion: T* not a member of M_n ===")
for s in [15,35,175,429]:
    a,r=greedy_seq(s,120)
    found=0
    for x in r:
        if x['is_promo'] and x['eq']==True and x['witness'] is not None:
            T=x['witness']
            is_member = T in x['M_n']
            Pnext=x['Pnext']
            contains_T = T <= Pnext
            print(f"  seed {s} n={x['n']}: eq-promo, witness={set(T)}, is_member_of_Mn? {is_member}, T⊆P(a_next)? {contains_T}")
            found+=1
            if found>=2: break
    if found==0:
        print(f"  seed {s}: no equality-promotion found in window")

# Verify {2,97} obstruction: pairwise-intersecting antichain, SPT holds, P_ess unbounded
print("\n=== {2,q} obstruction check ===")
fam=[frozenset({2,q}) for q in [5,7,11,13,97,101]]
# pairwise intersecting?
pi=all(len(a&b)>0 for i,a in enumerate(fam) for b in fam[i+1:])
print("pairwise-intersecting?",pi)
# antichain?
ac=all(not(a<b) and not(b<a) for i,a in enumerate(fam) for b in fam[i+1:])
print("antichain?",ac)
# SPT with p*=3: min(M)<=3 for all M
print("min(M)<=3 for all?",all(min(M)<=3 for M in fam))
# P_ess unbounded
Pess=set()
for M in fam: Pess|=M
print("P_ess=",sorted(Pess),"(unbounded as q->inf)")
# W1 check: witness (cheapest transversal) carries small prime?
mtp,wit=compute_mtp(fam,Pess)
print("mtp=",mtp,"witness=",set(wit) if wit else None,"carries <=3?", wit and any(p<=3 for p in wit))

# Verify W1-doesn't-bound-product: T*={5,97} with p*=5, product 485 > primorial(5)=30
print("\n=== W1 does not bound product (Prop 2.2) ===")
print("T*={5,97}, p*=5, product=",5*97,", primorial(5)=",2*3*5)
print("W1 satisfied (5<=5)? yes; product>primorial? yes")
