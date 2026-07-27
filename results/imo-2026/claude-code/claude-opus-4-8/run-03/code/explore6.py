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
    # also return delta, gamma
    delta=ang(L,C,K); gamma=ang(L,B,K)
    return A,B,C,M,N,K,L,delta,gamma
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def Phi(X,A,B,C):
    P=(np.array(B)+np.array(C))/2
    num=np.dot(np.array(X)-P,np.array(X)-A)
    den=cross(np.array(C)-np.array(B),np.array(X)-np.array(A))
    return num/den

A0,B0,C0=(1,5),(0,0),(7,0)
for beta in [0.15,0.25,0.35,0.45,0.55]:
    A,B,C,M,N,K,L,delta,gamma=solve_valid(A0,B0,C0,beta)
    print(f"beta={beta:.2f} delta={np.degrees(delta):.3f} gamma={np.degrees(gamma):.3f}  Phi(K)={Phi(K,A,B,C):.5f} Phi(L)={Phi(L,A,B,C):.5f}")
