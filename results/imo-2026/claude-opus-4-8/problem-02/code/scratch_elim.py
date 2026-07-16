import sympy as sp

al, ga, be, ph, ps, B, C = sp.symbols('al ga be ph ps B C', positive=True)
A = sp.pi - B - C

# rel_phi: tan ph = sin al sin ga /(cos al sin ga + 2 sin al cos ga)
rel_ph = sp.sin(ph)*(sp.cos(al)*sp.sin(ga)+2*sp.sin(al)*sp.cos(ga)) - sp.cos(ph)*sp.sin(al)*sp.sin(ga)
# constraint (I): sinC sin ga sin(A+2al+ga) - 2 sinA sin(C-al-ga) sin(al+ga)
I = sp.sin(C)*sp.sin(ga)*sp.sin(A+2*al+ga) - 2*sp.sin(A)*sp.sin(C-al-ga)*sp.sin(al+ga)

# Try to eliminate ga between rel_ph and I.  Use tan-half? Instead numeric-guess the phi relation.
# Let's just numerically find relation form: compute for fixed A? A depends on B,C. Let's fix C, A and solve.
import numpy as np
from scipy.optimize import brentq

def gamma_of(alpha, Aa, Cc):
    f=lambda g: np.sin(Cc)*np.sin(g)*np.sin(Aa+2*alpha+g)-2*np.sin(Aa)*np.sin(Cc-alpha-g)*np.sin(alpha+g)
    # root in (0, C-alpha)
    lo,hi=1e-6, Cc-alpha-1e-6
    return brentq(f,lo,hi)

def phi_of(alpha,Aa,Cc):
    g=gamma_of(alpha,Aa,Cc)
    cph=1/np.tan(alpha)+2/np.tan(g)
    return np.arctan2(1,cph)

# guess: maybe cot(phi) = cot(alpha) + 2 cot(gamma) and there's relation like
# tan(phi) related to ... Let's test candidate: sin(2phi)?  print table
Aa=np.radians(63.435); Cc=np.radians(45.0); Bb=np.pi-Aa-Cc
for adeg in [5,10,15,20,25,30]:
    alpha=np.radians(adeg)
    g=gamma_of(alpha,Aa,Cc); ph_=phi_of(alpha,Aa,Cc)
    # test some invariants
    print(f"a={adeg:5.1f} gamma={np.degrees(g):7.3f} phi={np.degrees(ph_):7.3f}  "
          f"cand1(C-al-2phi)={np.degrees(Cc-alpha-2*ph_):7.3f} "
          f"tanphi/tan(al+ga)={np.tan(ph_)/np.tan(alpha+g):.4f} "
          f"sin(al+ga)={np.sin(alpha+g):.4f}")
