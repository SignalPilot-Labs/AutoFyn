from fractions import Fraction as F
import itertools, random

def Phi_of_multiset(vals):
    s = sorted(vals, reverse=True)
    total = sum(s)
    A = F(0)
    sign = 1
    for v in s:
        A += sign*v
        sign = -sign
    return (total+A)/2

def bisect_topk(p, k):
    # p sorted descending list of Fractions
    m = len(p)
    vals = []
    for i in range(k):
        vals += [p[i]/2, p[i]/2]
    vals += p[k:]
    return Phi_of_multiset(vals)

def peel_then_bisect(p, j):
    # peel p1 against p2,...,p_j sequentially (j-1 cuts), residual w,
    # then bisect w and possibly further pieces with remaining budget (assume total budget n=m-1)
    # returns Phi using j-1 + 1 = j cuts (bisect w as final cut), leaving rest of tail untouched
    m = len(p)
    w = p[0]
    peeled = []
    for i in range(1, j):
        peeled.append(p[i])
        w -= p[i]
    vals = []
    for x in peeled:
        vals += [x, x]  # untouched originals cancel with peeled fragment... 
    vals += [w/2, w/2]
    vals += p[j:]
    return Phi_of_multiset(vals)

def brute_min_phi(p, n, trials=4000, seed=0):
    # crude float-based local search fallback using random compositions & random split points, 
    # but let's do exact random rational splits to at least sample.
    import random as rnd
    rnd.seed(seed)
    m = len(p)
    best = sum(p)  # do nothing upper bound
    # random compositions: choose which pieces get how many cuts, sum<=n
    for _ in range(trials):
        cuts_left = n
        comp = [0]*m
        idxs = list(range(m))
        rnd.shuffle(idxs)
        for i in idxs:
            if cuts_left<=0: break
            c = rnd.randint(0, cuts_left)
            comp[i] = c
            cuts_left -= c
        vals = []
        for i in range(m):
            c = comp[i]
            if c==0:
                vals.append(p[i])
            else:
                # random split into c+1 positive parts summing to p[i], using random Dirichlet-like via random Fractions
                parts = c+1
                cuts = sorted(F(rnd.randint(1,10000), 10000) for _ in range(parts-1))
                prev = F(0)
                segs = []
                for cpt in cuts:
                    segs.append(cpt-prev)
                    prev = cpt
                segs.append(F(1)-prev)
                vals += [p[i]*s for s in segs]
        val = Phi_of_multiset(vals)
        if val < best:
            best = val
    return best

def an(n):
    Dn = 2**(n+1)-1
    return F(2**n, Dn)

def Dn(n):
    return 2**(n+1)-1

random.seed(1)

def rand_case_b2(n, tries=2000):
    m = n+1
    a_n = an(n)
    D_n = Dn(n)
    for _ in range(tries):
        # random p1 < T/2, p2 in (T/Dn, an*T/2)
        T = F(1)
        p1 = F(random.randint(1,49),100)  # <0.5
        lo = F(1,D_n)
        hi = a_n/2
        if lo>=hi: continue
        # sample p2 in (lo,hi) and p2<=p1
        hi2 = min(hi, p1)
        if lo>=hi2: continue
        p2 = F(random.randint(int(lo*1000)+1, int(hi2*1000)-1),1000)
        if not (lo<p2<hi and p2<=p1): continue
        rest = T - p1 - p2
        if rest<=0: continue
        # generate p3..pm sorted descending summing to rest, each <=p2
        k = m-2
        if k==0:
            if rest!=0: continue
            tail = []
        else:
            # random composition
            cuts = sorted(F(random.randint(1,999),1000)*rest for _ in range(k-1)) if k>1 else []
            prev=F(0); segs=[]
            for c in cuts:
                segs.append(c-prev); prev=c
            segs.append(rest-prev)
            tail = sorted(segs, reverse=True)
            if any(t<=0 for t in tail): continue
            if tail[0] > p2: continue
        p = [p1,p2]+tail
        if p != sorted(p, reverse=True): continue
        yield p

for n in [3,4,5]:
    print("=== n =", n, "a_n =", an(n), float(an(n)))
    count=0
    best_margin = None
    for p in rand_case_b2(n, tries=3000):
        count+=1
        if count>15: break
        T=sum(p)
        target = an(n)*T
        # compute several candidate strategies
        cands = []
        for k in range(0, n+1):
            cands.append(bisect_topk(p,k))
        for j in range(2, len(p)):
            cands.append(peel_then_bisect(p,j))
        best_construct = min(cands)
        bruteval = brute_min_phi(p, n, trials=1500, seed=count)
        trueish = min(best_construct, bruteval)
        margin = target - trueish
        print(f"  p={[float(x) for x in p]} target={float(target):.4f} bisectk_best={float(best_construct):.4f} brute={float(bruteval):.4f} margin~{float(margin):.4f}")
