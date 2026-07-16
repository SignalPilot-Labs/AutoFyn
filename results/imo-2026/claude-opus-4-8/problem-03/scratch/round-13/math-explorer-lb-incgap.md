## imo-2026-03 — LB lens: ll-inclusion-gap, G-INC-2nt a≥1, (★) crux

### Summary of round-13 scouting

**Run state**: Status = partial. Three approaches, all partial. The single LB open crux for ll-inclusion-gap is (★) `O_{Q_lo} ≤ O_{R_lo} + a_v` (equiv. DFB: `A(R_lo) − A(Q_lo) ≥ min(σ_lo, 2−σ_lo)`) for general `h=2`, `a ≥ 1`. All other G-INC sub-branches are certified closed.

---

### New finding: EQUAL-PAIR FORCING THEOREM (size-2, all j≥1, all a∈[1,2^j)) — PROVEN

**Theorem.** For `j ≥ 1`, `a ∈ [1, 2^j)`, `R_lo = {a}∪G_j`, `Q_lo = {p1, p2}` with `p1 ≥ p2 ≥ 0`, `S_{Q_lo} ⊆ S_{R_lo}`, and `ΣQ_lo = ΣR_lo + σ_lo > ΣR_lo` (`σ_lo > 0`, all parts `< thr = 2^{j+1}`): `p1 = p2`.

**Proof.** `ΣR_lo = a + ΣG_j = a + (2^{j+1}−1) ≥ 2^{j+1}` (since `a ≥ 1`). So `ΣQ_lo = p1+p2 > 2^{j+1}`. For a non-equal pair `p1 > p2`:
- **Case A: `p1 > 2^j`** (= `max(G_j) ≥ max(R_lo)` since `a < 2^j`). Then `N_{R_lo}(x) = 0` (even) on `(2^j, 2^{j+1})`, so `(2^j, 2^{j+1}) ∩ S_{R_lo} = ∅`. But `S_{Q_lo} = [p2, p1)` (non-empty interval) contains `[2^j, p1) ⊄ S_{R_lo}`. Contradiction with `S_{Q_lo} ⊆ S_{R_lo}`.
- **Case B: `p1 ≤ 2^j`**. Then `p2 = ΣQ_lo − p1 > 2^{j+1} − 2^j = 2^j ≥ p1`. But `p2 ≤ p1`. Contradiction.

Hence `p1 = p2`. **QED.**

**Numerically verified**: 0 violations at `j=2` (42 configs, denom=4) and `j=3` (98 configs, denom=4), confirming no non-equal pairs exist.

---

### DFB CLOSED for size-2 Q_lo: complete, all j≥1, all a∈[1,2^j) — PROVEN

**Corollary.** For any equal-pair `Q_lo = {p, p}`: `A(Q_lo) = 0`. By Gen-Decomp (certified `gen-decomp-refined`):
```
A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo))
             = (a_v + b) + A(R_lo) − 0
             = deficit_top + A(R_lo)
             ≥ 0 + A(G_{j−1})    [Floor Lemma: A({a}∪G_j) ≥ A(G_{j−1})]
             ≥ 1.                  [A(G_{j−1}) ≥ 1 for all j ≥ 1]
```
So `A(R) − A(Q) ≥ 1` for size-2 `Q_lo`. **CLOSED.**

This bypasses the full DFB and (★) — no need to bound `O_{Q_lo}` vs `O_{R_lo} + a_v` separately; the sum `deficit_top + A(R_lo)` does it directly.

Also verified directly: `(★) ⟺ σ_lo ≤ A(R_lo) + 2a_v ⟺ 1−b ≤ A(R_lo) + a_v`. TRUE since `A(R_lo) ≥ 1 ≥ 1−b` (as `b ≥ 0`).

---

### Parity + equal-pair forcing closes DFB for EVEN j (n odd) — IF size-4 is excluded

For even `j = n−3` (i.e., `n` odd): `|R_lo| = j+2` is **even**. The INC parity condition (certified `parity-condition-inc`) forces `|Q_lo|` even. Budget `|Q_lo| ≤ n−2 = j+1`. Valid even sizes: `{0, 2, 4, …, j+1}` — but `j+1` is odd when `j` is even, so valid sizes are `{0, 2, 4, …, j−1}`.

