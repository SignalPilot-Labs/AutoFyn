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

rng = random.Random(123)
for n in [3, 4]:
    p = ladder(n)
    fn = f(n)
    worst = None
    for _ in range(200000):
        frags = rand_legal_response(p, n, rng)
        val = A(frags) - fn
        if worst is None or val < worst:
            worst = val
    print(n, "min margin over 200000 trials (full undecomposed L(n) check):", float(worst))
