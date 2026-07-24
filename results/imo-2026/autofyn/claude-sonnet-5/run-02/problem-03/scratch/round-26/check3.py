from fractions import Fraction as F
import random

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
    succ14 = (g14>=0)
    succ12 = (g12>=0)
    succDSA = DSA_TP_feasible and (gDSA>=0)
    succTP = DSA_TP_feasible and (gTP>=0)
    succR22 = R22_feasible and (gR22>=0)
    return any([succ14,succ12,succDSA,succTP,succR22]), dict(g14=g14,g12=g12,gDSA=gDSA if DSA_TP_feasible else None,
                                                              gTP=gTP if DSA_TP_feasible else None, gR22=gR22 if R22_feasible else None)

# fine grid near boundaries: p1 in [1/2,0.999], p2 in (1/15+eps,4/15-eps), p3 near extremes
bad=[]
tested=0
N=400
for i in range(1,N):
    p1 = F(1,2) + (F(1)-F(1,2))*F(i,N)  # up to near 1
    for j in range(1,60):
        p2 = F(1,15) + (F(4,15)-F(1,15))*F(j,60)
        if p1 < p2: continue
        rem = 1-p1-p2
        if rem<=0: continue
        # p3 range [rem/2, min(p2,rem)]
        p3lo = rem/2
        p3hi = min(p2, rem)
        if p3lo>p3hi: continue
        for k in range(0,6):
            p3 = p3lo + (p3hi-p3lo)*F(k,5) if p3hi>p3lo else p3lo
            p4 = rem-p3
            if not (p1>=p2>=p3>=p4>0): continue
            tested+=1
            ok,_ = chambers_status(p1,p2,p3,p4)
            if not ok:
                bad.append((p1,p2,p3,p4))

print("tested:", tested, "bad:", len(bad))
for b in bad[:5]:
    print(b)
