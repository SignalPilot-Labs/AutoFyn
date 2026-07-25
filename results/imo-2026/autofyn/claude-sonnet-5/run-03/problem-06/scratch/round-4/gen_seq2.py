import math
from sympy import primefactors

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

def analyze(a1, num_terms=800, max_check_period=300):
    a = gen_sequence(a1, num_terms)
    n = len(a)
    found = None
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
            found = (T, L, n0)
            break
    return a, found

results = {}
vals = [4,6,8,9,10,12,14,15,16,20,21,25,30,35,22,26,33,45,50,42,30,105]
for a1 in vals:
    a, found = analyze(a1)
    T,L,n0 = found if found else (None,None,None)
    if found:
        period_terms = a[n0-1:n0-1+T]
        Qset = set()
        for t in period_terms:
            Qset |= set(primefactors(t))
        radL = set(primefactors(L)) if L>0 else set()
        rad_a1 = set(primefactors(a1))
        print(f"a1={a1:4d}  T={T:3d} L={L:5d}  n0={n0:4d}  Q(period primes)={sorted(Qset)}  rad(L)={sorted(radL)}  rad(a1)={sorted(rad_a1)}")
    else:
        print(f"a1={a1}: no period found within {max(0,0)} bounds")
