"""
Simulator for IMO 2026 P6 sequence and minimal-transversal dynamics.
a_{n+1} = smallest m > a_n with gcd(m, a_i) > 1 for all i <= n.
"""
import sys
import math
from sympy import factorint
from itertools import combinations


def support(m):
    """Set of prime divisors of m."""
    return frozenset(factorint(m).keys())


def gen_sequence(a1, N):
    """Generate a_1..a_N."""
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


def minimal_transversals(family):
    """
    family: list/frozenset of frozensets (supports). Compute minimal hitting sets.
    Returns set of frozensets. Universe = union of all elements.
    Bounded size enumeration: try sizes 1,2,3,... up to len(union).
    """
    family = list(family)
    if not family:
        return set()
    universe = set()
    for f in family:
        universe |= set(f)
    universe = sorted(universe)
    # A hitting set H: H intersects every member of family.
    # Enumerate by increasing size. A set is minimal if no proper subset is a hitting set.
    # To find ALL minimal hitting sets, use the standard recursion.
    # We use a recursive algorithm: pick a set S in family, branch on which element of S to include.
    results = set()

    def recurse(remaining_family, chosen):
        # remaining_family: list of sets not yet hit by `chosen`
        if not remaining_family:
            # chosen is a hitting set; check minimality
            # minimality: no proper subset of chosen is a hitting set of ORIGINAL family
            cl = list(chosen)
            for r in range(1, len(cl)):
                for sub in combinations(cl, r):
                    sub_set = frozenset(sub)
                    if all(any(e in s for e in sub_set) for s in family):
                        # sub is a hitting set, so chosen not minimal -> but we only add minimal
                        return
            results.add(frozenset(chosen))
            return
        # pick the smallest remaining set to branch (fewest elements = fewer branches)
        target = min(remaining_family, key=len)
        rest = [s for s in remaining_family if s is not target]
        for el in target:
            if el in chosen:
                # already chosen, recurse with updated remaining
                new_remaining = [s for s in remaining_family if not (el in s)]
                recurse(new_remaining, chosen)
            else:
                new_remaining = [s for s in remaining_family if not (el in s)]
                recurse(new_remaining, chosen | {el})

    # Deduplicate family first
    uniq_family = list(set(family))
    recurse(uniq_family, frozenset())
    return results


def distinct_supports(a_list):
    """Distinct prime supports among a_1..a_n."""
    return list({support(a) for a in a_list})


def primes_in_mt(mt_set):
    """Union of all primes appearing in any minimal transversal."""
    u = set()
    for t in mt_set:
        u |= set(t)
    return u


