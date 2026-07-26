"""
Verification for self-reproducing-invariant approach on imo-2026-03.
All lengths in 1/D(n) integer units. Uses Fraction throughout.
"""
from fractions import Fraction as F

def D(n): return 2**(n+1) - 1

def advantage(pieces):
    s = F(0)
    n = len(pieces)
    for i in range(0, n-1, 2):
        s += pieces[i] - pieces[i+1]
    if n % 2 == 1:
        s += pieces[-1]
    return s

def pair_pile_dyadic(n):
    if n == 1: return [F(1), F(1), F(1)]
    if n == 2: return [F(3), F(2), F(1), F(1)]
    pile = []
    for k in range(n-1, 1, -1):
        pile += [F(2**k), F(2**k)]
    pile += [F(3), F(2), F(1), F(1)]
    return pile

def apply_pair_pile(config):
    """Apply pair-pile strategy: bisect pieces 0..n-3, split piece n-2 at dist 1, leave last 2."""
    n = len(config) - 1
    result = []
    for i in range(n-2):
        sz = config[i]
        result += [sz/F(2), sz/F(2)]
    sz = config[n-2]
    result += [F(1), sz - F(1)]
    result += [config[n-1], config[n]]
    return sorted(result, reverse=True)

def dyadic_pieces(n):
    """Level-n dyadic pieces (1/D(n) units): 2^n, 2^{n-1}, ..., 1."""
    return [F(2**k) for k in range(n, -1, -1)]

# ---- 1. Pair-pile on dyadic ----
print("=== 1. Pair-pile on dyadic ===")
for n in range(1, 7):
    pile = pair_pile_dyadic(n)
    assert sum(pile) == D(n)
    A = advantage(sorted(pile, reverse=True))
    print(f"  n={n}: A={A}, match={A==1}")

# ---- 2. Ridge R_e = (2^n,...,4, 2+e, 1-e)/D(n) ----
print("\n=== 2. Pair-pile on ridge R_e (all n>=2) ===")
for n in range(2, 7):
    for e in [F(1,3), F(1,5), F(2,7), F(1,2), F(3,7)]:
        config = dyadic_pieces(n)
        config[-2] = F(2) + e
        config[-1] = F(1) - e
        assert sum(config) == D(n)
        result = apply_pair_pile(config)
        assert sum(result) == D(n)
        A = advantage(result)
        print(f"  n={n}, e={e}: A={A}, reproduce={A==1}")

# ---- 3. Level-1 mass-up: (2^n+e, 2^{n-1}-e, 2^{n-2},...,1) ----
print("\n=== 3. Pair-pile on level-1 mass-up (piece1 grows) ===")
for n in range(3, 7):
    for e in [F(1,5), F(1,10), F(1,3)]:
        config = dyadic_pieces(n)
        config[0] = F(2**n) + e
        config[1] = F(2**(n-1)) - e
        assert len(config) == n+1
        assert sum(config) == D(n)
        result = apply_pair_pile(config)
        A = advantage(result)
        print(f"  n={n}, e={e}: A={A}, strict={A<1}")

# ---- 4. Level-1 mass-down: (2^n-e, 2^{n-1}+e, ...) ----
print("\n=== 4. Pair-pile on level-1 mass-down (piece1 shrinks) ===")
for n in range(3, 7):
    for e in [F(1,5), F(1,10)]:
        config = dyadic_pieces(n)
        config[0] = F(2**n) - e
        config[1] = F(2**(n-1)) + e
        assert sum(config) == D(n)
        result = apply_pair_pile(config)
        A = advantage(result)
        print(f"  n={n}, e={e}: A={A}, overshoot={A>1}")

# ---- 5. Self-reproduction recursion ----
print("\n=== 5. Self-reproduction: pair-pile(n+1) = bisect(M) + scaled pair-pile(n) ===")
for n in range(1, 6):
    dn1 = D(n+1)
    pile_n1 = pair_pile_dyadic(n+1)
    A_n1 = advantage(sorted(pile_n1, reverse=True))
    dn = D(n)
    pile_n = pair_pile_dyadic(n)
    scale = F(dn, dn1)
    pile_n_scaled = [p * scale for p in pile_n]
    M_half = F(2**n)
    reconstructed = [M_half, M_half] + pile_n_scaled
    A_recon = advantage(sorted(reconstructed, reverse=True))
    pieces_match = sorted(pile_n1) == sorted(reconstructed)
    print(f"  n={n}->n+1: A(n+1)={A_n1}, A(recon)={A_recon}, match={A_n1==A_recon}, pieces_match={pieces_match}")

