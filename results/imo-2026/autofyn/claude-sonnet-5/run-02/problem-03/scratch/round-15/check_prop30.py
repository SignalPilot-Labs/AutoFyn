from fractions import Fraction as F
import random

def A(multiset):
    s = sorted(multiset, reverse=True)
    total=F(0); sign=1
    for x in s:
        total+=sign*x; sign=-sign
    return total

def ladder(n):
    denom=2**(n+1)-1
    fn=F(1,denom)
    p=[F(2**(n+1-i),denom) for i in range(1,n+2)]
    return p, fn

def refine(multiset, cuts, rng):
    ms=list(multiset)
    for _ in range(cuts):
        idx=rng.randrange(len(ms))
        val=ms[idx]
        num=rng.randint(1,999)
        f1=val*F(num,1000); f2=val-f1
        if f1<=0 or f2<=0: continue
        ms[idx]=f1; ms.append(f2)
    return ms

def random_exact_pairing(total_target, rng, min_pairs=0, max_pairs=2):
    if total_target==0:
        return []
    npairs=rng.randint(1,max_pairs)
    parts=[]; remaining=total_target
    for i in range(npairs-1):
        num=rng.randint(1,999)
        part=remaining*F(num,1000)/(npairs-i)
        parts.append(part); remaining-=part
    parts.append(remaining)
    P=[]
    for part in parts:
        half=part/2; P.append(half); P.append(half)
    return P

random.seed(99)
mismatches=0
mismatches_no_eps=0
trials=0
for n in range(3,7):
    p, fn = ladder(n)
    p1,p2,p3=p[0],p[1],p[2]
    s = sum(p[2:])  # Total({p3,...,p_{n+1}})
    assert p2 - s == fn
    tail_rest = p[2:]  # {p3,...,p_{n+1}}
    for trial in range(3000):
        rng=random
        cuts = rng.randint(0, max(n-2,0))
        Rp = refine(tail_rest, cuts, rng)
        assert sum(Rp)==s
        num = rng.randint(1,999)
        v = p2*F(num,1000)  # v in (0,p2), covers both v>=s and v<s
        if v<=0 or v>=p2: continue
        Gp = [p2]+Rp
        # need some F = {v} union P with ell(F)=1; P arbitrary exact pairing (not part of this check, use P=[])
        full_lhs = [v]+Gp
        lhs = A(full_lhs)
        R_gt_v = [r for r in Rp if r>v]
        eps = 1 if len(R_gt_v)%2==1 else 0
        A_R = A(Rp)
        A_Rgtv = A(R_gt_v)
        rhs = p2 - v + A_R - 2*A_Rgtv + 2*v*eps
        rhs_no_eps = p2 - v + A_R - 2*A_Rgtv
        trials+=1
        if lhs!=rhs:
            mismatches+=1
            if mismatches<=5:
                print("MISMATCH", n, v, lhs, rhs)
        if lhs!=rhs_no_eps:
            mismatches_no_eps+=1
print("trials",trials,"mismatches(with eps)",mismatches,"mismatches(without eps, i.e. naive)",mismatches_no_eps)
