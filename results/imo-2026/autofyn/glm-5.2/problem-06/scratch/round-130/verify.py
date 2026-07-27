import numpy as np
from math import gcd
from sympy import factorint

def gen_seq(a1, N):
    a = [a1]
    for _ in range(N-1):
        an = a[-1]
        cand = an+1
        while True:
            if all(gcd(cand, x)>1 for x in a):
                a.append(cand); break
            cand += 1
    return a

def primes_of(n):
    return set(factorint(n).keys())

def prec_minimals(a):
    # a_m prec a_n iff m<n and rad(a_m)|rad(a_n) i.e. P(a_m) subset P(a_n)
    supp = [primes_of(x) for x in a]
    n = len(a)
    minimals = []
    for i in range(n):
        is_min = True
        for m in range(i):
            if supp[m] <= supp[i]:
                is_min = False; break
        if is_min:
            minimals.append(i)
    return minimals, supp

def M_family(supp):
    # minimal supports under subset
    fam = []
    for s in supp:
        if any(s2 < s for s2 in supp):
            continue
        # is it minimal among all? remove strict subsets
        is_min = not any(s2 < s for s2 in supp)
        # Actually compute minimal family: keep s if no other distinct support is a strict subset
        is_min = not any(s2 < s for s2 in supp)
        fam.append(s)
    # dedupe and minimality
    uniq = []
    for s in fam:
        if s not in uniq:
            uniq.append(s)
    M = []
    for s in uniq:
        if not any(t < s for t in uniq):
            M.append(s)
    return M

seeds = [15,30,175,429,273,210,46189,323,385]
for a1 in seeds:
    a = gen_seq(a1, 400)
    mins, supp = prec_minimals(a)
    maxp = 0
    for i in mins:
        for p in supp[i]:
            maxp = max(maxp, p)
    a1sq = a1*a1
    ok_smooth = maxp <= a1sq
    ok_le_a1 = maxp <= a1
    # Direction B: every M in minimal family is a prec-minimal support
    M = M_family(supp)
    prec_min_supports = set(frozenset(supp[i]) for i in mins)
    dirB = all(frozenset(m) in prec_min_supports for m in M)
    # Direction A: every prec-minimal support in M
    dirA = all(frozenset(s) in set(frozenset(m) for m in M) for s in prec_min_supports)
    print(f"a1={a1}: #prec-min={len(mins)}, maxp={maxp}, <=a1^2={a1sq} ok={ok_smooth}, <=a1={ok_le_a1}, #M={len(M)}, DirB={dirB}, DirA={dirA}")
