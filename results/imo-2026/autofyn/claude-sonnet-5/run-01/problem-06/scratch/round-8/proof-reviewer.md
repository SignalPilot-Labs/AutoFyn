# Round 8 proof-reviewer report — imo-2026-06

Reviewed three built approaches (all touching the shared FCBC/𝓥_S gap):
`sunflower-bundle-closure` (new), `persistent-backbone-monovariant`,
`forced-primes-well-ordering`. Independently re-derived every load-bearing
step by hand and independently re-simulated every numeric claim with a
fresh Python generator (not the builders' scripts), cross-validated against
brute-force gcd checking on 5 small `a_1` before trusting large-`N` runs.

## Independent verification method

Wrote `/tmp/gen.py` (efficient minimal-radical-antichain-based greedy
sequence generator, using `sympy.factorint` for exact factorization) and
`/tmp/brute.py` (naive `O(n^2)` all-pairs-gcd generator). Confirmed the two
agree exactly on `a_1∈{247,2747,91,375,221}` to `n=400`. Used the fast
generator for all further checks.

**Reproduced exactly, from scratch:**
- `max ω(a_n)` (`sunflower-bundle-closure`'s §5 numerics): `a_1=247`→`6` at
  `n=1039` (`N=3000`); `a_1=2747`→`6` at `n=1646` (`N=3000`);
  `a_1=21528751`→`7` at `n=872` (`N=1200`). Exact match on all three.
- `a_1=2747`, `S={67}` worked example (`persistent-backbone-monovariant`'s
  §"Worked example"): `a_2=2788` (rad `{2,17,41}`), `a_3=2814` (rad
  `{2,3,7,67}`), `a_4=2829` (rad `{3,23,41}`), `a_{10}=3157` (rad
  `{7,11,41}`) — exact match, confirming the claimed escape-chain witnesses
  and extracted primes `2,3,7`.
- `a_1=21528751`, `S={1061}` full 19-index table (`forced-primes-well-
  ordering`'s §H Step 5, the file's central numeric claim this round):
  generated the sequence to `n=60000` (fresh code, ~118s), independently
  found `|I_S|=19` with the identical 19 indices
  `{280,596,3741,7201,10658,14118,17577,21037,24495,27954,31413,34872,
  38332,41791,45250,48710,52169,55627,59086}`, every one of the 19 radicals
  cited (including both outliers `a_{280}={2,3,7,11,1061}` and
  `a_{596}={2,3,5,7,97,1061}`), the exact "extra prime" pattern (`q=5` for
  4 members, base value for 4 members, 9 distinct singleton `q`'s), and
  `S^+={2,3,7,1061}`. Zero discrepancies anywhere in this table.

No numeric discrepancy was found in any claim checked this round (a strong
result — every numerically-loaded claim across all three files that I had
time to re-derive matched exactly).

## sunflower-bundle-closure — verdict: APPROVE-quality progress, Status `partial` (CHANGES REQUESTED)

**This is the round's most consequential result.** Re-derived every step
of §0–§4c by hand, line by line, treating each cited "already-certified"
fact as a black box only after confirming its statement matches the actual
certified lemma file (checked `lemma-escape-confinement.md`,
`lemma-permanent-inadmissibility.md`, `lemma-ER-eventual-realization-
dichotomy.md`, `theorem-V-veto-finite-iff-MRS.md`,
`theorem-CD-core-decomposition-and-lemma-TC.md`,
`lemma-lambda-S-reduction-and-single-companion-finiteness.md`).

- **Lemma ERD-C (§1).** Mutual exclusion: both sub-cases (`i>j`, `i≤j`)
  correctly derive a contradiction from Permanent-Inadmissibility and Lemma
  P′ respectively. Exhaustiveness: the canonical test integer `T_C` is
  correctly shown to satisfy Lemma ER's hypothesis, giving `T_C=a_m`
  directly. No gap.
- **Lemma SR (§2).** Correct three-line argument from the No-Resurrection
  Lemma; correctly notes `(UB_S)` plays no role in this branch. No gap.
- **§3 (trivial finite-`I_S` case).** Correctly disposes of one of the
  round-8 outline's two flagged "open sub-gaps" (I_S finite/infinite
  handling) as an automatic case split, not a hypothesis. Verified.
- **§4a (Δ-system dichotomy).** I independently re-derived this classical
  fact from scratch (own induction, not reading the source's proof first)
  and it matches: base case `M=0` vacuous (distinct sets of size ≤0 force
  at most one member); inductive step's greedy-disjoint-then-pigeonhole
  construction is the standard argument, correctly handles the "process
  terminates" branch (maximal disjoint collection `U`, pigeonhole on `U`
  gives a common element, recurse with the bound decremented). The
  parenthetical remark handling the `M=1` vacuity subtlety is fussy but
  correct — I checked directly that distinct singletons are automatically
  pairwise disjoint, so the "terminates" branch never actually fires at
  `M=1`, exactly as the proof claims. No gap. No dependence on a finite
  ambient prime universe (checked explicitly, correctly).
- **§4b (applying the dichotomy).** Verified both branches (pairwise
  disjoint / sunflower with core `Y`) in full: the Case (a) pigeonhole
  injection into `comp(a_{j_3})` is correct; Case (b)'s two sub-cases
  (`κ'=S∪Y` realized vs. blocked) both correctly derive a contradiction —
  sub-case (b-i) via a fixed-finite-set argument from No-Resurrection,
  sub-case (b-ii) via a second application of Escape-Confinement to the
  *petals*, using `Y∩comp(a_{j_3}')=∅` correctly established first. I
  traced every set-membership claim (`S⊆P_1` disjointness from `comp(·)`,
  `Q_l∩comp(a_{j_3})≠∅` derivations) by hand; all correct.
- **§4c (assembly).** The claimed equivalence `(UB_S)` for all proper `S`
  `⟺ sup_{n∉I_{P_1}}ω(a_n)<∞` is correct (verified both directions
  algebraically).
- **§5 (honest report on `(UB_S)` itself).** Correctly diagnoses that the
  developed pigeonhole/Δ-system tools bound *count* of bounded-size
  objects, not *size* of individual objects — this is a real, useful
  negative finding, not hand-waving; I could not find a way around this
  limitation either in the time available.

**Verdict: this file's "dissolves both open sub-gaps" headline claim is
TRUE and independently confirmed** — a genuinely important result, since
both sibling approaches this round (`persistent-backbone-monovariant`,
`forced-primes-well-ordering`) got stuck exactly on the "core-avoiding
witness existence in general" sub-lemma that this mechanism sidesteps
entirely (see cross-approach synergy below). No circularity found anywhere
in the chain. `(UB_S)` itself is honestly reported as open, not solved —
correctly labeled `partial`, not `solved`. **CHANGES REQUESTED** (real,
substantial, gap-free advance; the sole remaining gap for the whole problem
is now precisely `(UB_S)`).

## persistent-backbone-monovariant — Status `partial` (CHANGES REQUESTED)

Verified the Realized–Blocked Dichotomy Lemma (RBD) — literally the same
theorem as `sunflower-bundle-closure`'s Lemma ERD-C, proven independently
via the identical mechanism (Lemma ER + Lemma P′ + Permanent-
Inadmissibility). Merged into one certified lemma file
(`lemmas/lemma-ERD-realized-blocked-dichotomy.md`) per this workspace's
standing convention for two-independent-proofs-of-the-same-fact.

Verified the Complement Witness Fact (correct, one line), the
Escape-Confinement Pairwise-Disjoint-Bundle-Count Corollary (correct,
identical mechanism to `sunflower-bundle-closure`'s §4b Case (a)), and the
Finite-Reachability Theorem — a genuine, correctly-proved finitely-branching
König's Lemma variant (I re-derived the "greedily extend along a
child with unboundedly-extending descendants" argument by hand; correct,
no gap) — and the Reachability Theorem for (SA)-bundles (verified the
inductive chain construction against the `a_1=2747,S={67},Q={2,3,7}` worked
example with my own fresh sequence generator: exact match on all four cited
witness indices `a_2,a_4,a_{10}` and the extracted primes `2,3,7` in order).

**Cross-approach synergy found (not noticed by either builder).** Combining
this file's own certified RBD Lemma with `sunflower-bundle-closure`'s Lemma
SR dissolves this file's own flagged "open gap (1)" (general
core-avoiding-witness existence): for any proper core `S`, either `S` is
realized (Lemma SR closes `𝓥_S` directly, no witness needed) or `S` is
blocked (RBD supplies the witness automatically). This file's remaining
open hypothesis is therefore exactly **NIBC alone**, narrower than the file
itself reports (it lists two open gaps). Recorded in `lemmas/lemma-SR-
self-realized-core-shortcut.md`'s synergy note and in `current.md`.

The file's own honest "Transient Bundles Are Invisible" finding (proved,
not just diagnosed: every transient bundle fails (SA) by definition of
being dominated) is correct and important — it shows this whole mechanism,
even with NIBC resolved, can never close `(UB_S)`/`Λ_S`-finiteness alone.

