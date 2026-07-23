import sys
from math import gcd

def generate(a1, N):
    """Generate first N terms of the sequence for given a_1, using the literal
    problem definition: a_{n+1} = smallest integer > a_n with gcd(a_{n+1}, a_i) > 1
    for all i <= n."""
    seq = [a1]
    while len(seq) < N:
        cand = seq[-1] + 1
        while True:
            if all(gcd(cand, x) > 1 for x in seq):
                seq.append(cand)
                break
            cand += 1
    return seq

def primes_upto(n):
    sieve = [True]*(n+1)
    sieve[0]=sieve[1]=False if n>=1 else None
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i,n+1,i):
                sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]]

def small_prime_set(n, small_primes):
    return frozenset(p for p in small_primes if n % p == 0)

# Test small values where full period P is tractable
for a1 in [6,10,12,15]:
    small_primes = primes_upto(a1)
    P = 1
    for p in small_primes:
        P *= p
    # generate enough terms so that max term > a1 + a few periods P (need many terms)
    # instead, generate up to some N steps and check
    N = 4000 if a1<=12 else 20000
    seq = generate(a1, N)
    maxterm = seq[-1]
    print(f"a1={a1} P={P} small_primes={small_primes} N={N} maxterm={maxterm}")
