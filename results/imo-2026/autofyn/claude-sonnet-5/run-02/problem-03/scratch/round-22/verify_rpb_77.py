from fractions import Fraction as F
import random

def A(S):
    S = sorted(S, reverse=True)
    total = F(0)
    for i, v in enumerate(S):
        total += (1 if i%2==0 else -1) * v
    return total

def ladder(n):
    D = 2**(n+1)-1
    f = F(1, D)
    return [F(2**(n+1-i))*f for i in range(1, n+2)]

def random_legal_refinement(pieces, budget):
    r = len(pieces)
    cuts = [0]*r
    remaining = budget
    for i in range(r):
        c = random.randint(0, remaining)
        cuts[i] = c
        remaining -= c
    out = []
    for i, piece in enumerate(pieces):
        c = cuts[i]
        if c == 0:
            out.append(piece)
        else:
            pts = sorted(F(random.randint(1, 999999), 1000000) * piece for _ in range(c))
            prev = F(0)
            for pt in pts:
                out.append(pt - prev)
                prev = pt
            out.append(piece - prev)
    return out

n = 4
p = ladder(n)
p1,p2,p3,p4,p5 = p
s = p3+p4+p5
f_n = F(1, 2**(n+1)-1)
assert p2 - s == f_n

random.seed(42)
fails = 0
trials = 50000
minmarg_diamond = None
minmarg_sharp = None
for _ in range(trials):
    Rp = random_legal_refinement([p3,p4,p5], n-3)  # budget 1
    v1 = p2 * F(random.randint(1,999999),1000000)  # in (0,p2) roughly, then filter
    # want v1 in (s, p2)
    v1 = s + (p2-s)*F(random.randint(1,999999),1000000)
    # want v2 in (p2-v1, s)
    lo = p2 - v1
    if lo >= s:
        continue
    v2 = lo + (s-lo)*F(random.randint(1,999999),1000000)
    R_gt_v2 = [x for x in Rp if x > v2]
    Delta = A(Rp) - 2*A(R_gt_v2)
    eps = 1 if (len(R_gt_v2) % 2 == 1) else 0
    marg_sharp = (s-(v1-v2)-2*v2*eps) - Delta
    marg_diamond = (v2 - f_n - 2*v2*eps) - Delta
    diff = marg_sharp - marg_diamond
    predicted = p2 - v1
    if diff != predicted:
        fails += 1
        if fails < 5:
            print("MISMATCH", Rp, v1, v2, diff, predicted)
    if minmarg_diamond is None or marg_diamond < minmarg_diamond:
        minmarg_diamond = marg_diamond
    if minmarg_sharp is None or marg_sharp < minmarg_sharp:
        minmarg_sharp = marg_sharp

print(f"trials effectively run, fails={fails}")
print("min marg_diamond'=", minmarg_diamond, float(minmarg_diamond))
print("min marg_sharp'=", minmarg_sharp, float(minmarg_sharp))
