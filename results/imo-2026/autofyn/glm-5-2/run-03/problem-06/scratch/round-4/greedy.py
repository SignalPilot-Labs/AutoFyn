import sys
from math import gcd

def greedy(a1, N):
    a = [a1]
    for _ in range(N-1):
        cur = a[-1]
        m = cur + 1
        while True:
            ok = True
            for x in a:
                if gcd(m, x) == 1:
                    ok = False
                    break
            if ok:
                a.append(m)
                break
            m += 1
    return a

def diffs(a):
    return [a[i+1]-a[i] for i in range(len(a)-1)]

def find_period(d, min_run=200):
    """find T such that d[n+T]==d[n] for min_run consecutive n, in tail."""
    n = len(d)
    for T in range(1, n//2):
        # check tail
        ok = True
        start = n - min_run
        for k in range(start, n-T):
            if d[k+T] != d[k]:
                ok = False
                break
        if ok:
            # find earliest n0 where it becomes periodic
            n0 = n - min_run
            while n0 > 0 and all(d[n0-1+j+T]==d[n0-1+j] for j in range(min(min_run, n-n0-T+1))):
                n0 -= 1
            return T, n0
    return None, None

if __name__ == '__main__':
    for a1 in [15, 35, 77, 91, 143, 175, 385, 847, 1309, 2085]:
        N = 4000 if a1 <= 200 else 8000
        a = greedy(a1, N)
        d = diffs(a)
        T, n0 = find_period(d, min_run=150)
        L = sum(d[n0:n0+T]) if T else None
        print(f"a1={a1}: T={T}, n0={n0}, L={L}, M1=rad={__import__('math').prod(sorted(set(__import__('sympy').factorint(a1))))}")
