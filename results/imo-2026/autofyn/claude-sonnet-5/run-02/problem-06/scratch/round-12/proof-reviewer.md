# Round 12 proof-reviewer report — imo-2026-06

## Overall Status: partial (unchanged). FAH/Cofinite FAH remains the sole open
crux, now also expressible as EEA (Eventual Escape from Ambiguity) at some finite
core — shown this round to be the same difficulty, not an easier route.

---

## Slug 1: subword-complexity-periodicity (NEW approach)

**Verdict: CHANGES REQUESTED** (Status: `partial`, matches builder's own
self-report — no overclaim to correct).

### Independent re-verification performed
- **Lemma A (Gap–Periodicity Equivalence).** Re-derived from scratch by hand
  (3-line telescoping each direction). Correct, unconditional, no gap.
- **Lemma B (Right-Extension Determinism ⟹ eventual periodicity).** Re-derived the
  sliding-window strong induction from scratch: infinite pigeonhole gives a
  colliding pair `i<j` of length-`k` windows; induction on `m` re-applies `RED_k`
  to the shifted pair `(i+m-k+1, j+m-k+1)` at each step. Verified the shifted
  indices remain legitimate (`≥ i ≥ 1`) at every step. Correct, fully general
  (independent of this problem), no gap. Also checked the `RED_1⟹RED_k`
  monotonicity corollary — correct, one line.
- **Reduction (§3).** Correctly instantiates Lemma B on `x=(g_n)` with alphabet
  `{1,...,a_1}` (Bounded Gap Lemma) and combines with Lemma A. This is a genuine
  derivation, not a bare citation of Morse–Hedlund, satisfying CLAUDE.md's
  no-citation-only rule.
- **Proposition (§4, "vacuous target").** Trivial and correct: at most `L₀`
  residues mod `L₀` can be ambiguous, no argument beyond alphabet finiteness.
  **Cross-checked against the actual outline** (`/tmp/round-12/proof-outliner.md`
  lines 61–91): the outline itself already flags "PROVIDED every sufficiently long
  run of visits eventually lands only in safe classes — itself a claim needing
  proof, not automatic," i.e. the outline never claimed bare finiteness suffices.
  **The builder's "vacuous target" finding is a genuine, correctly-scoped
  sharpening of what the outline already flagged as open — not a mis-scoping or
  a strawman of the outline's real claim** (dispatch question (a): confirmed
  genuine).
- **Theorem C (EEA ⟹ periodicity).** Re-derived the functional-graph pigeonhole
  argument from scratch (map `h(r):=(r+f(r)) mod L₀` on the finite safe-residue
  set, pigeonhole on `L₀+1` consecutive residues, forward determinism). **Found a
  genuine flaw in the source's exposition**: the prose definition of "safe"
  ("all visits *eventually* agree") is logically inconsistent with its own stated
  crisp negation ("ambiguous = some two visits differ" — a zero-tolerance
  condition); the source proof even contains a self-flagged "wait, we must double
  check" digression trying to reconcile the two readings. Resolved by adopting the
  zero-tolerance reading (forced by the negation): under this reading the
  digression is unnecessary and the rest of the proof (which is what actually gets
  used) goes through unchanged. This is a wording/definition fix, not a hole in
  the mathematical content — certified `eea-implies-periodicity.md` with the
  corrected definition (dispatch question (b): Theorem C is a genuine,
  independently-checked alternative derivation, not circular, modulo this fixed
  wording issue).
- **§5 (why EEA doesn't close the gap).** Independently re-derived: "residue `r`
  becomes safe" requires the successor rule (which checks `gcd` against every
  earlier term) to eventually depend only on the finite `S₀`-residue; the
  certified Confined-GCD Lemma already shows the decision-relevant information
  lives in `F'/F''`-primes outside `S₀`, so establishing EEA for one ambiguous
  residue is literally an instance of full (non-cofinite) FAH. Confirmed this
  reduction independently — EEA is the same crux under new vocabulary, not a
  bypass, matching the file's own honest conclusion.
- **§6 (numerical check).** Spot-re-ran `a_1=4807` at core `S₀=Q`; reproduces the
  reported high ambiguity fraction. Consistent, expected, correctly not
  over-interpreted by the builder.

### Certification decisions
- **Certified** `lemmas/gap-periodicity-equivalence.md` (Lemma A) — clean,
  unconditional, no changes needed.
- **Certified** `lemmas/red-k-periodicity-lemma.md` (Lemma B + corollary) — clean,
  unconditional, fully general, reusable beyond this problem.
- **Certified (wording corrected)** `lemmas/eea-implies-periodicity.md` (Theorem
  C) — "safe" redefined to the zero-tolerance reading; the confused digression
  removed; mathematical content used downstream is unchanged.
- **Not certified**: the §4 vacuous-target Proposition — correct and important as
  a negative finding recorded in `current.md`, but a one-line consequence of
  already-certified facts, not independently reusable enough to warrant its own
  lemma file.

