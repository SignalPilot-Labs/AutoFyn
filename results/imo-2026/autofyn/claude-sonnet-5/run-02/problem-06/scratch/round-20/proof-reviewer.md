# Round 20 proof-review — imo-2026-06

All four built slugs reviewed independently, from scratch: re-derived the
load-bearing algebra/logic of every claimed proof by hand, and independently
re-implemented every numeric check in fresh Python (distinct scripts from
the builders'). None of the four slugs claims Status `solved`; all four
self-reports were accurate.

## 1. `triangle-consistency-pigeonhole` — Status: partial (self-report
accurate). Verdict: **CHANGES REQUESTED**

**Claim reviewed.** §6.1 Constrained Singleton Coherence Lemma (+ two
corollaries): if `d* = gcd(a_{m_A}, a_x)` is the constant value of an
infinite pigeonhole class against a disjoint persistent type's occurrences,
and some `x` in that class is a singleton out-of-core occurrence
(`P(a_x)\S_0 = {q_x}`), then `d* = q_x^j`.

**Independent re-derivation.** Verified from scratch: `d*` is confined to
primes outside `S_0` (cited correctly from the already-certified
Confined-GCD Lemma / Double-Witness Nested Pigeonhole), and `d* | a_x`. So
every prime factor of `d*` is an outside-`S_0` prime factor of `a_x`,
i.e. lies in `{q_x}` by the singleton hypothesis. This forces `d* = q_x^j`
by unique factorization — a short, correct, elementary argument, no gap.
**Certified** to `lemmas/constrained-singleton-coherence-lemma.md`.

**§6.2 confound diagnosis.** Reviewed the claim that the round's positive
computational finding ("dominant class is always a prime power" on both
known hard test seeds) is fully explained by an *independent* mechanism
(the already-established Two-Sided Singleton Witness Theorem's witness
prime `q`, which by construction divides cofinitely many occurrences of the
far type already) — this reasoning is sound and correctly scoped (the file
explicitly claims it only for the two tested seeds, not as a universal
theorem, so there is no overclaim risk of the kind flagged in memory rule
20). Not certified as a portable lemma (it is a diagnostic tied to specific
computed instances, matching the Lemma-F/Lemma-I precedent), but is genuine,
correct content, useful as a standing screening check.

**§6.3 failed replication.** Honestly reported: a heuristic
core-recruitment procedure does not reproduce the workspace's documented
recruited cores on either known hard seed (over-recruits without
converging), so no new non-confounded test seed was obtained. No overclaim.

**§6.4 reduction argument.** Informal but sound reasoning that the sharpened
existence question is no easier in kind than the original Two-Sided
Singleton Witness existence hypothesis — correctly not presented as a
formal theorem.

**Gap that remains.** The Two-Sided Singleton Witness Theorem's existence
hypothesis (matching singleton witnesses on both sides of a rogue pair) is
still completely open in general; this round's new lemma is a genuine but
modest search-pruning sharpening, not a step toward closing it. Status
`partial` is correct.

## 2. `triangle-critical-dichotomy-witness` — Status: unsolved (self-report
accurate). Verdict: **RETHINK**

**Claim reviewed.** Universal Branch-(a) Dominance Theorem: for every
`n ≥ 2`, prime `p | a_n`, `e := v_p(a_n)`, `c := a_n/p^e ≤ a_{n-1}`.

**Independent re-derivation.** Re-derived the full proof from the certified
Bounded Gap Lemma (`a_n ≤ a_{n-1}+a_1`) plus strict monotonicity:
- `n ≥ 3`: `a_{n-1} > a_1` (monotonicity), so `a_n < 2a_{n-1}`, and since
  `p^e ≥ 2`, `c = a_n/p^e < a_{n-1}`.
- `n = 2`: `a_{n-1}=a_1`, `a_2 ≤ 2a_1`, so `c ≤ a_{n-1}` (non-strict).

Both cases check out exactly as claimed; tightness example (`a_1=5, a_2=10`)
verified by hand. **Independently re-simulated** on 6 seeds (15, 35, 105,
187, 209, 4807) — exhaustive check of every `(n,p)` pair up to 500 terms
each — zero violations, matching the builder's own ~2400-seed sweep.
**Certified** to `lemmas/universal-branch-a-dominance-theorem.md`.

**Consequence, correctly derived.** This proves branch (b) of the certified
Critical Prime Dichotomy Lemma is unconditionally vacuous (never fires),
killing this approach's dispatched mechanism (which requires *locating* a
genuine branch-(b) rescuer) at its root. The builder's §A equivalence check
(confirming this construction is genuinely different from the sibling's,
not a duplicate) is also correct on inspection but ultimately moot since
§B's independent finding kills the approach regardless.

