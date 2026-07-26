"""Numeric GAP-2 gate for miquel-spiral approach.

For each of several triangles, build the 1-parameter family of valid (K,L)
satisfying the IMO 2026 P2 angle conditions. Then for each (K,L):
  - compute the spiral-similarity center S1 sending B->C and K->L
  - compute the spiral-similarity center S2 sending M->N and K->L
  - compute O = circumcenter of AKL
  - check whether S1 (resp. S2) equals O, or lies on perp-bis(MN)
  - also compute Miquel point Mq of quadrilateral (AB,AC,BK,CL) and test.
"""
import numpy as np
from numpy import arctan2, sin, cos, pi
from scipy.optimize import brentq

def sub(a,b): return np.array(a,dtype=float)-np.array(b,dtype=float)
def cross2(u,v): return u[0]*v[1]-u[1]*v[0]
def ang(u,v):  # unsigned angle between vectors, in radians [0,pi]
    c = np.dot(u,v); s = cross2(u,v)
    return abs(arctan2(s,c))
def signed(u,v):  # signed angle from u to v, (-pi,pi]
    return arctan2(cross2(u,v), np.dot(u,v))

def rot(v,th):  # rotate vector v by angle th (positive = CCW)
    c,s = cos(th),sin(th)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])

def line_intersect(p1,d1,p2,d2):
    # intersection of p1+t d1 and p2+u d2
    M = np.array([[d1[0],-d2[0]],[d1[1],-d2[1]]])
    b = p2-p1
    tu = np.linalg.solve(M,b)
    return p1+tu[0]*d1

def circumcenter(A,K,L):
    ax,ay=A; kx,ky=K; lx,ly=L
    D = 2*(ax*(ky-ly)+kx*(ly-ay)+lx*(ay-ky))
    ux = (ax*ax+ay*ay)*(ky-ly)+(kx*kx+ky*ky)*(ly-ay)+(lx*lx+ly*ly)*(ay-ky)
    uy = (ax*ax+ay*ay)*(lx-kx)+(kx*kx+ky*ky)*(ax-lx)+(lx*lx+ly*ly)*(kx-ax)
    return np.array([ux/D, uy/D])

def spiral_center(P,Q,p,q):
    """Center S of the (direct) spiral similarity sending P->p and Q->q.
    S satisfies |S-P|/|S-p| = |S-Q|/|S-q| = ratio and angle(SP,Sp)=angle(SQ,Sq).
    Standard: S is intersection of circumcircles of (P,Q,p) and (P,Q,q)? No.
    The spiral center sending P->p and Q->q is the intersection of the
    circumcircles of triangles P-Q-p and ... actually it's the second
    intersection of circles (P Q p) wait. The two spiral centers (direct &
    indirect) are the two Miquel points of the complete quadrilateral
    P,p,Q,q? Let's use the standard construction:
       direct spiral center = second intersection of circles (P Q p) and (P Q q)? No.
    Correct: spiral center sending (P,Q)->(p,q) is the intersection point
    (other than the common one) of circles through (P,p,?) ...
    Use: the center S is the intersection of the circumcircle of (P,Q,X)
    and (p,q,X) where X is intersection of lines Pp and Qq? That's Miquel.
    Simpler analytic formula: S satisfies
       arg((p-S)/(P-S)) = arg((q-S)/(Q-S))  and  |p-S|/|P-S| = |q-S|/|Q-S|
    The direct center is the second intersection of circles (P,Q,p)? no.
    Standard result: the (direct) spiral center that maps segment PQ to pq
    is the second intersection of the circumcircles of triangles P Q (Pp ∩ Qq)?
    Let me just solve numerically: S=(x,y) with
       (p-S) = r R(theta) (P-S),  (q-S) = r R(theta) (Q-S)
    => |p-S|/|P-S| = |q-S|/|Q-S| (ratio eq)  and
       arg((p-S)/(P-S)) = arg((q-S)/(Q-S))  (angle eq)
    Solve 2 equations in x,y. We'll use fsolve; also get the OTHER (indirect)
    center via reflecting one image.
    """
    # We solve for S such that the two oriented angles are equal AND the two
    # ratios are equal. Two unknowns x,y; two equations.
    def eqs(S):
        aP = complex(P[0]-S[0], P[1]-S[1])
        ap = complex(p[0]-S[0], p[1]-S[1])
        aQ = complex(Q[0]-S[0], Q[1]-S[1])
        aq = complex(q[0]-S[0], q[1]-S[1])
        aPv=abs(aP); aQv=abs(aQ); apv=abs(ap); aqv=abs(aq)
        if aPv<1e-12 or aQv<1e-12 or apv<1e-12 or aqv<1e-12:
            return [1e6,1e6]
        # ratio equality: |ap|/|aP| - |aq|/|aQ|
        r1 = apv/aPv - aqv/aQv
        # angle equality: arg(ap/aP) - arg(aq/aQ)  (mod 2pi; use sin/cos)
        th1 = np.angle(ap/aP) - np.angle(aq/aQ)
        # wrap to (-pi,pi]
        th1 = (th1+pi)%(2*pi)-pi
        return [r1, sin(th1)]  # sin of angle diff -> 0 when diff=0 or pi
    from scipy.optimize import fsolve
    sols=[]
    for guess in [np.array([0.0,0.0]), np.array([5.0,5.0]),
                  np.array([-5.0,5.0]), np.array([3.0,-2.0]),
                  np.mean([P,Q,p,q],axis=0)]:
        S=fsolve(eqs,guess,full_output=True)
        x,info,ier,msg=S
        if ier==1:
            x=np.array(x)
            # verify
            r=eqs(x)
            if max(abs(r[0]),abs(r[1]))<1e-6 and not any(np.allclose(x,s) for s in sols):
                sols.append(x)
    return sols

