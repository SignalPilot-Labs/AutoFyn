import numpy as np
from scipy.optimize import least_squares
def ang(Y,X,Z):
    v1=X-Y;v2=Z-Y;cr=v1[0]*v2[1]-v1[1]*v2[0];dt=v1[0]*v2[0]+v1[1]*v2[1];return np.arctan2(abs(cr),dt)
def cross2(u,v):return u[0]*v[1]-u[1]*v[0]
def inside(P,U,V,W):
    def s(a,b,p):return cross2(b-a,p-a)
    d1=s(U,V,P);d2=s(V,W,P);d3=s(W,U,P)
    return (d1>=-1e-7 and d2>=-1e-7 and d3>=-1e-7) or (d1<=1e-7 and d2<=1e-7 and d3<=1e-7)

def valid_config(A,B,C,K,L):
    # K inside angle LBA at B, and L inside angle ACK at C.
    M=(A+B)/2;N=(A+C)/2
    # K inside angle LBA: ray BK between BL and BA (the angle < 180 containing the interior).
    # Use cross products: cross(BA,BK) and cross(BK,BL) and cross(BL,BA) all same sign? 
    def cr(P,Q):return P[0]*Q[1]-P[1]*Q[0]
    BA=A-B;BK=K-B;BL=L-B
    # For K inside angle LBA (vertex B), the three points A,K,L as seen from B with K inside.
    # K inside angle(L,B,A): angle from BL to BA (shorter) contains BK.
    # equivalent: cr(BA,BK)*cr(BA,BL) <= 0 and cr(BL,BK)*cr(BL,BA) <=0... let me just check BK is between.
    # Simplest: angle(BL,BK)+angle(BK,BA) == angle(BL,BA) (K between L and A rays)
    a1=ang(B,L,K); a2=ang(B,K,A); a3=ang(B,L,A)
    k_in_LBA = abs(a1+a2-a3)<1e-6
    # L inside angle ACK at C: L between CA and CK rays
    CA=A-C; CL=L-C; CK=K-C
    b1=ang(C,A,L); b2=ang(C,L,K); b3=ang(C,A,K)
    l_in_ACK = abs(b1+b2-b3)<1e-6
    return k_in_LBA and l_in_ACK

def cond1(u,v,a,b,g):
    return a**2*b**2*u**2 - a**2*b**2*u + a**2*b**2*v**2 - a**2*b*v - 2*a**2*u - 2*a*b*u**2 - 2*a*b*u - 2*a*b*v**2 + 2*a*v - b**2*u**2 - b**2*u - b**2*v**2 + b*v
def cond2(u,v,a,b,g):
    return a**2*g**2*u**2 - a**2*g**2*u + a**2*g**2*v**2 - a**2*g*v + 2*a**2*u - 2*a**2 - 2*a*g*u**2 + 6*a*g*u - 2*a*g*v**2 - 4*a*g + 2*a*v - g**2*u**2 + 3*g**2*u - g**2*v**2 - 2*g**2 + g*v

maxc1=maxc2=0;n=0; skipped=0
for (uv,vv) in [(0.3,2.0),(0.8,1.5),(1.2,3.0),(0.5,1.2),(0.1,1.0),(1.5,2.0),(0.7,2.5),(0.9,1.8),(0.2,1.3)]:
    A=np.array([2*uv,2*vv]);B=np.array([0.,0.]);C=np.array([2.,0.]);M=(A+B)/2;N=(A+C)/2
    def resv(vars,kx):
        K=np.array([kx,vars[0]]);L=np.array([vars[1],vars[2]])
        f1=ang(B,K,A)-ang(C,A,L);f2=ang(B,L,K)-ang(N,L,C);f3=ang(C,L,K)-ang(M,B,K)
        return [f1,f2,f3]
    found=None
    for kx in np.linspace(0.1,1.8,15):
        for seed in range(300):
            r2=np.random.RandomState(seed+11)
            try:
                sol=least_squares(resv,[r2.uniform(0.1,5),r2.uniform(0.1,1.9),r2.uniform(0.1,5)],args=(kx,),xtol=1e-15,ftol=1e-15,gtol=1e-15)
                r=sol.x;res=resv([r[0],r[1],r[2]],kx)
                if np.max(np.abs(res))<1e-11:
                    K=np.array([kx,r[0]]);L=np.array([r[1],r[2]])
                    if inside(K,B,M,C) and inside(L,B,N,C) and valid_config(A,B,C,K,L):
                        found=(K,L);break
            except:pass
        if found:break
    if not found:
        print(f"u={uv},v={vv}: no VALID solution"); continue
    K,L=found
    alpha=ang(B,K,A);beta=ang(B,L,K);gamma=ang(C,L,K)
    a=np.tan(alpha);b=np.tan(beta);g=np.tan(gamma)
    c1=cond1(uv,vv,a,b,g); c2=cond2(uv,vv,a,b,g)
    maxc1=max(maxc1,abs(c1)); maxc2=max(maxc2,abs(c2)); n+=1
    print(f"u={uv},v={vv}: cond1={c1:.2e}  cond2={c2:.2e}")
print(f"\n{n} valid configs. max|cond1|={maxc1:.2e}, max|cond2|={maxc2:.2e}")

print("\n--- Final OM=ON check on valid configs ---")
def circumcenter(P1,P2,P3):
    ax,ay=P1;bx,by=P2;cx,cy=P3;D=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    return np.array([((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/D,((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/D])
for (uv,vv) in [(0.3,2.0),(1.2,3.0),(0.1,1.0),(0.9,1.8)]:
    A=np.array([2*uv,2*vv]);B=np.array([0.,0.]);C=np.array([2.,0.]);M=(A+B)/2;N=(A+C)/2
    def resv(vars,kx):
        K=np.array([kx,vars[0]]);L=np.array([vars[1],vars[2]])
        f1=ang(B,K,A)-ang(C,A,L);f2=ang(B,L,K)-ang(N,L,C);f3=ang(C,L,K)-ang(M,B,K)
        return [f1,f2,f3]
    found=None
    for kx in np.linspace(0.1,1.8,15):
        for seed in range(300):
            r2=np.random.RandomState(seed+11)
            try:
                sol=least_squares(resv,[r2.uniform(0.1,5),r2.uniform(0.1,1.9),r2.uniform(0.1,5)],args=(kx,),xtol=1e-15,ftol=1e-15,gtol=1e-15)
                r=sol.x;res=resv([r[0],r[1],r[2]],kx)
                if np.max(np.abs(res))<1e-11:
                    K=np.array([kx,r[0]]);L=np.array([r[1],r[2]])
                    if inside(K,B,M,C) and inside(L,B,N,C) and valid_config(A,B,C,K,L):
                        found=(K,L);break
            except:pass
        if found:break
    K,L=found
    O=circumcenter(A,K,L)
    print(f"u={uv},v={vv}: |OM-ON|={abs(np.linalg.norm(O-M)-np.linalg.norm(O-N)):.2e}, Ox={O[0]:.6f} (target {uv+0.5:.6f})")
