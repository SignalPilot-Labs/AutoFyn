import math, sys
from sympy import factorint

def gen_sequence(a1, N):
    a = [a1]
    while len(a) < N:
        an = a[-1]
        cand = an + 1
        while True:
            ok = True
            for x in a:
                if math.gcd(cand, x) == 1:
                    ok = False
                    break
            if ok:
                a.append(cand)
                break
            cand += 1
    return a

def analyze(a1, S0, N, label):
    a = gen_sequence(a1, N)
    # a[0] is a_1 (index1)
    types = {}
    outside = {}
    for i, val in enumerate(a):
        n = i+1
        f = factorint(val)
        primes = set(f.keys())
        rho = primes & S0
        out = primes - S0
        types[n] = frozenset(rho)
        outside[n] = out
    return a, types, outside

if __name__ == "__main__":
    seeds = [
        (4807, {2,3,5,11,19,23}, frozenset({3,5,19}), frozenset({2,11}), 8000, "4807"),
        (11305, {2,3,5,7,13,17,19,23,29,37,43,101}, frozenset({2,5}), frozenset({3,7}), 8000, "11305"),
    ]
    for a1, S0, A, B, N, label in seeds:
        print("=== seed", label, "N=",N, "===")
        a, types, outside = analyze(a1, S0, N, label)
        XA = [n for n in range(1,N+1) if types[n]==A]
        XB = [n for n in range(1,N+1) if types[n]==B]
        print("len XA", len(XA), "len XB", len(XB))
        import pickle
        with open(f"/tmp/round-20/data_{label}.pkl","wb") as f:
            pickle.dump({"a":a,"types":types,"outside":outside,"XA":XA,"XB":XB,"A":A,"B":B,"S0":S0}, f)