**Verdict: CHANGES REQUESTED** (real new certified content: RBD [merged],
Complement Witness Fact, Pairwise-Disjoint Corollary, Finite-Reachability
Theorem + Reachability Theorem for (SA)-bundles; one open gap dissolved by
synergy; honestly still `partial`, NIBC and the transient-bundle limitation
remain fully open).

## forced-primes-well-ordering — Status `partial` (CHANGES REQUESTED)

Verified the Freeze-Confinement Domination Lemma (§H Step 1): the
minimality argument (choosing `j^*∈T` minimizing radical size, showing
`j^*∈M_n^S`) is correct, standard, no gap. Verified the `S^+` Necessity +
Finiteness Lemma (§H Step 4): part (a) trivial, part (b) a correct one-line
application of the already-certified Generalized Lemma C to `I_S` (the
same mechanism already used for `D_S`, just applied to a different index
set) — correct, no gap.

Verified Step 2's honest self-correction (the outline's proposed
depth-bound formula does not follow from domination alone — the natural
derivation only gives a lower bound, not the claimed upper bound; I
attempted the derivation myself independently and hit the identical wall)
— a genuine, valuable correction, not a failure.

Verified the Vacuity Proposition and Intersection-Fragility Proposition
(§H Step 5): both are short, correct, elementary set-theory facts. Their
application to the `a_1=21528751,S={1061}` counterexample is fully
consistent with my own independent recomputation of the full `I_S`
table (see numerics above): `11∉S^+` because `a_{596}`'s radical
`{2,3,5,7,97,1061}` omits `11`, exactly matching the
Intersection-Fragility Proposition's prediction, and `{2,3}⊆S^+` so the
Vacuity Proposition correctly predicts `S^{++}_{\{2,3,1061\}}=S^+`
(no improvement) for that bucket.

