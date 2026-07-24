import sympy
from sympy import mod_inverse
from math import gcd

p = 13

# Build (j,r) table: s0 solves s0*r = j mod p, K0 = p+s0
table = {}
for j in range(2, p):
    for r in range(1, p):
        s0 = (j * mod_inverse(r, p)) % p
        if s0 == 0:
            s0 = p  # shouldn't happen since j in 1..p-1, r invertible
        K0 = p + s0
        table[(j,r)] = (s0, K0)

print("Table size:", len(table))
print("Max K0:", max(v[1] for v in table.values()))
print("Min K0:", min(v[1] for v in table.values()))

# diagonal check
diag_ok = all(table[(j,j)][0]==1 for j in range(2,p))
print("Diagonal s0=1 for all j=r:", diag_ok)

# n0(j,r;q) = 1 + (s0*q - j)/p
def n0_val(j,r,q):
    s0,K0 = table[(j,r)]
    val = s0*q - j
    assert val % p == 0, (j,r,q,val)
    return 1 + val//p, K0

# Q1(j,r) sufficient-window threshold: q >= (p*(K0+1)+j)/s0
def Q1(j,r):
    s0,K0 = table[(j,r)]
    return (p*(K0+1)+j)/s0

import json
Q1table = {(j,r): Q1(j,r) for j in range(2,p) for r in range(1,p)}
# below threshold candidates
below = []
for (j,r),thresh in Q1table.items():
    qs = [q for q in sympy.primerange(p+1, 6000) if q % p == r and q < thresh]
    for q in qs:
        below.append((j,r,q))
print("Number of below-threshold (j,r,q) k=0 candidates:", len(below))
