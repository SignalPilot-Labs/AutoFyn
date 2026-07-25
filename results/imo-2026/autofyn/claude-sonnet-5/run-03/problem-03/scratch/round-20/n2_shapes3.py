import sympy as sp
from itertools import combinations

p1v, p2v, p3v = sp.Rational(4,7), sp.Rational(2,7), sp.Rational(1,7)

def oddsum_sym(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def solve_shape_two_splits(PX, PY, background, label):
    # split PX into a, PX-a ; PY into b, PY-b ; background is list of remaining fixed pieces
    a,b = sp.symbols('a b')
    frag_defs = {'a':a, 'PXa':PX-a, 'b':b, 'PYb':PY-b}
    exprs = [a, PX-a, b, PY-b]
    names_lin = ['a','PXa','b','PYb']
    box_constraints = {
        'a=0': sp.Eq(a,0), 'a=PX': sp.Eq(a,PX),
        'b=0': sp.Eq(b,0), 'b=PY': sp.Eq(b,PY),
    }
    tie_constraints = {}
    all_vals_for_ties = exprs + background
    # ties among the four fragment exprs and background constants (pairwise a=const etc.)
    for i in range(len(exprs)):
        for bgv in background:
            tie_constraints[f'{names_lin[i]}={bgv}'] = sp.Eq(exprs[i], bgv)
    for i,j in combinations(range(len(exprs)),2):
        tie_constraints[f'{names_lin[i]}={names_lin[j]}'] = sp.Eq(exprs[i], exprs[j])

    constraints = {**box_constraints, **tie_constraints}
    names = list(constraints.keys())
    found = {}
    for n1,n2 in combinations(names,2):
        try:
            sol = sp.solve([constraints[n1], constraints[n2]], [a,b], dict=True)
        except Exception:
            continue
        for s in sol:
            if a in s and b in s:
                av,bv = s[a], s[b]
            else:
                continue
            if av>=0 and av<=PX and bv>=0 and bv<=PY:
                found[(av,bv)] = True
    best=None; bestpt=None
    for (av,bv) in found:
        vals = [av, PX-av, bv, PY-bv] + background
        os = oddsum_sym(vals)
        if best is None or os<best:
            best=os; bestpt=(av,bv)
    print(f"Shape {label}: {len(found)} candidates, min OddSum = {best}, c2=4/7 match(equal): {best==sp.Rational(4,7)}, at a,b={bestpt}")
    return best,bestpt

# (1,1,0): split p1,p2; background p3
solve_shape_two_splits(p1v, p2v, [p3v], "(1,1,0)")
# (1,0,1): split p1,p3; background p2
solve_shape_two_splits(p1v, p3v, [p2v], "(1,0,1)")
# (0,1,1): split p2,p3; background p1
solve_shape_two_splits(p2v, p3v, [p1v], "(0,1,1)")
