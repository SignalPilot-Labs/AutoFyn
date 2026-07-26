"""Verify spiral_center routine + test extra pairings + O-centered rotation."""
import numpy as np
from numpy import arctan2, sin, cos, pi
from scipy.optimize import brentq, fsolve
import sys
sys.path.insert(0,'/tmp/round-1')
from gate import sub, cross2, ang, rot, circumcenter, spiral_center, perp_bis_dist, build_KL

# --- sanity test of spiral_center on a known case ---
# rotation by 90deg about origin: P=(1,0)->p=(0,1), Q=(2,0)->q=(0,2). center=origin.
P=np.array([1.0,0.0]); p=np.array([0.0,1.0])
Q=np.array([2.0,0.0]); q=np.array([0.0,2.0])
print("known-case spiral centers (expect (0,0) and the indirect one):")
for S in spiral_center(P,Q,p,q):
    print("  ", S.round(5).tolist(),
          "|SB|/|SC|=",round(np.linalg.norm(S-P)/np.linalg.norm(S-p),4),
          "th=",round(np.angle(complex(p[0]-S[0],p[1]-S[1]))-np.angle(complex(P[0]-S[0],P[1]-S[1])),4))

# --- now test O-centered rotation sending K->L: does it send M->N, B->C, or A->A*? ---
print("\n=== O-centered rotation sending K->L: what does it map M,N,B,C,A to? ===")
triangles = [
    ("scalene1", [0,0],[4,0],[1,3]),
    ("scalene2", [0,0],[5,0],[2,4]),
    ("right",    [0,0],[6,0],[0,4]),
    ("random",   [0,0],[5,0],[3,2]),
]
for name,A,B,C in triangles:
    A=np.array(A,dtype=float);B=np.array(B,dtype=float);C=np.array(C,dtype=float)
    M=(A+B)/2; N=(A+C)/2
    for a in [15,25,35]:
        res=build_KL(A,B,C,a)
        if not res: continue
        K,L,g=res[0][:3]
        O=circumcenter(A,K,L)
        # rotation about O sending K->L
        vK=K-O; vL=L-O
        th=np.angle(complex(vL[0],vL[1]))-np.angle(complex(vK[0],vK[1]))
        def rotO(P): d=P-O; r=complex(d[0],d[1])*np.exp(1j*th); return O+np.array([r.real,r.imag])
        Mp=rotO(M); Np=rotO(N); Bp=rotO(B); Cp=rotO(C); Ap=rotO(A)
        print(f"{name} a={a}: th={np.degrees(th):.3f}  rot(M)={Mp.round(3).tolist()}(N={N.round(3).tolist()}) "
              f"rot(B)={Bp.round(3).tolist()}(C={C.round(3).tolist()}) rot(A)={Ap.round(3).tolist()}(A={A.round(3).tolist()})")
        # extra pairings spiral centers
        for pairing in [(B,L,C,K),(B,C,L,K),(M,L,N,K),(M,N,L,K)]:
            P_,Q_,p_,q_=pairing
            try:
                Ss=spiral_center(np.array(P_,dtype=float),np.array(Q_,dtype=float),
                                 np.array(p_,dtype=float),np.array(q_,dtype=float))
            except Exception: continue
            for S in Ss:
                if np.linalg.norm(S)<1e6:
                    d=perp_bis_dist(M,N,S); dO=np.linalg.norm(S-O)
                    print(f"    pairing {pairing}: S={S.round(4).tolist()} perpbiMN={d:.3e} distO={dO:.3e}")
