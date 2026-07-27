import sys, itertools, math, signal
from sympy import factorint

def primes_of(n):
    return set(factorint(n).keys())

def prod(lst):
    r = 1
    for x in lst: r *= x
    return r

class TimeoutErr(Exception): pass

def _handler(sig, frame):
    raise TimeoutErr()

def transversals_via_choices(P_ess_set, Mlist, cap=200000):
    """Enumerate transversals (hitting sets) by picking one prime per M. Yield distinct sets. Cap count."""
    seen = set()
    Mlist = [list(set(m)) for m in Mlist]
    # sort each M's primes, and sort Mlist by size ascending to prune faster
    Mlist.sort(key=len)
    count = [0]
    def rec(idx, cur):
        if count[0] > cap:
            return
        if idx == len(Mlist):
            fs = frozenset(cur)
            if fs not in seen:
                seen.add(fs)
                count[0] += 1
                yield fs
            return
        for p in Mlist[idx]:
            if count[0] > cap:
                return
            cur.add(p)
            yield from rec(idx+1, cur)
            cur.discard(p)
    yield from rec(0, set())

def transversals_avoiding(P_ess_set, Mlist, cap=200000):
    Msets = [set(m) for m in Mlist]
    for T in transversals_via_choices(P_ess_set, Msets, cap):
        if not any(m <= T for m in Msets):
            yield T

def is_stable(P_ess_set, Mlist):
    return not any(True for _ in transversals_avoiding(P_ess_set, Mlist, cap=1))

def next_promotion(a, P_ess_list, Mlist):
    Peset = set(P_ess_list)
    best_m = None; best_T = None
    for T in transversals_avoiding(P_ess_list, Mlist, cap=200000):
        D = prod(sorted(T))
        S_primes = [p for p in P_ess_list if p not in T]
        S = prod(S_primes) if S_primes else 1
        K0 = a // D
        k = K0 + 1
        cap = 0
        while math.gcd(k, S) != 1:
            k += 1; cap += 1
            if cap > 500000:
                k = None; break
        if k is None: continue
        m = k * D
        if best_m is None or m < best_m:
            best_m = m; best_T = T
    if best_m is None:
        return None
    Pnew = primes_of(best_m)
    return best_m, best_T, Pnew

def run(a1, max_rounds=300, max_Pess=18, time_limit=12):
    signal.signal(signal.SIGALRM, _handler)
    signal.alarm(time_limit)
    M = [frozenset(primes_of(a1))]
    P_ess = sorted(M[0])
    a = a1
    history = []
    try:
        for rnd in range(max_rounds):
            if len(P_ess) > max_Pess:
                return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), stable=None,
                            rounds=rnd, history=history, reason='Pess_exceeded', a=a)
            if is_stable(P_ess, [set(m) for m in M]):
                L = prod(P_ess)
                return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), L=L, stable=True,
                            rounds=rnd, history=history, reason='stable', a=a)
            res = next_promotion(a, P_ess, [set(m) for m in M])
            if res is None:
                L = prod(P_ess)
                return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), L=L, stable=True,
                            rounds=rnd, history=history, reason='stable', a=a)
            m, T_star, Pnew = res
            old = set(P_ess)
            newM = []
            for mm in M:
                if Pnew <= set(mm): continue
                newM.append(set(mm))
            newM.append(set(Pnew))
            M = [frozenset(x) for x in newM]
            P_ess = sorted(set(P_ess) | Pnew)
            a = m
            history.append(dict(a=a, M=len(M), Pess=len(P_ess), Tstar=sorted(T_star),
                                newpr=sorted(Pnew-old)))
        return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), stable=False,
                    rounds=max_rounds, history=history, reason='max_rounds', a=a)
    except TimeoutErr:
        return dict(a1=a1, M=[set(m) for m in M], P_ess=set(P_ess), stable=None,
                    rounds=-1, history=history, reason='timeout', a=a)
    finally:
        signal.alarm(0)

if __name__ == '__main__':
    from sympy import primerange
    import itertools as it
    sp = list(primerange(2, 60))
    print("=== omega=2 ===")
    rows=[]
    for p,q in it.combinations(sp, 2):
        a1 = p*q
        r = run(a1, time_limit=15)
        flag = 'STABLE' if r['stable'] else ('CAP' if r['stable'] is None else 'UNSTABLE')
        rows.append((a1,p,q,flag,len(r['P_ess']),len(r['M']),r['rounds'],r.get('reason')))
    for a1,p,q,flag,pe,ms,rd,rs in rows:
        print(f"a1={a1} ({p},{q}): {flag} |Pess|={pe} |M|={ms} rounds={rd} {rs}")
    print("max |Pess| for omega=2 stable:", max((pe for _,_,_,fl,pe,_,_,_ in rows if fl=='STABLE'), default='none'))

print()
print("=== omega=2 LARGE PRIME pairs (cap raised) ===")
from sympy import prime
# test pairs of large primes to see if |Pess| grows unboundedly
tests = [(prime(i), prime(j)) for i,j in [(25,26),(30,40),(50,60),(60,80),(80,100),(100,120),(150,160)]]
for p,q in tests:
    a1 = p*q
    r = run(a1, max_rounds=400, max_Pess=40, time_limit=40)
    flag = 'STABLE' if r['stable'] else ('CAP' if r['stable'] is None else 'UNSTABLE')
    print(f"a1={a1} ({p},{q}): {flag} |Pess|={len(r['P_ess'])} |M|={len(r['M'])} rounds={r['rounds']} {r.get('reason')}")
