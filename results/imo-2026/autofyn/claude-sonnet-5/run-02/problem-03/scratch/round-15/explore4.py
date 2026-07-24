import random
from fractions import Fraction as F

def ladder(n):
    D = 2**(n+1) - 1
    return [F(2**(n+1-i), D) for i in range(1, n+2)], D

def A(S):
    S = sorted(S, reverse=True)
    total = F(0); sign=1
    for x in S:
        total += sign*x; sign=-sign
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
        v = total_mass * fr / 2
        out.extend([v, v])
    return out

random.seed(3)

def test_item4(n, trials=20000):
    # ell(F)>=3 (exactly 3 residuals, generic case), F is p1's split,
    # G' is a FULL legal refinement of the ENTIRE tail {p2,...,p_{n+1}} (p2 included!)
    pieces, D = ladder(n)
    p1 = pieces[0]
    full_tail = pieces[1:]   # includes p2 this time
    fn = F(1,D)
    worst=None; tested=0; info=None
    for _ in range(trials):
        num_pairs = random.randint(0,2)
        cuts_on_F = (3+2*num_pairs)-1   # fragments-1
        remaining = n - cuts_on_F        # budget left for tail refinement (n total cuts)
        if remaining < 0: continue
        a = F(random.randint(1,999),1000)
        b = F(random.randint(1,999),1000)*a
        c = F(random.randint(1,999),1000)*b
        s = a+b+c
        if s<=0: continue
        if num_pairs==0:
            frac = F(1)
        else:
            frac = F(random.randint(1,95),100)
        scale = frac*p1/s
        v1,v2,v3 = a*scale,b*scale,c*scale
        rem = p1-(v1+v2+v3)
        if num_pairs==0:
            if rem != 0: continue
            P=[]
        else:
            if rem<=0: continue
            P = exact_pair_set(rem, num_pairs)
        cuts = random.randint(0, remaining)
        Rp = random_refinement(full_tail, cuts)
        S = [v1,v2,v3]+P+Rp
        assert sum(S) == F(1), (sum(S),)
        val = A(S)
        tested+=1
        if worst is None or val<worst:
            worst=val; info=(v1,v2,v3,P,Rp,cuts,remaining,num_pairs)
    return worst, fn, (worst-fn if worst is not None else None), tested, info

for n in [3,4,5,6,7]:
    w,t,s,cnt,info = test_item4(n)
    print(f"n={n}: item4 ell>=3: min={float(w):.6f} f(n)={float(t):.6f} slack={float(s):.6f} tested={cnt}")
    if s < 0:
        print("  VIOLATION:", info)
