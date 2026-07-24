import sympy
from math import gcd

def greedy_seq(a1, nterms):
    a = [a1]
    while len(a) < nterms:
        an = a[-1]
        j = 1
        while True:
            cand = an + j
            legal = all(gcd(cand, ai) > 1 for ai in a)
            if legal:
                a.append(cand)
                break
            j += 1
    return a

p = 13
primes = list(sympy.primerange(p+1, 6000))
primes = [q for q in primes if q != p]

nterms = 10
deviations = {}
for q in primes:
    a1 = p*q
    seq = greedy_seq(a1, nterms)
    closed = [p*(q+n) for n in range(nterms)]  # a_{n+1}=p(q+n), i.e. a[n] index n (0-based) = p(q+n)
    dev_idx = None
    for n in range(nterms):
        if seq[n] != closed[n]:
            dev_idx = n+1  # 1-based
            dev_val = seq[n]
            break
    if dev_idx is not None:
        deviations[q] = (dev_idx, dev_val)

print("Number of primes tested:", len(primes))
print("Deviations found:", deviations)

print()
for q in [17,19,23,47]:
    a1 = p*q
    seq = greedy_seq(a1, 10)
    print(q, seq)
