# Round 5 proof review — imo-2026-03

Reviewed all 4 slugs built this round independently. All claimed identities,
constructions, and counterexamples were re-derived/re-verified from scratch
(exact-Fraction Python scripts, not trusting the builders' own arithmetic).
No solved claim was made by any builder (all self-report Status = partial);
I confirm none should be upgraded to solved, and none should be downgraded
either — the self-reported partial/gap descriptions are all accurate.

## Summary verdicts

| slug | verdict | Status |
|---|---|---|
| greedy-halving-adversary | CHANGES REQUESTED | partial |
| rank-tie-vertex-reduction | CHANGES REQUESTED | partial |
| rank-pigeonhole-budget | CHANGES REQUESTED | partial |
| dyadic-band-occupancy | CHANGES REQUESTED | partial |

---

## 1. `greedy-halving-adversary` — CHANGES REQUESTED (Status: partial, confirmed correct as self-reported)

**Claimed:** New Lemma 14 (single-cut perturbation identity), used to prove
Proposition 15 — a rigorous counterexample refuting the round-5 outline's
claim (B) ("refining the tail beyond leaving it untouched never helps Xiang
Yu") as stated for arbitrary $F$.

**Independent verification.**
- Re-derived Lemma 14's proof from `cross-term-identity-threshold` — correct,
  no gap.
- Ran 3000 random exact-`Fraction` trials of the identity
  $A(S')-A(S)=2(I_1+I_2)-2f_2$ against direct sort-and-alternate-sum: **zero
  mismatches**.
- Re-verified Proposition 15's counterexample by hand and by script: for
  $n=2$, $F=\{p_1\}=\{4/7\}$, tail $\{2/7,1/7\}$: $A(F\cup T)=3/7$ confirmed;
  after splitting $p_3=1/7$ into $1/10, 3/70$: $A=12/35$ confirmed — a
  strict decrease, exactly as claimed. **The refutation is genuine and
  correct**, not an artifact.
- Re-verified the claimed strengthening (splitting $p_2$ with $F=\{p_1\}$
  leaves $A$ unchanged for every split point, not only the symmetric
  bisection) by scanning 99 split ratios of $p_2$ at $n=2$: $A$ constant at
  $3/7$ throughout, confirming the claim.

**Assessment.** Both the identity and the counterexample are correct and
non-trivial new results — the negative finding (claim (B) is false as
literally posed) is exactly the kind of honest, verified refutation the
population needs to avoid a false lead. However, the top-level target
(general lower bound for $c\ge1$) is unchanged: the "correct" replacement
claim ("refining the tail never pushes $A$ below $a_n$") is explicitly
flagged unproved. Real progress (a certified new general lemma + a certified
refutation), no gap closed on the crux. Status `partial` is accurate;
Status was not overclaimed.

**Certified lemmas:** `single-cut-perturbation-identity` (Lemma 14, full
certification, promoted to `lemmas/`); `refutation-of-tail-refinement-
monotonicity` (dead-end record, promoted).

---

## 2. `rank-tie-vertex-reduction` — CHANGES REQUESTED (Status: partial, confirmed correct as self-reported)

**Claimed:** Cross-Term Reduction Theorem (generalizes
`symmetric-split-c1-lower-bound` to arbitrary asymmetric single cuts on
$p_1$, reducing domination to a residual inequality $(\star\star)$); an
honest finding that $(\star\star)$ is the same obstruction reached by
sibling approaches; a second infinite tie-vertex family (§5.3, interior
cross-ties against an untouched tail) fully closed in closed form.

**Independent verification.**
- Re-derived the Cross-Term Reduction Theorem's window formula and the full
  identity from `cross-term-identity-threshold`; ran 20 random-trial exact-
  `Fraction` checks (n=3, random asymmetric top-cut $x$, random single-piece
  tail split) comparing the theorem's RHS against direct sort-and-alternate-
  sum: **zero mismatches**.
- The claim that $(\star\star)$ recovers `symmetric-split-c1-lower-bound`
  exactly at $\Delta=0$ is immediate from the formula (vacuous inequality
  $0\le0$) — checked, correct.
- Re-verified §5.3's closed-form family: computed $A(S_j)$ for $n=1,\dots,7$
  and every $j=3,\dots,n+1$ directly — reproduces exactly the claimed
  pattern (equality with $a_n$ only at $n\le2$; strict excess at $n\ge3$),
  **zero violations found**. This matches the claim precisely, including
  its honestly-flagged limitation (only checked $n\le7$, not proved for
  general $n$).

**Assessment.** Both new results are correct as stated, and the reviewer
independently confirms the honest self-assessment that $(\star\star)$'s
content is the same wall the sibling approaches hit (verified by directly
comparing the reduction's structure to `greedy-halving-adversary`'s claim
(B) and `rank-pigeonhole-budget`'s Case-A obstruction — all three ask, in
different language, for a bound on how much odd-parity mass an adversarial
tail refinement can place in a fixed window). This convergence-confirmation
is itself valuable (not wasted effort) but does not close the crux. Status
`partial` accurate.

**Certified lemmas:** `cross-term-reduction-theorem` (certified as a
reduction only — $(\star\star)$ itself is explicitly NOT certified, still
open); `interior-cross-tie-evaluation-formula` (certified for the closed-
form identity only — the "$\ge a_n$" corollary is checked $n\le7$ only, NOT
certified as a general-$n$ fact; this distinction is preserved in the
promoted lemma file to prevent a future round from treating it as proved).

---

## 3. `rank-pigeonhole-budget` — CHANGES REQUESTED (Status: partial, confirmed correct as self-reported)

**Claimed:** Claim (A)'s achievability half fully proved via an explicit
construction $F^*$ for every $n\ge2$; Lemma 1 (at most one fragment of $F$
exceeds $p_2$); an exact reduction (§3, eqns 3.1–3.4) of Case II's lower
bound to a strictly smaller self-similar instance, with an unconditional
sub-range fully closed.

**Independent verification.**
- Re-derived $F^*=\{p_2,\dots,p_n,p_{n+1},p_{n+1}\}$'s sum ($=p_1$) and
  $A(F^*\cup T)$ symbolically and by exact-`Fraction` computation for
  $n=2,\dots,8$: matches $a_n$ exactly in every case, **zero mismatches**.
  This is a clean, general, gap-free construction.
- Independently re-verified the new even-rank-sum identity
  $E(U)=\Phi(U\setminus\{\max U\})$ (used in the §3 reduction) by 2000
  random exact-`Fraction` trials with distinct-valued multisets (satisfying
  the strict-unique-max hypothesis): **zero mismatches**.
- Re-derived the algebraic chain (3.1)→(3.4) by hand: correct use of the
  already-certified `sharp-dominant-removal-identity`, correct
  Total$-A=2E$ identity, correct substitution of the ratio-2 ladder
  identities from (0.1). No gap found in the reduction itself.
- The claimed unconditional closure of the sub-range $s\le
  \mathrm{Total}(T'')$ (where $A(F'\cup T'')\ge0$ trivially suffices) is
  immediate and correct.

**Assessment.** The achievability half is a genuine, fully general,
gap-free new result (first explicit closed-form tight Xiang-Yu response for
this sub-case). The reduction is a real narrowing (not a restatement) —
correctly flagged by the builder as reducing to "the same shape one level
down" rather than literally solving Claim (A) for $n-1$. Case I is honestly
left untouched. Status `partial` accurate; no overclaim.

**Certified lemmas:** `claim-a-achievability-construction` (full
certification); `even-rank-sum-phi-identity` (full certification, fully
general fact independent of the ladder).

---

## 4. `dyadic-band-occupancy` — CHANGES REQUESTED (Status: partial, confirmed correct as self-reported; new slug, first build)

**Claimed:** Proposition 1 (band-decomposition identity, fully general);
Proposition 2/2b (cardinality-relaxed minimum of claim (A) is exactly 0,
proving the finite cut budget is load-bearing); Proposition 3 (a rigorous
counterexample refuting the round-5 outline's own "band-invariance formula"
conjecture); an honest comparison to `rank-pigeonhole-budget` (does not
supersede it — the coarser invariant genuinely loses information).

**Independent verification.**
- Re-derived Proposition 1's XOR-expansion algebra — correct, no gap.
- Re-verified Proposition 2b's inequality $A(T)<p_1$ by direct substitution
  of the closed form for $n=1,\dots,8$: holds in every case, matching the
  claimed general algebraic argument (final step: $(-1)^{n-1}<2\cdot2^n$,
  trivially true for $n\ge1$).
- **Re-verified Proposition 3's counterexample independently and in full**:
  reconstructed both partitions of the $n=4$ ladder's band $(2/31,4/31)$
  ($a_1,b_1$ and $a_2,b_2$, both distinct exact fractions), confirmed both
  sum to $p_1$ exactly, confirmed both lie strictly inside the target band,
  and independently computed $A(F\cup T)$ for both via sort-and-alternate-
  sum: got $3781/38750$ and $15031/155000$ respectively — **exactly matching
  the builder's claimed values**, and confirmed these are unequal
  ($93/155000\ne0$). **This refutation is genuine, exact, and correct.**

**Assessment.** This is a solid first build for a brand-new slug: it
delivers two fully general, gap-free reusable propositions plus a correct,
rigorous refutation of its own assigned key technique — and, crucially,
does not paper over the refutation but explicitly diagnoses (correctly)
that the coarse count/mass-per-band invariant cannot work because within-
band positions matter (confirmed by the very counterexample). The honest
comparison to `rank-pigeonhole-budget` (not a redundant duplicate, but a
strictly weaker invariant) is also correct — the two approaches decompose
$F$ at different granularities and Proposition 3 shows the coarser one is
provably insufficient. I considered RETHINK (since the assigned mechanism
is now shown incapable of closing claim (A) alone) but the builder already
produced two independent, certifiable, general-purpose lemmas from the same
investigation and correctly identified what finer information is needed —
this is exactly the "genuine new lemma + honest negative finding" pattern
that CHANGES REQUESTED (not RETHINK) has been used for elsewhere in this
run (cf. round 3 `self-similar-bracketing`, round 2
`self-similar-potential-certificate`). Status `partial` accurate.

**Certified lemmas:** `band-decomposition-identity` (full certification);
`claim-a-cardinality-is-essential` (full certification);
`band-invariance-conjecture-refuted-dead-end` (dead-end record, promoted).

---

## Overall Status: remains `partial` (no change)

No approach reached `solved`; the problem's general-$n$ upper bound and
general-$n$ lower bound (for $c\ge1$/asymmetric splits/general Case I)
remain open. `results/imo-2026-03/current.md` updated to reflect the
combined strongest state, including all round-5 findings and 7 newly
certified lemma files plus 2 dead-end records (see
`results/imo-2026-03/lemmas/`).

## Plateau assessment: **ESCALATE — the shared-gap-plateau threshold is now met**

This is the critical judgment call for this round. Tracing the history:

- **Round 2**: the crux was identified as "a cross-term / anti-concentration
  inequality on interleaved fragments" (mass-based bound proven too weak).
- **Round 3**: reframed (via two independent Vertex-Minimum Theorem proofs)
  as "a finite but uncharacterized tie-vertex enumeration."
- **Round 4**: narrowed to a single residual inequality (Proposition 10 /
  rank-pigeonhole-budget's $(\star)$), closed only for the symmetric $c=1$,
  $n=3$ sub-case.
- **Round 5**: **all four built approaches, working on four ostensibly
  different framings assigned by this round's outline (surrogate-undo
  perturbation identity, cross-term window reduction via LP-vertex
  geometry, discrete case-split/self-similar peeling, and band-occupancy/
  integral-peeling), independently arrive at structurally the identical
  wall**: an induction/reduction step that requires an **upper bound** on
  $A$ (or an equivalent quantity) for a smaller sub-instance, while the only
  inductive hypothesis available supplies a **lower** bound. This is
  explicitly and independently confirmed in-file by three of the four
  builders this round (`rank-tie-vertex-reduction` §5.2 explicitly compares
  its $(\star\star)$ side-by-side with `greedy-halving-adversary`'s claim
  (B) and confirms they are the same ask; `dyadic-band-occupancy` §5
  explicitly names this as "the identical obstruction already located from
  three independent directions... confirming, via a fourth and genuinely
  different derivation route... that the crux difficulty is real").

Per CLAUDE.md's shared-gap-plateau rule: "When the top approaches have all
bottomed out on the same step for 3+ rounds... the real problem is usually
that the approaches are too close." This is now **4 consecutive rounds**
(2, 3, 4, 5) of independent rediscovery of the same core obstruction, and —
new this round — the rediscovery is now happening **within a single round**
across 4 supposedly-diverse framings simultaneously, not just across
rounds. That is a stronger plateau signal than previously recorded (rounds
2–4 each contributed one framing reaching the wall; round 5 shows that
*every* framing tried this round reaches the *same* wall, regardless of
whether it starts from perturbation identities, LP-vertex geometry,
discrete pigeonhole/self-similar peeling, or integral band-occupancy).

**What this means for round 6, concretely (per CLAUDE.md's "challenge the
gap itself" instruction):** do not dispatch a fifth variant of "reduce to a
smaller/simpler instance of the same claim." The recurring failure mode is
specifically the *directionality* of the induction: every reduction
attempted so far produces a lower-bound inductive hypothesis but the
reduced statement needs an upper bound (or a two-sided/exact result) on the
peeled sub-instance. Round 6 should open at least one approach that either
(a) seeks a *simultaneous* two-sided (exact, not one-sided) inductive
invariant strong enough to supply the missing upper bound as a byproduct
(e.g. proving $A$ of the reduced instance lies in an explicit closed
interval, not just $\ge$ something), or (b) abandons the peel-one-piece-
and-induct paradigm entirely in favor of a genuinely global argument (e.g.
a potential/weighting function argument over the *entire* final multiset at
once, or a direct combinatorial/bijective argument bounding the total number
of odd-parity crossings) — this is the kind of "genuinely different
framing, far from the current field" CLAUDE.md calls for, not another
integral-identity or vertex-enumeration variant.

The four framings currently in the population (greedy-halving-adversary,
rank-tie-vertex-reduction, rank-pigeonhole-budget, dyadic-band-occupancy)
should stay live (each has certified, reusable new machinery worth keeping),
but round 6's new approach should be explicitly told to avoid re-deriving
"reduce to a smaller ladder instance" — that route has now been tried via
perturbation, cross-term/window, discrete pigeonhole, and band-occupancy,
and lands on the identical directional-bound gap every time.
