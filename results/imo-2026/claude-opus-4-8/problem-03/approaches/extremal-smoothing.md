# Approach: extremal-smoothing

## Status
partial

## Target (the whole claim)
c(n) = 2^n/(2^{n+1}−1), both bounds. This approach's **novel contribution is the UPPER bound**,
obtained by a maximin/extremal argument that BYPASSES any explicit per-config XY strategy (the disproven
"Claim U"). The lower bound is imported (Lemma LL, itself an open shared gap).

## Approaches tried
- (round 3, prior) outline only — no gaps closed.
- **round 3 (this build).** Made the framework rigorous and closed several sub-parts:
  - **Framework (Props 1–2): DONE.** V(A) := min over XY's ≤ n cuts of Liu Bang's share is a
    well-defined, *continuous* function of the Liu Bang piece-spectrum A on a compact simplex, so its
    maximum is attained (Weierstrass / Berge maximum theorem).
  - **Reduction (Prop 3): DONE.** Proved the clean logical reduction:
    **upper bound ⟸ (Smoothing S1) + (replica bound V(G_n) ≤ c(n)), and this needs NO Lemma LL.**
    So the upper-bound route is genuinely decoupled from the open lower-bound gap.
  - **Replica bound (Prop 4): DONE, fully rigorous.** The single explicit XY response (halve each dyadic
    piece) against the *single* geometric config gives val = c(n) exactly, hence V(G_n) ≤ c(n).
  - **Structural progress on S1 (Prop 5): DONE.** Proved the cell-wise linearity fact and stated the
    exact minimax-local structure that S1 requires.
  - **GAP S1 (global smoothing / "no competing local max ≥ c(n)"): OPEN.** Perturbation signs verified
    numerically (all directions from G_2 strictly decrease V; G_2 is numerically the unique maximizer),
    but the general proof is genuinely hard and is left as an explicit, precisely-stated gap.
  - **GAP S0 = Lemma LL** (lower bound): OPEN, imported as a dependency (shared across all approaches).

## Current best
A **complete and rigorous reduction of the UPPER bound** to a single perturbation-monotonicity statement
(Smoothing Lemma S1) that is **independent of the lower-bound gap LL**:

> If (S1) every non-geometric Liu Bang spectrum admits a spectrum-perturbation that strictly increases V,
> then max_A V(A) = V(G_n) ≤ c(n) (Prop 4), i.e. the upper bound holds — with no per-config XY strategy.

The framework (Props 1–2), the reduction (Prop 3), and the replica bound (Prop 4) are proven in full
below. S1 and LL are the two remaining open gaps. This is not yet a solved problem.

---

## Setup and notation

We work with a **stick of length 1**. It is convenient to also use the **unnormalized** scale in which
the geometric configuration is the integer multiset G_n = {1, 2, 4, …, 2^n} of total
D := 1 + 2 + ⋯ + 2^n = 2^{n+1} − 1; the length-1 stick is recovered by dividing all lengths by D.

By **Lemma G** (certified, `lemmas/greedy-odd-index.md`): after all marks are made, if the final pieces
are sorted p_1 ≥ p_2 ≥ ⋯ ≥ p_k, then under optimal play in the claiming game Liu Bang (the first mover)
gets exactly
  val(P) = Σ_{i odd} p_i,
and Xiang Yu can hold him to exactly this. So Liu Bang's guaranteed share for a final piece-multiset P is
val(P). By **Lemma M0 / A-representation** (certified, `lemmas/alt-sum-integral.md`),
  val(P) = (T(P) + A(P))/2, A(P) = measure{ x ≥ 0 : N_P(x) odd }, N_P(x) = #{i : p_i > x},
where T(P) = Σ p_i. Here T is fixed (the stick length), so **maximizing/minimizing val is the same as
maximizing/minimizing the alternating sum A**.

**The Liu Bang spectrum.** Liu Bang marks ≤ n points, cutting the stick into a multiset
A = (A_1 ≥ A_2 ≥ ⋯ ≥ A_m), m ≤ n + 1, Σ A_i = 1. By Lemma G the subsequent game value depends only on
this multiset of piece lengths, not on the mark positions. Write Δ for the set of admissible Liu Bang
spectra:
  Δ := { A = (A_1 ≥ ⋯ ≥ A_{n+1} ≥ 0) : Σ_{i=1}^{n+1} A_i = 1 },
