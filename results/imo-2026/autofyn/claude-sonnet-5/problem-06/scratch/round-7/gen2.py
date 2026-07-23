import sympy
from sympy import primefactors
import sys

prime_bit = {}
def get_bit(p):
    if p not in prime_bit:
        prime_bit[p] = 1 << len(prime_bit)
    return prime_bit[p]

_factor_cache = {}
def rad_mask_and_set(x):
    if x in _factor_cache:
        return _factor_cache[x]
    ps = primefactors(x)
    mask = 0
    for p in ps:
        mask |= get_bit(p)
    _factor_cache[x] = (mask, frozenset(ps))
    return mask, frozenset(ps)

def generate(a1, N, verbose=False, verbose_every=2000):
    a = [None, a1]
    m1, s1 = rad_mask_and_set(a1)
    radset = [None, s1]
    antichain_masks = [m1]  # minimal antichain masks
    n = 1
    while n < N:
        x = a[n] + 1
        while True:
            rm, rs = rad_mask_and_set(x)
            ok = True
            for m in antichain_masks:
                if not (rm & m):
                    ok = False
                    break
            if ok:
                break
            x += 1
        a.append(x)
        radset.append(rs)
        new_antichain = [m for m in antichain_masks if not ((rm & m)==rm and m!=rm)]  # drop those that are strict supersets of rm (dominated)
        # check if rm itself is dominated by (superset of) something already there, i.e. some m subset of rm
        dominated = any((mm & rm)==mm for mm in new_antichain)
        if not dominated:
            new_antichain.append(rm)
        antichain_masks = new_antichain
        n += 1
        if verbose and n % verbose_every == 0:
            print(f"  n={n}, a_n={x}, antichain size={len(antichain_masks)}", flush=True)
    return a, radset

if __name__ == "__main__":
    a1 = int(sys.argv[1])
    N = int(sys.argv[2])
    import time
    t0=time.time()
    a, radset = generate(a1, N, verbose=True)
    print("done", a1, N, "last value", a[-1], "time", time.time()-t0)
