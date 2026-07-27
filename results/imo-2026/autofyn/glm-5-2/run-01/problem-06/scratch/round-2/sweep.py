import sys, itertools
from sympy import factorint

def primes_of(n):
    return set(factorint(n).keys())

def minimal_elements(family):
    # family: list of sets; return inclusion-minimal ones
    fam = [set(s) for s in family]
    out = []
    n = len(fam)
    for i in range(n):
        if any(fam[j] < fam[i] for j in range(n) if j != i):
            continue
        # also exclude duplicates strictly smaller; keep if no STRICT subset present
        out.append(frozenset(fam[i]))
    # dedup
    out = list({frozenset(s) for s in out})
    return out

def compute_stable(a1, max_rounds=400, max_L=3_000_000, verbose=False):
    """Residue-fast greedy. Returns dict with M (list of sets), P_ess (set), L, R_count, stable, rounds, history."""
    M = [frozenset(primes_of(a1))]
    P_ess = set(M[0])
    a = a1
    history = []
    for round_idx in range(max_rounds):
        L = 1
        for p in P_ess:
            L *= p
        if L > max_L:
            return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), L=L, R=None,
                        stable=None, rounds=round_idx, history=history, reason='L_exceeded')
        Mlist = [set(m) for m in M]
        # compute R: residues r in [0,L) whose essential prime divisors hit every M
        R = []
        for r in range(L):
            Dr = set()
            for p in P_ess:
                if r % p == 0:
                    Dr.add(p)
            ok = True
            for m in Mlist:
                if not (Dr & m):
                    ok = False; break
            if ok:
                R.append(r)
        if not R:
            return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), L=L, R=[],
                        stable=False, rounds=round_idx, history=history, reason='empty_R')
        Rsorted = sorted(R)
        T = len(Rsorted)
        r_to_idx = {r: i for i, r in enumerate(Rsorted)}
        def succ(r):
            i = r_to_idx[r]
            j = i + 1
            if j == T:
                return Rsorted[0]
            return Rsorted[j]
        def essential(res):
            return set(p for p in P_ess if res % p == 0)
        # triggers
        trigger_set = set()
        for r in Rsorted:
            s = succ(r)
            E = essential(s)
            if not any(m <= E for m in Mlist):
                trigger_set.add(r)
        r_cur = a % L
        if r_cur not in set(Rsorted):
            return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), L=L, R=Rsorted,
                        stable=None, rounds=round_idx, history=history, reason='r_cur_not_in_R')
        if not trigger_set:
            return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), L=L, R=Rsorted,
                        stable=True, rounds=round_idx, R_count=T, history=history, reason='stable')
        # walk from r_cur to first trigger (cyclic), accumulating a
        r = r_cur
        a_now = a
        steps = 0
        trigger_found = None
        while steps <= T + 1:
            if r in trigger_set:
                trigger_found = r
                break
            s = succ(r)
            gap = (s - r) if s > r else (s + L - r)
            a_now = a_now + gap
            r = s
            steps += 1
        if trigger_found is None:
            # no trigger in a full cycle -> stable
            return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), L=L, R=Rsorted,
                        stable=True, rounds=round_idx, R_count=T, history=history, reason='stable_no_walktrigger')
        # promotion at trigger_found; a_now mod L = trigger_found
        s = succ(trigger_found)
        gap = (s - trigger_found) if s > trigger_found else (s + L - trigger_found)
        a_new = a_now + gap
        Pnew = primes_of(a_new)
        E = Pnew & P_ess
        # verify promotion condition
        promo_ok = not any(set(m) <= E for m in Mlist)
        if not promo_ok:
            # inconsistency
            return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), L=L, R=Rsorted,
                        stable=None, rounds=round_idx, history=history, reason='promo_inconsistent')
        # refine: remove old M that are supersets of Pnew, add Pnew
        newM = []
        for m in M:
            if Pnew <= set(m):
                continue
            newM.append(set(m))
        newM.append(set(Pnew))
        M = [frozenset(x) for x in newM]
        P_ess = P_ess | Pnew
        a = a_new
        history.append(dict(a=a, M_size=len(M), Pess_size=len(P_ess), L=L, new_primes=sorted(Pnew - (P_ess - Pnew))))
        if verbose:
            print(f"  round {round_idx}: a={a} |M|={len(M)} |Pess|={len(P_ess)} L={L} new={sorted(Pnew-(P_ess-Pnew))}")
    return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), L=None, R=None,
                stable=False, rounds=max_rounds, history=history, reason='max_rounds')


if __name__ == '__main__':
    # sweep omega=2
    import itertools as it
    from sympy import primerange, prime
    small_primes = list(primerange(2, 60))
    # omega=2: pairs of distinct primes
    print("=== omega=2 ===")
    results2 = []
    for p, q in it.combinations(small_primes, 2):
        a1 = p*q
        res = compute_stable(a1)
        results2.append((a1, (p,q), res))
        if res['stable']:
            print(f"a1={a1} ({p},{q}): |Pess|={len(res['P_ess'])} |M|={len(res['M'])} L={res['L']} T={res.get('R_count')} rounds={res['rounds']}")
        else:
            print(f"a1={a1} ({p},{q}): UNSTABLE/L-exceeded reason={res.get('reason')} |Pess|={len(res['P_ess'])} rounds={res['rounds']}")
