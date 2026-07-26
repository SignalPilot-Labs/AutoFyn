"""Independent numerical sanity check: A >= 1/15 for real Xiang marks at n=3.
Fine grid + random. This VALIDATES (not proves) the vertex enumeration."""
import random
from fractions import Fraction as F

LIU_marks = [F(1,15), F(3,15), F(7,15)]

def A_real(x1,x2,x3):
    cuts = sorted(set([0,1] + list(LIU_marks) + [x1,x2,x3]))
    pieces = [cuts[i+1]-cuts[i] for i in range(len(cuts)-1)]
    pieces.sort(reverse=True)
    A = F(0)
    for i,p in enumerate(pieces):
        A += (1 if i%2==0 else -1)*p
    return A

# fine rational grid on [0,1]^3 with denominator 300 (=20*15, finer than D(3)=15)
N = 60   # grid denominator 60 -> 60^3 = 216000 points, denominator 60 = 4*15
worst = None
minv = None
viol = 0
cnt = 0
import itertools
for i in range(N+1):
  for j in range(N+1):
    for k in range(N+1):
        x1=F(i,N); x2=F(j,N); x3=F(k,N)
        # skip if any equals a Liu mark (degenerate, but A still defined)
        A = A_real(x1,x2,x3)
        cnt += 1
        if A < F(1,15):
            viol += 1
            if viol <= 5: print("GRID VIOL", (x1,x2,x3), A, A-F(1,15))
        if minv is None or A < minv:
            minv = A; worst=(x1,x2,x3)
print(f"grid points: {cnt}, violations: {viol}, min A = {minv} ({minv-F(0)}) at {worst}")

# random reals
random.seed(12345)
viol2 = 0
minv2 = None
for _ in range(300000):
    x1 = F(random.randint(0,10**6),10**6)
    x2 = F(random.randint(0,10**6),10**6)
    x3 = F(random.randint(0,10**6),10**6)
    A = A_real(x1,x2,x3)
    if A < F(1,15):
        viol2 += 1
        if viol2<=5: print("RAND VIOL",(x1,x2,x3),A)
    if minv2 is None or A < minv2:
        minv2 = A
print(f"random points: 300000, violations: {viol2}, min A = {minv2}")