**Verdict: CHANGES REQUESTED** (two new certified lemmas, one honest
self-correction, two new correct negative results ruling out an entire
family of candidate fixes; sufficiency gap for `S^+`/general `(MRS_S)`
remains fully open; does not by itself bound bundle size, so does not
close `(UB_S)` either).

## Cross-approach synergy check (explicit, per standing instruction)

Checked whether any combination of this round's new lemmas closes `(UB_S)`
or `Λ_S`-finiteness unconditionally. Found one real, actionable synergy
(RBD + Lemma SR dissolving `persistent-backbone-monovariant`'s witness-
existence gap, above) — recorded and used to sharpen that file's remaining
open hypothesis to NIBC alone. Found no combination that bounds bundle
*size* (what `(UB_S)` needs): `persistent-backbone-monovariant`'s
Escape-Confinement/Reachability machinery and `forced-primes-well-
ordering`'s `S^+`/`S^{++}` machinery both structurally bound *count* or
*necessary primes*, never *size* of an individual bundle — consistent with
`sunflower-bundle-closure`'s own honest §5 diagnosis of exactly this
limitation, independently confirmed by tracing all three mechanisms by
hand. **No combination closes `(UB_S)` or the whole problem this round.**

## Lemmas certified this round (7 new files, 46 total in `lemmas/`)

- `lemmas/lemma-ERD-realized-blocked-dichotomy.md` — merged (two
  independent proofs, `sunflower-bundle-closure`'s Lemma ERD-C and
  `persistent-backbone-monovariant`'s RBD Lemma).
- `lemmas/lemma-SR-self-realized-core-shortcut.md` (`sunflower-bundle-
  closure`), with the cross-approach synergy note.
- `lemmas/lemma-delta-system-dichotomy.md` (`sunflower-bundle-closure`) —
  general-purpose classical combinatorics, reusable outside this problem.
- `lemmas/theorem-UBS-sufficiency.md` (`sunflower-bundle-closure`) — the
  round's headline conditional theorem.
- `lemmas/lemma-freeze-confinement-domination-and-Splus.md`
  (`forced-primes-well-ordering`).
- `lemmas/lemma-vacuity-and-intersection-fragility.md`
  (`forced-primes-well-ordering`).
- `lemmas/lemma-finite-reachability-and-complement-witness.md`
  (`persistent-backbone-monovariant`).

All certified `solved`-quality for their unconditional parts; conditional
lemmas (Finite-Reachability Theorem, `theorem-UBS-sufficiency.md`) are
certified as valid *implications*, with their hypotheses (`NIBC`, `(UB_S)`)
explicitly and honestly still open.

## Verdicts summary

- `sunflower-bundle-closure` — Status `partial`. **Verdict: CHANGES
  REQUESTED.** (No RETHINK — this is real, substantial, gap-free progress;
  not `solved` because `(UB_S)` remains open.)
- `persistent-backbone-monovariant` — Status `partial`. **Verdict: CHANGES
  REQUESTED.**
- `forced-primes-well-ordering` — Status `partial`. **Verdict: CHANGES
  REQUESTED.**

None RETHINK. `results/imo-2026-06/current.md` updated with a Round 8
section (headline first, per convention); overall Status remains
`partial` — the whole problem now reduces to exactly one hypothesis,
`(UB_S)` (equivalently `sup_{n∉I_{P_1}}ω(a_n)<∞`), with a fully-verified,
gap-free conditional bridge from it to the complete theorem.

## Files touched

- `results/imo-2026-06/current.md` (Round 8 section added).
- `results/imo-2026-06/lemmas/lemma-ERD-realized-blocked-dichotomy.md` (new).
- `results/imo-2026-06/lemmas/lemma-SR-self-realized-core-shortcut.md` (new).
- `results/imo-2026-06/lemmas/lemma-delta-system-dichotomy.md` (new).
- `results/imo-2026-06/lemmas/theorem-UBS-sufficiency.md` (new).
- `results/imo-2026-06/lemmas/lemma-freeze-confinement-domination-and-Splus.md` (new).
- `results/imo-2026-06/lemmas/lemma-vacuity-and-intersection-fragility.md` (new).
- `results/imo-2026-06/lemmas/lemma-finite-reachability-and-complement-witness.md` (new).
- `mcp__approach-ranker__record_outcome` called for all 3 built slugs.
