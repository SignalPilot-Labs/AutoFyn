import sympy
from sympy import factorint
from itertools import combinations

def P(m):
    return frozenset(factorint(m).keys())

def greedy_seq(a1, max_terms=400):
    """Generate greedy sequence and record M_n, mtp, witness, etc."""
    a = [a1]
    # track family of P(a_i)
    F = [P(a1)]
    records = []
    n = 1
    while n < max_terms:
        # build M_n = minimal members of F
        Fn = F[:]
        Mn = []
        for S in Fn:
            if not any(T < S for T in Fn):  # S minimal: no proper subset in Fn
                Mn.append(S)
        # mtp: min product transversal
        Pess = set()
        for S in Mn:
            Pess |= set(S)
        Pess = sorted(Pess)
        mtp, witness = compute_mtp(Mn, Pess)
        # common primes
        if Mn:
            Cn = set(Mn[0])
            for S in Mn[1:]:
                Cn &= set(S)
        else:
            Cn = set()
        records.append({
            'n': n, 'a_n': a[-1], 'M_n': [set(s) for s in Mn],
            'Pess': set(Pess), 'mtp': mtp, 'witness': set(witness) if witness else None,
            'C_n': set(Cn),
        })
        # find a_{n+1}: smallest m > a_n with P(m) hitting every P(a_i)
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
    if not Mn:
        return 1, frozenset()
    if len(Pess) > 16:
        return None, None  # too big
    best = None
    bestT = None
    # enumerate subsets by increasing size
    Pess_list = list(Pess)
    for r in range(1, len(Pess_list)+1):
        for comb in combinations(Pess_list, r):
            T = frozenset(comb)
            if all(any(p in S for p in T) for S in Mn):
                prod = 1
                for p in T:
                    prod *= p
                if best is None or prod < best:
                    best = prod
                    bestT = T
        if best is not None:
            # min at this cardinality might not be global min (larger card could be smaller prod)
            # but products of primes, more primes => larger product generally; still continue one more
            pass
    return best, bestT

def classify_promotion(rec_prev, a_next):
    """Is a_next a promotion (new minimal)? equality vs strict-beat."""
    # equality if a_next == mtp-multiple (smallest multiple of mtp above a_prev)
    a_prev = rec_prev['a_n']
    mtp = rec_prev['mtp']
    if mtp is None:
        return 'unknown'
    # smallest multiple of mtp strictly above a_prev
    import math
    mult = math.ceil((a_prev+1)/mtp) * mtp
    if a_next == mult:
        return 'equality'
    elif a_next < mult:
        return 'strict-beat'
    else:
        return 'above-mtp??'

def is_new_minimal(F_before, P_next):
    """Does P_next become a new minimal in F_before ∪ {P_next}?"""
    Fn = F_before
    # is P_next minimal? no proper subset in Fn+{P_next} other than itself
    for S in Fn:
        if S < P_next:  # proper subset
            return False
    return True

def run(a1):
    print(f"\n=== a1={a1} ===")
    a, recs = greedy_seq(a1, max_terms=300)
    pstar = min(P(a1))
    print(f"p* = {pstar}, P(a1) = {set(P(a1))}")
    # detect stabilization (when M_n stops changing)
    # rebuild F with new-minimal detection + promotion tracking
    F = [P(a1)]
    promotions = []
    equality = 0; strict = 0
    w1_violations = 0
    spt_violations = 0
    w1_total = 0
    # recompute with promotion tracking
    a_seq = [a1]
    for n in range(1, len(a)):
        # M at step n (before a_{n+1})
        Fn = F[:]
        Mn = [S for S in Fn if not any(T < S for T in Fn)]
        Pess = sorted(set().union(*[set(s) for s in Mn])) if Mn else []
        mtp, wit = compute_mtp(Mn, Pess) if len(Pess)<=16 else (None,None)
        # W1 check: witness carries prime <= p*
        if wit is not None:
            w1_total += 1
            if not any(p <= pstar for p in wit):
                w1_violations += 1
        # SPT check on current M_n: every minimal has min <= p*
        for M in Mn:
            if min(M) > pstar:
                spt_violations += 1
        # a_{n+1} = a[n]  (since a is 0-indexed, a[0]=a1, a[1]=a2)
        a_next = a[n]  # this is a_{n+1}
        P_next = P(a_next)
        # is it a new minimal?
        newmin = is_new_minimal(Fn, P_next)
        if newmin:
            # classify
            kind = classify_promotion({'a_n': a_seq[-1], 'mtp': mtp}, a_next)
            promotions.append((n+1, a_next, kind, set(P_next)))
            if kind=='equality': equality+=1
            elif kind=='strict-beat': strict+=1
        F.append(P_next)
        a_seq.append(a_next)
        # stop if M stabilized (no new minimal for a long stretch) -- but we track all
    print(f"total terms computed: {len(a)}")
    print(f"promotions: {len(promotions)} (equality={equality}, strict-beat={strict})")
    print(f"W1 violations (witness lacks small prime): {w1_violations}/{w1_total}")
    print(f"SPT violations (some minimal min>p*): {spt_violations}")
    # final M
    Mn_final = [S for S in F if not any(T < S for T in F)]
    print(f"final |M|={len(Mn_final)}, Pess={sorted(set().union(*[set(s) for s in Mn_final]))}")

for s in [15, 429, 30, 273, 175, 19549]:
    try:
        run(s)
    except Exception as e:
        print(f"ERROR a1={s}: {e}")
