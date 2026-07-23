from fractions import Fraction as F
import itertools

def e_of(sorted_desc):
    # alternating sum with signs +,-,+,-...
    s = F(0)
    sign = 1
    for x in sorted_desc:
        s += sign*x
        sign = -sign
    return s

def e_multiset(vals):
    sv = sorted(vals, reverse=True)
    return e_of(sv)

def piecewise_check(D, i, j, ell_candidates):
    """D: list of ints (dyadic construction), i,j indices of tied pieces, rest untouched.
    Compute e({D[i]-t, D[j]-t} U rest) as function of t over breakpoints, find min.
    """
    rest = [D[k] for k in range(len(D)) if k not in (i,j)]
    ai, aj = D[i], D[j]
    # domain of t: 0 <= t < min(ai,aj)  (both must remain positive after cut, roughly)
    tmax = min(ai,aj)
    # breakpoints: where ai-t or aj-t crosses one of 'rest' values, or hits 0, or ai-t=aj-t (t=... always equal since both shift by t... wait ai-t and aj-t, sorted order between them is fixed (ai>aj so ai-t>aj-t always, no crossing between them)
    # breakpoints where ai-t crosses a rest value r: t = ai-r; similarly aj-t crosses r: t=aj-r
    bps = set([F(0), F(tmax)])
    for r in rest:
        t1 = ai-r
        if 0 <= t1 <= tmax: bps.add(F(t1))
        t2 = aj-r
        if 0 <= t2 <= tmax: bps.add(F(t2))
    bps = sorted(bps)
    # sample midpoints of each interval plus breakpoints themselves (use epsilon via fractions - sample slightly inside)
    samples = []
    for b in bps:
        samples.append(b)
    for k in range(len(bps)-1):
        mid = (bps[k]+bps[k+1])/2
        samples.append(mid)
    results = []
    for t in samples:
        vals = [ai-t, aj-t] + rest
        val = e_multiset(vals)
        results.append((t, val))
    # find min
    minval = min(v for t,v in results)
    minters = [t for t,v in results if v==minval]
    return bps, results, minval, minters, rest

# Test on D_2=(4,2,1)
D2 = [4,2,1]
for (i,j) in itertools.combinations(range(3),2):
    bps, results, minval, minters, rest = piecewise_check(D2, i, j, None)
    print("D2", D2, "pair", (D2[i],D2[j]), "rest(untouched)", rest, "breakpoints", bps)
    print("   results:", results)
    print("   min value:", minval, "achieved at t in:", minters)

print()
print("=== D_3 = (8,4,2,1) ===")
D3 = [8,4,2,1]
for (i,j) in itertools.combinations(range(4),2):
    bps, results, minval, minters, rest = piecewise_check(D3, i, j, None)
    print("pair", (D3[i],D3[j]), "rest(untouched)", rest, "breakpoints", bps)
    print("   min value:", minval, "achieved at t in:", minters)

print()
print("=== D_4 = (16,8,4,2,1) ===")
D4 = [16,8,4,2,1]
for (i,j) in itertools.combinations(range(5),2):
    bps, results, minval, minters, rest = piecewise_check(D4, i, j, None)
    print("pair", (D4[i],D4[j]), "rest(untouched)", rest, "min value:", minval, "achieved at t in:", minters)
