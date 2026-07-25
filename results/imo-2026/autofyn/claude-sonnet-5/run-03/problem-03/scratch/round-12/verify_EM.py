from fractions import Fraction as F
import random

def oddsum(M):
    s = sorted(M, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

random.seed(3)
trials=20000
fails=0
for _ in range(trials):
    n = random.randint(0,7)
    N = [F(random.randint(1,200), random.randint(1,50)) for _ in range(n)]
    x1 = F(random.randint(1,200), random.randint(1,50))
    x2 = x1 + F(random.randint(0,200), random.randint(1,50))  # x2>=x1
    v1 = oddsum(N+[x1])
    v2 = oddsum(N+[x2])
    if v2 < v1 - F(1,10**9):
        fails+=1
        print("FAIL", N, x1, x2, v1, v2)
print("trials",trials,"fails",fails)
