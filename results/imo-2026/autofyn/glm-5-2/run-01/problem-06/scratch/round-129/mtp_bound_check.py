"""Check: does mtp(M_n) <= primorial(p*) hold across saturated seeds?
Also: when witness T* contains a small prime, is prod(T*) still <= primorial(p*)?
Tests whether W1 (witness has small prime) vs SPT (every minimal has small prime) is the right GAP-1 closer."""
import sympy
from itertools import combinations

def P(m):
    return set(sympy.primefactors(m))

def minimal_family(fam_list):
    out = []
    for S in fam_list:
        if any((other <= S) and (other != S) for other in fam_list):
            continue
        if S not in out:
            out.append(S)
    return out

def mtp_and_witness(Mfam, Pess):
    plist = sorted(Pess)
    n = len(plist)
    if n > 18:
        return (None, None)
    best = None; bestT = None
    for k in range(1, n+1):
        for combo in combinations(range(n), k):
            T = set(plist[i] for i in combo)
            if all(T & Mm for Mm in Mfam):
                prod = 1
                for p in T: prod *= p
                if best is None or prod < best:
                    best = prod; bestT = frozenset(T)
    return (best, bestT)

def primorial(pstar):
    pr = 1
    for p in sympy.primerange(2, pstar+1):
        pr *= p
    return pr

def run(a1, max_steps=4000, stable_window=60):
    a = [a1]
    fam = [P(a1)]
    Mn = minimal_family(fam)
    Pess = set(P(a1))
    pstar = min(P(a1))
    prim = primorial(pstar)
    res = {'steps':0, 'mtp_le_prim':0, 'mtp_gt_prim':0, 'viol_examples':[],
           'witness_has_small':0, 'witness_large_only':0,
           'minimal_all_have_small':0, 'minimal_some_large_only':0}
    for n in range(1, max_steps):
        m = a[-1] + 1
        while True:
            Pm = P(m)
            if all(Pm & Mi for Mi in Mn):
                break
            m += 1
        Pm = P(m)
        mtp_val, Tstar = mtp_and_witness(Mn, Pess)
        res['steps'] += 1
        if mtp_val is not None:
            if mtp_val <= prim:
                res['mtp_le_prim'] += 1
            else:
                res['mtp_gt_prim'] += 1
                if len(res['viol_examples']) < 5:
                    res['viol_examples'].append({'n':n,'mtp':mtp_val,'prim':prim,'pstar':pstar,
                                                  'Mn':[sorted(s) for s in Mn],'Tstar':sorted(Tstar)})
            if Tstar is not None:
                if any(p <= pstar for p in Tstar):
                    res['witness_has_small'] += 1
                else:
                    res['witness_large_only'] += 1
        # SPT check: every minimal has a prime <= pstar
        if Mn:
            if all(any(p <= pstar for p in M) for M in Mn):
                res['minimal_all_have_small'] += 1
            else:
                res['minimal_some_large_only'] += 1
        a.append(m)
        fam.append(Pm)
        Mn = minimal_family(fam)
        Pess = set()
        for S in Mn: Pess |= S
        if n > stable_window:
            break
    regime = 'freeze' if (len(Mn)==1 and len(list(Mn)[0])==1) else 'saturated'
    return res, regime

seeds = [15, 35, 105, 165, 385, 429, 1001, 2145, 4199, 7429, 12673, 175, 187, 221,
         323, 899, 1147, 1517, 1763, 2021, 2461, 667, 1189, 1207, 1387, 1591,
         1739, 2501, 2773, 3059, 3239, 3713, 4331, 5293, 6499, 7387, 8633,
         15341, 5183, 6161, 10403]
print("=== mtp <= primorial(p*) ? and SPT (every minimal has small prime) ? ===")
any_viol = False
for s in seeds:
    try:
        res, regime = run(s)
        if regime != 'saturated':
            print(f"  a1={s}: regime={regime} (skip)")
            continue
        viol = res['mtp_gt_prim']
        spt_viol = res['minimal_some_large_only']
        flag = "" if viol==0 and spt_viol==0 else " <<< VIOLATION"
        if viol>0 or spt_viol>0:
            any_viol = True
        print(f"  a1={s}: steps={res['steps']} mtp_le_prim={res['mtp_le_prim']} mtp_gt_prim={viol} | "
              f"witness_has_small={res['witness_has_small']} witness_large_only={res['witness_large_only']} | "
              f"SPT_all_small={res['minimal_all_have_small']} SPT_some_large={spt_viol}{flag}")
        if res['viol_examples']:
            print(f"     viol examples: {res['viol_examples'][:2]}")
    except Exception as e:
        print(f"  a1={s} ERROR {e}")
print("ANY VIOLATION:", any_viol)
