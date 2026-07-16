import sympy as sp, pickle, numpy as np, random
k,l,b,c,kb,lb,bb,cb = sp.symbols('k l b c kb lb bb cb')
d = pickle.load(open('sol.pkl','rb'))
Xs=sp.sympify(d['Xs']); Ys=sp.sympify(d['Ys']); Zs=sp.sympify(d['Zs'])
D = k*lb - kb*l
TN = 2*k*l*(lb-kb)*(cb-bb) + 2*kb*lb*(k-l)*(c-b) - (c*cb - b*bb)*D
num = sp.expand(sp.numer(sp.cancel(sp.together(TN.subs({kb:Ys, lb:Zs})))))
R = sp.cancel(Ys*Zs - Xs); Rnum = sp.expand(sp.numer(sp.together(R)))
Rpoly = sp.Poly(Rnum, k)
# candidate factors (in k,l,b,c,bb,cb after kb->Ys,lb->Zs? factors of holomorphic denoms in k,l only)
cand = {'k-b':k-b,'l-c':l-c,'l-b':l-b,'2k-b':2*k-b,'k-c':k-c,'2l-c':2*l-c,
        'k-l':k-l, 'k':k,'l':l, }
P4 = b**2*c*k - 3*b**2*c*l + 2*b**2*l**2 - 3*b*c**2*k + b*c**2*l + 8*b*c*k*l - 6*b*k*l**2 + 2*c**2*k**2 - 6*c*k**2*l + 4*k**2*l**2
cand['P4']=P4
random.seed(1)
for trial in range(8):
    sub = {v: complex(random.uniform(-2,2),random.uniform(-2,2)) for v in (l,b,c,bb,cb)}
    coeffs = [complex(cf.subs(sub)) for cf in Rpoly.all_coeffs()]
    for kr in np.roots(coeffs):
        s = dict(sub); s[k]=complex(kr)
        nval = abs(complex(num.subs(s)))
        if nval>1e-3:  # spurious branch
            facs = {name: abs(complex(expr.subs(s))) for name,expr in cand.items()}
            small = {nm:v for nm,v in facs.items() if v<1e-6}
            print(f"spurious num={nval:.2e} small factors: {small}")
