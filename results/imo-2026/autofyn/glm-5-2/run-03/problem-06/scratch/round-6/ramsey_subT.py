"""Ramsey sub-T structure probe: in the PERIODIC part of d_n, what is the
longest constant-d arithmetic progression with spacing delta NOT a multiple of T?
This tells us whether Ramsey (van der Waerden) gives genuine sub-T structure
that the greedy rule sustains, or whether the only long constant-d APs are the
trivial delta = multiple-of-T ones."""
from mt_greedy import greedy_mt, sieve_primes, rad
import math
from collections import defaultdict


def longest_const_d_AP_excluding_T_mults(d, lo, hi, T, delta_cap=60):
    """Longest const-d AP with delta in [1, delta_cap], delta NOT dividing into a
    full-period coincidence. We just report the best few and whether delta is a
    divisor/multiple-rel of T."""
    best = []
    for delta in range(1, delta_cap + 1):
        if T % delta == 0 or delta % T == 0:
            # delta divides T: in a T-periodic word, delta | T => the word is also
            # delta-periodic only if delta | T AND the word is delta-periodic; but a
            # T-periodic word is delta-periodic iff delta | T. So delta | T gives
            # INFINITE const-d APs (trivial). Skip these.
            continue
        # find longest run d[i]=d[i+delta]=... within [lo,hi)
        cur_best = (0, -1, -1)
        for i in range(lo, hi - delta):
            c = d[i]
            k = 1
            j = i + delta
            while j < hi and d[j] == c:
                k += 1
                j += delta
            if k > cur_best[0]:
                cur_best = (k, delta, c)
        best.append(cur_best)
    best.sort(reverse=True)
    return best[:8]


def forward_det_count(states):
    succ = defaultdict(set)
    for n in range(len(states) - 1):
        succ[states[n]].add(states[n + 1])
    conflicts = sum(1 for k, v in succ.items() if len(v) > 1)
    return conflicts, len(succ)


CASES = [(15, 6000), (35, 6000), (77, 6000), (91, 6000), (175, 20000), (847, 50000)]

for a1, N in CASES:
    M1 = rad(a1)
    sp = sieve_primes(min(a1 + (N + 5) * M1 + 50, 5_000_000))
    a = greedy_mt(a1, N, sp)
    d = [a[i + 1] - a[i] for i in range(N - 1)]
    n = len(d)
    # detect true period with large min_run
    min_run = max(2000, N // 5)
    T = None
    for Tc in range(1, n // 2):
        ok = True
        start = n - min_run
        for k in range(start, n - Tc):
            if d[k + Tc] != d[k]:
                ok = False
                break
        if ok:
            T = Tc
            break
    if T is None:
        print(f"\n=== a1={a1} M1={M1}: no period at N={N} ===")
        continue
    L = sum(d[n - T:n])
    # find n0
    n0 = n - min_run
    while n0 > 0 and all(d[n0 - 1 + j + T] == d[n0 - 1 + j] for j in range(min(min_run, n - n0 - T + 1))):
        n0 -= 1
    print(f"\n=== a1={a1}  M1={M1}  T={T}  n0={n0}  L={L}  N={N} ===")

    # Ramsey sub-T structure in periodic part
    per_lo = max(n0, 0)
    per_hi = n
    delta_cap = min(T - 1, 80)
    best = longest_const_d_AP_excluding_T_mults(d, per_lo, per_hi, T, delta_cap=delta_cap)
    print(f"  Ramsey: longest const-d APs (delta not | T) in periodic part [{per_lo},{per_hi}):")
    for (k, delta, c) in best:
        print(f"    k={k}, delta={delta}, c={c}  (k/delta_ratio={k/delta:.2f} if k>0)")
    # for reference: a delta that IS a divisor of T
    for delta in range(1, min(T, 30)):
        if T % delta == 0:
            cur_best = (0, -1, -1)
            for i in range(per_lo, per_hi - delta):
                c = d[i]; k = 1; j = i + delta
                while j < per_hi and d[j] == c:
                    k += 1; j += delta
                if k > cur_best[0]: cur_best = (k, delta, c)
            print(f"    [delta={delta} DIVIDES T={T}] best k={cur_best[0]}, c={cur_best[2]}  (trivial long AP)")

    # forward-determinism re-check with correct T
    mod_a1 = [x % a1 for x in a]
    mc, mr = forward_det_count(mod_a1)
    print(f"  a_n mod a1={a1}: conflicts={mc}, realized={mr}, fwd-det={mc==0}  (size a1={a1}, T={T}; if fwd-det then period<=a1={a1}, but T={T} {'OK' if T<=a1 else 'CONTRADICTION (T>a1)'})")
