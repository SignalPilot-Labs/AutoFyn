import sympy
from math import gcd
from functools import reduce

def build_sequence(a1, N):
    a = [a1]
    while len(a) < N:
        an = a[-1]
        cand = an + 1
        while True:
            if all(gcd(cand, x) > 1 for x in a):
                a.append(cand)
                break
            cand += 1
    return a

def primes_of(x):
    return set(sympy.factorint(x).keys())

def build_state(a1, N=4000):
    a = build_sequence(a1, N)
    Q = primes_of(a1)
    types = [primes_of(x) & Q for x in a]
    # persistent base types: occur infinitely often -> approximate by occurring in last third of range
    from collections import Counter
    cnt = Counter(frozenset(t) for t in types)
    n = len(a)
    tail_cnt = Counter(frozenset(t) for t in types[2*n//3:])
    persistent = set(t for t in cnt if t in tail_cnt)  # crude persistence test
    return a, Q, types, persistent

if __name__ == "__main__":
    for a1 in [4807, 11305, 209, 247, 175]:
        a, Q, types, persistent = build_state(a1, N=3000)
        print(a1, "Q=", sorted(Q), "num persistent types=", len(persistent))
