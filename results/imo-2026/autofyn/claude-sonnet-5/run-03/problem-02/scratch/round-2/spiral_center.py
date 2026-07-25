import numpy as np
from scipy.optimize import fsolve

A = np.array([0.2, 3.1]); B = np.array([-2.0, 0.0]); C = np.array([3.5, -0.3])
M=(A+B)/2; N=(A+C)/2

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

def circumcenter(P1,P2,P3):
    ax,ay=P1; bx,by=P2; cx,cy=P3
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux=((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/d
    uy=((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/d
    return np.array([ux,uy])

def Qpoint():
    b=B-A; c=C-A
    num=np.dot(c-b,c+b); den=2*np.dot(c-b,c-b)
    return A+(num/den)*(c-b)
Q=Qpoint()

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

def to_c(P): return complex(P[0],P[1])
def to_pt(z): return np.array([z.real, z.imag])

Bc,Cc = to_c(B), to_c(C)
Ac = to_c(A)

print("Spiral similarity center S sending B->K, C->L: S = fixed point of z->alpha z+beta")
Ss = []
for theta_deg,K,L in family:
    Kc,Lc = to_c(K), to_c(L)
    alpha = (Kc-Lc)/(Bc-Cc)
    beta = Kc - alpha*Bc
    S = beta/(1-alpha)
    Ss.append((theta_deg, to_pt(S)))

for theta_deg, S in Ss[::15]:
    print(f"theta={theta_deg:6.1f}  S={S}")

# check: does S coincide with A? with Q? trace a line? a circle?
Spts = np.array([S for _,S in Ss])
print("\nDist(S,A) range:", np.linalg.norm(Spts-A,axis=1).min(), np.linalg.norm(Spts-A,axis=1).max())
print("Dist(S,Q) range:", np.linalg.norm(Spts-Q,axis=1).min(), np.linalg.norm(Spts-Q,axis=1).max())

# fit line to S locus
Amat = np.column_stack([Spts[:,0], np.ones(len(Spts))])
sol,_,_,_ = np.linalg.lstsq(Amat, Spts[:,1], rcond=None)
resid_line = Spts[:,1]-(Amat@sol)
print("S locus line fit residual max:", np.max(np.abs(resid_line)), "slope,intercept:", sol)
