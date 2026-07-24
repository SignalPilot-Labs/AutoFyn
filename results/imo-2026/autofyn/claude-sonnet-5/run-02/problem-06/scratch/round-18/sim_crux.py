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
N = 3000
seq = gen_sequence(a1, N)
Q = primes_of(a1)
print("Q =", Q)
S0 = {2,3,5,11,19,23}
Aprime = frozenset({3,5,19})
Bprime = frozenset({2,11})

occA = []
occB = []
for idx in range(1, N+1):
    a = seq[idx-1]
    rho = primes_of(a) & S0
    if frozenset(rho) == Aprime:
        occA.append(idx)
    if frozenset(rho) == Bprime:
        occB.append(idx)

print("num occ A':", len(occA), occA[:20])
print("num occ B':", len(occB), occB[:20])

# for each occurrence of A', compute F'_m = P(a_m)\S0
for m in occA[:15]:
    a = seq[m-1]
    Fp = primes_of(a) - S0
    print("m=",m,"a_m=",a,"F'_m=",Fp)

count17 = sum(1 for a in seq if a % 17 == 0)
print("fraction divisible by 17:", count17, "/", N)
notdiv = [i+1 for i,a in enumerate(seq) if a%17!=0]
print("num not divisible by 17:", len(notdiv))
print("last few not divisible:", notdiv[-20:])

# check B' occurrences all divisible by 17 (Singleton-Side FAH direction)
badB = [n for n in occB if seq[n-1] % 17 != 0]
print("B' occurrences NOT divisible by 17:", badB)

# now the real crux question: extend simulation, find more A' occurrences, check F'_m
