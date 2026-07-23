import sympy
from sympy import factorint, gcd

def brute_gen(a1, N):
    terms = [a1]
    while len(terms) < N:
        c = terms[-1] + 1
        while not all(gcd(c, t) > 1 for t in terms):
            c += 1
        terms.append(c)
    return terms

for a1, idxs in [(2747, [3,13,14,163]), (4087, [5,54])]:
    print(f"=== a1={a1} ===")
    P1 = set(factorint(a1).keys())
    print("P1 =", P1)
    N = max(idxs)+5
    terms = brute_gen(a1, N)
    for i in idxs:
        v = terms[i-1]
        f = factorint(v)
        core = set(f.keys()) & P1
        comp = set(f.keys()) - P1
        print(f"a_{i} = {v} = {f}, core={core}, comp={comp}")
