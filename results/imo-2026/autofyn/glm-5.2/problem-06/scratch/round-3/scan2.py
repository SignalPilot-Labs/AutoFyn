import math, sys, itertools, time
sys.path.insert(0, '/tmp/round-3')
from probe_fs import spf_table, factor, minimal_family_inc, mtp_of, common

N = 600000
spf = spf_table(N)

def cheap_transversal_product(M):
    """Upper bound on mtp: union of min-prime of each member. Valid transversal."""
    s = set()
    for mm in M:
        if mm: s.add(min(mm))
    p = 1
    for q in s: p *= q
    return p

def run_fast(a1, Nmax, spf, stable_window=60):
    a = [a1]; P1 = factor(a1, spf); M = [P1]; Pess = set(P1); gaps = []
    bound_cached = cheap_transversal_product(M)
    last_repr = tuple(sorted([tuple(sorted(s)) for s in M])); stable = 0
    entering_total = set()
    for n in range(1, Nmax):
        an = a[-1]
        bnd = bound_cached
        m = an + 1
        while m <= an + bnd:
            Pm = factor(m, spf)
            if all(Pm & Mm for Mm in M): break
            m += 1
        a.append(m); gaps.append(m - an)
        new_P = factor(m, spf); new_M = minimal_family_inc(M, new_P)
        if set(new_M) != set(M):
            entering_total |= (set(new_P) - Pess)
            Pess = set()
            for S in new_M: Pess |= set(S)
            bound_cached = cheap_transversal_product(new_M)
        M = new_M
        r = tuple(sorted([tuple(sorted(s)) for s in M]))
        if r == last_repr: stable += 1
        else: stable = 0; last_repr = r
        if stable >= stable_window: break
    return a, gaps, M, Pess, entering_total

# verify fast-vs-exact on 3 seeds against the exact run
from probe_fs import run as run_exact
print("=== verify cheap-bound greedy == exact greedy ===")
for a1 in [15, 105, 1001]:
    a1=15 if a1==15 else a1
    rf = run_fast(a1, 100, spf, stable_window=40)
    re = run_exact(a1, 100, spf, stable_window=40)
    print(f"a1={a1}: fast==exact? {rf[0]==re['a']}, maxgap_fast={max(rf[1])}, maxgap_exact={max(re['gaps'])}")
