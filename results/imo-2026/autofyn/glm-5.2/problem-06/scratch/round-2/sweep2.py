import sys, itertools, math
from sympy import factorint
from functools import reduce

def primes_of(n):
    return set(factorint(n).keys())

def prod(lst):
    r = 1
    for x in lst:
        r *= x
    return r

def transversals_avoiding_M(P_ess_list, Mlist):
    """Yield subsets T of P_ess that (a) hit every M in Mlist (transversal) and (b) contain no M as subset."""
    n = len(P_ess_list)
    Msets = [set(m) for m in Mlist]
    Peset = set(P_ess_list)
    # enumerate subsets by bitmask
    for mask in range(1, 1<<n):
        T = set()
        for i in range(n):
            if mask & (1<<i):
                T.add(P_ess_list[i])
        # transversal?
        ok = True
        for m in Msets:
            if not (T & m):
                ok = False; break
        if not ok:
            continue
        # avoids M (no M subset of T)?
        avoid = not any(m <= T for m in Msets)
        if avoid:
            yield T

def is_stable(P_ess_list, Mlist):
    """Stable iff every transversal contains some M (no transversal avoids M)."""
    return not any(True for _ in transversals_avoiding_M(P_ess_list, Mlist))

def next_promotion(a, P_ess_list, Mlist):
    """Return (m, T_star, Pnew) where m = smallest promoting value > a, T_star = essential part, Pnew = full prime set of m.
    Returns None if stable (no transversal avoids M)."""
    Peset = set(P_ess_list)
    best_m = None
    best_T = None
    for T in transversals_avoiding_M(P_ess_list, Mlist):
        D = prod(T)
        S_primes = [p for p in P_ess_list if p not in T]
        S = prod(S_primes) if S_primes else 1
        K0 = a // D
        # find smallest k > K0 with gcd(k, S)==1
        k = K0 + 1
        cap = 0
        while math.gcd(k, S) != 1:
            k += 1
            cap += 1
            if cap > 2000000:
                k = None; break
        if k is None:
            continue
        m = k * D
        if best_m is None or m < best_m:
            best_m = m
            best_T = T
    if best_m is None:
        return None  # stable
    Pnew = primes_of(best_m)
    return best_m, best_T, Pnew

def run(a1, max_rounds=200, max_Pess=22, verbose=False):
    M = [frozenset(primes_of(a1))]
    P_ess = sorted(M[0])
    a = a1
    history = []
    for rnd in range(max_rounds):
        if len(P_ess) > max_Pess:
            return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), stable=None,
                        rounds=rnd, history=history, reason='Pess_exceeded')
        # stable?
        if is_stable(P_ess, [set(m) for m in M]):
            L = prod(P_ess)
            return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), L=L, stable=True,
                        rounds=rnd, history=history, reason='stable')
        res = next_promotion(a, P_ess, [set(m) for m in M])
        if res is None:
            L = prod(P_ess)
            return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), L=L, stable=True,
                        rounds=rnd, history=history, reason='stable')
        m, T_star, Pnew = res
        old_Pess = set(P_ess)
        # refine M: remove supersets of Pnew, add Pnew
        newM = []
        for mm in M:
            if Pnew <= set(mm):
                continue
            newM.append(set(mm))
        newM.append(set(Pnew))
        M = [frozenset(x) for x in newM]
        P_ess = sorted(set(P_ess) | Pnew)
        a = m
        new_primes = sorted(Pnew - old_Pess)
        history.append(dict(a=a, M_size=len(M), Pess_size=len(P_ess), T_star=sorted(T_star), new_primes=new_primes))
        if verbose:
            print(f"  r{rnd}: a={a} |M|={len(M)} |Pess|={len(P_ess)} T*={sorted(T_star)} new={new_primes}")
    return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), stable=False,
                rounds=max_rounds, history=history, reason='max_rounds')

if __name__ == '__main__':
    from sympy import primerange
    import itertools as it
    sp = list(primerange(2, 60))
    print("=== omega=2 ===")
    for p,q in it.combinations(sp, 2):
        a1 = p*q
        r = run(a1)
        flag = 'STABLE' if r['stable'] else ('CAP' if r['stable'] is None else 'UNSTABLE')
        print(f"a1={a1} ({p},{q}): {flag} |Pess|={len(r['P_ess'])} |M|={len(r['M'])} rounds={r['rounds']} reason={r.get('reason')}")
