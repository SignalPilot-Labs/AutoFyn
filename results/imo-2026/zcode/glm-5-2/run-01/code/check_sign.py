import numpy as np, math
A=np.array([0.0,0.0]);B=np.array([1.0,0.0]);C=np.array([0.25,0.75])
M=(A+B)/2;N=(A+C)/2
# recompute K,L
from scipy.optimize import fsolve
def ang(v1,v2):
    c=np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)+1e-300)
    return np.arccos(max(-1,min(1,c)))
def eqs(vars):
    kx,ky,lx,ly=vars;K=np.array([kx,ky]);L=np.array([lx,ly])
    return [ang(K-B,A-B)-ang(A-C,L-C), ang(L-B,K-B)-ang(L-N,C-N), ang(L-C,K-C)-ang(B-M,K-M), kx-0.6]
x=fsolve(eqs,[0.6,0.2,0.3,0.5]); K=x[:2];L=x[2:]
print("K",K,"L",L)
def cross(u,v):return u[0]*v[1]-u[1]*v[0]
def dot(u,v):return u[0]*v[0]+u[1]*v[1]
# angle LNC: NL=L-N, NC=C-N
NL=L-N; NC=C-N
print("cross(NL,NC)=",cross(NL,NC)," dot(NL,NC)=",dot(NL,NC)," tan(beta)=",math.tan(math.radians(21.08047146055647)))
print("ratio cross/dot=",cross(NL,NC)/dot(NL,NC))
# So sign: is cross/dot = +tan(beta) or -tan(beta)?
print()
# angle BMK: MB=B-M, MK=K-M
MB=B-M; MK=K-M
print("cross(MB,MK)=",cross(MB,MK)," dot=",dot(MB,MK)," tan(gamma)=",math.tan(math.radians(35.582220333404194)))
print("ratio=",cross(MB,MK)/dot(MB,MK))
