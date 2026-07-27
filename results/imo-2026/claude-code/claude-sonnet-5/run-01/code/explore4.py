import numpy as np
from scipy.optimize import brentq, fsolve

# triangle data
A = np.array([0.0,0.0])
B = np.array([5.0,0.3])
C = np.array([1.2,4.0])

def length(P,Q): return np.linalg.norm(Q-P)

a = length(B,C); b=length(C,A); c=length(A,B)

def angle_at(P,Q,R):
    # angle at vertex P formed by Q,R
    u=Q-P; v=R-P
    cu=u/np.linalg.norm(u); cv=v/np.linalg.norm(v)
    return np.arccos(np.clip(np.dot(cu,cv),-1,1))

alpha0 = angle_at(A,B,C)
beta0 = angle_at(B,A,C)
gamma0 = angle_at(C,A,B)
print("angles:",alpha0,beta0,gamma0, alpha0+beta0+gamma0, np.pi)

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

def angle_between(u,v):
    cu=u/np.linalg.norm(u); cv=v/np.linalg.norm(v)
    return np.arccos(np.clip(np.dot(cu,cv),-1,1))

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
beta_full = angle_between(L_full-B,K_full-B)
gamma_full = angle_between(L_full-C,K_full-C)
print("full 2D solve: t,s=",t_full,s_full,"beta=",beta_full,"gamma=",gamma_full)

# Now solve the decoupled 1-var equations analytically derived:
def CL_of_beta(beta):
    return a*np.sin(beta0-theta-beta)/np.sin(alpha0+2*theta+beta)

def eqI(beta):
    CL = CL_of_beta(beta)
    lhs = np.tan(beta)
    rhs = CL*np.sin(theta)/(b/2-CL*np.cos(theta))
    return lhs-rhs

def BK_of_gamma(gamma):
    return a*np.sin(gamma0-theta-gamma)/np.sin(alpha0+2*theta+gamma)

def eqII(gamma):
    BK = BK_of_gamma(gamma)
    lhs = np.tan(gamma)
    rhs = BK*np.sin(theta)/(c/2-BK*np.cos(theta))
    return lhs-rhs

beta_sol = brentq(eqI, 0.001, beta0-theta-0.001)
gamma_sol = brentq(eqII, 0.001, gamma0-theta-0.001)
print("decoupled solve: beta=",beta_sol,"gamma=",gamma_sol)

print("diff beta:", beta_sol-beta_full)
print("diff gamma:", gamma_sol-gamma_full)
