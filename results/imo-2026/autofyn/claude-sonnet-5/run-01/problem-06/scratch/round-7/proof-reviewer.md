# Round 7 proof-review — IMO 2026 P6

## Scope and method

Independently re-derived and re-verified every new claim from this round's
three builds, with fresh Python (no builder script reused): a from-scratch
brute-force generator (`gen_brute.py`, checks `gcd` against every prior term
directly) and a from-scratch efficient generator (`gen_fast.py`, maintains
the minimal-radical antichain for O(small) admissibility checks, factoring
only accepted terms via `sympy.factorint`, cross-checked against manual
trial-division on at least one large value). Cross-validated the two
generators exactly on all five mandated `a_1` (`247,2747,4199,4087,21528751`)
at `N` up to 500 (200 for `21528751`) before trusting any large-`N` run.
Code retained at `/tmp/round-7/reviewer/`.

## 1. persistent-backbone-monovariant — VERDICT: CHANGES REQUESTED (Status `partial`, correctly self-assessed)

**Claims checked and confirmed correct, independently:**

- **Class-Decomposition Fact** (any dominator `R⊊S∪Q` of a bundle has
  `R_S:=R∩S≠∅`): re-derived by hand from Lemma P′; correct, three lines,
  no gap.
- **Permanent Pair Lemma**, corrected this round to add the Sub-Core
  Avoidance (SCA) case for `|S|≥2`. This is a genuine, real gap the builder
  found in its own round-7 outline's proof sketch (which only searched
  dominators within `I_S`) and fixed correctly. Independently re-derived the
  full case split (`R_S=S` vs. `R_S⊊S`) — exhaustive and correct.
  Independently confirmed the (SCA) witness proof for the one non-singleton
  instance on record (`a_1=21528751,S={103,197},Q={11,97}`): recomputed
  `rad(a_2)={2,41,103,2549}` and `rad(a_3)={2,3,7,197,1301}` by both
  `sympy.factorint` and manual trial division (exact match to the file's
  claim), and directly confirmed by exhaustive search through `n=100000`
  that none of the 8 candidate sub-core radicals (`{103},{103,11},
  {103,97},{103,11,97},{197},{197,11},{197,97},{197,11,97}`) is ever
  realized. (SCA) is correctly, rigorously proved for this instance, not
  merely sampled.
- **Permanent Bundle Lemma** (general `k`, with Subset Avoidance (SA) for
  `k≥3`): re-derived from scratch, correct. Independently confirmed all
  three named worked instances by direct computation: `a_1=2747,S={67},
  Q={2,3,7}` — `rad(a_2)={2,17,41}`, `rad(a_4)={3,23,41}`,
  `rad(a_{10})={7,11,41}` all confirmed disjoint from the claimed
  companion-pair complements, and `{2,3,7,67}` confirmed first realized at
  `a_3` and present in the antichain through `N=5{,}000{,}000$-scale`
  simulation (I ran to `N=1{,}000{,}000`, unchanged from `n=163` onward —
  see below); `a_1=21528751,S={103,197},Q={11,97}` — confirmed exactly as
  above; negative control `a_1=4199,S={19},Q={2,3,37}` — confirmed
  `{2,3,19}` is independently realized at `a_{11}` (violating (SA)) and
  `{2,3,19,37}` is correctly absent from the antichain at `N=500{,}000`.
  **Zero discrepancies found in any of the three worked instances.**
