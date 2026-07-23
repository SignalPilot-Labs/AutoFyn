import random

def L_of_pieces(cuts):
    s = sorted(cuts, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def one_cut(pieces, rng, base):
    i = rng.randrange(len(pieces))
    p = pieces.pop(i)
    r = rng.random()
    if r < 0.15:
        t = p/2
    elif r < 0.97:
        pool = base+pieces
        v = rng.choice(pool)
        t = v if v < p else p*rng.random()
    else:
        t = p*rng.random()
    pieces.extend([t, p-t])
    return pieces

def g_numeric_n(base, ncuts, ntrials, seed=0):
    rng = random.Random(seed)
    best = 999.0
    for _ in range(ntrials):
        k = ncuts  # always use full budget - using fewer never helps XY minimize (more cuts weakly better)
        pieces = list(base)
        for _ in range(k):
            pieces = one_cut(pieces, rng, base)
        val = L_of_pieces(pieces)
        if val < best:
            best = val
    return best

dy = [8/15,4/15,2/15,1/15]
other = [0.4,0.3,0.2,0.1]
mid = sorted([(a+b)/2 for a,b in zip(dy,other)], reverse=True)
print("points:", dy, other, mid)
for seed in [1,2,3]:
    g1 = g_numeric_n(dy, 3, 400000, seed=seed*10+1)
    g2 = g_numeric_n(other, 3, 400000, seed=seed*10+2)
    gm = g_numeric_n(mid, 3, 400000, seed=seed*10+3)
    print(f"seed{seed}: g1={g1:.5f} g2={g2:.5f} avg={(g1+g2)/2:.5f} gmid={gm:.5f}")