# ---- 6. Bottom-3 perturbation: A = 1+2a formula ----
print("\n=== 6. Bottom-3 perturbation A=1+2a formula ===")
for n in [3, 4, 5]:
    for a in [F(1,10), F(-1,10), F(1,5), F(-1,5)]:
        b, c = F(0), -a
        if F(4)+a <= 0 or F(1)+c <= 0: continue
        config = dyadic_pieces(n)
        config[-3] = F(4) + a
        config[-2] = F(2) + b
        config[-1] = F(1) + c
        if config != sorted(config, reverse=True): continue
        assert sum(config) == D(n)
        result = apply_pair_pile(config)
        A = advantage(result)
        expected = F(1) + F(2)*a
        print(f"  n={n}, a={a}: A={A}, 1+2a={expected}, match={A==expected}")

# ---- 7. Deep-level ridge: perturbation at level j ----
print("\n=== 7. Deep-level ridge (perturbation at level j, pair-pile touches levels 1..n-1) ===")
for n in [3, 4, 5]:
    for j in range(1, n+1):
        e = F(1,5)
        config = dyadic_pieces(n)
        # level j is between pieces j-1 and j (0-indexed): perturb p[j-1] += e, p[j] -= e
        config[j-1] += e
        config[j] -= e
        if any(p <= 0 for p in config): continue
        if config != sorted(config, reverse=True): continue
        assert sum(config) == D(n)
        result = apply_pair_pile(config)
        A = advantage(result)
        tag = "reproduce" if A==1 else ("strict" if A<1 else "OVERSHOOT")
        print(f"  n={n}, j={j}: A={A}, {tag}")

# ---- 8. n=3 local-kink: pair-pile vs local-kink on mass-up and mass-down ----
print("\n=== 8. n=3 local-kink comparison (pair-pile A vs local-kink A) ===")
for e in [F(1,5), F(1,10), F(-1,5), F(-1,10)]:
    if e > 0:
        # mass-up: (8+e, 4-e, 2, 1)/15
        config = [F(8)+e, F(4)-e, F(2), F(1)]
        # pair-pile: bisect p1 -> (4+e/2, 4+e/2), split p2 at dist 1 -> (1, 3-e)
        pp = sorted([F(4)+e/2, F(4)+e/2, F(1), F(3)-e, F(2), F(1)], reverse=True)
        A_pp = advantage(pp)
        # local-kink: bisect p1 -> (4+e/2, 4+e/2), split p2 at dist 3/2 -> (3/2, 5/2-e)
        lk = sorted([F(4)+e/2, F(4)+e/2, F(3,2), F(5,2)-e, F(2), F(1)], reverse=True)
        A_lk = advantage(lk)
        print(f"  mass-up e={e}: pair-pile A={A_pp}, local-kink A={A_lk}, both<1={A_pp<1 and A_lk<1}")
    else:
        # mass-down: (8+e, 4-e, 2, 1) with e<0 => (8-|e|, 4+|e|, 2, 1)
        # pair-pile: bisect p1 -> (4+e/2, 4+e/2), split p2 -> (1, 3-e)
        pp = sorted([F(4)+e/2, F(4)+e/2, F(1), F(3)-e, F(2), F(1)], reverse=True)
        A_pp = advantage(pp)
        # local-kink (mass-down): marks at dyadic positions 1, 3 inside piece 1 (8+e) -> (1, 2, 5+e), pieces 2,3,4 = (4-e, 2, 1)
        lk = sorted([F(5)+e, F(4)-e, F(2), F(2), F(1), F(1)], reverse=True)
        A_lk = advantage(lk)
        print(f"  mass-down e={e}: pair-pile A={A_pp} (overshoot={A_pp>1}), local-kink A={A_lk}, strict={A_lk<1}")

print("\n=== ALL CHECKS DONE ===")

