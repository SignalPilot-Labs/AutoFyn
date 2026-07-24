from fractions import Fraction as F
import random

def A(S, v=None):
    if v is None:
        lst = sorted(S, reverse=True)
    else:
        lst = sorted([x for x in S if x > v], reverse=True)
    s = F(0); sign=1
    for x in lst:
        s += sign*x; sign*=-1
    return s

def ladder(n):
    denom = 2**(n+1)-1
    return [F(2**(n+1-i),1)*F(1,denom) for i in range(1,n+2)]

def random_legal_response_of(Q, budget):
    m = len(Q)
    cuts = [0]*m
    b = budget
    for i in range(m):
        c = random.randint(0, b)
        cuts[i] = c
        b -= c
    S = []
    for p, c in zip(Q, cuts):
        if c == 0:
            S.append(p)
        else:
            pts = sorted(random.sample(range(1,1000), c))
            pts = [0]+pts+[1000]
            fracs = [F(pts[i+1]-pts[i],1000)*p for i in range(len(pts)-1)]
            S.extend(fracs)
    return S

def random_F_ell1(p1, cuts_avail):
    # F = {v} u P, ell(F)=1: c=2 minimal (v,a,a); use up to cuts_avail cuts, but keep it simple:
    # random v in (0,p1), pair up the remainder using extra cuts if budget allows (P pairs exactly)
    v = F(random.randint(1,999),1000)*p1
    rem = p1 - v
    # split rem into k equal pairs (k up to (cuts_avail-1)//2 ... keep simple: one pair)
    P = [rem/2, rem/2]
    return [v]+P, 2  # uses 2 cuts

def test(n, trials=20000):
    P_ = ladder(n)
    p1 = P_[0]
    tau = P_[1:]  # p2..p_{n+1}
    p2 = tau[0]
    R_tail = tau[1:]  # p3..p_{n+1}, size n-1... wait need size n-2 pieces for R' budget n-2 cuts
    fn = F(1, 2**(n+1)-1)
    s = sum(R_tail)  # Total({p3,...,p_{n+1}})
    worst = None
    for _ in range(trials):
        F_, c_used = random_F_ell1(p1, n)
        v = F_[0]
        if v >= p2:
            continue  # only test v<p2 branch; specifically want v<s sub-branch
        # legal budget remaining for tail refinement: n - c_used = n-2
        Rp = random_legal_response_of(R_tail, n-2)
        Gp = [p2] + Rp
        total = F_ + Gp
        val = A(total)
        margin = val - fn
        if worst is None or margin < worst:
            worst = margin
            worst_v = v
    print(f"n={n}: worst margin A(FuG')-f(n) = {worst}  (f(n)={fn}, s={s})")

for n in [3,4,5,6]:
    test(n, 20000)
