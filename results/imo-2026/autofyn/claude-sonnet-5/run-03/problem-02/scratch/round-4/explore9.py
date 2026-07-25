import numpy as np
from scipy.optimize import fsolve
import random

def angle(v1,v2):
    n1=np.linalg.norm(v1); n2=np.linalg.norm(v2)
    if n1<1e-9 or n2<1e-9: return np.nan
    c = np.dot(v1,v2)/(n1*n2)
    c = max(-1,min(1,c))
    return np.arccos(c)

def inside_triangle(P,X,Y,Z):
    def sign(p1,p2,p3):
        return (p1[0]-p3[0])*(p2[1]-p3[1])-(p2[0]-p3[0])*(p1[1]-p3[1])
    d1=sign(P,X,Y); d2=sign(P,Y,Z); d3=sign(P,Z,X)
    has_neg = (d1<0) or (d2<0) or (d3<0)
    has_pos = (d1>0) or (d2>0) or (d3>0)
    return not (has_neg and has_pos)

random.seed(42)
total_genuine=0
min_m1=1e9; min_m2=1e9
worstcase=None
maxangle=0
for trial in range(120):
    a = random.uniform(0.5,3)
    b = random.uniform(-2,2.5)
    cc = random.uniform(0.3,3)
    if abs(a*(b**2+cc**2-a*b))<1e-4: continue
    A=np.array([0,0.]); B=np.array([a,0.]); C=np.array([b,cc])
    M=(A+B)/2; N=(A+C)/2
    angleABC = angle(A-B,C-B)
    if np.isnan(angleABC) or angleABC<0.05: continue
    def K_of(t1,beta): return B + t1*np.array([-np.cos(beta), np.sin(beta)])
    def L_of(t2,beta):
        AC=A-C; ell=np.linalg.norm(AC); d=AC/ell
        R=np.array([[np.cos(beta),-np.sin(beta)],[np.sin(beta),np.cos(beta)]])
        return C + t2*(R@d)
    def sysf(x):
        t1,t2,beta=x
        K=K_of(t1,beta); L=L_of(t2,beta)
        h2 = angle(L-B,K-B) - angle(L-N,C-N)
        h3 = angle(L-C,K-C) - angle(B-M,K-M)
        return [h2,h3]
    found_this=[]
    for _ in range(150):
        t1_0=random.uniform(0.05,3); t2_0=random.uniform(0.05,3)
        beta0=random.uniform(0.01, angleABC-0.01) if angleABC>0.02 else 0.01
        try:
            sol,info,ier,msg = fsolve(lambda x: sysf(x), [t1_0,t2_0,beta0], full_output=True)
        except Exception:
            continue
        if ier!=1: continue
        t1,t2,beta = sol
        if t1<1e-4 or t2<1e-4 or not(0<beta<angleABC): continue
        r = sysf(sol)
        if max(abs(np.array(r)))>1e-7: continue
        K=K_of(t1,beta); L=L_of(t2,beta)
        if not inside_triangle(K,B,M,C): continue
        if not inside_triangle(L,B,N,C): continue
        found_this.append((t1,t2,beta))
    for (t1,t2,beta) in found_this:
        total_genuine+=1
        ell = np.hypot(b,cc)
        m1 = a/2 - t1*np.cos(beta)
        m2 = ell/2 - t2*np.cos(beta)
        ang1 = angle(L_of(t2,beta)-B, K_of(t1,beta)-B)
        maxangle=max(maxangle, np.degrees(ang1))
        if m1<min_m1:
            min_m1=m1; worstcase=(a,b,cc,t1,t2,beta,'m1')
        if m2<min_m2:
            min_m2=m2

print("total genuine solutions:", total_genuine)
print("min margin1 (a/2 - t1 cosB):", min_m1, worstcase)
print("min margin2 (AC/2 - t2 cosB):", min_m2)
