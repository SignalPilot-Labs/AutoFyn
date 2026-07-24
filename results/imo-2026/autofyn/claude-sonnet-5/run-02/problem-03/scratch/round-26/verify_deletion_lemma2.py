from fractions import Fraction as Fr
import random

def f(n):
    return Fr(1, 2**(n+1)-1)

def ladder(n):
    fn = f(n)
    return [2**(n+1-i)*fn for i in range(1, n+2)]

def A(S):
    S = sorted(S, reverse=True)
    total = Fr(0)
    sign = 1
    for x in S:
        total += sign*x
        sign *= -1
    return total

def random_legal_refinement(pieces, max_cuts):
    frags = list(pieces)
    cuts = random.randint(0, max_cuts)
    for _ in range(cuts):
        idx = random.randrange(len(frags))
        v = frags[idx]
        if v <= 0:
            continue
        r = Fr(random.randint(1,999),1000)
        a = v*r
        b = v-a
        frags[idx] = a
        frags.append(b)
    return frags

random.seed(2)
n=6
p = ladder(n); p4=p[3]; tail=p[4:]; fn=f(n)
for trial in range(8):
    Tpp = random_legal_refinement(tail, n-4)
    if not Tpp: continue
    idx = random.randrange(len(Tpp))
    tstar = Tpp[idx]
    mult = sum(1 for x in Tpp if x==tstar)
    if mult%2==0: continue
    B = [tstar, p4] + Tpp
    AB = A(B)
    bound = fn+tstar
    rest = list(Tpp); rest.remove(tstar)
    Arest = A(rest); Trest = sum(rest)
    print("AB=",AB," bound(f+t*)=",bound," p4-Arest=",p4-Arest," Arest=",Arest," Trest=",Trest, " p4-Trest+tstar=", p4-Trest+tstar)
