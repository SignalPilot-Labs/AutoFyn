"""
Test the no-lock recursion lemma: "every P1-prime recurs (divides infinitely many terms),
else the sequence locks (a prime power appears)."
Scan many a_1; classify lock vs no-lock; check P1-prime recurrence.
"""
import math
from sympy import factorint


def support(m):
    return frozenset(factorint(m).keys())


def is_prime_power(m):
    f = factorint(m)
    return len(f) == 1  # only one prime factor


def gen_seq_lock_check(a1, K):
    """Generate up to K terms; stop early if a prime power appears (lock).
    Return (seq, locked, lock_prime, lock_index)."""
    a = [a1]
    if is_prime_power(a1):
        return a, True, list(support(a1))[0], 1
    for n in range(1, K):
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
        if is_prime_power(m):
            return a, True, list(support(m))[0], len(a)
    return a, False, None, None


def p1_recurrence(seq, P1, half=True):
    """For each p in P1, does p divide some term in the second half of seq?"""
    n = len(seq)
    start = n // 2 if half else 0
    rec = {}
    for p in P1:
        appears_late = any(p in support(seq[i]) for i in range(start, n))
        # count appearances
        count = sum(1 for s in seq if p in support(s))
        rec[p] = (appears_late, count)
    return rec


def main():
    K = 250
    results = {"lock": [], "nolock": []}
    # scan a_1 from 6 to 3000 that are NOT prime powers (interesting regime)
    for a1 in range(6, 3001):
        f = factorint(a1)
        if len(f) <= 1:
            continue  # prime power -> trivial lock
        P1 = frozenset(f.keys())
        seq, locked, lp, li = gen_seq_lock_check(a1, K)
        if locked:
            results["lock"].append((a1, P1, lp, li))
        else:
            rec = p1_recurrence(seq, P1)
            # check: does every P1-prime recur in second half?
            all_recur = all(rec[p][0] for p in P1)
            dropped = [p for p in P1 if not rec[p][0]]
            results["nolock"].append((a1, P1, all_recur, dropped, rec))

    print(f"Scanned a1 in [6,3000], non-prime-power, K={K} terms.")
    print(f"  LOCK cases: {len(results['lock'])}")
    print(f"  NO-LOCK cases (no prime power in first {K} terms): {len(results['nolock'])}")

    # no-lock cases where some P1-prime does NOT recur in second half
    nolock_dropouts = [r for r in results["nolock"] if not r[2]]
    print(f"\n  NO-LOCK cases with a P1-prime NOT recurring in 2nd half: {len(nolock_dropouts)}")
    for (a1, P1, all_recur, dropped, rec) in nolock_dropouts[:20]:
        detail = {p: rec[p] for p in P1}
        print(f"    a1={a1} P1={set(P1)} dropped={dropped} rec={detail}")

    # do any no-lock cases actually fail to stabilize (truly aperiodic)? hard to tell in K terms.
    # Report: how many no-lock cases have ALL P1-primes recurring
    nolock_all_recur = [r for r in results["nolock"] if r[2]]
    print(f"\n  NO-LOCK cases where ALL P1-primes recur in 2nd half: {len(nolock_all_recur)} / {len(results['nolock'])}")

    # Check the specific claim: in LOCK cases, did exactly one P1-prime survive (lock prime)?
    print(f"\n  LOCK analysis (first 15):")
    for (a1, P1, lp, li) in results["lock"][:15]:
        # in lock, the lock prime lp divides every term from start; do OTHER P1-primes drop?
        seq_short = gen_seq_lock_check(a1, K)[0]
        other_p1 = [p for p in P1 if p != lp]
        # does lp divide every term? (should, by Lemma LOCK)
        lp_all = all(lp in support(s) for s in seq_short)
        # do other P1-primes keep appearing?
        other_recur = {p: sum(1 for s in seq_short if p in support(s)) for p in other_p1}
        print(f"    a1={a1} P1={set(P1)} lock_prime={lp} at term#{li}  lp_divides_all={lp_all}  other_counts={other_recur}")

    # The KEY test: is there any a1 where a P1-prime stops appearing AND no lock occurs (within K terms)?
    # If yes -> lemma potentially false (or just slow lock). If no -> lemma supported.
    print(f"\n  SUMMARY: lemma 'P1-prime drops => lock' — counterexamples (drop + no-lock within {K} terms): {len(nolock_dropouts)}")
    if nolock_dropouts:
        print("  POTENTIAL COUNTEREXAMPLES (need longer run to see if they lock later):")
        for (a1, P1, _, dropped, rec) in nolock_dropouts[:5]:
            print(f"    a1={a1} P1={set(P1)} dropped={dropped}")


if __name__ == "__main__":
    main()
