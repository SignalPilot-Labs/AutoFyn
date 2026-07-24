from fractions import Fraction as Fr
import random

def f(n):
    return Fr(1, 2**(n+1)-1)

def ladder(n):
    fn = f(n)
    return [Fr(2**(n+1-i))*fn for i in range(1, n+2)]

def A(mset):
    ms = sorted(mset, reverse=True)
    tot, sign = Fr(0), 1
    for x in ms:
        tot += sign*x
        sign *= -1
    return tot

def rand_legal_response(pieces, budget, rng):
    k = len(pieces)
    used = rng.randint(0, budget)
    cuts = [0]*k
    for _ in range(used):
        cuts[rng.randint(0, k-1)] += 1
    frags = []
    for piece, c in zip(pieces, cuts):
        if c == 0:
            frags.append(piece)
        else:
            pts = sorted(Fr(rng.randint(1,999999),1000000) for _ in range(c))
            pts = [Fr(0)] + pts + [Fr(1)]
            frags += [piece*(pts[i+1]-pts[i]) for i in range(len(pts)-1)]
    return frags

rng = random.Random(2023)
print("Theorem 37 check: b=p4, T'={p4}+T'' (T'' legal <=n-4-cut response to {p5..p_{n+1}})")
for n in range(5, 10):
    p = ladder(n)
    p3, p4 = p[2], p[3]
    tail_lower = p[4:]  # p5..p_{n+1}
    fn = f(n)
    worst = None
    for _ in range(20000):
        Tpp = rand_legal_response(tail_lower, n-4, rng)
        B = [p4, p4] + Tpp
        val = A(B) - fn
        if worst is None or val < worst:
            worst = val
    print(n, "min margin over 20000 trials:", float(worst), "(0 = tight)")
