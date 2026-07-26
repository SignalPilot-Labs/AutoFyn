import numpy as np
from fractions import Fraction as F
import itertools, random

random.seed(1)
np.random.seed(1)

def D(n): return 2**(n+1) - 1
def alpha(n): return F(1, D(n))
def f(n): return F(2**n, D(n))

# ---- A from sorted pieces (descending) ----
def A_from_pieces(pieces):
    # pieces: list of numbers
    s = sorted(pieces, reverse=True)
    a = 0
    for i,v in enumerate(s):
        a += ((-1)**i) * v   # (-1)^{i+1} p_i with i 0-based => (-1)^i * p (rank i+1)
    return a

def A_from_floats(pieces):
    s = np.sort(pieces)[::-1]
    return float(np.sum(np.where(np.arange(len(s))%2==0, 1, -1) * s))

# ---- Liu config -> sorted pieces (lengths) from cumulative marks ----
def liu_pieces_from_marks(marks):
    # marks: sorted list of positions in (0,1)
    bdy = [0.0] + sorted(marks) + [1.0]
    return [bdy[i+1]-bdy[i] for i in range(len(bdy)-1)]

def liu_pieces_from_marks_frac(marks):
    bdy = [F(0)] + sorted(marks) + [F(1)]
    return [bdy[i+1]-bdy[i] for i in range(len(bdy)-1)]

# ---- Phi(Liu) = min over Xiang marks of A ----
# For n marks: Xiang picks n distinct grid points (or reals) not at Liu marks.
# We do grid search for Xiang (denom N) and also continuous local opt via scipy.

def xiang_grid_marks_for_liu(liu_marks, N):
    # grid points k/N for k=1..N-1, excluding Liu marks (assume Liu marks on grid or off)
    pts = []
    for k in range(1, N):
        x = F(k, N)
        if x in set(liu_marks): continue
        pts.append(x)
    return pts

def phi_liu_grid_frac(liu_marks, N, n_xiang):
    """min over Xiang placements (exact Fraction) of A. Returns (min_A, argmin_marks)."""
    pts = xiang_grid_marks_for_liu(liu_marks, N)
    liu_pieces = liu_pieces_from_marks_frac(liu_marks)
    best = None; best_marks=None
    for combo in itertools.combinations(pts, n_xiang):
        # all marks
        all_marks = sorted(list(liu_marks) + list(combo))
        bdy = [F(0)] + all_marks + [F(1)]
        pieces = [bdy[i+1]-bdy[i] for i in range(len(bdy)-1)]
        a = A_from_pieces(pieces)
        if best is None or a < best:
            best = a; best_marks = combo
    return best, best_marks

def phi_liu_grid_float(liu_pieces, N, n_xiang):
    """min over Xiang placements (float) of A. liu_pieces given as lengths."""
    # rebuild boundary
    # we need positions; reconstruct cumsum
    cum = [0.0]
    for p in liu_pieces: cum.append(cum[-1]+p)
    liu_marks = cum[1:-1]
    # grid pts
    pts = [k/N for k in range(1,N) if abs((k/N) - round((k/N)/1)*1) < 1e-15]  # all grid
    # exclude points equal to a liu mark
    liu_set = set(round(m,12) for m in liu_marks)
    pts = [p for p in pts if round(p,12) not in liu_set]
    best = None
    for combo in itertools.combinations(pts, n_xiang):
        all_marks = sorted(list(liu_marks) + list(combo))
        bdy = [0.0] + all_marks + [1.0]
        pieces = [bdy[i+1]-bdy[i] for i in range(len(bdy)-1)]
        a = A_from_floats(pieces)
        if best is None or a < best:
            best = a
    return best

# ===================== n=2 verification (Fraction, grid) =====================
print("="*60)
print("n=2: verify (U-E): max_Liu Phi = alpha(2)=1/7, unique at dyadic")
n=2; N=84  # denom 84 (multiple of D=7)
dyadic_marks = [F(1,7), F(3,7)]  # pieces (1,2,4)/7
# Verify Phi(dyadic) = 1/7
phi_dy, argm = phi_liu_grid_frac(dyadic_marks, N, 2)
print(f"  Phi(dyadic_2) on grid N={N}: {phi_dy} = {float(phi_dy):.6f}  (alpha=1/7={float(F(1,7)):.6f})")
print(f"  argmin Xiang marks: {argm}")

# Now enumerate Liu configs on grid, find max of Phi
liu_pts_pool = [F(k,N) for k in range(1,N)]
max_phi = None; max_liu=None; count_at_max=0
all_phis = []
for combo in itertools.combinations(liu_pts_pool, 2):
    liu = sorted(combo)
    # skip if duplicate (distinct marks)
    phi, _ = phi_liu_grid_frac(liu, N, 2)
    all_phis.append((float(phi), [float(m) for m in liu]))
    if max_phi is None or phi > max_phi:
        max_phi = phi; max_liu = liu; count_at_max=1
    elif phi == max_phi:
        count_at_max += 1
print(f"  max_Liu Phi = {max_phi} = {float(max_phi):.6f}  (alpha(2)=1/7={float(F(1,7)):.6f})")
print(f"  argmax Liu marks: {max_liu}  (dyadic={(1/7,3/7)})")
print(f"  count Liu configs attaining max: {count_at_max}")
# distribution near max
near = [(p,m) for (p,m) in all_phis if p >= float(F(1,7)) - 1e-9]
print(f"  configs with Phi >= 1/7: {len(near)}")
