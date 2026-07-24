import sys, itertools, time
sys.path.insert(0,'/tmp/round-31')
from enum_chambers import gen_chambers
from fractions import Fraction as F

CHAMBERS = gen_chambers(5,4)

def A(vals):
    s=sorted(vals,reverse=True); tot=F(0); sign=1
    for v in s: tot+=sign*v; sign*=-1
    return tot

def phi_for_chamber(p, spec):
    partition, hosts, bisect_set = spec
    Q = []
    for B, h in zip(partition, hosts):
        if len(B) == 1:
            i = B[0]
            if i in bisect_set: continue
            else: Q.append(p[i])
        else:
            others = [i for i in B if i != h]
            s = sum(p[i] for i in others)
            rho = p[h] - s
            if rho < 0: return None
            Q.append(rho)
    T = sum(p)
    return (T + A(Q))/2

def best_phi(p):
    best=None
    for spec in CHAMBERS:
        v=phi_for_chamber(p,spec)
        if v is None: continue
        if best is None or v<best: best=v
    return best

a4 = F(16,31)
worst_margin = None
worst_p = None
count=0
t0=time.time()
for D in range(5, 26):
    for p1 in range(1, D+1):
        if not (5*p1 < D*... if False else True):
            pass
    # generate sorted compositions p1>=p2>=p3>=p4>=p5>=1 summing to D
    for p1 in range(1, D-3):
      for p2 in range(1, p1+1):
        if p2 > D - p1 - 2: pass
        for p3 in range(1, p2+1):
          for p4 in range(1, p3+1):
            p5 = D - p1 - p2 - p3 - p4
            if p5 < 1 or p5 > p4: continue
            p = [F(p1),F(p2),F(p3),F(p4),F(p5)]
            T = F(D)
            # region check
            if not (2*p1 < D):  # p1 < T/2
                continue
            if not (F(D,31) < F(p2) < F(8*D,31)):
                continue
            count += 1
            bp = best_phi(p)
            margin = bp - a4*T
            if worst_margin is None or margin < worst_margin:
                worst_margin = margin
                worst_p = p[:]
    print("D=",D,"cumulative count=",count,"worst so far=",worst_margin,"at",worst_p,"time",time.time()-t0, flush=True)
print("FINAL worst_margin", worst_margin, "at p=",worst_p, "count", count)
