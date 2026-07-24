import itertools
from scipy.optimize import linprog
import numpy as np

def ladder(n):
    denom = 2**(n+1) - 1
    return [ (2**(n+1-i)) / denom for i in range(1, n+2)]

def compositions(total_budget, parts):
    def rec(parts_left, budget_left):
        if parts_left == 0:
            yield ()
            return
        for c in range(budget_left+1):
            for rest in rec(parts_left-1, budget_left-c):
                yield (c,) + rest
    return list(rec(parts, total_budget))

def build_elems(p, comp):
    var_idx = 0
    elems = []
    for i, c in enumerate(comp):
        if c == 0:
            elems.append(('const', p[i], i))
        else:
            idxs = list(range(var_idx, var_idx + c))
            var_idx += c
            for j in idxs:
                elems.append(('var', j, i))
            elems.append(('lastvar', idxs, i))
    nvars = var_idx
    return elems, nvars

def elem_expr(e, nvars, p):
    vec = np.zeros(nvars); const = 0.0
    if e[0]=='const':
        const = e[1]
    elif e[0]=='var':
        vec[e[1]] = 1
    elif e[0]=='lastvar':
        idxs, i = e[1], e[2]
        const = p[i]
        for j in idxs: vec[j] -= 1
    return vec, const

def min_phi_for_composition(p, comp):
    elems, nvars = build_elems(p, comp)
    m = len(elems)
    if nvars == 0:
        vals = sorted([e[1] for e in elems], reverse=True)
        phi = sum(vals[k] for k in range(0,len(vals),2))
        return phi, None

    # group indices by piece for internal-order symmetry reduction
    # permute only over "distinguishable" arrangements: treat vars of same piece as interchangeable
    # We'll generate permutations of elems but skip those where within-piece var order is not descending
    # (fix canonical order within each piece's free vars to reduce redundant permutations)
    piece_of_pos = [e[2] for e in elems]
    var_positions_by_piece = {}
    for pos,e in enumerate(elems):
        if e[0]=='var':
            var_positions_by_piece.setdefault(e[2], []).append(pos)

    best = None
    best_info = None
    idxs_range = list(range(m))
    for perm in itertools.permutations(idxs_range):
        # canonical check: for each piece, the var-elems (by original position) must appear
        # in descending rank order in perm (i.e. earlier original var-index appears at <= rank of later)
        ok = True
        for piece, positions in var_positions_by_piece.items():
            # find rank (index in perm) of each position
            ranks = [perm.index(pos) for pos in positions]
            if ranks != sorted(ranks):
                ok = False
                break
        if not ok:
            continue
        c_obj = np.zeros(nvars)
        const_obj = 0.0
        for k in range(m):
            if k % 2 == 0:
                vec, const = elem_expr(elems[perm[k]], nvars, p)
                c_obj += vec
                const_obj += const
        A_ub = []
        b_ub = []
        for k in range(m-1):
            v1,c1 = elem_expr(elems[perm[k]], nvars, p)
            v2,c2 = elem_expr(elems[perm[k+1]], nvars, p)
            A_ub.append(v2-v1)
            b_ub.append(c1-c2)
        for e in elems:
            if e[0]=='lastvar':
                idxs, i = e[1], e[2]
                row = np.zeros(nvars)
                for j in idxs: row[j]=1
                A_ub.append(row)
                b_ub.append(p[i])
        bounds = [(0, None)]*nvars
        res = linprog(c_obj, A_ub=np.array(A_ub) if A_ub else None, b_ub=np.array(b_ub) if b_ub else None,
                       bounds=bounds, method='highs')
        if res.success:
            val = res.fun + const_obj
            if best is None or val < best - 1e-9:
                best = val
                best_info = [(perm, res.x.copy(), val)]
            elif abs(val - best) < 1e-9:
                best_info.append((perm, res.x.copy(), val))
    return best, best_info

def describe_vertex(elems, perm, x, p, tol=1e-6):
    def val_of(e):
        if e[0]=='const': return e[1]
        if e[0]=='var': return x[e[1]]
        if e[0]=='lastvar':
            idxs,i = e[1],e[2]
            return p[i] - sum(x[j] for j in idxs)
    vals = [val_of(elems[perm[k]]) for k in range(len(perm))]
    labels = []
    for k in range(len(perm)):
        e = elems[perm[k]]
        labels.append((e[2], e[0]))
    return vals, labels

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv)>1 else 3
    p = ladder(n)
    target = 2**n / (2**(n+1)-1)
    print("n=",n,"ladder p=",[round(v,5) for v in p],"target c(n)=",target)
    comps = compositions(n, n+1)
    print("num compositions:", len(comps))
    global_min = None
    winners = []
    for comp in comps:
        val, info = min_phi_for_composition(p, comp)
        if val is None: continue
        if global_min is None or val < global_min - 1e-9:
            global_min = val
            winners = [(comp, info)]
        elif abs(val - global_min) < 1e-7:
            winners.append((comp, info))
    print("computed global min Phi =", global_min, " target=", target, " diff=", global_min-target)
    print("num winning compositions (tied at min):", len(winners))
    for comp, info in winners:
        elems, nvars = build_elems(p, comp)
        print("--- composition", comp)
        for perm, x, val in info:
            vals, labels = describe_vertex(elems, perm, x, p)
            print("   vals(desc):", [round(v,5) for v in vals])
            print("   piece-labels:", labels)
