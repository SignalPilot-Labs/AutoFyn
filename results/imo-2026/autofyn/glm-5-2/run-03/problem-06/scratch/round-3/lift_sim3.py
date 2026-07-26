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

def distinct_supports(a):
    return set(frozenset(factorint(x).keys()) for x in a)

def compute_A_from_supports(supports, L):
    """A = {r in [0,L): r's prime-support hits every support in 'supports'}.
    r=0 treated as having support = primes of L."""
    G = sorted(factorint(L).keys())
    Gset = set(G)
    sups = list(supports)
    A = []
    for r in range(L):
        if r == 0:
            Sr = Gset
        else:
            Sr = set(factorint(r).keys())
        if all(Sr & s for s in sups):
            A.append(r)
    return set(A)

def lift_factors_via_supports(a1, N=2500):
    a = greedy_sequence(a1, N)
    # distinct supports
    ds = distinct_supports(a)
    print(f"a1={a1}: {N} terms, {len(ds)} distinct supports")
    # need L. Use known/candidate L. Try to detect from data table.
    known_L = {
        385: 43890,
        847: 2*3*7*11*41,   # = 19404
        1763: 2*3*7*41*43,
    }
    if a1 not in known_L:
        # detect period
        T, L, _ = None, None, None
        Na = len(a)
        for Tc in range(1, Na//4):
            Lc = a[Tc]-a[0]
            if Lc<=0: continue
            if all(a[n+Tc]-a[n]==Lc for n in range(Na-Tc)):
                T,L = Tc,Lc
                break
        if L is None:
            print(f"  no period; skip")
            return None
    else:
        L = known_L[a1]
    G = sorted(factorint(L).keys())
    # compute A
    A = compute_A_from_supports(ds, L)
    print(f"  L={L}, G={G}, |A|={len(A)}")
    Lk=1; prev=1
    for i,p in enumerate(G):
        Lk *= p
        Ak = set(r % Lk for r in A)
        cur = len(Ak)
        ratio = cur/prev if prev else float('inf')
        print(f"  stage {i}: +p={p:3d}  L_k={Lk:>8d}  |A_k|={cur:>6d}  ratio={ratio:8.4f}  bound=p={p}  slack={p/ratio:.4f}")
        prev=cur

for a1 in [385, 847]:
    print("="*70)
    lift_factors_via_supports(a1, N=2200)
