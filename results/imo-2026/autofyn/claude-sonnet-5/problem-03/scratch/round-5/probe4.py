from fractions import Fraction as F

def e_of(sorted_desc):
    s=0; sign=1
    for x in sorted_desc:
        s+=sign*x; sign*=-1
    return s

def one_shot_optimal_trace(A, m):
    n=len(A)
    best=[None]
    def rec(remaining_idx, produced, budget, actions):
        M = [A[i] for i in remaining_idx]+produced
        Msorted = tuple(sorted(M, reverse=True))
        val = e_of(Msorted)
        if best[0] is None or val<best[0][0]:
            best[0]=(val, list(actions))
        if budget==0 or len(remaining_idx)==0:
            return
        rem=list(remaining_idx)
        for i in rem:
            rec([x for x in rem if x!=i], produced, budget-1, actions+[('D',i)])
        for a in range(len(rem)):
            for b in range(len(rem)):
                if a==b: continue
                i,j=rem[a],rem[b]
                x,y=A[i],A[j]
                if x<y: continue
                rec([k for k in rem if k!=i and k!=j], produced+[x-y], budget-1, actions+[('M',i,j)])
    rec(tuple(range(n)), [], m, [])
    return best[0]

A1 = (F(239,500), F(112,500), F(75,500), F(74,500))
print("A1 (m=3):", one_shot_optimal_trace(A1,3))

A2 = (F(1,2), F(333,1000), F(167,1000))
print("A2 (m=2):", one_shot_optimal_trace(A2,2))

# a random m=4 case
import random
random.seed(3)
def rand_case2(k, denom=30):
    while True:
        vals = sorted([random.randint(1,denom) for _ in range(k)], reverse=True)
        if vals[-1]==0: continue
        Afull=[F(v) for v in vals]
        if Afull[0] < 2*Afull[1]:
            return tuple(Afull)
for _ in range(4):
    A = rand_case2(5, 25)
    print(A, "->", one_shot_optimal_trace(A,4))
