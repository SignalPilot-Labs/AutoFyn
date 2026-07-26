import sys
from math import gcd
from sympy import primefactors
from functools import reduce
from operator import mul

def rad(n):
    ps = primefactors(n)
    return reduce(mul, ps, 1)

def greedy_naive(a1, N):
    """Correct naive greedy: a_{n+1}=smallest m>a_n with gcd(m,a_i)>1 for all i<=n.
    Uses a running product-of-priors per prime to keep admissibility O(1)-ish."""
    a = [a1]
    # admissibility: m admissible iff for every i<=n, gcd(m,a_i)>1.
    # incremental: track for each prime p, the latest index where some a_i was divisible by p?
    # Simpler: keep list of prior terms; for candidate m compute primefactors(m); m admissible
    # iff every prior a_i shares >=1 prime with m, i.e. for each prior a_i, primefactors(a_i) & primefactors(m) != empty.
    # To make fast: precompute support sets; for m, ms=primefactors(m); admissible iff all(supp_i & ms for supp_i in supports[:n]).
    supps = [frozenset(primefactors(a1))]
    for _ in range(N-1):
        cur = a[-1]
        m = cur + 1
        while True:
            ms = frozenset(primefactors(m))
            if all(ms & s for s in supps):
                a.append(m)
                supps.append(ms)
                break
            m += 1
    return a, supps

def find_period(d, maxlen=None):
    """Fundamental eventual period of d. Accept T iff longest T-periodic suffix
    has length >= max(3T, 50). Returns (T, start) or None."""
    n = len(d)
    if maxlen is None:
        maxlen = n // 3
    best = None
    for T in range(1, maxlen+1):
        if T > n: break
        s = n
        while s - 1 >= T and d[s-1] == d[s-1-T]:
            s -= 1
        suflen = n - s
        if suflen >= max(3*T, 50):
            if best is None or T < best[0]:
                best = (T, s)
    return best

def analyze(a1, N):
    a, supps = greedy_naive(a1, N)
    d = [a[i+1]-a[i] for i in range(len(a)-1)]
    M1 = rad(a1)
    P1 = sorted(primefactors(a1))
    res = find_period(d)
    if res is None:
        return dict(a1=a1, M1=M1, P1=P1, N=N, period=None, d=d, a=a)
    T, start = res
    L = sum(d[start:start+T])
    return dict(a1=a1, M1=M1, P1=P1, N=N, T=T, start=start, L=L, d=d, a=a)

def type_of(dval, P1):
    return frozenset(p for p in P1 if dval % p == 0)

def has_nonP1_prime(av, P1set):
    return any(p not in P1set for p in primefactors(av))

def state_leak(states, dnext_vals):
    from collections import defaultdict
    m = defaultdict(set)
    for s, dn in zip(states, dnext_vals):
        m[s].add(dn)
    conflicts = sum(1 for s,vals in m.items() if len(vals)>1)
    distinct = len(m)
    return conflicts, distinct

def run(a1, N):
    r = analyze(a1, N)
    if r.get('T') is None:
        print(f"a1={a1}: NO PERIOD in {N} terms")
        return r
    T, start, L = r['T'], r['start'], r['L']
    d = r['d']; a = r['a']; M1 = r['M1']; P1 = r['P1']
    P1set = set(P1)
    print(f"\n=== a1={a1}, M1=rad={M1}, P1={P1} ===")
    print(f"  T={T}, L={L}, L/M1={L/M1:.3f}, start={start}, 2^|P1|={2**len(P1)}")
    types = [type_of(d[i], P1) for i in range(len(d))]
    distinct_types = len(set(types))
    print(f"  distinct types realized: {distinct_types} / 2^|P1|={2**len(P1)}")
    # minimal type-seq period in tail
    tper=None
    for tp in range(1, T+1):
        s=len(types)
        while s-1>=tp and types[s-1]==types[s-1-tp]:
            s-=1
        if len(types)-s >= max(3*tp,30):
            tper=tp; break
    print(f"  minimal type-seq period (tail): {tper} (vs T={T})")
    # STATE: (type_n, a_n mod M1) -> d_n
    st1=[(types[i], a[i]%M1) for i in range(len(d))]
    c1,d1=state_leak(st1,d)
    print(f"  STATE (type_n, a_n mod M1): {c1} conflicts, {d1} distinct  [FENCED if c1>0]")
    # STATE: type-window k + a_n mod M1 -> d_n ; minimal k with 0 conflicts
    print("  -- type-window + a_n mod M1, conflicts by k --")
    for k in [1,2,3,4,5,8,12,16,24,32,48,64,96,128]:
        if k+1 > len(d): break
        st=[]; dnl=[]
        for n in range(k-1, len(d)):
            win=tuple(types[n-k+1:n+1])
            st.append((win, a[n]%M1))
            dnl.append(d[n])
        ck,dk=state_leak(st,dnl)
        print(f"     k={k:3d}: {ck:5d} conflicts, {dk:5d} distinct")
        if ck==0:
            print(f"     --> MINIMAL DETERMINISTIC WINDOW k={k}")
            break
    # first repeat of (type_n, a_n mod M1)
    seen={}; fr=None
    for n in range(len(d)):
        s=(types[n],a[n]%M1)
        if s in seen: fr=(seen[s],n); break
        seen[s]=n
    if fr: print(f"  first repeat (type,a mod M1): n={fr[0]}->{fr[1]} gap={fr[1]-fr[0]}")
    else: print(f"  no repeat (type,a mod M1) in {len(d)} steps")
    return r

if __name__=='__main__':
    # verify known cases
    for a1,N in [(15,400),(35,1500),(77,1500),(91,1500),(175,3000)]:
        r=analyze(a1,N)
        print(f"a1={a1}: T={r.get('T')}, L={r.get('L')}, start={r.get('start')}")
