import sympy

def P(m):
    return set(sympy.primefactors(m))

def transversals_hit(T, Mfam):
    return all(T & M for M in Mfam)

def minimal_family(fam_list):
    # fam_list: list of sets
    mins = []
    for S in fam_list:
        if any(other < S for other in fam_list if other is not S):
            continue
        # S is minimal if no distinct other is a proper subset
        if not any((other < S) for other in fam_list if other != S):
            mins.append(S)
    # dedupe
    out = []
    for S in mins:
        if S not in out:
            out.append(S)
    return out

def run(a1, max_steps=2000):
    a = [a1]
    fam = [P(a1)]
    Mn = minimal_family(fam)
    pstar = min(P(a1))
    promotions = []  # (n, a_{n+1}, new_min_M', min_M', is_promotion, note)
    for n in range(1, max_steps):
        # find smallest m > a[-1] valid
        m = a[-1] + 1
        while True:
            Pm = P(m)
            if all(Pm & Mi for Mi in Mn):
                break
            m += 1
        # is P(m) a new minimal?
        Pm = P(m)
        is_promo = not any(S <= Pm for S in Mn)  # no existing minimal subset of Pm
        # also check it's minimal among fam (existing full family)
        new_fam = fam + [Pm]
        new_Mn = minimal_family(new_fam)
        # record
        minPm = min(Pm) if Pm else None
        promotions.append({
            'n': n, 'a_next': m, 'P_next': sorted(Pm),
            'min_P_next': minPm, 'pstar': pstar,
            'is_promo': is_promo,
            'Mn_before': [sorted(s) for s in Mn],
            'new_Mn': [sorted(s) for s in new_Mn],
            'gap': m - a[-1],
        })
        a.append(m)
        fam = new_fam
        Mn = new_Mn
        # stop if stabilized for a while + singleton
        if n > 20 and len(Mn) == 1 and len(list(Mn)[0]) == 1:
            break
        # stop if Mn unchanged for 50 steps
        if n > 60:
            if promotions[-1]['new_Mn'] == promotions[-1]['Mn_before']:
                # check freeze
                stable_count = sum(1 for r in promotions[-50:] if r['is_promo']==False)
                if stable_count == 50:
                    break
    return a, promotions, pstar

for a1 in [15, 105, 175, 429, 1001, 19549]:
    print(f"\n===== a1={a1}, P(a1)={sorted(P(a1))}, p*={min(P(a1))} =====")
    a, promo, pstar = run(a1, max_steps=4000)
    print(f"final a_n={a[-1]}, steps={len(a)}")
    # print promotions only
    promos = [r for r in promo if r['is_promo']]
    print(f"#promotions={len(promos)}")
    for r in promos:
        flag = "OK" if r['min_P_next'] <= pstar else "VIOLATION"
        print(f"  step {r['n']}: a_next={r['a_next']} P={r['P_next']} min={r['min_P_next']} p*={pstar} {flag}  Mn_before={r['Mn_before']}")
