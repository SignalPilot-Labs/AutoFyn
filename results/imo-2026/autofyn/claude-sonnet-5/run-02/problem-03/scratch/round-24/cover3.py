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
    frags = [p2/2,p2/2,p3]
    phi_bisect_mid = phi_of(frags)
    phi_mid = min(p2, phi_bisect_mid)
    return (p1+p4)/2 + phi_mid

def thmE_bisect_top_two(p):
    p1,p2,p3,p4 = p
    frags = [p3/2,p3/2,p4]
    phi_bisect_tail = phi_of(frags)
    phi_tail = min(p3, phi_bisect_tail)
    return (p1+p2)/2 + phi_tail

def new_double_sandwich(p):
    # p1 split into frag1 in (p3,p2), frag2=p1-frag1 in (p4,p3); p4 bisected (0 contribution)
    p1,p2,p3,p4=p
    lo = max(p3, p1-p3)
    hi = min(p2, p1-p4)
    if lo < hi:
        return (p1+p2+p3+p4 + p2+p3-p1)/2
    return None

def best_known(p, extra=True):
    vals=[]
    for k in range(4):
        vals.append(bisect_phi(p,k))
    fams = [altgapcross_j1, altgapcross_j2, chamberA, chamberA2, thmD_bisect_top_bottom, thmE_bisect_top_two]
    if extra:
        fams.append(new_double_sandwich)
    for fn in fams:
        v = fn(p)
        if v is not None:
            vals.append(v)
    return min(vals)

random.seed(2)
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

trials=10000
covered_without=0
covered_with=0
uncovered_with=[]
for _ in range(trials):
    p=sample()
    m1=best_known(p, extra=False)
    m2=best_known(p, extra=True)
    if m1<=a3: covered_without+=1
    if m2<=a3:
        covered_with+=1
    else:
        uncovered_with.append((p,m2))

print("tested",trials)
print("covered without new family:",covered_without, f"({100*covered_without/trials:.2f}%)")
print("covered WITH new double-sandwich family:",covered_with, f"({100*covered_with/trials:.2f}%)")
print("uncovered even with new family:", len(uncovered_with))
for p,m in uncovered_with[:20]:
    print([float(x) for x in p], float(m-a3))

def new_double_sandwich_above(p):
    p1,p2,p3,p4=p
    lo = max(p2, p1-p2)
    hi = p1-p3
    if lo < hi:
        return (p1+p2+p3+p4 + p1-p2-p3)/2
    return None

def best_known2(p):
    vals=[]
    for k in range(4):
        vals.append(bisect_phi(p,k))
    fams = [altgapcross_j1, altgapcross_j2, chamberA, chamberA2, thmD_bisect_top_bottom, thmE_bisect_top_two, new_double_sandwich, new_double_sandwich_above]
    for fn in fams:
        v = fn(p)
        if v is not None:
            vals.append(v)
    return min(vals)

covered2=0
uncovered2=[]
random.seed(3)
for _ in range(10000):
    p=sample()
    m=best_known2(p)
    if m<=a3: covered2+=1
    else: uncovered2.append((p,m))
print("\nWITH both double-sandwich families:")
print("covered:",covered2,f"({100*covered2/10000:.2f}%)","uncovered:",len(uncovered2))
for p,m in uncovered2[:20]:
    print([float(x) for x in p], float(m-a3))
