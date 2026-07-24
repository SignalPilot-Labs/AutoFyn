import random
from fractions import Fraction as F

def A(S):
    s = sorted(S, reverse=True)
    total = F(0)
    sign = 1
    for x in s:
        total += sign*x
        sign = -sign
    return total

def rand_multiset(n):
    return [F(random.randint(1,50), random.randint(1,20)) for _ in range(n)]

random.seed(1)

# 1. Max Domination Lemma: A(S) <= max(S)
viol=0
for _ in range(20000):
    r = random.randint(1,10)
    S = rand_multiset(r)
    if A(S) > max(S):
        viol+=1
print("MaxDomination violations:", viol)

# 2. Triangle bound: A(X)-A(Y) <= A(X union Y) <= A(X)+A(Y)
viol=0
for _ in range(20000):
    nx = random.randint(1,5); ny = random.randint(1,5)
    X = rand_multiset(nx); Y = rand_multiset(ny)
    AX, AY, AXY = A(X), A(Y), A(X+Y)
    if not (AX - AY - F(1,10**9) <= AXY <= AX+AY+F(1,10**9)):
        viol+=1
print("Triangle bound violations:", viol)

def D(n): return 2**(n+1)-1
def a(n): return F(2**n, D(n))

# 3. R13.2 unconditional p2-threshold closure
viol=0; hits=0
for _ in range(20000):
    n = random.randint(1,7)
    m = n+1
    if m<2: continue
    pieces = sorted([F(random.randint(1,50), random.randint(1,20)) for _ in range(m)], reverse=True)
    T = sum(pieces)
    p1, p2 = pieces[0], pieces[1] if m>=2 else F(0)
    if p2 <= T/F(D(n)):
        hits+=1
        # bisect p1 strategy: tail A(tail) computed directly
        tail = pieces[1:]
        Atail = A(tail)
        Phi = F(p1,2) + (T-p1+Atail)/2
        if Phi > a(n)*T + F(1,10**9):
            viol+=1
print("R13.2 hits:", hits, "violations:", viol)
