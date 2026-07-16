import sympy as sp
sa,ca,sb,cb,sg,cg,sB,cB,sC,cC = sp.symbols('sa ca sb cb sg cg sB cB sC cC', real=True)
sA = sB*cC+cB*sC
cA = sB*sC - cB*cC
def sin2(sx,cx,sy,cy): return sx*cy+cx*sy
def cos2(sx,cx,sy,cy): return cx*cy-sx*sy
s_ag=sin2(sa,ca,sg,cg); c_ag=cos2(sa,ca,sg,cg)
s_ab=sin2(sa,ca,sb,cb); c_ab=cos2(sa,ca,sb,cb)
s2a=sin2(sa,ca,sa,ca); c2a=cos2(sa,ca,sa,ca)
sA2a=sin2(sA,cA,s2a,c2a); cA2a=cos2(sA,cA,s2a,c2a)
sA2ag=sin2(sA2a,cA2a,sg,cg)
sA2ab=sin2(sA2a,cA2a,sb,cb)
s_Cmag=sC*c_ag-cC*s_ag
s_Bmab=sB*c_ab-cB*s_ab
I = sC*sg*sA2ag - 2*sA*s_Cmag*s_ag
II = sB*sb*sA2ab - 2*sA*s_Bmab*s_ab
p = ca*sg+2*sa*cg; qC= sa*sg; pp= ca*sb+2*sa*cb; qB= sa*sb
PC= sC*pp+cC*qB; PB= sB*p +cB*qC
NC2= qC**2+p**2; NB2= qB**2+pp**2
W = sA*(p*pp-qC*qB) - cA*(qC*pp+p*qB)
sCB= sC*cB-cC*sB
D = sp.expand(sC*PC*s_ab*NC2 - sB*PB*s_ag*NB2 - sCB*W*s_ag*s_ab)

# extract f by matching the part of D that carries sg/cg to leading total degree in {sg,cg}
# Hypothesis D = f*I + g*II + pyth-combos, f indep of sg,cg ; g indep of sb,cb.
# Strategy: reduce sb^2->1-cb^2, sg^2->1-cg^2 everywhere to normal form, then treat.
pg=sg**2-(1-cg**2); pb=sb**2-(1-cb**2)
def nf(e):
    e=sp.expand(e)
    e=sp.expand(e.subs(sg**2,1-cg**2).subs(sb**2,1-cb**2))
    e=sp.expand(e.subs(sg**2,1-cg**2).subs(sb**2,1-cb**2))
    return e
Dn=nf(D); In=nf(I); IIn=nf(II)
# In depends on sg,cg (deg<=1 after nf? sg*sg reduced). Try f = ratio of coeff of sg in D-part...
# Collect Dn in sg: Dn = A0 + A1*sg (A0,A1 polynomials in cg and beta,B,C, sa,ca)
A1=sp.expand(Dn.coeff(sg,1)); A0=sp.expand(Dn.coeff(sg,0))
I1=sp.expand(In.coeff(sg,1)); I0=sp.expand(In.coeff(sg,0))
# f should satisfy A1 = f*I1 + (g*II has no sg =>0)  => f = A1/I1 (if II indep of sg -> yes)
f=sp.simplify(A1/I1)
print("f=",f)
# then check A0 - f*I0 = g*II with g indep of sb? and A0-f*I0 should be divisible pattern
R0=sp.expand(A0-f*I0)
# now R0 should equal g*IIn. Collect in sb.
IIb1=sp.expand(IIn.coeff(sb,1)); IIb0=sp.expand(IIn.coeff(sb,0))
R0b1=sp.expand(R0.coeff(sb,1)); R0b0=sp.expand(R0.coeff(sb,0))
g=sp.simplify(R0b1/IIb1)
print("g=",g)
final=sp.simplify(R0b0-g*IIb0)
print("final residual (should be 0):", final)
