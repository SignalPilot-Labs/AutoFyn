import sympy as sp
k,l,b,c,kb,lb,bb,cb,t = sp.symbols('k l b c kb lb bb cb t')
E1 = sp.expand(b*c*(kb-bb)*(lb-cb) - bb*cb*(k-b)*(l-c))
E2 = sp.expand((k-b)*(2*l-c)*cb*(lb-bb) - (kb-bb)*(2*lb-cb)*c*(l-b))
E3 = sp.expand(b*(k-c)*(lb-cb)*(2*kb-bb) - bb*(kb-cb)*(l-c)*(2*k-b))
D = k*lb - kb*l
TN = sp.expand(2*k*l*(lb-kb)*(cb-bb) + 2*kb*lb*(k-l)*(c-b) - (c*cb - b*bb)*D)

# saturate by denominator factors one at a time via ideal quotient (I:f) using groebner elimination of t
factors = [(k-b),(l-c),(kb-bb),(lb-cb),(l-b),(lb-bb),(2*k-b),(2*kb-bb),(k-c),(kb-cb),(2*l-c),(2*lb-cb)]
gens = [k,l,kb,lb]
I = [E1,E2,E3]
def saturate(I, f):
    G = sp.groebner(I+[1 - t*f], t, k,l,kb,lb, order='lex')
    # keep polys without t
    out=[p for p in G.polys if t not in p.free_symbols]
    return [p.as_expr() for p in out]
for f in factors:
    I = saturate(I, f)
G = sp.groebner(I, k,l,kb,lb, order='grevlex')
r = G.reduce(TN)
rem = sp.simplify(r[1])
print("after saturation, remainder of TN:", rem)
