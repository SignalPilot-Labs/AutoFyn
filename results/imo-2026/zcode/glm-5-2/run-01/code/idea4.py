import numpy as np
from scipy.optimize import fsolve

def ang(v1, v2):
    c = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)+1e-300)
    return np.arccos(max(-1.0,min(1.0,c)))
def signed(v1,v2): return v1[0]*v2[1]-v1[1]*v2[0]
def between(v,w,p): return signed(v,p)*signed(v,w)>=0 and signed(p,w)*signed(v,w)>=0
def intr(P,X,Y,Z):
    s1=signed(Y-X,P-X); s2=signed(Z-Y,P-Y); s3=signed(X-Z,P-Z)
    return (s1>0 and s2>0 and s3>0) or (s1<0 and s2<0 and s3<0)

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
print("K",K,"L",L,"O",O)
print("OM,ON",np.linalg.norm(O-M),np.linalg.norm(O-N))
print()

# Investigate similarities. The conditions:
# ang KBA = ang ACL ; ang LBK = ang LNC ; ang LCK = ang BMK
# Let alpha = ang KBA = ang ACL
#     beta  = ang LBK = ang LNC
#     gamma = ang LCK = ang BMK
# At vertex B: rays BA, BK, BL, BC. ang KBA=alpha (between BK,BA). ang LBK=beta (between BL,BK).
#   So ang LBA = alpha+beta. ang ABC = ang LBA + ang LBC.
# At vertex C: rays CA, CL, CK, CB. ang ACL=alpha (between AC,CL). ang LCK=gamma (between CL,CK).
#   So ang ACK = alpha+gamma.
# Look at triangles with these angles. Consider triangles involving M,N (midpoints).
# Triangle LNC: angle at N = ang LNC = beta. N is midpoint of AC. 
# Triangle BMK: angle at M = ang BMK = gamma... wait ang BMK is at M? angle BMK = vertex M, rays MB,MK. 
#   M midpoint of AB.
# Triangle BKL: angles alpha+beta at B (ang LB A = alpha+beta, contains K)... 
#   In triangle BKL: angle at B = ang KBL = beta (since ang LBK = beta). 

# Let me think about TRIANGLE BK L vs others.
# In triangle BKL: 
#   angle at B = ang KBL. Note ang LBA=alpha+beta and K inside angle LBA => angle KBL = ang LBA - ang KBA = beta. Yes.
#   So angle B in triangle BKL = beta.
# Triangle LNC has angle beta at N.
# Are triangles BKL and LNC similar? They share angle beta. Need another.
# angle at L in BKL = ang BLK. Triangle LNC angles: at N=beta, at L = ang NLC, at C = ang LCN.
# ang LCK = gamma but that's at C with K not L. Hmm.

# Let me instead check numerically if triangles BKL ~ LNC.
def tri_angles(X,Y,Z):
    a=ang(Y-X,Z-X); b=ang(Z-Y,X-Y); c=ang(X-Z,Y-Z)
    return sorted([np.degrees(a),np.degrees(b),np.degrees(c)])
print("BKL angles:", tri_angles(B,K,L))
print("LNC angles:", tri_angles(L,N,C))
print("BMK angles:", tri_angles(B,M,K))
print("ACL angles:", tri_angles(A,C,L))
print()
print("KLC angles:", tri_angles(K,L,C))
print("BKM angles:", tri_angles(B,K,M))
print("AKL angles:", tri_angles(A,K,L))

print("\n--- detailed ---")
# ang BMK = gamma at M. Let's compute gamma and beta, alpha.
alpha = ang(K-B,A-B); beta=ang(L-B,K-B); gamma=ang(L-C,K-C)
print("alpha(deg)",np.degrees(alpha),"beta",np.degrees(beta),"gamma",np.degrees(gamma))
print("check alpha=ACL",np.degrees(ang(A-C,L-C)))
print("check beta=LNC",np.degrees(ang(L-N,C-N)))
print("check gamma=BMK",np.degrees(ang(B-M,K-M)))
