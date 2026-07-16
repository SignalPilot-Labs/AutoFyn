import numpy as np
from verify_config import find_KL_for_alpha, circumcenter, angle_at

# Pick a scalene triangle and a valid alpha
A = np.array([0.5,1.5]); B=np.array([0.0,0.0]); C=np.array([2.0,0.0])
M=(A+B)/2; N=(A+C)/2

def report(A,B,C,alpha_deg):
    alpha=np.radians(alpha_deg)
    res=find_KL_for_alpha(A,B,C,alpha)
    if res is None:
        print("no sol",alpha_deg); return
    K,L=res
    O=circumcenter(A,K,L)
    OM=np.linalg.norm(O-M); ON=np.linalg.norm(O-N)
    # triangle angles
    a=np.linalg.norm(B-C); b=np.linalg.norm(A-C); c=np.linalg.norm(A-B)
    Aang=angle_at(A,B,C); Bang=angle_at(B,A,C); Cang=angle_at(C,A,B)
    R=a/(2*np.sin(Aang))
    # measured alpha,beta,gamma
    al=angle_at(B,K,A)  # KBA
    al2=angle_at(C,A,L) # ACL
    beta=angle_at(B,L,K)
    gamma=angle_at(C,L,K)
    # phi=KAB, psi=LAC
    phi=angle_at(A,K,B)
    psi=angle_at(A,L,C)
    lamA=angle_at(A,K,L)
    k=np.linalg.norm(K-A); l=np.linalg.norm(L-A)
    print(f"alpha={alpha_deg:.2f} OM={OM:.6f} ON={ON:.6f} diff={abs(OM-ON):.1e}")
    print(f"  A,B,C deg={np.degrees(Aang):.3f},{np.degrees(Bang):.3f},{np.degrees(Cang):.3f} R={R:.4f}")
    print(f"  alpha={np.degrees(al):.3f}={np.degrees(al2):.3f} beta={np.degrees(beta):.3f} gamma={np.degrees(gamma):.3f}")
    print(f"  phi={np.degrees(phi):.3f} psi={np.degrees(psi):.3f} lamA={np.degrees(lamA):.3f}  A-phi-psi={np.degrees(Aang-phi-psi):.3f}")
    print(f"  b={b:.4f} c={c:.4f} k=AK={k:.4f} l=AL={l:.4f}")
    # check cot phi = cot al + 2 cot gamma
    print(f"  cotphi={1/np.tan(phi):.4f} vs cotal+2cotgam={1/np.tan(al)+2/np.tan(gamma):.4f}")
    print(f"  cotpsi={1/np.tan(psi):.4f} vs cotal+2cotbeta={1/np.tan(al)+2/np.tan(beta):.4f}")
    # check AK = c sin al/sin(al+phi)
    print(f"  k check={c*np.sin(al)/np.sin(al+phi):.4f}  l check={b*np.sin(al)/np.sin(al+psi):.4f}")
    # constraint I: sinC sin gam sin(A+2al+gam)=2 sinA sin(C-al-gam) sin(al+gam)
    I_l=np.sin(Cang)*np.sin(gamma)*np.sin(Aang+2*al+gamma)
    I_r=2*np.sin(Aang)*np.sin(Cang-al-gamma)*np.sin(al+gamma)
    II_l=np.sin(Bang)*np.sin(beta)*np.sin(Aang+2*al+beta)
    II_r=2*np.sin(Aang)*np.sin(Bang-al-beta)*np.sin(al+beta)
    print(f"  (I): {I_l:.5f} vs {I_r:.5f}   (II): {II_l:.5f} vs {II_r:.5f}")
    # simplification: c sin(A-psi)+b sin psi = 2R sinA sin(C+psi)
    lhs1=c*np.sin(Aang-psi)+b*np.sin(psi); rhs1=2*R*np.sin(Aang)*np.sin(Cang+psi)
    lhs2=c*np.sin(phi)+b*np.sin(Aang-phi); rhs2=2*R*np.sin(Aang)*np.sin(Bang+phi)
    print(f"  simp1 {lhs1:.5f} vs {rhs1:.5f}   simp2 {lhs2:.5f} vs {rhs2:.5f}")
    # (star star): k sin(C+psi) - l sin(B+phi) = R sin(C-B) sin(A-phi-psi)
    LL=k*np.sin(Cang+psi)-l*np.sin(Bang+phi)
    RR=R*np.sin(Cang-Bang)*np.sin(Aang-phi-psi)
    print(f"  (**) {LL:.6f} vs {RR:.6f}")
    # final: cd-be=(c^2-b^2)/2 where d=AA'=2u.O, e=2v.O  (A at origin frame). Use O directly:
    # d = 2*u.(O-A), u=unit(B-A)
    u=(B-A)/c; v=(C-A)/b
    d=2*np.dot(u,O-A); e=2*np.dot(v,O-A)
    print(f"  cd-be={c*d-b*e:.6f} vs (c^2-b^2)/2={(c**2-b**2)/2:.6f}")
    # numerator formula check
    numer=k*(c*np.sin(Aang-psi)+b*np.sin(psi))-l*(c*np.sin(phi)+b*np.sin(Aang-phi))
    print(f"  numer/sin lamA={numer/np.sin(Aang-phi-psi):.6f} vs cd-be={c*d-b*e:.6f}")

for ad in [5,10,15,20,25]:
    report(A,B,C,ad)
