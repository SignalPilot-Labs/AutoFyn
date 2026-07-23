import sys, time
from sim import gen_sequence
from sympy import primefactors, primerange

def rad_prod(C):
    p=1
    for x in C: p*=x
    return p

def T_C(a1, C):
    prod = rad_prod(C)
    x = prod
    while True:
        if x > a1 and set(primefactors(x)) == set(C):
            return x
        x += prod

def analyze(a1, N):
    a, history = gen_sequence(a1, N)
    prev_set = None
    collapses = []
    for n in range(1, N+1):
        cur = history[n]
        if prev_set is not None and len(cur) < len(prev_set):
            removed = prev_set - cur
            added = cur - prev_set
            collapses.append((n, removed, added))
        prev_set = cur
    ok = True
    report = []
    for n, removed, added in collapses:
        for newc in added:
            Tc = T_C(a1, newc)
            match = (Tc == a[n])
            prodc = rad_prod(newc)
            bound = sum(1 for p in primerange(2, Tc//prodc + 2) if p not in newc)
            observed = len(removed)
            within_bound = observed <= bound
            if not match or not within_bound:
                ok = False
            report.append((n, sorted(newc), Tc, a[n], match, observed, bound, within_bound))
    return ok, report, len(history[N])

tests = [15,35,65,105,143,221,247,375,1001,2431,4087,4199,91,323,1573,2747]
N = 4000
for a1 in tests:
    t0=time.time()
    ok, report, final_size = analyze(a1, N)
    t1=time.time()
    flag = "OK" if ok else "*** VIOLATION ***"
    print(f"a1={a1:>8}  time={t1-t0:5.1f}s  #collapses={len(report):3d}  final|M|={final_size:3d}  {flag}")
    if not ok:
        for row in report:
            print("   ", row)
