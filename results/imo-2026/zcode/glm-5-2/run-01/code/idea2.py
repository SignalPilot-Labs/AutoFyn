import numpy as np
from scipy.optimize import fsolve
# Let me examine the numerical solution's structure to find a hidden relation.
# Take one solution and look at angles, similarities.

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

x,info,ier,msg = fsolve(eqs, [2,1,0.9,1], args=(0.9,), full_output=True)
K=x[:2]; L=x[2:]
O=circumcenter(A,K,L)
print("A",A); print("B",B); print("C",C); print("M",M); print("N",N)
print("K",K); print("L",L); print("O",O)
print("OM,ON",np.linalg.norm(O-M),np.linalg.norm(O-N))
print()

# Check: is O on perpendicular bisector of MN? 
# MN direction: N-M = c/2 - b/2 = (C-B)/2
print("O - midpoint(MN) =", O - (M+N)/2)
print("should be perp to (N-M)=",N-M," dot:", np.dot(O-(M+N)/2, N-M))

# Look at angles around O
print()
print("OAK angle:", np.degrees(ang(A-O,K-O)))
print("OKL angle:", np.degrees(ang(K-O,L-O)))
print("OLA angle:", np.degrees(ang(L-O,A-O)))
print("central angle AOL:", np.degrees(ang(A-O,L-O)))

# Distances
print()
print("OA",np.linalg.norm(O-A),"OK",np.linalg.norm(O-K),"OL",np.linalg.norm(O-L))
print("OM",np.linalg.norm(O-M),"ON",np.linalg.norm(O-N))
# Is OM=ON related to A? M,N are midpoints. Note OM=ON means O equidistant from midpoints of AB,AC.
# i.e. O on perp bisector of MN. Since MN || BC, this means O lies on line through midpoint of MN 
# perpendicular to BC. Midpoint of MN = (A + midpoint of BC)/... let's see M+N = (A+B+A+C)/2=A+(B+C)/2
# so (M+N)/2 = A/2 + (B+C)/4.

# Key: OA, OK, OL are circumradii of AKL. 
# Maybe there's relation: O is on perp bisector of MN  <=>  power of something?
