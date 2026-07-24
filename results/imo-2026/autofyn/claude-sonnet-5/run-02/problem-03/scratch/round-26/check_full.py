from fractions import Fraction as F
import random

a3 = F(8,15); a2 = F(4,7)

def phi_via_6templates(trip):
    a,b,c = sorted(trip, reverse=True)
    T = a+b+c
    def Phi(pieces):
        s = sorted(pieces, reverse=True)
        alt = sum((x if i%2==0 else -x) for i,x in enumerate(s))
        return (T_total+alt)/2
    T_total = sum(pieces_total := [a,b,c])
    cands=[]
    cands.append(Phi([a/2,a/2,b,c]))
    cands.append(Phi([a/2,a/2,b/2,b/2,c]))
    cands.append(Phi([a,b,c/2,c/2]))
    cands.append(Phi([a,b/2,b/2,c/2,c/2]))
    if a>=b:
        cands.append(Phi([a-b,b,b,c]))
    if a>=c:
        cands.append(Phi([a-c,b,c,c]))
    return min(cands)

def chambers_status(p1,p2,p3,p4):
    T=p1+p2+p3+p4
    Phi14=(T+p2-p3)/2
    Phi12=(T+p3-p4)/2
    g14=a3*T-Phi14
    g12=a3*T-Phi12
    DSA_TP_feasible = p1>p2+p3
    PhiDSA=p1+p4/2
    PhiTP=T-p1
    gDSA=a3*T-PhiDSA
    gTP=a3*T-PhiTP
    R22_feasible=(p1>=2*p3) and (p2<=p3+p4)
    PhiR22=p1/2+p3+p4
    gR22=a3*T-PhiR22
    succ = (g14>=0) or (g12>=0) or (DSA_TP_feasible and gDSA>=0) or (DSA_TP_feasible and gTP>=0) or (R22_feasible and gR22>=0)
    return succ

def case_a_bound(p1,p2,p3,p4):
    T=p1+p2+p3+p4
    w=p1-p2
    Tprime = w+p3+p4
    phip = phi_via_6templates([w,p3,p4])
    total = p2+phip
    return total<=a3*T, total

random.seed(2)
N=100000
fails=0
for _ in range(N):
    denom=1000
    vals = sorted([random.randint(1,denom) for _ in range(4)], reverse=True)
    p1,p2,p3,p4 = [F(v) for v in vals]
    T=p1+p2+p3+p4
    if p2<=T/15:
        # case b1
        Phi = (T+p2)/2  # bisect p1 alone with A(tail)<=p2 -> actual achieved via max domination is upper bound only
        # just check theorem's guarantee holds: bisect p1 alone achieved value:
        # exact Phi for bisect-p1 alone = (T+A(tail))/2 with A(tail) computed exactly
        tail=sorted([p2,p3,p4],reverse=True)
        alt=tail[0]-tail[1]+tail[2]
        Phi_exact = (p1)/2 + (( (T-p1) + alt)/2)
        ok = Phi_exact <= a3*T
        case='b1'
    elif p2<T*4/15:
        ok = chambers_status(p1,p2,p3,p4)
        case='b2'
    else:
        ok,_ = case_a_bound(p1,p2,p3,p4)
        case='a'
    if not ok:
        fails+=1
        print("FAIL", case, p1,p2,p3,p4)

print("total fails:", fails, "/", N)
