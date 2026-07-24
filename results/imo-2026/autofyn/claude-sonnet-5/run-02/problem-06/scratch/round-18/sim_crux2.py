import sympy

def gen_sequence(a1, N):
    seq = [a1]
    while len(seq) < N:
        prev = seq[-1]
        c = prev + 1
        while True:
            ok = True
            for a in seq:
                if sympy.gcd(c, a) == 1:
                    ok = False
                    break
            if ok:
                seq.append(c)
                break
            c += 1
    return seq

def primes_of(n):
    return set(sympy.factorint(n).keys())

a1 = 4807
N = 20000
seq = gen_sequence(a1, N)
S0 = {2,3,5,11,19,23}
Aprime = frozenset({3,5,19})

occA = []
for idx in range(1, N+1):
    a = seq[idx-1]
    rho = primes_of(a) & S0
    if frozenset(rho) == Aprime:
        occA.append(idx)

print("num occ A':", len(occA))
for m in occA:
    a = seq[m-1]
    Fp = primes_of(a) - S0
    print("m=",m,"F'_m=",Fp, "17 in?", 17 in Fp)
