import numpy as np
from scipy.optimize import fsolve
def ang(v1,v2):
    c=np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)+1e-300);return np.arccos(max(-1,min(1,c)))
def signed(v1,v2):return v1[0]*v2[1]-v1[1]*v2[0]
def between(v,w,p):return signed(v,p)*signed(v,w)>=0 and signed(p,w)*signed(v,w)>=0
def intr(P,X,Y,Z):
    s1=signed(Y-X,P-X);s2=signed(Z-Y,P-Y);s3=signed(X-Z,P-Z)
    return (s1>0 and s2>0 and s3>0)or(s1<0 and s2<0 and s3<0)
def circumcenter(A,K,L):
    ax,ay=A;kx,ky=K;lx,ly=L;D=2*(ax*(ky-ly)+kx*(ly-ay)+lx*(ay-ky))
    ux=((ax**2+ay**2)*(ky-ly)+(kx**2+ky**2)*(ly-ay)+(lx**2+ly**2)*(ay-ky))/D
    uy=((ax**2+ay**2)*(lx-kx)+(kx**2+ky**2)*(ax-lx)+(lx**2+ly**2)*(kx-ax))/D
    return np.array([ux,uy])
# Second triangle: scalene, different shape. A=(0,0),B=(1,0),C=(0.7,1.3)
for (pval,qval) in [(0.7,1.3),(1.5,0.8),(0.3,2.0),(2.0,1.0)]:
    A=np.array([0.0,0.0]);B=np.array([1.0,0.0]);C=np.array([pval,qval]);M=(A+B)/2;N=(A+C)/2
    def eqs(vars,lam):
        kx,ky,lx,ly=vars;K=np.array([kx,ky]);L=np.array([lx,ly])
        return [ang(K-B,A-B)-ang(A-C,L-C),ang(L-B,K-B)-ang(L-N,C-N),ang(L-C,K-C)-ang(B-M,K-M),kx-lam]
    found=False
    for lam in np.linspace(0.3,0.85,30):
        for g in ([lam,0.1,0.2,0.4],[lam,0.3,0.1,0.6],[lam,0.05,0.4,0.2]):
            try:
                x,info,ier,msg=fsolve(eqs,g,args=(lam,),full_output=True)
                if ier==1 and np.max(np.abs(info['fvec']))<1e-9:
                    K=x[:2];L=x[2:]
                    if intr(K,B,M,C) and intr(L,B,N,C) and between(A-B,L-B,K-B) and between(A-C,K-C,L-C):
                        O=circumcenter(A,K,L)
                        d=abs(np.linalg.norm(O-M)-np.linalg.norm(O-N))
                        print(f"C=({pval},{qval}): OM-ON={d:.2e}  OM={np.linalg.norm(O-M):.5f}")
                        found=True;break
            except:pass
        if found:break
    if not found: print(f"C=({pval},{qval}): no valid config found")
