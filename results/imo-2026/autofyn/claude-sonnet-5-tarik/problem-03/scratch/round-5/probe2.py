import itertools, random
from fractions import Fraction as F

def e_of(sorted_desc):
    s=0; sign=1
    for x in sorted_desc:
        s+=sign*x; sign*=-1
    return s

def one_shot_optimal(A, m):
    n=len(A)
    best=[None]
    def rec(remaining_idx, produced, budget):
        M = [A[i] for i in remaining_idx]+produced
        M = tuple(sorted(M, reverse=True))
        val = e_of(M)
        if best[0] is None or val<best[0]:
            best[0]=val
        if budget==0 or len(remaining_idx)==0:
            return
        rem=list(remaining_idx)
        for i in rem:
            rec([x for x in rem if x!=i], produced, budget-1)
        for a in range(len(rem)):
            for b in range(len(rem)):
                if a==b: continue
                i,j=rem[a],rem[b]
                x,y=A[i],A[j]
                if x<y: continue
                rec([k for k in rem if k!=i and k!=j], produced+[x-y], budget-1)
    rec(tuple(range(n)), [], m)
    return best[0]

def target(m):
    return F(1, 2**(m+1)-1)

random.seed(7)
def rand_case2(k, denom=40):
    while True:
        vals = sorted([random.randint(1,denom) for _ in range(k)], reverse=True)
        if vals[-1]==0: continue
        Afull=[F(v) for v in vals]
        a1,a2=Afull[0],Afull[1]
        if a1 < 2*a2:
            return tuple(Afull)

fails=0
total=0
worst_margin = None
for m in [2,3,4]:
    k=m+1
    trials = 60 if m<=3 else 25
    tgt = target(m)
    for t in range(trials):
        A = rand_case2(k, denom=30)
        S = sum(A)
        val = one_shot_optimal(A,m)
        bound = tgt*S
        total+=1
        margin = bound-val
        if margin<0:
            fails+=1
            print("FAIL m=",m,"A=",A,"S=",S,"oneshot=",val,float(val),"target_bound=",float(bound))
        if worst_margin is None or margin<worst_margin[0]:
            worst_margin=(margin,m,A,val,bound)

print("total",total,"fails",fails)
print("worst margin:", worst_margin[0], float(worst_margin[0]), "at m=",worst_margin[1],"A=",worst_margin[2])

# Test the known hard counterexamples from round 3/4 files
from fractions import Fraction as F
A1 = (F(239,500), F(112,500), F(75,500), F(74,500))
m=3
val = one_shot_optimal(A1, m)
tgt = target(m)*sum(A1)
print("A1 one-shot:", val, float(val), "target:", float(tgt), "PASS" if val<=tgt else "FAIL")

A2 = (F(1,2), F(333,1000), F(167,1000))
m=2
val2 = one_shot_optimal(A2, m)
tgt2 = target(m)*sum(A2)
print("A2 one-shot:", val2, float(val2), "target:", float(tgt2), "PASS" if val2<=tgt2 else "FAIL")
