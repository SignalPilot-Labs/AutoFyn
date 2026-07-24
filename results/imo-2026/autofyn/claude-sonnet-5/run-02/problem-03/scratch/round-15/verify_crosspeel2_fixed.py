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
    # p sorted descending, len m>=3. Requires p1 > p2+p3 for legality of this exact construction.
    m=len(p)
    p1,p2,p3 = p[0],p[1],p[2]
    tail = p[2:]  # includes p3
    assert p1 > p2+p3, "legality condition (‡) fails"
    lo = max(p2, p1-p2)
    hi = p1-p3
    assert lo<hi
    f1 = (lo+hi)/2
    f2 = p1-f1
    final = [f1,f2,p2]+list(tail)
    Phi=phi(final)
    predicted_A = (p1-p2) + A(tail)
    predicted_Phi=(sum(p)+predicted_A)/2
    return Phi,predicted_Phi

random.seed(11)
count=0
for _ in range(8000):
    m=random.randint(3,9)
    p=sorted([F(random.randint(1,50),random.randint(1,12)) for _ in range(m)],reverse=True)
    if p[0] <= p[1]+p[2]:
        continue
    Phi,pred = crosspeel2(p)
    assert Phi==pred,(p,Phi,pred)
    count+=1
print(f"Cross-Peel-2 (j=1) identity verified exactly on {count} random trials satisfying legality condition p1>p2+p3, zero mismatches.")