**Verdict rationale.** No gap found in this negative result; it is a clean,
complete, and reusable kill of the dispatched mechanism. RETHINK (retire
this slug's mechanism) is the correct routing — not a failure of the round,
a genuine negative result with a portable byproduct lemma.

## 3. `a1-3q-subfamily-theorem` — Status: partial (self-report accurate).
Verdict: **CHANGES REQUESTED**

**Claims reviewed and independently re-derived/re-simulated:**
- Base case, illegality of `a_n+1`, Case (a) illegality of `a_n+2` — trivial,
  correct.
- Parity Witness Lemma (odd `n` ⟹ witness `i=n` for `a_n+2`'s illegality via
  `gcd(N,a_n)=gcd(N,2)`): re-derived the identity from scratch, correct.
- `n_0, K_0` closed forms (first Case-(b) occurrence): independently
  re-derived via case split on `q mod 3` and confirmed via Python for all
  primes `q ∈ [7,120)` — exact match on every case (`n_0(q+1)/3` or
  `(2q+1)/3`, `K_0 ∈ {4,5}`).
- The claimed unique exceptions to the window-sufficiency criterion
  (`q=7`, `q=11`) — independently re-derived the threshold inequalities and
  brute-force confirmed via Python enumeration over primes up to 80: these
  are exactly and only the two exceptions.
- Hand resolutions of both exceptions (`q=7,n_0=5,K_0=5`, witness `i=2`;
  `q=11,n_0=4,K_0=4`, witness `i=3`) — verified via direct gcd computation
  and confirmed via full greedy simulation that the predicted `3(q+i-1)`
  pattern actually continues past these points.
- `q=5` exclusion mechanism — independently simulated `a_1=15`: sequence
  is `15,18,20,24,...`, breaking the predicted pattern exactly at `n=3` as
  claimed (predicted 21, actual 20), matching the builder's stated
  single-candidate-fails mechanism.

All independently verified correct with **one minor arithmetic slip found**
in the open-gap discussion (the `k≥1` threshold constant should be
`(3q+2)/(q-3)`, not `(3q-1)/(q-3)`, re-derived via sympy) — this does not
change the stated conclusion (the correct threshold, ≤ 5.75 for `q=7`, is
still well below the actual `K≥7` for `k≥1`, so `n-1≥K` still always holds)
and does not appear in either certified lemma statement.

**Certified** both lemmas together to
`lemmas/a1-3q-parity-and-k0-window-lemmas.md`.

**The open gap is genuine, not hand-waved.** Case (b), `n` even, `k≥1`
requires a bound on the gap between consecutive integers coprime to a
composite modulus `qK` — the builder correctly identifies this is
structurally analogous to (though possibly much smaller than) Jacobsthal's
function, and honestly reports being unable to prove a sufficient bound
elementarily. The adversarial CRT construction (rad ≈ 1.16×10^13, actual
witness at `i=9`) is a fair, non-cherry-picked stress test showing the
naive pigeonhole is far too weak while a genuine bound likely exists — this
is presented as evidence, not proof, correctly.

**Verdict rationale.** Genuine, verified, substantial progress toward a
third restricted-subfamily theorem, but the theorem is not proved in full —
correctly `partial`, not `solved`.

## 4. `n1-periodicity-reconciliation` — Status: partial (self-report
accurate). Verdict: **CHANGES REQUESTED**

**Claim reviewed.** §7 Ambient-Statistic Obstruction, replacing round 19's
withdrawn Generalized Class-Blindness Obstruction (which round 19's review
found circular — its "two scenarios are a priori consistent... by
definition of open" step asserted, without construction, that a genuinely
divergent legal continuation exists).

**Independent check of the exact circularity fix (memory rule 7).**
Re-read §7.1's narrowed "ambient statistic" definition (formula never
references realized occupancy/values for `n > n_B`) and §7.2's proof
mechanism. The new proof's key move: construct a *purely formal* assignment
`σ` (not asserted to be an actual legal continuation of the deterministic
sequence) that agrees with the true sequence up to the cited window bounds
and diverges after — then check, premise by premise, that every cited
ambient premise's *formula* literally does not reference the diverged
region, so it is satisfied identically under `σ`. This is a genuine,
non-circular semantic-independence argument: since every cited premise is
by definition computable without consulting the diverged region, no valid
deduction from those premises alone can constrain that region — a standard
(if narrow) soundness-of-entailment fact, correctly distinguished from
round 19's illegitimate move (asserting a genuinely realizable alternate
continuation exists, which needs an actual construction). **This
genuinely closes the round-19 gap** — confirmed independently, not merely
trusted.

