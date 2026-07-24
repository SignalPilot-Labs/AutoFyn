import sympy
from sympy import primefactors, gcd

def gen_sequence(a1, N):
    a = [None, a1]
    while len(a) <= N:
        n = len(a)-1  # current last index
        prev = a[-1]
        c = prev+1
        while True:
            ok = True
            for i in range(1, n+1):
                if gcd(c, a[i]) == 1:
                    ok = False
                    break
            if ok:
                a.append(c)
                break
            c += 1
    return a  # 1-indexed, a[1..N]

a1 = 4807
N = 2500
a = gen_sequence(a1, N)
print("generated", len(a)-1, "terms")

S0 = {2,3,5,7,11,19,23,73,127}

def rho(n):
    return frozenset(primefactors(a[n])) & S0

types = {}
for n in range(1, N+1):
    t = rho(n)
    types.setdefault(t, []).append(n)

# print types with count>=3 and nonempty
for t, occ in sorted(types.items(), key=lambda kv: -len(kv[1])):
    if len(occ) >= 3 and len(t)>0:
        print(t, len(occ), occ[:6])

print("\n--- Rogue pair experiment ---")
Aprime = frozenset({3,19,5})
Bprime = frozenset({2,11,7})
assert Aprime & Bprime == frozenset()
nA = types[Aprime][0]
nB = types[Bprime][0]
print("nA", nA, "a_nA", a[nA], "factors", primefactors(a[nA]))
print("nB", nB, "a_nB", a[nB], "factors", primefactors(a[nB]))

Fp = set(primefactors(a[nA])) - S0
Fpp = set(primefactors(a[nB])) - S0
print("F'", Fp, "F''", Fpp, "intersection", Fp & Fpp)
