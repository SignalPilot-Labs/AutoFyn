import random
random.seed(123)

def bisect_f(p,S):
    idx=[i for i in range(4) if i not in S]
    R=[p[i] for i in idx]
    A=sum((1 if k%2==0 else -1)*v for k,v in enumerate(R))
    return (1+A)/2

def chambers5(p):
    p1,p2,p3,p4=p
    out=[]
    out.append(("bisect14", True, bisect_f(p,{0,3})))
    out.append(("bisect12", True, bisect_f(p,{0,1})))
    out.append(("DS-Above", p1>p2+p3, p1+p4/2))
    out.append(("R22.1.1", (p1>=2*p3) and (p2<=p3+p4), p1/2+p3+p4))
    out.append(("TriplePin", p1>p2+p3, 1-p1))
    return out

a3=8/15
uncov=0
trials=1000000
worst=[]
for _ in range(trials):
    p1 = random.uniform(0.0001, 0.4999)
    p2 = random.uniform(1/15+1e-6, min(p1, 4/15-1e-6))
    if p2<=0: continue
    rem=1-p1-p2
    if rem<=0: continue
    p3=random.uniform(1e-5, rem)
    p4=rem-p3
    if not (p1>=p2>=p3>=p4>0): continue
    p=(p1,p2,p3,p4)
    winners=[name for name,feas,phi in chambers5(p) if feas and (a3-phi)>=-1e-12]
    if not winners:
        uncov+=1
        worst.append(p)
print("trials", trials, "uncovered(5-chamber family):", uncov)
for p in worst[:10]:
    print(p)
