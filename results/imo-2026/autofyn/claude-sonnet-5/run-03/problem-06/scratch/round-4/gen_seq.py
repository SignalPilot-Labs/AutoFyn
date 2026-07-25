import sympy
from sympy import primefactors, gcd, factorint

def gen_sequence(a1, num_terms=2000):
    a = [a1]
    while len(a) < num_terms:
        an = a[-1]
        m = an + 1
        while True:
            ok = True
            for ai in a:
                if gcd(m, ai) == 1:
                    ok = False
                    break
            if ok:
                a.append(m)
                break
            m += 1
    return a

def analyze(a1, num_terms=1500, max_check_period=400):
    a = gen_sequence(a1, num_terms)
    # find period T, L by scanning differences a[n+T]-a[n] constant for n in some range
    n = len(a)
    found = None
    for T in range(1, max_check_period):
        # check if a[i+T]-a[i] is constant for i in last part of the sequence
        # use last 300 terms window
        start = n - 300 - T
        if start < 0:
            continue
        diffs = [a[i+T]-a[i] for i in range(start, n-T)]
        if len(set(diffs)) == 1:
            L = diffs[0]
            # find transient: smallest n0 such that a[i+T]-a[i]=L for all i>=n0
            # search from front
            n0 = None
            for i in range(len(a)-T):
                if a[i+T]-a[i] == L:
                    # verify holds for rest
                    if all(a[j+T]-a[j]==L for j in range(i, len(a)-T)):
                        n0 = i+1  # 1-indexed
                        break
            found = (T, L, n0)
            break
    return a, found

results = {}
for a1 in [4,6,8,9,10,12,14,15,16,20,21,25,30,35,22,26,33,45,50,6*7,2*3*5,105]:
    a, found = analyze(a1)
    results[a1] = found
    T,L,n0 = found if found else (None,None,None)
    # active prime set Q: primes appearing in the "period residues" - primes dividing L, or primes involved
    # compute the set of primes that appear among factors of a[n0-1:n0-1+T] (one period worth, in the periodic part)
    if found:
        period_terms = a[n0-1:n0-1+T]
        Qset = set()
        for t in period_terms:
            Qset |= set(primefactors(t))
        radL = set(primefactors(L)) if L>0 else set()
        rad_a1 = set(primefactors(a1))
        print(f"a1={a1:4d}  T={T:3d} L={L:4d}  n0(transient+1)={n0:4d}  Q(period primes)={sorted(Qset)}  rad(L)={sorted(radL)}  rad(a1)={sorted(rad_a1)}")
    else:
        print(f"a1={a1}: no period found within search bounds")

