import numpy as np
from scipy.optimize import fsolve
import random

def angle(v1,v2):
    c = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    c = max(-1,min(1,c))
    return np.arccos(c)

random.seed(0)
a,b,cc = 2.0, 0.6, 0.8
A=np.array([0,0.]); B=np.array([a,0.]); C=np.array([b,cc])
M=(A+B)/2; N=(A+C)/2
angleABC = angle(A-B,C-B)
print("angleABC deg", np.degrees(angleABC))

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
    h2 = angle(L-B,K-B) - angle(L-N, C-N)
    h3 = angle(L-C,K-C) - angle(B-M, K-M)
    return [h2,h3, 0.0]

found=0
for _ in range(2000):
    t1_0 = random.uniform(0.05, 3)
    t2_0 = random.uniform(0.05, 3)
    beta0 = random.uniform(0.01, angleABC-0.01)
    sol, info, ier, msg = fsolve(lambda x: sysf(x), [t1_0,t2_0,beta0], full_output=True)
    if ier==1:
        t1,t2,beta = sol
        if t1>1e-4 and t2>1e-4 and 0<beta<angleABC:
            r = sysf(sol)
            if max(abs(np.array(r)))<1e-8:
                found+=1
                if found<=5:
                    print(sol, r)
print("found", found)
