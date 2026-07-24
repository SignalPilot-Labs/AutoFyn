from fractions import Fraction as F
import random

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = F(0); sign=1
    for x in s:
        total += sign*x; sign=-sign
    return total

def greedy_peel_full(pieces):
    W = list(pieces)
    M = []  # finalized real physical pieces
    cuts = 0
    while len(W) >= 2:
        idxs = sorted(range(len(W)), key=lambda i: -W[i])
        i,j = idxs[0], idxs[1]
        a,b = W[i], W[j]
        rest = [W[k] for k in range(len(W)) if k not in (i,j)]
        if a == b:
            M.append(a); M.append(b)
            W = rest
        else:
            # cut a into b_frag=b and a-b; original b finalized, b_frag finalized, a-b re-enters
            M.append(b)      # original b, finalized
            M.append(b)      # new fragment equal to b, finalized
            W = rest + [a-b]
            cuts += 1
    if len(W)==1:
        vfinal = W[0]
        M.append(vfinal)
    else:
        vfinal = F(0)
    return M, vfinal, cuts

random.seed(2024)
viol_identity = 0
viol_corollary = 0
tot = 0
for n in range(1,7):
    m = n+1
    for _ in range(400):
        cuts_pts = sorted(random.sample(range(1,10000), m-1))
        prev=0; pieces=[]
        for c in cuts_pts:
            pieces.append(F(c-prev,10000)); prev=c
        pieces.append(F(10000-prev,10000))
        M, vfinal, c = greedy_peel_full(pieces)
        tot += 1
        AM = A(M)
        if AM != vfinal:
            viol_identity += 1
            print("IDENTITY MISMATCH", n, pieces, AM, vfinal)
        if c < n and vfinal > 0:
            # bisect vfinal in M
            Mp = [x for x in M if x != vfinal] # remove one occurrence -- careful with duplicates
            # remove exactly one occurrence of vfinal
            Mp = list(M)
            Mp.remove(vfinal)
            Mp.append(vfinal/2)
            Mp.append(vfinal/2)
            Aprime = A(Mp)
            an = F(2**n, 2**(n+1)-1)
            T = sum(pieces)
            Phi_prime = (T + Aprime)/2
            if Aprime != 0 or Phi_prime >= an*T:
                viol_corollary += 1
                print("COROLLARY VIOLATION", n, Aprime, Phi_prime, an*T)

print("trials:", tot, "identity mismatches:", viol_identity, "corollary violations:", viol_corollary)
