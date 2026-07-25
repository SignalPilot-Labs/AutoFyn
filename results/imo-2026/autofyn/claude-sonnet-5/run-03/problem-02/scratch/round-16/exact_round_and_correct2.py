import pickle
import numpy as np
import sympy as sp

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

DEN = 10**7
SHIM_LAM = 1e-5
SHIM_SIG = 3e-3
EIGCLIP = 1e-9

def project_psd_and_shim(Mnum, shim, eigclip=EIGCLIP):
    Mnum = (Mnum + Mnum.T)/2
    w, V = np.linalg.eigh(Mnum)
    w_clipped = np.clip(w, 0, None)
    w_clipped[w_clipped < eigclip] = 0.0
    w_shim = w_clipped + shim
    return (V * w_shim) @ V.T

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

M1s = project_psd_and_shim(M1n, SHIM_LAM); M1r = round_matrix_rational(M1s, DEN)
M2s = project_psd_and_shim(M2n, SHIM_LAM); M2r = round_matrix_rational(M2s, DEN)
M3s = project_psd_and_shim(M3n, SHIM_LAM); M3r = round_matrix_rational(M3s, DEN)
M0s = project_psd_and_shim(M0n, SHIM_SIG)

t_exact = sp.Rational(int(t_numeric*10**5)-5, 10**5)
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

# current (shimmed, pre-round) c0 from M0s
half0 = 17
n0 = half0+1
def gram_to_coeffs_np(M, half_deg):
    deg = 2*half_deg
    c = np.zeros(deg+1)
    for k in range(deg+1):
        for i in range(max(0,k-half_deg), min(half_deg,k)+1):
            j = k-i
            c[k] += M[i,j]
    return c
c0_current = gram_to_coeffs_np(M0s, half0)
resid_target = c0_target_f - c0_current
print("max |resid_target| before correction:", np.max(np.abs(resid_target)))
for k in range(35):
    print("  resid_target[",k,"]=",resid_target[k])

# build linear map A: (35 x n0*(n0+1)/2) from upper-tri free params (i<=j) to degree-k antidiagonal sums
idx_pairs = [(i,j) for i in range(n0) for j in range(i, n0)]
nparam = len(idx_pairs)
A = np.zeros((35, nparam))
for p,(i,j) in enumerate(idx_pairs):
    k = i+j
    if k <= 34:
        A[k, p] += (1.0 if i==j else 2.0)

# minimum Frobenius-norm ΔM0 (upper-tri params) solving A x = resid_target
x, *_ = np.linalg.lstsq(A, resid_target, rcond=None)
print("max |x| correction entries:", np.max(np.abs(x)))

DeltaM0 = np.zeros((n0,n0))
for p,(i,j) in enumerate(idx_pairs):
    DeltaM0[i,j] += x[p]
    if i != j:
        DeltaM0[j,i] += x[p]

M0_corrected_float = M0s + DeltaM0
eig = np.linalg.eigvalsh(M0_corrected_float)
print("M0_corrected_float min/max eig:", eig.min(), eig.max())

# now round M0_corrected_float to rational, then do exact fine sparse correction for residual leftover from rounding only
M0r = round_matrix_rational(M0_corrected_float, DEN)
c0r = gram_to_coeffs_exact(M0r, 17)
residual2 = [c0_target_exact[k] - c0r[k] for k in range(35)]
print("max |residual2| (post-round, float):", max(abs(float(r)) for r in residual2))

# apply the sparse single-entry fix for this much smaller residual (rounding-only, should be tiny ~1e-7 scale)
M0final = M0r.copy()
for k in range(35):
    i = min(k, 17); j = k-i
    r = residual2[k]
    if i == j:
        M0final[i,j] += r
    else:
        M0final[i,j] += r/2
        M0final[j,i] += r/2

c0f = gram_to_coeffs_exact(M0final, 17)
full_lhs = [c0f[k] + (term1[k] if k<len(term1) else 0) + (term2[k] if k<len(term2) else 0) + (term3[k] if k<len(term3) else 0) for k in range(35)]
full_rhs = [vNum[k] - (t_exact if k==0 else 0) for k in range(35)]
diffs = [sp.nsimplify(full_lhs[k]-full_rhs[k]) for k in range(35)]
print("exact identity residual (should be all 0):", diffs)

Mf = np.array([[float(M0final[i,j]) for j in range(n0)] for i in range(n0)])
eigf = np.linalg.eigvalsh(Mf)
print("M0final (exact matrix, float-eval) min/max eig:", eigf.min(), eigf.max())

with open('/tmp/round-16/exact_matrices2.pkl','wb') as fh:
    pickle.dump({'M0final':M0final,'M1r':M1r,'M2r':M2r,'M3r':M3r,'t_exact':t_exact,
                 'vNum':vNum,'vn1':vn1,'vn2':vn2,'vn4':vn4}, fh)
print("saved.")
