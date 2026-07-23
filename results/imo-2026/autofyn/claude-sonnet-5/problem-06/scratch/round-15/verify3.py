import time
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

def dichotomy_check(a1, N):
    t0=time.time()
    small_primes = primes_upto(a1)
    seq = generate(a1, N)
    maxterm = seq[-1]
    termset = set(seq)
    print(f"a1={a1}: small_primes(count={len(small_primes)})={small_primes if len(small_primes)<20 else small_primes[:20]}..., N={N}, maxterm={maxterm}, gen_time={time.time()-t0:.1f}s")
    # build signature -> list of (n, status) for n in [a1, maxterm]
    from collections import defaultdict
    sig_to_status = {}
    violations = []
    checked = 0
    for n in range(a1, maxterm+1):
        sig = 0
        for i,p in enumerate(small_primes):
            if n % p == 0:
                sig |= (1<<i)
        status = (n in termset)
        checked += 1
        if sig in sig_to_status:
            if sig_to_status[sig][1] != status:
                violations.append((sig_to_status[sig][0], sig_to_status[sig][1], n, status))
        else:
            sig_to_status[sig] = (n, status)
    print(f"  checked {checked} integers in [{a1},{maxterm}], distinct signatures found: {len(sig_to_status)}, violations: {len(violations)}")
    if violations:
        print("  SAMPLE VIOLATIONS:", violations[:5])
    return violations

for a1, N in [(247, 6000), (2747, 4000), (4087, 4000), (4199, 4000)]:
    dichotomy_check(a1, N)
