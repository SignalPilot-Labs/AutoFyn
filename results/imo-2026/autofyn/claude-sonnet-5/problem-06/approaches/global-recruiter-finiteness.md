## Status
unsolved

## Round 7 Outline (proof-outliner directive — new approach, opened this
round: reframe the whole remaining gap as ONE global statement instead of
`\le2^k-2` separate per-core statements)

**Why this approach exists.** Round 7's dedicated orthogonal-mechanism
explorer (`/tmp/round-7/math-explorer-orthogonal-mechanism.md`) confirmed,
for the second time (after round 5), that no genuinely new *top-level
technique* (Ramsey/compactness/WQO/analytic-density/crux-corpus transplants)
escapes the shared `𝓥_S`-finiteness gap. Per `CLAUDE.md`'s plateau-break
guidance, this is honest evidence that no outside technique is waiting to be
found — so this new approach is **not** a fake "genuinely new mechanism" of
that kind. It is a genuinely different *reformulation of the target*: this
round's cross-bucket-domination explorer
(`/tmp/round-7/math-explorer-cross-bucket-domination.md`, §4) found that,
empirically, the eventual minimal-radical antichain support for **every**
tested proper core of a fixed `a_1` draws from the **same** small set of
extra primes, regardless of which core. If true in general, this replaces
`\le2^k-2` independent local hitting-set questions (one per core `S`, the
form every sibling approach currently attacks) with **one** global
existential statement about small primes — a different route to the same
destination, attacking the whole remaining gap from a global angle instead
of a local per-core one.

