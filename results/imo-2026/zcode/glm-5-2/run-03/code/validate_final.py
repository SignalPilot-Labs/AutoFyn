import numpy as np
from scipy.optimize import least_squares

def ang(Y,X,Z):
    v1=X-Y;v2=Z-Y;cr=v1[0]*v2[1]-v1[1]*v2[0];dt=v1[0]*v2[0]+v1[1]*v2[1];return np.arctan2(abs(cr),dt)
def cross2(u,v):return u[0]*v[1]-u[1]*v[0]
def inside(P,U,V,W):
    def s(a,b,p):return cross2(b-a,p-a)
    d1=s(U,V,P);d2=s(V,W,P);d3=s(W,U,P)
    return (d1>=-1e-7 and d2>=-1e-7 and d3>=-1e-7) or (d1<=1e-7 and d2<=1e-7 and d3<=1e-7)

# cond1_num and cond2_num as functions
def cond1(u,v,a,b,g):
    return a**2*b**2*u**2 - a**2*b**2*u + a**2*b**2*v**2 - a**2*b*v - 2*a**2*u - 2*a*b*u**2 - 2*a*b*u - 2*a*b*v**2 + 2*a*v - b**2*u**2 - b**2*u - b**2*v**2 + b*v
def cond2(u,v,a,b,g):
    return a**2*g**2*u**2 - a**2*g**2*u + a**2*g**2*v**2 - a**2*g*v + 2*a**2*u - 2*a**2 - 2*a*g*u**2 + 6*a*g*u - 2*a*g*v**2 - 4*a*g + 2*a*v - g**2*u**2 + 3*g**2*u - g**2*v**2 - 2*g**2 + g*v

maxc1=maxc2=0; n=0
for (uv,vv) in [(0.3,2.0),(0.8,1.5),(1.2,3.0),(0.5,1.2),(0.1,1.0),(1.5,2.0),(0.7,2.5)]:
    A=np.array([2*uv,2*vv]);B=np.array([0.,0.]);C=np.array([2.,0.]);M=(A+B)/2;N=(A+C)/2
    def resv(vars,kx):
        K=np.array([kx,vars[0]]);L=np.array([vars[1],vars[2]])
        f1=ang(B,K,A)-ang(C,A,L);f2=ang(B,L,K)-ang(N,L,C);f3=ang(C,L,K)-ang(M,B,K)
        return [f1,f2,f3]
    found=None
    for kx in np.linspace(0.1,1.8,15):
        for seed in range(200):
            r2=np.random.RandomState(seed+11)
            try:
                sol=least_squares(resv,[r2.uniform(0.1,5),r2.uniform(0.1,1.9),r2.uniform(0.1,5)],args=(kx,),xtol=1e-15,ftol=1e-15,gtol=1e-15)
                r=sol.x;res=resv([r[0],r[1],r[2]],kx)
                if np.max(np.abs(res))<1e-11:
                    K=np.array([kx,r[0]]);L=np.array([r[1],r[2]])
                    if inside(K,B,M,C) and inside(L,B,N,C):
                        found=(K,L);break
            except:pass
        if found:break
    if not found:
        print(f"u={uv},v={vv}: no solution"); continue
    K,L=found
    alpha=ang(B,K,A);beta=ang(B,L,K);gamma=ang(C,L,K)
    a=np.tan(alpha);b=np.tan(beta);g=np.tan(gamma)
    c1=cond1(uv,vv,a,b,g); c2=cond2(uv,vv,a,b,g)
    maxc1=max(maxc1,abs(c1)); maxc2=max(maxc2,abs(c2)); n+=1
    print(f"u={uv},v={vv}: a={a:.4f} b={b:.4f} g={g:.4f}  cond1={c1:.2e}  cond2={c2:.2e}")
print(f"\n{n} configs. max|cond1|={maxc1:.2e}, max|cond2|={maxc2:.2e}")