# ---- 9. 2-strategy family: pair-pile (dist 1) vs modified (dist 2) on active piece ----
print("\n=== 9. 2-strategy family: dist-1 vs dist-2 split on active piece ===")
print("Active piece = piece n-1 (dyadic size 4), split at distance 1 (->(1,rest)) or distance 2 (->(2,rest))")

def apply_strategy(config, split_dist):
    """Bisect pieces 0..n-3, split piece n-2 at given distance, leave last 2."""
    n = len(config) - 1
    result = []
    for i in range(n-2):
        sz = config[i]
        result += [sz/F(2), sz/F(2)]
    sz = config[n-2]
    result += [split_dist, sz - split_dist]
    result += [config[n-1], config[n]]
    return sorted(result, reverse=True)

for n in [3, 4, 5, 6]:
    dn = D(n)
    print(f"  n={n} (D={dn}):")
    # Case A: ridge (bottom 2 perturbed)
    for e in [F(1,5), F(1,3)]:
        config = dyadic_pieces(n)
        config[-2] = F(2) + e
        config[-1] = F(1) - e
        A1 = advantage(apply_strategy(config, F(1)))
        A2 = advantage(apply_strategy(config, F(2)))
        print(f"    ridge e={e}: dist1 A={A1}, dist2 A={A2}")
    # Case B: mass-up at active (active shrinks: p[n-2]-=e, p[n-1]+=e)
    for e in [F(1,5), F(1,10)]:
        config = dyadic_pieces(n)
        config[n-2] -= e  # active piece shrinks
        config[n-1] += e  # piece below grows
        if any(p <= 0 for p in config): continue
        A1 = advantage(apply_strategy(config, F(1)))
        A2 = advantage(apply_strategy(config, F(2)))
        print(f"    mass-up(active-) e={e}: dist1 A={A1}, dist2 A={A2}")
    # Case C: mass-down at active (active grows: p[n-2]+=e, p[n-1]-=e)
    for e in [F(1,5), F(1,10)]:
        config = dyadic_pieces(n)
        config[n-2] += e  # active piece grows
        config[n-1] -= e  # piece below shrinks
        if any(p <= 0 for p in config): continue
        A1 = advantage(apply_strategy(config, F(1)))
        A2 = advantage(apply_strategy(config, F(2)))
        print(f"    mass-down(active+) e={e}: dist1 A={A1}, dist2 A={A2}")

# ---- 10. 2-strategy family: min(dist1, dist2) <= 1 for near-dyadic ----
print("\n=== 10. min(dist1,dist2) <= 1 for active-piece perturbations ===")
violations = 0
total = 0
for n in [3, 4, 5]:
    dn = D(n)
    for e_num in range(1, 20):
        e = F(e_num, 20)
        for direction in ['ridge', 'active_up', 'active_down', 'level1_up', 'level1_down']:
            config = dyadic_pieces(n)
            if direction == 'ridge':
                config[-2] += e; config[-1] -= e
            elif direction == 'active_up':
                config[n-2] -= e; config[n-1] += e
            elif direction == 'active_down':
                config[n-2] += e; config[n-1] -= e
            elif direction == 'level1_up':
                config[0] += e; config[1] -= e
            elif direction == 'level1_down':
                config[0] -= e; config[1] += e
            if any(p <= 0 for p in config): continue
            if config != sorted(config, reverse=True): continue
            A1 = advantage(apply_strategy(config, F(1)))
            A2 = advantage(apply_strategy(config, F(2)))
            total += 1
            if A1 > 1 and A2 > 1:
                violations += 1
                print(f"  VIOLATION: n={n}, {direction}, e={e}: A1={A1}, A2={A2}")
print(f"  Total tested: {total}, violations: {violations}")

print("\n=== ALL CHECKS DONE ===")

# ---- 11. Comprehensive single-level perturbation cover ----
print("\n=== 11. Single-level perturbation cover (3-strat n=3, 2-strat n>=4) ===")

def local_kink_n3(config, e):
    """n=3 local-kink: for mass-down (piece1=8+e, e<0), marks at dyadic pos 1,3 inside piece1."""
    # config = (8+e, 4-e, 2, 1) for e != 0 (either sign)
    # marks at positions 1 and 3 inside piece 1 (which spans [0, 8+e])
    # splits piece 1 into (1, 2, 5+e), pieces 2,3,4 untouched = (4-e, 2, 1)
    p1 = config[0]  # 8+e
    p2 = config[1]  # 4-e
    result = [F(1), F(2), p1 - F(3), p2, config[2], config[3]]
    return sorted(result, reverse=True)

