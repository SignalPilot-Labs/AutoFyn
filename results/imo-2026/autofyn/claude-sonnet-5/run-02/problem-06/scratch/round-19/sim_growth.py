import sympy

def gen_sequence(a1, N):
    seq = [a1]
    while len(seq) < N:
        cand = seq[-1] + 1
        while True:
            ok = True
            for prev in seq:
                if sympy.gcd(cand, prev) == 1:
                    ok = False
                    break
            if ok:
                seq.append(cand)
                break
            cand += 1
    return seq

def factor_set(n):
    return set(sympy.factorint(n).keys())

def analyze(a1, S0, N):
    seq = gen_sequence(a1, N)
    types = {}
    for i, v in enumerate(seq):
        n = i+1
        rho = frozenset(factor_set(v) & S0)
        types.setdefault(rho, []).append(n)
    return seq, types

# a1 = 4807, S0 = {2,3,5,11,19,23}
S0_4807 = {2,3,5,11,19,23}
N = 16000
seq, types = analyze(4807, S0_4807, N)
A = frozenset({3,5,19})
B = frozenset({2,11})
for windowfrac in [0.5,1.0]:
    Nw = int(N*windowfrac)
    for name, T in [("A'",A), ("B'",B)]:
        occ = [n for n in types.get(T,[]) if n<=Nw]
        singles = []
        for n in occ:
            v = seq[n-1]
            outside = factor_set(v) - S0_4807
            if len(outside)==1:
                singles.append((n, next(iter(outside))))
        print(f"4807 window {Nw} type {name}: occ={len(occ)} singles={len(singles)} sample={singles[:5]}")
