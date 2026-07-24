from fractions import Fraction as F
import itertools, random

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = F(0)
    sign = 1
    for x in s:
        total += sign * x
        sign *= -1
    return total

def f(n):
    return F(1, 2**(n+1)-1)

def ladder(n):
    # p_i = 2^(n+1-i) f(n), i=1..n+1
    fn = f(n)
    return [2**(n+1-i)*fn for i in range(1, n+2)]

# enumerate all legal refinements of a list of pieces using exactly k total cuts
# (a "legal refinement": each piece is either whole or split into >=2 positive parts,
#  total number of cuts summed over pieces <= k). We generate refinements using
# random rational split points (dyadic-ish) to get exact Fractions, exploring many
# cut-count distributions and split ratios.

def random_split(piece, cuts):
    # split `piece` into cuts+1 positive fragments summing to piece, random exact fractions
    if cuts == 0:
        return [piece]
    # random breakpoints as fractions with small denominator
    denom = random.choice([2,3,4,5,6,7,8,10,12])
    pts = sorted(random.sample(range(1, denom), min(cuts, denom-1)))
    if len(pts) < cuts:
        # fallback smaller cuts
        cuts = len(pts)
    bps = [F(0)] + [F(p, denom) for p in pts] + [F(1)]
    fracs = [bps[i+1]-bps[i] for i in range(len(bps)-1)]
    return [piece*fr for fr in fracs if fr > 0]

def random_refinement(pieces, total_cuts):
    # distribute total_cuts among len(pieces) pieces randomly
    k = len(pieces)
    if total_cuts == 0:
        cuts_dist = [0]*k
    else:
        cuts_dist = [0]*k
        for _ in range(total_cuts):
            cuts_dist[random.randrange(k)] += 1
    out = []
    for p, c in zip(pieces, cuts_dist):
        out.extend(random_split(p, c))
    return out

def test_n(n, trials=20000, seed=0):
    random.seed(seed)
    p = ladder(n)  # p[0]=p1 ... p[n]=p_{n+1}
    p3 = p[2]; p4 = p[3]
    tail = p[3:]  # p4 ... p_{n+1}
    budget = n-4  # T' budget
    fn = f(n)
    worst = None
    worst_info = None
    viol = 0
    for t in range(trials):
        k = random.randint(0, budget)
        Tprime = random_refinement(tail, k)
        # candidate b values: 0, p4, and every element of T' (in (0,p4])
        cands = set()
        cands.add(F(0))
        cands.add(p4)
        for x in Tprime:
            if 0 < x <= p4:
                cands.add(x)
        for b in cands:
            B = [b] + Tprime
            val = A(B)
            if worst is None or val < worst:
                worst = val
                worst_info = (b, Tprime, k)
            if val < fn:
                viol += 1
                print("VIOLATION", n, b, Tprime, val, fn)
    print(f"n={n}: worst A(B)={worst} vs f(n)={fn}  (worst>=f(n): {worst>=fn})  violations={viol}")
    print("  worst config: b=",worst_info[0]," T'=",worst_info[1]," cuts=",worst_info[2])

for n in [5,6,7,8]:
    test_n(n, trials=8000, seed=n)

def which_argmin_stats(n, trials=20000, seed=1):
    random.seed(seed)
    p = ladder(n)
    p4 = p[3]
    tail = p[3:]
    budget = n-4
    fn = f(n)
    counts = {"b=0":0, "b=p4(symmetric)":0, "deep-tie":0}
    deep_tie_examples = []
    for t in range(trials):
        k = random.randint(0, budget)
        Tprime = random_refinement(tail, k)
        cands = [(F(0), "b=0"), (p4, "b=p4(symmetric)")]
        for x in Tprime:
            if 0 < x < p4:
                cands.append((x, "deep-tie"))
        best_val = None
        best_label = None
        for b, label in cands:
            B = [b] + Tprime
            val = A(B)
            if best_val is None or val < best_val:
                best_val = val
                best_label = label
        counts[best_label] += 1
        if best_label == "deep-tie" and val <= fn*3:  # collect near-tight examples
            deep_tie_examples.append((Tprime, best_val))
    print(f"n={n}: argmin distribution over {trials} trials: {counts}")
    if deep_tie_examples:
        print("  example deep-tie-argmin cases (T', A(B)):", deep_tie_examples[:3])

for n in [5,6,7,8,9]:
    which_argmin_stats(n, trials=5000, seed=100+n)