**Scope check.** §7.3 explicitly and correctly narrows what is covered:
only purely ambient facts (subsuming `escape-cost-vacuity.md` and
`density-argument-vacuity-corollary.md`), explicitly NOT the
occupancy-referencing (practically useful) forms of density
ratio/second-moment/Borel–Cantelli/Fourier/LP methods, which the file
states remain formally un-ruled-out. This is the correct, honest walk-back
from round 19's overclaim — verified against the file's own text, no
smuggled generality. **Certified** to
`lemmas/ambient-statistic-obstruction.md`, with the mandatory scope note
attached (any future citation omitting the scope note should be rejected).

**Vacuous FAH under 2|a_1 Corollary (§4.1).** Re-derived from scratch
(citing the already-certified Uniform Evenness fact): `2 | a_1 ⟹ 2 ∈
ρ_S(n)` for every core `S ⊇ Q` and every `n`, so every two extended types
share `2`. Correct, trivial, low-priority since the sibling
`even-seed-literal-periodicity-theorem` already fully solves this
subfamily unconditionally by a stronger, independent route. **Certified**
to `lemmas/vacuous-fah-under-2-divides-a1-corollary.md`.

**§4.2 negative finding (H2 does not trivialize under 2|a_1) and the §6.1/
§6.2 round-18 findings (odd-prime non-trivialization, |Q|=2
non-tractability)** were already reviewed and accepted in prior rounds
(round 18); re-skimmed this round, unchanged, no new issues found. Kept as
diagnostic documentation, not separately certified, consistent with
precedent.

**Verdict rationale.** Genuine, verified repair of a previously-flagged
circularity (a real closed gap, not just a retraction), plus two small
correctly-scoped new certified lemmas. Does not touch H1 or H2 directly, as
instructed by the dispatch — correctly `partial`.

## Certified lemmas this round (5 files)

1. `lemmas/constrained-singleton-coherence-lemma.md` (from
   triangle-consistency-pigeonhole)
2. `lemmas/universal-branch-a-dominance-theorem.md` (from
   triangle-critical-dichotomy-witness)
3. `lemmas/a1-3q-parity-and-k0-window-lemmas.md` (Parity Witness + k=0-
   Window Criterion, from a1-3q-subfamily-theorem)
4. `lemmas/ambient-statistic-obstruction.md` (from
   n1-periodicity-reconciliation, replaces the withdrawn round-19 version —
   do not cite round 19's Generalized Class-Blindness Obstruction, ever)
5. `lemmas/vacuous-fah-under-2-divides-a1-corollary.md` (from
   n1-periodicity-reconciliation)

## Not certified (correctly, diagnostic/scope-limited content)

- §6.2 Dominant-Class Confound Diagnostic (triangle-consistency-pigeonhole)
  — correct but explicitly scoped to only the two tested seeds, not a
  general theorem; kept as in-file documentation per Lemma-F/Lemma-I
  precedent.
- §6.4 reduction argument (triangle-consistency-pigeonhole) — informal
  reasoning, not a formal theorem, correctly not certified.
- §4.2, §6.1, §6.2 negative findings (n1-periodicity-reconciliation) —
  diagnostic, not portable machinery, matches precedent; already documented
  in current.md's standing cautions.

## Overall

`results/imo-2026-06/current.md` updated: Status remains `partial`
overall. 15th consecutive plateau round (6-20) on the main FAH crux (H1)
itself, but real, verified progress every round: this round killed a
mechanism at its root (Universal Branch-(a) Dominance), genuinely fixed a
previously-flagged circularity (Ambient-Statistic Obstruction), advanced a
new restricted-subfamily target substantially (a1=3q), and sharpened the
diagnosis of why the leading existence-hypothesis mechanism's positive
evidence is confounded. No slug overclaimed; all four self-reported
Statuses were accurate on independent review. H1 (FAH) and H2 (absorption-
chain termination) remain the two named open hypotheses for the general
case; the run's floor deliverable (2|a_1 solved; a_1=p^k solved) is
unchanged and unaffected by this round.

---

**Per-slug verdict lines:**

- `triangle-consistency-pigeonhole`: **CHANGES REQUESTED** (Status: partial)
- `triangle-critical-dichotomy-witness`: **RETHINK** (Status: unsolved)
- `a1-3q-subfamily-theorem`: **CHANGES REQUESTED** (Status: partial)
- `n1-periodicity-reconciliation`: **CHANGES REQUESTED** (Status: partial)
