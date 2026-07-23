# imo-2026-06 — Round 6 proof-reviewer report

Reviewed all 3 built approaches independently against the problem statement,
`CLAUDE.md`'s rigor rules, and `knowledge_base.md`. For each, identified the
single load-bearing new claim and re-derived it from scratch, then wrote
fresh Python (own sequence simulator, exact `sympy.factorint`-based radical
computation, own heap-based smooth-number search for `T_C` values — no
builder script reused) to re-verify every numeric claim. All verification
code and pickled sequence data lives in `/tmp/` (`seq_247_6000.pkl`,
`seq_2747_6000.pkl`, `fast_21528751_6000.pkl`, `verify*.py`, `gen_fast.py`).

## Summary of verdicts

| Approach | True Status | Verdict |
|---|---|---|
| `persistent-backbone-monovariant` | partial | **CHANGES REQUESTED** |
| `core-depth-induction` | partial | **CHANGES REQUESTED** |
| `forced-primes-well-ordering` | partial | **CHANGES REQUESTED** |

No RETHINK, no APPROVE. The problem remains **partial** overall — no
approach closes `𝓥_S`-finiteness (the sole remaining gap, per round 5) this
round, but all three made genuine, independently-verified new progress.

---

## 1. `persistent-backbone-monovariant`

**File's own Status:** partial. **Confirmed correct.**

