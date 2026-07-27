import numpy as np
from scipy.optimize import fsolve
import pickle
import sympy as sp

A = np.array([0.0,0.0])
B = np.array([5.0,0.3])
C = np.array([1.2,4.0])

def length(P,Q): return np.linalg.norm(Q-P)
a = length(B,C); b=length(C,A); c=length(A,B)

def angle_at(P,Q,R):
    u=Q-P; v=R-P
    cu=u/np.linalg.norm(u); cv=v/np.linalg.norm(v)
    return np.arccos(np.clip(np.dot(cu,cv),-1,1))

alpha0 = angle_at(A,B,C)

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

# get x = angle BAK (signed, using orientation), y = angle LAC
x_val = angle_between(B-A,K_full-A)  # unsigned; need sign consistent with our setup (should be positive, K "above" AB towards C)
y_val = angle_between(L_full-A, C-A)

print("x_val, y_val:", x_val, y_val)
print("alpha0:", alpha0)
print("theta:", theta)

sx_v, cx_v = np.sin(x_val), np.cos(x_val)
sy_v, cy_v = np.sin(y_val), np.cos(y_val)
St_v, Ct_v = np.sin(theta), np.cos(theta)
Sa_v, Ca_v = np.sin(alpha0), np.cos(alpha0)

with open('target_cleared.pkl','rb') as f:
    target_cleared, EqK, EqL, pythx, pythy, sx,cx,sy,cy_s,St,Ct,Sa,Ca,b_s,c_s = pickle.load(f)

subs = {sx:sx_v, cx:cx_v, sy:sy_v, cy_s:cy_v, St:St_v, Ct:Ct_v, Sa:Sa_v, Ca:Ca_v, b_s:b, c_s:c}

print("EqK value:", float(EqK.subs(subs)))
print("EqL value:", float(EqL.subs(subs)))
print("target_cleared value:", float(target_cleared.subs(subs)))
