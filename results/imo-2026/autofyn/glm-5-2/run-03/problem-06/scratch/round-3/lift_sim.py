import sympy
from sympy import factorint, isprime
from functools import lru_cache

def primes_of(n):
    return set(factorint(n).keys())

def greedy_sequence(a1, N=6000):
    """Generate greedy sequence up to N terms."""
    a = [a1]
    for _ in range(N-1):
        an = a[-1]
        m = an + 1
        while True:
            ok = True
            for x in a:
                from math import gcd
                if gcd(m, x) == 1:
                    ok = False
                    break
            if ok:
                break
            m += 1
        a.append(m)
    return a

def rad(n):
    r = 1
    for p in factorint(n):
        r *= p
    return r

def prime_supports(a):
    return [primes_of(x) for x in a]

def detect_period_diff(a):
    """Detect eventual AP: find T,L s.t. a[n+T]=a[n]+L for all n>=n0, from start if possible."""
    N = len(a)
    # try from start
    for T in range(1, N//3):
        L = a[T] - a[0]
        ok = True
        for n in range(1, N - T):
            if a[n+T] - a[n] != L:
                ok = False
                break
        if ok:
            return T, L, 0
    # eventual
    for n0 in range(0, N//3):
        for T in range(1, (N-n0)//3):
            L = a[n0+T] - a[n0]
            ok = True
            for n in range(n0+1, N - T):
                if a[n+T] - a[n] != L:
                    ok = False
                    break
            if ok:
                return T, L, n0
    return None, None, None

def minimal_transversals(family_set):
    """family_set: set of frozensets. Return set of frozenset minimal transversals."""
    # brute force: enumerate subsets of the union
    universe = set()
    for s in family_set:
        universe |= set(s)
    universe = sorted(universe)
    n = len(universe)
    if n > 16:
        return None  # too big
    # transversals: subsets T s.t. T meets every set in family
    # enumerate by size
    from itertools import combinations
    mts = set()
    found_size = None
    for k in range(1, n+1):
        for comb in combinations(range(n), k):
            T = frozenset(universe[i] for i in comb)
            if all(T & s for s in family_set):
                # minimal: no proper subset is a transversal
                # since we go increasing size, check none of already-found mts is subset
                if not any(m <= T for m in mts):
                    mts.add(T)
    return mts

def governing_primes_from_supports(supports):
    """Distinct supports -> MT -> governing primes."""
    distinct = set(frozenset(s) for s in supports)
    mts = minimal_transversals(distinct)
    if mts is None:
        return None
    g = set()
    for t in mts:
        g |= set(t)
    return g, mts

def lift_factors(a1, N=4000):
    a = greedy_sequence(a1, N)
    T, L, n0 = detect_period_diff(a)
    if L is None:
        return None
    # Use a long prefix to stabilize supports; compute B_infty mod L
    # supports from the whole sequence (it's periodic from start per the lemmas)
    sup = prime_supports(a)
    # distinct supports
    distinct = set(frozenset(s) for s in sup)
    gset, mts = governing_primes_from_supports(sup)
    # B_infty = union over MT T of {m: rad(T) | m}
    # A = B_infty mod L
    def in_binfty(m):
        for t in mts:
            rad_t = 1
            for p in t: rad_t *= p
            if m % rad_t == 0:
                return True
        return False
    A = set(r for r in range(L) if in_binfty(r))
    assert len(A) == T, f"|A|={len(A)} != T={T}"
    # order governing primes (include P1 too? G = mts primes; L should = prod(G) if squarefree)
    G = sorted(gset)
    # check L == prod(G)?
    prodG = 1
    for p in G: prodG *= p
    print(f"a1={a1}: T={T}, L={L}, n0={n0}, G={G}, prodG={prodG}, L==prodG? {L==prodG}")
    # build up L_k = product of first k primes of G
    Lk = 1
    prev_Tk = 1  # mod 1, A has 1 element
    print(f"  stage -1: L_k=1, |A_k|={prev_Tk}")
    factors = []
    for i, p in enumerate(G):
        Lk *= p
        Ak = set(r for r in range(Lk) if (in_binfty(r)))  # B_infty mod Lk
        # actually B_infty mod Lk: r in Ak iff some m=r mod Lk is in B_infty; since L|... wait L might != Lk
        # B_infty is L-periodic and Lk|L so B_infty is Lk-periodic; r in Ak iff r (as 0..Lk-1) in_binfty
        Tk = len(Ak)
        ratio = Tk / prev_Tk if prev_Tk else float('inf')
        factors.append((p, Tk, ratio))
        print(f"  stage {i}: add p={p}, L_k={Lk}, |A_k|={Tk}, ratio={ratio:.4f}, bound p={p}, slack={p/ratio:.4f}")
        prev_Tk = Tk
    assert prev_Tk == T
    return T, L, G, factors

for a1 in [6, 30, 385, 1309, 145, 15, 35, 77, 105]:
    print("="*60)
    try:
        lift_factors(a1, N=2000 if a1 < 100 else 4000)
    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback; traceback.print_exc()
