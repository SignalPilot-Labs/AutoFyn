import sympy as sp
from itertools import combinations
from fractions import Fraction as F

p1v, p2v, p3v = sp.Rational(4,7), sp.Rational(2,7), sp.Rational(1,7)

def oddsum_sym(vals):
    # vals: list of sympy Rationals
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def solve_shape_3way(S_val, background, tie_targets, label):
    a,b = sp.symbols('a b')
    c_ = S_val - a - b
    constraints = {
        'a=0': sp.Eq(a,0),
        'b=0': sp.Eq(b,0),
        'c=0': sp.Eq(c_,0),
        'a=b': sp.Eq(a,b),
        'a=c': sp.Eq(a,c_),
        'b=c': sp.Eq(b,c_),
    }
    for i,t in enumerate(tie_targets):
        constraints[f'a=t{i}'] = sp.Eq(a,t)
        constraints[f'b=t{i}'] = sp.Eq(b,t)
        constraints[f'c=t{i}'] = sp.Eq(c_,t)
    names = list(constraints.keys())
    found = {}
    for n1,n2 in combinations(names,2):
        sol = sp.solve([constraints[n1], constraints[n2]], [a,b], dict=True)
        for s in sol:
            if a in s and b in s:
                av,bv = s[a], s[b]
            else:
                continue
            cv = S_val - av - bv
            if av>=0 and bv>=0 and cv>=0:
                found[(av,bv,cv)] = True
    best=None; bestpt=None
    for (av,bv,cv) in found:
        os = oddsum_sym([av,bv,cv]+background)
        if best is None or os<best:
            best=os; bestpt=(av,bv,cv)
    print(f"Shape {label}: {len(found)} candidates, min OddSum = {best} (={sp.nsimplify(best)}), c2=4/7 match: {best==sp.Rational(4,7)}, at {bestpt}")
    return best,bestpt

# (0,2,0): split p2 into a,b,c; background p1,p3
solve_shape_3way(p2v, [p1v,p3v], [p1v,p3v], "(0,2,0)")
# (0,0,2): split p3 into a,b,c; background p1,p2
solve_shape_3way(p3v, [p1v,p2v], [p1v,p2v], "(0,0,2)")
