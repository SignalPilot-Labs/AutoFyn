"""Investigate the rotation centered at S on perp-bis(MN) sending M->N and L->K.
Does it send A to A* (the A-star of the cyclicity route)? If so, that connects to O."""
import numpy as np, sys
sys.path.insert(0,'/tmp/round-1')
from gate import sub, cross2, circumcenter, spiral_center, perp_bis_dist, build_KL

def D_mid_BC_foot(A,B,C):
    # A* = A + (D - F), D = midpoint BC, F = foot of altitude from A to BC
    A=np.array(A,dtype=float);B=np.array(B,dtype=float);C=np.array(C,dtype=float)
    D=(B+C)/2
    BC=C-B; t=np.dot(A-B,BC)/np.dot(BC,BC)
    F=B+t*BC
    return A+(D-F)

triangles = [
    ("scalene1", [0,0],[4,0],[1,3]),
    ("scalene2", [0,0],[5,0],[2,4]),
    ("right",    [0,0],[6,0],[0,4]),
    ("random",   [0,0],[5,0],[3,2]),
]
for name,A,B,C in triangles:
    A=np.array(A,dtype=float);B=np.array(B,dtype=float);C=np.array(C,dtype=float)
    M=(A+B)/2; N=(A+C)/2
    Astar=D_mid_BC_foot(A,B,C)
    print(f"\n{name}: A*={Astar.round(4).tolist()}")
    for a in [15,25,35]:
        res=build_KL(A,B,C,a)
        if not res: continue
        K,L,g=res[0][:3]
        O=circumcenter(A,K,L)
        # spiral center sending M->N, L->K (reversed)
        Ss=spiral_center(M,L,N,K)
        for S in Ss:
            if np.linalg.norm(S)<1e5:
                pb=perp_bis_dist(M,N,S)
                # rotation about S sending M->N: angle
                vM=M-S; vN=N-S
                th=np.angle(complex(vN[0],vN[1]))-np.angle(complex(vM[0],vM[1]))
                # apply to A
                vA=A-S; rA=complex(vA[0],vA[1])*np.exp(1j*th)
                Aimg=S+np.array([rA.real,rA.imag])
                # check does it send L->K? (it should by construction)
                vL=L-S; rL=complex(vL[0],vL[1])*np.exp(1j*th)
                Limg=S+np.array([rL.real,rL.imag])
                print(f"  a={a}: S={S.round(4).tolist()} perpbiMN={pb:.2e} R(A)={Aimg.round(4).tolist()} (A*={Astar.round(4).tolist()}) "
                      f"R(L)={Limg.round(4).tolist()}(K={K.round(4).tolist()}) dist(R(A),A*)={np.linalg.norm(Aimg-Astar):.3e} |SM|/|SN|={np.linalg.norm(S-M)/np.linalg.norm(S-N):.4f}")
