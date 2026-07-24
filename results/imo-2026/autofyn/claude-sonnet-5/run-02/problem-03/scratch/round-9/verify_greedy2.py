from fractions import Fraction as F
import random

def A(S):
    S = sorted(S, reverse=True)
    total = F(0)
    sign = 1
    for x in S:
        total += sign*x
        sign *= -1
    return total

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

def funit(n):
    return F(1, 2**(n+1)-1)   # f(n) = 1/(2^{n+1}-1), a_n = p1 = 2^n f(n)

def refine_random(pieces, cuts):
    pcs = list(pieces)
    for _ in range(cuts):
        idx = random.randrange(len(pcs))
        x = pcs[idx]
        if x <= 0: continue
        t = F(random.randint(1,999),1000)
        a = x*t
        b = x-a
        if a==0 or b==0: continue
        pcs[idx]=a
        pcs.append(b)
    return pcs

random.seed(3)
for n in [3,4,5,6]:
    p = ladder(n)
    p2 = p[1]
    tail = p[1:]
    R = tail[1:]
    best = F(0)
    for trial in range(5000):
        cuts = n-2
        Gp = refine_random(R, cuts)  # p2 uncut
        full = [p2]+Gp
        val = A(full)
        if val > best: best = val
    bound = p2 - funit(n)
    print(n, "max A(G') found (p2-uncut sub-case):", best, " bound p2-f(n):", bound, "OK" if best<=bound else "VIOLATION")

# Also test full (dagger) over ALL refinements (including cutting p2), not just p2-uncut sub-case
random.seed(4)
for n in [3,4,5]:
    p = ladder(n)
    p2 = p[1]
    tail = p[1:]
    best = F(0)
    argmax=None
    for trial in range(20000):
        cuts = n-2
        Gp = refine_random(tail, cuts)
        val = A(Gp)
        if val > best:
            best = val
            argmax = Gp
    bound = p2 - funit(n)
    print(n, "FULL dagger max A(G'):", best, " bound:", bound, "OK" if best<=bound else "VIOLATION", argmax)
