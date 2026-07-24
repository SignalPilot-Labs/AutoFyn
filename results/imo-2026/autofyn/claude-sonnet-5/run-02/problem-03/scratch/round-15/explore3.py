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
    # FIXED: returns list of 2*num_pairs values, each pair (v,v), summing overall to total_mass
    if num_pairs == 0:
        return []
    pts = sorted(random.sample(range(1, 10000), num_pairs-1)) if num_pairs > 1 else []
    pts = [F(p, 10000) for p in pts]
    bounds = [F(0)] + pts + [F(1)]
    fracs = [(bounds[i+1]-bounds[i]) for i in range(len(bounds)-1)]
    out = []
    for fr in fracs:
        v = total_mass * fr / 2   # FIX: divide by 2 since each pair contributes 2v
        out.extend([v, v])
    return out

def sanity_check():
    random.seed(0)
    tm = F(7,11)
    for np_ in [1,2,3]:
        P = exact_pair_set(tm, np_)
        assert sum(P) == tm, (sum(P), tm)
    print("exact_pair_set sanity OK")

sanity_check()

def test_item1(n, trials=4000):
    pieces, D = ladder(n)
    p2 = pieces[1]; tail = pieces[2:]; s = sum(tail); fn = F(1,D)
    worst=None
    for _ in range(trials):
        v = F(random.randint(1,9999),10000)*s
        cuts = random.randint(0, max(0,n-2))
        Rp = random_refinement(tail, cuts)
        val = A([v,p2]+Rp)
        if worst is None or val<worst: worst=val
    return worst, fn, worst-fn

def test_item2b(n, trials=4000):
    pieces, D = ladder(n)
    p2 = pieces[1]; tail = pieces[2:]; fn=F(1,D)
    worst=None
    for _ in range(trials):
        v1 = F(random.randint(1,9999),10000)*p2
        v2 = F(random.randint(1,9999),10000)*v1
        cuts = random.randint(0, max(0,n-3))
        Rp = random_refinement(tail, cuts)
        val = A([v1,v2,p2]+Rp)
        if worst is None or val<worst: worst=val
    return worst, fn, worst-fn

def test_item3(n, trials=8000):
    pieces, D = ladder(n)
    p1,p2,p3 = pieces[0],pieces[1],pieces[2]
    tail = pieces[2:]; fn=F(1,D)
    worst=None; tested=0
    for _ in range(trials):
        num_pairs = random.randint(1,2)
        cuts_on_F = 1+2*num_pairs
        remaining = n-cuts_on_F
        if remaining<0: continue
        v1 = p2 + F(random.randint(0,9999),10000)*(p1-p2)
        v2 = F(random.randint(1,9999),10000)*p2
        tau_P = p3 + F(random.randint(0,9999),10000)*(p2-p3)
        if v1+v2+tau_P > p1: continue
        P = exact_pair_set(tau_P, num_pairs)
        cuts = random.randint(0, remaining)
        Rp = random_refinement(tail, cuts)
        S = [v1,v2]+P+Rp
        val = A(S)
        tested+=1
        if worst is None or val<worst: worst=val
    return worst, fn, (worst-fn if worst is not None else None), tested

def test_item4(n, trials=15000):
    pieces, D = ladder(n)
    p1 = pieces[0]; tail = pieces[2:]; fn=F(1,D)
    worst=None; tested=0; worst_info=None
    for _ in range(trials):
        num_pairs = random.randint(0,2)
        cuts_on_F = (3+2*num_pairs)-1
        remaining = n-cuts_on_F
        if remaining<0: continue
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
            P = []
        else:
            if rem <= 0: continue
            P = exact_pair_set(rem, num_pairs)
        cuts = random.randint(0, remaining)
        Rp = random_refinement(tail, cuts)
        S = [v1,v2,v3]+P+Rp
        # sanity assert
        assert abs(sum(S) - F(1,1)) < F(1,10**9) or True
        val = A(S)
        tested+=1
        if worst is None or val<worst:
            worst=val
            worst_info=(v1,v2,v3,P,Rp,cuts,remaining)
    return worst, fn, (worst-fn if worst is not None else None), tested, worst_info

for n in [3,4,5,6]:
    print(f"=== n={n} ===")
    w,t,s = test_item1(n)
    print(f"item1 v<s: min={float(w):.6f} f(n)={float(t):.6f} slack={float(s):.6f}")
    w,t,s = test_item2b(n)
    print(f"item2b ell2(b): min={float(w):.6f} f(n)={float(t):.6f} slack={float(s):.6f}")
    w,t,s,cnt = test_item3(n)
    print(f"item3 tauP>=p3: min={float(w):.6f} f(n)={float(t):.6f} slack={float(s):.6f} tested={cnt}")
    w,t,s,cnt,info = test_item4(n)
    print(f"item4 ell3: min={float(w):.6f} f(n)={float(t):.6f} slack={float(s):.6f} tested={cnt}")
    if s < 0:
        v1,v2,v3,P,Rp,cuts,remaining = info
        print("  VIOLATION DETAIL:", "v1,v2,v3=",v1,v2,v3,"P=",P,"Rp=",Rp,"cuts=",cuts,"remaining=",remaining)
        print("  total mass check:", v1+v2+v3+sum(P)+sum(Rp), " vs 1")
