import math
from sympy import primefactors

def gen_sequence(a1, num_terms):
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

def find_period_robust(a, max_T=400):
    n = len(a)
    for T in range(1, max_T):
        # find earliest n0 (0-indexed) such that a[i+T]-a[i] constant for all i>=n0 within available data
        for n0 in range(0, n-T):
            L = a[n0+T]-a[n0]
            if all(a[i+T]-a[i]==L for i in range(n0, n-T)):
                # require at least 100 confirming terms after n0
                if n-T-n0 >= 150:
                    return T, L, n0+1
                break
    return None

for a1 in [55, 65, 95, 77]:
    a = gen_sequence(a1, 1500)
    res = find_period_robust(a, max_T=200)
    if res:
        T,L,n0 = res
        print(f"a1={a1} T={T} L={L} n0={n0} rad(a1)={sorted(primefactors(a1))} rad(L)={sorted(primefactors(L))}")
    else:
        print(a1, "no robust period found in range")
