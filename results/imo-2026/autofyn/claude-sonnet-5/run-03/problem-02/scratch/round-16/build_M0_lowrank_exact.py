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

vNum = exact_vec(cNu, 34); vn1 = exact_vec(cN1, 10); vn2 = exact_vec(cN2, 6); vn4 = exact_vec(cN4, 6)
M0n = R['M0']
t_numeric = R['t']
t_exact = sp.Rational(int(t_numeric*10**5)-1, 10**5)
print("t_exact:", t_exact, float(t_exact))

# --- build exact rational rank-reduced M0 = Q^T Q ---
M0n = (M0n+M0n.T)/2
w, V = np.linalg.eigh(M0n)
order = np.argsort(w)[::-1]  # descending
w = w[order]; V = V[:,order]
print("eigs desc:", w)
RANK = int(np.sum(w > 1e-6))
print("chosen rank:", RANK)
Qnum = (np.sqrt(w[:RANK])[:,None]) * V[:,:RANK].T   # RANK x 18

DEN_Q = 10**7
Qr = sp.zeros(RANK, 18)
for a in range(RANK):
    for b in range(18):
        Qr[a,b] = sp.Rational(round(Qnum[a,b]*DEN_Q), DEN_Q)

M0final = (Qr.T * Qr)   # exact rational, automatically PSD (Gram matrix of real rational vectors)
M0final = sp.Matrix(M0final)
print("built M0final as Q^T Q, exactly PSD by construction. shape:", M0final.shape)

# sanity: is it really PSD? (should be trivially true; verify numerically as a smoke test only)
M0f = np.array(M0final.evalf(), dtype=float)
eig0 = np.linalg.eigvalsh(M0f)
print("float check of Q^T Q eigs (smoke test only):", np.sort(eig0)[:6], np.sort(eig0)[-3:])

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

c0 = gram_to_coeffs_exact(M0final, 17)
print("c0 computed exactly (degree 0..34).")

with open('/tmp/round-16/M0_lowrank_exact.pkl','wb') as fh:
    pickle.dump({'M0final':M0final, 'c0':c0, 't_exact':t_exact, 'vNum':vNum,'vn1':vn1,'vn2':vn2,'vn4':vn4,
                 'Qr':Qr, 'RANK':RANK}, fh)
print("saved.")
