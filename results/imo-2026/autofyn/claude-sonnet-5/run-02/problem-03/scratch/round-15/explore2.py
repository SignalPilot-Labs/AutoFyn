import random
from fractions import Fraction as F

def ladder(n):
    D = 2**(n+1) - 1
    return [F(2**(n+1-i), D) for i in range(1, n+2)], D

def A(S):
    S = sorted(S, reverse=True)
    total = F(0)
    sign = 1
    for x in S:
        total += sign * x
        sign = -sign
    return total

def random_split(piece, cuts):
    if cuts == 0:
        return [piece]
    pts = sorted(random.sample(range(1, 10000), cuts))
    pts = [F(p, 10000) for p in pts]
    bounds = [F(0)] + pts + [F(1)]
    fracs = [(bounds[i+1]-bounds[i]) for i in range(len(bounds)-1)]
    return [piece*fr for fr in fracs]

def random_refinement(pieces, total_cuts):
    k = len(pieces)
    if total_cuts <= 0:
        return list(pieces)
    cuts_alloc = [0]*k
    for _ in range(total_cuts):
        cuts_alloc[random.randrange(k)] += 1
    result = []
    for p, c in zip(pieces, cuts_alloc):
        result.extend(random_split(p, c))
    return result

def exact_pair_set(total_mass, num_pairs):
    if num_pairs == 0:
        return []
    pts = sorted(random.sample(range(1, 10000), num_pairs-1)) if num_pairs > 1 else []
    pts = [F(p, 10000) for p in pts]
    bounds = [F(0)] + pts + [F(1)]
    fracs = [(bounds[i+1]-bounds[i]) for i in range(len(bounds)-1)]
    out = []
    for fr in fracs:
        v = total_mass * fr
        out.extend([v, v])
    return out

random.seed(2)

def test_item3_fixed(n, trials=4000):
    # ell(F)=2 subcase c: v1>=p2>v2, P nonempty exact pairing, tau_P >= p3
    # cuts_on_F = (2 residuals + 2*num_pairs fragments) - 1 = 1+2*num_pairs
    pieces, D = ladder(n)
    p1, p2, p3 = pieces[0], pieces[1], pieces[2]
    tail = pieces[2:]
    fn = F(1, D)
    worst = None; worst_cfg=None
    tested=0
    for _ in range(trials):
        num_pairs = random.randint(1, 2)
        cuts_on_F = 1 + 2*num_pairs
        remaining = n - cuts_on_F
        if remaining < 0:
            continue
        v1 = p2 + F(random.randint(0, 9999), 10000) * (p1-p2)
        v2 = F(random.randint(1, 9999), 10000) * p2
        tau_P = p3 + F(random.randint(0, 9999), 10000) * (p2 - p3)
        # need v1+v2+tau_P <= p1 for legality (F's total = p1)
        if v1+v2+tau_P > p1:
            continue
        P = exact_pair_set(tau_P, num_pairs)
        cuts = random.randint(0, remaining)
        Rp = random_refinement(tail, cuts)
        S = [v1, v2] + P + Rp
        val = A(S)
        tested += 1
        if worst is None or val < worst:
            worst = val; worst_cfg=(v1,v2,tau_P,num_pairs,cuts)
    return worst, fn, (worst-fn if worst is not None else None), tested

def test_item4_fixed(n, trials=6000):
    pieces, D = ladder(n)
    p1 = pieces[0]
    tail = pieces[2:]
    fn = F(1, D)
    worst=None; worst_cfg=None; tested=0
    for _ in range(trials):
        num_pairs = random.randint(0,2)
        cuts_on_F = (3 + 2*num_pairs) - 1  # 3 residuals + pairs, minus 1
        remaining = n - cuts_on_F
        if remaining < 0:
            continue
        a = F(random.randint(1,999),1000)
        b = F(random.randint(1,999),1000)*a
        c = F(random.randint(1,999),1000)*b
        s = a+b+c
        if s<=0: continue
        scale = F(random.randint(1,95),100) * p1 / s
        v1,v2,v3 = a*scale,b*scale,c*scale
        rem = p1-(v1+v2+v3)
        if rem <= 0: continue
        P = exact_pair_set(rem, num_pairs) if num_pairs>0 else []
        if num_pairs==0 and rem>0:
            continue  # rem must be zero if no pairs allowed; skip illegal config
        cuts = random.randint(0, remaining)
        Rp = random_refinement(tail, cuts)
        S = [v1,v2,v3] + P + Rp
        val = A(S)
        tested+=1
        if worst is None or val<worst:
            worst=val; worst_cfg=(v1,v2,v3,cuts,num_pairs)
    return worst, fn, (worst-fn if worst is not None else None), tested

for n in [3,4,5,6]:
    print(f"=== n={n} ===")
    w,t,s,cnt = test_item3_fixed(n)
    print(f"item3_tauP>=p3 (budget-fixed): min={float(w) if w is not None else None}, f(n)={float(t):.6f}, slack={float(s) if s is not None else None}, tested={cnt}")
    w,t,s,cnt = test_item4_fixed(n)
    print(f"item4_ell3 (budget-fixed): min={float(w) if w is not None else None}, f(n)={float(t):.6f}, slack={float(s) if s is not None else None}, tested={cnt}")
