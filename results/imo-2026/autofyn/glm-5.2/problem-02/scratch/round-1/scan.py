import numpy as np, math
from numpy import sin,cos
from scipy.optimize import brentq

# H_early = Q^2 F1 - P Q F2 + P^2 F3,  C = P S - Q R   (full trig, real angles)
# Check: does H_early vanish on ALL real points of C=0 (with pyth auto), or only the interior config branch?

def PQRS_F(Halpha,beta,gamma,A):
    sag=sin(Halpha+gamma); sab=sin(Halpha+beta)
    sAa=sin(A+Halpha); cAa=cos(A+Halpha)
    sA2ag=sin(A+2*Halpha+gamma); sA2ab=sin(A+2*Halpha+beta)
    sAag=sin(A+Halpha+gamma); sAab=sin(A+Halpha+beta)
    kx=1-sin(gamma)*cos(Halpha)/(2*sag); ky=sin(gamma)*sin(Halpha)/(2*sag)
    lx=cos(A)-sin(beta)*cos(A+Halpha)/(2*sab); ly=sin(A)-sin(beta)*sin(A+Halpha)/(2*sab)
    K2=kx**2+ky**2; L2=lx**2+ly**2
    kxl=kx*ly-ky*lx; kxcA=kx*sin(A)-ky*cos(A); lxcA=lx*sin(A)-ly*cos(A)
    F1=2*L2*kxcA/kxl-1; F2=2*(L2*ky-K2*lxcA)/kxl; F3=-2*K2*ly/kxl+1
    P=2*sag**2; Q=-(2*sAag*sag-sin(gamma)*sA2ag)
    R=2*sab*sAab-sin(beta)*sA2ab; S=-2*sab**2
    C=P*S-Q*R; H=Q**2*F1-P*Q*F2+P**2*F3
    return C,H

# fix alpha=20deg, A=60deg. Scan gamma in (0,2pi) excluding singularities; for each gamma solve C(beta,gamma)=0 for beta.
alpha=math.radians(20); A=math.radians(60)
results=[]
for gdeg in range(5,360,3):
    g=math.radians(gdeg)
    sag=sin(alpha+g)
    if abs(sag)<1e-3: continue
    def Cb(bb):
        return PQRS_F(alpha,bb,g,A)[0]
    # scan beta
    prev=None
    for bd in range(1,720,2):
        bb=math.radians(bd/2)
        try: val=Cb(bb)
        except: continue
        if prev is not None and prev*val<0:
            try:
                bro=brentq(Cb, math.radians((bd-2)/2), math.radians(bd/2))
                Cc,Hh=PQRS_F(alpha,bro,g,A)
                results.append((gdeg, math.degrees(bro), Cc, Hh))
            except: pass
        prev=val

# report points where |C|<1e-6 but |H|>1e-3  (counterexamples to H in ideal)
print(f"found {len(results)} real (gamma,beta) on C=0")
ctr=0
for (gd,bd,Cc,Hh) in results:
    if abs(Cc)<1e-6 and abs(Hh)>1e-3:
        print(f"  COUNTEREX: gamma={gd}deg beta={bd:.2f}deg  C={Cc:.2e}  H={Hh:.4f}")
        ctr+=1
print("counterexamples:",ctr)
# also print a few H values distribution
import numpy as np
Hs=np.array([abs(h) for (_,_,_,h) in results if abs(_[2] if False else 0)<1])
Hvals=np.array([h for (_,_,c,h) in results if abs(c)<1e-6])
print("on C=0: H range", Hvals.min() if len(Hvals) else None, Hvals.max() if len(Hvals) else None, "n=",len(Hvals))
