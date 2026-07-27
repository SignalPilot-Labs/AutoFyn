import sympy
from sympy import factorint
from itertools import combinations

def P(m):
    return frozenset(factorint(m).keys())

def greedy_seq(a1, max_terms=400):
    a = [a1]
    F = [P(a1)]
    records = []
    n = 1
    while n < max_terms:
        Fn = F[:]
        Mn = []
        for S in Fn:
            if not any((T < S) for T in Fn):
                Mn.append(S)
        Pess = set()
        for S in Mn:
            Pess |= set(S)
        Pess = sorted(Pess)
        mtp, witness = compute_mtp(Mn, Pess)
        if Mn:
            Cn = set(Mn[0])
            for S in Mn[1:]:
                Cn &= set(S)
        else:
            Cn = set()
        records.append({
            'n': n, 'a_n': a[-1], 'M_n': [frozenset(s) for s in Mn],
            'Pess': set(Pess), 'mtp': mtp, 'witness': frozenset(witness) if witness else None,
            'C_n': frozenset(Cn),
        })
        m = a[-1] + 1
        while True:
            pm = P(m)
            ok = all(pm & Pa for Pa in F)
            if ok:
                break
            m += 1
        a.append(m)
        F.append(P(m))
        n += 1
    return a, records

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

# Verify pstar Lemma C-ref: a1=35 terminal family { {2,3,7},{2,5},{3,5},{5,7} }, Cov={5}
print("=== pstar Lemma C-ref check: a1=35 ===")
a, recs = greedy_seq(35, max_terms=300)
# find terminal (last M_n)
last = recs[-1]
print("a1=35 final M_n:", [set(s) for s in last['M_n']])
print("claimed terminal: {{2,3,7},{2,5},{3,5},{5,7}}")
print("a_n range:", a[0], "...", a[-1])
# Check Cov = {p in P(a1): {2,p} in M_n}
P1 = P(35)
Cov_final = set()
for M in last['M_n']:
    if 2 in M and len(M)==2:
        q = list(M-{2})
        if q[0] in P1:
            Cov_final.add(q[0])
print("Cov(final) =", Cov_final, " P(a1)=", P1, " claimed Cov={5}")
# check self-blocking
def is_self_blocking(Mn, Pess):
    plist = sorted(Pess)
    n = len(plist)
    if n > 16: return None
    # every transversal contains a member as subset
    for k in range(1, n+1):
        for combo in combinations(range(n), k):
            T = frozenset(plist[i] for i in combo)
            if all(T & Mm for Mm in Mn):
                # T is a transversal; does it contain a member?
                if not any(Mm <= T for Mm in Mn):
                    return False
    return True
sb = is_self_blocking(last['M_n'], last['Pess'])
print("self-blocking?", sb)

# Check Cov monotonicity across evolution
print("\n=== Cov monotonicity for a1=35 ===")
prev_cov = set()
viol = 0
for r in recs:
    cov = set()
    for M in r['M_n']:
        if 2 in M and len(M)==2:
            q = list(M-{2})
            if q[0] in P1:
                cov.add(q[0])
    if cov < prev_cov:
        viol += 1
        if viol <= 3:
            print("  VIOLATION at n=",r['n'], "cov=",cov,"prev=",prev_cov)
    prev_cov = cov
print("Cov monotone violations:", viol)
print("Cov trajectory (every 5): ", [set(r['M_n']) and {q for M in r['M_n'] if 2 in M and len(M)==2 and (list(M-{2})[0] in P1) for q in [list(M-{2})[0]]} for r in recs[::10]])
