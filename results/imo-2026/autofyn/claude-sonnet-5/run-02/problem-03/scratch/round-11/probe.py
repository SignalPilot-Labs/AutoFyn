from fractions import Fraction as F
import random, itertools

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

def A(multiset):
    # A(S) = sum over odd sorted rank (1-indexed) with alternating sign
    S = sorted(multiset, reverse=True)
    total = F(0)
    for i,v in enumerate(S):
        total += v if i%2==0 else -v
    return total

def f(n):
    return F(1, 2**(n+1)-1)

# random legal refinement generator: given a list of piece "slots" (pieces of tail),
# and a budget of cuts, randomly split some pieces (each cut only within one piece, at random rational point)
def random_refine(pieces, cuts_budget):
    pieces = list(pieces)
    cuts_used = 0
    # randomly decide how many cuts to use <= budget
    k = random.randint(0, cuts_budget)
    for _ in range(k):
        if not pieces: break
        idx = random.randrange(len(pieces))
        p = pieces.pop(idx)
        # random rational split point
        num = random.randint(1, 999)
        x = F(num,1000)*p
        y = p-x
        if x>0: pieces.append(x)
        if y>0: pieces.append(y)
    return pieces

random.seed(0)

for n in [3,4,5,6]:
    p = ladder(n)
    p1 = p[0]; p2=p[1]; p3=p[2] if n>=3 else None
    tail = p[1:]  # p2..p_{n+1}
    s = sum(p[2:])  # total of p3..
    fn = f(n)
    # Check v<s branch: F={v}, P empty (c=1 asymmetric... but ell(F)=1 with v<s requires c>=2 cuts typically)
    # We'll just directly search over legal configurations with p2 untouched, F residual v in (0,s), G'=  {p2} U R'
    worst = None
    trials = 20000
    for _ in range(trials):
        # choose F: split p1 into ell=1 config with v in (0,s)
        # simplest: pick v random in (0,s), then P = pairs summing to p1-v, using leftover multiplicities;
        # need at least c>=2 cuts -> use v + one pair (t,t) with 2t = p1-v
        v = F(random.randint(1,999),1000)*s
        t = (p1-v)/2
        if t<=0: continue
        Fset = [v,t,t]
        R_budget = n-2
        Rprime = random_refine([p[2+i] for i in range(len(p)-2)], R_budget)  # refine p3..
        Gset = [p2]+Rprime
        S = Fset+Gset
        val = A(S)
        if worst is None or val<worst:
            worst = val
    print(n, "v<s branch worst A found:", worst, "fn=",fn, "worst-fn=",worst-fn)
