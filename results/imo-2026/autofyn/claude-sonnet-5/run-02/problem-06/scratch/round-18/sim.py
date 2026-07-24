import sys, time

def sieve_primes(limit):
    is_p = bytearray([1])*(limit+1)
    is_p[0]=is_p[1]=0
    for i in range(2,int(limit**0.5)+1):
        if is_p[i]:
            for j in range(i*i, limit+1, i):
                is_p[j]=0
    return [i for i in range(2,limit+1) if is_p[i]]

PRIMES = sieve_primes(200000)  # covers factoring numbers up to 200000^2=4e10

def factor(c):
    primes = []
    x = c
    for p in PRIMES:
        if p*p > x:
            break
        if x % p == 0:
            primes.append(p)
            while x % p == 0:
                x //= p
    if x > 1:
        primes.append(x)
    return primes

def simulate(a1, N, report_every=20000, time_budget=None):
    t0=time.time()
    a = [None, a1]  # 1-indexed
    bitmask = {}  # prime -> int bitmask of indices with that prime factor
    full_mask = 0
    f1 = factor(a1)
    for p in f1:
        bitmask[p] = bitmask.get(p,0) | (1<<1)
    full_mask |= (1<<1)
    n = 1
    types = {}  # base type tuple(sorted Q-part) -> list of n where occurs (we'll compute Q part = intersection with set(f1))
    Q = set(f1)
    def qtype(c_primes):
        return tuple(sorted(set(c_primes) & Q))
    types.setdefault(qtype(f1), []).append(1)
    while n < N:
        c = a[n] + 1
        while True:
            fc = factor(c)
            m = 0
            for p in fc:
                bm = bitmask.get(p)
                if bm:
                    m |= bm
            if m == full_mask:
                break
            c += 1
        n += 1
        a.append(c)
        for p in fc:
            bitmask[p] = bitmask.get(p,0) | (1<<n)
        full_mask |= (1<<n)
        types.setdefault(qtype(fc), []).append(n)
        if n % report_every == 0:
            elapsed = time.time()-t0
            print(f"n={n} a_n={c} elapsed={elapsed:.1f}s", file=sys.stderr)
            if time_budget and elapsed > time_budget:
                print("TIME BUDGET EXCEEDED, stopping early", file=sys.stderr)
                break
    return a, types, Q

if __name__ == "__main__":
    import json
    a1 = int(sys.argv[1])
    N = int(sys.argv[2])
    time_budget = float(sys.argv[3]) if len(sys.argv)>3 else None
    a, types, Q = simulate(a1, N, time_budget=time_budget)
    print(f"Q={sorted(Q)}", file=sys.stderr)
    # report on the target type
    target = tuple(sorted({5,7,11,13,17}))
    occ = types.get(target, [])
    print(f"target type {target} occurrences: {occ}", file=sys.stderr)
    # also list types with exactly 1 occurrence
    singles = {k:v for k,v in types.items() if len(v)==1}
    print(f"num single-occurrence types (out of {len(types)} total types): {len(singles)}", file=sys.stderr)
    for k,v in sorted(singles.items()):
        print(f"  single: {k} at n={v}", file=sys.stderr)
