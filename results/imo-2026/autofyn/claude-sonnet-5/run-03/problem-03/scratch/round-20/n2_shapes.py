from fractions import Fraction as F
from itertools import combinations

p1, p2, p3 = F(4,7), F(2,7), F(1,7)
c2 = F(4,7)

def oddsum(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def check_min_over_vertices(candidates, background, split_names, tol_name):
    """candidates: list of dict free_var->value (exact Fractions), background: list of fixed values"""
    best = None
    bestpt = None
    results = []
    for pt in candidates:
        vals = list(pt.values()) + background
        # feasibility: all free vars >0, and any implied remaining var too (handled by caller)
        os = oddsum(vals)
        results.append((pt, os))
        if best is None or os < best:
            best = os
            bestpt = pt
    return best, bestpt, results

# ---------- Shape (2,0,0): split p1 into a,b,c ; background p2,p3 ----------
S = p1
bg = [p2, p3]
lines_vals = [F(0), p2, p3]  # a or b or c could equal these, plus a=b,a=c,b=c, a+b=S(c=0) etc.
cands = []
# vertices: intersection of two constraints among: a=0,b=0,c=0(a+b=S), a=b,a=c,b=c, a=p2,a=p3,b=p2,b=p3,c=p2,c=p3
# We'll enumerate a,b via solving systems using sympy for generality
import sympy as sp
a,b = sp.symbols('a b')
S_ = sp.Rational(4,7)
p2_ = sp.Rational(2,7); p3_ = sp.Rational(1,7)
c_ = S_ - a - b

constraints = {
    'a=0': sp.Eq(a,0),
    'b=0': sp.Eq(b,0),
    'c=0': sp.Eq(c_,0),
    'a=b': sp.Eq(a,b),
    'a=c': sp.Eq(a,c_),
    'b=c': sp.Eq(b,c_),
    'a=p2': sp.Eq(a,p2_),
    'a=p3': sp.Eq(a,p3_),
    'b=p2': sp.Eq(b,p2_),
    'b=p3': sp.Eq(b,p3_),
    'c=p2': sp.Eq(c_,p2_),
    'c=p3': sp.Eq(c_,p3_),
}
names = list(constraints.keys())
found = {}
for n1,n2 in combinations(names,2):
    sol = sp.solve([constraints[n1], constraints[n2]], [a,b], dict=True)
    for s in sol:
        if a in s and b in s:
            av, bv = s[a], s[b]
        elif a in s:
            av = s[a]; bv = b  # underdetermined, skip
            continue
        else:
            continue
        cv = S_ - av - bv
        # feasibility a,b,c >=0
        if av>=0 and bv>=0 and cv>=0:
            key = (av,bv,cv)
            found[key]=True

print("Shape (2,0,0): candidate vertices found:", len(found))
best=None; bestpt=None
for (av,bv,cv) in found:
    A,B,C = F(int(av.p),int(av.q)), F(int(bv.p),int(bv.q)), F(int(cv.p),int(cv.q))
    os = oddsum([A,B,C,p2,p3])
    if best is None or os<best:
        best=os; bestpt=(A,B,C)
print("min OddSum:", best, "= 4/7?", best==c2, "at", bestpt)
