import numpy as np, math
def ord_angle(p,q):
    cr=p[0]*q[1]-p[1]*q[0]; dt=p[0]*q[0]+p[1]*q[1]
    return np.arctan2(abs(cr),dt)
# verified config from power-secant-product: A=(0,0),B=(4,0),C=(1,3),
# K=(2.8,0.49465), L=(1.0479,2.3099)
A=(0,0);B=(4,0);C=(1,3);M=(2,0);N=(0.5,1.5);K=(2.8,0.49465);L=(1.0479,2.3099)
A_ang=ord_angle((4,0),(1,3))
B_ang=ord_angle((-4,0),(-3,3))
C_ang=math.pi-A_ang-B_ang
BK=(K[0]-4,K[1]); BA=(-4,0); alpha=ord_angle(BK,BA)
BL=(L[0]-4,L[1]); beta=ord_angle(BL,BK)
CL3=(L[0]-1,L[1]-3); CK=(K[0]-1,K[1]-3); MB=(2,0); MK=(K[0]-2,K[1])
gamma=ord_angle(CL3,CK)
print(f"A={math.degrees(A_ang):.4f} B={math.degrees(B_ang):.4f} C={math.degrees(C_ang):.4f}")
print(f"alpha={math.degrees(alpha):.4f} beta={math.degrees(beta):.4f} gamma={math.degrees(gamma):.4f}")
print(f"alpha+gamma={math.degrees(alpha+gamma):.4f} vs C={math.degrees(C_ang):.4f} (need <)")
print(f"alpha+beta={math.degrees(alpha+beta):.4f} vs B={math.degrees(B_ang):.4f} (need <)")
lhs=2*math.sin(A_ang)*math.sin(C_ang-alpha-gamma)*math.sin(alpha+gamma)
rhs=math.sin(C_ang)*math.sin(gamma)*math.sin(A_ang+2*alpha+gamma)
print(f"(C1) corrected: lhs={lhs:.6f} rhs={rhs:.6f} resid={abs(lhs-rhs):.2e}")
lhs_w=2*math.sin(A_ang)*math.sin(alpha+gamma-C_ang)*math.sin(alpha+gamma)
print(f"(C1) wrong: lhs_w={lhs_w:.6f} (vs rhs {rhs:.6f}) resid={abs(lhs_w-rhs):.2e}")
lhs2=2*math.sin(A_ang)*math.sin(B_ang-alpha-beta)*math.sin(alpha+beta)
rhs2=math.sin(B_ang)*math.sin(beta)*math.sin(A_ang+2*alpha+beta)
print(f"(C2) corrected: resid={abs(lhs2-rhs2):.2e}")
