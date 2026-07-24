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

def n0_val(j,r,q):
    s0,K0 = table[(j,r)]
    val = s0*q - j
    assert val % p == 0
    return 1 + val//p

def omega(n):
    return len(sympy.factorint(n))

def bound_for_omega(w):
    # rho* <= w+1
    rho = w+1
    return 2**rho*(rho+1)

# residual band k=1..11
Bad13 = {17,19,23,47}
below_quads = []
for (j,r),(s0,K0) in table.items():
    for k in range(1,12):
        Kk = K0 + p*k
        w = omega(Kk)
        bound = bound_for_omega(w)
        # threshold on q: L(q) = n0(j,r;q)-1 + k*q >= bound
        # n0 = 1+(s0*q-j)/p, so n0-1 = (s0*q-j)/p
        # L(q) = (s0*q-j)/p + k*q
        # solve for q: L(q) >= bound  => q*(s0/p + k) >= bound + j/p
        # q >= (bound*p + j) / (s0 + k*p)
        qthresh = (bound*p + j) / (s0 + k*p)
        qs = [q for q in sympy.primerange(p+1, 6000) if q % p == r and q < qthresh]
        # skip r=1 with gcd(k+1,j)==1 (free by lemma5 analog)
        if r == 1 and gcd(k+1, j) == 1:
            continue
        for q in qs:
            below_quads.append((j,r,k,q))

print("Total below-threshold (j,r,k,q) quadruples (k=1..11):", len(below_quads))
moot = [t for t in below_quads if t[3] in Bad13]
nonmoot = [t for t in below_quads if t[3] not in Bad13]
print("moot (q in Bad13):", len(moot))
print("non-moot:", len(nonmoot))
print(nonmoot)
