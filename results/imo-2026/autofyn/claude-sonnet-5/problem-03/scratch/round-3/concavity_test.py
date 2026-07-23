import random
from fractions import Fraction as F

def L_of_pieces(cuts):
    # cuts: sorted list of piece lengths (already the pieces, not boundary points)
    s = sorted(cuts, reverse=True)
    L = sum(s[i] for i in range(0,len(s),2))
    return L

def g_numeric(a1,a2,a3, ncuts=2, ntrials=60000, seed=0):
    # LB pieces a1,a2,a3 (a1+a2+a3=1). XY adds up to ncuts points that further split
    # any of the pieces. We model by choosing, for each of the ncuts points, which
    # piece index (0,1,2) it lands in and where within that piece (fraction).
    # We do random search + local refinement using many candidate "tie" positions.
    base = [a1,a2,a3]
    best = 999.0
    rng = random.Random(seed)
    candidates_frac = []
    # candidate cut fractions within a piece: bisect (0.5), or match to produce
    # a sub-piece equal to a1,a2,a3 (if that value < piece length)
    for trial in range(ntrials):
        # randomly decide 0,1,2 cuts and their piece assignment + position
        k = rng.choice([0,1,1,2,2,2])  # bias toward using cuts
        pieces = list(base)
        if k>=1:
            i = rng.randrange(len(pieces))
            p = pieces.pop(i)
            # choose cut position: random, or bisect, or match to a base value
            r = rng.random()
            if r < 0.3:
                t = p/2
            elif r < 0.9:
                # match to a random existing value (from base) if smaller than p
                v = rng.choice(base)
                t = v if v < p else p*rng.random()
            else:
                t = p*rng.random()
            pieces.extend([t, p-t])
        if k>=2:
            i = rng.randrange(len(pieces))
            p = pieces.pop(i)
            r = rng.random()
            if r < 0.3:
                t = p/2
            elif r < 0.9:
                v = rng.choice(pieces+base)
                t = v if v < p else p*rng.random()
            else:
                t = p*rng.random()
            pieces.extend([t, p-t])
        val = L_of_pieces(pieces)
        if val < best:
            best = val
    return best

# sanity check against known dyadic point n=2: expect L=4/7 ~ 0.5714
print("g(4/7,2/7,1/7) approx:", g_numeric(4/7,2/7,1/7, ntrials=200000))
print("target 4/7 =", 4/7)

def sorted3(a,b,c):
    return sorted([a,b,c], reverse=True)

def test_concavity(pt1, pt2, ntrials=150000, label=""):
    a1,a2,a3 = pt1
    b1,b2,b3 = pt2
    mid = ((a1+b1)/2, (a2+b2)/2, (a3+b3)/2)
    mid = sorted3(*mid)
    g1 = g_numeric(*sorted3(*pt1), ntrials=ntrials)
    g2 = g_numeric(*sorted3(*pt2), ntrials=ntrials)
    gm = g_numeric(*mid, ntrials=ntrials)
    avg = (g1+g2)/2
    print(f"{label}: g(pt1)={g1:.5f} g(pt2)={g2:.5f} avg={avg:.5f} g(mid)={gm:.5f}  concave_ok={gm>=avg-1e-3}")

random.seed(1)
# Test 1: near the dyadic point, both endpoints in Case ii region
test_concavity((4/7,2/7,1/7), (0.5,0.3,0.2), label="dyadic vs (0.5,0.3,0.2)")
# Test 2: far apart points
test_concavity((0.9,0.05,0.05), (0.34,0.33,0.33), label="near-degenerate vs near-uniform")
# Test 3: crossing Case i / ii boundary
test_concavity((0.8,0.15,0.05), (0.45,0.3,0.25), label="Case i pt vs Case ii pt")
# Test 4: dyadic vs a Case-i point
test_concavity((4/7,2/7,1/7), (0.9,0.08,0.02), label="dyadic vs deep Case i")
# Test 5: two points both far from dyadic, same side
test_concavity((0.7,0.2,0.1), (0.6,0.25,0.15), label="two Case i-ish points")
