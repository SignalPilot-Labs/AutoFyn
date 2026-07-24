from fractions import Fraction as F
import random

def A(S):
    S = sorted(S, reverse=True)
    return sum((-1)**i * S[i] for i in range(len(S)))

# Verify Lemma 14: A(S') - A(S) = 2(I1+I2) - 2 f2
def N(S, x):
    return sum(1 for v in S if v > x)

def indicator_integral(R, lo, hi, samplepts=None):
    # integral of 1[N_R(x) odd] over [lo,hi) -- since piecewise constant, compute via breakpoints
    # breakpoints are elements of R within (lo,hi)
    pts = sorted(set([lo,hi]+[v for v in R if lo<v<hi]))
    total = F(0)
    for i in range(len(pts)-1):
        a,b = pts[i], pts[i+1]
        mid = (a+b)/2
        if N(R, mid) % 2 == 1:
            total += (b-a)
    return total

random.seed(1)
mism = 0
for trial in range(3000):
    k = random.randint(1,5)
    R = [F(random.randint(1,50), random.randint(1,50)) for _ in range(k)]
    M = F(random.randint(1,50), random.randint(1,50))
    t = F(random.randint(1,99), 100)
    f1 = t*M if t*M >= M - t*M else M - t*M
    f2 = M - f1
    if f1 < f2:
        f1, f2 = f2, f1
    S = R + [M]
    Sp = R + [f1, f2]
    lhs = A(Sp) - A(S)
    I1 = indicator_integral(R, F(0), f2)
    I2 = indicator_integral(R, f1, M)
    rhs = 2*(I1+I2) - 2*f2
    if lhs != rhs:
        mism += 1
        print("MISMATCH", R, M, f1, f2, lhs, rhs)
print("Lemma14 trials done, mismatches:", mism)
