import sys, time
from sympy import factorint

factor_cache = {}
def factors(x):
    f = factor_cache.get(x)
    if f is None:
        f = set(factorint(x).keys())
        factor_cache[x] = f
    return f

def gen(a1, N, verbose=False):
    terms = [a1]
    rads = [factors(a1)]
    prime_to_indices = {}
    for p in rads[0]:
        prime_to_indices.setdefault(p, set()).add(0)
    n = 1
    cur = a1
    t0 = time.time()
    while n < N:
        x = cur + 1
        while True:
            fx = factors(x)
            covered = set()
            for p in fx:
                s = prime_to_indices.get(p)
                if s:
                    covered |= s
                    if len(covered) == n:
                        break
            if len(covered) == n:
                break
            x += 1
        terms.append(x)
        rads.append(fx)
        idx = n
        for p in fx:
            prime_to_indices.setdefault(p, set()).add(idx)
        cur = x
        n += 1
        if verbose and n % 1000 == 0:
            print(f"  a1={a1}: n={n}, a_n={cur}, elapsed={time.time()-t0:.1f}s", file=sys.stderr)
    return terms, rads

if __name__ == "__main__":
    a1 = int(sys.argv[1])
    N = int(sys.argv[2])
    t0 = time.time()
    terms, rads = gen(a1, N, verbose=True)
    print(f"a1={a1}: generated {N} terms in {time.time()-t0:.2f}s, a_N={terms[-1]}")
