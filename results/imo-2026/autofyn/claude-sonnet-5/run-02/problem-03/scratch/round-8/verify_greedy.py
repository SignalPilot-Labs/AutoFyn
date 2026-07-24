from fractions import Fraction as F
import random

def A(ms):
    s=sorted(ms, reverse=True)
    tot=F(0)
    for i,v in enumerate(s):
        tot += v if i%2==0 else -v
    return tot

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

def random_refine(pieces, cuts):
    pieces = pieces[:]
    for _ in range(cuts):
        idx = random.randrange(len(pieces))
        v = pieces.pop(idx)
        t = F(random.randint(1,999),1000)
        a = v*t
        b = v-a
        pieces += [a,b]
    return pieces

random.seed(3)
viol=0
tested=0
for trial in range(3000):
    n = random.randint(2,5)
    p = ladder(n)
    p1 = p[0]
    tail = p[1:]
    t = random.randint(1,3)
    # positive weights summing to 1000, strictly positive
    raw = [random.randint(1,300) for _ in range(t)]
    S = sum(raw)
    avals = [p1*F(w,S) for w in raw]
    assert sum(avals)==p1
    Fm = []
    for a in avals:
        Fm += [a,a]
    cuts = random.randint(0,3)
    Gp = random_refine(tail, cuts)
    lhs = A(Fm+Gp)
    rhs = A(Gp)
    tested+=1
    if lhs != rhs:
        viol+=1
        print("MISMATCH", n, avals, Gp, lhs, rhs)

print("tested",tested,"violations",viol)
