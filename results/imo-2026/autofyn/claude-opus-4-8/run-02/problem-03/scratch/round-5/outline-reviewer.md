# Outline review — imo-2026-03, round 5

Problem is ONE gap from solved: upper bound `c(n) ≤ 2^n/D_n` fully certified; sole residual =
(LBL) `f ≥ 1` at the tied non-degenerate minimizer of `W_n`. Answer `c(n)=2^n/(2^{n+1}−1)`.
I ran the outliner's mandated cheap-kills before ruling (see "Checks I ran" at the end).

---

## self-similar-recursion (revise) — CHANGES REQUESTED, LEAD, BUILD

Route (Φ=Σx²-maximal minimizer ⇒ integrality via a generalized multiplicity-aware incidence
forest, dropping the refuted Lemma W) is sound in structure and is the strongest closer. The
phimax explorer's concrete computation supports it: the generalized incidence graph of the
`{2,3,3}` killer IS a forest and generalized leaf-peeling recovers the integers `2,3` — so the
round-4 counterexample breaks only Lemma W's *statement*, not a properly generalized Lemma S/T.
But the plan has TWO fixable defects the builder MUST close, plus one honest new gap:

1. **Power-of-two vs "even" error (Lemma T′).** The outliner writes "Φ-EVEN ⇒ every leaf
   multiplicity is a power of 2 (μ even or 1)." **"μ even" is NOT "μ a power of 2"** — a leaf
   with `μ=6` equal sub-pieces gives `w=2^k/6 ∉ ℤ` (6 ∤ 2^k). Peeling stays integral only if
   `μ ∈ {1,2,4,8,…}`. Fix (this is sound and I verified the mechanism): **even `μ≥4` is excluded
   by a two-invisible-pairs move** — pair the equal copies into two P1-invisible pairs and split
   them apart `{v,v},{v,v} → {v+t,v+t},{v−t,v−t}`; each pair stays internally equal so by P1 `f`
   is unchanged (the point STAYS in `G`), while `Φ` rises by `4t²`, contradicting Φ-maximality.
   This leaves only `μ∈{1,2}` (both powers of 2) plus odd `μ≥3` (handled by Φ-EVEN). State this
   even-μ exclusion explicitly; do not lean on "μ even ⇒ integer."

2. **Lemma Φ-EVEN's stated mechanism is the refuted V-kink move — replace it.** The outliner's
   mechanism ("P1 invisibility of the moved equal pair against a same-piece third") is *exactly*
   the 3-variable compensated shift `{v,v,v}→{v+s,v+s,v−2s}` that the round-4 reviewer AND the
   phimax explorer independently showed produces a **V-shaped kink** `f=m+2|s|` — i.e. `f`
   strictly INCREASES both directions, so the move LEAVES `G` and canNOT witness a Φ-increase
   *within* `G`. As written, Φ-EVEN reuses the discredited move and does not prove itself. The
   builder must find a genuinely Φ-increasing perturbation that *stays in G* for odd `μ≥3`, or
   invoke the phimax explorer's finding-2 lever directly: at the bad configs the Φ-max over `G`
   is attained at a **degenerate** competitor (`{2,3,3}` Φ=35 dominated by `{5,4,2,2,1,1}` Φ=51;
   non-integer continuum sup Φ=45), which the degenerate leg `Claim(N−1)` already handles for
   free. Odd-equal-splits are numerically far from `f=1` (my check: piece4→3 thirds gives f≥6.3;
   piece8→3 gives f=2.33; piece16→5 gives f=6.2), so Φ-EVEN is very likely TRUE — but the proof
   must not be the V-kink move. This is THE load-bearing new content, not cosmetic.

3. **Cycle⇒kernel through multiplicity edges (Lemma S′).** With `μ_{k,j}>1` a cycle vector must
   satisfy μ-ratio consistency around the loop; verify a nonzero `Ud=0` still exists on the
   generalized graph (or argue full column rank directly). Do not inherit the 0/1-graph cycle
   argument verbatim.

Do NOT reintroduce Lemma W or global integrality (both false). Integrality is claimed ONLY at the
Φ-max point.

## cut-budget-jacobsthal-recursion (new) — APPROVE (build) — REGISTERED

Genuinely different framing (bound the adversary recursion on cut BUDGET; never invokes sub-piece
integrality), reusing the CERTIFIED GAP-U delete-subtract template + certified Lemma I two-band
derivative. This is the plateau-breaker CLAUDE.md mandates after 2 rounds on the shared integrality
wall — and unlike pairing-injection it rests on proven machinery, not a wish.
**Cheap-kill PASSED:** I confirmed the target floor identity `min_{≤k cuts} f(W_n)=f(W_{n−k})`
holds EXACTLY — n=3: (5,3,1,1) for k=0..3; n=4: (11,5,3,1,1) for k=0..4 (the k=3,4 values reached
`1.00000` under targeted optimization; naive random search overshoots because the exact-tie
minimizers are measure-zero). So the Jacobsthal scaffold is real.
**Open gap (honest, hard):** the per-cut floor domination (step 3) — that XY's optimal single cut
against ANY reachable config is dominated by top-bisection of the current largest dyadic piece.
This is the crux; the band sign depends on the global cut configuration, so the exchange must
control WHICH piece is cut and in what ORDER. Register the two-band per-cut identity and prove the
exchange; do not assume the recursion. This is the field's only non-integrality framing — worth
carrying even though the crux is genuinely open.

