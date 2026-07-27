import numpy as np
from scipy.optimize import fsolve
import itertools
def ang(P,Q,R):
    u=np.array(P)-np.array(Q);v=np.array(R)-np.array(Q)
    c=np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v));c=max(-1,min(1,c));return np.arccos(c)
def rot(v,t):
    c,s=np.cos(t),np.sin(t);return np.array([c*v[0]-s*v[1],s*v[0]+c*v[1]])
def circumcenter(P,Q,R):
    ax,ay=P;bx,by=Q;cx,cy=R
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux=((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy=((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])
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
def area(P,Q,R):return 0.5*((Q[0]-P[0])*(R[1]-P[1])-(R[0]-P[0])*(Q[1]-P[1]))
def cross(u,v):return u[0]*v[1]-u[1]*v[0]
def Phi(X,A,B,C):
    P=(np.array(B)+np.array(C))/2
    return np.dot(np.array(X)-P,np.array(X)-A)/cross(np.array(C)-np.array(B),np.array(X)-A)
def Psi(X,A,B,C):return 2*dist(X,A)**2+dist(X,B)**2+dist(X,C)**2-dist(A,B)**2-dist(A,C)**2
def Delta(X,A,B,C):return area(A,B,C)-area(B,X,C)
def concyc(pts):
    Mx=[[x*x+y*y,x,y,1] for (x,y) in pts]
    d=np.linalg.det(np.array(Mx))
    sc=np.mean([np.linalg.norm(p) for p in pts])**3+1
    return d/sc

A,B,C,M,N,K,L=solve_valid((1,5),(0,0),(7,0),0.35)
O=circumcenter(A,K,L);Astar=2*O-A;P=(B+C)/2
# verify formula
print("Phi(K)=",Phi(K,A,B,C)," -Psi/8Delta=",-Psi(K,A,B,C)/(8*Delta(K,A,B,C)))
print("Phi(L)=",Phi(L,A,B,C)," -Psi/8Delta=",-Psi(L,A,B,C)/(8*Delta(L,A,B,C)))
# concyclicity search tight
pts={'A':A,'B':B,'C':C,'M':M,'N':N,'K':K,'L':L,'O':O,'As':Astar,'P':P}
print("\nConcyclic 4-subsets |det/scale|<1e-3:")
for comb in itertools.combinations(pts,4):
    v=concyc([pts[c] for c in comb])
    if abs(v)<1e-3: print("  ",comb, f"{v:.2e}")
# specific angle relations
print("\nAngle checks:")
print(" is M,K,L,C concyclic? ", concyc([M,K,L,C]))
print(" is N,K,L,B concyclic? ", concyc([N,K,L,B]))
print(" ang(M,K,?) ...")
# test triangle similarity BMK ~ ? and CLK
print(" BMK angles:",[np.degrees(ang(B,M,K)),np.degrees(ang(M,K,B)),np.degrees(ang(K,B,M))])
print(" CLK angles:",[np.degrees(ang(C,L,K)),np.degrees(ang(L,K,C)),np.degrees(ang(K,C,L))])

print("\n--- DEBUG pieces for K ---")
num1=np.dot(K-A,K-P)  # KA·KP
print("KA·KP=",num1," Psi/4=",Psi(K,A,B,C)/4)
den1=cross(C-B,K-A)   # [BC, AK]  (AK = K-A)
print("[BC,K-A]=",den1," -2*Delta=",-2*Delta(K,A,B,C))
print("Delta(K)=area(ABC)-area(BKC)=",Delta(K,A,B,C)," area(ABC)=",area(A,B,C)," area(BKC)=",area(B,K,C))
print("Phi direct=",num1/den1)
