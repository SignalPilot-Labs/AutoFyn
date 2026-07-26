"""
Simulator for IMO 2026 P6 sequence and minimal-transversal dynamics - optimized.
"""
import math
from sympy import factorint
from itertools import combinations
from collections import defaultdict


def support(m):
    return frozenset(factorint(m).keys())


def gen_sequence(a1, N):
    a = [a1]
    for n in range(1, N):
        an = a[-1]
        m = an + 1
        while True:
            ok = True
            for ai in a:
                if math.gcd(m, ai) <= 1:
                    ok = False
                    break
            if ok:
                break
            m += 1
        a.append(m)
    return a


def minimal_transversals(family, max_size=6):
    """
    family: list of frozensets (distinct supports). Compute minimal hitting sets
    of size <= max_size via increasing-size enumeration with proper minimality.
    """
    family = list(set(family))
    if not family:
        return set()
    universe = sorted(set().union(*[set(f) for f in family]))
    results = set()
    # For each size k=1..max_size, find hitting sets of that size, keep minimal.
    # A hitting set H of size k is minimal iff no proper subset is a hitting set,
    # i.e. each element of H has a private set (a family member hit ONLY by that element).
    for k in range(1, max_size + 1):
        for combo in combinations(universe, k):
            H = set(combo)
            # is H a hitting set?
            if not all(H & set(f) for f in family):
                continue
            # is H minimal? each element must be essential: removing it breaks some set
            minimal = True
            for e in combo:
                Hminus = H - {e}
                # e is essential iff some family member is hit only by e among H
                if not any((set(f) & H) == {e} for f in family):
                    minimal = False
                    break
            if minimal:
                results.add(frozenset(H))
    return results


def compute_for_a1(a1, N):
    a = gen_sequence(a1, N)
    P1 = support(a1)
    M1 = math.prod(P1)
    prev_mt_primes = set(P1)
    events = []
    for n in range(1, N + 1):
        supports = list({support(ai) for ai in a[:n]})
        mt = minimal_transversals(supports)
        mt_primes = set().union(*[set(t) for t in mt]) if mt else set()
        new_primes = {q for q in mt_primes if q not in P1 and q not in prev_mt_primes}
        for q in sorted(new_primes):
            ts_with_q = [t for t in mt if q in t]
            A_set = set()
            B_set = set()
            for t in ts_with_q:
                for F in supports:
                    if q in F and len(set(F) & set(t)) == 1:
                        A_set.add(frozenset(set(F) & set(P1)))
                for p in P1:
                    if p not in t:
                        B_set.add(p)
            tau = (frozenset(A_set), frozenset(B_set))
            r1 = len(ts_with_q)
            supports_not_hit = set()
            for t in ts_with_q:
                tnq = set(t) - {q}
                for i, F in enumerate(supports):
                    if not (set(F) & tnq):
                        supports_not_hit.add(i)
            r2 = len(supports_not_hit)
            r3 = len(mt)
            events.append((n, q, tau, r1, r2, r3, len(supports), len(mt)))
        prev_mt_primes = mt_primes
    return a, P1, M1, events


def main():
    for a1 in [385, 77, 715, 1309, 2431]:
        print(f"\n===== a_1 = {a1} =====")
        N = 50
        try:
            a, P1, M1, events = compute_for_a1(a1, N)
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback; traceback.print_exc()
            continue
        print(f"  P1={sorted(P1)}  M1={M1}")
        print(f"  seq first 10: {a[:10]}")
        print(f"  last computed a_{N}={a[-1]}")
        print(f"  pulled-in events (n, q, A, B, r1, r2, r3, #supp, #MT):")
        for ev in events:
            n, q, tau, r1, r2, r3, ns, nm = ev
            print(f"    n={n:3d} q={q:5d} A={set(tau[0])} B={set(tau[1])} r1={r1} r2={r2} r3={r3} #supp={ns} #MT={nm}")
        by_type = defaultdict(list)
        for ev in events:
            n, q, tau, r1, r2, r3, ns, nm = ev
            by_type[tau].append((n, q, r1, r2, r3))
        print(f"  --- types with >=2 events ---")
        found_recur = False
        for tau, evs in by_type.items():
            if len(evs) >= 2:
                found_recur = True
                print(f"    TYPE A={set(tau[0])} B={set(tau[1])}: {len(evs)} events")
                for (n, q, r1, r2, r3) in evs:
                    print(f"        n={n} q={q} r1={r1} r2={r2} r3={r3}")
                r1s = [e[2] for e in evs]; r2s = [e[3] for e in evs]; r3s = [e[4] for e in evs]
                print(f"      r1 strict dec? {all(r1s[i]>r1s[i+1] for i in range(len(r1s)-1))} {r1s}")
                print(f"      r2 strict dec? {all(r2s[i]>r2s[i+1] for i in range(len(r2s)-1))} {r2s}")
                print(f"      r3 strict dec? {all(r3s[i]>r3s[i+1] for i in range(len(r3s)-1))} {r3s}")
        if not found_recur:
            print(f"    (no type recurs within {N} steps)")
        # also: does MT stabilize?
        # recompute final mt
        supports_final = list({support(ai) for ai in a})
        mt_final = minimal_transversals(supports_final)
        print(f"  final MT (n={N}): {sorted([sorted(t) for t in mt_final])}")
        print(f"  final MT primes: {sorted(set().union(*[set(t) for t in mt_final]) if mt_final else [])}")


if __name__ == "__main__":
    main()
