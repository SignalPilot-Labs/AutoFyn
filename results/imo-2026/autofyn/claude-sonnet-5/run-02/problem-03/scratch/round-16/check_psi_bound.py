from fractions import Fraction as F
import random

def A(S, v=None):
    if v is None:
        lst = sorted(S, reverse=True)
    else:
        lst = sorted([x for x in S if x > v], reverse=True)
    s = F(0); sign=1
    for x in lst:
        s += sign*x; sign*=-1
    return s

def eps(S, v):
    cnt = sum(1 for x in S if x>v)
    return 1 if cnt%2==1 else 0

def ladder(k):
    denom = 2**(k+1)-1
    return [F(2**(k+1-i),1)*F(1,denom) for i in range(1,k+2)]

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
    Q = ladder(k)  # this plays the role of the rescaled (n-2)-ladder tail
    s = sum(Q)  # =1
    budget = k
    worst_margin = None
    for _ in range(trials):
        Rp = random_legal_response(Q, budget)
        v = F(random.randint(0,999),1000)*s
        Ar = A(Rp)
        Arv = A(Rp, v)
        ev = eps(Rp, v)
        psi = Ar - 2*Arv + 2*v*ev
        margin = psi - (v-s)
        if worst_margin is None or margin < worst_margin:
            worst_margin = margin
    print(f"k={k}: worst margin (psi - (v-s)) = {worst_margin}  [should be >=0]")

for k in [1,2,3,4,5]:
    test(k, 20000)
