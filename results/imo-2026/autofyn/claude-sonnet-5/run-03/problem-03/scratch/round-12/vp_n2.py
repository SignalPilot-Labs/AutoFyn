import numpy as np
from scipy.optimize import minimize
from fractions import Fraction as Fr

def oddsum(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def softmax(x):
    e = np.exp(x - np.max(x))
    return e/e.sum()

def V_shape_noSplit(p):
    return oddsum(list(p))

def V_shape_1cut(p, i, restarts=25):
    # split p[i] into 2 parts
    others = [p[j] for j in range(len(p)) if j != i]
    best = None
    for _ in range(restarts):
        x0 = np.random.randn(2)
        def f(x):
            frac = softmax(x)
            frags = list(p[i]*frac)
            return oddsum(others+frags)
        res = minimize(f, x0, method='Nelder-Mead',
                        options={'xatol':1e-10,'fatol':1e-12,'maxiter':2000})
        if best is None or res.fun < best:
            best = res.fun
    # also check pure ties / boundary heuristics via fine grid
    for frac1 in np.linspace(1e-6, 1-1e-6, 4000):
        frags=[p[i]*frac1, p[i]*(1-frac1)]
        val = oddsum(others+frags)
        if best is None or val < best:
            best = val
    return best

def V_shape_2cut_same(p, i, restarts=25):
    others = [p[j] for j in range(len(p)) if j != i]
    best = None
    for _ in range(restarts):
        x0 = np.random.randn(3)
        def f(x):
            frac = softmax(x)
            frags = list(p[i]*frac)
            return oddsum(others+frags)
        res = minimize(f, x0, method='Nelder-Mead',
                        options={'xatol':1e-10,'fatol':1e-12,'maxiter':3000})
        if best is None or res.fun < best:
            best = res.fun
    return best

def V_shape_2cut_diff(p, i, j, restarts=30):
    others = [p[m] for m in range(len(p)) if m not in (i,j)]
    best = None
    for _ in range(restarts):
        x0 = np.random.randn(4)
        def f(x):
            fraci = softmax(x[:2])
            fracj = softmax(x[2:])
            frags = list(p[i]*fraci) + list(p[j]*fracj)
            return oddsum(others+frags)
        res = minimize(f, x0, method='Nelder-Mead',
                        options={'xatol':1e-10,'fatol':1e-12,'maxiter':3000})
        if best is None or res.fun < best:
            best = res.fun
    return best

def V(p, restarts=20):
    p = list(p)
    n = len(p)
    best = V_shape_noSplit(p)
    for i in range(n):
        best = min(best, V_shape_1cut(p, i, restarts))
    for i in range(n):
        best = min(best, V_shape_2cut_same(p, i, restarts))
    for i in range(n):
        for j in range(i+1, n):
            best = min(best, V_shape_2cut_diff(p, i, j, restarts))
    return best

if __name__ == "__main__":
    np.random.seed(0)
    gamma2 = Fr(1,7)
    c2 = Fr(4,7)
    e0 = (Fr(10,21), Fr(7,21), Fr(4,21))
    e1 = (Fr(1,2), Fr(9,28), Fr(5,28))
    e2 = (Fr(1,2), Fr(5,14), Fr(1,7))
    for name, pt in [("e0", e0), ("e1", e1), ("e2", e2)]:
        pf = [float(x) for x in pt]
        v = V(pf, restarts=30)
        print(name, pf, "V=", v, "c(2)=", float(c2))

def interior_point(a, g1, g2):
    # region B(2): p1=1/2-a, p1-p2=gamma+g1, p2-p3=gamma+g2
    gamma = 1/7
    p1 = 0.5 - a
    p2 = p1 - (gamma+g1)
    p3 = p2 - (gamma+g2)
    return (p1,p2,p3)

def test_monotone(p_interior, q_boundary, N=9, restarts=25, label=""):
    p_interior = np.array(p_interior); q_boundary = np.array(q_boundary)
    print(f"--- {label}: interior {p_interior} -> boundary {q_boundary} ---")
    vals=[]
    for t in np.linspace(0,1,N):
        pt = (1-t)*p_interior + t*q_boundary
        v = V(list(pt), restarts=restarts)
        vals.append(v)
        print(f"  t={t:.3f} p={pt} V={v:.6f}")
    diffs = np.diff(vals)
    print("  diffs:", np.round(diffs,6), "monotone nondecreasing (toward boundary)?", np.all(diffs>=-1e-4))
    return vals

if __name__ == "__main__" and False:
    pass

def bary(a,g1,g2):
    K = 1/14
    return (3*a/K, 2*g1/K, g2/K)

def from_bary(al0,al1,al2):
    K = 1/14
    return (al0*K/3, al1*K/2, al2*K)

def facet_target(a,g1,g2, drop_idx):
    al = list(bary(a,g1,g2))
    al[drop_idx] = 0.0
    s = sum(al)
    al = [x/s for x in al]
    return from_bary(*al)

def test_facet(a,g1,g2, drop_idx, N=7, restarts=20):
    names={0:'a->0 (opp e0)',1:'g1->0 (opp e1)',2:'g2->0 (opp e2)'}
    p_int = interior_point(a,g1,g2)
    aq,g1q,g2q = facet_target(a,g1,g2,drop_idx)
    p_bnd = interior_point(aq,g1q,g2q)
    return test_monotone(p_int, p_bnd, N=N, restarts=restarts, label=names[drop_idx]+f' a,g1,g2=({a},{g1},{g2})')