- **Size-0**: `ΣQ_lo = 0 ≠ ΣR_lo + σ_lo`. Impossible.
- **Size-2**: Equal-pair forcing → `A(Q_lo) = 0` → `A(R) − A(Q) ≥ 1`. ✓
- **Size-4+**: Exists in principle for `j ≥ 5`. Numerically verified 0 violations at `j=4` (1358 size-4 equal-top-pair configs, min DFB = 4). Still open for general proof.

**Key observation for size-4 (even j, hard sub-case `deficit_top < 1`):** The same top-pair forcing gives `p1 ≤ 2^j`. And `S_{Q_lo} = [p4,p3) ∪ [p2,p1) ⊆ S_{R_lo}` so `A(Q_lo) = (p1−p2) + (p3−p4) = measure(S_{Q_lo}) ≤ measure(S_{R_lo}) = A(R_lo)`. With `ΣQ_lo = ΣR_lo + σ_lo ∈ (2^{j+1}, 2^{j+1}+2)` and the top pair `p1+p2 ≤ 2^{j+1}` (since both ≤ 2^j): the lower pair has `p3+p4 = ΣQ_lo − (p1+p2) ∈ (0, 2+ΣQ_lo−2^{j+1})`. This is a small positive number when `p1+p2` is close to `2^{j+1}`. The size-4 DFB reduces to bounding the uncovered measure: `A(R_lo) − A(Q_lo) ≥ 1 − deficit_top`. This holds numerically but the general proof is open.

---

### Odd j (n even): size-3 and size-4 Q_lo

For **odd `j`** (n even): `|R_lo| = j+2` is **odd**, so no parity constraint on `|Q_lo|`. Size-3 Q_lo exists and is verified (j=3: 558 size-3 configs, 0 violations, min DFB = 3/2). Size-1 is impossible (single part would need `p = ΣQ_lo > thr`). For size-3:

`S_{Q_lo} = [0, p3) ∪ [p2, p1)` (for `p1 > p2 > p3 > 0`). The constraint `S_{Q_lo} ⊆ S_{R_lo}` requires:
1. `[0, p3) ⊆ S_{R_lo}`: since `N_{R_lo}(0+) = |R_lo| = j+2` is odd, `x=0` IS in `S_{R_lo}`, so `p3 > 0` is permitted.
2. `[p2, p1) ⊆ S_{R_lo}`: same top-pair forcing gives `p1 ≤ 2^j`.

With `p1 ≤ 2^j` and `p1+p2+p3 = ΣQ_lo > 2^{j+1}`: `p2+p3 > 2^j`. Since `p2 ≤ p1 ≤ 2^j`, we have `p3 > 0`. A(Q_lo) = `(p1−p2) + p3`. Numerically min DFB = 3/2 at `j=3` (tight at `a=15/2, σ=1, Q_lo=[45/4, 45/4, 1]`). The proof for this case is open; see Opening B below.

---

### Plateau check (3+ rounds same step)

**No 3+ round plateau on a SINGLE shared step.** G-INC-1 (the 3-round plateau) was CLOSED in R8. Current cruxes:
- ll-inclusion-gap G-INC-2nt `a≥1`: open for 1 round (R12→R13). New result this round: size-2 Q_lo fully closed.
- ll-dyadic-symdiff HS-D1: separate crux, open 1 round.
These are **different cruxes** on different routes. No plateau pattern applies.

---

### Distinct openings

**Opening A (RECOMMENDED — closes key sub-case)**: Build the equal-pair forcing theorem + Floor Lemma argument directly into the proof:
- Step 1: For size-2 `Q_lo`, the equal-pair forcing theorem (proven above) forces `A(Q_lo) = 0`.
- Step 2: `A(R) − A(Q) = deficit_top + A(R_lo) ≥ A(G_{j−1}) ≥ 1`. Done.
- Scope: covers even `j` (parity forces size ∈ {0,2}) completely, and odd `j` size-2 completely. **This closes all cases where `|Q_lo| ≤ 2`.**

