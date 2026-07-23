import numpy as np
from scipy.optimize import fsolve

A = np.array([0.0,0.0])
B = np.array([5.0,0.3])
C = np.array([1.2,4.0])
M=(A+B)/2; N=(A+C)/2

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

def circumcenter(P,Q,R):
    ax,ay=P; bx,by=Q; cx,cy=R
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux=((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy=((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

theta=0.35
sol,info,ier,msg = fsolve(equations,[1.6,1.1],args=(theta,),full_output=True)
t_full,s_full = sol
K,L = build_KL(theta,t_full,s_full)
O = circumcenter(A,K,L)
K1 = A+B-K
L1 = A+C-L

print("OK1:", np.linalg.norm(O-K1), " OL1:", np.linalg.norm(O-L1))
print("OK:", np.linalg.norm(O-K), " OL:", np.linalg.norm(O-L), " OA:", np.linalg.norm(O-A))
print("OM:", np.linalg.norm(O-M), " ON:", np.linalg.norm(O-N))
# is A,K1,L1 collinear with something? is O on line K1L1?
# check O, K1, L1 collinear:
v1 = K1-O; v2 = L1-O
cross = v1[0]*v2[1]-v1[1]*v2[0]
print("cross(O-K1,O-L1) [collinear check]:", cross)
# midpoint of K1L1 vs O
print("midpoint K1L1:", (K1+L1)/2, " O:", O)
