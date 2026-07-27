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
Aa=ang(B,A,C);Ba=ang(A,B,C);Ca=ang(A,C,B)
for beta in [0.2,0.35,0.5]:
    A_,B_,C_,M_,N,K,L=solve_valid(*tri,beta)
    mu=ang(B,A,K); nu=Aa-mu; delta=ang(B,M,K); eps=ang(A,C,K)
    star=2*np.sin(Ca)*np.sin(mu)*np.cos(beta+mu)*np.sin(Aa+beta)-np.sin(Aa)*np.sin(beta+mu)*np.sin(Ca-beta-mu)
    xi=Aa+beta-mu
    spade=np.sin(Ca)*(np.sin(xi)*np.sin(beta-mu)+2*np.sin(mu)*np.sin(beta)*np.cos(xi))-np.sin(Ba)*np.sin(beta+mu)**2
    # also check (diamond) directly: sinC sinbeta sin(A+beta+delta-mu) - sinB sin(beta+delta) sin(beta+mu)
    diamond=np.sin(Ca)*np.sin(beta)*np.sin(Aa+beta+delta-mu)-np.sin(Ba)*np.sin(beta+delta)*np.sin(beta+mu)
    print(f"beta={beta}: star={star:.3e}  spade={spade:.3e}  diamond={diamond:.3e}")
