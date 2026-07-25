import pickle
import numpy as np
import sympy as sp
import cvxpy as cp

with open('/tmp/round-16/exact_point_data.pkl','rb') as fh:
    D = pickle.load(fh)
with open('/tmp/round-16/sdp_numeric_result.pkl','rb') as fh:
    R = pickle.load(fh)

cNu, cN1, cN2, cN4 = D['cNu'], D['cN1'], D['cN2'], D['cN4']

def exact_vec(cd, maxdeg):
    v = [sp.Integer(0)]*(maxdeg+1)
    for k,val in cd.items():
        v[k] = sp.nsimplify(val) if not isinstance(val, sp.Basic) else val
    return v

vNum = exact_vec(cNu, 34)
vn1  = exact_vec(cN1, 10)
vn2  = exact_vec(cN2, 6)
vn4  = exact_vec(cN4, 6)

t_numeric = R['t']
# use a conservative t_exact with real slack given back (t* had ~7.8155, plenty of room since
# the *value* of t only needs to stay positive-ish; we deliberately sacrifice some of the
# maximized slack to buy PSD margin in the Gram matrices)
t_exact = sp.Rational(7, 1)   # comfortably below numeric t*=7.8155
print("t_exact =", t_exact, float(t_exact), " sacrificed slack:", t_numeric - float(t_exact))

vNumf = np.array([float(x) for x in vNum])
vn1f = np.array([float(x) for x in vn1])
vn2f = np.array([float(x) for x in vn2])
vn4f = np.array([float(x) for x in vn4])

def gram_coeffs(half_deg, M):
    n = half_deg+1
    deg = 2*half_deg
    coeffs = []
    for k in range(deg+1):
        idxs = [(i,k-i) for i in range(max(0,k-half_deg), min(half_deg,k)+1)]
        coeffs.append(cp.sum([M[i,j] for i,j in idxs]))
    return coeffs

def poly_mult(lam_coeffs, gvec):
    dl = len(lam_coeffs)-1; dg = len(gvec)-1
    out=[0]*(dl+dg+1)
    for i,li in enumerate(lam_coeffs):
        for j,gj in enumerate(gvec):
            if gj!=0: out[i+j]=out[i+j]+li*gj
    return out

n0,n1_,n2_,n3_ = 18,13,15,15
M0 = cp.Variable((n0,n0), symmetric=True)
M1 = cp.Variable((n1_,n1_), symmetric=True)
M2 = cp.Variable((n2_,n2_), symmetric=True)
M3 = cp.Variable((n3_,n3_), symmetric=True)
lam = cp.Variable()

cons = [M0 >> lam*np.eye(n0), M1 >> lam*np.eye(n1_), M2 >> lam*np.eye(n2_), M3 >> lam*np.eye(n3_), lam >= 0]

c0 = gram_coeffs(17, M0)
c1 = gram_coeffs(12, M1)
c2 = gram_coeffs(14, M2)
c3 = gram_coeffs(14, M3)
term1 = poly_mult(c1, vn1f)
term2 = poly_mult(c2, vn2f)
term3 = poly_mult(c3, vn4f)

eqs = []
for k in range(35):
    rhs = c0[k]
    for term in (term1,term2,term3):
        if k < len(term): rhs = rhs + term[k]
    target = vNumf[k] if k < len(vNumf) else 0
    if k == 0: target = target - float(t_exact)
    eqs.append(rhs == target)
cons += eqs

prob = cp.Problem(cp.Maximize(lam), cons)
val = prob.solve(solver='CLARABEL', verbose=False)
print("status:", prob.status, "max joint margin lam* =", val)

for name,M in [('M0',M0),('M1',M1),('M2',M2),('M3',M3)]:
    Mv=(M.value+M.value.T)/2
    eig=np.linalg.eigvalsh(Mv)
    print(name,"min eig",eig.min(),"max eig",eig.max())

with open('/tmp/round-16/joint_resolved.pkl','wb') as fh:
    pickle.dump({'M0':M0.value,'M1':M1.value,'M2':M2.value,'M3':M3.value,'lam':val,
                 't_exact':t_exact,'vNum':vNum,'vn1':vn1,'vn2':vn2,'vn4':vn4}, fh)