- **Deep count-bound stress test / global antichain freeze claim.**
  Independently re-ran (own generator, own code, cross-validated against
  brute force) the freeze computation on **all five** mandated hard cases
  (exceeding the "at least 2 of 5" instruction), pushed to
  `N=400{,}000$–$1{,}000{,}000`:

  | `a_1` | claimed freeze `n` | my confirmed freeze `n` | claimed final size | my confirmed final antichain |
  |---|---|---|---|---|
  | `247` | `7` | `7` (checked to `N=1{,}000{,}000`) | `7` | exact match, 7 elements |
  | `2747` | `163` | `163` (to `N=1{,}000{,}000`) | `5` | exact match, incl. `{2,3,7,67}` |
  | `4199` | `92` | `92` (to `N=500{,}000`) | `7` | exact match |
  | `4087` | `54` | `54` (to `N=500{,}000`) | `3` | exact match |
  | `21528751` | `44967` | `44967` (to `N=400{,}000`) | `9` | exact match, incl. `{11,97,103,197}` |

  **Every single freeze index and every element of every final antichain
  matches the file's claim exactly** — not just cardinality, literal set
  identity. This is a strong, independent confirmation of the round's
  central numerical claim. I also independently confirmed the specific
  by-core breakdowns cited in the sibling `global-recruiter-finiteness`
  file (e.g. `a_1=4199`: `S={19}→{2,3}`, `S={13}→{2,83},{2,3}`,
  `S={17}→{2},{3,83}`; `a_1=21528751,S={1061}→{2,3,7,11},{2,3,5,7,97}`) —
  all exact matches, and `|I_{\{103,197\}}|=252$ at `n=50000`, `=503` at
  `n=100000` — exact match.
- Lemma P′ itself spot-checked (no violations in 5000+ terms across 4
  cases) since everything above is built on it.

**Assessment.** This round's work is careful, honest, and — on every claim
I checked — correct. The self-reported gap (bundle-size induction
foreclosed a second, deeper way; the count-bound target remains open; "`J_S`
infinite" remains an unproved standing hypothesis) is accurately described,
not overclaimed. **No cross-approach synergy closes anything new this round**
(see §4 below). Status `partial` is correct. **Verdict: CHANGES REQUESTED.**

## 2. forced-primes-well-ordering — VERDICT: CHANGES REQUESTED, with an important correction to this round's central empirical claim

**The Escape-Confinement Lemma itself: verified correct, certified
(`lemmas/lemma-escape-confinement.md`, new file, written by me this round).**
Re-derived from scratch: a clean, three-line consequence of Lemma P′,
structurally identical in spirit to the Coarsening Lemma's proof. No gap.
Spot-checked three of the four populated `a_1=21528751,S={197}` escape
chains by direct computation: `a_{1291}=21710976={2,3,7,41,197}`,
`a_{5844}=22356348={2,3,7,193,197}`, `a_{7831}=22637664={2,3,7,19,197}` —
all exact matches to the file's claims.

**A genuine numerical error found in this round's central empirical claim
("real depth ≤2 in every instance tested," "no instance of depth ≥3 found
despite a deliberate, targeted search").** I extended the builder's own
search ranges modestly and found **two confirmed depth-3 counterexamples**,
both in buckets the builder explicitly classified as "unpopulated" (i.e.
depth `=∞`/undefined), each just past the builder's own tested cutoff:

1. **`a_1=2747, S={67}`, bucket `κ={17,23}` (bare value `{17,23,67}`).**
   Builder: "zero occupants, checked exhaustively through `n=6000`."
   I independently found, at `n=19617` (my own generator, cross-validated
   against brute force, and the value manually trial-divided):
   `a_{19617}=1{,}100{,}274=2·3·7·17·23·67`, radical
   `{2,3,7,17,23,67}⊋{17,23,67}` — a **populated bucket with escape depth
   3**, not unpopulated. This is the *only* occupant through `n=20000`
   (no depth-1 or depth-2 escape exists for this bucket in that range), so
   the corrected realized depth is exactly `3`.
2. **`a_1=21528751, S={197}`, bucket `κ={19,41}` (bare value
   `{19,41,197}`).** Builder: "zero occupants, checked exhaustively through
   `n=30000`." I independently found an occupant at `n=30017` — **17 steps
   past the builder's own cutoff** — `a_{30017}=25{,}781{,}784=
   2^3·3·7·19·41·197`, radical `{2,3,7,19,41,197}⊋{19,41,197}`, escape
   depth `3` (confirmed by manual trial-division factorization independent
   of `sympy`, matching exactly). A second, deeper occupant exists at
   `n=75501` (depth 4 relative to the bare value, though the *realized*
   depth per the file's own definition — `min` over realized supersets — is
   the first one found, depth 3).

**Consequence for this round's claims.** This directly refutes, as stated,
the headline finding "the maximum realized escape depth found is 2... no
instance of depth ≥3 was found despite a deliberate, targeted search" —
two depth-3 instances exist and are found by only a modest (3.3× and 6.5×
respectively, not orders-of-magnitude) extension of the builder's own
search range. It also weakens the "Recruiter-Alignment pattern"'s
disjunctive form ("`|κ∩W|=0⟹` unpopulated") — both counterexamples have
`κ∩W=∅` (`W={2,3,7}`) yet are populated, not unpopulated. **Interestingly,
the corrected data point is still numerically consistent with the
underlying linear relationship `d=3-|κ∩W|`** (both give `d=3-0=3`) — so the
proportional pattern itself is not refuted, only the builder's disjunctive
"zero-overlap ⟹ never populated" claim is. This is a real, useful
correction (a cleaner, uniform version of the pattern may still hold), not
merely a "gotcha" — but it must not be silently carried forward as "depth
≤2, verified." I did **not** exhaustively re-search the other 11 of the 13
originally-claimed buckets, nor the 6 additional smaller-`a_1` cores, at
extended range — only the two I checked (both from the two hardest `a_1`
values) turned up counterexamples on a modest range extension, so I flag
this as a scope-limited but reproducible finding, and recommend next
round's builder re-run the *entire* depth search at a systematically larger
`N` (e.g. `10×` the previous cutoff in each case) before citing any
"maximum observed depth" number again.

**This does not affect the certified Escape-Confinement Lemma itself**
(unconditional, general, still correct) nor the file's own honest §G Step 4
finding (naive branching does not visibly terminate; true depth-control
mechanism is cross-bucket domination, the same open gap). If anything, my
correction **reinforces** Step 4's conclusion: depth is not in fact capped
at a small constant across all tested instances, consistent with "no
uniform bound found" being the right honest assessment, and inconsistent
with any optimism that the true depth is small in general.

**Verdict: CHANGES REQUESTED.** Status stays `partial`. The certified
lemma is real progress; the round's specific depth-bound claim requires the
correction above, which I have written into `current.md` and the new
lemma file's scope note.

## 3. global-recruiter-finiteness — VERDICT: RETHINK (Status `unsolved`, correctly self-diagnosed as a dead end)

**The refutation of (GW) is confirmed correct and independently
re-derived.** `D_S∖P_1={2,3,7}$ for `a_1=21528751,S={103,197}` and the
permanent bundle `{11,97}` (via the persistent-backbone-monovariant's now
independently-verified Permanent Pair Lemma) lying outside `{2,3,7}` — both
confirmed above (§1). I independently pushed the check further than the
file's own `n=100000` claim, to `n=400000` (via the freeze-verification run
in §1): `{11,97,103,197}` remains in the antichain, undominated, throughout.

