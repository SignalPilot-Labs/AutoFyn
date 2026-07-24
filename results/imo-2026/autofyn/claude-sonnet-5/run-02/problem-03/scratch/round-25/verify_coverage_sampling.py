from fractions import Fraction as F
import random

a3 = F(8,15)

def chambers_ok(p1,p2,p3,p4):
    T=p1+p2+p3+p4
    assert T==1
    results = []
    # Bisect{1,4}
    phi14 = (1+p2-p3)/2
    results.append(("B14", True, phi14<=a3))
    # Bisect{1,2}
    phi12 = (1+p3-p4)/2
    results.append(("B12", True, phi12<=a3))
    # DS-Above
    feas_dsa = p1>p2+p3
    phi_dsa = p1+p4/2
    results.append(("DSA", feas_dsa, feas_dsa and phi_dsa<=a3))
    # Triple-Pin
    feas_tp = p1>p2+p3
    phi_tp = 1-p1
    results.append(("TP", feas_tp, feas_tp and phi_tp<=a3))
    # R22.1.1
    feas_r22 = (p1>=2*p3) and (p2<=p3+p4)
    phi_r22 = p1/2+p3+p4
    results.append(("R22", feas_r22, feas_r22 and phi_r22<=a3))
    return results

random.seed(42)
violations = 0
trials = 300000
for _ in range(trials):
    # sample p1>=p2>=p3>=p4>0, p1<1/2, 1/15<p2<4/15, sum=1
    # generate via rejection: pick random p2 in (1/15,4/15), p1 in (p2,1/2), p3 in (0,p2], p4=1-p1-p2-p3 with p4<=p3 and p4>0
    p2 = F(random.randint(1,999999),15000000)+F(1,15)+F(1,15000000)
    if not (F(1,15) < p2 < F(4,15)):
        continue
    p1 = p2 + F(random.randint(1,999999),3000000)
    if not (p1 < F(1,2)):
        continue
    if not (p1 >= p2):
        continue
    p3 = F(random.randint(1, int(p2*1000000)-1), 1000000) if p2>0 else F(0)
    if not (0 < p3 <= p2):
        continue
    p4 = 1 - p1 - p2 - p3
    if not (0 < p4 <= p3):
        continue
    res = chambers_ok(p1,p2,p3,p4)
    covered = any(succ for (_,_,succ) in res)
    if not covered:
        violations += 1
        print("VIOLATION", p1,p2,p3,p4, res)
        if violations>5: break

print("trials effectively used, violations:", violations)
