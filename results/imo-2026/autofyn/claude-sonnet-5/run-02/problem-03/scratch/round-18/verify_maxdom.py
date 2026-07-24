from fractions import Fraction as Fr
import random

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = 0
    for i,x in enumerate(s):
        if i % 2 == 0:
            total += x
        else:
            total -= x
    return total

random.seed(2)
viol=0
for _ in range(20000):
    k = random.randint(1,8)
    S = [Fr(random.randint(1,1000),1000) for _ in range(k)]
    a = A(S)
    m = max(S)
    if a > m:
        viol+=1
        print("violation", S, a, m)
print("max-domination violations:", viol)
