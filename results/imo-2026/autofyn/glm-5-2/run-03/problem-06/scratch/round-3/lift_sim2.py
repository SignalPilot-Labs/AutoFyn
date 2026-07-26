import sympy
from sympy import factorint
from math import gcd

def greedy_sequence(a1, N=6000):
    a = [a1]
    for _ in range(N-1):
        an = a[-1]
        m = an + 1
        while True:
            ok = all(gcd(m, x) > 1 for x in a)
            if ok:
                break
            m += 1
        a.append(m)
    return a

def detect_period_diff(a):
    N = len(a)
    for T in range(1, N//4):
        L = a[T] - a[0]
        if L <= 0: continue
        ok = all(a[n+T] - a[n] == L for n in range(N - T))
        if ok:
            return T, L, 0
    return None, None, None

def lift_factors(a1, Nmax=6000):
    a = greedy_sequence(a1, Nmax)
    T, L, n0 = detect_period_diff(a)
    if L is None:
        print(f"a1={a1}: no period found in {Nmax} terms")
        return None
    G = sorted(factorint(L).keys())
    A = set(x % L for x in a)
    print(f"a1={a1}: T={T}, L={L}, G={G}, |A|={len(A)}, squarefree_L={all(e==1 for e in factorint(L).values())}")
    Lk = 1
    prev = 1
    for i, p in enumerate(G):
        Lk *= p
        Ak = set(r % Lk for r in A)
        cur = len(Ak)
        ratio = cur / prev if prev else float('inf')
        print(f"  stage {i}: +p={p:3d}  L_k={Lk:>8d}  |A_k|={cur:>6d}  ratio={ratio:8.4f}  bound=p={p}  slack={p/ratio:.4f}")
        prev = cur
    return T, L, G

for a1 in [6, 30, 385, 1309, 145, 15, 35, 77, 105, 175, 847, 221, 1763]:
    print("="*70)
    try:
        lift_factors(a1, Nmax=3000 if a1 < 200 else 5000)
    except Exception as e:
        print(f"  ERROR: {e}")
