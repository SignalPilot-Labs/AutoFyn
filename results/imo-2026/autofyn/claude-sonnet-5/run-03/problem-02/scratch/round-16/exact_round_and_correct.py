import pickle
import numpy as np
import sympy as sp
from fractions import Fraction

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
print("numeric t* =", t_numeric)

DEN = 10**7          # rounding denominator
SHIM_LAM = 1e-5      # shim for lambda Gram matrices (M1,M2,M3)
SHIM_SIG = 1.5e-2       # shim for sigma0 Gram matrix (M0) -- bigger since it absorbs the correction
EIGCLIP = 1e-9

def project_psd_and_shim(Mnum, shim, eigclip=EIGCLIP):
    Mnum = (Mnum + Mnum.T)/2
    w, V = np.linalg.eigh(Mnum)
    w_clipped = np.clip(w, 0, None)
    w_clipped[w_clipped < eigclip] = 0.0
    w_shim = w_clipped + shim
    M_shimmed = (V * w_shim) @ V.T
    return M_shimmed

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

M1s = project_psd_and_shim(M1n, SHIM_LAM)
M2s = project_psd_and_shim(M2n, SHIM_LAM)
M3s = project_psd_and_shim(M3n, SHIM_LAM)
M0s = project_psd_and_shim(M0n, SHIM_SIG)

M1r = round_matrix_rational(M1s, DEN)
M2r = round_matrix_rational(M2s, DEN)
M3r = round_matrix_rational(M3s, DEN)
M0r = round_matrix_rational(M0s, DEN)

print("rounded matrices built.")

# choose t_exact: rational, safely below numeric t*, with small denominator
t_exact = sp.Rational(int(t_numeric*100)-5, 100)   # e.g. floor to 2 decimals minus a small safety margin
print("t_exact =", t_exact, float(t_exact))

def gram_to_coeffs_exact(Mr, half_deg):
    deg = 2*half_deg
    c = [sp.Integer(0)]*(deg+1)
    n = half_deg+1
    for k in range(deg+1):
        s = sp.Integer(0)
        for i in range(max(0,k-half_deg), min(half_deg,k)+1):
            j = k-i
            s += Mr[i,j]
        c[k] = s
    return c

def poly_mult_exact(coeffs, gvec):
    dl = len(coeffs)-1
    dg = len(gvec)-1
    out = [sp.Integer(0)]*(dl+dg+1)
    for i,ci in enumerate(coeffs):
        if ci == 0: continue
        for j,gj in enumerate(gvec):
            if gj != 0:
                out[i+j] += ci*gj
    return out

c0 = gram_to_coeffs_exact(M0r, 17)   # deg 0..34
c1 = gram_to_coeffs_exact(M1r, 12)   # deg 0..24
c2 = gram_to_coeffs_exact(M2r, 14)   # deg 0..28
c3 = gram_to_coeffs_exact(M3r, 14)   # deg 0..28

term1 = poly_mult_exact(c1, vn1)  # deg up to 34
term2 = poly_mult_exact(c2, vn2)
term3 = poly_mult_exact(c3, vn4)

# target that M0 alone must supply at each degree k
c0_target = [sp.Integer(0)]*35
for k in range(35):
    tk = vNum[k]
    if k == 0:
        tk = tk - t_exact
    if k < len(term1): tk -= term1[k]
    if k < len(term2): tk -= term2[k]
    if k < len(term3): tk -= term3[k]
    c0_target[k] = tk

# residual that must be added to M0's anti-diagonal sums
residual = [c0_target[k] - c0[k] for k in range(35)]
print("max |residual| (float):", max(abs(float(r)) for r in residual))

# apply sparse correction: for each k, pick representative (i,j) with i=min(k,17), j=k-i
M0final = M0r.copy()
for k in range(35):
    i = min(k, 17)
    j = k - i
    if not (0 <= j <= 17):
        raise ValueError(f"bad index at k={k}: i={i} j={j}")
    r = residual[k]
    if i == j:
        M0final[i,j] += r
    else:
        M0final[i,j] += r/2
        M0final[j,i] += r/2

# sanity check: recompute exact coefficients and compare to full target
c0f = gram_to_coeffs_exact(M0final, 17)
full_lhs = [c0f[k] + (term1[k] if k<len(term1) else 0) + (term2[k] if k<len(term2) else 0) + (term3[k] if k<len(term3) else 0) for k in range(35)]
full_rhs = [vNum[k] - (t_exact if k==0 else 0) for k in range(35)]
diffs = [sp.simplify(full_lhs[k]-full_rhs[k]) for k in range(35)]
print("exact identity residual (should be all 0):", diffs)

with open('/tmp/round-16/exact_matrices.pkl','wb') as fh:
    pickle.dump({'M0final':M0final,'M1r':M1r,'M2r':M2r,'M3r':M3r,'t_exact':t_exact,
                 'vNum':vNum,'vn1':vn1,'vn2':vn2,'vn4':vn4}, fh)
print("saved exact_matrices.pkl")
