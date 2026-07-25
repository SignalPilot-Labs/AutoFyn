import sympy as sp
from sympy import symbols, cos, sin, tan, expand, simplify, Rational, sqrt, solve, trigsimp

# Parametrize by angles alpha, beta, gamma (the three given equal angles).
# Place A at origin. Use directions:
# Let me set up at vertex B and C using the angles.
# 
# At B: rays BA, BK, BL. Going around: BA --(alpha)-- BK --(beta)-- BL.
#   angle KBA = alpha (between BK and BA)
#   angle LBK = beta (between BL and BK)
# So angle LBA = alpha + beta.
# Direction of BA: from B toward A.
# Direction of BK: rotate BA by alpha toward interior.
# Direction of BL: rotate BA by (alpha+beta) toward interior.
#
# At C: rays CA, CL, CK. 
#   angle ACL = alpha (between AC and CL)
#   angle LCK = gamma (between CL and CK)
# So angle ACK = alpha + gamma.
# Direction CA from C toward A. CL: rotate CA by alpha toward interior. CK: rotate CA by (alpha+gamma).
#
# Also angle LNC = beta at N, and angle BMK = gamma at M.
#
# Let's use complex coordinates. A=0. B, C complex.
# Direction of a ray "rotate vector v by angle t counterclockwise": multiply by e^{it}.
# Need to know orientations (which side is interior). Assume triangle oriented A,B,C counterclockwise 
# (so C is to the left of AB). Then at B, interior is to the... let me just pick signs and verify numerically.

# From numerics: A=(0,0),B=(1,0),C=(p,q) with q>0. 
# alpha=ang KBA: K-B and A-B=(-1,0). K is above x-axis mostly (k2>0 small). ang between (K-B) and (-1,0).
#   K-B points up-left-ish. The angle from BA=(-1,0) to BK=(K-B): rotating CCW by alpha. So BK = R(alpha)*BA up to length.
# Good: interior at B is upward.
# 
# Let me define unit direction of BA from B: e_BA = (A-B)/|A-B|.
# BK direction = R(alpha) e_BA   (CCW)
# BL direction = R(alpha+beta) e_BA
# 
# At C: CA direction from C: e_CA=(A-C)/|A-C|. 
# CL direction = R(alpha) e_CA  (which way? ang ACL = alpha, interior). 
#   From numerics L is up-left of C. C=(p,q), L near (1,2), A=(0,0). CA points down-left.
#   CL points... L-C roughly (1-p, 2-q) up. Rotating CA CCW or CW? 
#   Let me just compute: will determine sign by requiring L inside angle ACK and consistency.
# CK direction = rotate e_CA further by gamma.
#
# This is getting complicated with lengths. Let me instead use the SINE RULE in the sub-triangles 
# to express everything in terms of alpha,beta,gamma and the triangle ABC.
#
# Cleaner: Express K and L as intersections of rays, then impose the two remaining conditions 
# (beta at N, gamma at M) — but those DEFINE the family. The identity OM=ON must hold for ALL 
# alpha,beta,gamma satisfying... no.
#
# Hmm. Let me reconsider: we have 3 angle equations and 4 unknowns -> 1-param family. 
# alpha, beta, gamma are NOT all free. Let me recount using the ray parametrization:
# Free: alpha, beta, gamma (3 params) determine the 4 rays (BK,BL from B; CL,CK from C) up to 
# the triangle. K = BK ∩ CK, L = BL ∩ CL. That's 2 points = determined by 3 angles. 
# But we ALSO need angle LNC=beta and angle BMK=gamma — 2 more equations. So 3 angles, 2 eqns => 
# 1 free param. Consistent with 1-param family. Good.
# So: K=intersection(B-ray-BK, C-ray-CK), L=intersection(B-ray-BL, C-ray-CL).
# Then impose: ang(LNC)=beta, ang(BMK)=gamma. 
# Want: OM=ON.
# This parametrization automatically satisfies eq1 (alpha at B = alpha at C) and the ray structure.
# Let me set this up with complex numbers / rotation matrices and use tan half-angle or just trig.

# Use coordinates: A=(0,0), B=(1,0), C=(p,q).
# Let sB = sin stuff. Define directions via angle from x-axis.
# Direction of BA (from B): points toward A = angle pi (i.e., (-1,0)).
# BK direction angle = pi - alpha  (rotating BA=(-1,0) by +alpha CCW gives angle pi+alpha... 
#   wait rotating (-1,0) CCW by alpha: angle of (-1,0) is pi; +alpha -> pi+alpha, points down-left. 
#   But K is UP. So rotate CW: angle pi - alpha. Yes BK angle = pi - alpha.)
# BL direction angle = pi - (alpha+beta).
# 
# At C=(p,q). CA direction angle = atan2(-q,-p) = pi + atan2(q,p)... = angle of (-p,-q).
#   Let phi = atan2(q,p) (angle of C from A). Then CA from C has angle phi+pi.
# CL: rotate toward interior. Interior of triangle near C is below-left roughly. 
#   From numerics, L above C, so CL points upward => angle near pi/2 ish. 
#   CA angle = phi+pi (pointing back to origin, down-left). To get CL pointing up, rotate CW by alpha 
#   (since phi+pi is in third quadrant for p,q>0, rotating CW by alpha toward angle pi/2...).
#   Let me just say CL angle = (phi+pi) - alpha, CK angle = (phi+pi) - (alpha+gamma).
#   Check: phi in (0,pi/2). phi+pi in (pi,3pi/2). Minus alpha (small) still ~ third quadrant -> down-left. 
#   That's not up. Hmm.
# Let me reconsider: maybe rotate CCW: CL = (phi+pi)+alpha. That goes further into 3rd/4th quadrant. Also down.
# I'm confusing myself. Let me just numerically extract the actual angles of these rays.
print("param analysis - will compute numerically next")
