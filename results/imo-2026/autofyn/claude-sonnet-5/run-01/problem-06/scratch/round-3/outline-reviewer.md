## imo-2026-06 — outline review, round 3

Read: `results/imo-2026-06/current.md`, all five files in `results/imo-2026-06/approaches/`
(the four live outlines plus the imported lemma cache in `results/imo-2026-06/lemmas/`),
`/tmp/round-3/proof-outliner.md`, and all three round-3 math-explorer reports.
Independently re-verified (Python, exact integer arithmetic, not sympy `factorint`
for speed where it mattered):
- NC1/NC2's traces for `a_1=221,375` — exact match to the approach file's hand
  trace (`a_2..a_5=234,238,255,260` and `a_2..a_7=378,380,384,390,396,399`).
- The "forced primes" invariant `F_M` (used by `forced-primes-well-ordering`)
  on a fresh, previously-untested case `a_1=91=7\cdot13`: stabilizes at
  `{2,7,13}` by index 3 and never changes again through `M=1500` — consistent
  with the explorer's 24-case claim.
- The explicit window construction `H_K` (used by `explicit-window-backbone-
  construction`) on a fresh, previously-untested case `a_1=1073=29\cdot37`,
  `K=12`: zero covering failures across all `719{,}400` pairs among the first
  1200 terms — consistent with the explorer's claim and independently adds a
  25th confirming data point beyond the reports' own 24.

**Population-level note (agree with the outliner):** round-3 exploration found
`(\star\star)` (`W` itself finite) is very likely FALSE (`a_1=4199,4087`,
`|W|` growing past 21 primes with no plateau at `M=15000`). This is a real,
important negative result. The correctly-scoped shared target for the three
Gap-1 approaches is the strictly weaker Finite Covering Backbone Conjecture
(FCBC), and the reviewer-generalized `theorem-2.2`/`theorem-2.4` already make
this sufficient (not just `W` finite) to finish the periodicity bridge. No
approach's outline this round secretly assumes `W` finite — checked each of
the three Gap-1 files explicitly; all state FCBC as the target and cite the
generalized theorems, not the retracted `(\star\star)`.

---

### 1. persistent-backbone-monovariant (revise) — CHANGES REQUESTED

