from math import gcd
import sympy

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
Bad13 = {17,19,23,47}
sample_primes = [q for q in sympy.primerange(14, 400) if q != p and q not in Bad13][:15]
for q in sample_primes:
    a1 = p*q
    seq = greedy_seq(a1, 200)
    closed = [p*(q+n) for n in range(200)]
    ok = all(seq[n]==closed[n] for n in range(200))
    print(q, "OK" if ok else "MISMATCH")
