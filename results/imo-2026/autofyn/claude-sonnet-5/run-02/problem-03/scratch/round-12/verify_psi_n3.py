from fractions import Fraction as F
def A(ms):
    s=sorted(ms,reverse=True); tot=F(0); sign=1
    for x in s: tot+=sign*x; sign*=-1
    return tot
tau=[F(4,15),F(2,15),F(1,15)]
import random
random.seed(0)
for _ in range(2000):
    num=random.randint(1,3999)
    t=F(num,4000)*F(4,15)
    psi=A([t]+tau)
    if t<=F(1,15):
        pred=-t+F(1,5)
    elif t<=F(2,15):
        pred=t+F(1,15)
    else:
        pred=-t+F(1,3)
    if psi!=pred:
        print("MISMATCH", t, psi, pred)
print("done")
