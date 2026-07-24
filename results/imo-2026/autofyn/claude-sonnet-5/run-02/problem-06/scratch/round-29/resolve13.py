import sympy
from sympy import mod_inverse
from math import gcd

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

def a_i(q,i):
    return p*(q+i-1)

exceptions = []
resolved = []
for (j,r,q) in below:
    s0,K0 = table[(j,r)]
    n0 = 1 + (s0*q - j)//p
    N = a_i(q, n0) + j
    assert N == q*K0, (j,r,q,N,q*K0)
    witness = None
    for i in range(1, n0+1):
        if gcd(N, a_i(q,i)) == 1:
            witness = i
            break
    if witness is None:
        exceptions.append((j,r,q,n0,N))
    else:
        resolved.append((j,r,q,n0,N,witness))

print("Total below-threshold candidates:", len(below))
print("Resolved (witness found):", len(resolved))
print("EXCEPTIONS (no witness):", len(exceptions))
for e in exceptions:
    print(" ", e)
