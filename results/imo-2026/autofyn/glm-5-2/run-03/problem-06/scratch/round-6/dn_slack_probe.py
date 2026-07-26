"""Compute the admissible-increment set D_n in the stabilized periodic regime
for IMO 2026 P6 greedy sequence.

D_n := { d in [1, M1] : a_n + d shares a prime with EVERY prior term a_i, i<=n }.
The greedy rule picks d_{n+1} = min D_n (must be admissible).

We use the NAIVE correct gcd-greedy (no maximal-support pruning; the round-4
fast_greedy.py has an INVERTED subset bug per the run-state rules). Reuse the
structure from /tmp/round-5/probe_coincidence.py.

For each a_1 in {15, 35, 77, 91, 175} we:
  1. compute the greedy orbit (naive),
  2. detect the eventual period (start, T, L) on the increment word d,
  3. over the stabilized tail (one full period past `start`), enumerate D_n
     explicitly and report min / max / mean |D_n| and the fraction of steps
     with |D_n| >= 2.
"""
import math
from collections import defaultdict


def small_primes(a1):
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
    return tuple(sorted(fs))


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


def detect_period(d):
    n = len(d)
    for start in range(0, n // 4):
        for T in range(1, (n - start) // 2):
            ok = True
            for i in range(start, n - T):
                if d[i] != d[i + T]:
                    ok = False
                    break
            if ok:
                return start, T
    return None, None


def compute_Dn(a, n, M1):
    """D_n = {d in [1,M1] : gcd(a_n+d, a_i)>1 for all i<=n}.
    Indexing: a is 0-based, so a[n] is a_{n+1} in problem notation. We compute
    D for the transition from a_n (index n in list, i.e. a_{n+1} in problem)
    to a_{n+1}. To match the explorer's convention (D_n is the increment set
    at step n for a_n -> a_{n+1}), we treat a[list index n] as 'a_n' and the
    prior terms as a[0..n-1] (i.e. a_1..a_n in problem notation shifted by 1).
    For consistency we just compute, for each list-index k (k from 1..len-2),
    the set of d in [1,M1] s.t. a[k]+d shares a prime with every a[i], i<=k.
    """
    an = a[k_index := n]
    priors = a[: n + 1]  # a_0..a_n in list terms = the constraint set
    D = []
    d = 1
    while d <= M1:
        cand = an + d
        if all(math.gcd(cand, x) > 1 for x in priors):
            D.append(d)
        d += 1
    return D


def main():
    cases = [15, 35, 77, 91, 175]
    print("Re-verification of |D_n| slack in the stabilized periodic regime.")
    print("Using naive correct gcd-greedy (NOT the buggy round-4 fast_greedy).")
    print()
    results = {}
    for a1 in cases:
        P1 = small_primes(a1)
        M1 = 1
        for p in P1:
            M1 *= p
        if a1 == 175:
            N = 2500  # T=274 -> need > 2*T after stabilization
        elif a1 == 91:
            N = 200
        elif a1 == 77:
            N = 200
        elif a1 == 35:
            N = 400
        else:
            N = 200
        a = greedy(a1, N)
        d = [a[n + 1] - a[n] for n in range(len(a) - 1)]
        # verify gap bound
        maxd = max(d)
        gb_ok = maxd <= M1
        # verify greedy picks min D_n
        greedy_ok = True
        for k in range(len(a) - 1):
            Dk = compute_Dn(a, k, M1)
            if not Dk:
                greedy_ok = False
                break
            if Dk[0] != d[k]:
                greedy_ok = False
                print(f"  a1={a1} k={k}: greedy picked {d[k]} but min D={Dk[0]}")
                break
        start, T = detect_period(d)
        L = sum(d[start:start + T]) if T else None
        print(f"=== a1={a1}  P1={P1}  M1={M1}  N={N} ===")
        print(f"  period: start={start}, T={T}, L={L}")
        print(f"  gap bound d_n<=M1? {gb_ok} (max d={maxd})")
        print(f"  greedy == min D_n? {greedy_ok}")
        if T is None:
            print("  (no period detected within horizon)")
            continue
        # Sample |D_n| over one full period PAST stabilization
        # (use indices start..start+T-1, which are within the periodic regime)
        sizes = []
        dvals = []
        for k in range(start, start + T):
            Dk = compute_Dn(a, k, M1)
            sizes.append(len(Dk))
            dvals.append(d[k])
        smin, smax, smean = min(sizes), max(sizes), sum(sizes) / len(sizes)
        frac_ge2 = sum(1 for s in sizes if s >= 2) / len(sizes)
        # also over TWO periods for robustness
        sizes2 = []
        for k in range(start, min(start + 2 * T, len(a) - 1)):
            Dk = compute_Dn(a, k, M1)
            sizes2.append(len(Dk))
        smin2, smax2 = min(sizes2), max(sizes2)
        frac2 = sum(1 for s in sizes2 if s >= 2) / len(sizes2)
        print(f"  |D_n| over one period: min={smin} max={smax} mean={smean:.2f}")
        print(f"  fraction with |D_n|>=2 (one period): {frac_ge2:.3f}")
        print(f"  |D_n| over two periods: min={smin2} max={smax2}  frac>=2: {frac2:.3f}")
        # show the sequence of sizes over one period (truncated if long)
        disp = sizes if T <= 40 else sizes[:20] + ['...'] + sizes[-5:]
        print(f"  sizes per step (one period): {disp}")
        print(f"  d_n per step (one period):   {dvals if T<=40 else dvals[:20]+['...']+dvals[-5:]}")
        print()
        results[a1] = dict(M1=M1, T=T, L=L, smin=smin, smax=smax,
                           smean=smean, frac_ge2=frac_ge2,
                           smin2=smin2, smax2=smax2, frac2=frac2,
                           greedy_ok=greedy_ok, gb_ok=gb_ok, N=N)
    print("=== SUMMARY TABLE ===")
    print(f"{'a1':>5} {'M1':>5} {'T':>5} {'L':>6} {'min|D|':>7} {'max|D|':>7} "
          f"{'mean':>6} {'frac>=2':>8} {'min(2P)':>7} {'max(2P)':>7} {'frac2(2P)':>9} "
          f"{'greedy=minD':>11} {'d<=M1':>6}")
    for a1, r in results.items():
        print(f"{a1:>5} {r['M1']:>5} {r['T']:>5} {r['L']:>6} {r['smin']:>7} "
              f"{r['smax']:>7} {r['smean']:>6.2f} {r['frac_ge2']:>8.3f} "
              f"{r['smin2']:>7} {r['smax2']:>7} {r['frac2']:>9.3f} "
              f"{str(r['greedy_ok']):>11} {str(r['gb_ok']):>6}")


if __name__ == "__main__":
    main()