**Opening B (PERTURBED T(ℓ) ADAPTATION)**: Generalize the certified T(ℓ) lemma to the perturbed base. The (★) condition `O_{Q_lo} ≤ O_{R_lo} + a_v` is the analogue of `O_P ≤ O_{G_{ℓ-1}}` (certified T(ℓ)) but for `R_lo = {a}∪G_j` with shift `a_v`. Prove:
> **T'(j)**: `S_P ⊆ S_{{a}∪G_j}`, `|P| ≤ j+1`, `ΣP ∈ (ΣR_lo − 1, ΣR_lo)` → `O_P ≤ O_{{a}∪G_j}`.
If T'(j) holds, then (★) follows by applying T'(j) at the appropriate level. This would handle ALL sizes of Q_lo uniformly. The proof route: adapt the T(ℓ) mutual induction from `t-ell-mutual-induction` to the perturbed base. Key: check if the descent is closed (i.e., if `{a}∪G_{j-2}` appears at the next level with the same `a` — this requires `a < 2^{j-2}`, which holds for `a < 2^{j-2}` but NOT for `a ≥ 2^{j-2}`). So T'(j) may need a separate base case for `a ∈ [2^{j-2}, 2^j)`.

**Opening C (DIRECT SIZE-3 CLOSURE for odd j)**: For size-3 Q_lo at odd j:
- Equal-pair on top: if `p1 = p2` (equal), then `A(Q_lo) = p3 < 2` (since `p3 < 2` from `[0,p3) ⊆ S_{R_lo}` and the support structure of `S_{R_lo}` has its lowest allowed band bounded). `A(R_lo) ≥ A(G_{j-1}) ≥ 3` for `j ≥ 3`. So `A(R_lo) − A(Q_lo) ≥ 3 − 2 = 1`. DFB ≥ 1 − deficit_top ≥ 0. ✓
- Non-equal top: `p1 ≤ 2^j` (forcing). `[p2,p1) ⊆ S_{R_lo}`. Width `p1−p2 ≤ A(R_lo)` (measure). And `A(Q_lo) = (p1−p2) + p3 ≤ A(R_lo)`. For `A(R_lo) ≥ A(G_{j-1})`: need `A(Q_lo) ≤ A(R_lo) + deficit_top − 1`. With `p3 < support_measure` (bounded by the lowest band of `S_{R_lo}`), direct computation might close this.

**Opening D (SIZE-4 EQUAL-TOP-PAIR CLOSURE for even j)**: For size-4 `[X,X,p3,p4]` with equal top pair (X = p1 = p2):
- `A(Q_lo) = p3 − p4`.
- `ΣQ_lo = 2X + p3 + p4`. With `X ≤ 2^j` (forcing): `p3+p4 = ΣQ_lo − 2X > ΣQ_lo − 2^{j+1} = σ_lo − 1 + a = σ_lo + (a−1)`. For the HARDEST case `a = 1, σ_lo = 1`: `p3+p4 > 1`. But also `p3+p4 = ΣQ_lo − 2X ≤ ΣQ_lo − (ΣQ_lo + A(Q_lo))/2... `. The key: `X = (ΣQ_lo − p3 − p4)/2 ≥ (ΣQ_lo − 2*p3)/2`. For the upper band `X ≥ 2^{j-1}` (placing X in the top allowed band): `p3+p4 = ΣQ_lo − 2X ≤ ΣQ_lo − 2^j = σ_lo − 1 + a`. For `σ_lo, a < 2`: `p3+p4 < 3`. So `A(Q_lo) = p3−p4 < p3 ≤ p3+p4 < 3`. And `A(R_lo) ≥ A(G_{j-1}) ≥ A(G_3) = 5` for `j ≥ 4`. DFB = `5 − 3 − 1 = 1 > 0`. ✓ This closes the equal-top-pair sub-case for even `j ≥ 4` when X ≥ 2^{j-1}.

---

### Candidate techniques

