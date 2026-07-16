import sympy as sp

# atomic symbols
sa,ca,sb,cb,sg,cg,sB,cB,sC,cC = sp.symbols('sa ca sb cb sg cg sB cB sC cC', real=True)
# A = pi-B-C: sinA=sin(B+C)=sB cC+cB sC ; cosA=-cos(B+C)=-(cB cC - sB sC)=sB sC - cB cC
sA = sB*cC+cB*sC
cA = sB*sC - cB*cC

def S(x):  # sin of sum given as list of (s,c) pairs? We'll build directly.
    pass

# helper sin(x+y) with (sx,cx),(sy,cy)
def sin2(sx,cx,sy,cy): return sx*cy+cx*sy
def cos2(sx,cx,sy,cy): return cx*cy-sx*sy

# angle sums we need:
# alpha+gamma
s_ag=sin2(sa,ca,sg,cg); c_ag=cos2(sa,ca,sg,cg)
# alpha+beta
s_ab=sin2(sa,ca,sb,cb); c_ab=cos2(sa,ca,sb,cb)
# A+2al+gamma : (A+2al)+gamma ; first s(A+2al),c(A+2al)
s2a=sin2(sa,ca,sa,ca); c2a=cos2(sa,ca,sa,ca)      # 2alpha
sA2a=sin2(sA,cA,s2a,c2a); cA2a=cos2(sA,cA,s2a,c2a) # A+2alpha
sA2ag=sin2(sA2a,cA2a,sg,cg)                        # A+2al+gamma
sA2ab=sin2(sA2a,cA2a,sb,cb)                        # A+2al+beta
# C-al-gamma
s_Cag=sin2(sC,cC,-(sa*cg+ca*sg-2*sa*cg),0)  # placeholder -- do properly below
# proper: C-(al+gamma): sin(C-(al+ga))=sC c_ag - cC s_ag
s_Cmag=sC*c_ag-cC*s_ag
# B-(al+beta)
s_Bmab=sB*c_ab-cB*s_ab

# constraints
I = sC*sg*sA2ag - 2*sA*s_Cmag*s_ag
II = sB*sb*sA2ab - 2*sA*s_Bmab*s_ab

# building blocks for (5)
p = ca*sg+2*sa*cg          # C-side
qC= sa*sg
pp= ca*sb+2*sa*cb          # B-side
qB= sa*sb
PC= sC*pp+cC*qB
PB= sB*p +cB*qC
NC2= qC**2+p**2
NB2= qB**2+pp**2
W = sA*(p*pp-qC*qB) - cA*(qC*pp+p*qB)
sCB= sC*cB-cC*sB  # sin(C-B)

D = sC*PC*s_ab*NC2 - sB*PB*s_ag*NB2 - sCB*W*s_ag*s_ab

# Reduce D modulo pythagoras using groebner basis on {I,II,pyth}
pyth=[sa**2+ca**2-1, sb**2+cb**2-1, sg**2+cg**2-1, sB**2+cB**2-1, sC**2+cC**2-1]
gens=[sa,ca,sb,cb,sg,cg,sB,cB,sC,cC]
print("building groebner...")
G=sp.groebner(pyth+[I,II], *gens, order='grevlex')
print("reducing D...")
r=G.reduce(sp.expand(D))[1]
print("remainder:", sp.simplify(r))
