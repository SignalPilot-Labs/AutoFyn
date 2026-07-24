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

def n_val(j,r,q,k):
    s0,K0 = table[(j,r)]
    val = s0*q - j
    assert val % p == 0
    n0 = 1 + val//p
    return n0 + k*q, K0

def a_i(q,i):
    return p*(q+i-1)

nonmoot = [(2, 5, 2, 31), (2, 7, 1, 59), (3, 4, 1, 43), (4, 1, 1, 53), (5, 11, 1, 37),
           (7, 5, 1, 31), (8, 2, 1, 41), (9, 3, 2, 29), (10, 9, 1, 61), (12, 3, 1, 29)]

for (j,r,k,q) in nonmoot:
    n, K0 = n_val(j,r,q,k)
    K = K0 + p*k
    N = q*K
    # verify N = a_n + j using formula, but a_n only valid under H(n) closed form (may not hold if earlier deviation happened for this q -- but q not in Bad13 so should hold)
    Nexp = a_i(q, n-1+1) if False else None
    # a_n formula for closed form: a_n = p*(q+n-1)
    Nclosed = p*(q+n-1) + j
    assert N == Nclosed, (j,r,k,q,N,Nclosed)
    witness = None
    for i in range(1, n+1):
        if gcd(N, a_i(q,i)) == 1:
            witness = i
            break
    print((j,r,k,q), "n=",n,"K=",K,"N=",N,"witness=",witness)
