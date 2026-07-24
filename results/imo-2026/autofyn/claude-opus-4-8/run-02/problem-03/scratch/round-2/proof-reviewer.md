# Proof-reviewer report — round 2 — imo-2026-03 (IMO 2026 P3)

Answer under review: `c(n) = 2^n/(2^{n+1}−1)`, `D_n = 2^{n+1}−1`. Confirmed correct
(reviewer re-verified `n=1..4`: `2c−1 = 1/D_n` exactly; `c(1)=2/3, c(2)=4/7, c(3)=8/15`).
Reduction `c(n) = (1+max_LB min_XY f)/2`, `f = M`, still holds (certified round 1).

Three approaches reviewed independently. **All three are genuinely partial with honest,
correctly-delimited gaps. No overclaim of `solved` in any.** Verdicts below.

---

## 1. self-similar-recursion — CHANGES REQUESTED (Status: partial) ✔ correct

**Scrutiny of the headline claim (GAP-L "complete for integer/dyadic placements").**
I re-derived the parity argument from scratch:
- Lemma D (`f ≡ Σ mod 2` for integer pieces): `f = Σ − 2·Σ_{even} a_i`. CORRECT, trivial.
- Lemma E (`f ≥ 0`): grouping into descending brackets. CORRECT.
- Theorem F: `Σ(W_n) = D_n` is odd and preserved under cuts; integer cuts ⇒ integer pieces
  ⇒ `f` an odd integer `≥ 0` ⇒ `f ≥ 1`. CORRECT.
The parity route is sound and **genuinely closes GAP-L for the entire class of integer
(dyadic) cut placements** — the natural adversary and the one attaining the floor. This is
real, verifiable progress.

**Does it close GAP-L overall? NO.** Xiang Yu may cut at any real position; parity fails
for non-integer pieces. The builder is honest: Section 4 admits the residual is "at a vertex
whose pinned pieces are non-integer rationals, show `f ≥ 1`," and correctly notes parity is
provably insufficient there (a `d=3` scaling admits `f = 1/3` under the congruence — I
confirmed this obstruction). The reduction-to-vertices (piecewise-affine `f`, gradient
`∂f/∂y ∈ {−2,0,+2}`, min at a vertex) is a correct Weierstrass/LP-vertex argument, but the
non-integer vertices are the honest open gap. **I independently verified numerically that the
min of `f` over ALL real cut positions is exactly `1` for `n=1,2,3,4`** (random multi-cut
search found nothing below 1), so the residual inequality is TRUE but unproven.

- Lemma A (top-band localization), Lemma B (`f(P) = u + f(Q)`): re-derived and numerically
  verified (0 violations). CORRECT.
- Theorem G (cascade tightness, `min_XY f ≤ 1` via iterated top-bisection + P1): CORRECT.
- Lemma H (dominant-regime dichotomy) for GAP-U: CORRECT (peel + `f ≤ Σ`). GAP-U here is
  only the dichotomy — residual accounting open.

**Status recorded by builder (partial): CORRECT.** Gap remaining: (GAP-L residual)
non-integer polytope vertices; (GAP-U) residual-accounting closure. Outcome: **advanced**.

## 2. alternating-sum-threshold-potential — CHANGES REQUESTED (Status: partial) ✔ correct

**GAP-L dual-price "dead end" claim.** Verified as a legitimate NEGATIVE result about the
technique (not a proof that GAP-L is false): the min-weight perfect-matching LP dual equals
`f` tautologically (Lemma 2), and any fixed length-only price `φ` is forced `≤ 0` because a
cut can create an equal pair `x,x` matchable at cost 0 ⇒ `2φ(x) ≤ 0` ⇒ `Σφ ≤ 0 < 1`.
Correct; this rightly prunes the one-shot monovariant-dual route for the whole field. Not a
lemma (a non-existence argument), recorded in current.md.

**GAP-U reduction to Invariant (I) `g_b(P) ≤ Σ/D_b`.** I checked every proved piece:
- (★) `g_b(P) ≤ g_{b-1}(R)` via bisect-top / top-match + P1 (Lemma 4): CORRECT (I verified
  `f` is exactly preserved when adjoining the equal pair).
