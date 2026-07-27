import sympy as sp
from sympy import sin,cos,pi,symbols,together,fraction,expand,trigsimp,cancel,Symbol,simplify
import math,sys
sys.stdout.flush()

# ---- symbolic setup: angles A, alpha, beta, gamma as raw angles ----
A,al,be,ga = symbols('A al be ga', real=True)
b,c = symbols('b c', positive=True)

sA,cA=sin(A),cos(A); sa,ca=sin(al),cos(al); sb,cb=sin(be),cos(be); sg,cg=sin(ga),cos(ga)

# frame: A=(0,0), B=(c,0), C=(b*cA,b*sA).  set c=1 later for direction (homog).
# directions:
# BK from B: angle pi-al.  MK from M=(c/2,0): angle ga.
# CL from C: angle A+pi+al (-> line dir A+al, but ray toward K goes "down-right"; use direction A+al for the line? care.)
# We follow the established parametrisation from results file:
#   BK dir = pi-al ; BL dir = pi-al-be ; CL dir = A+pi+al ; CK dir = A+pi+al+ga ; MK dir = ga ; NL dir = A-be
# K = BK line (through B) intersect MK line (through M)
# L = CL line (through C) intersect NL line (through N)
M=(sp.Rational(1,2),0) if c==1 else (c/2,0)   # we'll fix c=1
# Use c=1 (direction homogeneous in b,c, set c=1; keep b).
c1=1
Bpt=(c1,0)
Cpt=(b*cA,b*sA)
Mpt=(sp.Rational(1,2),0)
Npt=(b*cA/2,b*sA/2)

def ray(origin,ang):
    return (origin[0]+sp.cos(ang)*Symbol('t'), origin[1]+sp.sin(ang)*Symbol('t'))

# line through point P with direction angle a: param P + u*(cos a, sin a)
# intersection of (P,u,a) and (Q,v,d):
def intersect(P,a,Q,d):
    # P + u*(ca,sa) = Q + v*(cd,sd)
    ca_,sa_=sp.cos(a),sp.sin(a); cd_,sd_=sp.cos(d),sp.sin(d)
    # solve 2x2
    det=ca_*sd_-sa_*cd_
    # u = ((Qx-Px)*sd_ - (Qy-Py)*cd_)/det
    ux=sp.cancel(((Q[0]-P[0])*sd_-(Q[1]-P[1])*cd_)/det)
    return (sp.cancel(P[0]+ux*ca_), sp.cancel(P[1]+ux*sa_))

K=intersect(Bpt, pi-al, Mpt, ga)
L=intersect(Cpt, A+pi+al, Npt, A-be)
log=print
Kx,Ky=K; Lx,Ly=L
log("K",sp.count_ops(Kx),sp.count_ops(Ky),"L",sp.count_ops(Lx),sp.count_ops(Ly))

# A' = line through K perp to AK  intersect  line through L perp to AL.
# line through K perp to AK: direction = angle(AK)+90.  AK direction = atan2(Ky-0,Kx-0)=atan2(Ky,Kx).
# perpendicular direction vector = R90(A-K)? -> line dir = AK angle + pi/2.
# Easier: point P on perp-through-K satisfies (P-K).(A-K)=0 i.e. P.K = K.K (since A=0). |K|^2.
# Similarly point on perp-through-L: P.L = |L|^2.
# So A' solves  A'.K=K2  and  A'.L=L2.  (linear system) -- matches reviewer formula.
K2=sp.cancel(Kx**2+Ky**2); L2=sp.cancel(Lx**2+Ly**2)
detKL=sp.cancel(Kx*Ly-Ky*Lx)
# A' = ( L2*K - K2*L ) / detKL   (solves dot with K =K2, dot with L=L2? check)
# We need P with P.K=K2, P.L=L2.  Solve [[Kx,Ky],[Lx,Ly]] P = [K2,L2]. inverse: 1/det [[Ly,-Ky],[-Lx,Kx]]
Ax=sp.cancel((Ly*K2 - Ky*L2)/detKL)
Ay=sp.cancel((Kx*L2 - Lx*K2)/detKL)
log("A' ops",sp.count_ops(Ax),sp.count_ops(Ay))

# direction identity: (A'-B) parallel to R_{90-A-al}(C-B)
th=pi/2-A-al
# R_th(C-B):
CBx=Cpt[0]-Bpt[0]; CBy=Cpt[1]-Bpt[1]
Rx=sp.cos(th)*CBx - sp.sin(th)*CBy
Ry=sp.sin(th)*CBx + sp.cos(th)*CBy
ABx=sp.cancel(Ax-Bpt[0]); ABy=sp.cancel(Ay)
# cross product G = ABx*Ry - ABy*Rx ; want =0
G=sp.cancel(ABx*Ry - ABy*Rx)
log("G ops",sp.count_ops(G))
G=sp.expand(G)
# substitute trig identities via expand_trig? keep
G=sp.trigsimp(G)
log("G trigsimp ops",sp.count_ops(G))