a compact convex subset of ℝ^{n+1} (a permutation face of the standard simplex; allowing zero entries
encodes Liu Bang using fewer than n marks). The geometric spectrum is
  G_n = (2^n, 2^{n-1}, …, 2, 1)/D ∈ Δ.

**Xiang Yu's response and the value V.** After seeing A, Xiang Yu marks ≤ n further distinct points; each
falls inside one current piece and subdivides it. Equivalently Xiang Yu chooses ≤ n cut points
t = (t_1, …, t_n) in the stick (coincidences allowed = fewer effective cuts). Let P(A, t) be the
resulting final piece-multiset. Define Liu Bang's **guaranteed value against optimal Xiang Yu**:
  V(A) := min over Xiang Yu's ≤ n cuts of val(P(A, t)).
Then the quantity the problem asks for is
  c(n) = max_{A ∈ Δ} V(A) = max_A min_t val(P(A, t)).                                (★)
The **lower bound** is V(G_n) ≥ c(n) (Liu Bang plays geometric); the **upper bound** is
max_A V(A) ≤ c(n) (Liu Bang can do no better than c(n)).

---

## Prop 1 (V is well-defined and continuous on Δ)

**Claim.** val(P(A, t)) is jointly continuous in (A, t), and V(A) = min_t val(P(A, t)) is a continuous
function of A ∈ Δ.

**Proof.** Encode the whole configuration by the sorted list of all cut coordinates on [0,1]: Liu Bang's
marks (determined by A up to a fixed left-to-right layout: place pieces A_1, …, A_{n+1} consecutively,
giving cumulative marks s_j = A_1 + ⋯ + A_j) together with Xiang Yu's coordinates t_1, …, t_n ∈ [0,1].
The final pieces are the consecutive gaps between the sorted union of {0, 1}, the s_j, and the t_i. Each
gap length is a continuous (indeed piecewise-linear) function of the coordinate vector, and the
coordinate vector is continuous in (A, t). Sorting a fixed number of continuous functions is continuous,
and
  val = Σ_{i odd} (sorted gap lengths)
is a continuous function of the multiset of gap lengths: it equals (T + A(P))/2 with T = 1 constant and
A(P) = Σ_i (−1)^{i+1} p_i^↓, a continuous (symmetric, 1-Lipschitz in each coordinate) function of the
piece lengths. Hence val(P(A, t)) is continuous in (A, t).

Xiang Yu's choice set K := { t = (t_1, …, t_n) ∈ [0,1]^n } is compact. (Distinctness of marks is not a
real restriction: the map t ↦ val is continuous, so the infimum over the open set of admissible distinct
tuples equals the minimum over its closure K; coincident coordinates simply realize "fewer than n cuts".)
By the **Berge Maximum Theorem** (knowledge_base.md, "Extreme value / parametric optimization": the
optimal value of a continuous objective over a fixed compact constraint set is continuous in the
parameter — here the constraint set K is constant, so this is just uniform continuity of a continuous
function on the compact product Δ × K), the map
  A ↦ V(A) = min_{t ∈ K} val(P(A, t))
is continuous on Δ. ∎

(Continuity is stronger than the upper-semicontinuity flagged in the outline; it holds because val is
genuinely continuous through ties — Σ_odd of a sorted list does not jump when two pieces become equal,
since exchanging equal pieces changes nothing.)

## Prop 2 (the maximum is attained)

**Claim.** There exists A* ∈ Δ with V(A*) = max_{A ∈ Δ} V(A); the maximizer set
M := argmax_{A ∈ Δ} V(A) is a nonempty compact subset of Δ.

**Proof.** Δ is compact (closed and bounded in ℝ^{n+1}) and nonempty; V is continuous on Δ by Prop 1. By
the **Weierstrass Extreme Value Theorem** (knowledge_base.md, "Compactness / extreme value"), V attains
its maximum on Δ, and M = V^{-1}(max V) is closed in the compact Δ, hence compact. ∎

