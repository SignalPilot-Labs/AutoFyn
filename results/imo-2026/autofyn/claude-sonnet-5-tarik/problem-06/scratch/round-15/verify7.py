import time, random, math
from math import gcd
from sympy import primerange

def generate(a1, N):
    seq = [a1]
    while len(seq) < N:
        cand = seq[-1] + 1
        while True:
            if all(gcd(cand, x) > 1 for x in seq):
                seq.append(cand)
                break
            cand += 1
    return seq

def check_claim3(a1, N, seed=2):
    random.seed(seed)
    seq = generate(a1, N)
    maxterm = seq[-1]
    termset = set(seq)
    k = a1
    small_primes_over_k = list(primerange(k+1, k+500))
    checked = 0
    violations = 0
    # iterate over ALL non-terms n in [k, maxterm//smallest_p] and a handful of small p>k
    p0 = small_primes_over_k[0]
    limit_n = maxterm // p0
    non_terms = [n for n in range(k, limit_n+1) if n not in termset]
    print(f"a1={a1}: candidates n count = {len(non_terms)}, testing against {len(small_primes_over_k[:5])} primes")
    for n in non_terms:
        for p in small_primes_over_k[:5]:
            np = n*p
            if np > maxterm: continue
            checked += 1
            if np in termset:
                violations += 1
                print("C3 VIOLATION", n, p, np)
    print(f"a1={a1}: Claim3 checked {checked} pairs, violations {violations}")

check_claim3(247, 6000)
check_claim3(2747, 4000)
check_claim3(21528751, 1200)
