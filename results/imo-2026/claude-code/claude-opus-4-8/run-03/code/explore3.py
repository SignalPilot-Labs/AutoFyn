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
def dist(P,Q):return np.linalg.norm(np.array(P)-np.array(Q))

A,B,C,M,N,K,L=solve_valid((1,5),(0,0),(7,0),0.35)
print("Given angle conditions check:")
print(" KBA=",ang(K,B,A)," ACL=",ang(A,C,L))
print(" LBK=",ang(L,B,K)," LNC=",ang(L,N,C))
print(" LCK=",ang(L,C,K)," BMK=",ang(B,M,K))
print()
# Test spiral similarity triangle BLK ~ NLC (center L): compare angles
print("Test T(B,L,K) vs T(N,L,C):")
print(" angle at L: KLB=",ang(K,L,B)," CLN=",ang(C,L,N))
print(" angle at B/N: LBK=",ang(L,B,K)," LNC=",ang(L,N,C))
print(" angle at K/C: BKL=",ang(B,K,L)," NCL=",ang(N,C,L))
print(" side ratios LB/LN=",dist(L,B)/dist(L,N)," LK/LC=",dist(L,K)/dist(L,C)," BK/NC=",dist(B,K)/dist(N,C))
print()
print("Test T(C,K,L) vs T(M,K,B) (center K):")
print(" angle at K: LKC=",ang(L,K,C)," BKM=",ang(B,K,M))
print(" angle at C/M: LCK=",ang(L,C,K)," BMK=",ang(B,M,K))
print(" angle at L/B: KLC=",ang(K,L,C)," KBM=",ang(K,B,M))
print(" ratios KC/KM=",dist(K,C)/dist(K,M)," KL/KB=",dist(K,L)/dist(K,B)," CL/MB=",dist(C,L)/dist(M,B))
