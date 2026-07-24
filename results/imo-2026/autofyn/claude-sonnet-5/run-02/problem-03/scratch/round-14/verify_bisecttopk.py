import random
from fractions import Fraction as F

def A(S):
    s = sorted(S, reverse=True)
    total = F(0); sign=1
    for x in s:
        total += sign*x; sign*=-1
    return total

random.seed(4)

def a_n(n):
    return F(2**n, 2**(n+1)-1)

def D_n(n):
    return 2**(n+1)-1

viol=0
trials=0
for n in range(1,8):
    m = n+1
    for k in range(0, n+1):
        for _ in range(200):
            trials+=1
            # random marking sorted descending
            vals = sorted([F(random.randint(1,999), random.randint(1,50)) for _ in range(m)], reverse=True)
            T = sum(vals)
            M_k = []
            for i in range(k):
                M_k += [vals[i]/2, vals[i]/2]
            R = vals[k:]
            M_k = M_k + R
            phi = (T + A(M_k))/2
            pk1 = vals[k] if k < m else F(0)
            bound = (T + pk1)/2
            if phi > bound:
                viol+=1
                print("PHI EXCEEDS BOUND", n,k,vals,phi,bound)
            # check threshold condition
            if pk1 <= T/D_n(n):
                if phi > a_n(n)*T:
                    viol+=1
                    print("THRESHOLD FAILS", n,k,vals,phi,a_n(n)*T)
print("trials", trials, "violations", viol)