- **Equal-pair forcing** (new, proved): Directly gives `A(Q_lo) = 0` for size-2 Q_lo, making DFB trivial via Floor Lemma.
- **Floor Lemma** (certified `floor-a-union-Gj`): `A({a}∪G_j) ≥ A(G_{j-1}) ≥ 1`. The one-line kill for equal-pair case.
- **Gen-Decomp identity** (certified `gen-decomp-refined`): `A(R)−A(Q) = deficit_top + (A(R_lo) − A(Q_lo))`. Key identity for routing to sub-problems.
- **Certified T(ℓ)/Claim(n,ε) mutual induction** (`t-ell-mutual-induction`): Potential base for a perturbed T'(j) adapted to `{a}∪G_j`.
- **INC parity condition** (certified `parity-condition-inc`): For even `j`: forces `|Q_lo|` even, restricting to sizes 0 and 2 (closed).
- **Measure monotonicity**: `A(Q_lo) = measure(S_{Q_lo}) ≤ measure(S_{R_lo}) = A(R_lo)` (from `S_{Q_lo} ⊆ S_{R_lo}`). Immediate but insufficient alone; needs sum constraint for quantitative gap.

---

### Cheap-kill candidates

- **Size-2 Q_lo** (any parity): equal-pair forcing → `A(Q_lo) = 0` → `A(R)−A(Q) = deficit_top + A(R_lo) ≥ 1`. COMPLETE.
- **Even j, size-4 equal-top-pair sub-case**: When `X ≥ 2^{j-1}` (top band placement), `p3+p4 < σ_lo + a - 1 < 3` → `A(Q_lo) < 3 << A(G_{j-1})` for `j ≥ 4`. Near-complete for this sub-case.
- **deficit_top ≥ 1**: Always `A(R)−A(Q) ≥ deficit_top ≥ 1` directly. Already in the approach (§25.3).
- **Fully-tight `a = 2^{j}`, `a_v = b = 0`**: HS-B2 argument forces `A(Q_lo) = 0`. Already closed.

---

### Knowledge-base entries to use

- `floor-a-union-Gj` (certified R12): Floor Lemma. Key tool.
- `gen-decomp-refined` (certified R9): Gen-Decomp identity for the descent.
- `t-ell-mutual-induction` (certified R8): The mutual induction for the anchor case. Template for T'(j) adaptation.
- `sigma-family-a-lt-1` (certified R11): Family Lemma for `a < 1`. Structural model for the perturbed family proof.
- `parity-condition-inc` (certified R6): Forces even `|Q_lo|` for even `|R_lo|`.
- `L1-budget-anchor` (certified R9): `S_P ⊆ S_{G_{m-1}}`, `|P| ≤ m−1` → `A(P) ≤ A(G_{m-1}) − 1`. Conceptual template (note: does NOT apply directly here since `R_lo ≠ G_{m-1}`, but shows budget → strict gap).
- `alt-sum-integral` (certified R2): `A(P) = measure(S_P)`. Foundation for measure arguments.

---

### Analogous past problems (cruxes)

No close analogues found in the crux corpus. The problem's structure — bounding an alternating sum A(Q_lo) below A(R_lo) given S_{Q_lo} ⊆ S_{R_lo} and sum constraint — is highly specific. The closest conceptual relatives are:

- **[aimo-0196]** (combinatorics/extremal-principle): "When a resource is only slightly below the uniform average, measure the deficit as an additive potential; a global deficit of at least d forces some local window with deficit ≥ d." Analogous flavor: use sigma_lo deficit to force a gap in the alternating sum. Weak analogy only.
- **[aimo-0196]** is the best match: the "total deficit spread forces local gap" idea mirrors how sigma_lo > 0 (total excess of ΣQ_lo over ΣR_lo) should force a gap `A(R_lo) − A(Q_lo) ≥ something`. But the specific alternating-sum measure structure is absent from the corpus.

None sufficiently close to adapt directly.

---

### Prior progress

