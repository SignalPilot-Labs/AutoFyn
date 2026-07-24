import math

def gen(a1, N):
    a = [a1]
    while len(a) < N:
        c = a[-1] + 1
        while True:
            if all(math.gcd(c, x) > 1 for x in a):
                a.append(c)
                break
            c += 1
    return a

tests = []
for p in [2,3,5,7,11,13,17,19,23,29,31,37,41]:
    for k in [1,2,3,4,5]:
        a1 = p**k
        if a1 > 2000:  # keep runtime reasonable but still test
            continue
        tests.append((p,k,a1))

# also test some larger a1 with bigger k for a few select primes
tests += [(29,2,841), (31,2,961), (2,10,1024), (3,7,2187), (5,5,3125), (7,4,2401), (13,3,2197)]

fail=0
for p,k,a1 in tests:
    N = 15
    seq = gen(a1, N)
    ok = all(seq[i] == a1 + p*i for i in range(N))
    if not ok:
        print("FAIL", p, k, a1, seq[:10])
        fail+=1
print("total tests", len(tests), "failures", fail)
