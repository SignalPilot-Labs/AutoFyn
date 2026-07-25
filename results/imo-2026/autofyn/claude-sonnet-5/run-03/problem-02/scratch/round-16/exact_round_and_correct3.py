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

DEN = 10**8            # rounding denominator (finer, less noise)
EIGCLIP = 1e-8          # threshold below which eigenvalues are set exactly to 0

def project_psd_clip(Mnum, eigclip=EIGCLIP):
    Mnum = (Mnum + Mnum.T)/2
    w, V = np.linalg.eigh(Mnum)
    w_clipped = np.clip(w, 0, None)
    w_clipped[w_clipped < eigclip] = 0.0
    return (V * w_clipped) @ V.T, w_clipped

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

M1s,w1 = project_psd_clip(M1n); M1r = round_matrix_rational(M1s, DEN)
M2s,w2 = project_psd_clip(M2n); M2r = round_matrix_rational(M2s, DEN)
M3s,w3 = project_psd_clip(M3n); M3r = round_matrix_rational(M3s, DEN)
M0s,w0 = project_psd_clip(M0n)
print("clipped eig counts (zeros): M0",np.sum(w0==0),"M1",np.sum(w1==0),"M2",np.sum(w2==0),"M3",np.sum(w3==0))
print("smallest nonzero eig: M0",np.min(w0[w0>0]),"M1",np.min(w1[w1>0]),"M2",np.min(w2[w2>0]),"M3",np.min(w3[w3>0]))

# t_exact: truncate to 1e-5 precision, safely below t_numeric
t_exact = sp.Rational(int(t_numeric*10**5)-1, 10**5)
print("t_exact =", t_exact, float(t_exact), " margin below numeric:", t_numeric-float(t_exact))

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

# round M0 (no shim), then apply per-entry sparse correction for the (now small) residual
M0r = round_matrix_rational(M0s, DEN)
c0r = gram_to_coeffs_exact(M0r, 17)
residual = [c0_target_exact[k] - c0r[k] for k in range(35)]
print("max |residual| pre final-correction (float):", max(abs(float(r)) for r in residual))
for k in range(35):
    fv=float(residual[k])
    if abs(fv) > 1e-4:
        print("  large residual at k=",k,":",fv)

M0final = M0r.copy()
for k in range(35):
    i = min(k, 17); j = k-i
    r = residual[k]
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
assert all(d==0 for d in diffs), "IDENTITY DOES NOT HOLD EXACTLY"

n0 = 18
Mf = np.array([[float(M0final[i,j]) for j in range(n0)] for i in range(n0)])
eigf = np.linalg.eigvalsh(Mf)
print("M0final float-eval eigs (min few):", np.sort(eigf)[:6])
print("M1r eigs (min few):", np.sort(np.linalg.eigvalsh(np.array([[float(M1r[i,j]) for j in range(13)] for i in range(13)])))[:4])
print("M2r eigs (min few):", np.sort(np.linalg.eigvalsh(np.array([[float(M2r[i,j]) for j in range(15)] for i in range(15)])))[:4])
print("M3r eigs (min few):", np.sort(np.linalg.eigvalsh(np.array([[float(M3r[i,j]) for j in range(15)] for i in range(15)])))[:4])

with open('/tmp/round-16/exact_matrices3.pkl','wb') as fh:
    pickle.dump({'M0final':M0final,'M1r':M1r,'M2r':M2r,'M3r':M3r,'t_exact':t_exact,
                 'vNum':vNum,'vn1':vn1,'vn2':vn2,'vn4':vn4}, fh)
print("saved.")
