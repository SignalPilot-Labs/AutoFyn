import sympy as sp
from sympy import symbols, cos, sin, tan, atan2, simplify, Rational, sqrt, solve, Abs, arg, I, re, im, expand

# Use A as origin. Let's parametrize via angles to make angle conditions linear.
# Rays from B: BA, BK, BL. From C: CA, CL, CK.
# alpha = ang KBA = ang ACL
# beta  = ang LBK = ang LNC  
# gamma = ang LCK = ang BMK
#
# Place A=origin. Put B on a ray, C on another. Use A at origin, and directions of AB, AC.
# Let me use a coordinate where AB along x-axis.
# A=(0,0), B=(c,0) where c=AB. C=(b cosA, b sinA) where b=AC, A=angle BAC.
# But the answer OM=ON is a metric relation; better to keep general.
#
# Alternative clean approach: parametrize K and L by the angles and use sine rule in sub-triangles.
# This is getting complicated; let me just do full symbolic with trig substitution via tangents.
#
# Actually, simplest: verify the algebraic identity that "OM^2 - ON^2 = 0" follows from the
# 3 angle equations. Express angles via tangent of arg, use resultants.

# Let's use coordinates A=(0,0), B=(1,0) (scale AB=1, WLOG by similarity since OM,ON scale together).
# C=(p,q) general. M=(1/2,0), N=(p/2,q/2).
# K=(k1,k2), L=(l1,l2).
#
# The angle conditions via cross/dot: tan(angle XYZ) = |cross|/dot.
# Equivalently the equality of (unsigned) angles between (u,v) and (w,z) means
#   cross(u,v)*dot(w,z) = ± dot(u,v)*cross(w,z)  with consistent sign.
# Since all are inside-angle (positive, in (0,pi)), we have
#   cross(u,v)/dot(u,v) and cross(w,z)/dot(w,z) have the same sign, and
#   ang equal  <=>  cross(u,v)*dot(w,z) - dot(u,v)*cross(w,z) = 0  (tan equal) 
#   BUT tan equality also holds for supplementary. Since both in (0,pi) and same orientation 
#   of "left turn", we use signed: the signed angle (oriented) from first ray to second.
# Let me define oriented carefully using cross and dot without sign ambiguity by squaring approach.
#
# Cleaner: ang(u,v)=ang(w,z)  <=>  (cross(u,v)*dot(w,z))^2 = (dot(u,v)*cross(w,z))^2  AND signs match.
# For algebraic identity verification, the squared version is what we want anyway (the identity 
# OM=ON should hold as algebraic consequence).

p,q = symbols('p q', real=True, positive=True)
k1,k2,l1,l2 = symbols('k1 k2 l1 l2', real=True)

def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def dot(u,v): return u[0]*v[0]+u[1]*v[1]

A=(sp.Integer(0),sp.Integer(0)); B=(sp.Integer(1),sp.Integer(0)); C=(p,q)
M=(sp.Rational(1,2),sp.Integer(0)); N=(p/2,q/2)
K=(k1,k2); L=(l1,l2)

def sub(P,Q): return (P[0]-Q[0],P[1]-Q[1])

# angle KBA: rays BK and BA -> vectors K-B, A-B
# angle ACL: rays CA, CL -> vectors A-C, L-C
u1=sub(K,B); v1=sub(A,B); u2=sub(A,C); v2=sub(L,C)
# ang(u1,v1) = ang(u2,v2):  cross(u1,v1)*dot(u2,v2) = dot(u1,v1)*cross(u2,v2)
eq1 = cross(u1,v1)*dot(u2,v2) - dot(u1,v1)*cross(u2,v2)

# angle LBK = angle LNC: rays BL,BK -> L-B,K-B ; rays NL,NC -> L-N,C-N
u1=sub(L,B); v1=sub(K,B); u2=sub(L,N); v2=sub(C,N)
eq2 = cross(u1,v1)*dot(u2,v2) - dot(u1,v1)*cross(u2,v2)

# angle LCK = angle BMK: rays CL,CK -> L-C,K-C ; rays MB,MK -> B-M,K-M
u1=sub(L,C); v1=sub(K,C); u2=sub(B,M); v2=sub(K,M)
eq3 = cross(u1,v1)*dot(u2,v2) - dot(u1,v1)*cross(u2,v2)

eq1=sp.expand(eq1); eq2=sp.expand(eq2); eq3=sp.expand(eq3)
print("eq1 terms:", len(eq1.as_ordered_terms()))
print("eq2 terms:", len(eq2.as_ordered_terms()))
print("eq3 terms:", len(eq3.as_ordered_terms()))
sp.save('/tmp/geom/eqs.py', {'eq1':eq1,'eq2':eq2,'eq3':eq3,'p':p,'q':q,'k1':k1,'k2':k2,'l1':l1,'l2':l2})
