import pickle, numpy as np, sympy as sp, cvxpy as cp

with open('/tmp/round-16/M0_lowrank_exact.pkl','rb') as fh:
    D = pickle.load(fh)
c0, t_exact, vNum, vn1, vn2, vn4 = D['c0'], D['t_exact'], D['vNum'], D['vn1'], D['vn2'], D['vn4']

target_for_123 = [sp.Integer(0)]*35
for k in range(35):
    tk = vNum[k] - c0[k]
    if k == 0: tk -= t_exact
    target_for_123[k] = tk
target_f = np.array([float(x) for x in target_for_123])
print("target_for_123 built (exact). max abs (float):", np.max(np.abs(target_f)))

vn1f = np.array([float(x) for x in vn1])
vn2f = np.array([float(x) for x in vn2])
vn4f = np.array([float(x) for x in vn4])

def gram_coeffs(half_deg, M):
    deg = 2*half_deg
    coeffs = []
    for k in range(deg+1):
        idxs = [(i,k-i) for i in range(max(0,k-half_deg), min(half_deg,k)+1)]
        coeffs.append(cp.sum([M[i,j] for i,j in idxs]))
    return coeffs

def poly_mult(lam_coeffs, gvec):
    dl=len(lam_coeffs)-1; dg=len(gvec)-1
    out=[0]*(dl+dg+1)
    for i,li in enumerate(lam_coeffs):
        for j,gj in enumerate(gvec):
            if gj!=0: out[i+j]=out[i+j]+li*gj
    return out

n1_,n2_,n3_ = 13,15,15
M1 = cp.Variable((n1_,n1_), symmetric=True)
M2 = cp.Variable((n2_,n2_), symmetric=True)
M3 = cp.Variable((n3_,n3_), symmetric=True)
lam = cp.Variable()
cons = [M1 >> lam*np.eye(n1_), M2 >> lam*np.eye(n2_), M3 >> lam*np.eye(n3_)]

c1 = gram_coeffs(12, M1); c2 = gram_coeffs(14, M2); c3 = gram_coeffs(14, M3)
term1 = poly_mult(c1, vn1f); term2 = poly_mult(c2, vn2f); term3 = poly_mult(c3, vn4f)

eqs=[]
for k in range(35):
    rhs = 0
    for term in (term1,term2,term3):
        if k < len(term): rhs = rhs+term[k]
    eqs.append(rhs == target_f[k])
cons += eqs

prob = cp.Problem(cp.Maximize(lam), cons)
val = prob.solve(solver='CLARABEL', verbose=False)
print("status:", prob.status, "max joint margin (M1,M2,M3 only) lam* =", val)

for name,M in [('M1',M1),('M2',M2),('M3',M3)]:
    Mv=(M.value+M.value.T)/2
    eig=np.linalg.eigvalsh(Mv)
    print(name,"min eig",eig.min(),"max eig",eig.max())

with open('/tmp/round-16/M123_resolved.pkl','wb') as fh:
    pickle.dump({'M1':M1.value,'M2':M2.value,'M3':M3.value,'lam':val,'target_for_123':target_for_123}, fh)
