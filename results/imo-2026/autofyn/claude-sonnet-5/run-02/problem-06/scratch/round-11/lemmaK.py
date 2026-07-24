import sympy
from sympy import primefactors, gcd, factorint, divisors

def gen_sequence(a1, N):
    a = [None, a1]
    while len(a) <= N:
        n = len(a)-1
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
    return a

a1 = 4807
N = 2500
a = gen_sequence(a1, N)
S0 = {2,3,5,7,11,19,23,73,127}

def rho(n):
    return frozenset(primefactors(a[n])) & S0

types = {}
for n in range(1, N+1):
    t = rho(n)
    types.setdefault(t, []).append(n)

Aprime = frozenset({3,19,5})
Bprime = frozenset({2,11})
nA = types[Aprime][0]
nB = types[Bprime][0]
print("nA",nA,"a_nA",a[nA])
print("nB",nB,"a_nB",a[nB],"=",factorint(a[nB]))

Fpp = set(primefactors(a[nB])) - S0
fac_nB = factorint(a[nB])
b = 1
for p,e in fac_nB.items():
    if p in Fpp: b*=p**e
qstar = 17
print("b",b,"Div(b)",divisors(b))

Aoccs = [n for n in types[Aprime] if n > nB]
print("A' occurrences > nB:", Aoccs)

for n in Aoccs:
    an = a[n]
    g = gcd(an, a[nB])
    q_divides = (an % qstar == 0)
    print(f"\nn={n} a_n={an} factors={factorint(an)} gcd(a_n,a_nB)={g} q*|a_n: {q_divides}")
    if not q_divides:
        # Apply Lemma K with q=qstar
        c = qstar * (an // qstar)
        print(f"  Lemma K: c = {c} (a_n - c = {an-c})")
        if c <= a[n-1]:
            print(f"  branch (a): c={c} <= a_{{n-1}}={a[n-1]}")
        else:
            # find blocking index j
            j = None
            for i in range(1, n):
                if gcd(c, a[i]) == 1:
                    j = i
                    break
            print(f"  branch (b): blocking index j={j}, a_j={a[j] if j else None}")
            if j:
                shared = set(primefactors(an)) & set(primefactors(a[j]))
                print(f"  shared primes P(a_n) ∩ P(a_j) = {shared}")
                print(f"  P(c) = {primefactors(c)}, P(c)∩P(a_j) = {set(primefactors(c))&set(primefactors(a[j]))}")
                print(f"  is j == nB? {j==nB}")
