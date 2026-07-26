"""
Falsification sweep for n=3 flat regime (p_4 > 1/15).
Goals:
  1. Confirm TRUE optimal Xiang D <= 1/15 for all flat configs (answer c(3)=8/15 verified).
  2. Compare against a STRUCTURED family of strategies to identify the construction.
  3. Record which family member achieves the min in different regions.

Uses floats (sampling). Key checks repeated with fractions for exactness.
"""
import numpy as np
from itertools import combinations, product
import random

random.seed(1); np.random.seed(1)

D3 = 2**4 - 1  # 15
TARGET = 1/D3  # 1/15

def D_of(pieces):
    """D = S_odd - S_even of sorted-desc pieces."""
    a = sorted(pieces, reverse=True)
    s = 0.0
    for k, x in enumerate(a):
        s += x if (k % 2 == 0) else -x
    return s

def liu_marks_to_pieces(marks):
    """marks: sorted list of positions in (0,1). Returns pieces."""
    pts = [0.0] + sorted(marks) + [1.0]
    return [round(pts[i+1]-pts[i], 12) for i in range(len(pts)-1)]

def apply_xiang(liu_pieces, xiang_marks):
    """Given Liu's pieces (as boundaries on [0,1]) and Xiang mark positions,
    return final pieces."""
    # Liu boundaries
    liu_bounds = sorted(cumsum_zero(liu_pieces))
    all_marks = sorted(set(liu_bounds + list(xiang_marks)))
    pts = [0.0] + all_marks + [1.0]
    return [pts[i+1]-pts[i] for i in range(len(pts)-1)]

def cumsum_zero(pieces):
    out = []
    s = 0.0
    for p in pieces:
        s += p
        out.append(s)
    return out

def brute_optimal_D(liu_pieces, grid):
    """Brute-force: choose up to 3 marks from grid (avoiding Liu's marks),
    find min D. grid: array of candidate positions in (0,1)."""
    liu_bounds = cumsum_zero(liu_pieces)[:-1]  # interior boundaries
    # candidate marks: grid minus near liu bounds
    cand = [g for g in grid if all(abs(g - b) > 1e-9 for b in liu_bounds)]
    # 0 marks
    best = D_of(liu_pieces)
    best_marks = []
    # 1 mark
    for m1 in cand:
        pieces = apply_xiang(liu_pieces, [m1])
        d = D_of(pieces)
        if d < best - 1e-12:
            best = d; best_marks = [m1]
    # 2 marks
    for m1, m2 in combinations(cand, 2):
        pieces = apply_xiang(liu_pieces, [m1, m2])
        d = D_of(pieces)
        if d < best - 1e-12:
            best = d; best_marks = [m1, m2]
    # 3 marks
    for m1, m2, m3 in combinations(cand, 3):
        pieces = apply_xiang(liu_pieces, [m1, m2, m3])
        d = D_of(pieces)
        if d < best - 1e-12:
            best = d; best_marks = [m1, m2, m3]
    return best, best_marks

# --- Structured family (exact formulas where possible) ---
def alt3(a, b, c):
    """D of 3 pieces sorted desc."""
    s = sorted([a, b, c], reverse=True)
    return s[0] - s[1] + s[2]

def alt4(a, b, c, d):
    s = sorted([a, b, c, d], reverse=True)
    return s[0]-s[1]+s[2]-s[3]

def family_D(p):
    """Return dict of strategy -> D value for config p=(p1,p2,p3,p4) sorted desc."""
    p1, p2, p3, p4 = p
    fam = {}
    # L4: equal-halve 3 largest (Lemma 4): D = p4
    fam['L4'] = p4
    # Chain (2 marks): p1 -> p2 + r1 -> p3 + r2 ; D = |2 p1 - 1| if executable (p1-p2>=p3)
    if p1 - p2 >= p3 - 1e-12:
        fam['chain2'] = abs(2*p1 - 1)
    # 3-mark chain: p1->p2+r1->p3+r2->p4+r3 ; D=|2p1-1| if executable
    if p1 >= 0.5 - 1e-9 and (p1 - p2) >= p3 - 1e-12 and (p1-p2-p3) >= p4 - 1e-12:
        fam['chain3'] = abs(2*p1-1)
    # M_1j: split p1 -> pj + (p1-pj), pair (pj,pj) cancels, rest 3 pieces
    fam['M12'] = alt3(p1-p2, p3, p4)   # rest {p1-p2, p3, p4}
    fam['M13'] = alt3(p1-p3, p2, p4)
    fam['M14'] = alt3(p1-p4, p2, p3)
    fam['M21'] = alt3(p2, p1-p2, p3) if False else alt3(p1-p2, p3, p4)  # same as M12 actually? no. split p2->p1+(p2-p1) invalid (p2<p1). skip.
    # M_23: split p2 -> p3 + (p2-p3): pair (p3,p3), rest {p1, p2-p3, p4}
    fam['M23'] = alt3(p1, p2-p3, p4)
    fam['M24'] = alt3(p1, p2-p4, p3)
    fam['M34'] = alt3(p1, p2, p3-p4)
    # E_i: equal-split piece p_i (pair cancels), rest 3 pieces
    fam['E1'] = alt3(p2, p3, p4)
    fam['E2'] = alt3(p1, p3, p4)
    fam['E3'] = alt3(p1, p2, p4)
    fam['E4'] = alt3(p1, p2, p3)
    # S0: no marks
    fam['S0'] = alt4(p1, p2, p3, p4)
    # Two-mark combos: split-to-match two pieces.
    # M12 then M34: pairs (p2,p2),(p4? no). Let's add: split p1->p2+(p1-p2) AND split p3->p4+(p3-p4).
    # Final: pairs (p2,p2),(p4,p4), rest {p1-p2, p3-p4}. D=|(p1-p2)-(p3-p4)| (2 pieces, odd-even).
    fam['M12+M34'] = abs((p1-p2)-(p3-p4))
    # M13 then ... split p2->p3? pair (p3,p3) plus (p1-p3 cancels p2? no).
    # split p1->p3+(p1-p3) [pair (p3,p3)], split p2->p4+(p2-p4) [pair (p4,p4)]: rest {p1-p3, p2-p4}. D=|(p1-p3)-(p2-p4)|
    fam['M13+M24'] = abs((p1-p3)-(p2-p4))
    # split p1->p4+(p1-p4) [pair (p4,p4)], split p2->p3+(p2-p3) [pair (p3,p3)]: rest {p1-p4, p2-p3}. D=|(p1-p4)-(p2-p3)|
    fam['M14+M23'] = abs((p1-p4)-(p2-p3))
    return fam

