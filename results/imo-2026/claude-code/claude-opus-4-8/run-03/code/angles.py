import numpy as np
from scipy.optimize import fsolve
def ang(P,Q,R):
    u=np.array(P)-np.array(Q);v=np.array(R)-np.array(Q)
    c=np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v));c=max(-1,min(1,c));return np.arccos(c)
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
tri=((1,5),(0,0),(7,0))
A,B,C=[np.array(x,float) for x in tri]
M=(A+B)/2
Aang=ang(B,A,C);Bang=ang(A,B,C);Cang=ang(A,C,B)
print(f"A={np.degrees(Aang):.3f} B={np.degrees(Bang):.3f} C={np.degrees(Cang):.3f}")
print(f"{'beta':>6} {'mu=BAK':>8} {'eps=ACK':>8} {'delta=BMK':>9} {'cotmu-cotbeta-2cotdel':>12} {'eps-beta-del':>10}")
for beta in [0.15,0.25,0.35,0.45,0.55]:
    A_,B_,C_,M_,N,K,L=solve_valid(*tri,beta)
    mu=ang(B,A,K);eps=ang(A,C,K);delta=ang(B,M,K)
    r1=1/np.tan(mu)-1/np.tan(beta)-2/np.tan(delta)
    print(f"{beta:>6} {np.degrees(mu):>8.3f} {np.degrees(eps):>8.3f} {np.degrees(delta):>9.3f} {r1:>12.2e} {np.degrees(eps-beta-delta):>10.2e}")
