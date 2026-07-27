import sympy as sp
sa,ca,sA,cA,tb,tg=sp.symbols('sa ca sA cA tb tg')
inner=2*cA*ca*sa*tb*tg - cA*sa**2*tb**2*tg - cA*sa**2*tb*tg**2 + cA*sa**2*tb + cA*sa**2*tg - ca**2*sA*tb*tg + ca*sA*sa*tb**2*tg + ca*sA*sa*tb*tg**2 - ca*sA*sa*tb - ca*sA*sa*tg - sA*sa**2*tb**2*tg**2 + sA*sa**2*tb**2 + sA*sa**2*tb*tg + sA*sa**2*tg**2 - sA*sa**2
# proposed collected form
sinAm=sa*cA-ca*sA  # sin(alpha-A)? = sa*cA-ca*sA = sin(α-A)=-sin(A-α)
P1=sA*sa**2*(tb**2-1)*(1-tg**2)
P2=(ca*sA*sa-cA*sa**2)*tb*tg*(tb+tg)
P3=-(ca*sA*sa-cA*sa**2)*(tb+tg)
P4=(2*cA*ca*sa-ca**2*sA+sA*sa**2)*tb*tg
coll=P1+P2+P3+P4
print("inner-coll =",sp.expand(inner-coll))
# So inner = sA*sa^2*(tb^2-1)(1-tg^2) + sa*sin(A-α)*[-tb*tg(tb+tg)+(tb+tg)] + (..)*tb*tg
# simplify P2+P3 = sa*(ca*sA-cA*sa)*(tb+tg)*(1-tb*tg)
# ca*sA-cA*sa = sin(A-α)
print("ca*sA-cA*sa = sin(A-α) coeff; P2+P3 = sa*(ca*sA-cA*sa)*(tb+tg)*(1-tb*tg)?")
print(sp.expand(P2+P3 - sa*(ca*sA-cA*sa)*(tb+tg)*(1-tb*tg)))
# P4 coeff: 2*cA*ca*sa-ca**2*sA+sA*sa**2 = sa*sin(2A)? check: sin(2A)=2 sA cA. sa*2 sA cA vs 2 cA ca sa -> different.
# = sa*(2 cA ca) + sA*(sa^2-ca^2) = sa*sin(2A?)*... leave as is. Try: = sin(α)*sin(2A)*ca/sA? no.
# Check if = sa*sA*( ... ). Just present as 2 cA ca sa + sA(sa^2-ca^2).
print("P4 coeff =",2*cA*ca*sa-ca**2*sA+sA*sa**2)
