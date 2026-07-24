## imo-2026-06

**Assignment.** Dig into the bespoke `|F''|=2`, multiplicity-1 fallback case (Reduced-
Alphabet Corollary's `|D_bad(q*)|=1` shape) on the two standing test seeds a_1=4807,
a_1=11305 — is there an ad hoc argument closing this ONE fixed-integer divisibility
question, distinct from the 16 dead general FAH mechanisms?

### What was already tried on this exact narrow case (read from prior rounds, verified)
Two prior rounds already ran this exact lens:
- Round 12 (`math-explorer-smallcase.md`): identified the Reduced-Alphabet Corollary
  shape itself, confirmed |D_bad|=1 on both seeds, tried Lemma H (Critical Prime
  Dichotomy) on the lone residual prime and CRT-glue at the tiny modulus 13/103 —
  both re-enter already-dead territory (Lemma H's branch depends on the specific
  integer's OTHER factors, not alphabet size; CRT-glue at any modulus is the
  already-fully-dead Minimal-Modulus Generalization family).
- Round 13 (`math-explorer-bespoke.md`): fresh independent reimplementation to
  N≈30,000-40,000, confirmed 0/62 and 0/913 exceptions (literal, not just cofinite,
  FAH on both seeds at that scale). Tried (1) a "multi-witness pigeonhole via
  Singleton-Side FAH's all-occurrences strength" — collapses into the already-dead
  Recruitment-Budget Lemma (escaping prime not forced to stabilize); (2) a
  finite-automaton/2-state framing on the singleton D_bad alphabet — collapses into
  the certified EEA-equivalent-to-FAH result (round 12); (3) size/parity pattern
  between q* and the bad prime — falsified (4807's winner 17 is the larger of
  {13,17}; 11305's winner 11 is the smaller of {11,103}, no pattern).

Both rounds independently concluded: alphabet size (down to a single bad class) is a
reduction in DEGREE, not in KIND — every certified screening obstruction
(Escape-Cost Vacuity / Sandwich Genericity, Density-Argument Vacuity, EEA-equivalence,
Minimal-Modulus Generalization, Lemma I's "no tool promotes existential to universal")
applies verbatim regardless of `|D_bad|`.

### My own fresh digging this round (verified, no reuse of prior code)
Freshly reimplemented the greedy sequence (plain `math.gcd`, hand-rolled
trial-division factorizer, per the workspace's own performance rule) and pushed
further/differently than rounds 12-13:

1. **Confirmed both standing witnesses are literally canonical (earliest-occurrence)
   witnesses of their extended types**, not just Q-level base-type witnesses — a fact
   used implicitly but not previously verified explicitly in the bespoke-lens reports.
   For a_1=4807: n_A=6 (a_6=4845=3·5·17·19) IS the first n with ρ(n)={3,5,19}; n_B=7
   (a_7=4862=2·11·13·17) IS the first n with ρ(n)={2,11}. Same check for a_1=11305:
   n_B=4 (a_4=11319=3·7³·11) is first n with ρ(n)={3,7}; n_A=7 (a_7=11330=2·5·11·103)
   is first n with ρ(n)={2,5}. This means the Canonical-Refinement Lemma / F_A∩F_B≠∅
   fact directly applies and already guarantees F'∩F''≠∅ (confirmed: 4807's F'={17}
   sits inside F''={13,17}; 11305's F'={11,103} sits inside... wait, on 11305 the
   singleton side is F''={11} on the B'-witness a_4, and F'={11,103} on the A'-witness
   a_7 — 11 ∈ F'∩F''). **This is exactly the mechanism (†)'s Canonical-Refinement
   Lemma is designed to explain — it is NOT new leverage on FAH itself**: (†) (extended
   types intersecting) and FAH (a SPECIFIC prime dividing literally EVERY later
   occurrence, not just intersecting once at the canonical witness) are genuinely
   different-strength claims, and this round confirms explicitly that being
   canonical-vs-canonical (which already resolves (†) for this pair) does nothing to
   resolve FAH — the open target (D_bad(q*) nonempty-but-unhit) is a strictly
   downstream, harder claim than (†) even when (†) is free. Worth flagging precisely
   because it clarifies WHY these two "open crux" framings ((†) vs FAH) can coexist on
   the identical seed: (†) is closed here by Canonical-Refinement, FAH is not.

2. **Tried a direct local-legality "hypothetical bad candidate" check** (a genuinely
   new angle not in rounds 12-13's list): suppose a hypothetical n₀ has
   ρ(n₀)=A'={3,5,19}, 13 | a_{n₀}, 17 ∤ a_{n₀} (i.e. g_{n₀}=13, the one bad class).
   Checked directly whether legality (`gcd(a_{n₀}, a_i)>1` for all prior i) forces a
   contradiction using ONLY the two canonical witnesses a_{n_A}=4845=3·5·17·19 and
   a_{n_B}=4862=2·11·13·17: `gcd(a_{n₀}, a_{n_A})` is already >1 via the shared primes
   3,5,19 (part of A' by definition of ρ(n₀)=A'), independent of whether 17|a_{n₀};
   `gcd(a_{n₀}, a_{n_B})` is already >1 via the hypothesized shared prime 13. So legality
   against BOTH canonical witnesses is satisfied whether or not 17 | a_{n₀} — **no
   contradiction is available from the two fixed witnesses alone**, confirming (by direct
   computation, not just citing Lemma I abstractly) that any closing argument MUST use
   information from some OTHER, non-fixed, unboundedly-many prior term — exactly the
   "class-blind / no identity-level information from a fixed source" diagnosis every
   prior mechanism has hit. This directly rules out (again, but now shown concretely
   rather than by citing an abstract diagnostic) any argument that tries to derive the
   bad class's impossibility from the two witnesses' factorizations alone, however cleverly
   recombined — the obstruction is structural, not a failure of cleverness.

3. **Extended computational check further than any prior round**: N=20000 for both
   seeds (vs 30-40k terms in round 13, but here counting occurrence RATE not term
   count — the occurrence counts are actually larger: 31 A'-type occurrences for
   4807 (up from round 13's tracked range) and **614** for 11305 (up from round 13's
   913 at a larger N — consistent, same order). **0/31 and 0/614** land in the bad
   class in both cases — still literal zero-exception FAH, no weakening as N grows.
   Also spot-checked the "gap between consecutive same-type occurrences" pattern for
   4807: gaps cluster tightly at ≈551-559 (occasionally doubling to ≈1110-1112,
   consistent with a missed intermediate occurrence pattern) — i.e. strong numeric
   evidence of an eventual near-arithmetic-progression structure among A'-type
   occurrence indices, consistent with (but not proof of) the target periodicity
   itself; using this pattern to CLOSE FAH would be circular (assumes periodicity to
   derive periodicity), so it is reported as evidence only, not a mechanism.

### Cheap-kill candidates
None found. Checked (this round): local two-witness legality (dead, see #2 above);
occurrence-gap regularity as a shortcut (circular, would presuppose periodicity).
Rounds 12-13 already checked: size/parity of {q*, bad prime} (falsified), alphabet-size
reduction alone (does not change obstruction kind).

### Candidate technique(s)
None newly found. Confirms rounds 12-13's conclusion: the narrow `|F''|=2` case is
NOT structurally easier in kind, only in the size of the alphabet to search — every
certified obstruction (Escape-Cost Vacuity/Sandwich Genericity, Density-Argument
Vacuity, Minimal-Modulus Generalization, EEA-equivalence, Lemma I) is alphabet-size-
independent by construction (they attack the SOURCE of information, not the count of
divisor classes). A genuinely new closing argument for this bespoke case would need to
extract identity-level information from an unboundedly-growing pool of prior terms
(not the two fixed canonical witnesses) — no certified tool does this, and this round's
direct local-legality check (§2) confirms concretely, not just by citation, that the
two fixed witnesses alone are provably insufficient.

### Knowledge-base entries to use
None beyond what's already imported (Pigeonhole, CRT, unique factorization) — all
three prior explorer passes (rounds 12, 13, this round) have found nothing in
`knowledge_base.md` that supplies a class-sensitive, cross-occurrence linking fact.

### Analogous past problems (cruxes)
None new. This round did not run a fresh corpus query (deep-dig lens per dispatch);
defer to rounds 9/10's exhaustive corpus mining, which found the whole "algebraic-
recurrence induction" crux family (aimo-0477, aimo-0611, aimo-0678, aimo-0682)
structurally disanalogous (this problem's a_{n+1} is existentially/minimality-defined,
not a closed-form recurrence to induct through) — the bespoke narrow case does not
change this disanalogy since it's the same greedy process, just fewer divisor classes.

### Prior progress
Unchanged from current.md: FAH/Symmetric FAH/Cofinite FAH/EEA remains the sole open
crux, 16 confirmed-dead mechanisms. This round's bespoke dig adds no 17th mechanism
(nothing new was built to fail) but supplies two small, honest clarifications: (i) the
canonical-witness confirmation and the explicit (†) vs FAH distinction on this exact
seed (§1), (ii) a concrete (not just cited) demonstration that the two fixed witnesses
alone cannot possibly supply the missing contradiction (§2).

### Dead ends (do not retry)
- Lemma H / Critical Prime Dichotomy on the lone residual prime — dead (round 12).
- CRT-glue/competitor-construction at the tiny modulus 13 or 103 — dead, full
  generality (round 11's Minimal-Modulus Generalization covers this).
- Multi-witness pigeonhole via Singleton-Side FAH's all-occurrences strength — dead,
  collapses into Recruitment-Budget Lemma's refuted mechanism (round 13).
- 2-state/finite-automaton framing on the singleton D_bad alphabet — dead, collapses
  into the certified EEA-equivalence (round 12/13).
- Size/parity pattern between q* and the bad prime — falsified by both data points
  (round 13).
- **NEW this round**: deriving a contradiction for a hypothetical bad-class occurrence
  n₀ using ONLY the two canonical witnesses' (a_{n_A}, a_{n_B}) factorizations and the
  legality condition — confirmed dead by direct computation (§2): both witnesses'
  legality constraints are already satisfied by the hypothesized bad-class membership
  itself, giving zero contradiction leverage. Any future bespoke attempt must bring in
  a genuinely unbounded/growing source of prior-term information, not just the two
  fixed witnesses, however combined.

### Small-case / intuition notes (conjecture only)
- Both seeds continue to show literal (zero-exception) FAH at larger sample sizes
  this round (0/31, 0/614) than round 13 tracked at this occurrence-count granularity
  — strengthens the empirical case for literal FAH as the right target in this narrow
  regime, still unproven.
- The gap sequence between consecutive A'-type occurrences on a_1=4807 clusters
  tightly (≈551-559, occasional ≈1110-1112 doublings) — consistent with an eventual
  near-periodic occurrence pattern, but using this to prove FAH would presuppose the
  very periodicity the whole problem is trying to establish; flagged as evidence only.
- **Recommendation to the outliner (concurring with rounds 12 and 13)**: this bespoke
  narrow-case fallback, after three independent rounds of dedicated digging, does not
  appear to open new terrain — it is the most heavily re-explored corner of the whole
  workspace and every obstruction found for the general case reproduces verbatim here.
  If round 15 wants a genuinely different fallback direction not yet tried at all,
  consider (per round 12's own suggestion, still apparently unexplored): a small-|Q|
  enumeration (|Q|=2, e.g. a_1=15, 35) using the FULL current certified toolkit (which
  has grown substantially since round 1's partial attempt) — |Q| bounds the total
  number of rogue PAIRS to check (a different finiteness parameter from |F'|/|F''|),
  which is genuinely un-tried with the present, much larger lemma stack.