**The equivalence argument (§3 of the file) is logically airtight.**
Re-checked by hand: for a fixed `a_1`, the family of proper cores
`S⊊P_1` has fixed cardinality `≤2^k-2` (`k=|P_1|`). `(⇐)`: a finite union
of finitely many finite sets `Λ_S` is finite, giving `W:=⋃Λ_S`, trivially
satisfying `(GW)`. `(⇒)`: `Λ_S⊆W(a_1)` finite gives `Λ_S` finite as a
subset of a finite set. Both directions are valid, elementary, and require
no additional hypothesis. The identical argument applies to any
depth-restricted or nesting-restricted variant, since those are likewise
finite sub-families of the same fixed, finite index set. **This is a
correct, complete proof that (GW)/(GW-depth)/(GW-nested) are logically
equivalent to the exact per-core statement the sibling approaches already
attack directly** — I found no flaw in this reasoning, and it matches the
same mechanism already underlying the already-certified Theorem CD
(re-checked: Theorem CD's own "finite union of finite sets" step is the
identical argument one level up).

**Also independently re-verified the two "incompatible companion structure"
data points** used to further weaken the "small universal `W`" intuition:
`a_1=21528751,S={1061}` needs `{2,3,7,11,97}` (confirmed exactly, via my
own antichain computation at `n=100000`: the two `S={1061}`-restricted
antichain elements minus `S` are `{2,3,7,11}` and `{2,3,5,7,97}` — exact
match); `a_1=4199`'s `S={13},{17},{19}` needing `{2,83},{2,3}`;
`{2},{3,83}`; `{2,3}` respectively — all confirmed exactly against my own
independently-computed final (frozen) antichain for `a_1=4199`.

**Assessment.** The approach's own conclusion — that this is a clean,
principled dead end, not merely an unlucky guess — is correct and well
argued; no flaw found in either the refutation or the equivalence proof.
Per `CLAUDE.md`'s routing rule ("a slug whose core mechanism turns out
fundamentally unworkable gets RETHINK"), this approach's distinguishing
premise (a strictly easier global reformulation) is now proved impossible,
not merely difficult. **Verdict: RETHINK** — this specific approach should
not be revived without first refuting the equivalence argument in its own
§3 (which I could not fault). The file's own recommendation to close it is
correct and I am recording the outcome accordingly.

