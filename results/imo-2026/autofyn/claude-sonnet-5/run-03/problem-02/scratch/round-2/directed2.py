import numpy as np
from scipy.optimize import fsolve

A = np.array([0.2, 3.1]); B = np.array([-2.0, 0.0]); C = np.array([3.5, -0.3])
M = (A+B)/2; N = (A+C)/2

def ang(P,Q,R):
    u=Q-P; v=R-P
    return np.arccos(np.clip(np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v)),-1,1))
def rot(v,theta):
    c,s=np.cos(theta),np.sin(theta)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])
def K_of(theta,rK):
    d=(A-B)/np.linalg.norm(A-B); return B+rK*rot(d,-theta)
def L_of(theta,rL):
    d=(A-C)/np.linalg.norm(A-C); return C+rL*rot(d,theta)
def resid(x,theta):
    rK,rL=x; K=K_of(theta,rK); L=L_of(theta,rL)
    return [ang(B,L,K)-ang(N,L,C), ang(C,L,K)-ang(M,B,K)]
def dirang(P1,P2,P3,P4):
    v1=P2-P1; v2=P4-P3
    a1=np.arctan2(v1[1],v1[0]); a2=np.arctan2(v2[1],v2[0])
    return (a2-a1)%np.pi

family=[]
for theta_deg in np.linspace(5,60,120):
    theta=np.radians(theta_deg)
    for rK0 in [0.5,1.0,1.5]:
        for rL0 in [0.5,1.0,1.5]:
            sol,info,ier,msg=fsolve(resid,[rK0,rL0],args=(theta,),full_output=True)
            if ier==1 and sol[0]>0 and sol[1]>0:
                rK,rL=sol; K=K_of(theta,rK); L=L_of(theta,rL)
                family.append((theta_deg,K,L)); break
        else: continue
        break

def Qpoint():
    b=B-A; c=C-A
    num=np.dot(c-b,c+b); den=2*np.dot(c-b,c-b)
    return A+(num/den)*(c-b)
Q=Qpoint()

abc_angle_B = dirang(B,A,B,C)  # constant, direction AB to BC at B... just some fixed value
print("family size", len(family))

# test: is dirang(K,Q,K,M) constant across family? (K's view of Q relative to M)
for name, f in {
  "dirang(K,Q,K,M) const?": lambda K,L: dirang(K,Q,K,M),
  "dirang(L,Q,L,N) const?": lambda K,L: dirang(L,Q,L,N),
  "dirang(K,Q,K,B) const?": lambda K,L: dirang(K,Q,K,B),
  "dirang(L,Q,L,C) const?": lambda K,L: dirang(L,Q,L,C),
  "dirang(K,Q,K,A) const?": lambda K,L: dirang(K,Q,K,A),
  "dirang(L,Q,L,A) const?": lambda K,L: dirang(L,Q,L,A),
}.items():
    vals = [f(K,L) for _,K,L in family]
    vals = np.array(vals)
    print(f"{name:30s} mean={vals.mean():.4f} std={vals.std():.5f} min={vals.min():.4f} max={vals.max():.4f}")

print()
# test spiral similarity centered at L sending B->N with ratio; check angle BLN vs angle KLC (full similarity BLK ~ NLC?)
for theta_deg,K,L in family[::30]:
    angBLK = ang(L,B,K)
    angNLC = ang(L,N,C)
    LB=np.linalg.norm(L-B); LN=np.linalg.norm(L-N); LK=np.linalg.norm(L-K); LC=np.linalg.norm(L-C)
    print(f"theta={theta_deg:5.1f}  angBLK={np.degrees(angBLK):7.2f} angNLC={np.degrees(angNLC):7.2f}  LB/LN={LB/LN:.3f} LK/LC={LK/LC:.3f}")

print("\n--- Check collinearity A,Q,K and A,Q,L directly ---")
for theta_deg,K,L in family[::20]:
    # cross product test for collinearity of A,Q,K
    v1 = Q-A; v2 = K-A
    cross_AQK = v1[0]*v2[1]-v1[1]*v2[0]
    v3 = L-A
    cross_AQL = v1[0]*v3[1]-v1[1]*v3[0]
    angQKA = ang(K,Q,A)
    angQLA = ang(L,Q,A)
    print(f"theta={theta_deg:6.1f} cross(A,Q,K)={cross_AQK:9.5f} cross(A,Q,L)={cross_AQL:9.5f}  angQKA(deg)={np.degrees(angQKA):7.3f} angQLA(deg)={np.degrees(angQLA):7.3f}")
