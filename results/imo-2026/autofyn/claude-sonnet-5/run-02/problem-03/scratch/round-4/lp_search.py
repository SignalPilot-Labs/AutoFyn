import itertools
from fractions import Fraction as F
from scipy.optimize import linprog
import numpy as np

def ladder(n):
    denom = 2**(n+1) - 1
    return [ (2**(n+1-i)) / denom for i in range(1, n+2)]

def compositions(total_budget, parts):
    # all tuples of length parts with nonneg ints summing to <= total_budget
    def rec(parts_left, budget_left):
        if parts_left == 0:
            yield ()
            return
        for c in range(budget_left+1):
            for rest in rec(parts_left-1, budget_left-c):
                yield (c,) + rest
    seen = set()
    for comp in rec(parts, total_budget):
        seen.add(comp)
    return seen

def min_phi_for_composition(p, comp, tol=1e-9):
    n1 = len(p)
    # variables: for each piece i with comp[i]=c_i>=1, we have c_i free fragments
    # (last fragment = p_i - sum of free ones), each free fragment >=0, and last>=0
    # Build list of "elements" each is either constant (untouched piece) or a variable expr
    var_idx = 0
    elems = []  # each elem: ('const', value) or ('var', index) or ('lastvar', piece_i, list_of_var_indices)
    piece_vars = []  # for each piece, list of var indices for its free fragments (excluding last)
    for i, c in enumerate(comp):
        if c == 0:
            elems.append(('const', p[i]))
        else:
            idxs = list(range(var_idx, var_idx + c))
            var_idx += c
            for j in idxs:
                elems.append(('var', j))
            elems.append(('lastvar', i, idxs))
    nvars = var_idx
    m = len(elems)
    if nvars == 0:
        # no free vars; just compute Phi directly
        vals = sorted([e[1] for e in elems], reverse=True)
        phi = sum(vals[k] for k in range(0,len(vals),2))
        return phi, None

    best = None
    best_info = None
    # iterate over all permutations of ranks assigned to elems (which elem sits at rank 0,1,2,...)
    # elems list order arbitrary; we permute positions
    idxs_range = list(range(m))
    count = 0
    for perm in itertools.permutations(idxs_range):
        count += 1
        # perm[k] = index into elems that occupies rank k (0=highest)
        # objective: sum over even k (rank k, 0-indexed = rank k+1 1-indexed odd) of value at perm[k]
        # build objective vector c_obj (for linprog minimize)
        c_obj = np.zeros(nvars)
        const_obj = 0.0
        for k in range(m):
            if k % 2 == 0:
                e = elems[perm[k]]
                if e[0] == 'const':
                    const_obj += e[1]
                elif e[0] == 'var':
                    c_obj[e[1]] += 1
                elif e[0] == 'lastvar':
                    i, idxs = e[1], e[2]
                    const_obj += p[i]
                    for j in idxs:
                        c_obj[j] -= 1
        # constraints: ordering perm[0]>=perm[1]>=...>=perm[m-1]
        A_ub = []
        b_ub = []
        def elem_expr(e):
            vec = np.zeros(nvars); const = 0.0
            if e[0]=='const':
                const = e[1]
            elif e[0]=='var':
                vec[e[1]] = 1
            elif e[0]=='lastvar':
                i, idxs = e[1], e[2]
                const = p[i]
                for j in idxs: vec[j] -= 1
            return vec, const
        for k in range(m-1):
            v1,c1 = elem_expr(elems[perm[k]])
            v2,c2 = elem_expr(elems[perm[k+1]])
            # need elem[perm[k]] >= elem[perm[k+1]]  => v2-v1 <= c1-c2  i.e (v2-v1).x <= c1-c2
            A_ub.append(v2-v1)
            b_ub.append(c1-c2)
        # bounds: each var in [0, p_i] roughly, but also need lastvar>=0 -> encode as ub constraint
        bounds = [(0, None)]*nvars
        # add lastvar>=0 constraints per piece
        for i,c in enumerate(comp):
            if c>=1:
                idxs = [j for j in range(nvars)]  # not needed generally; handled below
        for i,c in enumerate(comp):
            if c>=1:
                # find idxs for this piece
                pass
        # Need explicit lastvar >=0 constraints
        for e in elems:
            if e[0]=='lastvar':
                i, idxs = e[1], e[2]
                # p[i] - sum(idxs) >= 0  => sum(idxs) <= p[i]
                row = np.zeros(nvars)
                for j in idxs: row[j]=1
                A_ub.append(row)
                b_ub.append(p[i])
        res = linprog(c_obj, A_ub=np.array(A_ub) if A_ub else None, b_ub=np.array(b_ub) if b_ub else None,
                       bounds=bounds, method='highs')
        if res.success:
            val = res.fun + const_obj
            if best is None or val < best - 1e-12:
                best = val
                best_info = (perm, res.x.copy(), elems, comp)
    return best, best_info

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv)>1 else 3
    p = ladder(n)
    target = 2**n / (2**(n+1)-1)
    print("n=",n,"ladder p=",p,"target c(n)=",target)
    global_min = None
    global_info = None
    comps = compositions(n, n+1)
    print("num compositions:", len(comps))
    for comp in comps:
        val, info = min_phi_for_composition(p, comp)
        if val is None: continue
        if global_min is None or val < global_min - 1e-12:
            global_min = val
            global_info = (comp, info)
    print("computed min Phi =", global_min, " target=", target)
    comp, info = global_info
    print("achieved at composition", comp)
    if info:
        perm, x, elems, comp2 = info
        print("perm(rank order elem indices):", perm)
        print("x=",x)
        print("elems:", elems)
