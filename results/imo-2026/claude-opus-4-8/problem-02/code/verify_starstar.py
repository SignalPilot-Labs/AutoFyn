# Final numerical confirmation of the reduction chain and identity (**).
import numpy as np, mpmath as mp
mp.mp.dps=25
from numpy import sin,cos
def test(alv,Bv,Cv):
    Av=np.pi-Bv-Cv
    cv=np.sin(Cv);bv=np.sin(Bv);av=np.sin(Av)
    def RIn(g): return mp.sin(Cv)*mp.sin(g)*mp.sin(Av+2*alv+g)-2*mp.sin(Av)*mp.sin(Cv-alv-g)*mp.sin(alv+g)
    def RIIn(bb): return mp.sin(Bv)*mp.sin(bb)*mp.sin(Av+2*alv+bb)-2*mp.sin(Av)*mp.sin(Bv-alv-bb)*mp.sin(alv+bb)
    gav=float(mp.findroot(RIn,0.35)); bev=float(mp.findroot(RIIn,0.4))
    u=float(mp.acot(mp.cot(alv)+2*mp.cot(gav)))
    w=float(mp.acot(mp.cot(alv)+2*mp.cot(bev)))
    AK=cv*sin(alv)/sin(alv+u); AL=bv*sin(alv)/sin(alv+w)
    s=(bv**2-cv**2)/(2*av)
    lhs=AK*sin(Cv+w)-AL*sin(Bv+u); rhs=s*sin(u+w-Av)
    # full config OM=ON
    tK=(cv/2)*sin(gav)/sin(alv+gav); tL=(bv/2)*sin(bev)/sin(alv+bev)
    A=np.array([cv*cos(Bv),cv*sin(Bv)]);Bp=np.array([0,0.]);Cp=np.array([av,0.])
    K=np.array([tK*cos(Bv-alv),tK*sin(Bv-alv)]); L=np.array([av-tL*cos(Cv-alv),tL*sin(Cv-alv)])
    def cc(P,Q,R):
        ax,ay=P;bx,by=Q;cx,cy=R
        D=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
        ux=((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)*(ay-by))/D
        uy=((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+(cx*cx+cy*cy)*(bx-ax))/D
        return np.array([ux,uy])
    O=cc(A,K,L); M=(A+Bp)/2;N=(A+Cp)/2
    return abs(lhs-rhs), abs(np.linalg.norm(O-M)-np.linalg.norm(O-N))
for cfg in [(0.28,1.1,0.9),(0.3,1.0,1.05),(0.2,1.2,0.8),(0.15,0.95,1.15),(0.35,1.25,0.75)]:
    d1,d2=test(*cfg); print(f"cfg={cfg}: |(**)diff|={d1:.2e}  |OM-ON|={d2:.2e}")
