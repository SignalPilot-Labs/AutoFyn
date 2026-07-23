from math import gcd

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

def primes_upto(n):
    if n<2: return []
    sieve = [True]*(n+1)
    sieve[0]=sieve[1]=False
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i,n+1,i):
                sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]]

for a1, N in [(2,2000),(3,2000),(4,3000),(5,3000)]:
    small_primes = primes_upto(a1)
    P = 1
    for p in small_primes: P*=p
    seq = generate(a1, N)
    term_res = set(x % P for x in seq)
    T = len(term_res)
    maxn_check = N - T
    ok=True
    for n in range(1, maxn_check+1):
        if seq[n-1+T] != seq[n-1]+P:
            ok=False
            print("fail at", n)
            break
    print(f"a1={a1}, small_primes={small_primes}, P={P}, T={T}, first10={seq[:10]}, periodicity ok (n=1..{maxn_check}): {ok}")
