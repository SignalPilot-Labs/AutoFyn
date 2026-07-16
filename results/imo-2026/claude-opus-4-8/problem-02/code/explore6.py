import numpy as np, mpmath as mp
mp.mp.dps=25
from numpy import sin,cos
def config(alv,Bv,Cv):
    Av=np.pi-Bv-Cv
    cv=np.sin(Cv);bv=np.sin(Bv);av=np.sin(Av)
    def RIn(g): return mp.sin(Cv)*mp.sin(g)*mp.sin(Av+2*alv+g)-2*mp.sin(Av)*mp.sin(Cv-alv-g)*mp.sin(alv+g)
    def RIIn(bb): return mp.sin(Bv)*mp.sin(bb)*mp.sin(Av+2*alv+bb)-2*mp.sin(Av)*mp.sin(Bv-alv-bb)*mp.sin(alv+bb)
    gav=float(mp.findroot(RIn,0.35)); bev=float(mp.findroot(RIIn,0.4))
    tK=(cv/2)*sin(gav)/sin(alv+gav); tL=(bv/2)*sin(bev)/sin(alv+bev)
    A=np.array([cv*cos(Bv),cv*sin(Bv)]); Bp=np.array([0,0.]); Cp=np.array([av,0.])
    K=np.array([tK*cos(Bv-alv),tK*sin(Bv-alv)])
    L=np.array([av-tL*cos(Cv-alv),tL*sin(Cv-alv)])
    P=K-A; Q=L-A
    AK=np.linalg.norm(P); AL=np.linalg.norm(Q)
    # actual u=angle KAB, w=angle LAC
    u=np.arccos(np.dot(P,Bp-A)/(AK*np.linalg.norm(Bp-A)))
    w=np.arccos(np.dot(Q,Cp-A)/(AL*np.linalg.norm(Cp-A)))
    s=av/2-cv*cos(Bv)
    # star: |P|^2 Qy - |Q|^2 Py - s(Px Qy-Py Qx)
    star=AK**2*Q[1]-AL**2*P[1]-s*(P[0]*Q[1]-P[1]*Q[0])
    # star-star candidate
    ss=AK*sin(w-Cv)+AL*sin(Bv-u)-s*sin(Av+u+w)
    # compare cot u formula
    u_formula=float(mp.acot(mp.cot(alv)+2*mp.cot(gav)))
    return dict(gav=gav,u=u,u_formula=u_formula,w=w,star=star,ss=ss,
                Py=P[1],Qy=Q[1],Px=P[0],Qx=Q[0],AK=AK,AL=AL)
r=config(0.28,1.1,0.9)
for k,v in r.items(): print(k,v)
