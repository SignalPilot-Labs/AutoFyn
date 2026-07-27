"""Probe: does the mtp-witness transversal always contain a prime <= p*?
If yes, (b) is trivial (the unique mtp-multiple in (a_n,a_n+mtp] is valid & small-prime-divisible).
Also: when a_{n+1} is a strict-beat of the mtp-witness (promotion), what primes does it carry?
And: is there a <=p*-prime-divisible valid number BELOW a_{n+1} in (a_n, a_n+mtp] always?
"""
import sympy
from itertools import combinations

def P(m):
    return set(sympy.primefactors(m))

def minimal_family(fam_list):
    mins = []
    for S in fam_list:
        if any((other < S) for other in fam_list if other != S):
            continue
        mins.append(S)
    out = []
    for S in mins:
        if S not in out:
            out.append(S)
    return out

def mtp_and_witness(Mfam, Pess):
    plist = sorted(Pess)
    n = len(plist)
    if n > 16:
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

def run(a1, max_steps=4000, stable_window=80):
    a = [a1]
    fam = [P(a1)]
    Mn = minimal_family(fam)
    Pess = set(P(a1))
    pstar = min(P(a1))
    Pfam1 = P(a1)
    stats = {'steps':0, 'witness_has_small':0, 'witness_no_small':0,
             'witness_no_small_promo':0, 'witness_no_small_promo_but_carries_small':0,
             'total_promo':0, 'promo_carries_small':0}
    witness_no_small_examples = []
    for n in range(1, max_steps):
        m = a[-1] + 1
        while True:
            Pm = P(m)
            if all(Pm & Mi for Mi in Mn):
                break
            m += 1
        Pm = P(m)
        mtp_val, Tstar = mtp_and_witness(Mn, Pess)
        is_promo = not any(S <= Pm for S in Mn)
        stats['steps'] += 1
        if Tstar is not None:
            if any(p <= pstar for p in Tstar):
                stats['witness_has_small'] += 1
            else:
                stats['witness_no_small'] += 1
                if is_promo:
                    stats['witness_no_small_promo'] += 1
                    if any(p <= pstar for p in Pm):
                        stats['witness_no_small_promo_but_carries_small'] += 1
                    if len(witness_no_small_examples) < 8:
                        witness_no_small_examples.append({
                            'n':n,'a_next':m,'P_next':sorted(Pm),'Tstar':sorted(Tstar),
                            'pstar':pstar,'is_promo':is_promo,
                            'Mn_before':[sorted(s) for s in Mn]})
        if is_promo:
            stats['total_promo'] += 1
            if any(p <= pstar for p in Pm):
                stats['promo_carries_small'] += 1
        a.append(m)
        fam.append(Pm)
        Mn = minimal_family(fam)
        Pess = set()
        for S in Mn: Pess |= S
        if n > stable_window:
            recent_nonpromo = all(not (not any(S <= P(a[-1]+i) for S in Mn)) for i in range(1,stable_window+1)) if False else None
            break_loop = True
            for i in range(1, stable_window+1):
                # re-check: is the i-th future term a promotion? too expensive; use simpler: count non-promo via gap==mtp heuristic is unreliable.
                pass
            break
    # detect regime by final Mn
    regime = 'freeze' if (len(Mn)==1 and len(list(Mn)[0])==1 and list(list(Mn)[0])[0] in Pfam1) else 'saturated'
    return stats, witness_no_small_examples, regime

seeds_sat = [15, 35, 105, 165, 385, 429, 1001, 2145, 4199, 7429, 12673, 175, 187, 221,
             323, 899, 1147, 1517, 1763, 2021, 2461, 31213, 667, 1189, 1207, 1387, 1591,
             1739, 1963, 2501, 2773, 3059, 3239, 3713, 4331, 5293, 6499, 7387, 8633,
             15341, 19549, 5183, 6161, 10403]
print("=== mtp-witness small-prime analysis (saturated seeds) ===")
for s in seeds_sat:
    try:
        stats, ex, regime = run(s)
        if regime != 'saturated':
            print(f"  a1={s}: regime={regime} (skip)")
            continue
        ws = stats['witness_no_small']
        whs = stats['witness_has_small']
        tot = stats['steps']
        # skip seeds where many steps had None witness (|Pess|>16)
        computed = ws + whs
        print(f"  a1={s}: steps={tot} witness_computed={computed} has_small={whs} no_small={ws} | "
              f"promo_total={stats['total_promo']} promo_carries_small={stats['promo_carries_small']} | "
              f"no_small_promo={stats['witness_no_small_promo']} no_small_promo_but_carries_small={stats['witness_no_small_promo_but_carries_small']}")
        if ex:
            print(f"     examples (witness no-small, promo): {ex[:3]}")
    except Exception as e:
        print(f"  a1={s} ERROR {e}")
