from fractions import Fraction as F
import random

D3 = F(15)
a3 = F(8,15)

def chambers_status(p1,p2,p3,p4):
    T = p1+p2+p3+p4
    assert T==1
    Phi14 = (1+p2-p3)/2
    Phi12 = (1+p3-p4)/2
    g14 = a3-Phi14
    g12 = a3-Phi12
    DSA_TP_feasible = p1 > p2+p3
    PhiDSA = p1+p4/2
    PhiTP = 1-p1
    gDSA = a3-PhiDSA
    gTP = a3-PhiTP
    R22_feasible = (p1>=2*p3) and (p2<=p3+p4)
    PhiR22 = p1/2+p3+p4
    gR22 = a3-PhiR22
    # success of each chamber (feasible and g>=0)
    succ14 = (g14>=0)  # unconditional feasibility
    succ12 = (g12>=0)
    succDSA = DSA_TP_feasible and (gDSA>=0)
    succTP = DSA_TP_feasible and (gTP>=0)
    succR22 = R22_feasible and (gR22>=0)
    return any([succ14,succ12,succDSA,succTP,succR22])

# random search, restricting p1 >= 1/2 (the region NOT covered by stated domain), p2 in (1/15,4/15)
random.seed(1)
bad=[]
N=200000
denom=1000
for _ in range(N):
    # sample p2 in (1/15,4/15)
    lo,hi = F(1,15), F(4,15)
    p2 = lo + (hi-lo)*F(random.randint(1,denom-1),denom)
    # sample p1 >= max(p2, 1/2), p1<=1-p2-p3-p4 ... need p1>=p2, and p1>=1/2
    p1lo = max(p2, F(1,2))
    # p1 must be < 1 (leave room for p3,p4>0)
    p1hi = F(999,1000)  # just cap below 1, refine via rejection
    if p1lo>=p1hi:
        continue
    p1 = p1lo + (p1hi-p1lo)*F(random.randint(0,denom),denom)
    # remaining mass for p3,p4
    rem = 1-p1-p2
    if rem<=0:
        continue
    # p3 in [rem/2, min(p2,rem)]  (need p3<=p2, p4<=p3, p3+p4=rem, p4>0 => p3<rem)
    p3lo = rem/2
    p3hi = min(p2, rem)
    if p3lo>p3hi:
        continue
    p3 = p3lo + (p3hi-p3lo)*F(random.randint(0,denom),denom)
    p4 = rem-p3
    if not (p1>=p2>=p3>=p4>0):
        continue
    if not chambers_status(p1,p2,p3,p4):
        bad.append((p1,p2,p3,p4))

print("trials effective, bad found:", len(bad))
for b in bad[:10]:
    print(b)
