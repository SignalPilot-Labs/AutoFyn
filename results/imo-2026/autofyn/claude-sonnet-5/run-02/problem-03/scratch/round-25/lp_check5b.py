from scipy.optimize import linprog

a3 = 8/15

def run(eps):
    def base_constraints():
        A=[]; b=[]
        A.append([-1,1,0,0]); b.append(0)
        A.append([0,-1,1,0]); b.append(0)
        A.append([0,0,-1,1]); b.append(0)
        A.append([0,0,0,-1]); b.append(-eps)
        A.append([1,0,0,0]); b.append(0.5-eps)
        A.append([0,-1,0,0]); b.append(-1/15-eps)
        A.append([0,1,0,0]); b.append(4/15-eps)
        return A,b

    def g14(): return [0, -0.5, 0.5, 0], (a3-0.5)
    def g12(): return [0,0,-0.5,0.5], (a3-0.5)
    def gDSAbove(): return [-1,0,0,-0.5], a3
    def gTriplePin(): return [1,0,0,0], a3-1
    def gR22(): return [-0.5,0,-1,-1], a3

    def lt0_constraint(cd):
        c,d = cd
        return c, -d-eps

    def feas_DSAbove_infeasible(): return [1,-1,-1,0], 0
    def feas_DSAbove_feasible(): return [-1,1,1,0], -eps
    def feas_R22_p1lt2p3(): return [1,0,-2,0], -eps
    def feas_R22_p2gtp3p4(): return [0,-1,1,1], -eps

    branches = [(XY,R) for XY in ['X','Y'] for R in ['P1','P2','Q']]
    any_feasible = False
    for XY,R in branches:
        A,b = base_constraints()
        c,d = lt0_constraint(g14()); A.append(c); b.append(d)
        c,d = lt0_constraint(g12()); A.append(c); b.append(d)
        if XY=='X':
            c,d = feas_DSAbove_infeasible(); A.append(c); b.append(d)
        else:
            c,d = feas_DSAbove_feasible(); A.append(c); b.append(d)
            c,d = lt0_constraint(gDSAbove()); A.append(c); b.append(d)
            c,d = lt0_constraint(gTriplePin()); A.append(c); b.append(d)
        if R=='P1':
            c,d = feas_R22_p1lt2p3(); A.append(c); b.append(d)
        elif R=='P2':
            c,d = feas_R22_p2gtp3p4(); A.append(c); b.append(d)
        else:
            A.append([-1,0,2,0]); b.append(0)
            A.append([0,1,-1,-1]); b.append(0)
            c,d = lt0_constraint(gR22()); A.append(c); b.append(d)
        A_eq=[[1,1,1,1]]; b_eq=[1]
        res = linprog(c=[0,0,0,0], A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=[(0,1)]*4, method='highs')
        feasible = (res.status==0)
        if feasible:
            any_feasible = True
            print(f"  eps={eps} branch {XY},{R} FEASIBLE at x={res.x}")
    return any_feasible

for eps in [1e-9,1e-7,1e-6,1e-5,3e-5,1e-4,3e-4,1e-3]:
    bad = run(eps)
    print(f"eps={eps}: any bad branch feasible = {bad}")
