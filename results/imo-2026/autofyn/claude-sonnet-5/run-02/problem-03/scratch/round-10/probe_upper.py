import itertools, random
from fractions import Fraction as F

def phi(fragments):
    s = sorted(fragments, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def random_split(p, k, denom=80):
    if k == 0:
        return [p]
    cuts = sorted(random.sample(range(1, denom), k))
    positions = [0] + cuts + [denom]
    parts = [F(positions[i+1]-positions[i], denom) * p for i in range(len(positions)-1)]
    return parts

def search_min(p, n, trials=8000, denom=80):
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
        if sum(comp) == 0:
            trials_here = 1
        else:
            trials_here = max(1, trials // max(1,len(comps)))
        for _ in range(trials_here):
            frags = []
            for i in range(m):
                frags += random_split(p[i], comp[i], denom=denom)
            val = phi(frags)
            if best is None or val < best:
                best = val
                beststruct = (comp, sorted(frags, reverse=True))
    return best, beststruct

random.seed(1)

witnesses = {
    "n3_w1 (3/8,1/4,1/4,1/8)": [F(3,8), F(1,4), F(1,4), F(1,8)],
    "n3_w2 (2/5,3/10,1/5,1/10)": [F(2,5), F(3,10), F(1,5), F(1,10)],
}

for name, p in witnesses.items():
    n = len(p) - 1
    a_n = F(2**n, 2**(n+1)-1)
    best, struct = search_min(p, n, trials=15000, denom=120)
    print(name, "target a_n*T =", float(a_n), a_n, "found min approx", float(best), best)
    print("   comp/frags", struct)