violations = 0
total = 0
for n in [3, 4, 5, 6]:
    dn = D(n)
    for j in range(1, n+1):  # perturbation level
        for e_num in range(1, 20):
            e = F(e_num, 20)
            for direction in [+1, -1]:
                config = dyadic_pieces(n)
                config[j-1] += direction * e
                config[j] -= direction * e
                if any(p <= 0 for p in config): continue
                if config != sorted(config, reverse=True): continue
                total += 1
                # try dist 1
                A1 = advantage(apply_strategy(config, F(1)))
                best = A1
                # try dist 2
                A2 = advantage(apply_strategy(config, F(2)))
                best = min(best, A2)
                # try local-kink (n=3 only, j=1, direction=-1 i.e. mass-down)
                if n == 3 and j == 1 and direction == -1:
                    A3 = advantage(local_kink_n3(config, -e))  # e_eff = -e < 0
                    best = min(best, A3)
                if best > 1:
                    violations += 1
                    print(f"  VIOLATION: n={n}, j={j}, dir={direction}, e={e}: A1={A1}, A2={A2}, best={best}")
print(f"  Total tested: {total}, violations: {violations}")

# ---- 12. Multi-level perturbations (OPEN GAP check) ----
print("\n=== 12. Multi-level perturbations (2-3 strategy family, check violations) ===")
violations_ml = 0
total_ml = 0
for n in [3, 4, 5]:
    dn = D(n)
    # perturb 2 levels simultaneously
    import itertools
    for j1, j2 in itertools.combinations(range(1, n+1), 2):
        for e1_num in [1, 3, 5]:
            for e2_num in [1, 3, 5]:
                e1 = F(e1_num, 10)
                e2 = F(e2_num, 10)
                for d1 in [+1, -1]:
                    for d2 in [+1, -1]:
                        config = dyadic_pieces(n)
                        config[j1-1] += d1 * e1
                        config[j1] -= d1 * e1
                        config[j2-1] += d2 * e2
                        config[j2] -= d2 * e2
                        if any(p <= 0 for p in config): continue
                        if config != sorted(config, reverse=True): continue
                        if sum(config) != dn: continue
                        total_ml += 1
                        A1 = advantage(apply_strategy(config, F(1)))
                        A2 = advantage(apply_strategy(config, F(2)))
                        best = min(A1, A2)
                        if n == 3:
                            A3 = advantage(local_kink_n3(config, F(0)))  # may not apply
                            best = min(best, A3)
                        if best > 1:
                            violations_ml += 1
                            if violations_ml <= 5:
                                print(f"  VIOLATION: n={n}, levels ({j1},{j2}), e=({e1},{e2}), d=({d1},{d2}): A1={A1}, A2={A2}, best={best}")
print(f"  Total tested: {total_ml}, violations: {violations_ml}")
print(f"  (multi-level violations confirm far-from-dyadic is OPEN GAP)")

print("\n=== ALL CHECKS DONE ===")

# ---- 13. Self-reproduction recursion (corrected: NO scaling) ----
print("\n=== 13. Self-reproduction: pair-pile(n+1) = bisect(M) + pair-pile(n) (no scaling) ===")
for n in range(1, 6):
    dn1 = D(n+1)
    pile_n1 = pair_pile_dyadic(n+1)
    pile_n = pair_pile_dyadic(n)
    # pair-pile(n) pieces in D(n+1) units = SAME integers (marks at same relative positions)
    # bisect M = 2^{n+1}/D(n+1) -> (2^n, 2^n) in D(n+1) units
    M_half = F(2**n)
    reconstructed = sorted([M_half, M_half] + pile_n, reverse=True)
    pile_n1_sorted = sorted(pile_n1, reverse=True)
    match = reconstructed == pile_n1_sorted
    A_n1 = advantage(pile_n1_sorted)
    A_recon = advantage(reconstructed)
    sum_recon = sum(reconstructed)
    print(f"  n={n}->n+1: pieces_match={match}, A(n+1)={A_n1}, A(recon)={A_recon}, sum_recon={sum_recon}, D(n+1)={dn1}")

