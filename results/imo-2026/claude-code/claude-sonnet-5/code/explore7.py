import numpy as np
from scipy.optimize import fsolve

def concyclic_test(P,Q,R,S):
    # returns determinant; 0 means concyclic
    def row(X):
        return [X[0], X[1], X[0]**2+X[1]**2, 1]
    M = np.array([row(P),row(Q),row(R),row(S)])
    return np.linalg.det(M)

for trial in range(5):
    rng = np.random.default_rng(trial+1)
    A = rng.uniform(-2,2,2)
    B = rng.uniform(-2,2,2)
    C = rng.uniform(-2,2,2)
    # ensure non-degenerate
    if abs(np.cross(B-A,C-A))<0.3:
        continue
    M = (A+B)/2
    N = (A+C)/2

    def rot(v,ang):
        cs,sn=np.cos(ang),np.sin(ang)
        return np.array([cs*v[0]-sn*v[1], sn*v[0]+cs*v[1]])
    def signed_angle(u,v):
        a1=np.arctan2(u[1],u[0]); a2=np.arctan2(v[1],v[0])
        d=a2-a1
        while d>np.pi: d-=2*np.pi
        while d<=-np.pi: d+=2*np.pi
        return d
    def angle_between(u,v):
        cu=u/np.linalg.norm(u); cv=v/np.linalg.norm(v)
        return np.arccos(np.clip(np.dot(cu,cv),-1,1))
    def build_KL(theta,t,s):
        dirBA=A-B; dirBC=C-B
        sgn=np.sign(signed_angle(dirBA,dirBC))
        dir1=rot(dirBA,sgn*theta)
        K=B+t*dir1/np.linalg.norm(dir1)
        dirCA=A-C; dirCB=B-C
        sgn2=np.sign(signed_angle(dirCA,dirCB))
        dir2=rot(dirCA,sgn2*theta)
        L=C+s*dir2/np.linalg.norm(dir2)
        return K,L
    def equations(vars,theta):
        t,s=vars
        K,L=build_KL(theta,t,s)
        aLBK=angle_between(L-B,K-B)
        aLNC=angle_between(L-N,C-N)
        aLCK=angle_between(L-C,K-C)
        aBMK=angle_between(B-M,K-M)
        return [aLBK-aLNC, aLCK-aBMK]

    theta=0.3
    guess=[np.linalg.norm(B-A)/2, np.linalg.norm(C-A)/2]
    sol,info,ier,msg = fsolve(equations,guess,args=(theta,),full_output=True)
    if ier!=1:
        print(f"trial {trial}: solve failed"); continue
    t,s = sol
    K,L = build_KL(theta,t,s)
    K1 = A+B-K
    L1 = A+C-L

    detK = concyclic_test(A,K,C,K1)
    detL = concyclic_test(A,L,B,L1)
    print(f"trial {trial}: theta={theta} detK(A,K,C,K1)={detK:.3e}  detL(A,L,B,L1)={detL:.3e}")
