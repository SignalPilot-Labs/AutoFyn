from scipy.optimize import linprog
import numpy as np

# variables p1,p2,p3,p4
a3 = 8/15

# Box constraints (as <= 0 form), plus simplex order p1>=p2>=p3>=p4>0, sum=1
# We'll use equality p1+p2+p3+p4=1
# inequalities (all as A_ub x <= b_ub form), x=[p1,p2,p3,p4]

def base_constraints():
    A=[]; b=[]
    # order: p2<=p1 -> p2-p1<=0
    A.append([-1,1,0,0]); b.append(0)
    # p3<=p2
    A.append([0,-1,1,0]); b.append(0)
    # p4<=p3
    A.append([0,0,-1,1]); b.append(0)
    # p4>0 -> -p4 <= -eps ; use strict via eps small, but for feasibility test use <=-tiny to approximate open
    eps=1e-4
    A.append([0,0,0,-1]); b.append(-eps)
    # box: p1<1/2 -> p1<=1/2-eps
    A.append([1,0,0,0]); b.append(0.5-eps)
    # p2>1/15 -> -p2 <= -1/15-eps
    A.append([0,-1,0,0]); b.append(-1/15-eps)
    # p2<4/15
    A.append([0,1,0,0]); b.append(4/15-eps)
    return A,b

def g14(): # bisect{1,4}: S={0,3} (0-indexed p1,p4), R=[p2,p3]
    # phi = (1+p2-p3)/2 ; g=a3-phi
    # g = a3 - 0.5 - 0.5p2+0.5p3 = (a3-0.5) -0.5p2+0.5p3
    return [0, -0.5, 0.5, 0], (a3-0.5)

def g12(): # bisect{1,2}: S={0,1}, R=[p3,p4]
    # phi=(1+p3-p4)/2; g=a3-phi = (a3-0.5)-0.5p3+0.5p4
    return [0,0,-0.5,0.5], (a3-0.5)

def gDSAbove(): # phi=p1+p4/2 ; g=a3-p1-0.5p4
    return [-1,0,0,-0.5], a3

def gTriplePin(): # phi=1-p1; g=a3-1+p1
    return [1,0,0,0], a3-1

def gR22(): # phi=p1/2+p3+p4; g=a3-p1/2-p3-p4
    return [-0.5,0,-1,-1], a3

# linear forms: g(x) = c.x + d  (we want g<0 i.e. c.x+d<0 i.e. c.x <= -d-eps)
def lt0_constraint(cd, eps=1e-4):
    c,d = cd
    return c, -d-eps

def feas_DSAbove_infeasible():
    # p1<=p2+p3  i.e. p1-p2-p3<=0
    return [1,-1,-1,0], 0
def feas_DSAbove_feasible():
    # p1>p2+p3 i.e. -p1+p2+p3 <= -eps
    return [-1,1,1,0], -1e-9

def feas_R22_p1lt2p3():
    # p1<2p3 -> p1-2p3<=-eps
    return [1,0,-2,0], -1e-9
def feas_R22_p2gtp3p4():
    # p2>p3+p4 -> -p2+p3+p4<=-eps
    return [0,-1,1,1], -1e-9
def feas_R22_feasible():
    # p1>=2p3 AND p2<=p3+p4
    return None # handled as two constraints combined

results=[]
branches = []
# X: p1<=p2+p3 (DS-Above & TriplePin both infeasible)
# Y: p1>p2+p3 and g_DSAbove<0 and g_TriplePin<0
for XY in ['X','Y']:
    for R in ['P1','P2','Q']:
        branches.append((XY,R))

for XY,R in branches:
    A,b = base_constraints()
    c,d = g14(); cc,dd = lt0_constraint((c,d)); A.append(cc); b.append(dd)
    c,d = g12(); cc,dd = lt0_constraint((c,d)); A.append(cc); b.append(dd)
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
        # feasible R22: p1>=2p3 -> -p1+2p3<=0 ; p2<=p3+p4 -> p2-p3-p4<=0
        A.append([-1,0,2,0]); b.append(0)
        A.append([0,1,-1,-1]); b.append(0)
        c,d = lt0_constraint(gR22()); A.append(c); b.append(d)
    A_eq=[[1,1,1,1]]; b_eq=[1]
    res = linprog(c=[0,0,0,0], A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=[(0,1)]*4, method='highs')
    print(XY,R, "feasible:" , res.status==0, "x=" , res.x if res.status==0 else None)

print()
print("=== check example X-P1 point against full 20-chamber family ===")
from fractions import Fraction as F
p = (F(2,5), F(4,15), F(1,5), F(2,15))
print("sum", sum(p), "sorted?", p[0]>=p[1]>=p[2]>=p[3]>0)
print("box: p1<1/2?", p[0]<F(1,2), "p2 in (1/15,4/15)?", F(1,15)<p[1]<F(4,15))
