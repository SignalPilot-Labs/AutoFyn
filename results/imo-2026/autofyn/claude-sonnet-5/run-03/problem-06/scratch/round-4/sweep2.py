import math
from sympy import primefactors

def gen_sequence(a1, num_terms=1200):
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

def find_period(a, max_check_period=400):
    n = len(a)
    for T in range(1, max_check_period):
        start = n - 300 - T
        if start < 0:
            continue
        diffs = [a[i+T]-a[i] for i in range(start, n-T)]
        if len(set(diffs)) == 1:
            L = diffs[0]
            return T, L
    return None

vals = [9,15,21,25,33,35,39,45,51,55,57,63,65,69,77,85,91,95,99,105,15*7,3*5*7]
for a1 in vals:
    a = gen_sequence(a1, num_terms=1200)
    res = find_period(a)
    rad_a1 = sorted(primefactors(a1))
    if res is None:
        print(f"a1={a1:4d} rad(a1)={rad_a1}  NO PERIOD FOUND in range")
        continue
    T,L = res
    radL = sorted(primefactors(L))
    print(f"a1={a1:4d} rad(a1)={rad_a1}  T={T:4d} L={L:5d} rad(L)={radL}  new_primes={sorted(set(radL)-set(rad_a1))}")
