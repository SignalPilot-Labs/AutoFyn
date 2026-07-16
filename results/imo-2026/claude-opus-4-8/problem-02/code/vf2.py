import sympy as sp, pickle
k,l,b,c,kb,lb,bb,cb = sp.symbols('k l b c kb lb bb cb')
E1 = sp.expand(b*c*(kb-bb)*(lb-cb) - bb*cb*(k-b)*(l-c))
E2 = sp.expand((k-b)*(2*l-c)*cb*(lb-bb) - (kb-bb)*(2*lb-cb)*c*(l-b))
E3 = sp.expand(b*(k-c)*(lb-cb)*(2*kb-bb) - bb*(kb-cb)*(l-c)*(2*k-b))
def coeffs(E):
    a=E.coeff(kb,1).coeff(lb,1);p=E.coeff(kb,1).coeff(lb,0)
    q=E.coeff(kb,0).coeff(lb,1);dd=E.coeff(kb,0).coeff(lb,0);return a,p,q,dd
rows=[coeffs(E) for E in (E1,E2,E3)]
A=sp.Matrix([[r[0],r[1],r[2]] for r in rows]);rhs=sp.Matrix([-r[3] for r in rows])
sol=A.LUsolve(rhs);Xs,Ys,Zs=[sp.cancel(sol[i]) for i in range(3)]
D=k*lb-kb*l
TN=2*k*l*(lb-kb)*(cb-bb)+2*kb*lb*(k-l)*(c-b)-(c*cb-b*bb)*D
num=sp.expand(sp.numer(sp.cancel(sp.together(TN.subs({kb:Ys,lb:Zs})))))
R=sp.cancel(Ys*Zs-Xs);Rnum=sp.expand(sp.numer(sp.together(R)))
G=sp.expand(sp.gcd(num,Rnum))
qR=sp.cancel(Rnum/G); qN=sp.cancel(num/G)
print("Rnum/G =", sp.factor(qR))
print("num/G  =", sp.factor(qN))
print("Rnum==(b-k)(c-l)G:", sp.expand(Rnum-(b-k)*(c-l)*G)==0)
print("num == qN*G exact:", sp.expand(num-qN*G)==0, " qN is polynomial:", sp.denom(qN)==1)
vals={b:complex(-0.5,-1.5),c:complex(1.5,-1.5),k:complex(-0.2531182195716988,-1.1260806200681075),l:complex(0.7866438932120947,-1.0881436597179395)}
vals[bb]=vals[b].conjugate();vals[cb]=vals[c].conjugate()
print("G at geometry ~0:", abs(complex(G.subs(vals))))
print("qN at geometry:", complex(qN.subs(vals)))
pickle.dump({'G':sp.srepr(G),'qN':sp.srepr(sp.expand(qN)),'Ys':sp.srepr(Ys),'Zs':sp.srepr(Zs),'Xs':sp.srepr(Xs),'detA':sp.srepr(sp.expand(A.det()))},open('final.pkl','wb'))
print("saved")
