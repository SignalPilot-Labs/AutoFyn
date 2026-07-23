import random

def L_of_pieces(cuts):
    s = sorted(cuts, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def one_cut(pieces, rng, base):
    i = rng.randrange(len(pieces))
    p = pieces.pop(i)
    r = rng.random()
    if r < 0.3:
        t = p/2
    elif r < 0.9:
        v = rng.choice(base+pieces) if pieces else rng.choice(base)
        t = v if v < p else p*rng.random()
    else:
        t = p*rng.random()
    pieces.extend([t, p-t])
    return pieces

def g_numeric_n(base, ncuts, ntrials, seed=0):
    rng = random.Random(seed)
    best = 999.0
    for _ in range(ntrials):
        k = rng.randrange(ncuts+1)
        pieces = list(base)
        for _ in range(k):
            pieces = one_cut(pieces, rng, base)
        val = L_of_pieces(pieces)
        if val < best:
            best = val
    return best

# n=3 dyadic point (8,4,2,1)/15
dy = [8/15,4/15,2/15,1/15]
print("g(dyadic n=3) approx:", g_numeric_n(dy, 3, 300000, seed=1), " target 8/15=", 8/15)

def sorted4(v):
    return sorted(v, reverse=True)

def test_conc_n(p1,p2,ncuts,ntrials,label,seed=0):
    p1 = sorted4(p1); p2 = sorted4(p2)
    mid = sorted4([(a+b)/2 for a,b in zip(p1,p2)])
    g1 = g_numeric_n(p1, ncuts, ntrials, seed=seed+1)
    g2 = g_numeric_n(p2, ncuts, ntrials, seed=seed+2)
    gm = g_numeric_n(mid, ncuts, ntrials, seed=seed+3)
    avg = (g1+g2)/2
    print(f"{label}: g1={g1:.4f} g2={g2:.4f} avg={avg:.4f} gmid={gm:.4f} concave_ok={gm>=avg-3e-3}")

test_conc_n(dy, [0.4,0.3,0.2,0.1], 3, 150000, "n=3 dyadic vs uniform-ish")
test_conc_n([0.6,0.2,0.15,0.05], [0.45,0.3,0.15,0.1], 3, 150000, "n=3 two random pts")

print("\nRe-check with more trials:")
test_conc_n(dy, [0.4,0.3,0.2,0.1], 3, 600000, "n=3 dyadic vs uniform-ish (more trials)", seed=100)
