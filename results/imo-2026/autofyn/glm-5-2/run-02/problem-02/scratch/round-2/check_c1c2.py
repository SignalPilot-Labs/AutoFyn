"""
Verify the (C1),(C2) sign correction and the antipode (T') numerical residual
on a few configs, plus power-secant sign fix numerically.
"""
import numpy as np
from scipy.optimize import least_squares

def ord_angle(p,q):
    cr=p[0]*q[1]-p[1]*q[0]; dt=p[0]*q[0]+p[1]*q[1]
    return np.arctan2(abs(cr),dt)

# generate configs satisfying the 3 ordinary angle equalities + inside
def residual(X, Bn, Cn, lyfix):
    kxv,kyv,lxv=X; lyv=lyfix
    K=(kxv,kyv); L=(lxv,lyv); A=(0.0,0.0)
    Mn=(Bn[0]/2,0.0); Nn=(Cn[0]/2,Cn[1]/2)
    a1=ord_angle((K[0]-Bn[0],K[1]-Bn[1]),(A[0]-Bn[0],A[1]-Bn[1]))-ord_angle((A[0]-Cn[0],A[1]-Cn[1]),(L[0]-Cn[0],L[1]-Cn[1]))
    a2=ord_angle((L[0]-Bn[0],L[1]-Bn[1]),(K[0]-Bn[0],K[1]-Bn[1]))-ord_angle((L[0]-Nn[0],L[1]-Nn[1]),(Cn[0]-Nn[0],Cn[1]-Nn[1]))
    a3=ord_angle((L[0]-Cn[0],L[1]-Cn[1]),(K[0]-Cn[0],K[1]-Cn[1]))-ord_angle((Bn[0]-Mn[0],Bn[1]-Mn[1]),(K[0]-Mn[0],K[1]-Mn[1]))
    return [a1,a2,a3]

def in_tri(P,V1,V2,V3):
    def s(p,q,r): return (p[0]-r[0])*(q[1]-r[1])-(q[0]-r[0])*(p[1]-r[1])
    d1=s(P,V1,V2);d2=s(P,V2,V3);d3=s(P,V3,V1)
    neg=(d1<0)|(d2<0)|(d3<0); pos=(d1>0)|(d1>0)|(d3>0)
    return not(neg and pos)

rng=np.random.default_rng(3)
configs=[]
for _ in range(5000):
    bn=float(rng.uniform(3,7)); un=float(rng.uniform(-2,4)); vn=float(rng.uniform(3,6))
    Bn=(bn,0); Cn=(un,vn); Mn=(bn/2,0); Nn=(un/2,vn/2)
    lyfix=float(rng.uniform(0.3, vn-0.3))
    x0=[bn*0.55, rng.uniform(0.2,vn*0.4), un*0.5]
    res=least_squares(residual,x0,args=(Bn,Cn,lyfix),xtol=1e-15,ftol=1e-15)
    if res.cost>1e-22: continue
    kxv,kyv,lxv=res.x; K=(kxv,kyv); L=(lxv,lyfix)
    if not(in_tri(K,Bn,Mn,Cn) and in_tri(L,Bn,Nn,Cn)): continue
    configs.append((bn,un,vn,K,L))
    if len(configs)>=10: break

print(f"Found {len(configs)} configs.")
# Check (C1): 2 sin A sin(C-a-g) sin(a+g) = sin C sin g sin(A+2a+g)
# and the round-1 WRONG version sin(a+g-C)
import math
maxC1_corr=0; maxC1_wrong=0; maxC2_corr=0; maxC2_wrong=0
for cfg in configs:
    bn,un,vn,K,L=cfg
    A_=math.atan2(vn,un)  # angle A? No. A=(0,0), B=(bn,0), C=(un,vn).
    # angle A = angle BAC = angle between AB and AC
    AB=(bn,0); AC=(un,vn)
    A_ang=ord_angle(AB,AC)
    # angle B = angle ABC between BA=(-bn,0) and BC=(un-bn,vn)
    BA=(-bn,0); BC=(un-bn,vn)
    B_ang=ord_angle(BA,BC)
    C_ang=math.pi-A_ang-B_ang
    # alpha, beta, gamma
    Bpt=(bn,0); Cpt=(un,vn); Apt=(0,0); Mpt=(bn/2,0); Npt=(un/2,vn/2)
    BK=(K[0]-bn,K[1]-0); BA2=(-bn,0)
    alpha=ord_angle(BK,BA2)
    BL=(L[0]-bn,L[1]-0); NL=(L[0]-un/2,L[1]-vn/2); NC=(un/2,vn/2)
    beta=ord_angle(BL,BK)
    CL3=(L[0]-un,L[1]-vn); CK=(K[0]-un,K[1]-vn); MB=(bn/2,0); MK=(K[0]-bn/2,K[1])
    gamma=ord_angle(CL3,CK)
    # (C1) corrected
    lhs=2*math.sin(A_ang)*math.sin(C_ang-alpha-gamma)*math.sin(alpha+gamma)
    rhs=math.sin(C_ang)*math.sin(gamma)*math.sin(A_ang+2*alpha+gamma)
    maxC1_corr=max(maxC1_corr,abs(lhs-rhs))
    # wrong
    lhs_w=2*math.sin(A_ang)*math.sin(alpha+gamma-C_ang)*math.sin(alpha+gamma)
    maxC1_wrong=max(maxC1_wrong,abs(lhs_w-rhs))
    # (C2) corrected
    lhs2=2*math.sin(A_ang)*math.sin(B_ang-alpha-beta)*math.sin(alpha+beta)
    rhs2=math.sin(B_ang)*math.sin(beta)*math.sin(A_ang+2*alpha+beta)
    maxC2_corr=max(maxC2_corr,abs(lhs2-rhs2))
    lhs2_w=2*math.sin(A_ang)*math.sin(alpha+beta-B_ang)*math.sin(alpha+beta)
    maxC2_wrong=max(maxC2_wrong,abs(lhs2_w-rhs2))
print(f"(C1) corrected max resid: {maxC1_corr:.2e}; wrong (round-1) max resid: {maxC1_wrong:.2e}")
print(f"(C2) corrected max resid: {maxC2_corr:.2e}; wrong (round-1) max resid: {maxC2_wrong:.2e}")
