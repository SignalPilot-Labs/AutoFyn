# Outline review — imo-2026-03, round 5

Answer under attack: c(n) = 2^n/D_n, D_n = 2^{n+1}−1 (certified consistent n=1,2,3; c(1) fully
proved). LB machinery L0–L11 certified. Two open walls: LB residual (PM) ∫[D odd] ≥ ∫D on the
{D≥2} interior, and the general-A UB (branch inequalities). I verified the load-bearing LB charging
example numerically (exact Fraction): Q_low={12/5,8/5,2,2}, C={1,2,4} gives ∫D=1 and ∫[D odd]=3, so
(PM) holds, and ∫D = sumQ−sumC = 1 matches the certified R1 identity. Skeleton spine is sound.

---

## induction-peel — APPROVE (advance), build
Elo 1693 (top). Verdict: the strategy is sound and the round-5 openings are concrete and honest.

- Step 1 (two-source charging dichotomy on k_C) rests on two certified facts — D(0+) ≤ 1−2k_C
  (§3.3) for the k_C≥1 bottom-band, and the surviving uncut H-part forcing a D=−1 top-band for
  k_C=0 — with the part budget c+k_C ≤ n as the joint cap. This is the correct lever: it consumes
  the part budget, NOT a cut-count-on-C cap (which round-4 refuted; the outline explicitly flags
  this). The band example I checked exhibits exactly the over-compensation claimed.
- Step 2 (positional-vs-path Abel summation) is a genuine second route; the strict-parity-
  alternation fact it rests on is L2/L3 restated per-origin, verified ~83% generic in the explorer's
  sweep. Sound.
- Issue to close while building (CHANGES-level, not fatal): the dichotomy is currently an
  *observed* pattern over sampled configs, not a proof — the explicit charging MAP (which D≥2
  sub-interval injects into which band's length) is the make-or-break and is still unwritten. The
  builder must produce the map, not just assert "surplus ≥ deficit by interval-length compare."
- Tie case (step 3, L9 self-pairing cancellation): must cover ALL tie configs, not just pure-
  BISECT — the outline says so; enforce it (cheap-kill first, as instructed).
- UB (step 4): the two-parameter (r = a_1/ρ, plus a secondary spread statistic) casework is the
  honest UB crux and is corroborated by the upper-bound explorer's three independent greedy-failure
  sweeps (F1 is a real structural fact — no single statistic threads {4,2,1}/{2,2,1}/{6,4,2}). This
  is hard but it is the only sound UB route on the table.

## alternating-sum-potential — APPROVE (advance), build
Elo 1580. Verdict: sound, and deliberately in a distinct LANGUAGE (β/matching, not D/parity).

- Step 1 (scale-bucket Hall-deficit): the mechanism — even-ranked mass at each scale bounded by
  the lower-origin-group partner mass Σ_{j<n}2^j = 2^n−1, with the part budget ≤2n+1 capping the
  shredding — is the correct global, budget-consuming form. It respects all four certified
  obstructions: O1 (bisect-all with unlimited cuts breaks the bound ⟹ MUST consume the budget),
  O2 (B={4,2,2,2,2,2,1}, β=6≤7 ⟹ accounting must be integral/global, not heightwise), O3
  (β-split reproduces W ⟹ global not single-split), O4 (majorization-only insufficient).
- Issue to close (CHANGES-level): the Hall deficit is stated as a mechanism but the actual
  injective matching (which lower-group unit pays for which even-ranked top shard) is the unwritten
  crux — same category of gap as induction-peel step 1, expressed in matching language. Build it as
  a concrete injection, and check it against O2 as a live test, not just cite O2.

## interlacing-bijection — APPROVE (new), REGISTER, build
Registered at Elo 1500 (→1502 after ranking). Verdict: a genuinely different framing (discrete/
combinatorial injection on the interleaving word) vs the two analytic LB mechanisms — this is the
breadth bet current.md explicitly called for ("a genuinely different framing on ≥1 approach is
warranted"). It is a WHOLE attempt: LB via the injection, UB imported from induction-peel.

- The reframing is well-grounded: newframing explorer showed S(B)=1 at A=P_n is a positive-measure
  union of interlacing cells (~4.7% at n=3), so the natural object for the {D≥2} gap is a rank
  pattern, not a measure — a target no live approach uses.
- HONEST caveat, carried into the build: this is a REFRAME, not yet a proof. The explorer found the
  target object but NOT the injection (step 3). The builder's job is to construct the excess→deficit
  injection; if it resists, the slug still de-risks the field by testing whether the discrete view
  beats the analytic charging. Keep it in pure word/crossing language — no measure-charging
  vocabulary — or it collapses into induction-peel.

## randomized-xy-cut — RETHINK, do NOT register, do NOT build
Verdict: fatal, by a SOUND a-priori obstruction that the outliner itself states and the upper-bound
explorer independently confirms. Not registered — junk stays out of the pool.

- The UB is a pure MINIMIZATION (XY minimizes S; no adversary responds to the randomization). For
  any distribution over ≤k-cut strategies, E[S] ≥ min_strategy S. The min already EQUALS the target
  (tight at the dyadic cascade, S=1/D_n exact, verified n=1,2,3). Hence E[S] ≥ target, with equality
  only if the law is supported entirely on minimizers — i.e. you must already produce the
  deterministic minimizing strategy. Randomization buys provably ZERO leverage; it cannot certify
  any value below the deterministic min.
- This is the SAME failure family as averaging-upper-bound, already recorded as a round-4 dead-end.
  My role bars re-running a recorded dead end. The gated "probe then fall back to branch
  inequalities" design does not rescue it: on the (certain) gate failure it collapses into
  induction-peel's step-4 branch inequalities — duplicating that slug's UB, not an independent
  approach. The upper-bound explorer agrees ("not a new mechanism… designing it is plausibly as
  hard as the branch inequalities themselves"). The 30s gate can be run as a throwaway diagnostic if
  desired, but it does not warrant a population slug or a builder. The honest UB effort belongs
  inside induction-peel step 4, where it already lives.

---

## Field diagnosis for the orchestrator (diversity / shared-gap risk)
- The UB wall is under-attacked and has NO sound new technique: every non-branch-inequality UB route
  (top-part averaging, whole-profile randomization, min-pairing witness, huffman/merge, LP duality,
  one-step and max-gap greedies) is now refuted or structurally dead. UB rides solely inside
  induction-peel's two-parameter branch-inequality casework this round. If that stalls again, next
  round needs a genuinely different UB *framing* (not another describable-strategy rule — F1 kills
  those), e.g. an adversary/potential argument that does not reduce to picking XY's move.
- All three live LB approaches (induction-peel charging, alternating-sum β-Hall, interlacing
  injection) target the SAME certified residual ({D≥2}/(PM)/Gβ). They use genuinely different tools
  (analytic charging vs matching-deficit vs combinatorial injection), which satisfies the breadth
  mandate — but they share one wall, so watch for a collective stall. interlacing is the intended
  discrete escape hatch; if the analytic pair stalls a 4th round, promote interlacing or seed a
  non-residual LB framing.

## Build set
Three builders, one per slug: two LB advances in distinct languages + the new discrete-framing LB
bet; UB is carried inside induction-peel step 4 (no separate UB slug survives the zero-slack
obstruction). randomized-xy-cut held out (RETHINK, unregistered).

build set: induction-peel, alternating-sum-potential, interlacing-bijection
