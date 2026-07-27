import sympy
from sympy import factorint
from itertools import combinations

def P(m):
    return frozenset(factorint(m).keys())

def minimal_family_dedup(Fn):
    mins = []
    for S in Fn:
        if any((T < S) for T in Fn if T != S):
            continue
        mins.append(S)
    out = []
    for S in mins:
        if S not in out:
            out.append(S)
    return out

def compute_mtp(Mn, Pess):
    plist = sorted(Pess)
    n = len(plist)
    if n > 18:
        return (None, None)
    best = None; bestT = None
    for k in range(1, n+1):
        for combo in combinations(range(n), k):
            T = frozenset(plist[i] for i in combo)
            if all(T & Mm for Mm in Mn):
                prod = 1
                for p in T: prod *= p
                if best is None or prod < best:
                    best = prod; bestT = T
    return (best, bestT)

def greedy_seq(a1, max_terms=400):
    a = [a1]; F = [P(a1)]; records = []
    n = 1
    while n < max_terms:
        Mn = minimal_family_dedup(F)
        Pess = set()
        for S in Mn: Pess |= set(S)
        Pess = sorted(Pess)
        mtp, witness = compute_mtp(Mn, Pess)
        if Mn:
            Cn = set(Mn[0])
            for S in Mn[1:]: Cn &= set(S)
        else: Cn = set()
        # find a_{n+1}
        m = a[-1]+1
        while True:
            pm = P(m)
            if all(pm & Pa for Pa in F): break
            m += 1
        # classify: promotion if P(m) is new minimal in F+[P(m)]
        Fn2 = F + [P(m)]
        Mn2 = minimal_family_dedup(Fn2)
        is_promo = (frozenset(P(m)) in Mn2) and (frozenset(P(m)) not in Mn)
        # equality vs strict-beat
        if mtp is not None:
            mu = ((a[-1]//mtp)+1)*mtp
            eq = (m == mu)
        else:
            eq = None
        records.append({'n':n,'a_n':a[-1],'M_n':[frozenset(s) for s in Mn],
            'M_n2':[frozenset(s) for s in Mn2],'Pess':set(Pess),'mtp':mtp,
            'witness':frozenset(witness) if witness else None,'C_n':frozenset(Cn),
            'a_next':m,'is_promo':is_promo,'eq':eq})
        a.append(m); F.append(P(m)); n += 1
    return a, records

# a1=175 terminal claimed Cov=emptyset
print("=== a1=175 terminal Cov ===")
a, recs = greedy_seq(175, 300)
last = recs[-1]
print("final M_n:", [set(s) for s in last['M_n']])
print("claimed: {{2,13,7},{3,7},{13,3,5},{2,3,5},{5,7}}")
P1 = P(175)
Cov = set()
for M in last['M_n']:
    if 2 in M and len(M)==2:
        q=list(M-{2})
        if q[0] in P1: Cov.add(q[0])
print("Cov(final)=",Cov,"P(a1)=",P1,"claimed Cov=emptyset")

# Verify Cov monotone + {2,p} persistence on 175 (regime S)
prev=set(); viol=0; persisted=set()
for r in recs:
    cov=set()
    for M in r['M_n']:
        if 2 in M and len(M)==2:
            q=list(M-{2})
            if q[0] in P1: cov.add(q[0])
    if cov < prev: viol+=1
    prev=cov
print("Cov monotone violations (175):", viol)
# {2,p} persistence: once {2,p} appears, does it stay?
import collections
twop_seen = collections.defaultdict(list) # p -> list of n where {2,p} in M_n
twop_vanished = []
for r in recs:
    cur = set()
    for M in r['M_n']:
        if 2 in M and len(M)==2: cur.add(list(M-{2})[0])
    for p in cur: twop_seen[p].append(r['n'])
# check gaps: for each p in twop_seen with p in P1, after first appearance, should be continuous
for p,ns in twop_seen.items():
    if p in P1:
        # check continuity from first to last
        first=ns[0]; lastn=ns[-1]
        present=set(ns)
        cont = all(i in present for i in range(first,lastn+1))
        if not cont: twop_vanished.append((p,first,lastn))
print("{2,p}-persistence violations (p in P1, after first appears, stays):", twop_vanished[:5])

# Core nonempty (GAP-A) check
core_empty=[r['n'] for r in recs if not any(2 in M for M in r['M_n'])]
print("GAP-A (core empty) events:", core_empty[:10])

# Equality vs strict-beat promotion counts across seeds
print("\n=== equality/strict-beat promotion counts ===")
seeds=[15,35,77,143,175,323,385,1001,4199,91,195,429,273,30,19549]
tot_eq=0; tot_sb=0; tot_promo=0
for s in seeds:
    try:
        a,r=greedy_seq(s,200)
        eq=sum(1 for x in r if x['is_promo'] and x['eq']==True)
        sb=sum(1 for x in r if x['is_promo'] and x['eq']==False)
        promo=sum(1 for x in r if x['is_promo'])
        tot_eq+=eq; tot_sb+=sb; tot_promo+=promo
    except Exception as e:
        print(f"seed {s} err: {e}")
print(f"total promotions={tot_promo}, equality={tot_eq}, strict-beat={tot_sb}")
print(f"claimed 344 promotions: 170 eq + 174 sb")
