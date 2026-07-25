import math
from sympy import primefactors, factorint

def gen_sequence(a1, num_terms=800):
    a = [a1]
    while len(a) < num_terms:
        an = a[-1]
        m = an + 1
        while True:
            ok = True
            for ai in a:
                if math.gcd(m, ai) == 1:
                    ok = False
                    break
            if ok:
                a.append(m)
                break
            m += 1
    return a

def find_period(a, max_check_period=300):
    n = len(a)
    for T in range(1, max_check_period):
        start = n - 200 - T
        if start < 0:
            continue
        diffs = [a[i+T]-a[i] for i in range(start, n-T)]
        if len(set(diffs)) == 1:
            L = diffs[0]
            n0 = None
            for i in range(len(a)-T):
                if a[i+T]-a[i] == L:
                    if all(a[j+T]-a[j]==L for j in range(i, len(a)-T)):
                        n0 = i+1
                        break
            return T, L, n0
    return None

def check_Q_covers(a, Q):
    """Check: for all i<j in range, gcd stuff -- does a_i share a prime in Q with a_j, for all pairs?"""
    Qset = set(Q)
    factors = [set(primefactors(x)) & Qset for x in a]
    bad_pairs = []
    n = len(a)
    for i in range(n):
        if not factors[i]:
            bad_pairs.append((i, "no Q-prime at all"))
            continue
    # check pairwise intersection with ALL others (approx: check pairwise intersection of the whole family: is it pairwise intersecting?)
    for i in range(n):
        for j in range(i+1, n):
            if factors[i] & factors[j]:
                continue
            else:
                bad_pairs.append((i,j))
    return bad_pairs

vals = [4,6,8,9,10,12,14,15,16,20,21,25,30,35,22,26,33,45,50,42,105]
for a1 in vals:
    a = gen_sequence(a1, num_terms=600)
    res = find_period(a)
    if res is None:
        print(a1, "no period found")
        continue
    T,L,n0 = res
    radL = sorted(primefactors(L))
    rad_a1 = sorted(primefactors(a1))
    Q = sorted(set(radL) | set(rad_a1))
    bad = check_Q_covers(a[:400], Q)
    print(f"a1={a1:4d} T={T:3d} L={L:5d} rad(a1)={rad_a1} rad(L)={radL}  Q_used={Q}  #bad_pairs(first400 terms)={len(bad)}  sample_bad={bad[:3]}")