## 4. Cross-approach synergy check (explicit, per standing instruction)

Checked whether this round's three builds, combined, close
multi-companion-bundle finiteness, Hypothesis (MRS)/`𝓥`-finiteness, or the
whole problem. **They do not.** Specifically:

- `persistent-backbone-monovariant`'s Permanent Pair/Bundle Lemma and
  `forced-primes-well-ordering`'s Escape-Confinement Lemma are complementary
  descriptions of the *same* underlying difficulty (a permanently-realized
  configuration, once it exists, resists a size- or depth-based inductive
  reduction) — I checked concretely whether combining them on the shared
  `a_1=21528751` instance yields anything new: the Permanent Pair Lemma
  certifies `{11,97,103,197}` (core `{103,197}`) permanent; the
  Escape-Confinement Lemma's machinery is scoped to a *different* core
  (`{197}` alone) in the file's worked examples. Applying Escape-Confinement
  to the `{103,197}`-core escape structure directly would require first
  identifying disjoint-companion witnesses for that specific (depth-2) core
  — not attempted by either file this round — so there is no ready
  combination; this is a plausible direction for a future round, not a
  synergy realized this round.
- `global-recruiter-finiteness`'s equivalence proof formally confirms
  that no amount of "global" repackaging of the other two approaches'
  per-core results can substitute for closing them individually — it
  actively *rules out* one hoped-for shortcut (a shared finite `W`), which
  is useful negative information but not a source of positive synergy.
- The deep antichain-freeze numerics (both `persistent-backbone-
  monovariant`'s `N=400{,}000$–$1{,}000{,}000` run, independently confirmed
  by me above) remain the strongest empirical evidence for (MRS)/FCBC
  produced in this workspace's history, but — as in every prior round —
  **no analytic mechanism converting "unchanged over a large tested range"
  into "unchanged forever, for a general `a_1`" was found or combined from
  any pairing of this round's results.** The pointwise-vs-cumulative
  obstruction (flagged since round 3) persists unchanged.

**Conclusion: no cross-approach combination closes any part of the
remaining gap this round.** The population's shared residual gap is
unchanged in substance from round 6: finiteness of `Λ_S` (equivalently
`𝓥_S`) for each remaining proper core `S`, now further sharpened (permanent
bundles are a real, unavoidable phenomenon; escape depth is not capped at
a small constant, contrary to this round's initial claim) but not closed.

## 5. Lemma-file audit

All referenced lemma files exist and say what the approach files claim:
`lemmas/lemma-permanent-bundle.md` (verified correct, annotated with my
independent-verification note), `lemmas/lemma-permanent-inadmissibility.md`
(pre-existing, re-confirmed trivial and correct),
`lemmas/lemma-lambda-S-reduction-and-single-companion-finiteness.md`
(pre-existing, re-confirmed), `lemmas/lemma-companion-disjointness-
coarsening.md` (pre-existing, spot-checked against my own `a_1=2747,S={67}`
bucket computation — exact match), `lemmas/lemma-P-prime-pairwise-
intersecting.md` (pre-existing, foundational, spot-checked numerically).
**New this round:** `lemmas/lemma-escape-confinement.md` (written and
certified by me, since the source file only proposed it for certification
under "Promotable lemmas" without creating the standalone file).

## 6. Outcomes recorded

- `persistent-backbone-monovariant`: outcome `advanced` (two new certified
  lemmas, deepest verified numerics in the workspace's history, all
  independently confirmed with zero discrepancies).
- `forced-primes-well-ordering`: outcome `partial` (one new certified
  lemma, but this round's central empirical claim required a real,
  independently-found correction).
- `global-recruiter-finiteness`: outcome `dead-end` (approach's own
  premise proved impossible; correctly self-diagnosed, RETHINK).

## 7. current.md

Rewritten with a new "Round 7 update" section reflecting all of the above:
what is newly certified (Permanent Pair/Bundle Lemma, Escape-Confinement
Lemma), the corrected depth-bound finding, the confirmed-dead-end status of
the global-recruiter-finiteness reformulation family, and the precise
unchanged state of the sole remaining gap. Status stays `partial`. Problem
is **not solved**.
