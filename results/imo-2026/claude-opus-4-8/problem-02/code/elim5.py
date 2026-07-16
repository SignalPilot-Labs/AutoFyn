import sympy as sp, pickle
k,l,b,c,kb,lb,bb,cb = sp.symbols('k l b c kb lb bb cb')
d = pickle.load(open('sol.pkl','rb'))



# rebuild via parse


Xs=sp.sympify(d['Xs']); Ys=sp.sympify(d['Ys']); Zs=sp.sympify(d['Zs'])

D = k*lb - kb*l
TN = 2*k*l*(lb-kb)*(cb-bb) + 2*kb*lb*(k-l)*(c-b) - (c*cb - b*bb)*D
TN_sub = TN.subs({kb:Ys, lb:Zs})
TN_sub = sp.cancel(sp.together(TN_sub))
num = sp.numer(TN_sub); den = sp.denom(TN_sub)
num = sp.expand(num)
print("TN_sub numerator is zero?:", num==0)
if num!=0:
    R = sp.cancel(Ys*Zs - Xs)
    Rnum = sp.expand(sp.numer(sp.together(R)))
    q,r = sp.div(num, Rnum, k)  # try divide as poly in k
    print("divisible by Rnum in k? remainder zero:", sp.expand(r)==0)
    # numeric check num=0 on geometry
    vals = {b:complex(-0.5,-1.5), c:complex(1.5,-1.5),
            k:complex(-0.2531182195716988,-1.1260806200681075),
            l:complex(0.7866438932120947,-1.0881436597179395)}
    vals[bb]=vals[b].conjugate(); vals[cb]=vals[c].conjugate()
    print("num numeric on geometry:", complex(num.subs(vals)))
    print("Rnum numeric:", complex(Rnum.subs(vals)))
    print("num total degree:", sp.Poly(num, k,l,b,c,bb,cb).total_degree())
    print("Rnum total degree:", sp.Poly(Rnum, k,l,b,c,bb,cb).total_degree())
