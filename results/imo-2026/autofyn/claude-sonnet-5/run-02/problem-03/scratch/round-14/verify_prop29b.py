import random
from fractions import Fraction as F

def A(S):
    s = sorted(S, reverse=True)
    total = F(0); sign=1
    for x in s:
        total += sign*x; sign*=-1
    return total

def rand_frac(lo=1,hi=200):
    return F(random.randint(lo,hi), random.randint(1,30))

random.seed(2)
# Verify: P exact pairs invisibility even combined with extra set G
viol=0
trials=20000
for _ in range(trials):
    v = rand_frac()
    npairs = random.randint(0,3)
    P=[]
    for _ in range(npairs):
        val = rand_frac()
        P += [val,val]
    kg = random.randint(0,4)
    G = [rand_frac() for _ in range(kg)]
    lhs = A([v]+P+G)
    rhs = A([v]+G)
    if lhs!=rhs:
        viol+=1
        print("MISMATCH", v,P,G,lhs,rhs)
print("pair-invisibility trials", trials, "violations", viol)

# Verify sharp-dominant-removal-identity: A({f1}∪T) = f1 - A(T) when f1>max(T)
viol2=0
trials2=20000
for _ in range(trials2):
    kt = random.randint(0,5)
    T = [rand_frac() for _ in range(kt)]
    mx = max(T) if T else F(0)
    f1 = mx + rand_frac(1,50)  # f1>max(T)
    lhs = A([f1]+T)
    rhs = f1 - A(T)
    if lhs!=rhs:
        viol2+=1
        print("SHARP REMOVAL MISMATCH", f1, T, lhs, rhs)
print("sharp-removal trials", trials2, "violations", viol2)
