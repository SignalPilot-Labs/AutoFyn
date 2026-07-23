import itertools, random
from fractions import Fraction as F

def e_of(sorted_desc):
    s=0
    sign=1
    for x in sorted_desc:
        s+= sign*x
        sign*=-1
    return s

def full_optimal(A, m):
    # A: tuple of Fractions, sorted desc not required
    best = [None]
    def rec(M, budget):
        M = tuple(sorted(M, reverse=True))
        val = e_of(M)
        if best[0] is None or val < best[0]:
            best[0] = val
        if budget==0 or len(M)==0:
            return
        n=len(M)
        # D moves
        for i in range(n):
            newM = M[:i]+M[i+1:]
            rec(newM, budget-1)
        # M moves (pairs)
        for i in range(n):
            for j in range(n):
                if i==j: continue
                x=M[i]; y=M[j]
                if x<y: continue
                newval = x-y
                rest = [M[k] for k in range(n) if k!=i and k!=j]
                newM = rest+[newval]
                rec(newM, budget-1)
    rec(A, m)
    return best[0]

def one_shot_optimal(A, m):
    # A: tuple of Fractions original, sorted desc
    n=len(A)
    idx=list(range(n))
    best=[None]
    def rec(remaining_idx, produced, budget):
        # remaining_idx: set of original indices untouched
        # produced: list of new values created by M ops (not touchable further)
        M = [A[i] for i in remaining_idx]+produced
        M = tuple(sorted(M, reverse=True))
        val = e_of(M)
        if best[0] is None or val<best[0]:
            best[0]=val
        if budget==0 or len(remaining_idx)==0:
            return
        rem=list(remaining_idx)
        # D on one original element
        for i in rem:
            rec([x for x in rem if x!=i], produced, budget-1)
        # M on pair of originals
        for a in range(len(rem)):
            for b in range(len(rem)):
                if a==b: continue
                i,j=rem[a],rem[b]
                x,y=A[i],A[j]
                if x<y: continue
                newprod = produced+[x-y]
                rec([k for k in rem if k!=i and k!=j], newprod, budget-1)
    rec(tuple(idx), [], m)
    return best[0]

random.seed(1)
def rand_case2(k, denom=1000):
    while True:
        vals = sorted([random.randint(1,denom) for _ in range(k)], reverse=True)
        if vals[-1]==0: continue
        s=sum(vals)
        A=[F(v,s) for v in vals]  # normalize sum=1, but keep integer ratios via fraction of ints/s... let's just use Fraction(v, sum_of_all) with denom scaled
        # ensure sum exactly 1: use Fraction(v,1) then normalize later, sum could be non-1 in reduced form - let's just keep raw ints, sum needn't be 1 for testing e-ratios
        Afull = [F(v) for v in vals]
        a1,a2=Afull[0],Afull[1]
        if a1 < 2*a2:  # Case (ii): no dominant piece
            return tuple(Afull)

trials = 12
for m in [2,3]:
    print(f"--- m={m} ---")
    for t in range(trials):
        k = m+1
        A = rand_case2(k, denom=30)
        full = full_optimal(A,m)
        oneshot = one_shot_optimal(A,m)
        S = sum(A)
        gap = oneshot - full
        print(f"A={A} S={S} full_opt={full}({float(full):.4f}) oneshot_opt={oneshot}({float(oneshot):.4f}) equal={full==oneshot}")