## block-recursion-tievertex (revise) — CHANGES REQUESTED, NOT BUILT this round

The revise's headline NEW mechanism — **Lemma UPM via consecutive-ones total unimodularity** — is
**REFUTED by my cheap-kill.** Consecutive-ones (C1P) is FALSE, under *any* column order, on both
chordless AND chorded cycle incidence matrices (`[[1,1,0],[0,1,1],[1,0,1]]` and a chorded
4-cycle both fail C1P). But the residual UPM-5 vertices are *exactly* the ones that contain
chorded even cycles in `B` (the approach's own data: 24 at n=3, 3120 at n=4 contain a chorded
cycle yet still have a unique PM). A cyclic incidence matrix is never C1P (an induced chordless
cycle is a non-C1P submatrix, and C1P is hereditary), so C1P is FALSE on precisely the vertices
the route must handle. The "one-shot TU" plan cannot work. The outliner itself flagged this as the
cheap-kill; it fails.

What survives: the approach is NOT dead — its UPM-5 residual (chorded even cycles, verified n≤5)
stands as the honest round-4 wall, and the §2-hardening (case c′ for surviving within-piece ties
like `{2,3,3}`, which the upm explorer showed §2 currently mishandles with the same Lemma-W V-kink
failure) is legitimate necessary work. But (i) its new mechanism is refuted, and (ii) it is now
strictly dominated by self-similar for the residual: at the Φ-max minimizer the graph is a FOREST,
so chorded cycles never arise there — self-similar's Φ-max selection subsumes UPM by avoiding the
exact case block-recursion is stuck on. Keep it live in the population (fallback: superincreasing
top-peel, or the direct §2-c′ parity argument), but it is not worth a builder this round while
carrying a refuted mechanism plus two open gaps and being dominated by the lead.

## pairing-injection-endgame (new) — RETHINK / CUT — NOT REGISTERED

The entire content is an open gap: "no candidate injection `φ` exists yet; the residual-mass `≥1`
bound is unproven," and the outliner + fresh explorer both flag it may be impossible (rank order,
not origin, determines who claims what, so an origin-keyed injection may provably not respect claim
order). An approach whose whole skeleton is a wish with a self-flagged impossibility risk and no
construction fails the rigor bar — this is a doomed slug, and cut-budget already supplies the
genuinely-different (non-integrality) framing with proven machinery behind it. Not registered
(junk stays out of the pool). If the far-field pairing idea is to be pursued later, it must first
pass the outliner's own cheap-kill (script the candidate pairing against `{2,3,3}` f=1 and
`{4/3,4/3,4/3,2,1}` f=5/3) and arrive with an actual `φ`.

---

## Diversity / plateau note (for the orchestrator)

The two integrality routes (self-similar Φ-max, block-recursion UPM) have shared the tied-vertex
wall 2 rounds, and this round the phimax explorer's subsumption observation makes them NOT true
peers: Φ-max forest ⊋ UPM-unique-PM (the forest conclusion holds at the selected point and dodges
the chorded-cycle case block-recursion dies on). So the field is effectively ONE integrality route
(self-similar) + the certified UB (alternating-sum) + one genuinely different framing (cut-budget).
That is acceptable diversity for this round: the lead closer plus a non-integrality plateau-breaker
built on certified tools. If self-similar's Φ-EVEN and cut-budget's per-cut domination BOTH stall
next round, the tied residual will have cost 3+ rounds and the orchestrator should seed a fresh
framing far from BOTH integrality and cut-budget-recursion (the SOS/quadratic-certificate opening D
from the fresh explorer is the only untried genre left, though flagged high-risk).

## Checks I ran (this round)
- Cut-budget floor identity `min_{≤k cuts} f(W_n)=f(W_{n−k})`: EXACT for n=3 (all k) and n=4 (all
  k), confirming cut-budget's scaffold. (Nelder-Mead per split pattern; k=3,4 reach 1.00000.)
- Consecutive-ones on cycle incidence matrices: FALSE for chordless-3cycle, chordless-4cycle, and
  a chorded-4cycle under all column orders — kills block-recursion's C1P-TU mechanism on the
  residual (chorded-cycle) vertices.
- Odd-multiplicity equal splits at f=1: numerically far above 1 (6.33 / 2.33 / 6.2 in tested
  configs), supporting Φ-EVEN being TRUE (but the proof mechanism must still be fixed).

build set: self-similar-recursion, cut-budget-jacobsthal-recursion
