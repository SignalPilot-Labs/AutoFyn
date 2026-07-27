import sympy as sp
B,C,beta,delta=sp.symbols('B C beta delta',real=True)
A=sp.pi-B-C
a=sp.Integer(1)
a2=2*a*sp.sin(B)*sp.sin(C)/sp.sin(A)
a1=-a+2*a*sp.sin(C)*sp.cos(B)/sp.sin(A)
den=sp.sin(A+2*beta+delta)
k2=2*a*sp.sin(B-beta)*sp.sin(C-beta-delta)/den
k1=-a+2*a*sp.sin(C-beta-delta)*sp.cos(B-beta)/den
htar=a*sp.cot(A+beta)
G=k1*(a1-k1)+(a2-k2)*(k2-htar)
F=sp.sin(C)*sp.sin(delta)*sp.sin(A+2*beta+delta)-2*sp.sin(A)*sp.sin(beta+delta)*sp.sin(C-beta-delta)
import random
random.seed(1)
f=sp.lambdify((B,C,beta,delta),G/F,'mpmath')
import mpmath as mp
mp.mp.dps=30
for _ in range(6):
    b=random.uniform(0.6,1.2);c=random.uniform(0.6,1.2);be=random.uniform(0.1,0.4);de=random.uniform(0.1,0.4)
    val=f(b,c,be,de)
    # guess: compare to various
    A_=mp.pi-b-c
    cand={'sin(A+2b+d)/(2 sinA)':mp.sin(A_+2*be+de)/(2*mp.sin(A_)),
          '1/(2 sin(A+b) sin? )':None}
    print(f"B={b:.3f} C={c:.3f} b={be:.3f} d={de:.3f} G/F={mp.nstr(val,12)}")
    print(f"   sin(A+2b+d)/(2 sinA sin(A+b))^? test... val*2*sinA*sin(A+b)^2/sin(A+2b+d)=",mp.nstr(val*2*mp.sin(A_)*mp.sin(A_+be)**2/mp.sin(A_+2*be+de),8))
