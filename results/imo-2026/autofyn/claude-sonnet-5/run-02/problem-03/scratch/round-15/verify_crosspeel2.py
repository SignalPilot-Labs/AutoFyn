from fractions import Fraction as F
import random

def A(vals):
    s = sorted(vals, reverse=True)
    a = F(0); sign=1
    for v in s:
        a += sign*v; sign=-sign
    return a
def phi(vals):
    return (sum(vals)+A(vals))/2

def crosspeel2(p):
    # p sorted descending, len m>=2. Split p1 sandwiching p2 (if p1>p2); tail = p[2:]
    m=len(p)
    p1,p2 = p[0],p[1]
    tail = p[2:]
    if p1==p2:
        final = [p1,p2]+tail
    else:
        lo=max(p2,p1-p2); hi=p1
        assert lo<hi
        f=(lo+hi)/2
        final=[f,p1-f,p2]+tail
    Phi=phi(final)
    predicted_A=(p1-p2)+ (A(tail) if tail else F(0))
    predicted_Phi=(sum(p)+predicted_A)/2
    return Phi,predicted_Phi

random.seed(11)
for _ in range(5000):
    m=random.randint(2,9)
    p=sorted([F(random.randint(1,50),random.randint(1,12)) for _ in range(m)],reverse=True)
    Phi,pred = crosspeel2(p)
    assert Phi==pred,(p,Phi,pred)
print("Cross-Peel-2 (j=1) identity verified exactly on 5000 random trials, zero mismatches, legal for every marking with m>=2 (0 or 1 cuts).")
