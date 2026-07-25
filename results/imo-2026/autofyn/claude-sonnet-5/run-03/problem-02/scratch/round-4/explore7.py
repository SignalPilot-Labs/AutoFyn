import numpy as np
from scipy.optimize import fsolve
import random

def angle(v1,v2):
    c = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    c = max(-1,min(1,c))
    return np.arccos(c)

def solve_triangle(a,b,cc, tries=60):
    A=np.array([0,0.]); B=np.array([a,0.]); C=np.array([b,cc])
    M=(A+B)/2; N=(A+C)/2
    angleABC = angle(A-B, C-B)
    def K_of(t1,beta):
        return B + t1*np.array([-np.cos(beta), np.sin(beta)])
    def L_of(t2,beta):
        AC = A-C
        ell = np.linalg.norm(AC)
        d = AC/ell
        R = np.array([[np.cos(beta),-np.sin(beta)],[np.sin(beta),np.cos(beta)]])
        return C + t2*(R@d)
    def sysf(x):
        t1,t2,beta = x
        K = K_of(t1,beta); L = L_of(t2,beta)
        # hyp1 encoded via beta param already (angle KBA = angle ACL = beta) -- built into K_of, L_of def
        h2 = angle(L-B,K-B) - angle(L-N, C-N)
        h3 = angle(L-C,K-C) - angle(B-M, K-M)
        h1check = 0.0  # trivially satisfied by construction
        return [h2,h3,h1check]
    sols=[]
    for _ in range(tries):
        t1_0 = random.uniform(0.1, max(a,1)*1.5)
        t2_0 = random.uniform(0.1, np.hypot(b,cc)*1.5)
        beta0 = random.uniform(0.01, angleABC-0.01) if angleABC>0.02 else random.uniform(0.01,0.5)
        x0=[t1_0,t2_0,beta0]
        try:
            sol, info, ier, msg = fsolve(lambda x: sysf(x)+[0], x0[:2]+[x0[2]], full_output=True)
        except Exception:
            continue
        if ier!=1: continue
        t1,t2,beta = sol
        if t1<=1e-6 or t2<=1e-6: continue
        if not (0<beta<np.pi): continue
        K=K_of(t1,beta); L=L_of(t2,beta)
        # containment checks
        def inside_triangle(P,X,Y,Z):
            def sign(p1,p2,p3):
                return (p1[0]-p3[0])*(p2[1]-p3[1])-(p2[0]-p3[0])*(p1[1]-p3[1])
            d1=sign(P,X,Y); d2=sign(P,Y,Z); d3=sign(P,Z,X)
            has_neg = (d1<0) or (d2<0) or (d3<0)
            has_pos = (d1>0) or (d2>0) or (d3>0)
            return not (has_neg and has_pos)
        if not inside_triangle(K,B,M,C): continue
        if not inside_triangle(L,B,N,C): continue
        sols.append((t1,t2,beta,K,L))
    return sols, A,B,C,M,N

random.seed(0)
min_margin_bmk = 1e9
min_margin_nlnc = 1e9
worst = None
count=0
for trial in range(60):
    a = random.uniform(0.5,3)
    b = random.uniform(-2,2.5)
    cc = random.uniform(0.3,3)
    # ensure nondeg triangle
    if abs(a*(b**2+cc**2-a*b))<1e-6: continue
    sols, A,B,C,M,N = solve_triangle(a,b,cc, tries=40)
    for (t1,t2,beta,K,L) in sols:
        count+=1
        bmk = a*(a-2*t1*np.cos(beta))/4
        ell2 = b**2+cc**2
        nlnc = ell2*(1-2*(t2/np.sqrt(ell2))*np.cos(beta))/4
        margin1 = a/2 - t1*np.cos(beta)   # want >0
        margin2 = np.sqrt(ell2)/2 - t2*np.cos(beta)  # want >0
        if margin1 < min_margin_bmk:
            min_margin_bmk = margin1
            worst = (a,b,cc,t1,t2,beta,'BMK')
        if margin2 < min_margin_nlnc:
            min_margin_nlnc = margin2
            worst2=(a,b,cc,t1,t2,beta,'NLNC')

print("genuine solutions found:", count)
print("min margin (a/2 - t1 cosβ):", min_margin_bmk, worst)
print("min margin (AC/2 - t2 cosβ):", min_margin_nlnc)
