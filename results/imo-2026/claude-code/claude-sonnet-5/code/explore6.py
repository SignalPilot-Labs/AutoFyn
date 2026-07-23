import numpy as np
from scipy.optimize import fsolve

A = np.array([0.0,0.0])
B = np.array([5.0,0.3])
C = np.array([1.2,4.0])

M=(A+B)/2
N=(A+C)/2

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

theta=0.35
sol,info,ier,msg = fsolve(equations,[1.6,1.1],args=(theta,),full_output=True)
t_full,s_full = sol
K_full,L_full = build_KL(theta,t_full,s_full)

def circumcenter(P,Q,R):
    ax,ay=P; bx,by=Q; cx,cy=R
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux=((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy=((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

# Hypothesis: circle through B, N tangent to line AC at N. Check if L lies on it.
# center of that circle lies on line through N perpendicular to AC, and also on perpendicular bisector of BN.
dirAC = (C-A)/np.linalg.norm(C-A)
perp_at_N_dir = np.array([-dirAC[1], dirAC[0]])
# center = N + r*perp_at_N_dir, also equidistant from B: |center-B| = |center - N| = r
# solve for r: (N + r*perp - B).(N+r*perp-B) = r^2
NB = N-B
# |NB + r*perp|^2 = r^2  => NB.NB + 2r NB.perp + r^2 perp.perp = r^2 ; perp.perp=1
r = -(np.dot(NB,NB))/(2*np.dot(NB,perp_at_N_dir))
center = N + r*perp_at_N_dir
radius = abs(r)
print("center",center,"radius",radius, "check |center-N|",np.linalg.norm(center-N),"check |center-B|",np.linalg.norm(center-B))
distL = np.linalg.norm(center-L_full)
print("dist(center,L_full) =", distL, " vs radius=",radius)