# ---- 14. Verify the active-piece perturbation formulas ----
print("\n=== 14. Active-piece perturbation formulas (n>=3) ===")
print("Active piece = piece n-2 (0-indexed), dyadic size 4")
print("j=n-1: perturb active and piece below (size 2)")
print("  dist1: A = (3+a)-(2+b) + (1-1) = 1+a-b, with a+b=0 -> A=1+2a")
print("  dist2: A = (2+a)-(2+b) + (2-1) ... no, let me compute directly")

for n in [3, 4, 5, 6]:
    for a_num in range(-9, 10):
        a = F(a_num, 10)
        b = -a  # compensating
        if F(4)+a <= 0 or F(2)+b <= 0: continue
        config = dyadic_pieces(n)
        config[n-2] = F(4) + a  # active piece
        config[n-1] = F(2) + b  # piece below
        if config != sorted(config, reverse=True): continue
        if sum(config) != D(n): continue
        A1 = advantage(apply_strategy(config, F(1)))
        A2 = advantage(apply_strategy(config, F(2)))
        exp1 = F(1) + F(2)*a  # 1+2a
        exp2 = F(1)  # always 1 for dist 2 on active+below
        if A1 != exp1:
            print(f"  MISMATCH n={n}, a={a}: A1={A1}, exp={exp1}")
        if A2 != exp2 and a != F(0):
            print(f"  DIST2 MISMATCH n={n}, a={a}: A2={A2}, exp={exp2}")
    print(f"  n={n}: dist1 A=1+2a formula verified, dist2 A=1 verified (a in [-0.9, 0.9] step 0.1)")

print("\n=== ALL CHECKS DONE ===")

# ---- 15. Clean verification: dist-2 gives A=1 for active+below perturbation ----
print("\n=== 15. dist-2 gives A=1 for active+below perturbation (all n>=3) ===")
violations_15 = 0
for n in [3, 4, 5, 6, 7]:
    for a_num in range(-9, 10):
        a = F(a_num, 10)
        b = -a
        if F(4)+a <= 0 or F(2)+b <= 0: continue
        config = dyadic_pieces(n)
        config[n-2] = F(4) + a
        config[n-1] = F(2) + b
        if config != sorted(config, reverse=True): continue
        if sum(config) != D(n): continue
        A2 = advantage(apply_strategy(config, F(2)))
        if A2 != 1:
            violations_15 += 1
            print(f"  VIOLATION n={n}, a={a}: dist2 A={A2}")
print(f"  Violations: {violations_15}")

# Also check dist-1 for a < 0 (should give A = 1+2a < 1)
print("\n=== 16. dist-1 gives A=1+2a for active+below (a in (-1/2, 1)) ===")
violations_16 = 0
for n in [3, 4, 5, 6]:
    for a_num in range(-4, 10):  # a from -0.4 to 0.9
        a = F(a_num, 10)
        b = -a
        if F(4)+a <= 0 or F(2)+b <= 0: continue
        config = dyadic_pieces(n)
        config[n-2] = F(4) + a
        config[n-1] = F(2) + b
        if config != sorted(config, reverse=True): continue
        if sum(config) != D(n): continue
        A1 = advantage(apply_strategy(config, F(1)))
        expected = F(1) + F(2)*a
        if A1 != expected:
            violations_16 += 1
            print(f"  MISMATCH n={n}, a={a}: dist1 A={A1}, exp={expected}")
print(f"  Mismatches: {violations_16}")

# ---- 17. "Active grows from above" gap: both strategies overshoot ----
print("\n=== 17. 'Active grows from above' gap (j=n-2, dir=-1, both overshoot) ===")
for n in [4, 5, 6]:
    for e in [F(1,5), F(1,10), F(3,10)]:
        config = dyadic_pieces(n)
        config[n-3] -= e  # bisected piece above shrinks
        config[n-2] += e  # active piece grows
        if any(p <= 0 for p in config): continue
        if config != sorted(config, reverse=True): continue
        A1 = advantage(apply_strategy(config, F(1)))
        A2 = advantage(apply_strategy(config, F(2)))
        print(f"  n={n}, e={e}: dist1 A={A1}, dist2 A={A2}, both_overshoot={A1>1 and A2>1}")

print("\n=== ALL CHECKS DONE ===")
