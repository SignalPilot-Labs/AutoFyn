import random
random.seed(7)

def chambers_all(p):
    p1,p2,p3,p4 = p
    def bisect_f(S):
        idx=[i for i in range(4) if i not in S]
        R=[p[i] for i in idx]
        A=sum((1 if k%2==0 else -1)*v for k,v in enumerate(R))
        return (1+A)/2
    import itertools
    out=[]
    for r in range(4):
        for S in itertools.combinations(range(4), r):
            out.append((f"bisect{S}", True, bisect_f(set(S))))
    out.append(("DS-Below", (p3+p4/2<p1) and (p1<p2+p3), p2+p3+p4/2))
    out.append(("DS-Above", p1>p2+p3, p1+p4/2))
    out.append(("TriplePin", p1>p2+p3, 1-p1))
    out.append(("B1", (p2+p3-p4<p1) and (p1<p2+p3), p1+p4))
    out.append(("B2", (p2<=p1) and (p1<p2+p3-p4), p2+p3))
    out.append(("P1P2p3", p2>=2*p3, p1+p3))
    out.append(("R22.1.1", (p1>=2*p3) and (p2<=p3+p4), p1/2+p3+p4))
    out.append(("A", (p1>=3*p4) and (p1<=2*p3+p4), p2+(p1+p4)/2))
    out.append(("A2", p1<=p2+2*p4, (p1+p2)/2+p3))
    return out

a3=8/15
pts=[]
trials=150000
for _ in range(trials):
    p1 = random.uniform(0.0001, 0.4999)
    p2 = random.uniform(1/15+1e-6, min(p1, 4/15-1e-6))
    if p2<=0: continue
    rem=1-p1-p2
    if rem<=0: continue
    p3=random.uniform(1e-5, rem)
    p4=rem-p3
    if not (p1>=p2>=p3>=p4>0): continue
    pts.append((p1,p2,p3,p4))
print("num pts", len(pts))

names = [c[0] for c in chambers_all(pts[0])]
winners_list = []
for p in pts:
    w = set(name for name,feas,phi in chambers_all(p) if feas and (a3-phi)>=-1e-12)
    winners_list.append(w)

remaining=set(range(len(pts)))
chosen=[]
while remaining:
    best=None; bc=-1
    for name in names:
        c = sum(1 for i in remaining if name in winners_list[i])
        if c>bc: bc=c; best=name
    if bc==0: break
    chosen.append((best,bc))
    remaining={i for i in remaining if best not in winners_list[i]}
print("greedy family:", chosen, "uncovered_left:", len(remaining))
