from fractions import Fraction as F
import random

def ladder(n):
    D = 2**(n+1) - 1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

def A(S):
    S = sorted(S, reverse=True)
    return sum((1 if i%2==0 else -1)*v for i,v in enumerate(S))

def random_partition_piece(total, num_cuts):
    # split a single piece of length `total` using exactly num_cuts random interior cuts
    if num_cuts==0:
        return [total]
    positions = sorted(random.sample(range(1,10000), num_cuts))
    bounds=[0]+positions+[10000]
    parts=[F(bounds[i+1]-bounds[i],10000)*total for i in range(len(bounds)-1)]
    parts[-1]+= total-sum(parts)
    return parts

def legal_refinement(pieces, total_cuts_budget):
    # distribute total_cuts_budget cuts arbitrarily among the pieces list (each piece cut independently)
    k = len(pieces)
    if k==0: return []
    cuts_alloc = [0]*k
    remaining = total_cuts_budget
    for i in range(k-1):
        c = random.randint(0, remaining)
        cuts_alloc[i]=c
        remaining-=c
    cuts_alloc[-1]=remaining
    out=[]
    for piece,c in zip(pieces,cuts_alloc):
        out += random_partition_piece(piece, c)
    return out

random.seed(3)
viol=0
trials_per_n = 8000
for n in (3,4):
    p = ladder(n)
    p1,p2,p3 = p[0],p[1],p[2]
    tail_pieces = p[2:]  # p3,...,p_{n+1} as individual pieces
    fn = F(1, 2**(n+1)-1)
    s = sum(tail_pieces)
    for t in range(trials_per_n):
        num = random.randint(0, 9999)
        v = s + F(num,10000)*(p2-s)
        if v >= p2: continue
        rem = p1 - v
        if rem <= 0: continue
        npairs = random.randint(1,2)
        half = rem/2
        comp = random_partition_piece(half, npairs-1) if npairs>=1 else [half]
        pair_vals=[]
        for val in comp:
            pair_vals += [val, val]
        actual_npairs = len(comp)
        cuts_F = 2*actual_npairs
        if cuts_F > n: continue
        tail_budget_cuts = n - cuts_F
        if tail_budget_cuts < 0: continue
        max_R_cuts = random.randint(0, tail_budget_cuts)  # actual cuts used, <= budget
        Rprime = legal_refinement(tail_pieces, max_R_cuts)
        Gprime = [p2] + Rprime
        Fset = [v] + pair_vals
        S = Fset + Gprime
        total_cuts = (len(Fset)-1) + (len(Gprime)-1)
        if total_cuts > n: continue
        assert sum(S)==1
        AS = A(S)
        if AS < fn - F(1,10**12):
            viol+=1
            if viol<=5:
                print("VIOLATION",n,v,AS,fn,Fset,Gprime)
print("done violations:",viol)
