import numpy as np, mpmath as mp
mp.mp.dps=25
from numpy import sin,cos
# verify (star-star): AK sin(w-C)+AL sin(B-u) = s sin(A+u+w)
# with u=angle KAB, w=angle LAC, AK=c sina/sin(a+u), AL=b sina/sin(a+w)
def config(alv,Bv,Cv):
    Av=np.pi-Bv-Cv
    cv=np.sin(Cv);bv=np.sin(Bv);av=np.sin(Av)
    # solve for gamma via (I), beta via (II)
    def RIn(g): return mp.sin(Cv)*mp.sin(g)*mp.sin(Av+2*alv+g)-2*mp.sin(Av)*mp.sin(Cv-alv-g)*mp.sin(alv+g)
    def RIIn(bb): return mp.sin(Bv)*mp.sin(bb)*mp.sin(Av+2*alv+bb)-2*mp.sin(Av)*mp.sin(Bv-alv-bb)*mp.sin(alv+bb)
    gav=float(mp.findroot(RIn,0.35)); bev=float(mp.findroot(RIIn,0.4))
    # cot u = cot a + 2 cot g
    u=float(mp.acot(mp.cot(alv)+2*mp.cot(gav)))
    w=float(mp.acot(mp.cot(alv)+2*mp.cot(bev)))
    AK=cv*sin(alv)/sin(alv+u); AL=bv*sin(alv)/sin(alv+w)
    s=av/2-cv*cos(Bv)
    lhs=AK*sin(w-Cv)+AL*sin(Bv-u)
    rhs=s*sin(Av+u+w)
    return gav,bev,u,w,lhs,rhs
for (alv,Bv,Cv) in [(0.28,1.1,0.9),(0.3,1.0,1.05),(0.2,1.2,0.8)]:
    g,b,u,w,lhs,rhs=config(alv,Bv,Cv)
    print(f"al={alv} B={Bv} C={Cv}: (**) lhs={lhs:.8f} rhs={rhs:.8f} diff={lhs-rhs:.2e}")

# Now test trig-Ceva form for u: sin u/sin(A-u)*sin(a+g)/sin(C-a-g)*sin(B-a)/sin(a)=1
def checkceva(alv,Bv,Cv):
    Av=np.pi-Bv-Cv
    def RIn(g): return mp.sin(Cv)*mp.sin(g)*mp.sin(Av+2*alv+g)-2*mp.sin(Av)*mp.sin(Cv-alv-g)*mp.sin(alv+g)
    gav=float(mp.findroot(RIn,0.35))
    u=float(mp.acot(mp.cot(alv)+2*mp.cot(gav)))
    val=sin(u)/sin(Av-u)*sin(alv+gav)/sin(Cv-alv-gav)*sin(Bv-alv)/sin(alv)
    return val
print("trig Ceva check (should=1):", checkceva(0.28,1.1,0.9))
