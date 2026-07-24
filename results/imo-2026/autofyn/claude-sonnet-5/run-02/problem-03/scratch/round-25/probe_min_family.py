from fractions import Fraction as F
import itertools

a3 = F(8,15)

def bisect_subset_phi(p, S):
    idx = [i for i in range(4) if i not in S]
    R = [p[i] for i in idx]
    A = sum((F(1) if k%2==0 else F(-1))*v for k,v in enumerate(R))
    return (F(1)+A)/2

# candidate minimal family found by greedy: bisect{1,4}(0-indexed {0,3}), bisect{1,2}({0,1}), DS-Above, R22.1.1
def chambers(p):
    p1,p2,p3,p4 = p
    out = []
    out.append(("bisect14", True, bisect_subset_phi(p, {0,3})))
    out.append(("bisect12", True, bisect_subset_phi(p, {0,1})))
    out.append(("DS-Above", p1 > p2+p3, p1+p4/2))
    out.append(("R22.1.1", (p1 >= 2*p3) and (p2 <= p3+p4), p1/2+p3+p4))
    return out

def covered(p):
    for name, feas, phi in chambers(p):
        if feas and (a3-phi) >= 0:
            return name
    return None

import random
random.seed(42)
uncov = 0
trials = 200000
worst = None
worst_margin = F(10)
for _ in range(trials):
    # random rational-ish via random.uniform then Fraction with limited denom for speed -> use float then check w/ float, flag close ones for exact recheck
    p1 = random.uniform(0.0001, 0.4999)
    p2 = random.uniform(1/15+1e-6, min(p1, 4/15-1e-6))
    if p2 <= 0: continue
    rem = 1-p1-p2
    if rem <= 0: continue
    p3 = random.uniform(0.00001, rem)
    p4 = rem-p3
    if not (p1>=p2>=p3>=p4>0): continue
    p = (p1,p2,p3,p4)
    # float version check
    def bisect_f(S):
        idx=[i for i in range(4) if i not in S]
        R=[p[i] for i in idx]
        A=sum((1 if k%2==0 else -1)*v for k,v in enumerate(R))
        return (1+A)/2
    cands=[]
    phi = bisect_f({0,3}); cands.append((True, 8/15-phi))
    phi = bisect_f({0,1}); cands.append((True, 8/15-phi))
    feas = p1>p2+p3; phi=p1+p4/2; cands.append((feas, 8/15-phi))
    feas = (p1>=2*p3) and (p2<=p3+p4); phi=p1/2+p3+p4; cands.append((feas,8/15-phi))
    ok = any(f and g>=-1e-12 for f,g in cands)
    if not ok:
        uncov += 1
        m = max(g for f,g in cands if True)  # not quite right but track
        if worst is None or True:
            worst = p
print("trials", trials, "uncovered(float,4-chamber family)", uncov)
if worst:
    print("example uncovered point:", worst)
