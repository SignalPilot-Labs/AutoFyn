import sympy, time
from math import gcd

def fast_greedy_full(a1, N, track_minimal_every=0):
    a = [a1]
    minimal = [frozenset(sympy.primefactors(a1))]
    minimal_history = []
    for step in range(N-1):
        cur = a[-1]; m = cur + 1
        while True:
            ms = frozenset(sympy.primefactors(m))
            if all(ms & S for S in minimal):
                a.append(m)
                if not any(S <= ms for S in minimal):
                    minimal = [S for S in minimal if not (ms <= S)]
                    minimal.append(ms)
                break
            m += 1
        if track_minimal_every and (step+1) % track_minimal_every == 0:
            minimal_history.append((step+1, len(minimal), set(minimal)))
    return a, minimal, minimal_history

# a1=385: run to N=12000, check period, minimal supports, window determinism
t0=time.time()
a, minimal, mh = fast_greedy_full(385, 12000, track_minimal_every=2000)
print(f"385 done in {time.time()-t0:.1f}s, len={len(a)}, last={a[-1]}")
print("final #minimal supports:", len(minimal))
print("minimal supports:", sorted([sorted(s) for s in minimal]))
# period detection
d = [a[i+1]-a[i] for i in range(len(a)-1)]
n=len(d)
# find T with longest tail run
best=None
for T in range(5080, 5100):
    run=0; i=n-1
    while i-T>=0 and d[i]==d[i-T]:
        run+=1; i-=1
    if run>1000:
        L=sum(d[i:i+T])
        print(f"T={T}, run={run}, n0~={i}, L={L}, factors={sympy.factorint(L)}")
        if best is None or run>best[1]: best=(T,run,i,L)
# minimal support count over time
print("minimal history:")
for step,cnt,sups in mh:
    print(f"  n={step}: #minimal={cnt}, max prime in any minimal support={max((max(s) for s in sups if s), default=0)}")
