import numpy as np
from scipy.optimize import fsolve

def ang(v1, v2):
    c = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)+1e-300)
    c = max(-1.0,min(1.0,c))
    return np.arccos(c)

def circumcenter(A,K,L):
    ax,ay=A; kx,ky=K; lx,ly=L
    D = 2*(ax*(ky-ly)+kx*(ly-ay)+lx*(ay-ky))
    ux = ((ax**2+ay**2)*(ky-ly)+(kx**2+ky**2)*(ly-ay)+(lx**2+ly**2)*(ay-ky))/D
    uy = ((ax**2+ay**2)*(lx-kx)+(kx**2+ky**2)*(ax-lx)+(lx**2+ly**2)*(kx-ax))/D
    return np.array([ux,uy])

def in_tri(P,X,Y,Z):
    """barycentric all positive"""
    v0=Y-X; v1=Z-X; v2=P-X
    d00=np.dot(v0,v0); d01=np.dot(v0,v1); d11=np.dot(v1,v1)
    d20=np.dot(v2,v0); d21=np.dot(v2,v1)
    den=d00*d11-d01*d01
    v=(d11*d20-d01*d21)/den
    w=(d00*d21-d01*d20)/den
    u=1-v-w
    return u>1e-6 and v>1e-6 and w>1e-6, (u,v,w)

A = np.array([0.0,0.0]); B = np.array([4.0,0.0]); C = np.array([1.0,3.0])
M = (A+B)/2; N = (A+C)/2

def eqs(vars, lam):
    kx,ky,lx,ly = vars
    K = np.array([kx,ky]); L=np.array([lx,ly])
    e1 = ang(K-B, A-B) - ang(A-C, L-C)
    e2 = ang(L-B, K-B) - ang(L-N, C-N)
    e3 = ang(L-C, K-C) - ang(B-M, K-M)
    e4 = lx - lam
    return [e1,e2,e3,e4]

results=[]
for lam in np.linspace(0.2,1.8,80):
    for guess in ([2,1,lam,1],[1,1.5,lam,0.5],[2.5,0.8,lam,1.2]):
        try:
            x,info,ier,msg = fsolve(eqs, guess, args=(lam,), full_output=True)
            if ier==1 and np.max(np.abs(info['fvec']))<1e-9:
                K=x[:2]; L=x[2:]
                ink,_=in_tri(K,B,M,C); inl,_=in_tri(L,B,N,C)
                if ink and inl:
                    # dedupe
                    if all(np.linalg.norm(K-rk)>1e-4 or np.linalg.norm(L-rl)>1e-4 for _,rk,rl,_ in results):
                        results.append((lam,K.copy(),L.copy(),np.max(np.abs(info['fvec']))))
        except: pass

print("solutions:",len(results))
for lam,K,L,r in results:
    O=circumcenter(A,K,L)
    print(f"lam={lam:.3f} K=({K[0]:.4f},{K[1]:.4f}) L=({L[0]:.4f},{L[1]:.4f}) OM={np.linalg.norm(O-M):.6f} ON={np.linalg.norm(O-N):.6f} diff={abs(np.linalg.norm(O-M)-np.linalg.norm(O-N)):.2e}")
