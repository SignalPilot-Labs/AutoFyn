"""Variational/extremal probe for IMO 2026 P6.

Questions:
 (V1) Is the greedy increment-word d the lex-min element of the set D of admissible
      increment-words over alphabet {1,...,M_1}? (Check: at step n, is d_{n+1} the
      smallest d in {1,..,M_1} with a_n+d admissible w.r.t. a_1..a_n?  Trivially yes
      by the greedy rule + gap bound; record it.)
 (V2) Does the set of admissible increments D_n := {d in 1..M_1 : a_n+d admissible}
      stabilize (become periodic) at some index N_stab < N_period?  If yes, what is
      the stabilization width W = N_period - N_stab?  Is W bounded by f(M_1)?
 (V3) Does B_n (as realized via the successor map on the *periodic* residue set A)
      already govern from n=1 (pure-from-start), i.e. is there NO transient in the
      successor map s_infty?  (Already certified yes; re-confirm.)
 (V4) Is the greedy orbit characterized by a slope (asymptotic growth rate L/T) that
      is the MINIMUM over admissible sequences?  (Cannot enumerate all admissible
      sequences; instead check: does the slope L/T equal (sum of D_n-min)/T pattern
      and is the realized d the pointwise min of D_n?)
"""
import math
from collections import defaultdict


def rad(a1):
    fs = set()
    x = a1
    d = 2
    while d * d <= x:
        while x % d == 0:
            fs.add(d)
            x //= d
        d += 1
    if x > 1:
        fs.add(x)
    r = 1
    for p in fs:
        r *= p
    return r, tuple(sorted(fs))


def greedy(a1, N):
    a = [a1]
    for _ in range(N - 1):
        an = a[-1]
        m = an + 1
        while True:
            ok = all(math.gcd(m, x) > 1 for x in a)
            if ok:
                a.append(m)
                break
            m += 1
    return a


def admissible_increments(a, M1):
    """D_n = {d in 1..M1 : a_n+d shares a prime with every a_i, i<=n}."""
    an = a[-1]
    return [d for d in range(1, M1 + 1)
            if all(math.gcd(an + d, x) > 1 for x in a)]


def detect_period(d):
    n = len(d)
    for start in range(0, n // 2):
        for T in range(1, (n - start) // 2):
            ok = True
            for i in range(start, n - T):
                if d[i] != d[i + T]:
                    ok = False
                    break
            if ok:
                return start, T
    return None, None


def stabilization_index(Dn_seq, start, T):
    """Find smallest N_stab >= start such that Dn_seq[n] == Dn_seq[n+T] for all
    n in [N_stab, len(Dn_seq)-T).  Return (N_stab, width=N_period - N_stab)."""
    n = len(Dn_seq)
    for ns in range(start, n - T):
        ok = True
        for i in range(ns, n - T):
            if Dn_seq[i] != Dn_seq[i + T]:
                ok = False
                break
        if ok:
            return ns, (start + T) - ns  # width relative to first periodic index
    return None, None


def main():
    cases = [15, 35, 77, 91, 175, 847]
    for a1 in cases:
        M1, P1 = rad(a1)
        N = 220 if a1 <= 77 else (1600 if a1 <= 175 else 1900)
        a = greedy(a1, N)
        d = [a[n + 1] - a[n] for n in range(len(a) - 1)]
        start, T = detect_period(d)
        L = sum(d[start:start + T]) if T else None
        print(f"\n=== a1={a1}  P1={P1}  M1={M1}  N={N} ===")
        print(f"  period: start={start}, T={T}, L={L}, max_d={max(d)} (<= M1? {max(d)<=M1})")

        # V1: greedy d_{n+1} is min of D_n
        bad = 0
        for n in range(len(a) - 1):
            Dn = admissible_increments(a[:n + 1], M1)
            if d[n] != min(Dn):
                bad += 1
        print(f"  V1 (d_{n+1} = min D_n): {bad} violations / {len(a)-1} steps")

        # V2: D_n stabilization width
        # compute D_n for first ~ (start + 2T) steps (cheap-ish)
        lim = min(len(a) - 1, start + 2 * T) if T else len(a) - 1
        Dn_seq = []
        for n in range(lim):
            Dn = admissible_increments(a[:n + 1], M1)
            Dn_seq.append(tuple(Dn))
        ns, width = stabilization_index(Dn_seq, start if start else 0, T)
        print(f"  V2 (D_n stabilizes to T-periodic): N_stab={ns}, "
              f"width(start+T - N_stab)={width}, T={T}, M1={M1}")
        if ns is not None:
            # how many DISTINCT D_n patterns occur in the stabilized tail?
            distinct = len(set(Dn_seq[ns:ns + T]))
            print(f"      distinct D_n patterns in one stabilized period: {distinct}")
            # is the realized d_n always min(D_n)? (yes by V1) -- does min(D_n) alone pin d_n?
            # i.e. is |D_n| = 1 always once stabilized?  (variational "no slack")
            sizes = [len(Dn_seq[i]) for i in range(ns, ns + T)]
            print(f"      |D_n| sizes in stabilized period: min={min(sizes)}, "
                  f"max={max(sizes)}, all 1? {min(sizes)==1 and max(sizes)==1}")

        # V4: slope
        if T:
            slope = L / T
            print(f"  V4 (slope L/T): {slope:.4f}  (compare M1={M1}, L={L})")


if __name__ == "__main__":
    main()
