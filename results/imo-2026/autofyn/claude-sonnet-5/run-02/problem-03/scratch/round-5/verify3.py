from fractions import Fraction as F
import random

def A(S):
    S = sorted(S, reverse=True)
    return sum((-1)**i * S[i] for i in range(len(S)))

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

# n=2 ladder, F={p1}, split p2 at various points, check A unchanged
n=2
p1,p2,p3 = ladder(n)
base = A([p1,p2,p3])
print("base A:", base)
for num in range(1,100):
    f1 = F(num,100)*p2
    f2 = p2 - f1
    if f1 <= 0 or f2 <=0: continue
    if f1 < f2:
        f1,f2 = f2,f1
    newA = A([p1,f1,f2,p3])
    if newA != base:
        print("MISMATCH split p2 at", f1,f2, newA, base)
print("p2-split check done (should print nothing if all match)")

# --- Verify rank-pigeonhole-budget's F* construction, general n ---
def check_Fstar(n):
    p = ladder(n)  # p[0]=p1,...
    T = p[1:]  # p2..p_{n+1}
    Fstar = p[1:n] + [p[n], p[n]]  # p2..p_{n-1}... wait indices
    # F* = {p2,...,p_n, p_{n+1}, p_{n+1}}
    Fstar = p[1:n] + [p[n], p[n]]   # p[1]=p2 .. p[n-1]=p_n ; p[n]=p_{n+1}
    total = sum(Fstar)
    assert total == p[0], (total, p[0])
    An = A(Fstar + T)
    target = F(1, 2**(n+1)-1)
    return An, target

for n in range(2,9):
    An, target = check_Fstar(n)
    print(n, An, target, An==target)
