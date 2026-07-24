import sympy as sp
from itertools import combinations, product
from fractions import Fraction

def ladder(n):
    D = 2**(n+1) - 1
    return [sp.Rational(2**(n+1-i), D) for i in range(1, n+2)], D

def compositions_leq(total, slots):
    # all tuples of length `slots` nonneg ints summing to <= total
    def rec(slots, remaining):
        if slots == 1:
            for v in range(remaining+1):
                yield (v,)
            return
        for v in range(remaining+1):
            for rest in rec(slots-1, remaining-v):
                yield (v,) + rest
    yield from rec(slots, total)

def build_fragments(p, comp):
    # returns list of (piece_index, frag_index, sympy_expr), list of free symbols
    syms = []
    frags = []  # list of expr
    frag_owner = []  # (piece_idx) each frag belongs to, for bookkeeping
    for i, ci in enumerate(comp):
        pi = p[i]
        if ci == 0:
            frags.append(sp.sympify(pi))
            frag_owner.append(i)
        else:
            local = [sp.Symbol(f'y_{i}_{j}') for j in range(ci)]
            syms.extend(local)
            for s in local:
                frags.append(s)
                frag_owner.append(i)
            frags.append(pi - sum(local))
            frag_owner.append(i)
    return frags, syms, frag_owner

def A_of_multiset(vals):
    # vals: list of sympy Rational; sort descending, alternate sum
    vs = sorted(vals, reverse=True)
    s = sp.Integer(0)
    sign = 1
    for v in vs:
        s += sign*v
        sign = -sign
    return sp.nsimplify(s)

def vertex_min_for_composition(p, comp, verbose=False):
    frags, syms, owner = build_fragments(p, comp)
    d = len(syms)
    m = len(frags)
    if d == 0:
        # no free params, single point
        val = A_of_multiset(frags)
        return val, frags
    # build constraint candidates: zero-constraints for frags that depend on syms (i.e. not pure constants)
    zero_constraints = []
    for f in frags:
        if f.free_symbols:
            zero_constraints.append(sp.Eq(f, 0))
    tie_constraints = []
    for i in range(m):
        for j in range(i+1, m):
            fi, fj = frags[i], frags[j]
            if fi.free_symbols or fj.free_symbols:
                # skip trivial identical exprs
                if sp.simplify(fi - fj) != 0:
                    tie_constraints.append(sp.Eq(fi, fj))
    all_constraints = zero_constraints + tie_constraints
    best = None
    best_point = None
    seen_solutions = set()
    for subset in combinations(all_constraints, d):
        try:
            sol = sp.linsolve(subset, syms)
        except Exception:
            continue
        if not sol:
            continue
        sol = list(sol)
        if len(sol) != 1:
            continue
        point = sol[0]
        if any(s.free_symbols for s in point):
            continue  # underdetermined, not a true vertex
        subs = dict(zip(syms, point))
        key = tuple(point)
        if key in seen_solutions:
            continue
        seen_solutions.add(key)
        # check feasibility: all frags >=0
        vals = [f.subs(subs) for f in frags]
        if all(v >= 0 for v in vals):
            A = A_of_multiset(vals)
            if best is None or A < best:
                best = A
                best_point = subs
    return best, best_point

def A_min_for_c(n, c, p, verbose=False):
    best = None
    bestinfo = None
    tail_slots = n  # slots 2..n+1 -> n slots
    for tailcomp in compositions_leq(n-c, tail_slots):
        comp = (c,) + tailcomp
        val, point = vertex_min_for_composition(p, comp)
        if val is None:
            continue
        if best is None or val < best:
            best = val
            bestinfo = (comp, point)
    return best, bestinfo

for n in [3,4]:
    p, D = ladder(n)
    fn = sp.Rational(1, D)
    print(f"=== n={n}, D={D}, target f(n)=1/D={fn} ===")
    for c in range(0, n+1):
        best, info = A_min_for_c(n, c, p)
        print(f"  c={c}: A_min(c) = {best}  (={float(best):.6f})  target={float(fn):.6f}  comp={info[0] if info else None}")
