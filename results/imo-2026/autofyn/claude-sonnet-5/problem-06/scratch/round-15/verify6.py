import time, random
from math import gcd
from sympy import factorint, primerange, isprime

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

def check_claims(a1, N, ntrials_c2=20000, ntrials_c3=20000, seed=1):
    random.seed(seed)
    seq = generate(a1, N)
    maxterm = seq[-1]
    termset = set(seq)
    def is_term(n):
        return n in termset
    k = a1
    # Claim 2: rs>=k non-term => r^2 s non-term.  scan r,s pairs such that rs, r^2 s <= maxterm
    c2_checked = 0
    c2_violations = 0
    # brute force over r in [1, some bound], s to make rs in [k,maxterm], r^2 s <= maxterm
    import math
    maxr = int(math.isqrt(maxterm // 1)) + 2
    for _ in range(ntrials_c2):
        r = random.randint(1, min(200, maxr))
        # need r^2 * s <= maxterm and rs>=k
        max_s = maxterm // (r*r) if r*r>0 else 0
        if max_s < 1: 
            continue
        min_s = (k + r - 1)//r if r>0 else 1
        if min_s > max_s:
            continue
        s = random.randint(min_s, max_s)
        rs = r*s
        r2s = r*r*s
        if rs < k or r2s > maxterm:
            continue
        c2_checked += 1
        if not is_term(rs):  # rs is non-term
            if is_term(r2s):  # claim says r^2s should be non-term too
                c2_violations += 1
                print("C2 VIOLATION", r, s, rs, r2s)
    # Claim 3: p>k prime, n>=k non-term => np non-term
    c3_checked = 0
    c3_violations = 0
    small_primes_over_k = [p for p in primerange(k+1, k+2000)]
    for _ in range(ntrials_c3):
        n = random.randint(k, maxterm)
        if is_term(n):
            continue
        p = random.choice(small_primes_over_k)
        np = n*p
        if np > maxterm:
            continue
        c3_checked += 1
        if is_term(np):
            c3_violations += 1
            print("C3 VIOLATION", n, p, np)
    print(f"a1={a1}: C2 checked {c2_checked} violations {c2_violations}; C3 checked {c3_checked} violations {c3_violations}")

check_claims(247, 6000)
check_claims(21528751, 1200, ntrials_c2=20000, ntrials_c3=20000)
