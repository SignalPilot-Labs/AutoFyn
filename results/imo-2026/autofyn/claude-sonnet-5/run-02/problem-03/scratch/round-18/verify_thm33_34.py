from fractions import Fraction as Fr
import random, itertools

def f(n):
    return Fr(1, 2**(n+1)-1)

def ladder(n):
    fn = f(n)
    return [ (2**(n+1-i)) * fn for i in range(1, n+2) ]  # p_1..p_{n+1}

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = 0
    for i,x in enumerate(s):
        if i % 2 == 0:
            total += x
        else:
            total -= x
    return total

def random_refinement(piece, max_cuts):
    # split a single piece into random number of positive fragments (<= max_cuts+1 fragments)
    k = random.randint(0, max_cuts)  # number of cuts on this piece
    if k == 0:
        return [piece]
    # random cut points
    cuts = sorted(Fr(random.randint(1,999),1000) for _ in range(k))
    cuts = [Fr(0)] + cuts + [Fr(1)]
    fracs = [cuts[i+1]-cuts[i] for i in range(len(cuts)-1)]
    return [piece*x for x in fracs if x > 0]

def legal_refinement(pieces, total_cut_budget):
    # distribute cut budget among pieces randomly, sum of cuts <= total_cut_budget
    m = len(pieces)
    # random partition of budget
    remaining = total_cut_budget
    cuts_per_piece = [0]*m
    for _ in range(remaining):
        idx = random.randint(0, m-1)
        cuts_per_piece[idx]+=1
    frags = []
    for p,c in zip(pieces, cuts_per_piece):
        frags.extend(random_refinement(p, c))
    return frags

def test_theorem33(n, trials):
    fn = f(n)
    p = ladder(n)
    p1,p2 = p[0], p[1]
    tailpieces = p[2:]  # p3..p_{n+1}
    s = sum(tailpieces)
    viol=0
    minmargin = None
    for _ in range(trials):
        budget = random.randint(0, n-1)  # unrestricted per theorem 33 claim
        Rp = legal_refinement(tailpieces, budget)
        # v1 in (s,p2), v2 in [s,v1)
        if p2 <= s: continue
        v1 = s + (p2-s)*Fr(random.randint(1,999),1000)
        v2 = s + (v1-s)*Fr(random.randint(0,999),1000)  # v2 in [s, v1)
        F = [v1, v2]  # P = empty
        Gp = [p2]+Rp
        final = F+Gp
        Aval = A(final)
        margin = Aval - fn
        if minmargin is None or margin < minmargin:
            minmargin = margin
        if Aval <= fn:
            viol+=1
            print("VIOLATION thm33", n, v1, v2, Aval, fn)
    return viol, minmargin

def test_theorem34(n, trials):
    fn = f(n)
    p = ladder(n)
    p1,p2 = p[0], p[1]
    tailpieces = p[2:]
    s = sum(tailpieces)
    viol=0
    minmargin=None
    for _ in range(trials):
        budget = random.randint(0, n-2) if n>=2 else 0
        Rp = legal_refinement(tailpieces, budget)
        if p2 <= s: continue
        v1 = s + (p2-s)*Fr(random.randint(1,999),1000)
        # v2 < s and v1+v2 <= p2  => v2 <= min(s, p2-v1)
        upper = min(s, p2-v1)
        if upper <= 0: continue
        v2 = upper*Fr(random.randint(0,999),1000)
        F=[v1,v2]
        Gp=[p2]+Rp
        final=F+Gp
        Aval=A(final)
        margin = Aval-fn
        if minmargin is None or margin<minmargin:
            minmargin=margin
        if Aval < fn:
            viol+=1
            print("VIOLATION thm34", n, v1, v2, Aval, fn)
    return viol, minmargin

random.seed(1)
for n in range(3,7):
    v,m = test_theorem33(n, 3000)
    print("Thm33 n=",n,"violations=",v,"minmargin=",float(m) if m else None)
for n in range(3,7):
    v,m = test_theorem34(n, 3000)
    print("Thm34 n=",n,"violations=",v,"minmargin=",float(m) if m else None)
