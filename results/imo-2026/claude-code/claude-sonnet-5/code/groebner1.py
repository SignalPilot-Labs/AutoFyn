import sympy as sp

sx, cx, sy, cy = sp.symbols('sx cx sy cy')
St, Ct, Sa, Ca, b, c = sp.symbols('St Ct Sa Ca b c')  # sin/cos theta, sin/cos alpha0

# cos(theta+x) = Ct*cx - St*sx ; sin(alpha0-x) = Sa*cx - Ca*sx
cos_theta_x = Ct*cx - St*sx
sin_alpha_x = Sa*cx - Ca*sx

EqK = -b*St**2 - 2*b*St*sx*cos_theta_x - b*sx**2 + c*St*(Sa*Ct+Ca*St) - c*sx*sin_alpha_x
EqK = sp.expand(EqK)

# by symmetry b<->c, x<->y for L's equation (condition ii'/Lemma B), same structural form
cos_theta_y = Ct*cy - St*sy
sin_alpha_y = Sa*cy - Ca*sy
EqL = -c*St**2 - 2*c*St*sy*cos_theta_y - c*sy**2 + b*St*(Sa*Ct+Ca*St) - b*sy*sin_alpha_y
EqL = sp.expand(EqL)

pythx = sx**2+cx**2-1
pythy = sy**2+cy**2-1

print("EqK:", EqK)
print("EqL:", EqL)

# AK = c*St/sin(x+theta) ; sin(x+theta)=sx*Ct+cx*St
# AL = b*St/sin(y+theta)
denomK = sx*Ct+cx*St
denomL = sy*Ct+cy*St

# F(x) = b*sin(alpha0-x)+c*sin(x) = b*(Sa*cx-Ca*sx) + c*sx
F = b*(Sa*cx-Ca*sx) + c*sx
# G(y) = b*sin(y)+c*sin(alpha0-y) = b*sy + c*(Sa*cy-Ca*sy)
G = b*sy + c*(Sa*cy-Ca*sy)

# target (*): AL*F(x) - AK*G(y) - (b^2-c^2)/2 * sin(alpha0-x-y) = 0
# sin(alpha0-x-y) = sin((alpha0-x)-y) = sin(alpha0-x)*cy - cos(alpha0-x)*sy
# sin(alpha0-x) = Sa*cx-Ca*sx ; cos(alpha0-x) = Ca*cx+Sa*sx
sin_a_x_y = (Sa*cx-Ca*sx)*cy - (Ca*cx+Sa*sx)*sy

AK_num = c*St   # AK * denomK = AK_num
AL_num = b*St   # AL * denomL = AL_num

# Multiply target by denomK*denomL to clear denominators:
# AL*F(x)*denomK*denomL - AK*G(y)*denomK*denomL = (AL_num/denomL... let's just do directly
target_cleared = AL_num*denomK*F - AK_num*denomL*G - sp.Rational(1,2)*(b**2-c**2)*sin_a_x_y*denomK*denomL
target_cleared = sp.expand(target_cleared)
print("target_cleared degree check done")

import pickle
with open('target_cleared.pkl','wb') as f:
    pickle.dump((target_cleared, EqK, EqL, pythx, pythy, sx,cx,sy,cy,St,Ct,Sa,Ca,b,c), f)
print("saved")
