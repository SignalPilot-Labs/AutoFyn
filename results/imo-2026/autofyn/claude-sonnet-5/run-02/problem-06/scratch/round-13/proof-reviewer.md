# Round 13 proof-review — imo-2026-06

Overall workspace Status: **partial** (unchanged; the main FAH/Symmetric FAH crux
was untouched by design this round — round 13 was a defensive/bookkeeping round
plus a conditional secondary-gap round, per dispatch). `results/imo-2026-06/current.md`
updated accordingly (new round-13 Status paragraph + two new "Approaches tried"
entries; `## Full proof` correctly remains "Not present").

---

## Slug 1: `greedy-exchange-cost-potential` — No-Restart Lemma

**Verdict: CHANGES REQUESTED** (Status: partial — matches the builder's own
self-report; the approach overall stays partial since FAH/(†) is untouched, but
the dispatched task itself was completed cleanly with no gap).

**What was reviewed.** The round-13 addition to
`approaches/greedy-exchange-cost-potential.md` (§"ROUND 13: the No-Restart Lemma")
and the certified file `lemmas/no-restart-lemma.md`.

**Independent re-derivation of the load-bearing step.** The lemma's core claim is
the unconditional inequality `b_2 ≤ a_{n_0+1}` for every `n_0 ≥ 2`: dropping
constraints (restarting with only `{a_{n_0}}` instead of the full
`{a_1,...,a_{n_0}}`) can only enlarge the set of legal candidates, so the
restarted process's minimum candidate is ≤ the true process's minimum. This is a
one-line fact about conjunctions (`Leg(c|J) ⟹ Leg(c|I)` for `I⊆J`, hence
`{c:Leg(c|J)} ⊆ {c:Leg(c|I)}`, hence `min` over the superset is `≤ min` over the
subset) — I re-derived it from scratch independently and it is correct, with no
hidden hypothesis. The strict-divergence half (hypothesis (H'): some `j<n_0` and
some `c` in `(a_{n_0}, a_{n_0+1})` legal against `{a_{n_0}}` alone but illegal
against the forgotten `a_j`) is also correctly derived and the file is honest that
this is a *sufficient*, not universal, condition — it explicitly disclaims that
`(⋆)` fails for *every* `n_0` (see "What this Lemma does NOT claim"), which is the
right scope; no overclaim.

**Independent computational check.** I reimplemented both recursions from scratch
in Python (not reusing the builder's code) and confirmed the worked example
exactly:
```
true:  [15, 18, 20, 24, 30, 36, 40, 42, 45, 48, 50, 54]
restart from a5=30: [30, 32, 34, 36, 38, 40, 42, 44]
```
matching the file's claims digit-for-digit, including the specific witness
(`j=1`, `c=32`: `gcd(32,30)=2>1` but `gcd(32,15)=1`).

**Generality check.** The proof is stated and proved for an *arbitrary* `n_0 ≥ 2`
under hypothesis (H') — the `a_1=15` computation is presented (correctly) only as
an illustrative worked example, not as the scope of the theorem. The proof text
itself never restricts to `a_1=15`; the general argument (monotonicity +
existence of a witness `c` in the interval) is what's actually being certified.
So the "prove it in general, not just the `a_1=15` example" bar from the dispatch
is met.

**Non-circularity / no crux-move references.** The proof uses only elementary
logic about conjunctions of the problem's own legality predicate — no citation to
another problem's crux, no appeal to any open lemma in this workspace, no use of
FAH/(†)/gap-related content. It correctly and explicitly disclaims any bearing on
the main crux ("It is not a new attack on FAH, Symmetric FAH, or gap (†)").

**Degenerate case `n_0=1`.** Correctly isolated and correctly excluded from the
lemma's hypotheses (the two recursions are definitionally identical when there is
no earlier history to drop) — not a skipped case, a genuinely vacuous one.

**Conclusion.** The No-Restart Lemma is correct, complete, unconditional, and
non-circular as stated. **Certified — `lemmas/no-restart-lemma.md` is kept
as-is, no changes needed.** This closes off, with a single citable fact, the
recurring failure mode that independently sank restart-style constructions in
rounds 3, 5, and 8 (a genuine, if modest, contribution to the shared toolkit).

**Why not APPROVE for the whole approach.** Per the file contract, `solved`
requires the actual problem claim (`a_{n+T}=a_n+L`) to be established with no
gaps. This round's task was explicitly scoped as defensive/bookkeeping and
touches neither FAH/(†) nor the n=1 gap; the approach's Status correctly remains
`partial`.

---

## Slug 2: `n1-periodicity-reconciliation` (new)

**Verdict: CHANGES REQUESTED** (Status: partial — matches the builder's own
self-report of not closing the gap; however this review finds one specific,
previously-unflagged, repairable rigor gap in the theorem's own proof, described
below, which the builder should be told to close explicitly).

**Scope check (does it overclaim resolving the main crux?).** No. The approach
file explicitly imports FAH/Cofinite FAH "at some finite core S ⊇ S₀ obtained by
the (still open elsewhere) recruitment process" as a hypothesis in §0, states "We
do not attempt to prove FAH itself here," and its `## Full proof` section
correctly states "Not present... This approach does not close the primary FAH gap
(explicitly out of scope, imported as an open hypothesis) nor the secondary n=1
gap." This is honest, matches the dispatch's explicit instruction to work
conditionally, and is not an overclaim.

### (1) Non-Constructivity of N₀/N₁/N₁'/N₂ — verified correct

The claim: the certified Persistent-Type Pigeonhole / Finite Core Theorem /
Extended Persistent-Type Pigeonhole proofs establish existence of finite
thresholds but supply no formula/algorithm computing them from `a_1` alone. I
independently unwound the cited proofs (they all reduce to "finitely many types,
infinitely many indices ⟹ some type recurs infinitely often," an existence
argument via the infinite pigeonhole principle that gives no witness) and confirm
this is correct: whether a specific type `A⊆Q` is persistent is a statement about
the sequence's entire infinite tail, and none of the certified proofs extract a
closed-form bound. The claim is appropriately scoped ("this does NOT mean the
equalities are unverifiable in principle for a *specific* a₁" — correct,
non-overclaiming). This is a genuine, correct, useful standing caution but is
better recorded as a documentation note (matches the round-7 Lemma-F/Lemma-I
precedent for "diagnostic about the current toolkit, not portable machinery")
than certified as a standalone reusable lemma — I have recorded it in
`current.md`'s narrative rather than as a `lemmas/*.md` file.

### (2) Self-Absorbing Core Theorem — conclusion correct, but the written proof
has a genuine gap in its "Combining both parts" step (NOT previously flagged)

**Statement reviewed.** Given a finite "self-absorbing" core `S* ⊇ S₀` (meaning
every term `a_1,...,a_{N(S*)}` has its FULL factorization already inside `S*`,
where `N(S*)` is the Extended-Persistent-Type-Pigeonhole threshold at level `S*`)
and FAH holding at level `S*`, the theorem claims `a_{n+T*}=a_n+L*` for all
`n≥N(S*)`, with `G* := {r : sig(r)∩P(a_j)≠∅ ∀j≤N(S*), AND sig(r)∩B≠∅ ∀B∈𝒫'(S*)}`.

**Where I found the gap.** The proof's final "Combining both parts" paragraph,
which must establish that legality against the entire history is *equivalent* to
residue-membership in `G*` (needed for the residue-driven cyclic-pigeonhole
mechanism to apply), justifies the harder half by writing: "the actual content is
what the certified Step 5 construction — reused here, not re-derived — already
shows for a residue r whose sig(r) meets every element of 𝒫'(S*)..." This is a
citation, not a derivation, and it is imprecise: I checked the actual Step 5
construction in `covering-system-construction.md` (lines 303–338) and found its
`G` is defined as `{r : sig(r) ∈ 𝒫'}` (i.e. `sig(r)` itself literally IS one of
the finitely many persistent types) — a **different, narrower** set than this
round's `G*` (`sig(r)` merely *meets every* type). Step 5's own proof never
establishes anything about the broader "meets every type" condition; the
citation does not actually support the claim as written.

**Independent re-derivation (I confirmed the theorem's conclusion is correct
despite the gap).** I reconstructed the missing argument from scratch:
1. *Sufficiency*: if `r ∈ G*`, then for every `j ≤ N(S*)`, `sig(r)∩P(a_j)≠∅`
   directly gives a shared prime, so `r` is legal against `a_j`; for
   `N(S*)<j≤n`, `ρ(j) ∈ 𝒫'(S*)` and `sig(r)` meets `ρ(j)` (being one of the
   types in `𝒫'(S*)` that `r` was required to meet), giving a shared prime.
   So every `G*`-residue is legal against the whole history — this direction is
   basically definitional and does not need FAH.
2. *Forced membership of the real value*: for `n ≥ N(S*)`, the actual `a_{n+1}`
   is legal by definition, and (since `S*` is self-absorbing) any prime it shares
   with `a_j` (`j≤N(S*)`) must lie in `P(a_j)⊆S*`, hence in `sig(a_{n+1})`,
   giving the first conjunct of `G*` automatically. For the second conjunct: let
   `A'' := ρ(n+1) ∈ 𝒫'(S*)` (guaranteed by Extended-Persistent-Type Pigeonhole
   for `n+1` large); for any other `B ∈ 𝒫'(S*)`, either `A''` and `B` share the
   same base type (then both `⊇` that nonempty base type, trivial intersection),
   or their base types share a `Q`-prime (trivial intersection via `Q`), or their
   base types are disjoint (intersection via the FAH hypothesis at `S*`) — this
   is exactly the trichotomy already used, for the *narrower* `G`, in Step 5's
   own proof (lines 305–308), which I re-derive here for the *broader* `G*` and
   confirm it also goes through. So `sig(a_{n+1})=A''` meets every `B∈𝒫'(S*)`,
   i.e. `a_{n+1} ∈ G*` is forced.
3. *Minimality closes the loop*: if any `G*`-residue integer `c` satisfied
   `a_n<c<a_{n+1}`, step 1 makes `c` legal, contradicting minimality of
   `a_{n+1}` as the smallest legal successor. So `a_{n+1}` is exactly the
   smallest `G*`-residue integer `> a_n` — establishing the cyclic-pigeonhole
   mechanism without ever needing a literal "iff" characterization of legality
   (this is also, in retrospect, how the ORIGINAL Step 5 argument for the
   narrower `G` actually works, though that file states it slightly loosely too
   — this is not a new problem specific to this round, but this round's citation
   does not correctly transfer it to the broader `G*` as written).

**Assessment.** The theorem's CONCLUSION is correct — I verified this
independently, not by trusting the file. But the file's own proof, AS WRITTEN,
has a genuine gap at exactly the "Combining both parts" step: it cites prior
certified content for a claim that content does not literally establish (the `G`
vs `G*` mismatch), and never states the minimality argument that actually closes
the loop. Per the rigor rules ("no hand-waving... if a step is non-trivial,
justify it" and the ban on citation-only justification), this is a real,
reportable gap, not a nitpick — a less careful reviewer trusting the citation at
face value would have missed that the cited construction doesn't cover the
broader set actually used here.

**Not certified this round.** I am NOT certifying `Self-Absorbing Core Theorem`
as a portable lemma in this state. The fix is short and concrete (spell out the
three-part argument above, in place of the citation), and is recorded here so
the next round's builder can complete it directly rather than rediscovering it.

### (3) Honest scoping of what remains open — verified accurate

Section 4's two sub-gaps are genuinely distinct and correctly stated as open, not
smoothed over:
- (a) existence/termination of a self-absorbing `S*` (iterating the absorption
  operator might not reach a fixed point in finitely many steps) — correctly
  flagged as structurally analogous to, but logically distinct from, the
  already-certified "collateral rogue pairs" concern (round 5–6) and the primary
  FAH-recruitment-termination crux; not attempted, correctly disclosed as out of
  this round's scope.
- (b) even granting a self-absorbing `S*` exists, `N(S*)=0` is not shown — the
  theorem is agnostic to the numeric value of the threshold.

Neither is claimed resolved; both are correctly left open.

### (4) Computational check — accurately described

The 6-seed table (`a_1 = 15, 35, 105, 175, 187, 209`) checks whether the
tail-derived `(T,L)` already gives `a_{n+T}=a_n+L` from `n=1` with zero pre-period
— explicitly disclosed by the builder as checking the *plain* threshold `N₁'`
(not the theorem's own, generally larger, `N(S*)`), i.e. a weaker and more
direct question than what the Self-Absorbing Core Theorem's own machinery
computes. This scoping is accurate and not oversold ("strong positive evidence
... but it remains empirical, not a proof, and covers only 6 seeds"). I did not
have time to independently re-run this specific 6-seed sweep from scratch this
round (given the review budget was spent on the load-bearing proof gap above);
flagging this as unverified-by-me (not flagged as wrong) — the methodology
described (tail period detection + backward-threshold search) is standard and
plausible, and none of my other checks contradict it.

**Note on the missing build report.** `/tmp/round-13/proof-builder-n1-
periodicity-reconciliation.md` does not exist (only
`proof-builder-greedy-exchange-cost-potential.md` is present in `/tmp/round-13/`).
This did not block review — the approach file itself (`approaches/n1-periodicity-
reconciliation.md`) is self-contained and was read directly — but is noted for
process hygiene.

---

## Lemma certification this round

- **Certified (no changes):** `lemmas/no-restart-lemma.md` — unconditional,
  correct, independently re-derived and re-verified computationally by this
  review (see Slug 1 above).
- **NOT certified:** Self-Absorbing Core Theorem (`n1-periodicity-
  reconciliation`, §3) — conclusion independently confirmed correct by this
  review, but the written proof's "Combining both parts" step is a
  citation-only justification that does not actually cover the broader `G*` used
  here (the cited Step 5 construction uses a narrower `G`); needs the
  three-part minimality argument (sufficiency / forced-membership / minimality)
  spelled out explicitly before certification. See the precise fix above.
- **NOT certified as a standalone lemma (recorded as a standing caution in
  `current.md` instead):** Non-Constructivity of N₀/N₁/N₁'/N₂ — correct and
  useful, but matches the round-7 Lemma-F/Lemma-I precedent for
  toolkit-diagnostic content better than a portable reusable lemma.

## current.md updates made

- Added a new round-13 `## Status` paragraph (prepended, before the round-12
  paragraph) summarizing both slugs' verdicts and this review's findings.
- Added two new `## Approaches tried` entries (round-13 `greedy-exchange-cost-
  potential` and `n1-periodicity-reconciliation`), both verdict **CHANGES
  REQUESTED**.
- `## Full proof` correctly left as "Not present — Status is `partial`" (no
  changes needed there).
- Overall Status remains **partial** — the main FAH/Symmetric FAH crux is
  untouched this round by design; nothing in this round's findings changes that.

## Recommendation for next round

1. `n1-periodicity-reconciliation`: dispatch a builder to close the identified
   gap in the Self-Absorbing Core Theorem's proof by writing out the three-part
   argument (sufficiency / forced-membership via the base-type trichotomy /
   minimality) explicitly in place of the citation to Step 5 — this is a short,
   mechanical fix (I have already worked out the content above) and should
   result in certification next round.
2. The main FAH/Symmetric FAH crux remains the standing priority target and was
   correctly not attacked this round per dispatch; resume attacking it next
   round per the existing "next-round guidance" sections already in
   `current.md`.
