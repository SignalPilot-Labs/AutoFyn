"""
Self-contained verification of the load-bearing algebraic step in the Problem 2
solution (claude-code / claude-sonnet-5).

The written proof reduces OM = ON to a single trigonometric identity, equation (5),
in the angle unknowns x = angle BAK and y = angle CAL, and claims that (5) is an
algebraic consequence of the two angle-condition equations E_K, E_L together with
the Pythagorean relations sin^2 + cos^2 = 1.

This script reproduces that claim from scratch: it rebuilds the cleared target
polynomial and the ideal generators, computes a Groebner basis of
    < E_K, E_L, sx^2+cx^2-1, sy^2+cy^2-1 >
over Q(sin/cos theta, sin/cos alpha, b, c), reduces the target modulo it, and
checks that the remainder vanishes once the parameter Pythagorean relations
sin^2(theta)+cos^2(theta)=1 and sin^2(alpha)+cos^2(alpha)=1 are imposed.

Expected output: the final remainder prints as 0.

Requires: sympy (tested with 1.14.0). Run: python3 verify_certificate.py
"""
import sympy as sp

# Generators (the four sin/cos unknowns) and parameters.
sx, cx, sy, cy = sp.symbols('sx cx sy cy')
St, Ct, Sa, Ca, b, c = sp.symbols('St Ct Sa Ca b c')  # sin/cos theta, sin/cos alpha

# The two angle-condition equations, in cleared polynomial form.
EqK = sp.expand(
    -b*St**2 - 2*b*St*sx*(Ct*cx - St*sx) - b*sx**2
    + c*St*(Sa*Ct + Ca*St) - c*sx*(Sa*cx - Ca*sx)
)
EqL = sp.expand(
    -c*St**2 - 2*c*St*sy*(Ct*cy - St*sy) - c*sy**2
    + b*St*(Sa*Ct + Ca*St) - b*sy*(Sa*cy - Ca*sy)
)

pythx = sx**2 + cx**2 - 1
pythy = sy**2 + cy**2 - 1

# Cleared form of target equation (5):
#   AL*F(x) - AK*G(y) - (b^2-c^2)/2 * sin(alpha - x - y) = 0,
# multiplied through by denomK * denomL to clear the sine denominators.
denomK = sx*Ct + cx*St
denomL = sy*Ct + cy*St
F = b*(Sa*cx - Ca*sx) + c*sx
G = b*sy + c*(Sa*cy - Ca*sy)
sin_a_x_y = (Sa*cx - Ca*sx)*cy - (Ca*cx + Sa*sx)*sy
AK_num = c*St
AL_num = b*St
target_cleared = sp.expand(
    AL_num*denomK*F - AK_num*denomL*G
    - sp.Rational(1, 2)*(b**2 - c**2)*sin_a_x_y*denomK*denomL
)

gens = [sx, cx, sy, cy]
params = [St, Ct, Sa, Ca, b, c]

basis = sp.groebner(
    [EqK, pythx, EqL, pythy], *gens,
    order='grevlex', domain=sp.FractionField(sp.QQ, params),
)
remainder = basis.reduce(target_cleared)[1]

# The raw remainder is a rational expression in the parameters that vanishes once
# the parameter Pythagorean identities are imposed; substitute trig functions and
# simplify to collapse it.
theta, alpha = sp.symbols('theta alpha', real=True)
remainder_trig = remainder.subs(
    {St: sp.sin(theta), Ct: sp.cos(theta), Sa: sp.sin(alpha), Ca: sp.cos(alpha)}
)
final = sp.simplify(remainder_trig)

print("target polynomial term count:", len(sp.Add.make_args(target_cleared)))
print("remainder modulo the Groebner basis, after imposing the parameter")
print("Pythagorean identities (should be 0):")
sp.pprint(final)
assert final == 0, "certificate FAILED to reduce to zero"
print("\nOK: equation (5) is in the ideal < E_K, E_L, pyth_x, pyth_y >.")