**Verified sound:** the certified content (Lemma C, NC1, NC2) is unchanged
and already reviewer-certified; not re-litigated. The new algebra this round
— `q^*\le r\cdot a_n/n`, `a_n/n\to L` a genuine constant (from Lemma 1), so
`\omega(a_n)\le M$ for every $n$ (a uniform bound) `\Rightarrow` `q^*(n)\le
M(a_1+L)` for every `n` — is correct and non-circular: it only uses already-
certified Domination Lemma + Lemma 1, three lines of algebra, checked by
hand. Since a bounded value has only finitely many possible primes below it,
this legitimately gives `\{q^*(n)\}` finite *if* `\omega(a_n)=O(1)` (a
uniform-in-`n` bound, not a per-term-only fact) is established.

**Issue (push back on this before building further):** the outline never
states a mechanism for the second half of the reduction — even granting
`\omega(a_n)=O(1)` and hence `q^*(n)` uniformly bounded, this only shows a
*specific* recruited prime at each step is drawn from a finite set
(**necessity**-flavored). It does **not** by itself show that this same
finite set of dominant primes actually *covers* every pair `i<j`
(**sufficiency** — the actual FCBC requirement). The Domination Lemma only
guarantees `q^*(n)` divides an `n/r`-*fraction* of `a_1,\dots,a_n`, not all of
them, and says nothing about coverage of arbitrary far-apart pairs. The
outline itself flags this ("also (separate, flagged) that even a finite set
of ever-dominant primes must be shown *sufficient*...") but with zero
proposed mechanism — this is exactly the "lemma named without a mechanism"
pattern the reviewer role is asked to push back on. **Requested change:** the
builder must either (a) sketch a concrete bridge from "dominant primes drawn
from a bounded set" to "this set covers every pair" (e.g. a density/eventual-
saturation argument for each of the finitely many candidate primes), or (b)
if no such bridge is found, report honestly that closing `\omega(a_n)=O(1)`
alone does *not* finish FCBC, rather than silently declaring victory once the
`\omega`-bound is in hand. Do not let a builder claim FCBC closed from the
necessity half alone.

**Watch-out already correctly flagged, keep it:** `\omega(a_n)=O(\log\log n)`
(unbounded but slow) is a live alternative to genuine `O(1)`; the outline
explicitly warns against silently downgrading — good, keep this discipline in
the build.

### 2. forced-primes-well-ordering (new, copy) — CHANGES REQUESTED

**Verified sound:** Lemma FN (necessity: a singleton-intersection pair forces
its unique common prime into any covering `H`) is a genuine one-line
consequence of the covering definition — correct, no issue. The well-
ordering setup for Lemma FF (first-forced index `m(p)`, monotone `F_M`) is
mechanically fine and independently numerically supported (my own check on
`a_1=91`, plus the explorer's 24-case survey).

**Issue:** Lemma FF's actual contradiction mechanism is the weakest-
specified of the three Gap-1 outlines — it only says an infinite supply of
new single-use forced primes is "in tension with," "suggesting," and
"numerically correlated with but not proved to force" `\omega`-growth. No
quantitative claim is stated (e.g. "`k` forced primes among the first `M`
terms implies `\omega(a_j)\ge f(k)` for some explicit `j\le M`"), so there is
currently no candidate inequality to even attempt to prove — this is a
genuine gap in the outline, not just in the proof. **Requested change:**
before the builder spends effort on Lemma FF, the outline (or the builder's
first step) must state a *precise* quantitative bridge claim connecting
count-of-forced-primes to `\omega`-growth (or explicitly abandon this
mechanism and pick a different one, e.g. borrowing directly from the
sibling's cleaner `\omega`-bound algebra). As written, "suggesting" is not a
mechanism.

**Also flag, same as sibling:** step 5 (sufficiency of `F`, or an augmented
`F`) is a second, independent open gap, correctly flagged as not to be
conflated with Lemma FF — good, keep this discipline.

**Shared-wall risk (explicit warning for next round, per CLAUDE.md and prior
memory rule):** both this approach and `persistent-backbone-monovariant`
ultimately need the *same* missing analytic bridge — a relationship between
"how many primes get recruited/forced" and "`\omega(a_n)` growth," mediated
through the Domination Lemma — just applied in opposite directions (forward
induction vs. contradiction). This is legitimate diversity of *technique*
(induction vs. well-ordering) on one open target, which CLAUDE.md and prior
rounds explicitly permit, but it is not full diversity of *obstruction*. If
both approaches report next round that they are stuck at the identical
"forced-prime-count vs. `\omega`-growth" wall, that is the trigger to stop
iterating on this pair and instead push `explicit-window-backbone-
construction` (or a fresh framing) harder, per CLAUDE.md's plateau-break
guidance.

### 3. explicit-window-backbone-construction (new) — CHANGES REQUESTED

**Verified sound and genuinely distinct technique:** unlike approaches 1–2,
this one does not go through `\omega(a_n)$/dominant-prime growth-rate
reasoning at all — its open content (step 6) is a purely combinatorial/
pigeonhole claim about realized "signature" values, structurally closer to
`intersecting-family-covering-construction`'s certified `\Sigma_n`-
stabilization (Lemma 2.3) than to the Domination-Lemma-based approaches. This
is the strongest diversity contribution among the three Gap-1 approaches —
keep it in the build set for that reason alone, independent of its own
progress. Steps 3–4 (every term meets `H_K`; finitely many signature values
realized) are correctly marked "free" — they really are trivial corollaries
of Lemma P and pigeonhole, no issue. Independently re-verified the
construction itself on a fresh case (`a_1=1073`, `K=12`, zero failures across
~720K pairs).

**Issue:** the outline's proposed mechanism (i) for the Key Lemma — "the
escaping common prime must itself already lie in some `rad(a_i)`, `i\le K'`,
for a slightly larger `K'`, and iterate/bound the number of enlargements
needed" — has no stated termination argument. Without one, this could in
principle recurse forever (enlarge `K` indefinitely without ever reaching a
sufficient window), which would not prove FCBC at all, just restate it in
a different form. **Requested change:** the builder must either produce an
explicit descent/monovariant showing the number of enlargements is bounded
(analogous to Lemma C's `|C_n|` non-increasing-integer argument — a genuine,
already-certified template to reuse), or pursue mechanism (ii) (`K` bounded
by a function of `\omega(a_1)` alone) with an actual argument, not just cite
it as an option. As written, option (i) is not yet a real proof strategy,
only a description of what a proof strategy would need to establish.

**Correctly flagged already:** the outline explicitly warns not to conflate
"finitely many signature values realized" (free) with "realized values
pairwise intersect" (open) — good, and it explicitly says to report an
honest partial result (`K` finite but not proved uniform) rather than
overclaim — good, keep this discipline.

### 4. intersecting-family-covering-construction (revise) — APPROVE

