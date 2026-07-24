from fractions import Fraction as F
import random

def ladder(n):
    D = 2**(n+1) - 1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

def A(S):
    S = sorted(S, reverse=True)
    return sum((1 if i%2==0 else -1)*v for i,v in enumerate(S))

def random_partition_piece(total, num_cuts):
    if num_cuts==0:
        return [total]
    positions = sorted(random.sample(range(1,10000), num_cuts))
    bounds=[0]+positions+[10000]
    parts=[F(bounds[i+1]-bounds[i],10000)*total for i in range(len(bounds)-1)]
    parts[-1]+= total-sum(parts)
    return parts

def legal_refinement(pieces, total_cuts_budget):
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

random.seed(4)
viol=0
trials_per_n=8000
for n in range(3,7):
    p = ladder(n)
    p1,p2,p3 = p[0],p[1],p[2]
    fn = F(1, 2**(n+1)-1)
    lower_pieces = p[3:]  # p4,...,p_{n+1}
    s4 = sum(lower_pieces)
    for t in range(trials_per_n):
        num = random.randint(0,9999)
        wprime = p3 + F(num,10000)*(p2-p3)
        if wprime >= p2: continue
        rem = p2 - wprime
        if rem < 0: continue
        npairs = random.randint(0,3)
        pair_vals=[]
        if npairs>0:
            half = rem/2
            comp = random_partition_piece(half, npairs-1)
            for val in comp:
                pair_vals += [val, val]
        else:
            if rem != 0: continue
        # cuts used so far: for F2 = {wprime}+pairs, cuts = npairs*2 (splitting p2 into 1+2*npairs pieces)
        cuts_F2 = 2*npairs
        # R''' any legal refinement of lower_pieces, using arbitrary cuts (Prop25 imposes no cut-budget restriction)
        num_cuts_R = random.randint(0, 2*len(lower_pieces)+2)  # just try a range
        Rppp = legal_refinement(lower_pieces, num_cuts_R)
        Gprime = [wprime] + pair_vals + [p3] + Rppp
        assert sum(Gprime) == p2 + p3 + s4
        AG = A(Gprime)
        bound = p2 - fn
        if AG > bound + F(1,10**12):
            viol+=1
            if viol<=5:
                print("VIOLATION",n,wprime,AG,bound)
print("done violations:",viol)
