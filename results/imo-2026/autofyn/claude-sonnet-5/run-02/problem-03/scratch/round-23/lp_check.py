from scipy.optimize import linprog
from fractions import Fraction as F

# variables order: p1,p2,p3,p4
# T=1 constraint: p1+p2+p3+p4=1

def run_lp(extra_ub=None, extra_eq=None, obj_coef=None, label=""):
    # minimize obj_coef . p  subject to constraints
    A_ub = []
    b_ub = []
    # p1>=p2 -> p2-p1<=0
    A_ub.append([-1,1,0,0]); b_ub.append(0)
    A_ub.append([0,-1,1,0]); b_ub.append(0)
    A_ub.append([0,0,-1,1]); b_ub.append(0)
    # p1 <= 1/2 - eps (use <=0.5 closure, i.e. non-strict at boundary is fine for inf)
    A_ub.append([1,0,0,0]); b_ub.append(0.5)
    # p2 <= 4/15
    A_ub.append([0,1,0,0]); b_ub.append(4/15)
    # p2 >= 1/15 -> -p2 <= -1/15
    A_ub.append([0,-1,0,0]); b_ub.append(-1/15)
    if extra_ub:
        for row,rhs in extra_ub:
            A_ub.append(row); b_ub.append(rhs)
    A_eq = [[1,1,1,1]]
    b_eq = [1]
    if extra_eq:
        for row,rhs in extra_eq:
            A_eq.append(row); b_eq.append(rhs)
    bounds = [(1e-9,None)]*4
    res = linprog(obj_coef, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    print(label, "status:", res.status, "x=", res.x, "obj=", res.fun)
    return res

a3 = 8/15

print("=== Chamber A: (2,0,0,0) tied-to-p4:  Phi = p2+(p1+p4)/2 ===")
# constraints: p1<=2p3+p4 -> p1-2p3-p4<=0 ; p1>=3p4 -> -p1+3p4<=0
extra = [([1,0,-2,-1],0), ([-1,0,0,3],0)]
# g = a3 - p2 - (p1+p4)/2 ; minimize g -> minimize -p2-(p1+p4)/2 shifted; let's directly minimize Phi_min's NEGATIVE... 
# we want min of g = a3*1 - (p2 + (p1+p4)/2). minimize g <=> maximize (p2+(p1+p4)/2)
obj = [-0.5,-1,0,-0.5]  # minimize -(0.5p1+p2+0.5p4) = maximize (0.5p1+p2+0.5p4)
res = run_lp(extra_ub=extra, obj_coef=obj, label="max p2+(p1+p4)/2 over chamberA:")
maxval = -res.fun
print("g_min = a3 - maxval =", a3-maxval)

print()
print("=== Chamber B: (1,0,1,0) cross-tie: Phi = p1+p4 ===")
# constraints: p3<=2p4 -> p3-2p4<=0 ; p1+p4>=p2+p3 -> -p1+p2+p3-p4<=0
extraB = [([0,0,1,-2],0), ([-1,1,1,-1],0)]
objB = [-1,0,0,-1]  # minimize -(p1+p4) = maximize p1+p4
resB = run_lp(extra_ub=extraB, obj_coef=objB, label="max p1+p4 over chamberB:")
maxvalB = -resB.fun
print("g_min = a3 - maxval =", a3-maxvalB)

print()
print("=== Chamber A2: (2,0,0,0) type 2 (p1 -> p2, w, w):  Phi = p4+(p1+p2)/2 ===")
extraA2 = [([1,-2,0,0],0)]  # p1 <= p2+2p4  -> p1-p2-2p4<=0
objA2 = [-0.5,-0.5,0,-1]  # maximize (p1+p2)/2+p4
resA2 = run_lp(extra_ub=extraA2, obj_coef=objA2, label="max phi_A2 over chamberA2:")
maxvalA2 = -resA2.fun
print("g_min = a3 - maxval =", a3-maxvalA2)

print()
print("=== Chamber A restricted to A2-infeasible region (p1 > p2+2p4) ===")
extraA_restr = [([1,0,-2,-1],0), ([-1,0,0,3],0), ([-1,1,0,2],0)]  # p1<=2p3+p4; p1>=3p4; p1>=p2+2p4 (-p1+p2+2p4<=0)
resAr = run_lp(extra_ub=extraA_restr, obj_coef=obj, label="max phi_A over chamberA (A2-infeasible region):")
maxvalAr = -resAr.fun
print("g_min = a3 - maxval =", a3-maxvalAr)

print()
print("=== Chamber A2 CORRECTED formula: Phi = (p1+p2)/2 + p3 ===")
objA2c = [-0.5,-0.5,-1,0]
resA2c = run_lp(extra_ub=extraA2, obj_coef=objA2c, label="max phi_A2_corrected over chamberA2:")
maxvalA2c = -resA2c.fun
print("g_min = a3 - maxval =", a3-maxvalA2c)
