import numpy as np
from scipy.optimize import least_squares

def ang(Y,X,Z):
    v1=X-Y;v2=Z-Y;cr=v1[0]*v2[1]-v1[1]*v2[0];dt=v1[0]*v2[0]+v1[1]*v2[1];return np.arctan2(abs(cr),dt)
def cross2(u,v):return u[0]*v[1]-u[1]*v[0]
def circumcenter(P1,P2,P3):
    ax,ay=P1;bx,by=P2;cx,cy=P3;D=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    return np.array([((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/D,((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/D])
def inside(P,U,V,W):
    def s(a,b,p):return cross2(b-a,p-a)
    d1=s(U,V,P);d2=s(V,W,P);d3=s(W,U,P)
    return (d1>=-1e-7 and d2>=-1e-7 and d3>=-1e-7) or (d1<=1e-7 and d2<=1e-7 and d3<=1e-7)

maxdiff=0
nsuccess=0
for trial in range(40):
    rng=np.random.RandomState(trial)
    # random triangle
    A=rng.uniform([-3,-1],[3,5]); B=rng.uniform([-4,-2],[0,1]); C=rng.uniform([0,-2],[4,1])
    # ensure nondegenerate
    if abs(cross2(C-B,A-B))<0.5: continue
    M=(A+B)/2;N=(A+C)/2
    def resv(vars,kx):
        K=np.array([kx,vars[0]]);L=np.array([vars[1],vars[2]])
        f1=ang(B,K,A)-ang(C,A,L);f2=ang(B,L,K)-ang(N,L,C);f3=ang(C,L,K)-ang(M,B,K)
        return [f1,f2,f3]
    ok=False
    # pick kx within x-range of triangle BMC
    for kx in np.linspace(min(B[0],M[0],C[0])+0.1, max(B[0],M[0],C[0])-0.1, 8):
        for seed in range(80):
            r2=np.random.RandomState(seed+1000)
            try:
                sol=least_squares(resv,[r2.uniform(-1,3),r2.uniform(-1,3),r2.uniform(-1,3)],args=(kx,),xtol=1e-15,ftol=1e-15,gtol=1e-15)
                r=sol.x;res=resv([r[0],r[1],r[2]],kx)
                if np.max(np.abs(res))<1e-9:
                    K=np.array([kx,r[0]]);L=np.array([r[1],r[2]])
                    if inside(K,B,M,C) and inside(L,B,N,C):
                        O=circumcenter(A,K,L)
                        d=abs(np.linalg.norm(O-M)-np.linalg.norm(O-N))
                        maxdiff=max(maxdiff,d)
                        nsuccess+=1
                        ok=True
                        break
            except:pass
        if ok:break
print(f"Successful solutions: {nsuccess}, max |OM-ON| = {maxdiff:.2e}")
