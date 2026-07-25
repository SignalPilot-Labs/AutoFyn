import numpy as np
from scipy.optimize import fsolve
def ang(v1, v2):
    c = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)+1e-300)
    return np.arccos(max(-1.0,min(1.0,c)))
A = np.array([0.0,0.0]); B = np.array([1.0,0.0]); C = np.array([0.25,0.75])
M=(A+B)/2; N=(A+C)/2
def circumcenter(A,K,L):
    ax,ay=A; kx,ky=K; lx,ly=L
    D=2*(ax*(ky-ly)+kx*(ly-ay)+lx*(ay-ky))
    ux=((ax**2+ay**2)*(ky-ly)+(kx**2+ky**2)*(ly-ay)+(lx**2+ly**2)*(ay-ky))/D
    uy=((ax**2+ay**2)*(lx-kx)+(kx**2+ky**2)*(ax-lx)+(lx**2+ly**2)*(kx-ax))/D
    return np.array([ux,uy])
def eqs(vars):
    kx,ky,lx,ly=vars; K=np.array([kx,ky]);L=np.array([lx,ly])
    e1=ang(K-B,A-B)-ang(A-C,L-C); e2=ang(L-B,K-B)-ang(L-N,C-N); e3=ang(L-C,K-C)-ang(B-M,K-M)
    # 4th: pin via a parameter, use ang BMK ... no, add natural: angle LBK extra? 
    # Actually 3 eqs 4 unknowns. Pin kx.
    return [e1,e2,e3, kx-0.6]
x=fsolve(eqs,[0.6,0.2,0.3,0.5],full_output=True)
K=x[0][:2];L=x[0][2:]
O=circumcenter(A,K,L)
print("K",K,"L",L)
print("OM,ON",np.linalg.norm(O-M),np.linalg.norm(O-N))
def dirang(v): return np.degrees(np.arctan2(v[1],v[0]))
print("\nRay directions (degrees):")
print("BA from B:", dirang(A-B))
print("BK from B:", dirang(K-B), " ang KBA=",np.degrees(ang(K-B,A-B)))
print("BL from B:", dirang(L-B), " ang LBK=",np.degrees(ang(L-B,K-B))," ang LBA=",np.degrees(ang(L-B,A-B)))
print("BC from B:", dirang(C-B))
print()
print("CA from C:", dirang(A-C))
print("CL from C:", dirang(L-C), " ang ACL=",np.degrees(ang(A-C,L-C)))
print("CK from C:", dirang(K-C), " ang LCK=",np.degrees(ang(L-C,K-C))," ang ACK=",np.degrees(ang(A-C,K-C)))
print("CB from C:", dirang(B-C))
print()
alpha=np.degrees(ang(K-B,A-B));beta=np.degrees(ang(L-B,K-B));gamma=np.degrees(ang(L-C,K-C))
print(f"alpha={alpha:.4f} beta={beta:.4f} gamma={gamma:.4f}")
# Verify: BK angle = (pi - alpha) since BA angle=180.
print(f"predicted BK angle = {180-alpha:.4f}, actual {dirang(K-B):.4f}")
print(f"predicted BL angle = {180-alpha-beta:.4f}, actual {dirang(L-B):.4f}")
# CA angle:
ca=dirang(A-C)
print(f"CA angle = {ca:.4f}")
print(f"predicted CL angle = CA+alpha = {ca+alpha:.4f} or CA-alpha={ca-alpha:.4f}, actual {dirang(L-C):.4f}")
print(f"predicted CK angle = CL+gamma, actual {dirang(K-C):.4f}")
