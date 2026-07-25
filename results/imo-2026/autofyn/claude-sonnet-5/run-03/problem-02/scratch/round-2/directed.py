import numpy as np
from scipy.optimize import fsolve

A = np.array([0.3, 2.7]); B = np.array([-1.5, 0.0]); C = np.array([2.2, 0.1])
M = (A+B)/2; N = (A+C)/2

def ang(P,Q,R):
    u=Q-P; v=R-P
    return np.arccos(np.clip(np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v)),-1,1))

def rot(v,theta):
    c,s=np.cos(theta),np.sin(theta)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])

def K_of(theta,rK):
    d=(A-B)/np.linalg.norm(A-B); return B+rK*rot(d,-theta)
def L_of(theta,rL):
    d=(A-C)/np.linalg.norm(A-C); return C+rL*rot(d,theta)

def resid(x,theta):
    rK,rL=x; K=K_of(theta,rK); L=L_of(theta,rL)
    return [ang(B,L,K)-ang(N,L,C), ang(C,L,K)-ang(M,B,K)]

def dirang(P1,P2,P3,P4):
    # directed angle mod pi from line P1P2 to line P3P4
    v1 = P2-P1; v2 = P4-P3
    a1 = np.arctan2(v1[1],v1[0])
    a2 = np.arctan2(v2[1],v2[0])
    d = (a2-a1) % np.pi
    return d

family=[]
for theta_deg in np.linspace(5,60,120):
    theta=np.radians(theta_deg)
    for rK0 in [0.5,1.0,1.5]:
        for rL0 in [0.5,1.0,1.5]:
            sol,info,ier,msg = fsolve(resid,[rK0,rL0],args=(theta,),full_output=True)
            if ier==1 and sol[0]>0 and sol[1]>0:
                rK,rL=sol
                K=K_of(theta,rK); L=L_of(theta,rL)
                family.append((theta_deg,K,L)); break
        else: continue
        break

print("family size", len(family))

def Qpoint():
    b=B-A; c=C-A
    num=np.dot(c-b,c+b); den=2*np.dot(c-b,c-b)
    return A+(num/den)*(c-b)
Q=Qpoint()

# candidate directed-angle identities (mod pi) to test across family; report std of (lhs-rhs) mod pi
candidates = {
 "KB,KM vs LC,LN": lambda K,L: (dirang(K,B,K,M), dirang(L,C,L,N)),
 "KB,KA vs LC,LA": lambda K,L: (dirang(K,B,K,A), dirang(L,C,L,A)),
 "KM,KQ vs LN,LQ": lambda K,L: (dirang(K,M,K,Q), dirang(L,N,L,Q)),
 "KA,KQ vs LA,LQ": lambda K,L: (dirang(K,A,K,Q), dirang(L,A,L,Q)),
 "AK,AQ vs AL,AQ_sym": lambda K,L: (dirang(A,K,A,Q), dirang(A,L,A,Q)),
 "QK,QA vs LK,LA (target)": lambda K,L: (dirang(Q,K,Q,A), dirang(L,K,L,A)),
 "BK,BQ vs CL,CQ": lambda K,L: (dirang(B,K,B,Q), dirang(C,L,C,Q)),
 "MK,MQ vs NL,NQ": lambda K,L: (dirang(M,K,M,Q), dirang(N,L,N,Q)),
}

for name, f in candidates.items():
    diffs = []
    for theta_deg,K,L in family:
        lhs, rhs = f(K,L)
        d = (lhs-rhs) % np.pi
        d = min(d, np.pi-d)
        diffs.append(d)
    diffs = np.array(diffs)
    print(f"{name:35s} mean_gap={diffs.mean():.4f} std={diffs.std():.4f} min={diffs.min():.4f} max={diffs.max():.4f}")