- Base `b=0`, STOP rule (`f ≤ Σ/D_b` ⇒ stop, `f ≤ a₁`): CORRECT.
- Geometric step under (H) `max(a₁,2a₂) ≥ (2^b/D_b)Σ`: I verified `1 − D_{b-1}/D_b =
  2^b/D_b`, so removed mass gives `Σ(R) ≤ D_{b-1}/D_b·Σ` and the IH closes to `Σ/D_b`.
  CORRECT.
- **Invariant (I) itself is TRUE and tight** — my first crude random search showed apparent
  violations, but a proper recursive search using the paper's atomic moves (bisect-top,
  top-match, generic match/bisect) gives worst ratio **exactly 1.0, 0 violations** over
  random `(b≤4)` configs. So the target is sound; the reduction is not chasing a false claim.

**Open gap (M):** `f(P) > Σ/D_b` AND `max(a₁,2a₂) < (2^b/D_b)Σ` (near-balanced, surplus
budget) — needs an amortised multi-cut phase bound. Genuine, well-diagnosed.

**Status recorded by builder (partial): CORRECT.** Outcome: **advanced**.

## 3. game-value-recursion — CHANGES REQUESTED (Status: partial) ✔ correct

New game-space framing. Lemma R0 (`0 ≤ f ≤ Σ`, peel identity): CORRECT. Reformulation
(LB lower bound ⇔ first mover claims `≥ 2^n` on any ≤n-cut refinement of `W_n` ⇔ `f ≥ 1`):
CORRECT. Theorem LB-A (Case A, top uncut): CORRECT but it re-derives the already-certified
Case 1. Base cases `n=0,1`: CORRECT. The crux (BNF, budget non-fungibility) is exactly
GAP-L Case 2, reached from the claiming-game side and left OPEN — no new gap closed, and the
upper bound is not attempted. Value is diversity (framing seed) only.

**Status recorded by builder (partial): CORRECT.** Outcome: **partial** (no gap closed).

---

## Lemmas certified into results/imo-2026-03/lemmas/

- `integer-parity-alt-sum.md` (Lemma D + Theorem F, restricted to integer cuts) — CERTIFIED.
- `alt-sum-two-max-minus-total.md` (Lemma 5: `f ≥ 2a₁−Σ`, `0≤f≤Σ`, peel) — CERTIFIED.
- `top-band-decoupling.md` (Lemmas A, B, Cor C) — CERTIFIED.
- `cut-and-pair-reduction.md` (Lemma 4 + Lemma H) — CERTIFIED.

Rejected/not separately cached: game-value's Lemma R0 (subsumed by
`alt-sum-two-max-minus-total`); the dual-price collapse (a non-existence result, recorded in
prose, not a reusable lemma).

## Scores (Correctness / Rigor / Progress, 0–10)
- self-similar-recursion: 10 / 8 / 8 — parity closes the integer case cleanly; non-integer
  vertices + GAP-U closure remain.
- alternating-sum-threshold-potential: 10 / 8 / 8 — GAP-U reduced to one verified-tight
  invariant with one delimited sub-case; GAP-L dual route correctly pruned.
- game-value-recursion: 10 / 9 / 4 — all correct but redundant with certified results; new
  framing but no gap closed.

## Goal Progress (for Eval History)
Status stays **partial** (no APPROVE — both extremal bounds still have a gap). Real movement:
GAP-L is now PROVED for all integer/dyadic adversary placements and shown tight (floor = 1);
GAP-U is reduced to a single verified-tight invariant with only the "middle regime" open; the
one-shot LP-dual route to GAP-L is proven dead (field-wide prune). 4 new lemmas certified
(6 total in cache). Ranking after round 2: self-similar-recursion 1546 (advanced) >
alternating-sum-threshold-potential 1541 (advanced) > game-value-recursion 1485 (partial).

**Remaining cruxes for round 3:**
- GAP-L residual: `f ≥ 1` at non-integer vertices of the cut polytope of `W_n` (exchange /
  perturbation toward a dyadic tie; parity provably insufficient). Numerically true (`n≤4`).
- GAP-U middle regime (M): amortised multi-cut phase bound; strengthen IH to track piece
  count `m` / a gentler per-cut rate.
Both are now sharply delimited single-inequality targets, not open cruxes. The two leaders
converge on complementary halves (self-similar → GAP-L, alternating-sum → GAP-U); consider
a build set that pairs GAP-L residual (self-similar) with GAP-U (M) (alternating-sum). The
single-gap trap is partially broken (three distinct routes), but GAP-L residual and GAP-U(M)
are each still shared walls — a focused exchange-lemma attack is warranted.
