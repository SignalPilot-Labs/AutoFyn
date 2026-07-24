import sympy, time

def gen_sequence(a1, N):
    seq = [a1]
    full_mask = 1  # mask of indices covered so far (bit i-1 for term i), grows
    prime_mask = {}  # prime -> bitmask of indices (1-based, bit i-1) divisible by prime
    def add_term(idx, a):
        for p in sympy.factorint(a):
            prime_mask[p] = prime_mask.get(p, 0) | (1 << (idx-1))
    add_term(1, a1)
    target_full = 1  # bits 0..n-1 all set = (1<<n)-1
    n = 1
    while len(seq) < N:
        prev = seq[-1]
        need_mask = (1 << n) - 1  # bits for indices 1..n
        c = prev + 1
        while True:
            f = sympy.factorint(c)
            cov = 0
            for p in f:
                cov |= prime_mask.get(p, 0)
                if cov == need_mask:
                    break
            if cov == need_mask:
                seq.append(c)
                add_term(n+1, c)
                n += 1
                break
            c += 1
    return seq

def primes_of(n):
    return set(sympy.factorint(n).keys())

a1 = 4807
N = 8000
t0=time.time()
seq = gen_sequence(a1, N)
print("time", time.time()-t0)
S0 = {2,3,5,11,19,23}
Aprime = frozenset({3,5,19})

occA = []
for idx in range(1, N+1):
    a = seq[idx-1]
    rho = primes_of(a) & S0
    if frozenset(rho) == Aprime:
        occA.append(idx)

print("num occ A':", len(occA))
for m in occA:
    a = seq[m-1]
    Fp = primes_of(a) - S0
    print("m=",m,"F'_m=",Fp, "17 in?", 17 in Fp)

occB = []
for idx in range(1, N+1):
    a = seq[idx-1]
    rho = primes_of(a) & S0
    if frozenset(rho) == frozenset({2,11}):
        occB.append(idx)
print("num occ B':", len(occB))
singleton_witnesses = []
for x in occB:
    a = seq[x-1]
    Fpp = primes_of(a) - S0
    if Fpp == {17}:
        singleton_witnesses.append(x)
print("B' occurrences with F''={17} exactly:", singleton_witnesses[:30], "count", len(singleton_witnesses))

# Test the triangle mechanism directly: e = gcd(a_{m_A}, a_{m_A'}) for two A' witnesses
import math
for i in range(len(occA)-1):
    for j in range(i+1, min(i+3,len(occA))):
        mA, mAp = occA[i], occA[j]
        e = math.gcd(seq[mA-1], seq[mAp-1])
        Fp_mA = primes_of(seq[mA-1]) - S0
        Fp_mAp = primes_of(seq[mAp-1]) - S0
        print(f"m_A={mA} m_A'={mAp} e={e} primes(e)={sorted(primes_of(e))} F'_mA={Fp_mA} F'_mA'={Fp_mAp} outsideCore(e)={sorted(primes_of(e)-S0)}")
