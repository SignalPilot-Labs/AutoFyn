import math
from sympy import factorint

def gen_seq(a1, N):
    a = [None, a1]
    for _ in range(N-1):
        an = a[-1]
        c = an + 1
        while True:
            ok = True
            for prev in a[1:]:
                if math.gcd(c, prev) == 1:
                    ok = False
                    break
            if ok:
                a.append(c)
                break
            c += 1
    return a

def primeset(x, cache={}):
    if x in cache: return cache[x]
    s = set(factorint(x).keys())
    cache[x] = s
    return s
