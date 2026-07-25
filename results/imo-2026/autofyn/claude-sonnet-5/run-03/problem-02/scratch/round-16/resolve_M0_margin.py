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

M0n, M1n, M2n, M3n = R['M0'], R['M1'], R['M2'], R['M3']
t_numeric = R['t']

DEN = 10**8
EIGCLIP = 1e-8

def project_psd_clip(Mnum, eigclip=EIGCLIP):
    Mnum = (Mnum + Mnum.T)/2
    w, V = np.linalg.eigh(Mnum)
    w_clipped = np.clip(w, 0, None)
    w_clipped[w_clipped < eigclip] = 0.0
    return (V * w_clipped) @ V.T

def round_matrix_rational(Mnum, den):
    n = Mnum.shape[0]
    Mr = sp.zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            val = Mnum[i,j] if i==j else (Mnum[i,j]+Mnum[j,i])/2
            r = sp.Rational(round(val*den), den)
            Mr[i,j] = r
            Mr[j,i] = r
    return Mr

M1s = project_psd_clip(M1n); M1r = round_matrix_rational(M1s, DEN)
M2s = project_psd_clip(M2n); M2r = round_matrix_rational(M2s, DEN)
M3s = project_psd_clip(M3n); M3r = round_matrix_rational(M3s, DEN)

t_exact = sp.Rational(int(t_numeric*10**5)-1, 10**5)
print("t_exact =", t_exact, float(t_exact))

def gram_to_coeffs_exact(Mr, half_deg):
    deg = 2*half_deg
    c = [sp.Integer(0)]*(deg+1)
    for k in range(deg+1):
        s = sp.Integer(0)
        for i in range(max(0,k-half_deg), min(half_deg,k)+1):
            j = k-i
            s += Mr[i,j]
        c[k] = s
    return c

def poly_mult_exact(coeffs, gvec):
    dl = len(coeffs)-1; dg = len(gvec)-1
    out = [sp.Integer(0)]*(dl+dg+1)
    for i,ci in enumerate(coeffs):
        if ci == 0: continue
        for j,gj in enumerate(gvec):
            if gj != 0:
                out[i+j] += ci*gj
    return out

c1 = gram_to_coeffs_exact(M1r, 12)
c2 = gram_to_coeffs_exact(M2r, 14)
c3 = gram_to_coeffs_exact(M3r, 14)
term1 = poly_mult_exact(c1, vn1)
term2 = poly_mult_exact(c2, vn2)
term3 = poly_mult_exact(c3, vn4)

c0_target_exact = [sp.Integer(0)]*35
for k in range(35):
    tk = vNum[k]
    if k == 0: tk = tk - t_exact
    if k < len(term1): tk -= term1[k]
    if k < len(term2): tk -= term2[k]
    if k < len(term3): tk -= term3[k]
    c0_target_exact[k] = tk
c0_target_f = np.array([float(x) for x in c0_target_exact])

# Solve: find M0 PSD, M0 >> lam*I, maximize lam, s.t. gram_to_coeffs(M0) == c0_target_f exactly
n0 = 18
half0 = 17
M0 = cp.Variable((n0,n0), symmetric=True)
lam = cp.Variable()
cons = [M0 >> lam*np.eye(n0)]
eqs = []
for k in range(35):
    idxs = [(i,k-i) for i in range(max(0,k-half0), min(half0,k)+1)]
    expr = cp.sum([M0[i,j] for i,j in idxs])
    eqs.append(expr == c0_target_f[k])
cons += eqs
prob = cp.Problem(cp.Maximize(lam), cons)
val = prob.solve(solver='CLARABEL', verbose=False)
print("status:", prob.status, "max achievable min-eig lam* =", val)

M0_opt = M0.value
eig = np.linalg.eigvalsh((M0_opt+M0_opt.T)/2)
print("M0_opt actual eigs (min few):", np.sort(eig)[:8])

with open('/tmp/round-16/M0_resolved.pkl','wb') as fh:
    pickle.dump({'M0_opt':M0_opt, 'lam':val, 't_exact':t_exact,
                 'M1r':M1r,'M2r':M2r,'M3r':M3r,'vNum':vNum,'vn1':vn1,'vn2':vn2,'vn4':vn4,
                 'c0_target_exact':c0_target_exact}, fh)
