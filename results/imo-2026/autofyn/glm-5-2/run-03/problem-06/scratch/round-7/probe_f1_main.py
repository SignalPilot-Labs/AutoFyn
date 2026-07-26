import sys, math
sys.path.insert(0, '/tmp/round-6')
from mt_greedy import sieve_primes, prime_factors, rad, add_set_to_MT, prune_minimal

def greedy_mt_tracked(a1, N, small_primes):
    a=[0]*N; a[0]=a1
    P0=prime_factors(a1,small_primes)
    MT=prune_minimal([{p} for p in P0])
    recs=[]
    def snap(n, m):
        mp=set()
        for t in MT: mp|=set(t)
        recs.append((n,m,len(MT),len(mp),sum(1/q for q in mp),
                     sum(len(t) for t in MT),max((len(t) for t in MT),default=0),
                     sorted(q for q in mp if q>rad(a1))))
    snap(0,a1)
    for step in range(1,N):
        prev=a[step-1]; m=prev+1
        while True:
            Pm=prime_factors(m,small_primes)
            if any(t<=Pm for t in MT): break
            m+=1
        a[step]=m
        MT=add_set_to_MT(MT, prime_factors(m,small_primes))
        snap(step,m)
    return a, recs

def find_period(d):
    n=len(d)
    for T in range(1, n//2):
        ok=True
        for k in range(n-T):
            if d[k+T]!=d[k]: ok=False; break
        if ok: return T
    return None

cases = [15,35,77,91,175,385,847]
sp = sieve_primes(2_000_000)
for a1 in cases:
    M1 = rad(a1)
    # choose N to comfortably exceed n0+T for known cases
    N = {15:60, 35:200, 77:120, 91:120, 175:1200, 385:130000, 847:60000}[a1]
    a, recs = greedy_mt_tracked(a1, N, sp)
    d=[a[i+1]-a[i] for i in range(N-1)]
    T=find_period(d)
    # last record
    last=recs[-1]
    print(f"a1={a1} M1={M1} N={N}: T={T}, n0(last-run-check)")
    print(f"  final: n={last[0]} a={last[1]} |MT|={last[2]} mpc={last[3]} sum1/q={last[4]:.4f} sum|T|={last[5]} max|T|={last[6]}")
    print(f"  mt_primes>M1: {last[7][:20]}" + ('...' if len(last[7])>20 else '') + f" (count={len(last[7])})")
    # monotonicity checks on |MT| and mt_primes_count and sum1/q
    mt_sizes=[r[2] for r in recs]
    mpc=[r[3] for r in recs]
    s1q=[r[4] for r in recs]
    # check if eventually constant
    def ev_const(xs, tail=20):
        v=xs[-1]
        return all(x==v for x in xs[-tail:])
    print(f"  |MT| eventually-const(last20)? {ev_const(mt_sizes)} first5={mt_sizes[:5]} last5={mt_sizes[-5:]}")
    print(f"  mt_primes_count ev-const(last20)? {ev_const(mpc)} first5={mpc[:5]} last5={mpc[-5:]}")
    print(f"  sum1/q ev-const(last20)? {ev_const(s1q)} first5={[round(x,4) for x in s1q[:5]]} last5={[round(x,4) for x in s1q[-5:]]}")
    # monotone (non-decreasing) over last half?
    half=mt_sizes[len(mt_sizes)//2:]
    nd=all(half[i+1]>=half[i] for i in range(len(half)-1))
    print(f"  |MT| non-decr on 2nd half? {nd}")
    half2=mpc[len(mpc)//2:]
    nd2=all(half2[i+1]>=half2[i] for i in range(len(half2)-1))
    print(f"  mt_primes_count non-decr 2nd half? {nd2}")
    # number of distinct values taken by |MT| in stabilized tail
    print(f"  distinct |MT| vals in last {min(50,len(mt_sizes))}: {len(set(mt_sizes[-50:]))}")
    print()
