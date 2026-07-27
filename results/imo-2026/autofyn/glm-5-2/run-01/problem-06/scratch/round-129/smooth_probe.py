"""Smooth-number / density route probe for imo-2026-06 saturated-regime wall.

At every step (and especially at every promotion), record:
  a_n, a_{n+1}, gap, mtp(M_n), mtp-witness-above-a_n, smallest prime factor of a_{n+1},
  whether a_{n+1} carries a prime <= p* := min P(a_1),
  whether there EXISTS a valid number in (a_n, a_n+mtp] divisible by some prime <= p*,
  count of valid numbers in (a_n, a_n+mtp] carrying a prime <= p*,
  count of ALL valid numbers in (a_n, a_n+mtp] (density proxy).
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
    """Return (mtp_value, witness_transversal_set) or (None,None) if too big."""
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
                for p in T:
                    prod *= p
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
    records = []
    for n in range(1, max_steps):
        m = a[-1] + 1
        while True:
            Pm = P(m)
            if all(Pm & Mi for Mi in Mn):
                break
            m += 1
        gap = m - a[-1]
        Pm = P(m)
        spf = min(Pm)
        carries_small = any(p <= pstar for p in Pm)
        mtp_val, Tstar = mtp_and_witness(Mn, Pess)
        # mtp-witness multiple above a_n
        if mtp_val is not None:
            import math
            witness_above = ((a[-1] // mtp_val) + 1) * mtp_val
            le_witness = (m <= witness_above)
        else:
            witness_above = None; le_witness = None
        # promotion: P(m) is a new minimal (no existing minimal is a subset)
        is_promo = not any(S <= Pm for S in Mn)
        # scan (a_n, a_n + mtp_window] for valid numbers carrying a small prime
        if mtp_val is not None:
            lo = a[-1]; hi = a[-1] + mtp_val
            cnt_valid_small = 0; cnt_valid_total = 0
            first_small = None
            # cap scan length to avoid huge loops
            for x in range(lo+1, hi+1):
                Px = P(x)
                if all(Px & Mi for Mi in Mn):
                    cnt_valid_total += 1
                    if any(p <= pstar for p in Px):
                        cnt_valid_small += 1
                        if first_small is None:
                            first_small = x
        else:
            cnt_valid_small = None; cnt_valid_total = None; first_small = None
        records.append({
            'n': n, 'a_n': a[-1], 'a_next': m, 'gap': gap,
            'mtp': mtp_val, 'witness_above': witness_above,
            'le_witness': le_witness, 'spf': spf, 'carries_small': carries_small,
            'is_promo': is_promo, 'P_next': sorted(Pm),
            'cnt_valid_small': cnt_valid_small,
            'cnt_valid_total': cnt_valid_total,
            'first_small': first_small,
        })
        a.append(m)
        # update family
        fam.append(Pm)
        Mn = minimal_family(fam)
        Pess = set()
        for S in Mn:
            Pess |= S
        # stabilization detection: if last stable_window steps all non-promo -> done
        if n > stable_window:
            recent = records[-stable_window:]
            if all(not r['is_promo'] for r in recent):
                break
    # regime: freeze if final Mn is singleton {p} with p in Pfam1; else saturated
    final_Mn = Mn
    regime = 'freeze' if (len(final_Mn) == 1 and len(list(final_Mn)[0]) == 1 and list(list(final_Mn)[0])[0] in Pfam1) else 'saturated'
    # also: detect freeze by common prime persistence
    return a, records, pstar, regime, final_Mn

def summarize(a1):
    a, recs, pstar, regime, Mn = run(a1)
    promos = [r for r in recs if r['is_promo']]
    nonpromos = [r for r in recs if not r['is_promo']]
    print(f"\n===== a1={a1} P(a1)={sorted(P(a1))} p*={pstar} regime={regime} steps={len(recs)} =====")
    print(f"  final Mn={[sorted(s) for s in Mn]}  #promos={len(promos)}")
    # (a) is a_{n+1}'s smallest prime factor always <= p*?
    if regime == 'saturated':
        viol_a = [r for r in recs if r['spf'] > pstar]
        print(f"  (a) spf>p* violations: {len(viol_a)} / {len(recs)} steps")
        if viol_a[:5]:
            for r in viol_a[:5]:
                print(f"      step {r['n']}: a_next={r['a_next']} spf={r['spf']} P={r['P_next']}")
        # also promotions only
        viol_a_promo = [r for r in promos if r['spf'] > pstar]
        print(f"      (at promotions only: {len(viol_a_promo)} violations)")
        # carries_small
        viol_cs = [r for r in recs if not r['carries_small']]
        print(f"      carries-prime<=p* violations: {len(viol_cs)} / {len(recs)}")
        viol_cs_promo = [r for r in promos if not r['carries_small']]
        print(f"      (at promotions only: {len(viol_cs_promo)} violations)")
        if viol_cs_promo[:5]:
            for r in viol_cs_promo[:5]:
                print(f"      step {r['n']}: a_next={r['a_next']} P={r['P_next']} carries_small={r['carries_small']} mtp={r['mtp']}")
    # (b) is there always a <=p*-divisible valid number in (a_n, a_n+mtp]?
    if regime == 'saturated':
        viol_b = [r for r in recs if r['cnt_valid_small'] is not None and r['cnt_valid_small'] == 0]
        print(f"  (b) no-small-valid-in-window violations: {len(viol_b)} / {len([r for r in recs if r['cnt_valid_small'] is not None])}")
        viol_b_promo = [r for r in promos if r['cnt_valid_small'] is not None and r['cnt_valid_small'] == 0]
        print(f"      (at promotions only: {len(viol_b_promo)} violations)")
        if viol_b_promo[:5]:
            for r in viol_b_promo[:5]:
                print(f"      step {r['n']}: a_n={r['a_n']} mtp={r['mtp']} window-end={r['a_n']+r['mtp']} cnt_valid_total={r['cnt_valid_total']}")
    # (c) gap vs mtp
    if promos:
        gaps_p = [r['gap'] for r in promos]
        mtps_p = [r['mtp'] for r in promos if r['mtp']]
        gaps_np = [r['gap'] for r in nonpromos]
        mtps_np = [r['mtp'] for r in nonpromos if r['mtp']]
        import statistics as st
        if mtps_p:
            print(f"  (c) promos: gap mean={st.mean(gaps_p):.2f} max={max(gaps_p)} | mtp mean={st.mean(mtps_p):.2f} max={max(mtps_p)} | ratio gap/mtp mean={st.mean(g/m for g,m in zip(gaps_p,mtps_p) if m):.3f}")
        if mtps_np:
            print(f"      nonpromos: gap mean={st.mean(gaps_np):.2f} max={max(gaps_np)} | mtp mean={st.mean(mtps_np):.2f} max={max(mtps_np)}")
        # le_witness at promotions
        le_p = [r['le_witness'] for r in promos if r['le_witness'] is not None]
        if le_p:
            print(f"      promos: a_next <= mtp-witness-above: {sum(le_p)}/{len(le_p)}")
    return regime, promos, recs

seeds = [15, 21, 33, 35, 39, 105, 165, 231, 385, 429, 1001, 2145, 4199, 7429, 12673,
         175, 187, 221, 323, 899, 1147, 1517, 1763, 2021, 2461, 31213, 273, 323, 667,
         1189, 1207, 1387, 1591, 1739, 1963, 2501, 2773, 3059, 3239, 3713, 4331, 5293,
         6499, 7387, 8633, 15341, 19549, 5183, 6161, 10403, 10787]
seen = set()
for s in seeds:
    if s in seen: continue
    seen.add(s)
    try:
        summarize(s)
    except Exception as e:
        print(f"  a1={s} ERROR {e}")
