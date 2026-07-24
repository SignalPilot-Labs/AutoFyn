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
        v = total_mass * fr
        out.extend([v, v])
    return out

random.seed(2)
n=4
pieces, D = ladder(n)
p1 = pieces[0]
tail = pieces[2:]
fn = F(1, D)
worst=None; worst_info=None
for _ in range(6000):
    num_pairs = random.randint(0,2)
    cuts_on_F = (3 + 2*num_pairs) - 1
    remaining = n - cuts_on_F
    if remaining < 0: continue
    a = F(random.randint(1,999),1000)
    b = F(random.randint(1,999),1000)*a
    c = F(random.randint(1,999),1000)*b
    s = a+b+c
    if s<=0: continue
    scale = F(random.randint(1,95),100) * p1 / s
    v1,v2,v3 = a*scale,b*scale,c*scale
    rem = p1-(v1+v2+v3)
    if rem <= 0: continue
    if num_pairs==0:
        continue
    P = exact_pair_set(rem, num_pairs)
    cuts = random.randint(0, remaining)
    Rp = random_refinement(tail, cuts)
    S = [v1,v2,v3] + P + Rp
    val = A(S)
    if worst is None or val<worst:
        worst=val
        worst_info=(v1,v2,v3,P,Rp,num_pairs,cuts,remaining)

v1,v2,v3,P,Rp,num_pairs,cuts,remaining = worst_info
print("n=",n,"p1=",p1,"tail=",tail)
print("v1,v2,v3=",v1,v2,v3, "sum=",v1+v2+v3)
print("P=",P,"sum(P)=",sum(P))
print("total F =", v1+v2+v3+sum(P), "should equal p1=",p1)
print("Rp=",Rp,"sum=",sum(Rp),"should equal sum(tail)=",sum(tail))
print("num_pairs=",num_pairs,"cuts on F used=",1+2*num_pairs,"remaining budget=",remaining,"cuts used in tail=",cuts)
print("total cuts = F_cuts + tail_cuts =", (1+2*num_pairs)+cuts, " must be <= n =",n)
print("A(S) =", float(worst), " f(n)=",float(fn), "slack=", float(worst-fn))
print("Full multiset S sorted:", sorted([v1,v2,v3]+P+Rp, reverse=True))