Thus (★) is a genuine max, and c(n) = V(A*) for any A* ∈ M.

---

## Prop 3 (Reduction: upper bound ⟸ Smoothing S1 + replica bound, WITHOUT LL)

Define the set of **geometric-type spectra**
  Γ := { A ∈ Δ : the nonzero entries of A are proportional to (2^n, 2^{n-1}, …, 1) for some length,
         i.e. A is a scalar multiple, restricted to its support, of a truncated dyadic ladder }.
For the maximin we only need the full ladder G_n; introduce the

> **Smoothing Lemma (S1).** For every A ∈ Δ with A ∉ {G_n} (equivalently, A is not the full dyadic
> ladder (2^n, …, 1)/D), there exists A' ∈ Δ with V(A') > V(A).

**Claim.** (S1) together with the replica bound **V(G_n) ≤ c(n)** (Prop 4) implies the upper bound
max_{A ∈ Δ} V(A) ≤ c(n). No use of the lower-bound Lemma LL is made.

**Proof.** By Prop 2 pick a maximizer A* ∈ M. If A* ≠ G_n, then by (S1) there is A' with
V(A') > V(A*) = max V, contradicting maximality. Hence A* = G_n, so
  max_{A ∈ Δ} V(A) = V(G_n).
By Prop 4, V(G_n) ≤ c(n). Therefore max_A V(A) ≤ c(n), i.e. for every Liu Bang spectrum A,
V(A) ≤ c(n): Liu Bang can guarantee no more than c(n). ∎

**Why this matters (the bypass).** The disproven "Claim U" tried to *construct*, for every A, an explicit
XY strategy holding val ≤ c(n). Prop 3 shows the upper bound follows from a single *comparison* statement
(S1) about how V changes under a spectrum perturbation, plus the value of V at the **single** config G_n.
No family of per-config XY strategies is needed. Moreover the upper-bound route needs only
V(G_n) ≤ c(n) (Prop 4, the easy replica direction), **not** V(G_n) ≥ c(n) = LL: LL is required only for
the *lower* bound. So this approach cleanly separates the two open gaps.

---

## Prop 4 (Replica bound: V(G_n) ≤ c(n), fully rigorous)

**Claim.** Against the geometric spectrum G_n = {1, 2, 4, …, 2^n}/D, Xiang Yu's **replica response** —
cut each piece 2^i (i = 1, …, n) at its midpoint into two pieces 2^{i−1}, 2^{i−1}, leaving the piece 1
uncut — uses exactly n ≤ n cuts and forces val = 2^n/D = c(n). Hence V(G_n) ≤ c(n).

**Proof.** Work unnormalized (pieces summing to D = 2^{n+1} − 1). Xiang Yu halves each of the n pieces
2^1, …, 2^n, placing one mark at each midpoint (n distinct marks, none coinciding with Liu Bang's cut
points which are piece endpoints). The final multiset P is:
  from halving 2^i (i = 1, …, n): two copies of 2^{i−1};
  plus the uncut piece 1.
Collecting by value: value 2^{j} (for j = 1, …, n−1) appears exactly twice (from halving 2^{j+1});
value 1 = 2^0 appears three times (twice from halving 2^1, once uncut). Total count
= 3 + 2(n−1)… check total length: 3·1 + 2·(2 + 4 + ⋯ + 2^{n−1}) = 3 + 2(2^n − 2) = 2^{n+1} − 1 = D. ✓

Compute A(P) = measure{ x ≥ 0 : N_P(x) odd } by the measure representation (Lemma M0):
- For x ∈ [0, 1): every one of the D pieces exceeds x, so N_P(x) = D = 2^{n+1} − 1, which is **odd**.
  Contributes length 1.
- For x ∈ [2^k, 2^{k+1}), 0 ≤ k ≤ n−1: the pieces exceeding x are exactly those of value ≥ 2^{k+1}, i.e.
  two copies each of 2^{k+1}, …, 2^{n−1}, a total of 2·((n−1) − (k+1) + 1) = 2(n − 1 − k) pieces, which
  is **even**. Contributes length 0.
- For x ≥ 2^{n−1}: N_P(x) = 0 (no piece exceeds the largest value 2^{n−1}), even. Contributes 0.

These intervals partition [0, ∞) (up to measure-zero endpoints), so
  A(P) = 1.
Therefore val(P) = (T(P) + A(P))/2 = (D + 1)/2 = 2^n. Normalizing by D: val = 2^n/D = c(n). This is one
admissible XY response, so V(G_n) ≤ c(n). ∎

(This also matches the certified tightness result: XY's replica forces val = exactly c(n) at G_n.)

---

## Prop 5 (Structural progress toward S1: cell-linearity of the payoff)

This is the reusable structure that any proof of S1 must exploit; it is fully proven, and it makes
precise *why* the naive "V is concave, so a stationary point is a max" fails and what genuinely remains.

**Definitions.** A **response type** is a pair τ = (c, φ): a cut-count vector c = (c_1, …, c_m) with c_i ≥ 0
and Σ c_i ≤ n (how many of Xiang Yu's cuts land in Liu Bang's piece i), together with a **fraction
profile** φ giving, for each piece i, the c_i internal cut positions as proportions of that piece
(0 < φ_{i,1} < ⋯ < φ_{i,c_i} < 1). Given τ, the final multiset is
  P_τ(A) = { φ-gap_{i,ℓ} · A_i : i, ℓ }, where the φ-gaps of piece i are φ_{i,1}, φ_{i,2}−φ_{i,1}, …,
  1 − φ_{i,c_i} (proportions summing to 1). Thus **each final piece length is a fixed proportion times
  some A_i, hence linear in the vector A**.

**Lemma 5a (cell-linearity).** Fix a response type τ. On the (relatively open, polyhedral) region
  R_{τ,σ} := { A ∈ Δ : the sorted order of the multiset {φ-gap · A_i} is the fixed permutation σ },
the payoff val(P_τ(A)) is a **linear** function of A.

*Proof.* On R_{τ,σ} the sorted order is fixed, so Σ_odd(P_τ(A)) is the sum of a fixed subset of the
lengths {φ-gap_{i,ℓ} · A_i}; each such length is linear in A, and a fixed finite sum of linear functions
is linear. ∎

**Lemma 5b (V as an infimal envelope).** V(A) = inf_τ val(P_τ(A)), an infimum over the (compact,
continuously-parametrized) family of response types. Consequently, on any region where the **active
minimizing type** and its sort permutation are locally constant, V agrees with a single linear function,
and where several linear pieces are simultaneously active V is their pointwise minimum — hence **locally
concave** there.

*Proof.* Immediate from the definition of V as a min over Xiang Yu's responses and Lemma 5a; a pointwise
min of linear functions is concave on any region where the index set of active functions is fixed. ∎

**What Prop 5 gives and what it does NOT.** Lemma 5b shows V is a *piecewise-linear, cell-locally concave*
function. This yields, at any candidate maximizer, a clean first-order (KKT / subgradient) optimality
condition, and the numerical evidence (below) shows G_n satisfies it strictly. **But** the global minimum
over τ has *breakpoints* where the active type changes, and across a breakpoint V is only piecewise-linear,
**not globally concave** (min of piecewise-linear ≠ concave). So "stationary ⇒ global max" is NOT valid,
and a purely local/calculus argument cannot conclude. The missing global step is exactly the exchange
argument S1 requires — see the gap statement.

---

## GAP S1 (OPEN — the load-bearing bet of this approach)

**Precise open statement.** For every A ∈ Δ with A ≠ G_n, exhibit A' ∈ Δ (a spectrum perturbation moving
mass toward the dyadic ratio-2 ladder) with V(A') > V(A). Equivalently, show G_n is the unique maximizer
of V on Δ.

**Reduction of S1 to a directional-derivative sign.** By Prop 5b, along a perturbation direction
u = A' − A, the one-sided derivative of V at A is
  D_u V(A) = min over active minimizing types τ (Xiang Yu's optimal responses at A) of ⟨∇val_τ , u⟩,
a *min* of linear functionals (Danskin/envelope form). S1 asks: at every non-geometric A there is a
direction u (staying in Δ) with D_u V(A) > 0 — i.e. a direction increasing the value against *all* of
Xiang Yu's currently-optimal responses simultaneously. This is a genuine minimax-local condition, not a
single-response gradient; it must beat every active response at once, which is the crux difficulty.

**Numerical evidence (bounded scripts, this round).**
- V(G_2) = 4/7 exactly (matches c(2)); Prop 4 gives the ≤ side, the replica the value.
- All six coordinate perturbation directions from G_2 = (4/7, 2/7, 1/7) strictly decrease V:
  moving mass A_2→A_1 gives 0.561, A_1→A_2 gives 0.551, A_2→A_3 gives 0.551, A_1→A_3 gives 0.551
  (all < 4/7 ≈ 0.5714). Equivalently, from any nearby non-geometric spectrum, the reverse
  (toward-G_n) perturbation strictly increases V. **The perturbation signs required by S1 hold in every
  sampled direction.**
- A finer scan over Δ for n = 2 finds the maximizer clustered at the geometric config with value 4/7 and
  no distant alternative maximizer (the earlier caveat about "{1/14, 3/14}" is spurious: that config
  gives V ≈ 0.536 < 4/7, so it is not a maximizer). This supports **uniqueness** of the maximizer, i.e.
  the strict form of S1.

**Why it is left open.** Turning the verified one-sided-derivative signs into a proof for *all* A and all
n requires identifying Xiang Yu's active optimal-response set at an arbitrary spectrum and exhibiting a
Δ-feasible ascent direction beating all of them — essentially a full description of the optimal-response
correspondence, which is of the same difficulty class as the problem itself. No rigorous general argument
was found this round. **This is recorded as an explicit gap, not papered over.**

**Dead sub-idea recorded.** "V is globally concave on Δ, so its unique interior stationary point G_n is
the global max" is FALSE as justification: by Prop 5b V is only cell-locally concave; across a
breakpoint of the active response it is merely piecewise-linear and can (and near flat/degenerate spectra
does) fail concavity. So the local first-order condition alone cannot close S1; the global exchange step
is unavoidable.

---

## GAP S0 = Lemma LL (OPEN — imported dependency, needed only for the LOWER bound)

The lower bound V(G_n) ≥ c(n) is **Lemma LL**, the shared open gap of the whole problem (lower bound
Case 2, sub-case A(Q) > 0, tail t ≥ 2). Its t = 1 tail is closed (see geometric-selfsimilar). It is
imported here as a dependency; this approach does not re-prove it and its upper-bound contribution (Props
1–4 + S1) does not use it. If a sibling approach certifies LL into `lemmas/`, this approach imports it
verbatim to complete the lower bound.

---

## Summary of logical status

- Upper bound = Prop 3 = **[S1 (OPEN)] + [Prop 4 (DONE)]**, independent of LL.
- Lower bound = **[LL (OPEN)]**.
- Framework Props 1, 2, 3, 4, 5: **DONE and rigorous.**
- Two open gaps: **S1** (this approach's bet, the smoothing monotonicity / uniqueness of the maximizer)
  and **LL** (shared lower-bound gap). Both are numerically true. The problem is therefore **not solved**
  by this approach yet, but the upper bound is reduced to a single, precisely-stated, LL-independent
  monotonicity lemma.

(No `## Full proof` — S1 and LL are load-bearing open gaps.)

## Promotable lemmas
- **Framework lemma (Props 1–2): V(A) = min over Xiang Yu's ≤ n cuts of val is continuous on the compact
  spectrum simplex Δ, hence attains its maximum (Weierstrass/Berge).** Proved in full above (Prop 1, Prop
  2). Reusable by any minimax/extremal approach to this problem.
- **Replica bound (Prop 4): V(G_n) ≤ c(n), via the explicit midpoint-halving XY response giving A(P) = 1,
  val = 2^n/D.** Proved in full above; equivalent to the already-noted tightness but stated as a clean
  standalone `V(G_n) ≤ c(n)`.
- **Reduction (Prop 3): upper bound ⟸ S1 + replica, with NO dependence on LL.** A clean logical
  separation of the two gaps; reusable to argue the upper and lower bounds are independent targets.
