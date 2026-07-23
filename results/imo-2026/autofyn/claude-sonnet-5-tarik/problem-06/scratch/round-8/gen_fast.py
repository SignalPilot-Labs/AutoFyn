import sys, json, time
from sympy import factorint

def rad(x, cache={}):
    r = cache.get(x)
    if r is None:
        r = frozenset(factorint(x).keys())
        cache[x] = r
    return r

def generate(a1, N, verbose=True, report_every=2000):
    t0 = time.time()
    a = [None, a1]
    r1 = rad(a1)
    antichain = [r1]  # list of frozensets, kept minimal under inclusion
    n = 1
    x = a1
    while n < N:
        x += 1
        while True:
            ok = True
            for T in antichain:
                hit = False
                for p in T:
                    if x % p == 0:
                        hit = True
                        break
                if not hit:
                    ok = False
                    break
            if ok:
                break
            x += 1
        rx = rad(x)
        a.append(x)
        n += 1
        # update antichain: drop members that are proper supersets of rx, add rx if not superset of/equal existing member
        new_antichain = [T for T in antichain if not (rx < T)]
        if not any(T <= rx for T in new_antichain):
            new_antichain.append(rx)
        antichain = new_antichain
        if verbose and n % report_every == 0:
            print(f"  n={n} a_n={x} antichain_size={len(antichain)} elapsed={time.time()-t0:.1f}s", file=sys.stderr)
    return a[1:]

if __name__ == "__main__":
    a1 = int(sys.argv[1])
    N = int(sys.argv[2])
    out = sys.argv[3]
    seq = generate(a1, N)
    with open(out, "w") as f:
        json.dump(seq, f)
    print("done", a1, N, "last", seq[-1])
