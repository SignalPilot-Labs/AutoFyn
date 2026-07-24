from fractions import Fraction as F
import random

D3 = F(15)
a3 = F(8,15)

def alt_sum(lst):
    lst = sorted(lst, reverse=True)
    A=F(0); s=1
    for x in lst:
        A+=s*x; s=-s
    return A

def phi_of(lst):
    T=sum(lst)
    return (T+alt_sum(lst))/2

def bisect_phi(p, k):
    tail = p[k:]
    return (sum(p)+alt_sum(tail))/2

def altgapcross_j1(p):
    p1,p2,p3,p4 = p
    T=sum(p)
    if p1<=p2: return None
    gamma1 = min(p1-p2, p2)
    if gamma1 > p3:
        A = (p1-p2) - (p3-p4)
        return (T+A)/2
    return None

def altgapcross_j2(p):
    p1,p2,p3,p4 = p
    T=sum(p)
    if p1<=p2 or p3<=p4: return None
    gamma1 = min(p1-p2,p2)
    need = max(p4, p3-p4)
    if gamma1 > need:
        A = (p1-p2)-(p3-p4)
        return (T+A)/2
    return None

def chamberA(p):
    p1,p2,p3,p4=p
    if p1>=3*p4 and p1<=2*p3+p4:
        return p2+(p1+p4)/2
    return None

def chamberA2(p):
    p1,p2,p3,p4=p
    if p1<=p2+2*p4:
        return (p1+p2)/2+p3
    return None

def thmD_bisect_top_bottom(p):
    p1,p2,p3,p4 = p
    # middle {p2,p3}, budget1: min(untouched p2, bisect p2 -> phi)
    frags = [p2/2,p2/2,p3]
    phi_bisect_mid = phi_of(frags)
    phi_mid = min(p2, phi_bisect_mid)
    return (p1+p4)/2 + phi_mid

def thmE_bisect_top_two(p):
    p1,p2,p3,p4 = p
    # bisect p1,p2; recurse on {p3,p4} budget1
    frags = [p3/2,p3/2,p4]
    phi_bisect_tail = phi_of(frags)
    phi_tail = min(p3, phi_bisect_tail)
    return (p1+p2)/2 + phi_tail

def best_known(p):
    vals=[]
    for k in range(4):
        vals.append(bisect_phi(p,k))
    for fn in (altgapcross_j1, altgapcross_j2, chamberA, chamberA2, thmD_bisect_top_bottom, thmE_bisect_top_two):
        v = fn(p)
        if v is not None:
            vals.append(v)
    return min(vals)

random.seed(1)
denom=300
def sample():
    while True:
        raw = [random.randint(1,denom) for _ in range(4)]
        raw.sort(reverse=True)
        s = sum(raw)
        p = [F(r,s) for r in raw]
        p1,p2,p3,p4 = p
        if p1 < F(1,2) and F(1,15) < p2 < F(4,15) and p1>=p2>=p3>=p4>0:
            return p

trials=8000
covered=0
uncovered=[]
for _ in range(trials):
    p=sample()
    m=best_known(p)
    if m<=a3:
        covered+=1
    else:
        uncovered.append((p,m))

print("tested",trials,"covered",covered,"uncovered",len(uncovered))
for p,m in uncovered[:20]:
    print([float(x) for x in p], float(m-a3))
