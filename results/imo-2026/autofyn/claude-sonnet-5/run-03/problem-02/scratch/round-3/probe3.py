import numpy as np
from scipy.optimize import fsolve

A = np.array([0.3, 2.7]); B = np.array([-1.5, 0.0]); C = np.array([2.2, 0.1])
M = (A+B)/2; N = (A+C)/2

def ang(P, Q, R):
    u = Q-P; v = R-P
    cosv = np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))
    return np.arccos(np.clip(cosv,-1,1))

def rot(v, theta):
    c,s = np.cos(theta), np.sin(theta)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])

def K_of(theta, rK):
    d = rot((A-B)/np.linalg.norm(A-B), -theta)
    return B + rK*d
def L_of(theta, rL):
    d = rot((A-C)/np.linalg.norm(A-C), theta)
    return C + rL*d

def resid(x, theta):
    rK, rL = x
    K = K_of(theta, rK); L = L_of(theta, rL)
    return [ang(B,L,K)-ang(N,L,C), ang(C,L,K)-ang(M,B,K)]

def inside_triangle(P,X,Y,Z):
    def sign(p1,p2,p3): return (p1[0]-p3[0])*(p2[1]-p3[1])-(p2[0]-p3[0])*(p1[1]-p3[1])
    d1=sign(P,X,Y);d2=sign(P,Y,Z);d3=sign(P,Z,X)
    return not((d1<0 or d2<0 or d3<0) and (d1>0 or d2>0 or d3>0))
def between_rays(P,X,Y,T):
    ux,uy=X-P; vx,vy=Y-P; tx,ty=T-P
    def cross(a,b,c,d): return a*d-b*c
    c1=cross(ux,uy,tx,ty); c2=cross(tx,ty,vx,vy); c3=cross(ux,uy,vx,vy)
    return (c1*c3>=-1e-9) and (c2*c3>=-1e-9)

good=[]
seen={}
for theta_deg in np.linspace(5,80,200):
    theta=np.radians(theta_deg)
    for rK0 in [0.5,1.0,1.5,2.0]:
        for rL0 in [0.5,1.0,1.5,2.0]:
            sol,info,ier,msg = fsolve(resid,[rK0,rL0],args=(theta,),full_output=True,xtol=1e-13)
            if ier==1 and sol[0]>0 and sol[1]>0:
                K=K_of(theta,sol[0]); L=L_of(theta,sol[1])
                if inside_triangle(K,B,M,C) and inside_triangle(L,B,N,C):
                    key=round(theta_deg,3)
                    if key not in seen: seen[key]=(K,L)
for k in sorted(seen):
    K,L = seen[k]
    if between_rays(B,L,A,K) and between_rays(C,A,K,L):
        good.append((k,K,L))
print(len(good),"valid")

def circumcenter(P,Q,R):
    ax,ay=P;bx,by=Q;cx,cy=R
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux=((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy=((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

def inv(P,r2=1.0):
    v=np.array(P)-A; d2=np.dot(v,v)
    return A+(r2/d2)*v

def circle_fit_relresid(P1,P2,P3,P4):
    O=circumcenter(P1,P2,P3)
    R=np.linalg.norm(P1-O)
    d4=np.linalg.norm(P4-O)
    return abs(d4-R)/R

print("\n--- normalized (relative) concyclicity residual: K*,L*,B*,C* ---")
for k,K,L in good[::20]:
    Ks=inv(K); Ls=inv(L); Bs=inv(B); Cs=inv(C)
    print(f"theta={k:.2f} relresid={circle_fit_relresid(Ks,Ls,Bs,Cs):.6e}")

print("\n--- normalized: M*,N*,K*,L* ---")
for k,K,L in good[::20]:
    Ks=inv(K); Ls=inv(L); Ms=inv(M); Ns=inv(N)
    print(f"theta={k:.2f} relresid={circle_fit_relresid(Ms,Ns,Ks,Ls):.6e}")

# calibrate noise floor using a KNOWN true fact: A,M,N,Q concyclic
b=B-A; c=C-A
Qshift=(np.dot(c-b,c+b))/(2*np.dot(c-b,c-b))*(c-b)
Q=A+Qshift
print("\n--- calibration: known-true A,M,N,Q concyclic relative residual (should be ~1e-10 to 1e-13) ---")
print(circle_fit_relresid(A,M,N,Q))

print("\n--- known-true A,K,L,Q concyclic (established gap) relative residual, few thetas ---")
for k,K,L in good[::20]:
    print(f"theta={k:.2f} relresid={circle_fit_relresid(A,K,L,Q):.6e}")

print("\n--- Test: B,K,L,C concyclic? ---")
for k,K,L in good[::20]:
    print(f"theta={k:.2f} relresid={circle_fit_relresid(B,K,L,C):.6e}")

print("\n--- Test: K,L,M,N concyclic? ---")
for k,K,L in good[::20]:
    print(f"theta={k:.2f} relresid={circle_fit_relresid(K,L,M,N):.6e}")

print("\n--- Test: does line KL pass through a fixed point? print KL line params (a,b,c) normalized ---")
def line_through(P,Q):
    a = Q[1]-P[1]; b = P[0]-Q[0]; c = -(a*P[0]+b*P[1])
    norm = np.hypot(a,b)
    return a/norm,b/norm,c/norm
for k,K,L in good[::15]:
    a,b,c = line_through(K,L)
    print(f"theta={k:.2f} line KL: {a:.4f} x + {b:.4f} y + {c:.4f} = 0")

print("\n--- Test: midpoint of KL vs O, vs midpoint MN ---")
midMN = (M+N)/2
for k,K,L in good[::20]:
    O = circumcenter(A,K,L)
    midKL = (K+L)/2
    print(f"theta={k:.2f} midKL={midKL} O={O} midMN={midMN}")
