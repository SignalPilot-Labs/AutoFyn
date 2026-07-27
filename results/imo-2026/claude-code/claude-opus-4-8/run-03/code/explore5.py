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
def dist(P,Q):return np.linalg.norm(np.array(P)-np.array(Q))
def inter(P1,d1,P2,d2):
    # line P1+t d1 = P2+s d2
    A=np.array([[d1[0],-d2[0]],[d1[1],-d2[1]]]);b=np.array(P2)-np.array(P1)
    t,s=np.linalg.solve(A,b);return np.array(P1)+t*np.array(d1)

for (tri,beta) in [(((1,5),(0,0),(7,0)),0.35),(((2,6),(-1,0),(9,0)),0.5),(((0,4),(-2,0),(5,0)),0.25)]:
    A,B,C,M,N,K,L=solve_valid(*tri,beta)
    O=circumcenter(A,K,L);R=dist(O,A)
    Astar=2*O-A
    print("tri",tri,"beta",beta)
    print("  A*B=",dist(Astar,B)," A*C=",dist(Astar,C)," equal?",abs(dist(Astar,B)-dist(Astar,C))<1e-6)
    print("  check perp: A*K.AK=",np.dot(Astar-K,A-K)," A*L.AL=",np.dot(Astar-L,A-L))
    # is A* = intersection of BK and CL?
    try:
        X=inter(B,K-B,C,L-C); print("  BK∩CL=",X.round(4)," A*=",Astar.round(4)," same?",dist(X,Astar)<1e-6)
    except: pass
    # perpendicular bisector of BC passes A*? 
    P=(B+C)/2
    print("  (A*-P).(B-C)=",np.dot(Astar-P,B-C))
