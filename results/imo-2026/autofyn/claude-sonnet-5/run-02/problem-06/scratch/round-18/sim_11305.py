import sympy, time

def gen_sequence(a1, N):
    seq = [a1]
    prime_mask = {}
    def add_term(idx, a):
        for p in sympy.factorint(a):
            prime_mask[p] = prime_mask.get(p, 0) | (1 << (idx-1))
    add_term(1, a1)
    n = 1
    while len(seq) < N:
        prev = seq[-1]
        need_mask = (1 << n) - 1
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

a1 = 11305
N = 8000
t0=time.time()
seq = gen_sequence(a1, N)
print("time", time.time()-t0)
print("Q=", primes_of(a1))
S0 = {2,3,5,7,11,103}  # guess: recruited core per prior report A'={3,7}, B'={2,5}, F''={11,103}
# verify n_A=4, n_B=7
for idx in [4,7]:
    print(idx, seq[idx-1], primes_of(seq[idx-1]))

S0 = {2,3,5,7,13,17,19,23,29,37,43,101}
Aprime = frozenset({2,5})
Bprime = frozenset({3,7})
occA=[]; occB=[]
for idx in range(1,N+1):
    a=seq[idx-1]
    rho = primes_of(a)&S0
    if frozenset(rho)==Aprime: occA.append(idx)
    if frozenset(rho)==Bprime: occB.append(idx)
print("occA (n>4):", [x for x in occA if x>4][:40], "count", len([x for x in occA if x>4]))
print("occB (n>7):", [x for x in occB if x>7][:40], "count", len([x for x in occB if x>7]))

# check occA all divisible by 11 (already known)
badA = [n for n in occA if n>4 and seq[n-1]%11!=0]
print("A' occ (n>4) NOT div by 11:", badA)

# check occB divisible by 11
badB = [n for n in occB if n>7 and seq[n-1]%11!=0]
print("B' occ (n>7) NOT div by 11:", badB, "of", len([x for x in occB if x>7]))

# find A' occurrences with F'_n singleton = {11}
singletons = []
for n in occA:
    if n<=4: continue
    Fp = primes_of(seq[n-1]) - S0
    if Fp == {11}:
        singletons.append(n)
print("A' occurrences (n>4) with F'_n={11} exactly:", singletons[:20], "count", len(singletons))
