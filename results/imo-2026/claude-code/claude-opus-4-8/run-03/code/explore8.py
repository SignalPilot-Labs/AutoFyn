import numpy as np
from scipy.optimize import fsolve
def ang(P,Q,R):
    u=np.array(P)-np.array(Q);v=np.array(R)-np.array(Q)
    c=np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v));c=max(-1,min(1,c));return np.degrees(np.arccos(c))
def rot(v,t):
    c,s=np.cos(t),np.sin(t);return np.array([c*v[0]-s*v[1],s*v[0]+c*v[1]])
def solve_valid(A,B,C,beta):
    A=np.array(A,float);B=np.array(B,float);C=np.array(C,float)
    M=(A+B)/2;N=(A+C)/2
    dK=rot((A-B)/np.linalg.norm(A-B),-beta);dL=rot((A-C)/np.linalg.norm(A-C),+beta)
    def eqs(x):
        s,u=x;K=B+s*dK;L=C+u*dL
        return [ang(L,B,K)-ang(L,N,C),ang(L,C,K)-ang(B,M,K)]
    sol=fsolve(eqs,(1.0,3.0));K=B+sol[0]*dK;L=C+sol[1]*dL
    return A,B,C,M,N,K,L

for beta in [0.2,0.35,0.5]:
    A,B,C,M,N,K,L=solve_valid((1,5),(0,0),(7,0),beta)
    print(f"beta={beta}")
    print(f"  BAK={ang(B,A,K):.4f} CAL={ang(C,A,L):.4f}  (isogonal in A?)")
    print(f"  BAL={ang(B,A,L):.4f} CAK={ang(C,A,K):.4f}")
    print(f"  BAK+CAL={ang(B,A,K)+ang(C,A,L):.4f}  BAC={ang(B,A,C):.4f}")
    # angle AKB, AKC
    print(f"  AKB={ang(A,K,B):.4f} AKC={ang(A,K,C):.4f}  ALB={ang(A,L,B):.4f} ALC={ang(A,L,C):.4f}")
