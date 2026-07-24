from fractions import Fraction as F
import random

a3 = F(8,15)

def chambers_ok(p1,p2,p3,p4):
    results = []
    phi14 = (1+p2-p3)/2
    results.append(("B14", True, phi14<=a3))
    phi12 = (1+p3-p4)/2
    results.append(("B12", True, phi12<=a3))
    feas_dsa = p1>p2+p3
    phi_dsa = p1+p4/2
    results.append(("DSA", feas_dsa, feas_dsa and phi_dsa<=a3))
    feas_tp = p1>p2+p3
    phi_tp = 1-p1
    results.append(("TP", feas_tp, feas_tp and phi_tp<=a3))
    feas_r22 = (p1>=2*p3) and (p2<=p3+p4)
    phi_r22 = p1/2+p3+p4
    results.append(("R22", feas_r22, feas_r22 and phi_r22<=a3))
    return results

random.seed(7)
N = 2000000
SCALE = 100000
count=0
violations=0
worst_margin = None
for _ in range(N):
    p2n = random.randint(1, SCALE-1)  # p2/T scaled, need 1/15<p2<4/15 -> p2n in (SCALE/15, 4SCALE/15)
    lo2, hi2 = SCALE/15, 4*SCALE/15
    if not (lo2 < p2n < hi2): continue
    p2 = F(p2n, SCALE)
    p1n = random.randint(p2n, SCALE//2 -1)
    if p1n <= p2n: continue
    p1 = F(p1n, SCALE)
    if not (p1 < F(1,2)): continue
    p3n = random.randint(1, p2n)
    p3 = F(p3n, SCALE)
    p4n = SCALE - p1n - p2n - p3n
    if p4n <=0 or p4n > p3n: continue
    p4 = F(p4n, SCALE)
    # sanity checks
    if not (p1>=p2>=p3>=p4>0): continue
    count += 1
    res = chambers_ok(p1,p2,p3,p4)
    covered = any(succ for (_,_,succ) in res)
    if not covered:
        violations += 1
        print("VIOLATION", p1,p2,p3,p4,res)

print("valid samples:", count, "violations:", violations)
