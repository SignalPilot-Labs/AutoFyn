import sys
from fast_greedy_correct import greedy_fast, rad

a1 = 847
N = 50000
a = greedy_fast(a1, N)
d = [a[i+1]-a[i] for i in range(N-1)]
n = len(d)
M1 = rad(a1)
# detect with multiple min_run thresholds
for min_run in [300, 1000, 3000, 10000]:
    found = None
    for T in range(1, n//2):
        ok = True
        start = n - min_run
        for k in range(start, n - T):
            if d[k+T] != d[k]:
                ok = False
                break
        if ok:
            n0 = n - min_run
            while n0 > 0 and all(d[n0-1+j+T]==d[n0-1+j] for j in range(min(min_run, n-n0-T+1))):
                n0 -= 1
            found = (T, n0)
            break
    T, n0 = found if found else (None, None)
    L = sum(d[n0:n0+T]) if T else None
    print(f"min_run={min_run}: T={T}, n0={n0}, L={L}")
# also test whether 1744 is a period at all anywhere in tail
for candT in [297, 594, 891, 1188, 1485, 1744, 1782, 2087, 2376]:
    # count longest suffix where d[k+candT]==d[k]
    run = 0
    k = n - 1 - candT
    while k >= 0 and d[k+candT]==d[k]:
        run += 1
        k -= 1
    print(f"  candidate T={candT}: longest suffix run = {run}")
