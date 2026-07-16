import numpy as np
from verify_config import find_KL_for_alpha
import cmath

# Build a valid CCW config, translate A to origin, go complex.
A=np.array([0.5,1.5]); B=np.array([0.0,0.0]); C=np.array([2.0,0.0])
alpha=np.radians(20)
K,L=find_KL_for_alpha(A,B,C,alpha)
def cx(P): return complex(P[0],P[1])
# translate A->0
a=cx(A)
b=cx(B)-a; c=cx(C)-a; k=cx(K)-a; l=cx(L)-a
bb,cc,kk,ll=b.conjugate(),c.conjugate(),k.conjugate(),l.conjugate()
def Im(z): return z.imag
print("CCW Im(bb*c)=",Im(bb*c),">0?")
print("K int: Im(bb*k)=",Im(bb*k),">0?")
print("L int: Im(cc*l)=",Im(cc*l),"<0?")
print("L Cside AB: Im(bb*l)=",Im(bb*l),">0?")
# directed angles
def arg(z): return cmath.phase(z)
t1=arg(-b/(k-b)); t2=arg((l-c)/(-c))
print("theta1=",np.degrees(t1),"in(0,pi)?",0<t1<np.pi)
print("theta2=",np.degrees(t2),"in(0,pi)?",0<t2<np.pi)
b1=arg((k-b)/(l-b)); b2=arg(c/(2*l-c))
print("beta1=",np.degrees(b1),"in(0,pi)?",0<b1<np.pi)
print("beta2=",np.degrees(b2),"in(0,pi)?",0<b2<np.pi)
g1=arg((k-c)/(l-c)); g2=arg((2*k-b)/b)
print("gamma1=",np.degrees(g1),"in(0,pi)?",0<g1<np.pi)
print("gamma2=",np.degrees(g2),"in(0,pi)?",0<g2<np.pi)
C1=b*c/((k-b)*(l-c)); C2=(k-b)*(2*l-c)/(c*(l-b)); C3=b*(k-c)/((l-c)*(2*k-b))
print("C1=",C1," arg=",np.degrees(arg(C1)))
print("C2=",C2," arg=",np.degrees(arg(C2)))
print("C3=",C3," arg=",np.degrees(arg(C3)))
print("arg(C1)==theta1-theta2?",abs(arg(C1)-(t1-t2))<1e-9)
print("arg(C2)==beta1-beta2?",abs(arg(C2)-(b1-b2))<1e-9)
print("arg(C3)==gamma1-gamma2?",abs(arg(C3)-(g1-g2))<1e-9)
