from fractions import Fraction as F
import random, itertools

def phi(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def bisect_prefix(vals, k):
    # vals sorted desc list of 4 base pieces; bisect the first k of them each into two halves
    out = []
    for i,v in enumerate(vals):
        if i < k:
            out += [v/2, v/2]
        else:
            out.append(v)
    return out

def bisect_suffix(vals, k):
    # bisect the last k pieces (smallest) each into two halves
    n = len(vals)
    out = []
    for i,v in enumerate(vals):
        if i >= n-k:
            out += [v/2, v/2]
        else:
            out.append(v)
    return out

target = F(8,15)  # c(3) conjectured = 2^3/(2^4-1) = 8/15

random.seed(1)
worst_ratio = None
for trial in range(20000):
    # random p>=q>=r>=s>0 summing to 1, use fractions with small denom for exactness via random ints
    denom = random.choice([15,20,25,30,45,60,100])
    while True:
        a = sorted(random.sample(range(1, denom*4), 3))
        parts = [a[0], a[1]-a[0], a[2]-a[1], denom*4-a[2]]
        if all(x>0 for x in parts):
            break
    vals = sorted([F(x, denom*4) for x in parts], reverse=True)
    assert sum(vals)==1
    p,q,r,s = vals
    cands = {}
    cands['T1'] = phi(bisect_prefix(vals,1))
    cands['T2'] = phi(bisect_prefix(vals,2))
    cands['T3'] = phi(bisect_prefix(vals,3))
    cands['D1'] = phi(bisect_suffix(vals,1))
    cands['D2'] = phi(bisect_suffix(vals,2))
    cands['D3'] = phi(bisect_suffix(vals,3))
    m = min(cands.values())
    if worst_ratio is None or m > worst_ratio[0]:
        worst_ratio = (m, vals, cands)

print("Max over trials of min(templates):", worst_ratio[0], "=", float(worst_ratio[0]))
print("target:", target, float(target))
print("at vals:", worst_ratio[1])
print("cands:", worst_ratio[2])
