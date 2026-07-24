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

seq = gen(15, 24)
print(seq)
Q = {3,5}
types = [frozenset(p for p in Q if x % p == 0) for x in seq]
print([sorted(t) for t in types])

seq3000 = gen(15, 3000)
c3 = sum(1 for x in seq3000 if x%3==0)
c5 = sum(1 for x in seq3000 if x%5==0)
print("3000 terms: 3| count", c3, c3/3000, "5| count", c5, c5/3000)

fail_idx = [i+1 for i,x in enumerate(seq3000) if x%3!=0]
print("first 10 fail-3 indices:", fail_idx[:10])
diffs = set(fail_idx[i+1]-fail_idx[i] for i in range(len(fail_idx)-1))
print("diffs set (should be {4}):", diffs)
