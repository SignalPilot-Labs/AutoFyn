# Outline review — round 4 — imo-2026-03

Answer c(n) = 2^n/(2^{n+1}−1), D = 2^{n+1}−1. Target O ≤ c(n) ⟺ A := 2O−1 = μ{N odd} ≤ 1/D.
Certified/imported free: G1, R, H (closes UB Case A), Lemma S, fragment-count bound,
interleaving value 2^n, top-fragment cascade. Field-wide wall for 3 rounds: U1 = Case B.

I independently re-ran both numerical kill-switches (not trusting the outliner's numbers):
- **caseB-matching Lemma M** (exhaustive matching+halving over Case-B configs): 0 failures /800
  at n=2,3,4. In fact the best matching drives A to ≈0 (worst excess exactly −1/D each n) — the
  bound A ≤ 1/D holds with full room. The tight A = 1/D case is the geometric config, whose
  smallest piece equals 1/D (Case A boundary), so strict Case B is genuinely slack. Kill-switch
  PASSES strongly.
- **L1 Route A** (confined case a=0): min A = 1.000 with legal cut count k ≤ n; min A drops to
  0.05–0.42 with an illegal k = n+1 cuts. Confirms A ≥ 1 AND that the cut-count constraint is
  load-bearing (as flagged). Technique sound.

---

## direct-constructive — advance — APPROVE

Whole-problem attempt, most-proven line (elo 1592.9, certified G1/R/H/S/cascade). This round it
targets the cleanest wins (close the lower bound L1+L2) and pushes Case B.

- **L1 case a=0 (Route A identity)** — sound. Mechanism is real: A = 1 + 2·Σ_inverted(I_k−f_j),
  each term ≥ 0 by Lemma S applied crossing-by-crossing, path-independent hence an identity (not a
  circular reformulation — distinct from the dropped integral ‡). Verified A ≥ 1 numerically. The
  cut-count entry (k ≤ n needed for the n+1-slot interleaving) is correctly identified as
  essential and is the subtle load-bearing point the builder must write carefully.
- **L2 unreachable-interleaving** — sound. Mechanism: with a cut spent outside R_n only ≤ n
  fragments of R_n exist, so the n+1-slot interleaving is unreachable ⟹ an intact stranded at an
  odd rank ⟹ A > 1. Rests on the certified fragment-count bound. Confirmed (min O ≈ 8.04 > 8 with
  one stray cut, n=3).
- **U1 = Case B (IH(n) pair-creation)** — the genuine open risk. Base IH(2)/IH(3) proved by the
  explorer with clean algebra; the general induction step (doubly-hard leaf |b_j−b_{j+1}−b_{j+2}|
  < 1/D generalizing to n) is NOT yet shown to generalize. Flagged with a mechanism (sum bound
  (2^n−1)/D forces the residual singleton). Acceptable as a stated gap; the builder should
  prioritize L1+L2 (the sure wins) and treat the IH(n) generalization as the harder secondary.

Watch-outs correctly recorded: no ∫⌊(N_F−N_I)/2⌋ (circular), no per-rank bound r_{2j} ≤ 2^{n−j}
(false), Route A must use k ≤ n.

## caseB-matching — new — APPROVE, registered

Whole-problem attempt: reuses certified G1/R/H + direct-constructive's lower bound, substituting
the Case-B upper bound with a **finite matching-exchange** (Lemma M). Genuinely distinct route and
NOT a graveyard framing — it is induction-free (explicitly separated from direct-constructive's
IH(n)) and differs from all four graveyard framings (game-separation induction, concavity-of-g,
amortized-greedy, potential-duality). It puts a second live approach at the field-wide Case-B wall,
which is exactly the shared-plateau diversification CLAUDE.md asks for after 3 rounds on one wall.

- **Kill-switch genuinely applied and passing** — independently reproduced above (0 failures,
  A→0). Not a graveyard collapse: the mechanism is a combinatorial optimization over a finite
  matching menu, not a game induction or a potential/concavity claim.
- **Lemma M** is the single open core, flagged with a mechanism (exchange: swap two pairs or
  match↔halve strictly lowers A when A > 1/D; termination via Σa_i = 1 and all a_i > 1/D). The
  parity/XOR evaluator is correctly identified as the exact scoring tool, with the correct warning
  that the naive "altsum of residual gaps" is FALSE. Given my kill-switch shows A→0 achievable with
  full slack, the exchange proof has room and looks tractable.
- Minor: shares the lower bound with direct-constructive, so both die if L1/L2 fail — but L1/L2 are
  near-closed and numerically tight (low risk), and the intended rivalry is purely the Case-B
  route, which is the point. This is legitimate shared-cache reuse, not a split proof.

Budget lemma (|M|+|H| ≤ n) is routine but must be written for p = n+1 odd-leftover.

## lower-routeB — copy-of direct-constructive — CUT (not registered)

Route B (sub-problem induction) for L1. The outliner itself deprioritizes it ("build only if Route
A stalls; the reviewer may cut it"), and both the outliner and the lower-bound explorer flag that
Route B needs a generalized sub-statement (O_sub ≤ 2^n−1 is NOT G-L1(n−1)) that is itself an open
gap — i.e. Route B loops where Route A is a clean, numerically-confirmed identity. Route A has NOT
stalled (it is fresh and verified this round), so a parallel Route B builder is premature and would
thin the build set. Route B stays documented in the outline as a fallback; I do not register or
copy it this round. Revisit only if Route A stalls next round.

## Diversity note for the orchestrator

The field now has TWO distinct live routes at the Case-B wall: IH(n) induction (direct-constructive)
vs finite matching-exchange (caseB-matching). This breaks the 3-round single-framing plateau on U1.
The lower bound (L1/L2) is shared by both — if next round the lower bound unexpectedly resists, that
becomes a single-gap risk; but it is near-closed, so acceptable. If BOTH Case-B routes stall next
round, the orchestrator should demand a lower-bound-independent or a fresh Case-B framing.

## Ranking (updated, stale flags cleared)

direct-constructive 1592.9 (advanced, live) > caseB-matching 1516.5 (new, live, kill-switch passed)
> potential-duality 1464.0 (parked) > induction-recursion 1426.5 (dead-end).

build set: direct-constructive, caseB-matching
