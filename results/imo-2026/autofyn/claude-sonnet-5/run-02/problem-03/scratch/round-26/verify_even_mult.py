from fractions import Fraction as Fr
import random

def f(n):
    return Fr(1, 2**(n+1)-1)

def ladder(n):
    fn = f(n)
    return [2**(n+1-i)*fn for i in range(1, n+2)]

def A(S):
    S = sorted(S, reverse=True)
    total = Fr(0); sign=1
    for x in S:
        total += sign*x; sign*=-1
    return total

def random_legal_refinement_with_forced_tie(pieces, max_cuts):
    frags = list(pieces)
    cuts = random.randint(1, max_cuts)
    for _ in range(cuts):
        idx = random.randrange(len(frags))
        v = frags[idx]
        if v <= 0: continue
        r = Fr(random.randint(1,999),1000)
        a=v*r; b=v-a
        frags[idx]=a; frags.append(b)
    return frags

random.seed(3)
violations=0
trials=0
minAB=None
for n in range(5,9):
    p=ladder(n); p4=p[3]; tail=p[4:]; fn=f(n)
    for trial in range(20000):
        Tpp = random_legal_refinement_with_forced_tie(tail, n-4)
        if not Tpp: continue
        idx = random.randrange(len(Tpp))
        tstar = Tpp[idx]
        mult = sum(1 for x in Tpp if x==tstar)
        if mult%2!=0: continue  # only even-multiplicity (including possibly artificially forced ties by duplicating)
        trials+=1
        B=[tstar,p4]+Tpp
        AB=A(B)
        if minAB is None or AB<minAB:
            minAB=AB; minn=n
        if AB < fn - Fr(1,10**9):
            violations+=1
print("even-mult trials:",trials,"violations:",violations)
print("min AB observed:", minAB, float(minAB) if minAB else None, "at n=",minn if trials else None)
