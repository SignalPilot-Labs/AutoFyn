from fractions import Fraction as F
import random

def A(S):
    S = sorted(S, reverse=True)
    return sum((-1)**i * S[i] for i in range(len(S)))

def N(S,x):
    return sum(1 for v in S if v>x)

def indicator_integral(S, lo, hi):
    pts = sorted(set([lo,hi]+[v for v in S if lo<v<hi]))
    total = F(0)
    for i in range(len(pts)-1):
        a,b=pts[i],pts[i+1]
        mid=(a+b)/2
        if N(S,mid)%2==1:
            total += (b-a)
    return total

def ladder(n):
    D=2**(n+1)-1
    return [F(2**(n+1-i),D) for i in range(1,n+2)]

# Cross-Term Reduction Theorem check: F={x,p1-x}, x>=p1-x, G' random tail refinement
random.seed(2)
n=3
p=ladder(n)
p1=p[0]; T=p[1:]; r=sum(T)
for trial in range(20):
    x_frac = F(random.randint(50,99),100)
    x = x_frac*p1
    if x < p1-x: x = p1-x
    Delta = 2*x - p1
    # random tail refinement G' of T (split each piece randomly into 2, using budget <=2 cuts, just test single split)
    idx = random.choice(range(len(T)))
    piece = T[idx]
    t = F(random.randint(1,99),100)
    a = t*piece; b = piece-a
    Gp = T[:idx]+T[idx+1:]+[a,b]
    F1 = [x, p1-x]
    lhs = A(F1+Gp)
    W_lo, W_hi = p1-x, x
    v_int = indicator_integral(Gp, max(W_lo,F(0)), min(W_hi,r))
    AGp = A(Gp)
    rhs = Delta + AGp - 2*v_int
    print(trial, lhs==rhs, lhs, rhs)
