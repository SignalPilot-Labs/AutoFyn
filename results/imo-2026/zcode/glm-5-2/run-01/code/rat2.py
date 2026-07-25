import sympy as sp
from sympy import symbols, expand, groebner, Rational, simplify, Matrix

p,q = symbols('p q', positive=True)
A,P,G = symbols('A P G', positive=True)  # tan(alpha/2), tan((alpha+beta)/2), tan((alpha+gamma)/2)
one = sp.Integer(1)

def rot_half(v, t):
    # rotate vector v=(x,y) by angle with tan(half)=t: cos=(1-t^2)/(1+t^2), sin=2t/(1+t^2)
    x,y = v
    c = (1-t**2)/(1+t**2); s = 2*t/(1+t**2)
    return (expand(c*x - s*y), expand(s*x + c*y))

# BA direction from B = (-1, 0). 
BA = (-one, sp.Integer(0))
dir_BK = rot_half(BA, A)   # rot by alpha
dir_BL = rot_half(BA, P)   # rot by alpha+beta
# CA direction from C = (-p,-q).
CA = (-p,-q)
dir_CL = rot_half(CA, A)   # rot by alpha
dir_CK = rot_half(CA, G)   # rot by alpha+gamma
dir_BK = (expand(dir_BK[0]), expand(dir_BK[1]))
dir_BL = (expand(dir_BL[0]), expand(dir_BL[1]))
dir_CL = (expand(dir_CL[0]), expand(dir_CL[1]))
dir_CK = (expand(dir_CK[0]), expand(dir_CK[1]))

def cross(u,v): return expand(u[0]*v[1]-u[1]*v[0])
def dot(u,v): return expand(u[0]*v[0]+u[1]*v[1])

# Intersections. K = B + t*dir_BK, also = C + u*dir_CK.
# t*dir_BK - u*dir_CK = C - B = (p-1, q)
def intersect(d1,d2,W):
    # t d1 - u d2 = W  =>  t = cross(W,d2)/cross(d1,d2)
    return cross(W,d2), cross(d1,d2)
W = (p-1, q)
tK_num, tK_den = intersect(dir_BK, dir_CK, W)
tK_num=expand(tK_num); tK_den=expand(tK_den)
K = (expand(1 + tK_num*dir_BK[0]), expand(tK_num*dir_BK[1]))  # over tK_den
# Keep K as (Kx/tK_den, Ky/tK_den) common denom
Kx=K[0]; Ky=K[1]

tL_num, tL_den = intersect(dir_BL, dir_CL, W)
tL_num=expand(tL_num); tL_den=expand(tL_den)
L=(expand(1 + tL_num*dir_BL[0]), expand(tL_num*dir_BL[1]))
Lx=L[0]; Ly=L[1]
# Note tK_den should equal tL_den? cross(dir_BK,dir_CK) vs cross(dir_BL,dir_CL) - different.
# K expressed with denom tK_den, L with denom tL_den.
print("tK_den:", tK_den)
print("tL_den:", tL_den)
print("Kx (num):", expand(Kx))
print("Ky (num):", expand(Ky))
sp.save = None
import pickle
with open('/tmp/geom/kl.pkl','wb') as f:
    pickle.dump(dict(Kx=Kx,Ky=Ky,Lx=Lx,Ly=Ly,tKden=tK_den,tLden=tL_den,p=str(p),q=str(q),A=str(A),P=str(P),G=str(G)),f)
print("saved")
