import numpy as np
from scipy.optimize import fsolve

def ang(v1, v2):
    c = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)+1e-300)
    return np.arccos(max(-1.0,min(1.0,c)))

def signed(v1,v2):
    return v1[0]*v2[1]-v1[1]*v2[0]

A = np.array([0.0,0.0]); B = np.array([4.0,0.0]); C = np.array([1.0,3.0])
M = (A+B)/2; N = (A+C)/2

def circumcenter(A,K,L):
    ax,ay=A; kx,ky=K; lx,ly=L
    D = 2*(ax*(ky-ly)+kx*(ly-ay)+lx*(ay-ky))
    ux = ((ax**2+ay**2)*(ky-ly)+(kx**2+ky**2)*(ly-ay)+(lx**2+ly**2)*(ay-ky))/D
    uy = ((ax**2+ay**2)*(lx-kx)+(kx**2+ky**2)*(ax-lx)+(lx**2+ly**2)*(kx-ax))/D
    return np.array([ux,uy])

def eqs(vars, lam):
    kx,ky,lx,ly = vars
    K = np.array([kx,ky]); L=np.array([lx,ly])
    e1 = ang(K-B, A-B) - ang(A-C, L-C)
    e2 = ang(L-B, K-B) - ang(L-N, C-N)
    e3 = ang(L-C, K-C) - ang(B-M, K-M)
    return [e1,e2,e3, lx-lam]

# Strict conditions:
# K inside triangle BMC, L inside triangle BNC
# K inside angle LBA (at B, between rays BL and BA)
# L inside angle ACK (at C, between rays CA and CK)

def satisfies(K,L):
    # inside triangle BMC
    def intr(P,X,Y,Z):
        s1=signed(Y-X,P-X); s2=signed(Z-Y,P-Y); s3=signed(X-Z,P-Z)
        return (s1>0 and s2>0 and s3>0) or (s1<0 and s2<0 and s3<0)
    if not intr(K,B,M,C): return False
    if not intr(L,B,N,C): return False
    # K inside angle LBA: at B, the wedge from BA to BL contains BK
    # use signed cross products with consistent orientation
    # angle LBA means vertex B, sides BL and BA. K inside => BK is between BA and BL.
    ba=A-B; bl=L-B; bk=K-B
    # K between means bk is convex combination direction
    def between(v,w,p):
        # p between v and w (both from origin) up to the smaller angle
        return signed(v,p)*signed(v,w)>=0 and signed(p,w)*signed(v,w)>=0
    if not between(ba,bl,bk): return False
    # L inside angle ACK: vertex C, sides CA and CK. CL between CA and CK.
    ca=A-C; ck=K-C; cl=L-C
    if not between(ca,ck,cl): return False
    return True

results=[]
for lam in np.linspace(0.2,2.0,200):
    for guess in ([2,1,lam,1],[1,1.5,lam,0.5],[2.5,0.8,lam,1.2],[1.5,1,lam,2],[3,1,lam,2.5]):
        try:
            x,info,ier,msg = fsolve(eqs, guess, args=(lam,), full_output=True)
            if ier==1 and np.max(np.abs(info['fvec']))<1e-9:
                K=x[:2]; L=x[2:]
                if satisfies(K,L):
                    if all(np.linalg.norm(K-rk)>1e-3 or np.linalg.norm(L-rl)>1e-3 for rk,rl in results):
                        results.append((K.copy(),L.copy()))
        except: pass

print("strict solutions:",len(results))
for K,L in results:
    O=circumcenter(A,K,L)
    print(f"K=({K[0]:.4f},{K[1]:.4f}) L=({L[0]:.4f},{L[1]:.4f}) OM={np.linalg.norm(O-M):.6f} ON={np.linalg.norm(O-N):.6f} diff={abs(np.linalg.norm(O-M)-np.linalg.norm(O-N)):.2e}")
