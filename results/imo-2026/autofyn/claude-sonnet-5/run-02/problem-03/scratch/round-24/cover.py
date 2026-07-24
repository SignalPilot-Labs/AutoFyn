from fractions import Fraction as F
import random, itertools

D3 = F(15)
a3 = F(8,15)

def bisect_phi(p, k):
    # p sorted descending list of Fractions, m=4
    tail = p[k:]
    # alternating sum of tail
    A = F(0)
    sign = 1
    for x in tail:
        A += sign*x
        sign = -sign
    T = sum(p)
    return (T + A)/2

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

def best_known(p):
    T=sum(p)
    vals=[]
    for k in range(4):
        vals.append(bisect_phi(p,k))
    for fn in (altgapcross_j1, altgapcross_j2, chamberA, chamberA2):
        v = fn(p)
        if v is not None:
            vals.append(v)
    return min(vals), vals

# sample grid: n=3, T=1, p1>=p2>=p3>=p4>0, p2 in (1/15, 4/15), p1<1/2
random.seed(1)
N=100
denom = 300
uncovered = []
tested = 0
covered = 0
for _ in range(4000):
    # random rational sample
    # pick p2 in (1/15,4/15)
    lo2, hi2 = F(1,15), F(4,15)
    p2 = lo2 + F(random.randint(1,denom-1), denom)*(hi2-lo2)
    # p1 in (p2, 1/2)
    hi1 = F(1,2)
    if p2>=hi1: continue
    p1 = p2 + F(random.randint(1,denom-1), denom)*(hi1-p2)
    # p3 in (0, p2], p4 in (0,p3]
    p3 = F(random.randint(1,denom-1), denom)*p2
    p4 = F(random.randint(1,denom-1), denom)*p3
    rest = 1 - p1 - p2 - p3 - p4
    if rest <= 0:
        continue
    # need p3>=p4 and account for 'rest' -- instead let's directly normalize four positive fractions
    # simpler: pick p1,p2,p3,p4 proportional then normalize to sum 1, then re-check case-b2 box
    continue

# Better: direct approach - sample p1,p2,p3,p4 with sum=1 via Dirichlet-like random fractions, filter to box
def sample():
    while True:
        raw = [random.randint(1,denom) for _ in range(4)]
        raw.sort(reverse=True)
        s = sum(raw)
        p = [F(r,s) for r in raw]
        p1,p2,p3,p4 = p
        if p1 < F(1,2) and F(1,15) < p2 < F(4,15) and p1>=p2>=p3>=p4>0:
            return p

trials = 3000
uncovered_list = []
for _ in range(trials):
    p = sample()
    tested += 1
    m, vals = best_known(p)
    if m <= a3:
        covered += 1
    else:
        uncovered_list.append((p, m))

print("tested", tested, "covered", covered, "uncovered", len(uncovered_list))
for p,m in uncovered_list[:15]:
    print([float(x) for x in p], float(m), float(a3))
