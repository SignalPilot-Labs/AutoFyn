import sys

def factorize(m, cache={}):
    if m in cache: return cache[m]
    orig=m
    f=set()
    d=2
    while d*d<=m:
        if m%d==0:
            f.add(d)
            while m%d==0: m//=d
        d+=1 if d==2 else 2
    if m>1: f.add(m)
    cache[orig]=f
    return f

def simulate(a1, N):
    """Returns seq (1-indexed list of length N) using bitmask coverage."""
    seq=[a1]
    prime_masks = {}  # prime -> bitmask, bit (i-1) set if prime | seq[i-1]
    full_mask = 0
    def add_term(idx, val):
        nonlocal full_mask
        bit = 1 << idx
        full_mask |= bit
        for p in factorize(val):
            prime_masks[p] = prime_masks.get(p, 0) | bit
    add_term(0, a1)
    for n in range(1, N):
        c = seq[-1] + 1
        while True:
            f = factorize(c)
            mask = 0
            for p in f:
                mask |= prime_masks.get(p, 0)
            if mask == full_mask:
                break
            c += 1
        seq.append(c)
        add_term(n, c)
    return seq

if __name__ == "__main__":
    import time
    t0=time.time()
    seq = simulate(15, 20)
    print(seq)
    print(time.time()-t0)
