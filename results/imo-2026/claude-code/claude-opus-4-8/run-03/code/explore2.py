import numpy as np
from scipy.optimize import fsolve
import itertools

def ang_between(P, Q, R):
    u = np.array(P)-np.array(Q); v = np.array(R)-np.array(Q)
    cu = np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v)); cu=max(-1,min(1,cu))
    return np.arccos(cu)
def rot(vec, theta):
    c,s=np.cos(theta),np.sin(theta); return np.array([c*vec[0]-s*vec[1],s*vec[0]+c*vec[1]])
def circumcenter(P,Q,R):
    ax,ay=P;bx,by=Q;cx,cy=R
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux=((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy=((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])
def circum_R(P,Q,R):
    O=circumcenter(P,Q,R); return np.linalg.norm(O-np.array(P))
def concyclic4(pts):
    # returns determinant-based measure; ~0 means concyclic
    M=[]
    for (x,y) in pts:
        M.append([x*x+y*y,x,y,1])
    return np.linalg.det(np.array(M))
def solve_valid(A,B,C,beta):
    A=np.array(A,float);B=np.array(B,float);C=np.array(C,float)
    M=(A+B)/2;N=(A+C)/2
    dK=rot((A-B)/np.linalg.norm(A-B),-beta)
    dL=rot((A-C)/np.linalg.norm(A-C),+beta)
    def eqs(x):
        s,u=x;K=B+s*dK;L=C+u*dL
        return [ang_between(L,B,K)-ang_between(L,N,C), ang_between(L,C,K)-ang_between(B,M,K)]
    sol=fsolve(eqs,(1.0,3.0))
    K=B+sol[0]*dK;L=C+sol[1]*dL
    return A,B,C,M,N,K,L

A,B,C,M,N,K,L=solve_valid((1,5),(0,0),(7,0),0.35)
O=circumcenter(A,K,L)
pts={'A':A,'B':B,'C':C,'M':M,'N':N,'K':K,'L':L,'O':O}
for k,v in pts.items(): print(k,v.round(5))
print("OM,ON:",np.linalg.norm(O-M),np.linalg.norm(O-N))
Rakl=np.linalg.norm(O-A)
def pow_(P): return np.linalg.norm(O-P)**2-Rakl**2
print("pow M,N:",pow_(M),pow_(N))
print("pow B,C:",pow_(B),pow_(C))

# search concyclic quadruples
names=list(pts.keys())
print("\n--- near-concyclic 4-subsets (normalized) ---")
for comb in itertools.combinations(names,4):
    ps=[pts[c] for c in comb]
    d=concyclic4(ps)
    # normalize by scale
    scale=np.mean([np.linalg.norm(p) for p in ps])**3 +1
    nd=d/scale
    if abs(nd)<0.05:
        print(comb, "det/scale=",f"{nd:.4f}")

# search collinear triples
print("\n--- near-collinear triples ---")
for comb in itertools.combinations(names,3):
    p,q,r=[pts[c] for c in comb]
    area=abs((q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]))
    if area<0.05: print(comb,"area=",f"{area:.4f}")