def perp_bis_dist(P,Q,S):
    """signed distance of S from the PERPENDICULAR bisector of PQ (0 means on it).
    The perp-bisector of PQ is perpendicular to PQ, so its normal is parallel to PQ."""
    mid=(P+Q)/2
    n=np.array(Q-P,dtype=float)  # normal to the perp-bisector (parallel to PQ)
    return np.dot(S-mid, n)/np.linalg.norm(n)

def miquel_complete_quad(L1p,L1d,L2p,L2d,L3p,L3d,L4p,L4d):
    """Miquel point of complete quadrilateral of 4 lines.
    Lines: (p,d). Vertices = pairwise intersections. Miquel point is the
    common point of circumcircles of the 4 triangles.
    We compute the 6 vertices, then the two 'opposite' triangles and intersect
    their circumcircles (two points: one vertex, one = Miquel).
    Standard: for lines l1..l4, the 4 triangles are formed by choosing 3 of 4
    lines. Their circumcircles share the Miquel point. Take triangles (l1,l2,l3)
    and (l1,l2,l4): they share vertex l1∩l2; second intersection = Miquel.
    """
    def I(i,j):
        return line_intersect(L1p if i==1 else (L2p if i==2 else (L3p if i==3 else L4p)),
                              L1d if i==1 else (L2d if i==2 else (L3d if i==3 else L4d)),
                              L1p if j==1 else (L2p if j==2 else (L3p if j==3 else L4p)),
                              L1d if j==1 else (L2d if j==2 else (L3d if j==3 else L4d)))
    V12=I(1,2); V13=I(1,3); V14=I(1,4); V23=I(2,3); V24=I(2,4); V34=I(3,4)
    # triangle (l1,l2,l3): vertices V12,V13,V23 ; circle C123
    C1=circumcircle_pts(V12,V13,V23)
    # triangle (l1,l2,l4): V12,V14,V24
    C2=circumcircle_pts(V12,V14,V24)
    # intersect C1 and C2: shared point V12, other = Miquel
    return circle_second_intersection(C1,C2,V12), V12

def circumcircle_pts(P,Q,R):
    cx,cy=circumcenter(P,Q,R)
    return (np.array([cx,cy]), np.linalg.norm(P-np.array([cx,cy])))

def circle_second_intersection(C1,C2,known):
    c1,r1=C1; c2,r2=C2
    # line through the two circle centers (radical line perpendicular to it)
    d=c2-c1; base=np.array([d[1],-d[0]])  # direction of radical axis
    # radical axis: |x-c1|^2-r1^2 = |x-c2|^2-r2^2
    # 2 x.(c2-c1) = r1^2-r2^2 + |c2|^2-|c1|^2
    rhs=r1**2-r2**2+np.dot(c2,c2)-np.dot(c1,c1)
    t0=rhs/(2*np.dot(d,d))
    foot=c1+t0*d
    # find points on radical axis at distance
    dd=np.dot(c1-c2,c1-c2); a=0.5; mid=c1+0.5*d
    h2=r1**2-np.dot(foot-c1,foot-c1)
    if h2<0: h2=0
    h=np.sqrt(h2)
    cand1=foot+h*base/np.linalg.norm(base)
    cand2=foot-h*base/np.linalg.norm(base)
    if np.linalg.norm(cand1-known)<1e-6: return cand2
    return cand1

