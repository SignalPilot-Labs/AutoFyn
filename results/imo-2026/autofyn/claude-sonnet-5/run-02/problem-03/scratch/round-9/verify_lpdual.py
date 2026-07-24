from fractions import Fraction as F
import itertools, random

def phi(S):
    S = sorted(S, reverse=True)
    tot = F(0)
    for i,x in enumerate(S):
        if i%2==0: tot+=x
    return tot

def A(S):
    S = sorted(S, reverse=True)
    tot=F(0); sign=1
    for x in S:
        tot+=sign*x; sign*=-1
    return tot

def a(n):
    return F(2**n, 2**(n+1)-1)

# Telescoping threshold identity: a_{n-1} = a_n / (2*(1-a_n))
for n in range(1,15):
    lhs = a(n-1)
    rhs = a(n) / (2*(1-a(n)))
    assert lhs==rhs, (n, lhs, rhs)
print("Telescoping threshold identity: OK for n=1..14")

# Theorem C' identity: bisect p1, phi(combined) = p1/2 + phi(tail-refinement)
random.seed(5)
for trial in range(2000):
    m = random.randint(2,6)
    pieces = sorted([F(random.randint(1,50),random.randint(1,50)) for _ in range(m)], reverse=True)
    p1 = pieces[0]; tail = pieces[1:]
    # random refinement of tail
    def refine(pcs, cuts):
        pcs = list(pcs)
        for _ in range(cuts):
            idx = random.randrange(len(pcs))
            x = pcs[idx]
            t = F(random.randint(1,99),100)
            aa = x*t; bb = x-aa
            if aa==0 or bb==0: continue
            pcs[idx]=aa; pcs.append(bb)
        return pcs
    cuts = random.randint(0,3)
    Mp = refine(tail, cuts)
    combined = [p1/2, p1/2] + Mp
    lhs = phi(combined)
    rhs = p1/2 + phi(Mp)
    assert lhs == rhs, (pieces, Mp, lhs, rhs)
print("Theorem C' exact identity: OK, 2000 trials")

# n<=3 (p1>=T/2) closure: check that Theorem C' + Theorem A actually achieve <= a_3 T for all p1>=T/2, m=4
random.seed(6)
worst = None
for trial in range(200000):
    # random 4-piece marking with p1>=T/2
    T = F(1)
    while True:
        raw = [random.randint(1,300) for _ in range(4)]
        s = sum(raw)
        pieces = sorted([F(r,s) for r in raw], reverse=True)
        if pieces[0] >= F(1,2):
            break
    p1,p2,p3,p4 = pieces
    a3 = a(3)
    if p1 < a3:
        # Theorem A directly
        val = p1
    else:
        # Theorem C' with tail handled optimally... but we don't have exact optimal;
        # instead check: does exhaustive best-of-known-strategies on tail (3 pieces) achieve <= a2*T' ?
        # We trust P(3) fully closed elsewhere; here just check p1/2 + a2*(T-p1) <= a3
        T2 = F(1)-p1
        bound = p1/2 + a(2)*T2
        val = bound
    if val > a3 + F(0):
        if worst is None or val>worst[0]:
            worst = (val, pieces)
print("worst case found among p1>=T/2, m=4:", worst)
