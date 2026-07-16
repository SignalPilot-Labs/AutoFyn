import sympy as sp
k,l,b,c,kb,lb,bb,cb = sp.symbols('k l b c kb lb bb cb')
E1 = b*c*(kb-bb)*(lb-cb) - bb*cb*(k-b)*(l-c)
E2 = (k-b)*(2*l-c)*cb*(lb-bb) - (kb-bb)*(2*lb-cb)*c*(l-b)
E3 = b*(k-c)*(lb-cb)*(2*kb-bb) - bb*(kb-cb)*(l-c)*(2*k-b)
D = k*lb - kb*l
TN = 2*k*l*(lb-kb)*(cb-bb) + 2*kb*lb*(k-l)*(c-b) - (c*cb - b*bb)*D
TN = sp.expand(TN)

# Groebner basis over QQ(b,c,bb,cb) in vars k,l,kb,lb
G = sp.groebner([sp.expand(E1),sp.expand(E2),sp.expand(E3)], k,l,kb,lb,
                order='grevlex')
print("GB size:", len(G.exprs))
q, r = sp.reduce(TN, G) if False else (None,None)
# use groebner reduce
r = G.reduce(TN)
print("remainder of TN mod GB:")
print(sp.simplify(r[1]))