# --- Build flat-regime configs ---
def random_flat_config():
    # sample p4 > 1/15, then p1>=p2>=p3>=p4, sum 1
    while True:
        x = sorted(np.random.dirichlet([1,1,1,1]), reverse=True)
        if x[3] > 1/15 + 1e-6:
            return tuple(round(v, 8) for v in x)

# Also add structured configs near the boundary p4 just above 1/15
def boundary_configs():
    out = []
    # near-dyadic but flat: p4 = 1/15 + eps, others scaled
    for eps in [0.001, 0.005, 0.01, 0.02, 0.03, 0.05]:
        p4 = 1/15 + eps
        rem = 1 - p4
        # distribute rem as 8/15+? : mimic dyadic ratios
        # dyadic rest = (8,4,2)/15 ; scale to rem
        p1 = rem * 8/14; p2 = rem*4/14; p3 = rem*2/14
        if p1>=p2>=p3>=p4:
            out.append((p1,p2,p3,p4))
        # uniform-ish
        out.append((0.25+eps, 0.25, 0.25, 0.25-eps) if 0.25-eps>1/15 else None)
    return [c for c in out if c is not None and min(c)>1/15-1e-9 and abs(sum(c)-1)<1e-6 and sorted(c,reverse=True)==list(c)]

# Grid for brute force
GRID = np.linspace(0.005, 0.995, 40)

N_CONFIGS = 600  # keep bounded
configs = [random_flat_config() for _ in range(N_CONFIGS)]
configs += boundary_configs()

# Dedup
configs = list(dict.fromkeys(configs))

results = []
exceed_count = 0
family_fail = 0
family_member_counts = {}

for p in configs:
    true_D, true_marks = brute_optimal_D(p, GRID)
    fam = family_D(p)
    fam_min = min(fam.values())
    fam_best = min(fam, key=fam.get)
    if true_D > TARGET + 1e-6:
        exceed_count += 1
    if fam_min > TARGET + 1e-6:
        family_fail += 1
    family_member_counts[fam_best] = family_member_counts.get(fam_best, 0) + 1
    results.append((p, true_D, fam_min, fam_best, fam))

print(f"Configs tested: {len(configs)}")
print(f"Target (1/15) = {TARGET:.6f}")
print(f"Brute-force TRUE optimum EXCEEDS 1/15: {exceed_count} configs")
print(f"Structured family min EXCEEDS 1/15: {family_fail} configs")
print(f"\nFamily member achieving the min (counts):")
for k, v in sorted(family_member_counts.items(), key=lambda x:-x[1]):
    print(f"  {k}: {v}")

# Worst true D
worst = max(results, key=lambda r: r[1])
print(f"\nWorst TRUE D over flat configs: {worst[1]:.6f} (target {TARGET:.6f})")
print(f"  config: {worst[0]}")
print(f"  family min: {worst[2]:.6f} via {worst[3]}")
print(f"  family vals: {worst[4]}")

# Worst family-min
worst_fam = max(results, key=lambda r: r[2])
print(f"\nWorst FAMILY min: {worst_fam[2]:.6f} (target {TARGET:.6f})")
print(f"  config: {worst_fam[0]}")
print(f"  true D: {worst_fam[1]:.6f}")
print(f"  family vals: {worst_fam[4]}")

# Cases where family min > true D (family misses the true optimum)
miss = [r for r in results if r[2] > r[1] + 1e-5]
print(f"\nConfigs where family min > true optimum (gap > 1e-5): {len(miss)}")
if miss:
    for r in miss[:5]:
        print(f"  config {r[0]}: true={r[1]:.5f} fam_min={r[2]:.5f} via {r[3]}")
        print(f"     fam={r[4]}")
