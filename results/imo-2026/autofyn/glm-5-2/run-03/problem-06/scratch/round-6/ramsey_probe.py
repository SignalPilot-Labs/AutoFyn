"""Ramsey / van-der-Waerden probe for IMO 2026 P6.

For each a_1, compute the greedy sequence (naive correct gcd-greedy), detect the
eventual period T of the increment word d_n, and probe:

  (P1) Longest constant-d arithmetic progression in the TRANSIENT (pre-period) part
       of d_n: indices i, i+delta, ..., i+(k-1)*delta all carrying the same d value.
       Report k_max, delta, c, and k_max vs T.

  (P2) Forward-determinism of candidate states (NOT just f(M_1)-bounded):
       - d_n alone           (f(M_1)-bounded, fenced)
       - window (d_n, d_{n+1}, ..., d_{n+w-1}) for small w
       - a_n mod a_1          (size a_1, NOT a function of M_1=rad(a_1) only)
       - a_n mod (a_1 * M_1)   (a hybrid)
       For each, count "conflict states" (a state with >1 successor).

  (P3) Does a_n mod a_1 forward-determinism HOLD? If yes, period <= a_1 by pigeonhole;
       if actual T > a_1 this is impossible, so it must FAIL. Verify.
"""
import math
from collections import defaultdict


def greedy(a1, N):
    a = [a1]
    for _ in range(N - 1):
        cur = a[-1]
        m = cur + 1
        while True:
            ok = True
            for x in a:
                if math.gcd(m, x) == 1:
                    ok = False
                    break
            if ok:
                a.append(m)
                break
            m += 1
    return a


def diffs(a):
    return [a[i + 1] - a[i] for i in range(len(a) - 1)]


def find_period(d, min_run=200):
    n = len(d)
    for T in range(1, n // 2):
        ok = True
        start = n - min_run
        for k in range(start, n - T):
            if d[k + T] != d[k]:
                ok = False
                break
        if ok:
            n0 = n - min_run
            while n0 > 0 and all(d[n0 - 1 + j + T] == d[n0 - 1 + j]
                                 for j in range(min(min_run, n - n0 - T + 1))):
                n0 -= 1
            return T, n0
    return None, None


def longest_const_d_AP_in_range(d, lo, hi):
    """Longest AP of indices (i, i+delta, ...) within [lo, hi) all carrying same d value.
    Brute force over delta up to some cap and i up to hi."""
    best = (0, 0, 0)  # (k, delta, c)
    cap_delta = min(hi - lo, 400)
    for delta in range(1, cap_delta + 1):
        # for each start i, count run length
        for i in range(lo, hi - delta):
            c = d[i]
            k = 1
            j = i + delta
            while j < hi and d[j] == c:
                k += 1
                j += delta
            if k > best[0]:
                best = (k, delta, c)
    return best


def forward_det_count(states):
    """states: list. Return (# conflict states with >1 successor, #realized states)."""
    succ = defaultdict(set)
    for n in range(len(states) - 1):
        succ[states[n]].add(states[n + 1])
    conflicts = sum(1 for k, v in succ.items() if len(v) > 1)
    return conflicts, len(succ)


def determines_count(states, target):
    """Does `states` determine `target` (same length)?"""
    M = defaultdict(set)
    for n in range(len(states)):
        M[states[n]].add(target[n])
    conflicts = sum(1 for k, v in M.items() if len(v) > 1)
    return conflicts, len(M)


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
    return r


CASES = [15, 35, 77, 91, 175, 847]

for a1 in CASES:
    N = 6000 if a1 <= 200 else 20000
    a = greedy(a1, N)
    d = diffs(a)
    T, n0 = find_period(d, min_run=min(200, N // 4))
    M1 = rad(a1)
    L = sum(d[n0:n0 + T]) if T else None
    print(f"\n=== a1={a1}  M1=rad={M1}  N={N} ===")
    print(f"  T={T}, n0={n0}, L={L}")
    if T is None:
        print("  (no period detected; skip)")
        continue

    # P1: longest constant-d AP in TRANSIENT (pre-period)
    transient_hi = max(n0, 1)
    # search within [0, n0) but also a bit into the periodic part for contrast
    k_tr, delta_tr, c_tr = longest_const_d_AP_in_range(d, 0, transient_hi)
    print(f"  P1 transient [0,{transient_hi}): longest const-d AP k={k_tr}, delta={delta_tr}, c={c_tr}")
    # contrast: in the periodic tail, longest should be ~ unbounded (delta=T gives all)
    k_per, delta_per, c_per = longest_const_d_AP_in_range(d, n0, len(d))
    print(f"  P1 periodic  [{n0},{len(d)}): longest const-d AP k={k_per}, delta={delta_per}, c={c_per}  (expect delta=T => huge)")

    # P2/P3: forward-determinism of candidate states
    # d_n alone
    cd_confl, cd_real = forward_det_count(d)
    print(f"  P2 d_n alone:           conflicts={cd_confl}, realized={cd_real}  (fenced if deterministic)")
    # a_n mod a_1  (size a_1, NOT f(M_1))
    mod_a1 = [x % a1 for x in a]
    ma1_confl, ma1_real = forward_det_count(mod_a1)
    print(f"  P2 a_n mod a1={a1}:     conflicts={ma1_confl}, realized={ma1_real}  (size a1={a1}; T={T}; fwd-det? {ma1_confl==0})")
    # does a_n mod a1 determine d_n (the gap AFTER a_n)?
    det_ma1, _ = determines_count(mod_a1[:-1], d)
    print(f"     a_n mod a1 determines d_n? conflicts={det_ma1}  (==0 would be a Gap-A-fence escape)")
    # a_n mod (a1 * M1)
    mod_hyb = [x % (a1 * M1) for x in a]
    hyb_confl, hyb_real = forward_det_count(mod_hyb)
    print(f"  P2 a_n mod (a1*M1={a1*M1}): conflicts={hyb_confl}, realized={hyb_real}  (size {a1*M1}; fwd-det? {hyb_confl==0})")
    det_hyb, _ = determines_count(mod_hyb[:-1], d)
    print(f"     a_n mod (a1*M1) determines d_(n+1)? conflicts={det_hyb}")
