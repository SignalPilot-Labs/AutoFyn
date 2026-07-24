from fractions import Fraction as F
import random

def A(S):
    S = sorted(S, reverse=True)
    total = F(0)
    for i,x in enumerate(S):
        if i % 2 == 0:
            total += x
        else:
            total -= x
    return total

# Branch 3: q2=2 split into (y,2-y), y in [1,2)
def branch3_min(trials=20000):
    worst = None
    for _ in range(trials):
        y = F(random.randint(1,999999),1000000) + F(1,1)  # in (1,2)
        # also test y=1 exactly sometimes
        if random.random()<0.1:
            y = F(1,1)
        S = [4, y, 2-y, 1]
        # sweep c across breakpoints plus random c values
        cs = set()
        for b in [2-y,1,y,F(4,1)]:
            cs.add(b)
        for _ in range(20):
            cs.add(F(random.randint(1,400000),100000))
        for c in cs:
            if c<=0 or c>4: continue
            val = A(S+[c])
            if worst is None or val<worst[0]:
                worst = (val, y, c)
    return worst

def branch4_min(trials=20000):
    worst = None
    for _ in range(trials):
        z = F(random.randint(500000,999999),1000000)  # in [1/2,1)
        if random.random()<0.1:
            z = F(1,2)
        S = [4,2,z,1-z]
        cs = set([1-z,z,F(2,1),F(4,1)])
        for _ in range(20):
            cs.add(F(random.randint(1,400000),100000))
        for c in cs:
            if c<=0 or c>4: continue
            val = A(S+[c])
            if worst is None or val<worst[0]:
                worst = (val, z, c)
    return worst

print("Branch3 worst:", branch3_min())
print("Branch4 worst:", branch4_min())

# exact closed form check
# Branch3: at c=4, A should = 1 for all y
for yn in range(10,20):
    y = F(yn,10)
    if not (1<=y<2): continue
    S=[4,y,2-y,1,4]
    print("y=",y,"A=",A(S))

# Branch4 closed form at c=4: 3-2z
for zn in range(5,10):
    z=F(zn,10)
    if not (F(1,2)<=z<1): continue
    S=[4,2,z,1-z,4]
    print("z=",z,"A=",A(S), "predicted", 3-2*z)

print("---dense segment check branch3---")
import itertools
# check each closed-form piece exactly on random points within each open interval
random.seed(1)
mismatches = 0
for _ in range(3000):
    y = F(random.randint(1000001,1999999),1000000)  # (1,2)
    twomy = 2-y
    for interval,formula in [
        ((0,twomy), lambda c: 3+c),
        ((twomy,1), lambda c: 7-2*y-c),
        ((1,y), lambda c: 5-2*y+c),
        ((y,4), lambda c: 5-c),
    ]:
        lo,hi = interval
        if hi<=lo: continue
        c = lo + (hi-lo)*F(random.randint(1,999),1000)
        val = A([4,y,twomy,1,c])
        pred = formula(c)
        if val != pred:
            mismatches += 1
            print("MISMATCH branch3", y, c, val, pred)
print("branch3 mismatches:", mismatches)

print("---dense segment check branch4---")
mismatches=0
for _ in range(3000):
    z = F(random.randint(500001,999999),1000000) # (1/2,1)
    omz = 1-z
    for interval,formula in [
        ((0,omz), lambda c: 1+2*z+c),
        ((omz,z), lambda c: 3-c),
        ((z,2), lambda c: 3+c-2*z),
        ((2,4), lambda c: 7-c-2*z),
    ]:
        lo,hi=interval
        if hi<=lo: continue
        c = lo + (hi-lo)*F(random.randint(1,999),1000)
        val = A([4,2,z,omz,c])
        pred = formula(c)
        if val != pred:
            mismatches += 1
            print("MISMATCH branch4", z, c, val, pred)
print("branch4 mismatches:", mismatches)
