import sympy
from sympy import mod_inverse
from math import gcd
from collections import defaultdict

p = 13
table = {}
for j in range(2, p):
    for r in range(1, p):
        s0 = (j * mod_inverse(r, p)) % p
        K0 = p + s0
        table[(j,r)] = (s0, K0)

def Q1(j,r):
    s0,K0 = table[(j,r)]
    return (p*(K0+1)+j)/s0

below = []
for (j,r) in table:
    thresh = Q1(j,r)
    qs = [q for q in sympy.primerange(p+1, 6000) if q % p == r and q < thresh]
    for q in qs:
        below.append((j,r,q))

byq = defaultdict(list)
for (j,r,q) in below:
    byq[q].append((j,r))

dupq = {q:v for q,v in byq.items() if len(v)>1}
print("Number of q's with multiple below-threshold bands:", len(dupq))
for q,v in sorted(dupq.items()):
    print(q, v)
