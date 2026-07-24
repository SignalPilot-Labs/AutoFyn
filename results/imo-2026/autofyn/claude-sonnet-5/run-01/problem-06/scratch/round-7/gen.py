import sympy
from sympy import factorint, primefactors

def rad_set(x, cache={}):
    if x in cache:
        return cache[x]
    f = set(primefactors(x))
    cache[x] = f
    return f

def generate(a1, N, verbose=False):
    a = [None, a1]
    rad = [None, rad_set(a1)]
    # minimal antichain of radicals (list of frozensets), each corresponds to some index but we just need the antichain condition
    # admissibility: candidate x admissible against prefix a_1..a_n iff rad(x) intersects rad(a_i) for every i<=n
    # equivalent to: rad(x) intersects every element of the *minimal* antichain of {rad(a_i): i<=n} (since if it hits a subset it hits supersets)
    antichain = [rad[1]]  # list of frozensets, minimal ones
    n = 1
    while n < N:
        x = a[n] + 1
        while True:
            rx = rad_set(x)
            if all(rx & m for m in antichain):
                break
            x += 1
        a.append(x)
        rad.append(rx)
        # update antichain: remove any dominated (superset of rx), add rx if not superset of existing
        if not any(m <= rx for m in antichain):  # rx not a superset of (or equal to) existing minimal elt... actually need: only add if no existing m subset of rx
            pass
        # proper update:
        new_antichain = [m for m in antichain if not (rx < m)]  # remove those strictly dominated by rx (m superset of rx, m != rx)
        if not any(m <= rx for m in new_antichain):
            new_antichain.append(rx)
        antichain = new_antichain
        n += 1
        if verbose and n % 1000 == 0:
            print(f"  n={n}, a_n={x}, antichain size={len(antichain)}")
    return a, rad

if __name__ == "__main__":
    import sys
    a1 = int(sys.argv[1])
    N = int(sys.argv[2])
    a, rad = generate(a1, N, verbose=True)
    print("done", a1, N, "last value", a[-1])
