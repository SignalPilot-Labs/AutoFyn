import numpy as np
from scipy.optimize import fsolve

def circumcenter(P,Q,R):
    ax,ay=P; bx,by=Q; cx,cy=R
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux=((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy=((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

def ang(P,V,Q):
    # angle PVQ unsigned
    a=P-V; b=Q-V
    ca=np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    ca=max(-1,min(1,ca))
    return np.degrees(np.arccos(ca))

def build(p,q,theta_deg):
    B=np.array([-1.0,0]); C=np.array([1.0,0]); A=np.array([p,q])
    M=(A+B)/2; N=(A+C)/2
    theta=np.radians(theta_deg)
    def eqs(x):
        r1,phiK,r2,phiL=x
        K=B+r1*np.array([np.cos(phiK), np.sin(phiK)])
        L=C+r2*np.array([np.cos(phiL), np.sin(phiL)])
        e1=ang(A,B,K)-np.degrees(theta)
        e2=ang(A,C,L)-np.degrees(theta)
        e3=ang(L,B,K)-ang(L,N,C)
        e4=ang(L,C,K)-ang(B,M,K)
        return [e1,e2,e3,e4]
    # initial guess
    x0=[0.5, np.radians(120), 0.5, np.radians(60)]
    sol=fsolve(eqs,x0,full_output=True)
    x,info,ier,msg=sol
    if ier!=1:
        return None
    r1,phiK,r2,phiL=x
    K=B+r1*np.array([np.cos(phiK), np.sin(phiK)])
    L=C+r2*np.array([np.cos(phiL), np.sin(phiL)])
    res=np.max(np.abs(eqs(x)))
    return A,B,C,M,N,K,L,res

for (p,q,theta) in [(0.3,1.7,15),(-0.6,1.2,12),(0.1,2.5,10),(0.9,1.3,8)]:
    out=build(p,q,theta)
    if out is None:
        print(p,q,theta,"fail")
        continue
    A,B,C,M,N,K,L,res=out
    O=circumcenter(A,K,L)
    OM=np.linalg.norm(O-M); ON=np.linalg.norm(O-N)
    print(f"p={p},q={q},theta={theta}: residual={res:.2e} OM={OM:.6f} ON={ON:.6f} diff={OM-ON:.2e}")

    # Now test inversion+reflection sigma centered at A swapping B,C
    AB=np.linalg.norm(B-A); AC=np.linalg.norm(C-A)
    k=AB*AC
    def sigma(P):
        v=P-A
        d=np.linalg.norm(v)
        if d<1e-12: return None
        # reflect direction over angle bisector of angle A (between AB,AC directions), then invert with power k... 
        # simpler: sigma(P) defined by: along ray, but direction must be reflected across bisector of BA,CA
        dirAB=(B-A)/AB
        dirAC=(C-A)/AC
        # bisector direction
        bis = dirAB+dirAC
        bis = bis/np.linalg.norm(bis)
        # reflect v across bis line
        vhat=v/d
        refl = 2*np.dot(vhat,bis)*bis - vhat
        newd = k/d
        return A + newd*refl
    sB=sigma(B); sC=sigma(C); sM=sigma(M); sN=sigma(N); sO=sigma(O)
    print("  sigma(B)=",sB," (should be C=",C,")")
    print("  sigma(C)=",sC," (should be B=",B,")")
    print("  sigma(M)=",sM, " AC'=|sigma(M)-A|=",np.linalg.norm(sM-A), " 2AC=",2*AC)
    print("  sigma(N)=",sN, " AB'=|sigma(N)-A|=",np.linalg.norm(sN-A), " 2AB=",2*AB)

print("\n--- checking sigma(Gamma) collinearity / power relation ---")
