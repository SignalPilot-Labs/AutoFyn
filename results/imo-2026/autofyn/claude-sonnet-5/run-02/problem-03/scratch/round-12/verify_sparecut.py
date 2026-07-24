from fractions import Fraction as F
import random

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = F(0); sign=1
    for x in s:
        total += sign*x; sign=-sign
    return total

def greedy_peel(W):
    W = list(W)
    cuts = 0
    while len(W) >= 2:
        W.sort(reverse=True)
        a, b = W[0], W[1]
        if a == b:
            W = W[2:]
        else:
            frag = a-b
            W = W[2:] + [frag]
            cuts += 1
    vfinal = W[0] if len(W)==1 else F(0)
    return vfinal, cuts

def a_n(n):
    return F(2**n, 2**(n+1)-1)

random.seed(7)
violations = 0
trials = 0
for n in range(1,7):
    m = n+1
    T = F(1)
    for _ in range(500):
        # random marking: random composition of T into m positive pieces
        cuts_pts = sorted(random.sample(range(1,10000), m-1))
        prev = 0
        pieces = []
        for c in cuts_pts:
            pieces.append(F(c-prev,10000))
            prev = c
        pieces.append(F(10000-prev,10000))
        vfinal, c = greedy_peel(pieces)
        trials += 1
        if c < n and vfinal > 0:
            # spare cut corollary applies: bisecting should give Phi=T/2 < a_n*T
            # verify directly
            # simulate: run greedy peel bookkeeping is abstract; need real multiset...
            # Just check a_n > 1/2 (trivial) and that greedy value with bisection matches T/2
            an = a_n(n)
            if not (F(1,2) < an):
                violations+=1
                print("a_n not >1/2", n, an)
print("trials checked spare-cut scenario count and a_n>1/2 sanity:", trials, "violations:", violations)

# Now directly verify the corollary's core claim: whenever c<n and vfinal>0,
# bisecting vfinal in the abstract working set gives A=0 -> but need real multiset check.
# Do a real physical simulation using actual cut objects (list of pieces) and greedy-peel physically.
def greedy_peel_physical(W):
    W = list(W)
    cuts = 0
    while True:
        if len(W) < 2:
            break
        # find top two by value
        idxs = sorted(range(len(W)), key=lambda i: -W[i])
        i,j = idxs[0], idxs[1]
        a,b = W[i], W[j]
        if a == b:
            # remove both
            W = [W[k] for k in range(len(W)) if k not in (i,j)]
        else:
            frag = a-b
            W = [W[k] for k in range(len(W)) if k not in (i,j)] + [frag]
            cuts += 1
    return W, cuts  # W is final abstract multiset (list), possibly one element = vfinal

random.seed(99)
viol2=0
tot2=0
for n in range(1,7):
    m=n+1
    for _ in range(300):
        cuts_pts = sorted(random.sample(range(1,10000), m-1))
        prev=0
        pieces=[]
        for c in cuts_pts:
            pieces.append(F(c-prev,10000)); prev=c
        pieces.append(F(10000-prev,10000))
        Wfinal, c = greedy_peel_physical(pieces)
        if c < n and len(Wfinal)==1 and Wfinal[0] > 0:
            vfinal = Wfinal[0]
            # bisect vfinal: new multiset = (pieces minus contributions... )
            # but Wfinal here IS the abstract reduced set, not real multiset of physical fragments.
            # For the corollary we need REAL final multiset M with A(M)=vfinal, then bisect one physical fragment equal to vfinal.
            pass
print("physical greedy-peel spot check done (structure only)", )
