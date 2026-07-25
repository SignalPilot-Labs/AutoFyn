import sympy as sp
from sympy import symbols, expand, groebner, Rational, solve, simplify

# Rational parametrization using slopes.
# A=(0,0), B=(1,0), C=(p,q), p,q >0 rational symbols.
# Rays from B: BK and BL. BA is the x-axis (toward A, i.e. negative x direction).
# Let the slope-based: a ray from B making angle phi above the negative x-axis.
#   direction = (-cos phi, sin phi). Parametrize by t = tan(phi/2): 
#   cos phi = (1-t^2)/(1+t^2), sin phi = 2t/(1+t^2).  direction = (-(1-t^2)/(1+t^2), 2t/(1+t^2)).
# Let ta = tan(alpha/2), so phi=alpha for BK. 
# For BL, phi = alpha+beta. Let tb such that tan((alpha+beta)/2) = ... combine? 
#   Messy. 
#
# ALTERNATIVE: parametrize the RAYS directly by a slope parameter, NOT tied to angle-addition.
# Let ray BK from B have direction (-1, m_K) scaled: actually direction (-cos a, sin a) ~ (-1, tan a) 
# normalized doesn't matter for line. Line BK through B=(1,0) with direction (-1, s) where s=tan(a)>0:
#   param: (1 - lambda, lambda*s). 
# Line BL through B with direction (-1, t): t = tan(alpha+beta). 
# At C: CA direction = (-p,-q). Line through C in direction obtained by rotating CA. 
#   Rotating (-p,-q) by angle alpha: direction = (-(p cos a - q sin a), -(p sin a + q cos a)).
#   As a LINE direction (up to scale), use the slope. Express via tan(a)=s:
#   cos a = 1/sqrt(1+s^2), sin a = s/sqrt(1+s^2). direction ~ (-(p - q s), -(p s + q)) up to common sqrt factor.
#   So line CL through C=(p,q) with direction (-(p-q s), -(p s+q))... but we can use direction (p - q s, p s + q) 
#   (sign flip, same line) -- need correct orientation but line is what matters for intersection.
#   Actually let's keep direction d_CL = (-(p - q s), -(p s + q)) = (q s - p, -p s - q).
# Line CK through C with rotation by alpha+gamma. tan(alpha+gamma) = combined. 
#   Let me use a SEPARATE slope param for the rotation angle alpha+gamma: call the total rotation from 
#   CA by using tan. Hmm.
#
# Cleanest: parametrize each of the 4 rotation angles by independent tan-half variables, but enforce 
# angle KBA = angle ACL (same alpha) by using the SAME tan(alpha/2)=A for both B and C rotations,
# and tan(gamma/2)=G for the extra C rotation, tan(beta/2)=Bt for extra B rotation.
# Then BK rotation from BA by alpha: BA dir = (-1,0). 
#   Using tan-half A: rot by alpha of (-1,0): 
#   R(alpha)*(-1,0) = (-cos a, sin a) = (-(1-A^2)/(1+A^2), 2A/(1+A^2)). Direction fine.
# BL rotation by alpha+beta from BA: need rot by (alpha+beta). tan-half of sum is messy.
#
# KEY SIMPLIFICATION: Instead of "alpha then beta", parametrize BK and BL by INDEPENDENT half-angle 
# params A (for alpha=ang KBA) and P (for alpha+beta = ang LBA). Then beta = (alpha+beta) - alpha 
# is implicit. The condition ang LBK = beta means ang LBA - ang KBA = beta = ang LNC. So:
#   Let A = tan(alpha/2), P = tan((alpha+beta)/2). 
#   BK dir from B: rot_{alpha}(-1,0).  BL dir from B: rot_{alpha+beta}(-1,0).
#   At C: CL rotation by alpha from CA -> uses same A. CK rotation by (alpha+gamma) from CA.
#   Let G = tan((alpha+gamma)/2). CK uses G.
#   Then gamma = (alpha+gamma)-alpha, beta=(alpha+beta)-alpha.
# Conditions: ang LNC = beta, ang BMK = gamma.
# This is fully rational in A,P,G (and p,q). Let's do it.
print("strategy confirmed: half-angle params A,P,G")
