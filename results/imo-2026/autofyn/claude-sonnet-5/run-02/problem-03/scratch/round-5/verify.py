from fractions import Fraction as F
import itertools, random

def A(S):
    S = sorted(S, reverse=True)
    return sum((-1)**i * S[i] for i in range(len(S)))

def Phi(S):
    S = sorted(S, reverse=True)
    return sum(S[i] for i in range(0,len(S),2))

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

# --- Verify greedy-halving-adversary Proposition 15 counterexample (n=2) ---
n=2
p = ladder(n)
p1,p2,p3 = p
print("ladder n=2:", p1,p2,p3)
F0 = [p1]
T = [p2,p3]
AF0T = A(F0+T)
print("A(F cup T) =", AF0T, "expect 3/7:", F(3,7))

f1 = F(1,10)
f2 = p3 - f1
print("f1,f2 =", f1, f2, "sum", f1+f2, "p3", p3)
newset = [p1,p2,f1,f2]
Anew = A(newset)
print("A after splitting p3:", Anew, "expect 12/35:", F(12,35))
