from fractions import Fraction as F
import random

def A(S):
    S = sorted(S, reverse=True)
    return sum((-1)**i * S[i] for i in range(len(S)))

def Phi(S):
    S=sorted(S,reverse=True)
    return sum(S[i] for i in range(0,len(S),2))

def E(S):
    # sum of even-rank (2nd,4th,...) elements
    S=sorted(S,reverse=True)
    return sum(S[i] for i in range(1,len(S),2))

random.seed(3)
mism=0
for trial in range(2000):
    k=random.randint(2,7)
    U=[F(random.randint(1,50),random.randint(1,50)) for _ in range(k)]
    if len(set(U))!=len(U): continue  # need strict unique max generally; just test
    m = max(U)
    Upp = [v for v in U if v!=m]
    if len(Upp) != len(U)-1: continue
    lhs = E(U)
    rhs = Phi(Upp)
    if lhs!=rhs:
        mism+=1
        print("mismatch",U,lhs,rhs)
print("done, mismatches:",mism)
