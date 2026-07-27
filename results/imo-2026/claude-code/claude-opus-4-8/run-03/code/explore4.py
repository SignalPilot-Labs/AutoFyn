import numpy as np
from scipy.optimize import fsolve
def ang(P,Q,R):
    u=np.array(P)-np.array(Q);v=np.array(R)-np.array(Q)
    c=np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v));c=max(-1,min(1,c));return np.degrees(np.arccos(c))
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
def line_circle_2nd(P,dirv,O,R,known):
    # intersect line P+t*dirv with circle center O radius R, return the intersection != known
    d=np.array(dirv,float);d=d/np.linalg.norm(d)
    f=np.array(P)-O
    b=2*np.dot(f,d);c=np.dot(f,f)-R*R
    disc=b*b-4*c
    if disc<0: return None
    t1=(-b+np.sqrt(disc))/2;t2=(-b-np.sqrt(disc))/2
    X1=np.array(P)+t1*d;X2=np.array(P)+t2*d
    if np.linalg.norm(X1-known)<np.linalg.norm(X2-known): return X2
    return X1
def dist(P,Q):return np.linalg.norm(np.array(P)-np.array(Q))

A,B,C,M,N,K,L=solve_valid((1,5),(0,0),(7,0),0.35)
O=circumcenter(A,K,L);R=dist(O,A)
# second intersections
AB2=line_circle_2nd(A,B-A,O,R,A)  # line AB, second pt (other than A)
AC2=line_circle_2nd(A,C-A,O,R,A)
BK2=line_circle_2nd(K,B-K,O,R,K)  # line through K,B; second pt other than K
CL2=line_circle_2nd(L,C-L,O,R,L)
print("A',along AB:",AB2.round(4)," M=",M.round(4))
print("A'',along AC:",AC2.round(4)," N=",N.round(4))
print("BK 2nd:",BK2.round(4))
print("CL 2nd:",CL2.round(4))
# pow M via line AB: MA*MA2 (signed)
def signed_prod(P, X, Y):
    # P on line XY: returns (P-X)·(P-Y) with sign along line
    return np.dot(np.array(X)-P, np.array(Y)-P)
print("pow(M)=",dist(O,M)**2-R**2, " MA*MA'(signed)=",signed_prod(M,A,AB2))
print("pow(N)=",dist(O,N)**2-R**2, " NA*NA''(signed)=",signed_prod(N,A,AC2))
# distances to identify AB2, AC2
print("MA=",dist(M,A)," MB=",dist(M,B)," MA'=",dist(M,AB2)," A'B=",dist(AB2,B)," A'A=",dist(AB2,A))
print("NA=",dist(N,A)," NC=",dist(N,C)," NA''=",dist(N,AC2)," A''C=",dist(AC2,C))
# Is BK2 = something like reflection? print distances to all pts
pts={'A':A,'B':B,'C':C,'M':M,'N':N,'K':K,'L':L,'O':O,'A_AB':AB2,'A_AC':AC2}
for nm in ['BK2','CL2']:
    X=BK2 if nm=='BK2' else CL2
    print(nm, {k:round(dist(X,v),4) for k,v in pts.items()})
