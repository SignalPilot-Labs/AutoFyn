import random
from fractions import Fraction as F

def phi(fragments):
    s = sorted(fragments, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def random_split(p, k, denom=120):
    if k == 0:
        return [p]
    cuts = sorted(random.sample(range(1, denom), k))
    positions = [0] + cuts + [denom]
    parts = [F(positions[i+1]-positions[i], denom) * p for i in range(len(positions)-1)]
    return parts

def search_min(p, n, trials=30000, denom=120, max_cuts_per_piece=None):
    m = len(p)
    best = None
    beststruct = None
    comps = []
    def gen(i, remaining, cur):
        if i == m:
            comps.append(tuple(cur))
            return
        for c in range(0, remaining+1):
            gen(i+1, remaining-c, cur+[c])
    gen(0, n, [])
    for comp in comps:
        trials_here = max(2, trials // max(1,len(comps)))
        for _ in range(trials_here):
            frags = []
            for i in range(m):
                frags += random_split(p[i], comp[i], denom=denom)
            val = phi(frags)
            if best is None or val < best:
                best = val
                beststruct = (comp, sorted(frags, reverse=True))
    return best, beststruct

random.seed(2)
# n=4, p1<T/2 random marking, normalize total = 1
raw = [37, 22, 18, 14, 9]  # descending, p1=37/100 < 1/2
tot = sum(raw)
p = [F(x, tot) for x in raw]
n = len(p) - 1
a_n = F(2**n, 2**(n+1)-1)
best, struct = search_min(p, n, trials=40000, denom=200)
print("marking", p, "T/2=", F(1,2), "p1=", p[0])
print("target a_n*T=", float(a_n), a_n)
print("found min approx", float(best), best)
print("comp/frags", struct)