**Verified sound.** Re-derived Theorem 2.2's generalized proof
(`lemmas/theorem-2.2-H-hitting-characterization.md`) and Theorem 2.4's
pigeonhole argument (`lemmas/theorem-2.4-conditional-eventual-
periodicity.md`) line by line — both correct, no gaps, and correctly
conditional (never overclaimed as unconditional). This round's two
obstructions are well-posed, logically independent, and each carries an
honest, non-hand-wavy mechanism sketch:
- Obstruction 1 (coincidence lemma) is a precisely stated equality of two
  explicit minima, with a concrete strong-induction + gap-bound mechanism
  proposed (not a bare "then it follows") and strong, methodologically
  cleaned-up numerical support (60/60 checks, including at `n=1` where
  `\Sigma_1\subsetneq\Sigma_\infty`, using the corrected true covering set,
  not round 2's flawed `\mathrm{rad}(a_1)` guess).
- Obstruction 2 (injectivity of `G`) correctly imports crux `aimo-0577`'s
  *technique* (confine to a finite state, show the transition map is a
  permutation) as a hint to adapt, not a citation — consistent with
  CLAUDE.md's crux-corpus rule — and honestly notes no closed-form inverse
  exists here, so a genuinely new adapted argument (via greedy-minimality) is
  needed, not a transplant.
The outline explicitly warns a builder must not treat closing one obstruction
as closing the other — good discipline, matches the round-3 explorer's own
finding that both held independently on the same 7 test cases.

**On the "whole attempt vs. fragment" question (explicit note per dispatch):**
this approach's target is stated as *the whole problem, conditional on
`(\dagger')`* — a finite covering `H` supplied by a sibling. This is not the
CLAUDE.md-prohibited pattern of "one proof split across sibling slugs whose
shared gap kills them all together": (a) the Theorem 2.2–2.4 chain this
approach built is a complete, *unconditionally proved* theorem in its own
right (IF a covering H exists THEN periodicity), reusable by every Gap-1
approach regardless of which one (if any) eventually supplies `H`; (b) this
approach's own remaining content (Obstructions 1–2) is a self-contained
mathematical claim parametrized by "some valid `H`," not dependent on which
sibling produces it. This is standard "prove `A\Rightarrow B`, separately
attack `A`" structure, not fragment-splitting, and matches the precedent
already blessed by two prior rounds' outline-reviewers. Flagging this
explicitly so the pattern is on record, not because it is a new problem this
round.

---

### Field diversity assessment (summary for the orchestrator)

Three Gap-1 approaches, correctly scoped to the same open FCBC target (this
is legitimate per CLAUDE.md — same target lemma via different technique is
not the single-gap trap). Real distinctions:
- `persistent-backbone-monovariant`: growth-rate/inductive-invariant on
  `\omega(a_n)`, most developed partial algebra, but sufficiency step
  entirely unaddressed.
- `forced-primes-well-ordering`: well-ordering/contradiction on forced
  primes `F`, same underlying analytic bridge as the sibling above (forced-
  prime-count vs. `\omega`-growth), least-specified mechanism of the three.
- `explicit-window-backbone-construction`: purely combinatorial/pigeonhole,
  genuinely orthogonal to the other two (no `\omega`/Domination-Lemma
  dependence in its open step) — the best diversity hedge if approaches 1–2
  both stall on the shared bridge.
One Gap-2 approach (`intersecting-family-covering-construction`), cleanest
and most rigorous outline this round, independent of Gap-1's outcome.

**Explicit trigger for next round's orchestrator/outliner:** if both
`persistent-backbone-monovariant` and `forced-primes-well-ordering` report
being stuck at the identical "forced/dominant-prime-count vs.
`\omega`-growth" wall after this round's build, treat that as the single-
gap-trap signal for *that pair* specifically — do not open a third variant of
the same `\omega`-growth idea; instead push `explicit-window-backbone-
construction`'s pigeonhole route harder, or open a genuinely new framing per
`math-explorer-monovariant-mechanism.md` opening 4 (the `aimo-0727`-style
auxiliary-monovariant-with-converse-link technique, not yet attempted by any
live approach).

### Ranking

Registered `explicit-window-backbone-construction` fresh (cold-start Elo).
Copied `forced-primes-well-ordering` from `persistent-backbone-monovariant`
(outliner-directed branch: same target, two techniques). Ran `update_ranking`
across the whole sampled field (new cohort anchored against both each other
and the established `bounded-gap-density-covering`/`backbone-existence-crt`):
intersecting-family-covering-construction (1595, most complete/rigorous this
round) > persistent-backbone-monovariant (1554, most developed partial
algebra among Gap-1 attempts) > explicit-window-backbone-construction (1518,
new, strong independent numerical confirmation, genuine technique diversity)
> forced-primes-well-ordering (1510, new, least-specified mechanism) >
backbone-existence-crt (1467, parked) > bounded-gap-density-covering (1384,
confirmed dead-end on its distinguishing strategy).

---

build set: persistent-backbone-monovariant, forced-primes-well-ordering, explicit-window-backbone-construction, intersecting-family-covering-construction
