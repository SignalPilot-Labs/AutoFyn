import sys, time
import numpy as np

def build_spf(bound):
    spf = np.zeros(bound+1, dtype=np.int64)
    for i in range(2, bound+1):
        if spf[i] == 0:
            spf[i::i] = np.where(spf[i::i]==0, i, spf[i::i])
    return spf

def factor_spf(x, spf):
    fs = set()
    while x > 1:
        p = spf[x]
        if p == 0:
            # x itself is prime, larger than sieve bound reach for its own value
            fs.add(x)
            break
        fs.add(p)
        while x % p == 0:
            x //= p
    return fs

def run(a1, N, S0, bound, report_points, tag):
    spf = build_spf(bound)
    S0set = set(S0)
    prime_bits = {}
    full_mask = 0
    def add_term(x, idx):
        nonlocal full_mask
        for p in factor_spf(x, spf):
            prime_bits[p] = prime_bits.get(p, 0) | (1 << (idx-1))
        full_mask |= (1 << (idx-1))

    add_term(a1, 1)
    n = 1
    c = a1
    new_types = {}
    t0 = frozenset(p for p in factor_spf(a1, spf) if p in S0set)
    new_types[t0] = 1
    report_set = set(report_points)
    results = []
    t_start = time.time()
    while n < N:
        c += 1
        while True:
            if c > bound:
                raise RuntimeError(f"candidate {c} exceeds sieve bound {bound} at n={n}")
            fs = factor_spf(c, spf)
            cov = 0
            for p in fs:
                if p in prime_bits:
                    cov |= prime_bits[p]
            if (cov & full_mask) == full_mask:
                break
            c += 1
        n += 1
        add_term(c, n)
        t = frozenset(p for p in fs if p in S0set)
        if t not in new_types:
            new_types[t] = n
        if n in report_set:
            elapsed = time.time() - t_start
            results.append((n, c, len(new_types), elapsed))
            print(f"[{tag}] n={n} a_n={c} distinct_types={len(new_types)} elapsed={elapsed:.1f}s", flush=True)
    return results, new_types

if __name__ == "__main__":
    which = sys.argv[1]
    N = int(sys.argv[2])
    bound = int(sys.argv[3])
    if which == "4807":
        a1 = 4807
        S0 = [2,3,5,7,11,19,23,73,127]
    elif which == "11305":
        a1 = 11305
        S0 = [2,3,5,7,13,17,19,23,29,37,43,101]
    else:
        raise ValueError(which)
    report_points = sorted(set([25000,50000,100000,200000,300000,400000,500000,750000,1000000,1500000,2000000,2500000,3000000,4000000,5000000]) & set(range(1, N+1)))
    # also always include N itself
    report_points = sorted(set(report_points) | {N})
    results, new_types = run(a1, N, S0, bound, report_points, which)
    print(f"[{which}] FINAL n={N} distinct_types={len(new_types)}")
