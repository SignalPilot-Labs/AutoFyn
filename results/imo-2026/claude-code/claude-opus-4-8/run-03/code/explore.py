import numpy as np
from scipy.optimize import fsolve

def ang_between(P, Q, R):
    # angle at Q between rays QP and QR (unsigned, in [0,pi])
    u = np.array(P)-np.array(Q); v = np.array(R)-np.array(Q)
    cu = np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))
    cu = max(-1,min(1,cu))
    return np.arccos(cu)

def rot(vec, theta):
    c,s = np.cos(theta), np.sin(theta)
    return np.array([c*vec[0]-s*vec[1], s*vec[0]+c*vec[1]])

def solve_config(A,B,C,beta, guess=(1.0,1.0)):
    A=np.array(A,float);B=np.array(B,float);C=np.array(C,float)
    M=(A+B)/2; N=(A+C)/2
    # direction of BK: rotate BA by -beta (clockwise toward C) -- need to pick correct sign so K inside
    dBA = A-B
    # decide rotation sign: interior toward C. test both.
    def dirK(sign):
        return rot(dBA/np.linalg.norm(dBA), sign*beta)
    dCA = A-C
    def dirL(sign):
        return rot(dCA/np.linalg.norm(dCA), sign*beta)
    # We'll choose signs so that K is inside triangle. Let's just try combos and see which yields interior solution.
    results=[]
    for sK in (+1,-1):
        for sL in (+1,-1):
            dK = dirK(sK); dL = dirL(sL)
            def eqs(x):
                s,u = x
                K = B + s*dK
                L = C + u*dL
                e1 = ang_between(L,B,K) - ang_between(L,N,C)
                e2 = ang_between(L,C,K) - ang_between(B,M,K)
                return [e1,e2]
            try:
                sol,info,ier,msg = fsolve(eqs, guess, full_output=True)
                if ier==1 and sol[0]>0 and sol[1]>0:
                    K=B+sol[0]*dK; L=C+sol[1]*dL
                    results.append((sK,sL,sol,K,L))
            except Exception as e:
                pass
    return A,B,C,M,N,results

def circumcenter(P,Q,R):
    ax,ay=P;bx,by=Q;cx,cy=R
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux=((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy=((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

def inside_tri(P,X,Y,Z):
    # barycentric sign test
    def sign(a,b,c): return (a[0]-c[0])*(b[1]-c[1])-(b[0]-c[0])*(a[1]-c[1])
    d1=sign(P,X,Y);d2=sign(P,Y,Z);d3=sign(P,Z,X)
    neg=(d1<0)or(d2<0)or(d3<0); pos=(d1>0)or(d2>0)or(d3>0)
    return not(neg and pos)

A=(1,5);B=(0,0);C=(7,0)
for beta in [0.2,0.3,0.4,0.5]:
    res=solve_config(A,B,C,beta)
    A_,B_,C_,M,N,results=res
    print("beta=",beta)
    for (sK,sL,sol,K,L) in results:
        M_=(np.array(A)+np.array(B))/2; N_=(np.array(A)+np.array(C))/2
        # check interior: K in BMC, L in BNC
        inK = inside_tri(K,B_,M,C_)
        inL = inside_tri(L,B_,N,C_)
        O=circumcenter(np.array(A,float),K,L)
        OM=np.linalg.norm(O-M_);ON=np.linalg.norm(O-N_)
        print(f"  sK={sK} sL={sL} s={sol[0]:.4f} u={sol[1]:.4f} K={K.round(4)} L={L.round(4)} inK={inK} inL={inL} OM={OM:.5f} ON={ON:.5f} diff={OM-ON:.2e}")
