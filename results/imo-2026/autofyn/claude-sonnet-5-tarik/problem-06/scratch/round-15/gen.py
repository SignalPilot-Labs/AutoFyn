import sys, math, time
from sympy import factorint

def factor(x, cache={}):
    if x in cache: return cache[x]
    f = factorint(x)
    s = frozenset(f.keys())
    cache[x] = s
    return s

def prod(s):
    v=1
    for p in s: v*=p
    return v

def antichain_update(M, newset):
    # M: list of (frozenset, product) pairs
    dominated = any(m <= newset for m,_ in M)
    if dominated:
        return M
    M2 = [(m,v) for m,v in M if not (newset < m)]
    M2.append((newset, prod(newset)))
    return M2

def gen_sequence(a1, N, verbose=False):
    terms = [a1]
    rad1 = factor(a1)
    M = [(rad1, prod(rad1))]
    radicals = [rad1]
    x = a1
    t0=time.time()
    for n in range(1, N):
        cand = x+1
        while True:
            ok = True
            for m,mv in M:
                if math.gcd(cand, mv) == 1:
                    ok = False
                    break
            if ok:
                break
            cand += 1
        x = cand
        terms.append(x)
        rs = factor(x)
        radicals.append(rs)
        M = antichain_update(M, rs)
        if verbose and n % 5000==0:
            print(n, x, time.time()-t0, len(M))
    return terms, radicals

if __name__=="__main__":
    a1=int(sys.argv[1]); N=int(sys.argv[2])
    terms,radicals = gen_sequence(a1,N,verbose=True)
    print("done", terms[-1])
