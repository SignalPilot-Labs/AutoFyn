import numpy as np, math
from numpy import sin,cos
from scipy.optimize import fsolve

# Reconstruct Phi and check it on valid configurations
# Phi = sA*sa^2*(tb^2-1)*(1-tg^2) + sa*(ca*sA-cA*sa)*(tb+tg)*(tb*tg-1) + (2*cA*ca*sa+sA*(sa^2-ca^2))*tb*tg

def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def build(A,al,be,ga,b,c):
    B=np.array([c,0.0]); C=np.array([b*cos(A),b*sin(A)]); M=B*0.5; N=C*0.5
    def isect(P,a,Q,d):
        ca_,sa_=cos(a),sin(a); cd_,sd_=cos(d),sin(d); det=ca_*sd_-sa_*cd_
        u=((Q[0]-P[0])*sd_-(Q[1]-P[1])*cd_)/det; return P+u*np.array([ca_,sa_])
    K=isect(B,np.pi-al,M,ga); L=isect(C,A+np.pi+al,N,A-be)
    return B,C,K,L

def incid(A,al,be,ga,b,c):
    B,C,K,L=build(A,al,be,ga,b,c)
    dCK=np.array([cos(A+np.pi+al+ga),sin(A+np.pi+al+ga)]); incK=cross(K-C,dCK)
    dBL=np.array([cos(np.pi-al-be),sin(np.pi-al-be)]); incL=cross(L-B,dBL)
    return incK,incL

configs=[(70,15,1.4,1.0),(55,25,1.0,1.2),(80,10,1.6,1.1),(45,18,0.9,1.3),(65,8,1.1,0.8),(50,30,1.3,1.0),(40,20,1.0,1.5),(75,12,1.2,0.9)]
print("Checking Phi and Td on valid configurations:")
print(f"{'A':>4} {'al':>4} {'b':>4} {'c':>4} {'beta':>8} {'gamma':>8} {'Phi':>12} {'tg^2+1':>10} {'Td':>12} {'Ccon':>12}")
for (Ad,ald,b,c) in configs:
    A_=np.radians(Ad); al_=np.radians(ald)
    def f(x):
        be,ga=x; return list(incid(A_,al_,np.radians(be),np.radians(ga),b,c))
    x,inf,ier,msg=fsolve(f,[12,12],full_output=True)
    be,ga=x[0],x[1]
    sa,ca=sin(al_),cos(al_)
    sA,cA=sin(A_),cos(A_)
    tb,tg=math.tan(math.radians(be)/2),math.tan(math.radians(ga)/2)
    Phi = sA*sa**2*(tb**2-1)*(1-tg**2) + sa*(ca*sA-cA*sa)*(tb+tg)*(tb*tg-1) + (2*cA*ca*sa+sA*(sa**2-ca**2))*tb*tg
    Td = (tg**2+1)*Phi
    # also compute Ccon numerically
    Cval = float(max(abs(inf['fvec'][0]),abs(inf['fvec'][1])))
    print(f"{Ad:4d} {ald:4d} {b:4.1f} {c:4.1f} {be:8.4f} {ga:8.4f} {Phi:12.6e} {tg**2+1:10.4f} {Td:12.6e} {Cval:12.2e}")
