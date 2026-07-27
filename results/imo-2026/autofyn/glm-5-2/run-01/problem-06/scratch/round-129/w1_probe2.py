import sympy, math
from sympy import factorint
from itertools import combinations

def P(m):
    return frozenset(factorint(m).keys())

def min_members(F):
    """M = inclusion-minimal members of family F (list of frozensets)."""
    out = []
    for S in F:
        if not any(T < S for T in F):  # no proper subset in F
            out.append(S)
    return out

def all_mtp_witnesses(Mn):
    """Return (mtp, [list of all min-product transversals]). None if Pess too big."""
    if not Mn:
        return 1, [frozenset()]
    Pess = sorted(set().union(*[set(s) for s in Mn]))
    if len(Pess) > 16:
        return None, None
    best = None
    witnesses = []
    for r in range(1, len(Pess)+1):
        for comb in combinations(Pess, r):
            T = frozenset(comb)
            if all(any(p in S for p in T) for S in Mn):
                prod = 1
                for p in T: prod *= p
                if best is None or prod < best:
                    best = prod; witnesses = [T]
                elif prod == best:
                    witnesses.append(T)
    return best, witnesses

def greedy(a1, max_terms=300):
    F = [P(a1)]          # all supports so far
    a = [a1]
    steps = []           # per-step record BEFORE choosing a_{n+1}
    n = 1
    while n < max_terms:
        Mn = min_members(F)
        mtpval, wits = all_mtp_witnesses(Mn)
        Cn = set(Mn[0]) if Mn else set()
        for S in Mn[1:]: Cn &= set(S)
        steps.append(dict(n=n, a_n=a[-1], Mn=Mn, mtp=mtpval, wits=wits, Cn=Cn))
        # choose a_{n+1}
        m = a[-1]+1
        while not all(P(m)&Pa for Pa in F):
            m += 1
        a.append(m)
        F.append(P(m))
        n += 1
    return a, steps

def run(a1):
    print(f"\n=== a1={a1} ===")
    a, steps = greedy(a1, 300)
    pstar = min(P(a1))
    print(f"p*={pstar} P(a1)={sorted(P(a1))}  terms={len(a)}")
    # W1: EVERY mtp-witness carries a prime <= p*
    w1_viol=0; w1_tot=0
    # SPT: every minimal has min <= p*
    spt_viol=0
    for st in steps:
        if st['wits'] is not None:
            for w in st['wits']:
                w1_tot += 1
                if not any(p<=pstar for p in w): w1_viol+=1
        for M in st['Mn']:
            if min(M) > pstar: spt_viol+=1
    print(f"W1: {w1_viol} violations / {w1_tot} witness-instances")
    print(f"SPT(M_n per step): {spt_viol} violations")
    # promotions + equality/strict split: promotion iff M_{n+1} != M_n
    prom=0; eq=0; sb=0; nonprom_eq=0
    F=[P(a1)]
    for n in range(1, len(a)):
        Mn = min_members(F)
        mtpval = steps[n-1]['mtp']
        a_prev = steps[n-1]['a_n']
        Pn = P(a[n])
        F2 = F+[Pn]
        Mn1 = min_members(F2)
        is_prom = set(map(frozenset,Mn1)) != set(map(frozenset,Mn))
        if mtpval is not None:
            mult = math.ceil((a_prev+1)/mtpval)*mtpval
            kind = 'equality' if a[n]==mult else ('strict-beat' if a[n]<mult else 'above')
        else:
            kind='?'
        if is_prom:
            prom+=1
            if kind=='equality': eq+=1
            elif kind=='strict-beat': sb+=1
        else:
            if kind=='equality': nonprom_eq+=1
        F=F2
    print(f"promotions={prom} (equality={eq}, strict-beat={sb}); non-promotion equality(mtp-multiple)={nonprom_eq}")
    print(f"final Mn={sorted([sorted(s) for s in min_members(F)])}")
    print(f"final Pess={sorted(set().union(*[set(s) for s in min_members(F)]))}")

for s in [15,429,30,273,175,19549,35,77,143,5005]:
    try: run(s)
    except Exception as e:
        import traceback; traceback.print_exc(); print(f"ERR a1={s}: {e}")