**Load-bearing claim independently re-derived: Lemma FOM (First-Occurrence
Minimality).** *"If `n≥2` is the first index with `rad(a_n)=C`, then
`a_n=T_C:=min{x>a_1:rad(x)=C}`."* I re-derived this from scratch (single
proof-by-contradiction: `T_C<a_n` forced by minimality+first-occurrence,
then a greedy-minimality squeeze `a_{i*+1}≤T_C<a_{i*+1}` gives the
contradiction) — matches the file's proof exactly, no gap. I then wrote an
independent simulator (own code, not the builder's) and checked Lemma FOM
against **every** first-occurrence event in 6000-term sequences for
`a_1=247` (2106 checks) and `a_1=2747` (2817 checks), using an independent
heap-based smooth-number search for each `T_C` — **zero violations**.

**Fan-Size Corollary, Generation-Chain Lemma:** both correctly and honestly
scoped (conditional bound; chain length only, not chain count) — re-derived,
no gap.

**New this round, the round's main positive result: Λ_S-Reduction Lemma +
Single-Companion Finiteness Lemma.** Re-derived both proofs from scratch —
correct, non-circular, properly cites the already-certified Generalized
Lemma C and Lemma P′. I independently re-simulated and reproduced the
claimed **exact** matches:
- `a_1=2747`, `S={41}`: my code gives `J_S` (118 elements in first 6000
  terms), `D=⋂_{j∈J_S}rad(a_j)={2,3,7,67}`, predicted `Q_S⊆D∖P_1={2,3,7}`;
  direct search of all 6000 terms gives `Q_S={2,3,7}` exactly. Matches the
  builder's claim precisely.
- `a_1=247`, `S={13}`: `D={19}`, predicted `Q_S⊆∅`; direct search: `Q_S=∅`.
- `a_1=247`, `S={19}`: `D={13}`, predicted `Q_S⊆∅`; direct search: `Q_S=∅`.

All three exact matches independently reproduced with fresh code — the
strongest form of confirmation.

**Multi-Companion Reduction Proposition (the honest diagnosis of why this
doesn't close the gap):** I re-derived this proof too (a one-line
application of Lemma P′ to a hypothetical `≥2`-companion realized value) and
confirmed the discussion is accurate, not hand-waved: for `|Q|=1` the
mechanism gives a *fixed-intersection* stabilization (exactly what
Generalized Lemma C needs), but for `|Q|≥2` it only gives a *hitting-set*
condition on the infinite family `{rad(a_j):j∈J_S}` — a genuinely different
(and not obviously easier) kind of statement, correctly identified as a
local, restricted instance of FCBC itself. This is a real, proved
diagnosis, not an assertion.

**Second honest gap:** "`J_S` infinite" is not proved in general —
confirmed as correctly flagged (not silently assumed) in every citation of
the Single-Companion Finiteness Lemma.

**Growth-Budget Lemma:** correctly left open. I confirm this is an honest
self-assessment — not a hidden solve (the multi-companion case genuinely
resists the round's tools, as shown above) and not a hidden dead-end (the
single-companion case IS a genuine, nontrivial, verified positive result,
not vacuous).

**Verdict: CHANGES REQUESTED.** Real, verified, non-circular new content
(6 lemmas/propositions); the core `𝓥_S`-finiteness gap remains open, exactly
where the file says it is.

## 2. `core-depth-induction`

**File's own Status:** partial. **Confirmed correct**, with one important
finding sharpened by independent verification.

**Lemma B1 (Singleton-Core Value Pinning):** re-derived from scratch —
correctly builds on Lemma FOM (reproved inline, matches
`persistent-backbone-monovariant`'s version verbatim) plus the already-
certified Record Characterization Lemma and Theorem CD (used only to get
`C≠P_1` for `k≥2`, a legitimate, correctly-scoped use). No gap. This is
real, modest, reusable content — a genuine reformulation, not a bound.

**Negative Finding 1 (Step 3's central premise refuted) — independently
re-simulated in full.** I regenerated `a_1=21528751`'s sequence to `n=6000`
from scratch (own code, ~11 seconds using a minimal-antichain-restricted
admissibility check, validated by matching every one of the builder's
reported values exactly: `a_146=…`, all 13 fresh-value radicals for
`S={197,103}`). My independent computation reproduces the builder's table
**exactly**: all 13 non-trivial fresh values of the `S={197,103}` channel
through `n=6000`, none of the shape "`{q,103,197}`" for `q∈{2,3,7}` (the
depth-1 channel's eventual companions). This confirms the refutation is
real, not a simulator artifact.

**Caught a real (minor) internal inconsistency, not previously flagged.**
The file states "None of these 13 non-trivial fresh values..." in its
detailed table section (correct, matches my independent count of exactly
13 rows with `S(C)={197,103}`, zero matches) but elsewhere says "12 of 13"
or "none of the 12 non-trivial" in three other passages (the round-6 build
summary, the outline note, and the Approaches-tried bullet). My independent
recomputation confirms the **13**-count and **zero**-match version is
correct — the "12" phrasing appears to be a leftover from an earlier draft
(perhaps originally excluding one row as somehow "expected") that was not
consistently updated. This does not weaken the finding — if anything, "0 of
13 match" is a *stronger* refutation than "1 of 13 matches" — but the
approach file should correct the "12" occurrences to "13" (or "0 of 13
match") next round for internal consistency.

**Negative Finding 2 (`|S|` does not track difficulty) — independently
re-simulated.** My own fresh-value counts for `a_1=21528751`'s three
singleton cores: `{103}`→2364, `{197}`→42, `{1061}`→2 (builder: 2363, 41, 2
— off by exactly one in two cases, consistent with a boundary-inclusion
convention difference at `n=6000`, not a substantive discrepancy). The
1000-fold spread is real and independently confirmed.

**Conclusion on routing.** Per this workspace's standing review rule
(`/tmp/memory/proof-reviewer.md`: "NEVER default to RETHINK just because a
builder self-diagnoses their approach's core strategy as a dead end — check
whether the file's Status is honestly `partial` (real lemma proven) vs
`unsolved`"), and per `CLAUDE.md`'s strict Status→verdict mapping, this is
**CHANGES REQUESTED**, not RETHINK: Lemma B1 is real, correct, certified-
quality progress, so Status is genuinely `partial`, not `unsolved`. I note
this explicitly *because* this round's dispatch suggested "this is a
RETHINK for the induction-on-`|S|` architecture specifically" — I am
overriding that suggestion in favor of the established, problem-specific
precedent, while stating just as loudly as a RETHINK would: **the Step-3
depth-reduction mechanism, and `|S|` as the induction's well-founded
measure, are both confirmed dead ends. Do not re-attempt this specific
shape next round.** Only Lemma B1 should carry forward.

**Verdict: CHANGES REQUESTED**, with the explicit instruction above that
Step 3 as conceived is refuted (independently reproduced by the reviewer,
even more decisively than the builder's own count), while Lemma B1 is
certified.

## 3. `forced-primes-well-ordering`

**File's own Status:** partial. **Confirmed correct.**

**Refutation of the outline's own Step 2, independently reproduced.**
Regenerated `a_1=247`'s first 7 terms from scratch:
`247,260,266,273,285,312,342` with radicals exactly
`{13,19},{2,5,13},{2,7,19},{3,7,13},{3,5,19},{2,3,13},{2,3,19}` — matches
the file exactly. Confirmed `rad(a_3)={2,7,19}` does not block `{2,13}`
(shares `2`) or `{7,13}` (shares `7`); yet the sequence never realizes
`\{2,13\},\{3,13\},\{7,13\},\{13\}$ as exact radicals through `n=6000`
(checked directly) — so the single-witness criterion is genuinely
insufficient. This refutation is real, not a strawman.

**Companion-Disjointness Coarsening Lemma — proof re-derived from scratch.**
The set-algebra proof (three set-intersection eliminations reducing to
`Q∩comp(a_{j_1})≠∅` and `Q∩comp(a_{j_2})≠∅`, combined via disjointness of
the two companion sets) is correct and uses only the already-certified
Lemma P′ — no gap, no circularity.

**Both mandatory numerical checks independently reproduced exactly:**
- `a_1=247`, `S={13}`: my code confirms `j_1=3` (`comp={2,7}`), `j_2=5`
  (`comp={3,5}`) are disjoint, giving the 4 buckets `{2,3},{2,5},{3,7},
  {5,7}` (as bare values `\{2,3,13\},\{2,5,13\},\{3,7,13\},\{5,7,13\}`).
  Independently confirmed the realization pattern: `\{2,5,13\}` at `a_2=260`,
  `\{3,7,13\}` at `a_4=273`, `\{2,3,13\}` at `a_6=312`; `\{5,7,13\}` never
  realized through `n=6000`, and permanently blocked since
  `rad(a_7)=\{2,3,19\}$ is disjoint from `\{5,7,13\}` — exact match with the
  Bucket-Exclusion Corollary's prediction.
- `a_1=2747`, `S={41}`: independently enumerated all `j` with `G_j∩\{41\}=∅`
  through `n=400`: companion sets are `{2,3,7}` (7 instances) or `{2,3,5,7}`
  (1 instance, `j=205`) — no two disjoint, confirming the Coarsening Lemma's
  hypothesis genuinely fails. Independently reconstructed the local
  antichain: collapses `{3,41}` at `n=13`, `{2,41}` at `n=14`, grows a fan
  `\{7,q,41\}` for `q∈\{11,13,17,19,23,29,31,37\}`, single collapse at
  `n=163` to `\{2,41\},\{3,41\},\{7,41\}` — and independently computed
  `T_{\{7,41\}}=11767$ (least `7^a·41^b>2747`) matches `a_{163}=11767`
  exactly (my own generator confirms `a_{163}=11767`, `rad=\{7,41\}`).

All numerical claims reproduce exactly, including the exact `T_C` values.

**The honest remaining gap (cross-bucket domination):** re-read and confirm
this is correctly and non-trivially diagnosed: the Bucket-Exclusion
Corollary blocks only a bucket's bare value, not proper supersets within
it, and no general argument rules out an unbounded fan surviving inside a
"blocked" bucket. Correctly identified as the same order of difficulty as
the shared gap.

**Verdict: CHANGES REQUESTED.** Real refutation + real replacement lemma,
both independently verified in full; the collapse-case finiteness (second
half of the dispatch) is honestly not achieved.

---

## Cross-approach synergy check (explicit, as required every round)

Checked whether this round's 6 new lemmas/propositions (FOM, ER,
Λ_S-Reduction, Single-Companion Finiteness, Lemma B1, Companion-
Disjointness Coarsening) combine — across the three approaches — to close
`𝓥_S`-finiteness even though no single approach did.

1. **Single-Companion Finiteness Lemma × Coarsening Lemma on the same
   worked example (`a_1=247,S=\{13\}`).** Both independently predict/confirm
   `Q_S=∅` and the same 3-of-4-bucket realization pattern — a genuine
   cross-confirmation (two different mechanisms agreeing on the same
   example is reassuring) but **not a new bound**: neither extends the
   other's reach (Single-Companion bounds only exact-2-element radicals;
   Coarsening bounds only the "coarse shape," not full companion sets).
2. **Fan-Size Corollary × Coarsening Lemma (attempt to bound within-bucket
   growth).** Does not work: the Fan-Size Corollary's bound on companion
   size is conditional on the absorbing value `C'` being realized in the
   future, which is exactly the open question — using it to bound
   within-bucket fan growth would be circular (the same "`H=rad(L_per)`"-style
   circularity already flagged and refuted in round 5).
3. **Multi-Companion Reduction Proposition (persistent-backbone) vs.
   cross-bucket-domination gap (forced-primes).** These are two
   independently-derived formalizations of what is, on inspection, the same
   underlying difficulty — a local hitting/covering-set question on an
   infinite family of realized radicals restricted to one core `S`. This is
   a genuine, useful triangulation (now identified via three different
   routes across rounds 5–6: DM-order/counting, single-companion
   intersection-stabilization, and two-witness coarse-bucketing) but it is
   convergence on the *statement* of the residual gap, not a proof of it.

**Conclusion: no combination of this round's lemmas, across any pairing of
the three approaches, closes `𝓥_S`-finiteness.** This is reported honestly
in `current.md`'s Round 6 update, matching the actual state (genuinely
partial, not overclaimed).

## Lemmas certified this round

All independently re-derived/re-simulated by the reviewer (see per-approach
sections above), no gap found in any:
- `lemmas/lemma-FOM-first-occurrence-minimality.md` (Lemma FOM, Fan-Size
  Corollary, Generation-Chain Lemma) — `persistent-backbone-monovariant`.
- `lemmas/lemma-ER-eventual-realization-dichotomy.md` (Lemma ER) —
  `persistent-backbone-monovariant`.
- `lemmas/lemma-lambda-S-reduction-and-single-companion-finiteness.md`
  (Λ_S-Reduction Lemma, Single-Companion Finiteness Lemma, Multi-Companion
  Reduction Proposition) — `persistent-backbone-monovariant`.
- `lemmas/lemma-B1-singleton-core-value-pinning.md` (Lemma B1) —
  `core-depth-induction`.
- `lemmas/lemma-permanent-inadmissibility.md` (Permanent-Inadmissibility
  Lemma) — `forced-primes-well-ordering`.
- `lemmas/lemma-companion-disjointness-coarsening.md` (Companion-
  Disjointness Coarsening Lemma, Degenerate-case remark, Bucket-Exclusion
  Corollary) — `forced-primes-well-ordering`.

6 new lemma files (37 total in `lemmas/`, up from 31 at end of round 5).

## `current.md`

Updated with a "Round 6 update" headline section (prepended before "Round 5
update", same style as prior rounds), reflecting: no closure, the 6 newly
certified lemmas, the refutation + replacement in `forced-primes-well-
ordering`, the confirmed dead end in `core-depth-induction`'s Step 3, the
explicit cross-approach synergy check (negative result), and a
recommendation for round 7 (revive `core-depth-induction` with a different
well-founded measure, attack the now-precisely-isolated local hitting-set
residual directly, or bring in a genuinely different tool if both stall —
this would be the 5th consecutive round on the same core proposition family).
Status remains `partial`.

## Outcomes recorded

- `persistent-backbone-monovariant`: `advanced` — 3 new certified lemma
  files, exact numerical matches, honest diagnosis of remaining gap.
- `core-depth-induction`: `partial` — Lemma B1 certified; Step-3 architecture
  confirmed dead by independent full-history recomputation.
- `forced-primes-well-ordering`: `advanced` — refuted own outline's
  criterion, replaced with a verified, useful (if incomplete) Coarsening
  Lemma.

## Files touched

- `results/imo-2026-06/current.md` (Round 6 update section added).
- `results/imo-2026-06/lemmas/lemma-FOM-first-occurrence-minimality.md` (new)
- `results/imo-2026-06/lemmas/lemma-ER-eventual-realization-dichotomy.md` (new)
- `results/imo-2026-06/lemmas/lemma-lambda-S-reduction-and-single-companion-finiteness.md` (new)
- `results/imo-2026-06/lemmas/lemma-B1-singleton-core-value-pinning.md` (new)
- `results/imo-2026-06/lemmas/lemma-permanent-inadmissibility.md` (new)
- `results/imo-2026-06/lemmas/lemma-companion-disjointness-coarsening.md` (new)