def build_KL(A,B,C, alpha_deg):
    """Given triangle and alpha (deg), find K on ray B (angle alpha from BA
    inside BMC) satisfying master relation ∠ACK = alpha + ∠BMK, then find L.
    Returns (K,L,gamma,beta) or None."""
    A=np.array(A,dtype=float);B=np.array(B,dtype=float);C=np.array(C,dtype=float)
    M=(A+B)/2; N=(A+C)/2
    a=alpha_deg*pi/180
    # BA direction from B
    BA=sub(A,B); BA=BA/np.linalg.norm(BA)
    # BMC interior: between BM(=BA dir) and BC. Rotate BA toward BC by CCW or CW?
    # We need the side where C lies.
    BC=sub(C,B)
    s = cross2(BA,BC)  # sign: if >0, C is CCW from BA
    sgn = 1 if s>0 else -1
    BKdir = rot(BA, sgn*a)
    # K = B + t*BKdir, t>0. Find t s.t. ∠ACK = alpha + ∠BMK.
    def master(t):
        K=B+t*BKdir
        # ∠ACK = angle at C between CA and CK
        CA=sub(A,C); CK=sub(K,C)
        ack=ang(CA,CK)
        # ∠BMK = angle at M between MB and MK
        MB=sub(B,M); MK=sub(K,M)
        g=ang(MB,MK)
        return ack - (a+g)
    # search t in a range
    ts=np.linspace(0.05,4.0,40)
    vals=np.array([master(t) for t in ts])
    # find sign change
    sols=[]
    for i in range(len(ts)-1):
        if vals[i]*vals[i+1]<0:
            try:
                tt=brentq(master,ts[i],ts[i+1])
                K=B+tt*BKdir
                # verify K inside BMC (barycentric) - rough
                sols.append(K)
            except: pass
    if not sols: return None
    out=[]
    for K in sols:
        # gamma
        MB=sub(B,M); MK=sub(K,M); g=ang(MB,MK)
        # now L: on ray from C, direction CL: CA rotated by alpha (toward interior of BNC, i.e., toward B)
        CA=sub(A,C); CA=CA/np.linalg.norm(CA)
        CB=sub(B,C)
        s2 = 1 if cross2(CA,CB)>0 else -1
        CLdir=rot(CA, s2*a)
        # L = C + u*CLdir. Need ∠LBK = ∠LNC = beta.
        def eqL(u):
            Lp=C+u*CLdir
            # ∠LNC at N between NL and NC
            NC=sub(C,N); NL=sub(Lp,N)
            b1=ang(NC,NL)
            # ∠LBK at B between BL and BK
            BL=sub(Lp,B); BK=sub(K,B)
            b2=ang(BL,BK)
            return b1-b2
        us=np.linspace(0.01,4.0,50)
        vls=np.array([eqL(u) for u in us])
        Ls=[]
        for i in range(len(us)-1):
            if vls[i]*vls[i+1]<0:
                try:
                    uu=brentq(eqL,us[i],us[i+1])
                    Ls.append(C+uu*CLdir)
                except: pass
        for L in Ls:
            out.append((K,L,g))
    return out

def main():
    triangles = [
        ("scalene1", [0,0],[4,0],[1,3]),
        ("scalene2", [0,0],[5,0],[2,4]),
        ("right",    [0,0],[6,0],[0,4]),
        ("isoceles", [0,3],[-2,0],[2,0]),
        ("random",   [0,0],[5,0],[3,2]),
    ]
    alphas=[15,20,25,30,35]  # degrees
    for name,A,B,C in triangles:
        A=np.array(A,dtype=float);B=np.array(B,dtype=float);C=np.array(C,dtype=float)
        M=(A+B)/2; N=(A+C)/2
        print(f"\n=== {name}: A={A.tolist()} B={B.tolist()} C={C.tolist()} ===")
        print(f"  M={M.tolist()} N={N.tolist()}")
        for a in alphas:
            res=build_KL(A,B,C,a)
            if not res: continue
            for (K,L,g) in res[:2]:
                O=circumcenter(A,K,L)
                pbmn = perp_bis_dist(M,N,O)
                print(f"  alpha={a} K={K.round(3).tolist()} L={L.round(3).tolist()} O={O.round(4).tolist()} O-perpbiMN={pbmn:.2e} OM={np.linalg.norm(O-M):.4f} ON={np.linalg.norm(O-N):.4f}")
                # spiral center S1: B->C, K->L
                S1s=spiral_center(B,C,K,L)
                for S1 in S1s:
                    d1=perp_bis_dist(M,N,S1)
                    dO=np.linalg.norm(S1-O)
                    # also |SB| vs |SC| check (should be equal)
                    print(f"     S1(B->C,K->L)={S1.round(4).tolist()} perpbiMN={d1:.3e} dist(S1,O)={dO:.3e} |SB|={np.linalg.norm(S1-B):.3f}|SC|={np.linalg.norm(S1-C):.3f}|SK|={np.linalg.norm(S1-K):.3f}|SL|={np.linalg.norm(S1-L):.3f}")
                # spiral center S2: M->N, K->L
                S2s=spiral_center(M,N,K,L)
                for S2 in S2s:
                    d2=perp_bis_dist(M,N,S2)
                    dO=np.linalg.norm(S2-O)
                    print(f"     S2(M->N,K->L)={S2.round(4).tolist()} perpbiMN={d2:.3e} dist(S2,O)={dO:.3e} |SM|={np.linalg.norm(S2-M):.3f}|SN|={np.linalg.norm(S2-N):.3f}")
                # Miquel point of (AB,AC,BK,CL)
                BKdir=sub(K,B); CLdir=sub(L,C)
                Mq,V12=miquel_complete_quad(A,sub(B,A),A,sub(C,A),B,BKdir,C,CLdir)
                dm=perp_bis_dist(M,N,Mq)
                dO=np.linalg.norm(Mq-O)
                print(f"     Miquel Mq={Mq.round(4).tolist()} perpbiMN={dm:.3e} dist(Mq,O)={dO:.3e}")

if __name__=='__main__':
    main()
