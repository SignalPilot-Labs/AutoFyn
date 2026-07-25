import numpy as np
from scipy.optimize import fsolve
def ang(v1,v2):
    c=np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)+1e-300);return np.arccos(max(-1,min(1,c)))
def signed(v1,v2):return v1[0]*v[1]-v1[1]*v2[1] if False else v1[0]*v2[1]-v1[1]*v2[0]
def between(v,w,p):return signed(v,p)*signed(v,w)>=0 and signed(p,w)*signed(v,w)>=0
def intr(P,X,Y,Z):
    s1=signed(Y-X,P-X);s2=signed(Z-Y,P-Y);s3=signed(X-Z,P-Z)
    return (s1>0 and s2>0 and s3>0)or(s1<0 and s2<0 and s3<0)
def circumcenter(A,K,L):
    ax,ay=A;kx,ky=K;lx,ly=L;D=2*(ax*(ky-ly)+kx*(ly-ay)+lx*(ay-ky))
    ux=((ax**2+ay**2)*(ky-ly)+(kx**2+ky**2)*(ly-ay)+(lx**2+ly**2)*(ay-ky))/D
    uy=((ax**2+ay**2)*(lx-kx)+(kx**2+ky**2)*(ax-lx)+(lx**2+ly**2)*(kx-ax))/D
    return np.array([ux,uy])
# verify OM=ON: since OM=ON <=> O on perp bisector of MN <=> TGT=0. Direct check.
import random
random.seed(42)
ok=0;tot=0
for trial in range(40):
    pval=random.uniform(0.2,2.5);qval=random.uniform(0.3,2.5)
    A=np.array([0.,0.]);B=np.array([1.,0.]);C=np.array([pval,qval]);M=(A+B)/2;N=(A+C)/2
    def eqs(vars,lam):
        kx,ky,lx,ly=vars;K=np.array([kx,ky]);L=np.array([lx,ly])
        return [ang(K-B,A-B)-ang(A-C,L-C),ang(L-B,K-B)-ang(L-N,C-N),ang(L-C,K-C)-ang(B-M,K-M),kx-lam]
    for lam in np.linspace(0.3,0.8,12):
        for g0 in ([lam,0.1,0.2,0.4],[lam,0.2,0.5,0.3]):
            try:
                x,info,ier,msg=fsolve(eqs,g0,args=(lam,),full_output=True)
                if ier==1 and np.max(np.abs(info['fvec']))<1e-9:
                    K=x[:2];L=x[2:]
                    if intr(K,B,M,C) and intr(L,B,N,C) and between(A-B,L-B,K-B) and between(A-C,K-C,L-C):
                        O=circumcenter(A,K,L)
                        d=abs(np.linalg.norm(O-M)-np.linalg.norm(O-N))
                        tot+=1
                        if d<1e-7:ok+=1
                        else:print("FAIL",pval,qval,d)
                        break
            except:pass
        else: continue
        break
print(f"valid configs: {tot}, OM=ON holds: {ok}, all pass: {ok==tot}")
