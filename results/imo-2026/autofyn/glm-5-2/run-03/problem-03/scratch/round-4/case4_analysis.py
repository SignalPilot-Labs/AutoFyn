"""
Analyze the winning (peel, menu-member) pair in each regime, especially Case 4
(p2,p3 < 4/15, p4 > 1/15, p1 > 2/5). Goal: find a clean case split for the proof.
"""
import numpy as np
from itertools import product
np.random.seed(3)

def n2_full(rest):
    """Return dict of 4 menu D-values for rest (3 pieces)."""
    a,b,c = sorted(rest, reverse=True)
    T=a+b+c
    return {'c':c, 'B':abs(2*a-T), 'ab':a-b, 'bc':b-c}

def peel_rests(p):
    p1,p2,p3,p4=p
    out={}
    out['p1p2']=[p1-p2,p3,p4]
    out['p1p3']=[p1-p3,p2,p4]
    out['p1p4']=[p1-p4,p2,p3]
    out['p2p3']=[p2-p3,p1,p4]
    out['p2p4']=[p2-p4,p1,p3]
    out['p3p4']=[p3-p4,p1,p2]
    return out

def best_pair(p):
    best=1e9; bl=None; bm=None
    for pl,rest in peel_rests(p).items():
        menu=n2_full(rest)
        for m,v in menu.items():
            if v<best: best=v; bl=pl; bm=m
    return best,bl,bm

# Case 4 configs
def gen_case4():
    while True:
        x=sorted(np.random.dirichlet([1,1,1,1]),reverse=True)
        if x[1]<4/15 and x[2]<4/15 and x[3]>1/15:
            return tuple(x)

from collections import Counter
cnt=Counter()
subcnt=Counter()
for _ in range(20000):
    p=gen_case4()
    d,pl,m=best_pair(p)
    cnt[pl]+=1; subcnt[(pl,m)]+=1
print("Case 4 (p2,p3<4/15, p4>1/15): winning peel (counts):")
for k,v in cnt.most_common(): print(f"  {k}: {v}")
print("winning (peel,menu) (top):")
for k,v in subcnt.most_common(8): print(f"  {k}: {v}")

# In Case4, subcase by p1 regime
print("\nSubcase by p1:")
for plo,phi in [(0.4,7/15),(7/15,8/15),(8/15,0.8)]:
    sub=Counter()
    for _ in range(20000):
        p=gen_case4()
        if plo<=p[0]<phi:
            d,pl,m=best_pair(p)
            sub[(pl,m)]+=1
    print(f" p1 in [{plo:.4f},{phi:.4f}]:")
    for k,v in sub.most_common(5): print(f"   {k}: {v}")