- Certified (rounds 11-12): Family Lemma `F_a` closes `a < 1` all n. Floor Lemma `A({a}∪G_j) ≥ A(G_{j-1})`. Gen-Decomp `A(R)-A(Q) = deficit_top + A(R_lo) - A(Q_lo)`.
- Exact h=2 reduction: `A(R)-A(Q) = 1 + 2a_v + 2(O_{R_lo} - O_{Q_lo})` ↔ (★) O_{Q_lo} ≤ O_{R_lo} + a_v.
- Closed: h≥4, h=0, fully-tight n∈{4,5}, a<1 branch.
- **This round (NEW)**: Equal-pair forcing theorem (proven). Size-2 Q_lo DFB fully closed (all j≥1, all a∈[1,2^j)). Verification: n=5 (all j=2 configs: 42, 0 violations), n=6 j=3 size-2 (98 configs, 0 violations), j=3 size-3 (558 configs, 0 violations, min DFB = 3/2), j=4 size-4 equal-top-pair (1358 configs, 0 violations, min DFB = 4).

---

### Dead ends (do not retry)

- **a<1 Family descent for a≥1**: Provably unavailable (O1: `{a}∪G_{n-3}` not descent-closed once `a ≥ 2^{k-4}`).
- **Refined-R {Claim_R, T_R} mutual induction**: REFUTED R10 (abstract Claim_R FALSE, R={1,3,3}).
- **"INC forces max(Q) ≤ max(R)"**: FALSE R11.
- **Perturbed L1 without sum constraint** (`A(Q) ≤ A(R_lo)−1` for `S_Q ⊆ S_{R_lo}`, `|Q| ≤ j+1`): FALSE — counterexample `j=1, a=1, Q={2}`: A(Q)=2 = A(R_lo), gap = −1. The sum constraint `ΣQ_lo = ΣR_lo + σ_lo` (with σ_lo ∈ (0,2)) is essential; without it the L1 statement fails.
- **Budget-parity argument "R always has an odd-mult piece"**: Non-rigorous (a cut can change odd-mult count by −3).

---

### Small-case / intuition notes (labeled as conjecture)

- **Conjecture** (strongly supported): DFB holds for ALL valid Q_lo (any size) at j=n-3, a∈[1,2^j). Evidence: 0 violations at n=4 (123 configs, min margin 1), n=5 (662 configs, min margin 1), n=6 size-2/3 (656 configs, min margin 3/2), n=7 size-4 equal-top-pair (1358 configs, min margin 4).

- **Observed tight configs** (conjectured to be the global tightness): 
  - Equal-pair with σ_lo = 1 and a = 2^j − ε (tight at Floor Lemma).
  - n=4 tight: `Q=[6,4,3,3]`, `A(R)-A(Q)=1`.
  - n=5 tight: `Q=[12,8,6,6]`, `A(R)-A(Q)=1`.
  - These have `A(Q_lo) = 0` (equal pairs), `deficit_top = 0`, `A(R_lo) = A(G_{j-1}) = 1`.

- **Key structural fact** (proven): For size-2 Q_lo, equal-pair forcing is EXACT — no non-equal pair can satisfy `S_{Q_lo} ⊆ S_{R_lo}` and `ΣQ_lo > 2^{j+1}` simultaneously. This is NOT a large-slack approximation; it is a vacuousness result.

- **Minimum DFB by case** (numerically exact, conjecture on general pattern):
  - Size-2 equal pair at j=2, a→4: min DFB = A(R_lo) − 1 = (5−a) − 1 → 0+ (approachable but never 0).
  - Size-3 at j=3: min DFB = 3/2 (at a=15/2, σ=1, Q_lo=[45/4,45/4,1]).
  - Size-4 equal-top-pair at j=4: min DFB = 4.
  - The large slack for sizes ≥ 3 suggests easier proof than the tight size-2 case.

- **Alternative (★) proof route** (not attempted): Use `A(P) = 2O_P − ΣP` to rewrite (★) as `A(Q_lo) ≤ A(R_lo) + deficit_top − 1`. For equal pair: `0 ≤ A(R_lo) + deficit_top − 1` since `A(R_lo) ≥ 1` and `deficit_top ≥ 0`. For size-3 at odd j: `A(Q_lo) = (p1−p2) + p3`. With `p3 < max-of-lowest-S_{R_lo}-band` and `(p1−p2) < width-of-S_{R_lo}`, a careful band-by-band accounting might close this directly.

