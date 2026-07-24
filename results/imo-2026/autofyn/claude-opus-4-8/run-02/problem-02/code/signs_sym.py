import sympy as sp
p,q,a,s,tK,tL = sp.symbols('p q a s tK tL', positive=True)  # q,s,tK,tL>0 ; a>0
B=sp.Matrix([0,0]); C=sp.Matrix([a,0]); A=sp.Matrix([p,q])
M=(A+B)/2; N=(A+C)/2
u  = sp.Matrix([ p*(1-s**2)+q*(2*s), -p*(2*s)+q*(1-s**2) ])
dL = sp.Matrix([ (p-a)*(1-s**2)-q*(2*s), (p-a)*(2*s)+q*(1-s**2) ])
K = tK*u ;  L = C + tL*dL
def cross(V,W): return sp.expand(V[0]*W[1]-V[1]*W[0])
w=1+s**2
print("cross(MB,MK) =", sp.factor(cross(B-M,K-M)))
print("cross(CL,CK) =", sp.factor(cross(L-C,K-C)))
print("cross(BL,BK) =", sp.factor(cross(L-B,K-B)))
print("cross(NL,NC) =", sp.factor(cross(L-N,C-N)))
