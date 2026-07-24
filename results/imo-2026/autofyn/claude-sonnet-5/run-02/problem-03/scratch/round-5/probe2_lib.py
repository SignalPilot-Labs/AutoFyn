from fractions import Fraction as F
from itertools import combinations
import time

def ladder(n):
    D = 2**(n+1) - 1
    return [F(2**(n+1-i), D) for i in range(1, n+2)], D

def compositions_leq(total, slots):
    def rec(slots, remaining):
        if slots == 1:
            for v in range(remaining+1):
                yield (v,)
            return
        for v in range(remaining+1):
            for rest in rec(slots-1, remaining-v):
                yield (v,) + rest
    yield from rec(slots, total)

# fragment representation: (coeff_vector tuple of Fractions length d, const Fraction)
def build_fragments(p, comp):
    d = sum(comp)
    frags = []  # (coeffvec, const)
    sym_ptr = 0
    for i, ci in enumerate(comp):
        pi = p[i]
        if ci == 0:
            zero = tuple(F(0) for _ in range(d))
            frags.append((zero, pi))
        else:
            local_idxs = list(range(sym_ptr, sym_ptr+ci))
            sym_ptr += ci
            for idx in local_idxs:
                vec = [F(0)]*d
                vec[idx] = F(1)
                frags.append((tuple(vec), F(0)))
            vec = [F(0)]*d
            for idx in local_idxs:
                vec[idx] = F(-1)
            frags.append((tuple(vec), pi))
    return frags, d

def vec_sub(a, b):
    (va,ca),(vb,cb) = a,b
    return (tuple(x-y for x,y in zip(va,vb)), ca-cb)

def solve_linear(eqs, d):
    # eqs: list of (coeffvec length d, rhs) meaning coeffvec . x = rhs
    # augmented matrix
    M = [list(vec)+[rhs] for vec, rhs in eqs]
    n = len(M)
    if n != d:
        return None
    # Gaussian elimination with Fraction
    for col in range(d):
        piv = None
        for r in range(col, n):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            return None  # singular
        M[col], M[piv] = M[piv], M[col]
        pivval = M[col][col]
        M[col] = [x / pivval for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                factor = M[r][col]
                M[r] = [a - factor*b for a,b in zip(M[r], M[col])]
    return [M[i][d] for i in range(d)]

def eval_frag(frag, x):
    vec, const = frag
    return sum(c*xi for c,xi in zip(vec,x)) + const

def A_of_vals(vals):
    vs = sorted(vals, reverse=True)
    s = F(0)
    sign = 1
    for v in vs:
        s += sign*v
        sign = -sign
    return s

def dedup_add(eqvecs, cand):
    return eqvecs + [cand]

def vertex_min_for_composition(p, comp):
    frags, d = build_fragments(p, comp)
    m = len(frags)
    if d == 0:
        vals = [c for (_,c) in frags]
        return A_of_vals(vals), comp, None
    # candidate equations: zero constraints (frag = 0) for frags with nonzero coeff vec
    cand_eqs = []
    for f in frags:
        vec, const = f
        if any(v != 0 for v in vec):
            cand_eqs.append((vec, -const))  # vec.x = -const  i.e. vec.x+const=0
    for i in range(m):
        for j in range(i+1, m):
            vi, ci = frags[i]
            vj, cj = frags[j]
            vec = tuple(a-b for a,b in zip(vi,vj))
            const = ci-cj
            if any(v!=0 for v in vec):
                cand_eqs.append((vec, -const))
    best = None
    bestpt = None
    seen = set()
    for subset in combinations(cand_eqs, d):
        sol = solve_linear(subset, d)
        if sol is None:
            continue
        key = tuple(sol)
        if key in seen:
            continue
        seen.add(key)
        vals = [eval_frag(f, sol) for f in frags]
        if all(v >= 0 for v in vals):
            A = A_of_vals(vals)
            if best is None or A < best:
                best = A
                bestpt = sol
    return best, comp, bestpt

def A_min_for_c(n, c, p):
    best = None
    bestinfo = None
    tail_slots = n
    for tailcomp in compositions_leq(n-c, tail_slots):
        comp = (c,) + tailcomp
        val, comp_, pt = vertex_min_for_composition(p, comp)
        if val is None:
            continue
        if best is None or val < best:
            best = val
            bestinfo = (comp, pt)
    return best, bestinfo