### Gap that remains (why this is `partial`, not `solved`)
EEA (equivalently FAH/Cofinite FAH) is not proved. The approach's own §5 honestly
shows the crux reappears under new vocabulary rather than dissolving.

---

## Slug 2: covering-system-construction (bookkeeping-only touch)

**Verdict: CHANGES REQUESTED** (Status: `partial`, matches builder's own
self-report).

### Independent re-verification performed
- **Reduced-Alphabet Corollary.** Re-derived the divisor-counting bijection from
  scratch: divisors `d|b` correspond to exponent tuples `(f_p)_{p∈F''}`,
  `0≤f_p≤e_p`; `q*∤d ⟺ f_{q*}=0`; excluding `d=1` gives
  `|D_bad(q*)| = ∏_{p∈F''\{q*}}(e_p+1) − 1`. Correct, one-line, built only from
  already-certified Free Facts + Confined-GCD Lemma + Singleton-Side FAH Lemma —
  **no circularity**.
- **Numerical re-verification (independent, from a fresh Python simulation of the
  actual greedy sequence, not the builder's numbers).** Simulated `a_1=4807`
  directly: `a_6=4845=3·5·17·19`, `a_7=4862=2·11·13·17`. With
  `S₀={2,3,5,11,19,23}`: `ρ(6)={3,5,19}`, `F'=P(a_6)\S₀={17}` (singleton, as
  required); `ρ(7)={2,11}`, `F''=P(a_7)\S₀={13,17}`, `b=13·17=221`. Taking
  `q*=17`: formula predicts `|D_bad(17)|=(1+1)-1=1`; direct enumeration
  `Div(221)={1,13,17,221}`, `D_bad(17)={d>1: 17∤d}={13}` — **exact match**
  (dispatch question (c): confirmed correct).
- **Scope statement.** Verified the file does NOT overclaim — it explicitly says
  this does not rule out any element of `D_bad`, does not generalize to a uniform
  bound, and does not resolve FAH. No overclaim found.

### Certification decision
- **Certified** `lemmas/reduced-alphabet-corollary.md` (file was already placed
  by the builder in `lemmas/`; this review independently verifies and finalizes
  the certification — correct, non-circular, unconditional, honestly scoped).

### Gap that remains
Pure bookkeeping; does not narrow FAH itself beyond making the residual alphabet
explicit. In the `|F''|=2`, multiplicity-1 case (every concretely computed
`|F''|=2` seed to date), the residual open question collapses to a SINGLE
divisibility-persistence question for one fixed integer — flagged in
`current.md` as the most concretely attackable fallback target for round 13 if no
new corridor is found.

---

## Answer to dispatch question (d): no overclaim

Neither builder marked its slug `solved`. Independent verification confirms
neither should be: the standing crux (FAH/Cofinite FAH, equivalently EEA at some
finite core) is not closed by either build. **`current.md` Status remains
`partial`.**

---

## current.md — updated (I own this file)

- Prepended a round-12 summary paragraph to `## Status` (kept prior rounds' text
  below for the audit trail, per the existing file convention).
- Appended a full `## ROUND 12` section with per-approach independent
  re-verification detail, matching the file's existing per-round convention.
- Appended a `## Lemma certification this round (round 12)` section.
- Appended `## Next-round guidance (current, round 12)`, flagging: (1) EEA and
  FAH are now known-equivalent-difficulty vocabularies, don't re-dispatch hoping
  EEA is a shortcut without a genuinely new ingredient; (2) the vacuous
  finite-defect idea is dead, don't re-propose it; (3) the Reduced-Alphabet
  Corollary's single-divisor-class alphabet in the `|F''|=2` mult-1 case is
  flagged as the most concrete residual fallback target for round 13 per
  CLAUDE.md's plateau-breaking escalation guidance.

## Lemmas certified this round
- `lemmas/gap-periodicity-equivalence.md` (Lemma A) — clean.
- `lemmas/red-k-periodicity-lemma.md` (Lemma B + monotonicity corollary) — clean,
  general-purpose.
- `lemmas/eea-implies-periodicity.md` (Theorem C) — certified WITH a wording
  correction to the "safe residue" definition (zero-tolerance reading; removes an
  internally inconsistent digression the source proof itself flagged as
  uncertain).
- `lemmas/reduced-alphabet-corollary.md` — finalized certification of the file
  the builder had already placed in `lemmas/`; independently re-verified exact
  numeric match on `a_1=4807`.

## Ranking outcomes recorded (approach-ranker MCP)
- `subword-complexity-periodicity`: outcome `partial`, round 12.
- `covering-system-construction`: outcome `partial`, round 12.

## Memory rules added
Two new rules appended to `/tmp/memory/proof-reviewer.md`:
1. Always cross-check a "vacuous/trivial target" finding against the actual
   dispatched outline text before accepting it as a genuine correction (not a
   strawman).
2. Never accept a derived-property definition at face value when its prose form
   and its stated crisp negation logically disagree — resolve by the reading
   forced by the negation, verify downstream use still holds, certify with a
   wording correction rather than rejecting sound content outright.