**The target: Hypothesis (GW) (Global recruiter-set).** There exists a
finite set of primes `W=W(a_1)`, disjoint from `P_1`, such that for **every**
proper nonempty core `S\subsetneq P_1`, every `C\in𝓥_S` (every radical value
ever minimal within class `S`, in the already-certified sense of
`persistent-backbone-monovariant`'s Theorem V / `imprint-automaton-
periodicity`'s Theorem V-MRS) has the form `C=S\cup Q` with `Q\subseteq W`.

**The reduction chain, if (GW) holds (mostly citation — low risk, do this
first once Step 0 below is resolved).** `(GW)\Rightarrow` `𝓥_S` finite for
every proper core `S` (trivial: `𝓥_S\subseteq\{S\cup Q:Q\subseteq W\}`, a set
of size `\le2^{|W|}`, since `W` is finite) `\Rightarrow` (via the
already-certified Theorem CD + Lemma TC, `imprint-automaton-periodicity`)
`𝓥` is finite `\Rightarrow` (via the already-certified Theorem V/V-MRS)
Hypothesis (MRS) holds `\Rightarrow` (via the already-certified Lemma MS)
FCBC holds `\Rightarrow` (via the already-certified Theorem 5.1) the whole
problem is solved, with exact periodicity from `n=1`. **This chain is pure
citation of already-certified lemmas**; the entire content of this approach
is proving (GW) itself.

**Step 0 (do this FIRST — a cheap kill/repair check on (GW) as literally
stated, found by cross-referencing this round's two explorer reports; do not
skip).** `(GW)` as stated requires `W` to work for **every** proper core,
including nested (depth-`\ge2`) ones, not just singletons. The cross-bucket
explorer's empirical table only tested singleton cores (verifying
`W(21528751)=\{2,3,7\}` against `S=\{103\}` and `S=\{197\}` alone). But this
round's sibling `multicompanion-induction` explorer independently found, for
the **same** `a_1=21528751`, a depth-2 core `S=\{103,197\}` with `D_S
\setminus P_1=\{2,3,7\}` (identical to the singleton cores' bound) yet a
**provably permanent** bundle `\{11,97\}` (via the newly-certified Permanent
Pair Lemma, `persistent-backbone-monovariant`'s Round 7 Outline — cite, do
not re-derive): `11,97\notin D_S\setminus P_1=\{2,3,7\}`, so this bundle can
never be dominated. `11,97\notin\{2,3,7\}=W(21528751)$ as claimed.
**This looks like a live, checkable counterexample to (GW) exactly as
stated.** Before any further development:
1. Confirm (independently, fresh computation) that `\{11,97\}` really is
   permanent for `S=\{103,197\}` — i.e. verify `J_S` is infinite (the
   Permanent Pair Lemma's standing hypothesis) and that no dominating
   witness ever appears (the explorer only checked to `n=50000`; push
   further if cheap, but the Permanent Pair Lemma's *proof*, once its
   hypothesis is confirmed, makes further simulation unnecessary — the
   conclusion is unconditional once `J_S` is confirmed infinite).
2. If confirmed: **(GW) as literally stated is REFUTED.** Do not force it —
   report this cleanly (a fast, honest kill is real progress, not failure)
   and pivot immediately to a weakened form, e.g.:
   - **(GW-depth)**: `W` may depend on core *depth* `|S|` (one finite set
     per depth level `1,\dots,k-1`, not one set for all of `P_1` at once) —
     test whether `W(a_1,\text{depth}=2)\supseteq\{11,97\}` for
     `a_1=21528751` and whether it is still small/finite and still
     `S`-independent *within* each fixed depth; or
   - **(GW-nested)**: `W` may need to depend on which *specific* singleton
     "parents" the core nests inside (e.g. `W` for `S=\{103,197\}` is a
     function of the individual `W`'s already found for `\{103\}` and
     `\{197\}`, plus new depth-2-specific recruits) — check whether `\{11,
     97\}` relates to the individual-witness "outlier" structure the
     multicompanion explorer flagged in §3.2's "Bonus structural insight"
     (index `596`'s `97`-instead-of-`11` anomaly).
   Either weakening still gives a genuine reformulation (a small number of
   finite sets, structured by depth, rather than `2^k-2` unrelated ones) —
   just not the cleanest possible version. If *neither* weakening survives
   a similarly cheap counterexample search, report that honestly too; this
   would be a valuable negative result closing off the whole reformulation
   family, parallel to round 6/7's induction refutations.
3. If Step 0.1 instead finds `\{11,97\}` is **not** actually permanent (e.g.
   `J_S` is finite for this `S`, so the Permanent Pair Lemma's hypothesis
   fails, or a dominator is found beyond `n=50000`), (GW) survives this
   particular challenge — proceed to Step 1 below, but flag this
   resolution explicitly so it isn't silently lost.

**Step 1 (only after Step 0 is resolved) — characterize `W(a_1)` (or its
depth-dependent replacement) explicitly.** The empirical table (4 `a_1`
values, `W=\{2,3\}`,`\{2\}`,`\{2,3,7\}`,`\{2,3,7\}`) suggests "smallest primes
not dividing `a_1`," but the unexplained "skip 5" anomaly (`2,3,7` for both
`2747=41\cdot67` and `21528751=103\cdot197\cdot1061`, neither divisible by
5) needs a real explanation, not a pattern-match — investigate whether `5`
is excluded because bundles built from it get dominated by something else
early, or some other structural reason. Do not present an unexplained
pattern as a proved characterization.

**Step 2 — attempt the actual mechanism for why small primes should suffice
(this is the genuinely open content; high risk, be honest if it fails).**
Candidate heuristic (explicitly NOT a proof): small primes divide a much
larger density of integers than any fixed large prime, so a term divisible
by a small `p\notin P_1` should recur "for free" inside almost every
companion set — combined with the already-certified Lemma ER (Eventual
Realization Dichotomy) and, once certified, `forced-primes-well-ordering`'s
Escape-Confinement Lemma, try to show any companion set built only from
primes outside a fixed small `W` is eventually dominated once the
corresponding small-prime bare value is itself realized. **Explicit
warning**: this has the same shape as the already-refuted Growth-Budget/
Markov/Cauchy–Schwarz pointwise-vs-cumulative attempts (rounds 3–6,
`current.md`) — do not resurrect that mechanism verbatim; find genuinely new
leverage (e.g. specific to *this* problem's structure) or report honestly
that (GW)/(GW-depth) resists this round's tools too, exactly as the
per-core framing already does. A confirmed "the global reformulation is
real progress in stating the problem more sharply, but the underlying
difficulty is the same" is a legitimate, valuable outcome — do not overclaim
a proof that isn't there.

**Step 3 (secondary, cheap) — broaden the empirical base before or alongside
Steps 0–2.** Test (GW)/(GW-depth) against more `a_1` values, especially ones
with `k=|P_1|\ge3` and multiple nested cores (not just `21528751`), to see
whether the depth-2+ tension found in Step 0 is a one-off or systematic.

## Round 7 Builder Update — (GW) refuted, (GW-depth)/(GW-nested) shown to be
no easier than the per-core statement, approach recommended DEAD-END

**Summary of verdict.** Step 0's counterexample is independently
re-confirmed (fresh computation, pushed further than before, to `n=100000`).
Beyond that numerical refutation, this round found a **structural** reason
the whole "global reformulation" premise cannot work, which forecloses
*every* repair (`GW-depth`, `GW-nested`, or any other finite-index-set
variant), not just the specific guessed `W={2,3,7}`: for a **fixed** `a_1`,
the family of proper cores `S⊊P_1` is **already finite** (`\le2^k-2` of
them, `k:=|P_1|` fixed once `a_1` is fixed — this is literally the constant
appearing in the already-certified Theorem CD,
`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`). A finite union of
finite sets is finite. Hence **`(GW)` is logically equivalent to** — not a
weaker or more tractable restatement of — **"`Λ_S` is finite for every
proper core `S`"**, the exact per-core statement `persistent-backbone-
monovariant` and `forced-primes-well-ordering` are already attacking
directly. Packaging `\le2^k-2` already-finite-in-number local questions into
"one global statement about a shared prime pool `W`" creates no new
leverage, because there was never an unbounded family to compress — Theorem
CD already performs exactly this finite-union reduction one level up (`𝓥`
finite `\iff` `𝓥_S` finite for each proper `S`) and is already certified;
`(GW)` merely re-derives the same trivial fact in more complicated
"companion-prime" language, for free, without simplifying anything. This is
a decisive, principled reason to close this approach, independent of and
stronger than the numerical refutation alone.

**1. Step 0 re-confirmed, and pushed further (own fresh computation, not
reused from any prior script).** Built an independent greedy-sequence
simulator (`/tmp/round-7/grf/sim.py`, `sim_resume.py` — exact
`sympy.primefactors`, minimal-antichain-frontier admissibility, resumable to
extend a run without recomputation) and a per-core antichain analyzer
(`/tmp/round-7/grf/analyze.py`, `analyze2.py`, `dcheck.py`). Simulated
`a_1=21528751` to `n=100000` (up from the outline-reviewer's `n=50000`).
Confirmed: `S=\{103,197\}`'s bundle `\{11,97\}` is **still present, still
undominated** in the class-`S` minimal antichain at `n=100000` (`|I_S|=503`
now, up from `252` at `n=50000`); `D_S\setminus P_1=\{2,3,7\}` unchanged.
So the naive `(GW)` with the pattern-matched `W(21528751)=\{2,3,7\}` remains
refuted at twice the previously-checked range — not a truncation artifact.

**2. New numerical finding: the tension is not confined to depth 2 — but
this does NOT, by itself, refute mere existence of *some* finite `W_d`
(important correction to the outline's framing, see point 3 for the real
kill).** Computed `D_S\setminus P_1` and the full per-core minimal antichain
for **every** proper core of `a_1=21528751` (`P_1=\{103,197,1061\}`) and
`a_1=4199` (`P_1=\{13,17,19\}`) at growing `n` (`21528751` to `n=100000`;
`4199` to `n=30000`, `5\times` the outline's data, to check stability):

- `a_1=21528751`, depth-1 core `S=\{1061\}` (**not** checked by the round-7
  cross-bucket-domination explorer's table, which only covered `\{103\}` and
  `\{197\}` for this `a_1`): `D_{\{1061\}}\setminus P_1=\varnothing` (no
  prime can *ever* be a sole companion of `\{1061\}` — confirmed,
  `|J_{\{1061\}}|=99875` at `n=100000`). The minimal antichain is
  `\{\{2,3,5,7,97\},\{2,3,7,11\}\}\cup\{1061\}` — **unchanged** between
  `n=50000` (`|I_S|=16`) and `n=100000` (`|I_S|=30`), i.e. stable under a
  near-doubling of the sample even though `I_S` itself nearly doubled. This
  companion structure needs `\{2,3,5,7,11,97\}`, strictly larger than
  `\{2,3,7\}` (the set that suffices for `\{103\}` and `\{197\}`) — but note
  `\{2,3,7\}\subsetneq\{2,3,5,7,11,97\}`, so this is a *superset* relation,
  not an incompatible clash; a single `W_1(21528751)=\{2,3,5,7,11,97\}`
  would cover **all three** depth-1 cores. **This is not yet a refutation of
  "some finite `W_1` exists"** — only of the *specific* small guessed set.
  (Honest caveat: the two `\{1061\}` bundles have size `4` and `5`, so the
  already-certified Permanent Pair Lemma, which only covers `|Q|=2`, does
  **not** apply to certify them permanent; only the weaker fact "no
  singleton dominator exists" — from `D_S\setminus P_1=\varnothing` plus
  Permanent-Inadmissibility — is rigorously established here. Whether these
  size-4/5 bundles are truly permanent, or could still be dominated by an
  intermediate-size sub-bundle not yet realized, is open; a "Permanent
  `k`-tuple Lemma" generalizing the Permanent Pair Lemma to `|Q|\ge3` is
  flagged but not attempted by any approach yet, including this one — not
  pursued further here since it does not bear on this file's own verdict.)
- `a_1=4199`: at `n=30000` (`5\times` the outline's `n=6000` base),
  depth-1 core `S=\{19\}`'s antichain is **stably** `\{\{2,3\}\}` (a single
  provably-permanent pair, via the already-certified Permanent Pair Lemma —
  `D_{\{19\}}\setminus P_1=\varnothing`, `2,3\notin\varnothing`, `J_{\{19\}}`
  has `24071` elements and growing), while `S=\{13\}` and `S=\{17\}` both
  provably need `83` as well (`S=\{13\}`: pairs `\{2,83\}` and `\{2,3\}`,
  both permanent by the same Lemma since `D_{\{13\}}\setminus
  P_1=\varnothing`; `S=\{17\}`: `\{2\}` realized as a legitimate sole
  companion — consistent with `D_{\{17\}}\setminus P_1=\{2\}` — plus a
  permanent pair `\{3,83\}`). Again, `\{2,3\}\subsetneq\{2,3,83\}`, so a
  single `W_1(4199)=\{2,3,83\}` would cover all three depth-1 cores — again
  *not* by itself a refutation of "some finite `W_1` exists," just evidence
  the "small universal set" intuition motivating this whole direction (the
  cross-bucket-domination explorer's "smallest primes not dividing `a_1`"
  pattern-match) was already too optimistic even before considering
  incompatible clashes.

**3. The decisive point: even if some repaired `W_d(a_1)` (or `W(a_1)`)
exists, proving it is provably no easier than proving `\Lambda_S` finite for
each proper core directly — so this whole approach is strictly dominated by
its two sibling approaches, which are already making direct progress on
exactly that statement.** For fixed `a_1`, `k:=|P_1|` is fixed, so the
number of proper cores `S⊊P_1` (`\le2^k-2`) and, for any fixed depth `d`, the
number of depth-`d` cores (`\binom{k}{d}`) are both fixed finite numbers —
not growing with `n` or with anything else. Hence:

`(GW)`: `\exists` finite `W(a_1)` s.t. `\forall` proper core `S`,
`\Lambda_S\subseteq W(a_1)` `\iff` `\forall` proper core `S`, `\Lambda_S` is
finite.

*Proof.* `(\Leftarrow)` If `\Lambda_S` is finite for each of the `\le2^k-2`
(fixed, finite-in-number) proper cores, then `W(a_1):=\bigcup_{S\text{
proper}}\Lambda_S` is a finite union of finite sets, hence finite, and
`\Lambda_S\subseteq W(a_1)` for every `S` trivially. `(\Rightarrow)` If
`(GW)` holds with some finite `W(a_1)`, then `\Lambda_S\subseteq W(a_1)` is a
subset of a finite set, hence finite, for every proper `S`. `\blacksquare`

The identical argument applies verbatim to `(GW-depth)` (restricting to the
fixed, finite set of depth-`d` cores) and to any `(GW-nested)` variant
defined by a rule over the fixed finite family of proper cores of a fixed
`a_1`: **any "one shared finite set works for a fixed finite family of
statements" hypothesis is logically equivalent to the conjunction of those
finitely many statements**, with zero reduction in content. This is not a
new trick invented here — it is *exactly* the reduction the already-
certified **Theorem CD** (`lemmas/theorem-CD-core-decomposition-and-lemma-
TC.md`) already performs one level up, unconditionally, since round 5:
`𝓥` finite `\iff` `𝓥_S` finite for each of the `\le2^k-2` proper cores `S`,
via the identical "finite union of finite sets" argument. `(GW)` merely
re-derives this same already-certified equivalence in a different notation
(companion-prime pools instead of value-sets), buying nothing new. The
premise motivating this whole approach — "replace `\le2^k-2` independent
local hitting-set questions with **one** global existential statement, a
different, sharper route to the destination" (Round 7 Outline, above) — is
therefore false: `(GW)` is not a different or sharper target, it is the
identical target in a different costume.

*Fair caveat, stated honestly.* This equivalence kills the claim that `(GW)`
is a logically easier *target*; it does not, strictly, rule out that
attempting a **uniform proof technique** across all cores at once could be
an easier proof-*strategy* even for a logically-equivalent target (e.g. one
symmetric density argument might be simpler to write than `\le2^k-2`
separate ad hoc ones). This round tested that possibility too: the Round 7
Outline's own Step 2 candidate mechanism ("small primes divide a much larger
density of integers... so a companion set built only from large primes
should be eventually dominated") was flagged in advance as having "the same
shape as the already-refuted Growth-Budget/Markov/Cauchy–Schwarz pointwise-
vs-cumulative attempts (rounds 3–6)." No new leverage for this mechanism was
found this round either (attempting it would require exactly the same
pointwise-vs-cumulative argument already refuted three times in `current.md`
for three different framings; the `S=\{19\}` vs `S=\{13\},\{17\}` example
above shows directly why: `D_{\{19\}}\setminus P_1=\varnothing` places *no*
a priori bound on which future primes could join a new permanent pair for
`\{19\}`, so bounding `\Lambda_{19}` requires exactly the same unresolved
local-hitting-set argument as bounding `\Lambda_{13}` or `\Lambda_{17}` —
uniformity buys no shortcut in practice, matching the logical-equivalence
finding). So even the soft "uniform strategy" fallback provides no
demonstrated advantage.

**4. Recommendation.** Mark this approach a clean, honest **dead-end**. Its
distinguishing premise (a genuinely different, more tractable global
reformulation) is refuted twice over — numerically (the specific candidate
`W` fails, confirmed independently to `n=100000`) and structurally (any
repair is logically equivalent to, and demonstrably no easier in practice
than, the per-core statement `persistent-backbone-monovariant` and `forced-
primes-well-ordering` are already directly and more productively attacking,
with real certified partial progress — Permanent Pair Lemma, Escape-
Confinement Lemma). No further round should reopen `(GW)`/`(GW-depth)`/
`(GW-nested)` without first refuting this equivalence argument, which none
of the numerics above come close to touching.

## Approaches tried
- **Hypothesis (GW)** (a single finite `W(a_1)`, independent of core and
  depth, bounding every proper core's companions) — **dead-end, refuted**.
  Counterexample (`a_1=21528751`, depth-2 core `\{103,197\}`, permanent
  bundle `\{11,97\}\not\subseteq\{2,3,7\}`) independently confirmed by the
  round-7 outline-reviewer and re-confirmed here at `n=100000` (twice the
  previously-checked range) — still present, still undominated.
- **Hypothesis (GW-depth)** (one finite `W_d(a_1)` per core-depth `d`) and
  **Hypothesis (GW-nested)** (`W` a function of a core's singleton
  "parents") — **dead-end, foreclosed structurally, not just numerically**.
  Proved (§3 above) that for any fixed `a_1`, both are logically equivalent
  to "`\Lambda_S` finite for every core `S` in the relevant fixed finite
  family" (a direct corollary of the same finite-union argument underlying
  the already-certified Theorem CD), so neither can be strictly easier to
  prove than the per-core statement the sibling approaches already attack
  directly. This forecloses the entire "global reformulation" program for
  this problem, not merely the specific patterns tried.
- **The "small universal recruiter set" intuition** (cross-bucket-domination
  explorer's empirical pattern, "smallest primes not dividing `a_1`") —
  **empirically weakened further**, independent of the equivalence argument:
  found two additional core-instances (`a_1=21528751,S=\{1061\}`;
  `a_1=4199,S=\{13\},\{17\}` vs `\{19\}`) where different cores of the
  *same depth* of the *same `a_1`* provably (via the certified Permanent
  Pair Lemma) need incompatible-sized companion structures, reinforcing that
  even a corrected, larger `W` would need to be found by essentially solving
  each core's `\Lambda_S`-finiteness first — there is no shortcut via
  pattern-matching a small shared set.
- **Step 2's density/uniformity mechanism** (attempt at a genuinely uniform
  proof technique, as a possible soft consolation even given the logical-
  equivalence kill) — **not pursued beyond the already-flagged risk**: this
  round found no new leverage distinguishing it from the already-refuted
  Growth-Budget/Markov/Cauchy–Schwarz pointwise-vs-cumulative mechanisms
  (rounds 3–6), and the concrete `S=\{19\}` example shows directly why no
  uniform shortcut is available (`D_{\{19\}}\setminus P_1=\varnothing`
  imposes no a priori bound on future permanent-pair primes).

## Current best
Nothing of positive value toward the theorem is established by this
approach's own distinguishing claim, and none is expected: `(GW)` itself is
refuted (numerically, independently re-confirmed at `n=100000`), and every
proposed repair (`GW-depth`, `GW-nested`) is proved (§3 above, a three-line
argument from the fixed finite cardinality of the proper-core family, the
same mechanism already underlying the certified Theorem CD) to be logically
equivalent to — hence no easier than — the exact per-core `\Lambda_S`-
finiteness statement the sibling approaches `persistent-backbone-monovariant`
and `forced-primes-well-ordering` are already directly attacking, with real
certified partial progress (Permanent Pair Lemma, Escape-Confinement Lemma).
This approach's reduction chain ("(GW) `\Rightarrow` whole problem", listed
in the Round 7 Outline above as "mostly citation") is therefore moot: there
is no route by which closing `(GW)` could be strictly easier than closing
the shared gap directly, and this approach contributes no new proof
technique beyond what the sibling approaches already have in hand.
Recommendation: treat this approach as closed/dead-end; do not re-open the
global-reformulation family without first refuting the logical-equivalence
argument in §3.

## Full proof
(Not present — Status is `unsolved`. This approach's own distinguishing
premise has been refuted, both numerically and structurally; see the "Round
7 Builder Update" above for the complete argument. No claim toward the main
theorem is made by this approach.)
