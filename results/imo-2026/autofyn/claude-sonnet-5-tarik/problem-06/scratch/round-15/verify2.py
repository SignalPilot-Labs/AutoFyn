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
    sieve = [True]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i,n+1,i):
                sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]]

def good_residues(a1, P, small_primes, seq):
    # determine status of each residue r in [0,P) using the generated seq:
    # a residue is 'good' iff a1's terms include an element == r mod P.
    # We just check which residues among generated seq terms occur.
    term_residues = set(x % P for x in seq)
    return term_residues

for a1, N in [(6,6000),(10,8000),(12,9000),(15,22000)]:
    small_primes = primes_upto(a1)
    P = 1
    for p in small_primes:
        P *= p
    seq = generate(a1, N)
    term_res = good_residues(a1, P, small_primes, seq)
    T = len(term_res)
    # verify periodicity a_{n+T} = a_n + P for as many n as available
    maxn_check = N - T
    ok = True
    bad_at = None
    for n in range(1, maxn_check+1):  # 1-indexed
        if seq[n-1+T] != seq[n-1] + P:
            ok = False
            bad_at = n
            break
    print(f"a1={a1}, P={P}, T={T}, checked n=1..{maxn_check}, periodicity holds: {ok}", "bad at" if not ok else "", bad_at if not ok else "")

print()
print("NEW a1 values not tested by builder:")
for a1, N in [(7,8000),(9,8000),(11,9000),(14,22000)]:
    small_primes = primes_upto(a1)
    P = 1
    for p in small_primes:
        P *= p
    seq = generate(a1, N)
    term_res = good_residues(a1, P, small_primes, seq)
    T = len(term_res)
    maxn_check = N - T
    ok = True
    bad_at = None
    for n in range(1, maxn_check+1):
        if seq[n-1+T] != seq[n-1] + P:
            ok = False
            bad_at = n
            break
    print(f"a1={a1}, P={P}, T={T}, checked n=1..{maxn_check}, periodicity holds: {ok}")
