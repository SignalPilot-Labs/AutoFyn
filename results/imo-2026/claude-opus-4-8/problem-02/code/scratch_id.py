import numpy as np
from verify_config import find_KL_for_alpha, circumcenter, angle_at

A = np.array([0.5,1.5]); B=np.array([0.0,0.0]); C=np.array([2.0,0.0])
M=(A+B)/2; N=(A+C)/2

def check(A,B,C,alpha_deg):
    alpha=np.radians(alpha_deg)
    res=find_KL_for_alpha(A,B,C,alpha)
    if res is None: return
    K,L=res
    Aang=angle_at(A,B,C); Bang=angle_at(B,A,C); Cang=angle_at(C,A,B)
    al=angle_at(B,K,A); beta=angle_at(B,L,K); gamma=angle_at(C,L,K)
    sa,ca=np.sin(al),np.cos(al); sb,cb=np.sin(beta),np.cos(beta); sg,cg=np.sin(gamma),np.cos(gamma)
    sB,cB=np.sin(Bang),np.cos(Bang); sC,cC=np.sin(Cang),np.cos(Cang)
    sA=np.sin(Aang); cA=np.cos(Aang)
    # PC, PB, N_C^2, N_B^2
    PC=sC*(ca*sb+2*sa*cb)+cC*sa*sb
    PB=sB*(ca*sg+2*sa*cg)+cB*sa*sg
    NC2=sg**2+4*sa*cg*np.sin(al+gamma)
    NB2=sb**2+4*sa*cb*np.sin(al+beta)
    # W
    W=sA*((ca*sg+2*sa*cg)*(ca*sb+2*sa*cb)-sa**2*sg*sb) - cA*(sa*sg*(ca*sb+2*sa*cb)+(ca*sg+2*sa*cg)*sa*sb)
    sab=np.sin(al+beta); sag=np.sin(al+gamma)
    # (5): sC PC sab NC2 - sB PB sag NB2 = sin(C-B) W sag sab
    lhs=sC*PC*sab*NC2 - sB*PB*sag*NB2
    rhs=np.sin(Cang-Bang)*W*sag*sab
    # constraints
    I=sC*sg*np.sin(Aang+2*al+gamma)-2*sA*np.sin(Cang-al-gamma)*sag
    II=sB*sb*np.sin(Aang+2*al+beta)-2*sA*np.sin(Bang-al-beta)*sab
    print(f"a={alpha_deg:5.1f}  (5)LHS={lhs:.6f} RHS={rhs:.6f} diff={lhs-rhs:.2e}  I={I:.1e} II={II:.1e}")

for ad in [5,10,15,20,25,30]:
    check(A,B,C,ad)
# second triangle
A2=np.array([1.0,2.0]);B2=np.array([0.0,0.0]);C2=np.array([3.0,0.0])
print("triangle2")
for ad in [5,12,20]:
    check(A2,B2,C2,ad)
