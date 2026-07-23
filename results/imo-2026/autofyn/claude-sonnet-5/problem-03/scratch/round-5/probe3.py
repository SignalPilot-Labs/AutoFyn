import random
from fractions import Fraction as F
exec(open('/tmp/round-5/probe2.py').read().split("random.seed(7)")[0])  # reuse functions

def target(m):
    return F(1, 2**(m+1)-1)

random.seed(42)
def rand_case2(k, denom=30):
    while True:
        vals = sorted([random.randint(1,denom) for _ in range(k)], reverse=True)
        if vals[-1]==0: continue
        Afull=[F(v) for v in vals]
        a1,a2=Afull[0],Afull[1]
        if a1 < 2*a2:
            return tuple(Afull)

fails=0; total=0
for m in [5]:
    k=m+1
    trials=15
    tgt=target(m)
    for t in range(trials):
        A = rand_case2(k, denom=25)
        S=sum(A)
        val = one_shot_optimal(A,m)
        bound = tgt*S
        total+=1
        if bound-val<0:
            fails+=1
            print("FAIL", m, A, val, float(bound))
print("m=5 total",total,"fails",fails)