def compute_ranks_for_a1(a1, N):
    """
    For each step n, compute MT(F_n), identify pulled-in primes (new non-P1 primes in MT),
    and for each pulled-in prime compute candidate ranks at the moment of pull-in.
    """
    a = gen_sequence(a1, N)
    P1 = support(a1)
    M1 = 1
    for p in P1:
        M1 *= p

    prev_mt_primes = set(P1)  # primes in MT(F_{n-1}); at n=1, MT = singletons of P1
    # Actually at n=1, F_1 = {P1}, MT(F_1) = {{p} for p in P1}
    events = []  # list of (step_n, prime_q, type, r1, r2, r3, r4)

    prev_mt = None
    for n in range(1, N + 1):
        if n > len(a):
            break
        supports = distinct_supports(a[:n])
        mt = minimal_transversals(supports)
        mt_primes = primes_in_mt(mt)
        # pulled-in primes at this step: in mt_primes but not in prev_mt_primes, and not in P1
        new_primes = {q for q in mt_primes if q not in P1 and q not in prev_mt_primes}
        for q in new_primes:
            # compute type and ranks
            # Witnessing: find a private witness for q in some T containing q
            ts_with_q = [t for t in mt if q in t]
            # A(q): set of P1-parts of private witnesses
            A_set = set()
            B_set = set()  # p in P1 with some T containing q avoiding p
            for t in ts_with_q:
                # find private witness: a support F in family with F cap t = {q}
                for F in supports:
                    if q in F and len(set(F) & set(t)) == 1:
                        # F is a private witness of q in t
                        A_set.add(frozenset(set(F) & set(P1)))
                for p in P1:
                    if p not in t:
                        B_set.add(p)
            tau = (frozenset(A_set), frozenset(B_set))
            # Rank candidates:
            r1 = len(ts_with_q)  # number of MTs containing q
            # r2: number of distinct supports that q's witnessing transversals must hit
            # = number of supports NOT hit by t\{q}, summed/union over t containing q
            supports_not_hit = set()
            for t in ts_with_q:
                tnq = set(t) - {q}
                for i, F in enumerate(supports):
                    if not (set(F) & tnq):
                        supports_not_hit.add(i)
            r2 = len(supports_not_hit)
            # r3: size of avoidance sub-antichain = number of MTs avoiding... let's define
            # number of MTs T (among all) that avoid a fixed p? Hard. Let's use:
            # r3 = number of distinct minimal transversals (size of MT)
            r3 = len(mt)
            # r4: count of residues < M1 "covered" by q
            # residues r in [0, M1) such that some multiple of rad(T) for T containing q
            # is congruent to r. Simplify: r mod M1 where rad(T)\ q ... too complex.
            # Use: number of residues r in [1, M1] with q | r and r in some "hit" class.
            # Skip r4 for now, use count of MTs containing q that are "q-private"
            r4 = len(ts_with_q)  # placeholder
            events.append((n, q, tau, r1, r2, r3, r4, len(supports), len(mt)))
        prev_mt_primes = mt_primes
        prev_mt = mt
    return a, P1, M1, events


def main():
    for a1 in [385, 77, 715, 1309, 2431]:
        print(f"\n===== a_1 = {a1} =====")
        # determine how far to simulate; these stabilize by ~50-200 terms typically
        N = 60
        try:
            a, P1, M1, events = compute_ranks_for_a1(a1, N)
        except Exception as e:
            print(f"  ERROR: {e}")
            continue
        print(f"  P1={sorted(P1)}  M1={M1}")
        print(f"  sequence (first 15): {a[:15]}")
        print(f"  pulled-in events (step, q, tau, r1=#MT_containing_q, r2=#supports_q_must_hit, r3=#MT_total, r4, #supp, #MT):")
        for ev in events:
            n, q, tau, r1, r2, r3, r4, ns, nm = ev
            print(f"    n={n:3d}  q={q:5d}  tau={set(tau[0]) if len(tau[0])<3 else tau[0]},{set(tau[1]) if len(tau[1])<3 else tau[1]}  r1={r1} r2={r2} r3={r3} #supp={ns} #MT={nm}")
        # group by type, check monotonicity of each rank
        from collections import defaultdict
        by_type = defaultdict(list)
        for ev in events:
            n, q, tau, r1, r2, r3, r4, ns, nm = ev
            by_type[tau].append((n, q, r1, r2, r3))
        print(f"  --- monotonicity within fixed type ---")
        for tau, evs in by_type.items():
            if len(evs) >= 2:
                print(f"    TYPE {tau}: {len(evs)} events")
                for (n, q, r1, r2, r3) in evs:
                    print(f"        n={n} q={q} r1={r1} r2={r2} r3={r3}")
                r1_seq = [e[2] for e in evs]
                r2_seq = [e[3] for e in evs]
                r3_seq = [e[4] for e in evs]
                print(f"      r1 strictly decreasing? {all(r1_seq[i] > r1_seq[i+1] for i in range(len(r1_seq)-1))}  seq={r1_seq}")
                print(f"      r2 strictly decreasing? {all(r2_seq[i] > r2_seq[i+1] for i in range(len(r2_seq)-1))}  seq={r2_seq}")
                print(f"      r3 strictly decreasing? {all(r3_seq[i] > r3_seq[i+1] for i in range(len(r3_seq)-1))}  seq={r3_seq}")


if __name__ == "__main__":
    main()
