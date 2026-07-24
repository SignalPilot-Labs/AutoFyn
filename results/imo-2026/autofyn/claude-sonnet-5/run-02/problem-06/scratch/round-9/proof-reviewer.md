# Proof review — imo-2026-06, round 9

Build set reviewed: `covering-system-construction`, `cofinite-window-capacity-bound`
(new), `greedy-exchange-cost-potential`.

All independent verifications below were done from scratch (own Python
reimplementations, not trusting the builders' scripts), per role rules.

---

## 1. covering-system-construction — Step 10 (Recruitment-Budget Lemma refutation)

**Claim under review.** The dispatched "Recruitment-Budget Lemma" proposes a fixed,
Q-level pool `W_{A,B} := P(a_{m_A}) ∪ P(a_{m_B})` (m_A, m_B the base-type earliest
witnesses) containing every prime the recruitment process can ever pull in against a
fixed disjoint base pair (A,B). The builder claims to refute this with a_1=209
(prime q=7 forced at recruitment round 2, lying outside W_{A,B}), and reports the
same escape on 5/7 tested seeds.

**Independent verification (own scripts, `/tmp/round-9/work/verify209.py`,
`verify209b.py`).**
- Reimplemented the greedy sequence generator independently (plain Python, trial
  division, no sympy dependency for the second script) and reproduced the exact
  terms claimed: a_1=209, a_2=220=2²·5·11, a_3=228=2²·3·19, a_4=231=3·7·11 — matches
  the file's hand-verification exactly.
- Reimplemented the recruitment process from scratch, using a different
  "persistence" proxy (occurrence count ≥5 in the tail half of a 3000-term window,
  vs. the builder's own proxy) and a different violation-detection loop. Result:
  Round 0 recruits q=2 (F'={2,5}), Round 1 recruits q=3 (F'={3}), Round 2 forces the
  earliest occurrence of extended type {3,11} to be a_4=231 (not a_2=220, whose own
  extended type at that stage is {2,11}), giving F'={7} and forcing q=7. Computed
  `W_{A,B} = P(228) ∪ P(220) = {2,3,19} ∪ {2,5,11} = {2,3,5,11,19}`. **7 ∉ W_{A,B}** —
  refutation independently confirmed, exact match to the file's claim including the
  specific witness shift (Witness Discontinuity Obstruction) that causes it.
- Ran a second independent check on a_1=247 (the file's claim of an even earlier,
  round-1 escape): my own simulation reproduces q=3 recruited at round 1 with
  `W_{A,B}={2,5,7,13,19}`, and 3 ∉ W_{A,B} — confirms the file's second example too.

**Assessment.** The counterexample and its generality claim are correct and
independently reproduced by a from-scratch reimplementation with different
methodological choices, which is the strongest form of confirmation available here.
The "expand the pool" rescue is correctly diagnosed as circular (it presupposes
finiteness of the very recruitment history whose termination is the open question) —
I agree with this diagnosis; no patch to it is apparent. No previously-certified
lemma is affected (the file correctly scopes the refutation to only its own new
proposed Lemma).

**No new lemma to certify here** — per established workspace precedent (round-3
Lemma F / round-6 Lemma I / round-8 "r∈S₀" precedent), a refutation of a proposed
mechanism is recorded as documentation (now in `current.md`), not packaged as a
standalone positive lemma file.

**Verdict: CHANGES REQUESTED.** Status: **partial** (matches the file's own
self-report — no overclaim). Real progress: a ninth mechanism for the FAH crux is
now ruled out, with the underlying cause (Witness Discontinuity Obstruction, already
certified) shown to concretely bite this specific new mechanism rather than remain
an abstract risk. Gap remaining: FAH/Symmetric FAH itself, unresolved as ever; any
future mechanism must avoid tracking any single distinguished witness across the
recruitment process.

---

## 2. cofinite-window-capacity-bound (new approach)

**Claim under review.** New approach importing the certified reduction chain
verbatim, then proving (1) a Cofinite Sufficiency Lemma (weakening literal FAH to
"cofinite" suffices for the certified CRT finish) and (2) a Confined-GCD Lemma (a
finite-alphabet divisor-class recast of the exception set), and reporting that the
resulting window-capacity counting bound stalls at the same
existential-to-universal promotion wall Lemma I already diagnosed.

**Independent verification of Confined-GCD Lemma (load-bearing algebraic step).**
Re-derived from scratch: for `g_n := gcd(a_n, a_{n_B})` with `n` an A'-occurrence
past `n_B`, any prime `r | g_n` with `r ∈ S₀` would force `r ∈ ρ(n) ∩ ρ(n_B) = A' ∩
B'`, contradicting rogueness (`A'∩B'=∅`) — so every prime factor of `g_n` lies in
`F'' = P(a_{n_B})\S₀`; combined with `g_n | a_{n_B}` this gives `g_n | b` (the
F''-part of `a_{n_B}`). Parts (b) (g_n>1, from Free Facts) and (c) (the `q*|a_n ⟺
q*|g_n` equivalence) are elementary and check out exactly as stated. This is
correctly distinguished from, and strictly stronger than, the previously-certified
Divisor-Chain Well-Definedness Lemma (which only bounds `gcd(a_{n_A},a_n)` by
`Div(a_{n_A})` without confining prime factors to F''). **Confirmed correct,
non-circular, fully unconditional.**

**Independent verification of Cofinite Sufficiency Lemma.** Re-derived the two-case
split (A'∩B'≠∅ trivial by the Projection Lemma's monotonicity under core growth;
A'∩B'=∅ uses the batch-recruited canonical prime `q*_{A',B'}`, an occurrence `n* >
N₀` past the exception threshold on both sides, giving `q*_{A',B'} ∈ A''∩B''`). The
step requiring `q*_{A',B'} ∈ S₁` (i.e. every currently-rogue extended pair's
canonical prime gets recruited in one batch round) is a legitimate use of the
already-established fact that there are finitely many `Q`-persistent base types
(hence finitely many disjoint extended-type pairs at any fixed S₀) — batch
recruitment of finitely many primes in one round is not new machinery, just
bookkeeping. **Confirmed correct.**

**Confirmed the stall is real, not an avoidable gap.** Re-examined both of the
file's two reasons independently: (i) infinite pigeonhole over the finite alphabet
`Div(b)\{1}` yields SOME infinite divisor-class, with nothing certified ruling out
other, non-`q*`-divisible classes also being infinite simultaneously; (ii) no
certified lemma (Divisor-Chain Well-Definedness, this round's own Confined-GCD
Lemma, Free Facts, Bounded/Generalized Bounded Gap, Adjacent Multiple Blocking,
Critical Prime Dichotomy) links `g_n` for one occurrence `n` to `g_{n'}` for a
different occurrence `n'` — each of these produces either a single-term magnitude
bound or a single-term existential divisor fact, never a cross-occurrence relation.
I could not find a rescue within my review time either (this matches the workspace's
now five-round pattern — rounds 3, 5, 6, 7, 8 all independently hit the identical
wall in different vocabularies), so I treat the stall as genuine and structural, not
a hand-waved gap.

**Spot-checked the a_1=11305 computational example** (D_bad = {103} after the file's
own self-correction of an arithmetic slip in-line — 1133=11·103, Div={1,11,103,1133},
excluding 1 (part b) and multiples of 11 leaves {103}) — arithmetic verified
correct.

**Verdict: CHANGES REQUESTED.** Status: **partial** (matches self-report). Two new
unconditional, non-circular, portable lemmas certified. Cofinite FAH itself (the
approach's headline target) is not proved; the gap is honestly and precisely
located, and independently confirmed as the same crux every other mechanism has hit.

---

## 3. greedy-exchange-cost-potential

**Claim under review.** Round-9 dispatched cheap-kill check (before attempting a
"predecessor-inheritance" successor mechanism): search for FAH failures in the
genuinely open |F'|/|F''|≥2 regime at properly-recruited cores. Builder reports
~270 fresh seeds, zero counterexamples found anywhere (only one qualifying
non-singleton instance on record, a_1=11305, reconfirmed with a larger sample).
Then proves a Successor-Transport Reduction Lemma and finds the underlying
"Successor Claim" stalls on the same Lemma-I obstruction.

**Independent verification of Successor-Transport Reduction Lemma.** Trivial but
correctly stated ordinary induction: given `q*|a_{n_{j0}}` for some `j0 ≥ J` (exists
since the set of divisibility indices is infinite/nonempty and `J` finite) and the
successor implication for `j≥J`, induction gives `q*|a_{n_j}` for all `j≥j0`. Checked
step by step — correct, non-circular (assumes only the conditional hypothesis).

**Independent verification of Same-Type Free Facts Vacuity.** Elementary and
correct: if `ρ(n)=ρ(n')=A'`, every prime of `A'` already divides both `a_n, a_{n'}`
by definition, so Free Facts' `gcd>1` conclusion is a tautology here and gives no
outside-S₀ information — contrasted correctly with its genuinely informative use on
DISJOINT types in Lemma G. Confirmed correct.

**Independent re-check of the seed-sweep methodology.** Reimplemented an
independent ~185-seed sweep (own script, `/tmp/round-9/work/sweep_fah.py`, a
different persistence proxy and violation search order than the builder's) looking
for |F'| or |F''| ≥ 2 rogue instances and checking exception rates. Found several
instances with SUBSTANTIAL exception rates (e.g. a_1=30361, round 1, 260/352
exceptions) — but in every such case the flagged rogue pair was itself further
refined by subsequent recruitment rounds in my own simulation (i.e. it was an
intermediate, not-yet-finally-settled core stage, exactly analogous to the
already-documented a_1=4807-at-unrecruited-core finding from round 8). This is
consistent with, not contradictory to, the builder's claim, which is specifically
scoped to "properly recruited" (stable) cores. I flag this as a genuine
methodological subtlety (my own sweep is a rough proxy and cannot rigorously
distinguish "final" from "intermediate" states the way the certified Finite Core
Theorem construction does) rather than a counterexample to the builder's report —
but it means the "≈270 seeds, zero failures" claim should be read as applying to the
specific class of instances the builder actually filtered for, not as an exhaustive
sweep of every intermediate rogue pair a naive simulation might produce. This is a
fair caveat for the record, not a refutation.

**Assessment of Step 3 (Successor Claim attempt).** Both routes (Critical Prime
Dichotomy on the would-be failing occurrence; Free Facts on the two consecutive
same-type occurrences) are checked concretely against real data (a_1=4807, 11305),
not merely cited by name — route (a) reproduces the already-certified
"branch-(a)-fires-generically-and-is-uninformative" pattern, route (b) is shown
vacuous by the newly-proved Same-Type Free Facts Vacuity fact. No rescue found; I
attempted no additional route myself beyond confirming these two are exhaustive
given the currently certified toolkit (matches the precedent set in rounds 3, 5, 6,
7, 8 of the same wall recurring under different framings).

**Verdict: CHANGES REQUESTED.** Status: **partial** (matches self-report). Real
progress: a large, mostly-corroborated computational sweep strengthening the case
for literal FAH, plus a new correct unconditional reduction lemma and a new correct
diagnostic fact. The successor step itself remains unproved and the gap is honestly
reported, not smoothed over.

---

## Cross-approach synthesis

All three mechanisms attempted this round — a global counting-budget bound
(covering-system-construction), a window-capacity divisor-class counting bound
(cofinite-window-capacity-bound), and a one-step successor/transport argument
(greedy-exchange-cost-potential) — independently arrive at the identical structural
obstruction: **the certified toolkit can produce an existential "some
occurrence/class/witness has property P" statement via infinite pigeonhole, but
never a universal "all sufficiently large occurrences have P" statement**, because
no certified lemma links two different occurrences of the same extended type to
each other (only a fixed witness to the general occurrence, or a general occurrence
to a fixed witness). This is now confirmed, independently, by three genuinely
different framings in a single round on top of five prior rounds' confirmations
(3, 5, 6, 7, 8) — strong evidence this is the actual crux of the whole problem, not
an artifact of any one approach's vocabulary. Per CLAUDE.md's plateau-breaking
guidance, future rounds should prioritize opening an approach that supplies a
genuinely new SOURCE of cross-occurrence information (not a new counting/pigeonhole
technique applied to the same single-witness data), e.g. jointly analyzing the FULL
infinite family of occurrences of a type rather than any single distinguished one
(as Step 4f's route-2 diagnosis from round 5 already suggested, and as this round's
synthesis independently re-confirms from three directions).

## current.md and lemma-cache updates made this round

- `results/imo-2026-06/current.md`: `## Status` and `## Approaches tried` updated
  with a round-9 summary; round-8 sections retained verbatim below for audit trail.
- Certified 4 new lemmas to `results/imo-2026-06/lemmas/`:
  - `cofinite-sufficiency-lemma.md` (cofinite-window-capacity-bound)
  - `confined-gcd-lemma.md` (cofinite-window-capacity-bound)
  - `successor-transport-reduction-lemma.md` (greedy-exchange-cost-potential)
  - `same-type-free-facts-vacuity.md` (greedy-exchange-cost-potential)
- No lemma certified from covering-system-construction this round (the Step 10
  result is a negative/refutation finding, correctly recorded as documentation
  rather than a portable lemma, per established workspace precedent).
- Ranker outcomes recorded for all three built slugs (all `partial`).

## Verdicts summary

- covering-system-construction: **CHANGES REQUESTED** (Status: partial)
- cofinite-window-capacity-bound: **CHANGES REQUESTED** (Status: partial)
- greedy-exchange-cost-potential: **CHANGES REQUESTED** (Status: partial)
