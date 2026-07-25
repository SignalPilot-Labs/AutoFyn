import pickle, numpy as np, cvxpy as cp

with open('/tmp/round-16/exact_point_data.pkl','rb') as fh:
    D = pickle.load(fh)
cNu, cN1, cN2, cN4 = D['cNu'], D['cN1'], D['cN2'], D['cN4']

def coeff_vec(cd, maxdeg):
    v = np.zeros(maxdeg+1)
    for k,val in cd.items():
        v[k] = float(val)
    return v

vNum = coeff_vec(cNu, 34)
vn1 = coeff_vec(cN1, 10)
vn2 = coeff_vec(cN2, 6)
vn4 = coeff_vec(cN4, 6)

def gram_coeffs(half_deg):
    n = half_deg+1
    M = cp.Variable((n,n), PSD=True)
    deg = 2*half_deg
    coeffs = []
    for k in range(deg+1):
        idxs = [(i,k-i) for i in range(max(0,k-half_deg), min(half_deg,k)+1)]
        expr = cp.sum([M[i,j] for i,j in idxs])
        coeffs.append(expr)
    return M, coeffs

def poly_mult(lam_coeffs, gvec):
    dl = len(lam_coeffs)-1
    dg = len(gvec)-1
    out=[0]*(dl+dg+1)
    for i,li in enumerate(lam_coeffs):
        for j,gj in enumerate(gvec):
            if gj!=0:
                out[i+j]=out[i+j]+li*gj
    return out

M0,c0=gram_coeffs(17)
M1,c1=gram_coeffs(12)
M2,c2=gram_coeffs(14)
M3,c3=gram_coeffs(14)
cons=[M0>>0,M1>>0,M2>>0,M3>>0]
term1=poly_mult(c1,vn1); term2=poly_mult(c2,vn2); term3=poly_mult(c3,vn4)
t=cp.Variable()
eqs=[]
for k in range(35):
    rhs=c0[k]
    for term in (term1,term2,term3):
        if k<len(term): rhs=rhs+term[k]
    target=vNum[k] if k<35 else 0
    if k==0: eqs.append(rhs+t==target)
    else: eqs.append(rhs==target)
cons+=eqs
prob=cp.Problem(cp.Maximize(t), cons)

results = {}
for solver, kw in [('CLARABEL', {}), ('SCS', {'eps':1e-11,'max_iters':300000})]:
    val = prob.solve(solver=solver, verbose=False, **kw)
    print(solver, "status:", prob.status, "t*=", val)
    results[solver] = (prob.status, val, [M0.value.copy(), M1.value.copy(), M2.value.copy(), M3.value.copy()], t.value)

# save CLARABEL's result (usually more accurate) as primary
import numpy.linalg as la
for name,M in [('M0',M0),('M1',M1),('M2',M2),('M3',M3)]:
    Mv = M.value
    eig = la.eigvalsh(Mv)
    print(name, "eigs:", np.round(eig,6))

with open('/tmp/round-16/sdp_numeric_result.pkl','wb') as fh:
    pickle.dump({'M0':M0.value,'M1':M1.value,'M2':M2.value,'M3':M3.value,'t':t.value,
                 'vNum':vNum,'vn1':vn1,'vn2':vn2,'vn4':vn4}, fh)
