from fractions import Fraction as F
import itertools, random

def ladder(k):
    # k-ladder: k+1 pieces, ratio 2, sum 1
    denom = 2**(k+1)-1
    return [F(2**(k+1-i),1)*F(1,denom) for i in range(1,k+2)]

def A_trunc(S, v):
    lst = sorted([x for x in S if x > v], reverse=True)
    s = F(0)
    sign = 1
    for x in lst:
        s += sign*x
        sign *= -1
    return s

def random_legal_response(Q, budget):
    m = len(Q)
    cuts = [0]*m
    b = budget
    for i in range(m):
        c = random.randint(0, b)
        cuts[i] = c
        b -= c
    S = []
    for p, c in zip(Q, cuts):
        if c == 0:
            S.append(p)
        else:
            pts = sorted(random.sample(range(1,1000), c))
            pts = [0]+pts+[1000]
            fracs = [F(pts[i+1]-pts[i],1000)*p for i in range(len(pts)-1)]
            S.extend(fracs)
    return S

def test(k, trials=20000):
    Q = ladder(k)
    budget = k
    worst_violation = F(0)
    viol_count = 0
    for _ in range(trials):
        S = random_legal_response(Q, budget)
        v = F(random.randint(0,999),1000)
        lhs = A_trunc(S, v)
        rhs = A_trunc(Q, v)
        if lhs > rhs:
            viol_count += 1
            if lhs - rhs > worst_violation:
                worst_violation = lhs - rhs
                print("violation", k, v, S, lhs, rhs)
    print(f"k={k}: violations={viol_count}/{trials}, worst={worst_violation}")

for k in [1,2,3,4]:
    test(k, 20000)
