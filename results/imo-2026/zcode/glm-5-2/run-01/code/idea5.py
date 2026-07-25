import numpy as np
from scipy.optimize import fsolve

def ang(v1, v2):
    c = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)+1e-300)
    return np.arccos(max(-1.0,min(1.0,c)))

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
x,info,ier,msg = fsolve(eqs, [2.5,0.4,0.95,2.1], args=(0.95,), full_output=True)
K=x[:2]; L=x[2:]
O=circumcenter(A,K,L)

# Check triangle BMK angles precisely
def show(name,P,Q,R):
    aP=ang(Q-P,R-P); aQ=ang(P-Q,R-Q); aR=ang(P-R,Q-R)
    print(f"{name}: at {name[0]}? P={np.degrees(aP):.4f} Q={np.degrees(aQ):.4f} R={np.degrees(aR):.4f}")
print("BMK (B,M,K):"); print(f"  at B={np.degrees(ang(M-B,K-B)):.4f} at M={np.degrees(ang(B-M,K-M)):.4f} at K={np.degrees(ang(B-K,M-K)):.4f}")
print("KLC (K,L,C):"); print(f"  at K={np.degrees(ang(L-K,C-K)):.4f} at L={np.degrees(ang(K-L,C-L)):.4f} at C={np.degrees(ang(K-C,L-C)):.4f}")
print()
print("LNC (L,N,C):"); print(f"  at L={np.degrees(ang(N-L,C-L)):.4f} at N={np.degrees(ang(L-N,C-N)):.4f} at C={np.degrees(ang(L-C,N-C)):.4f}")
print("BKL (B,K,L):"); print(f"  at B={np.degrees(ang(K-B,L-B)):.4f} at K={np.degrees(ang(B-K,L-K)):.4f} at L={np.degrees(ang(B-L,K-L)):.4f}")
print()
# Similarity check: BMK and KLC. BMK angles: at M = gamma=34.22. KLC at L = ?
# If BMK ~ KLC with M<->L (both gamma). BMK: B,M,K ; KLC: K,L,C. 
#   M(gamma=34.2)<->L. Need BMK at B = KLC at K and BMK at K = KLC at C, OR swapped.
print("Match attempt BMK~KLC: M-gamma<->L-gamma?")
print(f"  BMK at B={np.degrees(ang(M-B,K-B)):.4f} vs KLC at C={np.degrees(ang(K-C,L-C)):.4f}")
print(f"  BMK at K={np.degrees(ang(B-K,M-K)):.4f} vs KLC at K={np.degrees(ang(L-K,C-K)):.4f}")
