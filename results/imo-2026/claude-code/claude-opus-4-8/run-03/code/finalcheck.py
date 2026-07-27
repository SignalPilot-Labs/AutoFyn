import numpy as np
from scipy.optimize import fsolve
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
allok=True
for tri in [((1,5),(0,0),(7,0)),((2,6),(-1,0),(9,0)),((3,8),(0,0),(5,0)),((0,4),(-2,0),(5,0))]:
    A,B,C=[np.array(x,float) for x in tri]
    Aa=ang(B,A,C);Ba=ang(A,B,C);Ca=ang(A,C,B)
    a=np.linalg.norm(B-C)/2
    for beta in [0.2,0.35,0.5]:
        A_,B_,C_,M,N,K,L=solve_valid(*tri,beta)
        O=circumcenter(A,K,L)
        # 1) reduction: OM=ON
        red = abs(np.linalg.norm(O-M)-np.linalg.norm(O-N))
        # 2) antipode
        Astar=2*O-A
        red2=abs(np.linalg.norm(Astar-B)-np.linalg.norm(Astar-C))
        # 3) A* on perp bisector at height a cot(A+beta): height along perp bisector from P
        P=(B+C)/2
        # signed height toward A: component of (Astar-P) along unit normal to BC pointing to A
        bc=(C-B)/np.linalg.norm(C-B); nrm=np.array([-bc[1],bc[0]]); 
        if np.dot(A-P,nrm)<0: nrm=-nrm
        hgt=np.dot(Astar-P,nrm)
        pred=a*np.cos(Aa+beta)/np.sin(Aa+beta)
        # sign: pred can be negative meaning below; compare
        red3=abs(hgt-pred)
        # 4) mu-formula for h (B-side): 
        mu=ang(B,A,K)
        hform=-a*np.cos(Ba+mu)/np.sin(Ba+mu)+2*a*np.sin(Ca)*np.sin(mu)*np.cos(beta+mu)/(np.sin(Aa)*np.sin(beta+mu)*np.sin(Ba+mu))
        red4=abs(hform-hgt)
        ok = max(red,red2,red3,red4)<1e-5
        allok = allok and ok
        print(f"tri={tri} b={beta}: OM-ON={red:.1e} A*B-A*C={red2:.1e} hgt-acot={red3:.1e} hform-hgt={red4:.1e} {'OK' if ok else 'FAIL'}")
print("\nALL CHECKS PASS" if allok else "\nSOME FAILED")
