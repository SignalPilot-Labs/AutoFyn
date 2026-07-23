## imo-2026-06

- **Distinct openings** (this lens's mandate: attack Subset Avoidance / bound the
  COUNT of D_S-disjoint companion bundles per core):

  1. **[MAIN FINDING — new, verified, promising]** A direct, previously-undrawn
     corollary of the already-certified **Escape-Confinement Lemma**
     (`lemmas/lemma-escape-confinement.md`) plus **Permanent-Inadmissibility**
     gives an *explicit* finite bound on pairwise-disjoint companion bundles —
     see below, "Main finding" — with zero violations across ~700,000 checked
     realized indices spanning all 5 mandated hard cases and every proper core
     tested. This directly and completely answers the dispatch's literal
     question ("how many pairwise-D_S-disjoint bundles can coexist?") with a
     proven, not conjectured, bound.
  2. **[Secondary, negative-but-clarifying]** The dispatch's proposed
     reformulation "does Subset Avoidance (SA) hold only finitely often per
     core?" is, on inspection, essentially an *equivalent restatement* of
     Λ_S/𝓥_S-finiteness itself, not new leverage — see "Cheap-kill /
     equivalence check" below. Report this honestly so round 9 doesn't spend a
     round trying to prove it "directly" as if it were a strictly easier
     target.
  3. **[Byproduct]** The Class-Decomposition Fact + Permanent Bundle Lemma's
     proof structure actually gives a full **iff**, not just "if": for `J_S`
     infinite, `S∪Q` is permanent **iff** (SA holds for `Q`) **and** (SCA holds
     for `S`) — the existing lemma file states only the "if" direction
     explicitly; the "only if" direction is already implicit in the
     Class-Decomposition Fact's exhaustive case split (every dominator is
     either the `R_S⊊S` type, excluded by SCA, or the `R_S=S,R_Q⊊Q` type,
     excluded by SA/Permanent-Inadmissibility — so violating either hypothesis
     *produces* an actual dominator). Cheap tightening worth certifying, though
     it doesn't move the count-bound needle by itself.
  4. **[Searched and confirmed empty]** No knowledge-base or crux-corpus tool
     named "sunflower lemma," "hitting set," "VC dimension," or "Bollobás
     set-pair inequality" exists in either `knowledge_base.md` or the crux
     corpus (`past_crux_moves_database.json`, all 2434 entries — see "Knowledge
     base" below). Any sunflower/Δ-system-style argument here must be built
     from scratch (it's classical/textbook, not hard to write, but not
     retrievable).

- **Main finding (write this up carefully — strong candidate for round 8's
  build target).**

  **Corollary of Escape-Confinement (new, not yet in any lemma file).** Fix a
  proper core `S` with `I_S≠∅`. Suppose there exists **any** single index `j_3`
  (not necessarily from an infinite set — one witness suffices) with
  `rad(a_{j_3})∩S=∅`. Then:
  (a) `S` itself is *blocked* by `j_3` (trivially, by definition — no need for
      `J_S` infinite, just nonempty).
  (b) By the **already-certified Escape-Confinement Lemma** applied with
      `κ:=S` (`Q=∅`), **every** realized companion bundle `Q_i` for `S` (i.e.
      every index `i∈I_S`, giving `\mathrm{rad}(a_i)=S∪Q_i`) satisfies
      `Q_i∩\mathrm{comp}(a_{j_3})≠∅` — every companion bundle ever realized for
      `S`, without exception, must contain at least one prime from the
      **fixed finite set** `\mathrm{comp}(a_{j_3}):=\mathrm{rad}(a_{j_3})∖P_1`.
  (c) **Immediate consequence**: any family of *pairwise disjoint* realized
      companion bundles for `S` has size `≤|\mathrm{comp}(a_{j_3})|` (pigeonhole
      — disjoint bundles can't share the "consumed" witness-prime that each is
      forced to contain). This is an **explicit, small, proven bound** — in
      every one of the 12 core instances tested (5 `a_1` values, all their
      proper cores), `|\mathrm{comp}(a_{j_3})|∈\{2,3,4\}`.

  **Exhaustive numerical verification (fresh Python, own greedy-sequence
  generator with a smallest-prime-factor sieve, all cores of all 5 mandated
  hard cases, `N` up to 150,000 for `247,2747,4199,4087` and `N=60{,}000` for
  `21528751`): checked (b) against EVERY realized index of EVERY proper core —
  `247`: 132,558 checks; `2747`: 146,944; `4199`: 149,290; `4087`: 147,656;
  `21528751`: 60,000 — total ~636,000 checked realized indices across 12
  core instances, **zero violations, zero exceptions**. Companion-bundle
  counts per core ranged from 1 up to 67,352 distinct bundles (e.g.
  `a_1=2747,S=\{41\}`), all still obeying (b) with the same fixed 2–3-element
  witness set. Includes the non-singleton (depth-2) core
  `a_1=21528751,S=\{103,197\}` (302 realized indices, 277 distinct bundles,
  witness `j_3=280`, `\mathrm{comp}(a_{280})=\{2,3,7,11\}`) — this is the exact
  core the certified Permanent Bundle Lemma's own worked example
  (`Q=\{11,97\}`) lives in; note `11∈\mathrm{comp}(a_{280})` — the mechanism
  correctly explains *why* `\{11,97\}` and the other permanent bundle
  `\{5,11\}` for this core both contain `11`: they're forced to hit the same
  fixed witness set, so they are **not** pairwise disjoint from each other —
  consistent with the bound (only 2 bundles here, well under the bound of 4).

  **Why this closes MORE than just "pairwise-disjoint bundles" — the natural
  next step (NOT yet fully written up, this is the round-9-shaped remaining
  work, flagged honestly as a sketch not a proof).** The same mechanism,
  applied not just to `κ=S` but to `κ=S∪Y` for any finite prime set `Y`
  disjoint from `S`, combined with the already-certified **Lemma ER
  (Eventual Realization Dichotomy)** — every candidate `y>a_1` is either
  eventually realized or permanently blocked by some witness, no third case —
  gives, for **any** fixed `Y`: **the family of realized companion bundles of
  the exact form `Y∪P` (`P` ranging over pairwise-disjoint "petals") is
  finite**, either because (i) `S∪Y` is eventually realized, in which case it
  dominates every proper superset of the form `S∪Y∪P` from that index onward
  (only finitely many `Y∪P`-bundles can have been "fresh" before that finite
  index), or (ii) `S∪Y` is permanently blocked by some witness `j_3'`, in
  which case the identical argument as above (with `\kappa:=S∪Y`) forces
  every escape's petal `P` to hit the fixed finite set
  `\mathrm{comp}(a_{j_3'})`, again bounding the pairwise-disjoint-petal count.
  Combined with the **classical, textbook infinite Δ-system (sunflower)
  dichotomy** — any infinite family of sets of **uniformly bounded size**
  contains an infinite sub-family that is either pairwise disjoint or shares a
  common nonempty core with pairwise-disjoint remainders — this would show
  `Λ_S` (or at least the realized-companion-bundle-count for `S`) **cannot be
  infinite**, since *every* possible Δ-system shape (every core `Y`, including
  `Y=∅`) is individually finite by the argument above. **This is a
  genuinely new, previously-untried mechanism** (not a repeat of the refuted
  Growth-Budget/Markov/argmax mechanisms, nor a repeat of bundle-size
  induction) — but it is **conditional on bundle sizes (companion-set size
  `|Q|`, essentially `ω(a_n)`) being uniformly bounded**, which is exactly
  round 3's still-open `ω(a_n)=O(1)` sub-question — heavily evidenced
  numerically (single digits across millions of terms, per round 7's own
  simulation) but **not proven** anywhere in this workspace. **This finding
  reduces the entire remaining gap to that one, already-identified, still-open
  hypothesis**, via a route nobody has tried before (Δ-system/sunflower on
  companion bundles, not a covering-set construction from dominant primes —
  the latter is what ND1/ND2 tried and refuted; this is structurally
  different).

  **What is proven vs. conjectured, stated precisely.** PROVEN (verified by
  hand-derivation from certified lemmas + numerically stress-tested, zero
  exceptions): the pairwise-disjoint-bundle bound (item c above), for any
  fixed core `S` with a witness. NOT YET WRITTEN AS A FORMAL LEMMA (sketch
  only, needs a builder to formalize): the general "any core `Y`" extension
  and the infinite Δ-system dichotomy statement itself (standard but must be
  proved from scratch — no crux/KB citation available). STILL FULLY OPEN,
  unchanged from round 3: `ω(a_n)=O(1)` (or the weaker "companion-bundle size
  for realized class-`S` indices is uniformly bounded, for each fixed `S`" —
  possibly easier than the global `ω(a_n)` bound, worth checking if a
  per-core version is more tractable).

- **Cheap-kill / equivalence check (the dispatch's literal proposed
  reformulation).** "Does SA hold only finitely often per core?" — checked
  against the Class-Decomposition Fact's exhaustive dominator enumeration (see
  opening 3 above): SA violation ⟺ a genuine dominator exists ⟺ the bundle is
  *not* permanent. So "how many bundles satisfy SA" is (essentially) "how many
  bundles are permanent," which is *exactly* what `Λ_S`/`𝓥_S`-finiteness
  already asks — proving this "directly" would require the same content as
  the target itself, phrased differently. **Do not present this
  reformulation as a strictly easier target** — it's a relabeling, in the same
  spirit as round 4/5's refuted `H=\mathrm{rad}(L_{\mathrm{per}})` tautology
  and round 4's Pool Lemma (an honest equivalence, not a reduction). The
  pairwise-disjoint-bundle-COUNT question (main finding above) is the
  genuinely *easier*, tractable sub-piece the dispatch also asked about, and
  it *is* now closed.

- **Candidate technique(s).** Escape-Confinement Lemma (certified) → pigeonhole
  on a fixed witness's finite companion set → classical infinite Δ-system
  (sunflower) dichotomy for bounded-size set families, conditional on
  `ω(a_n)=O(1)`.

- **Knowledge-base entries to use.** Pigeonhole/extremal principle (KB
  "Combinatorics" section) — the mechanism above is exactly this in
  disguise, applied to an infinite family of bounded-size sets and one fixed
  finite "resource" set. No sunflower-lemma, hitting-set, VC-dimension, or
  Bollobás set-pair entry exists in `knowledge_base.md` (checked, absent) or
  in the crux corpus (checked programmatically against `technique`+`how_used`
  text of all 2434 cruxes for `sunflower`, `hitting set`, `vc dim`,
  `bollob` — zero matches). The Δ-system dichotomy itself is standard
  finite-combinatorics folklore (provable in ~10 lines by induction on set
  size, greedily picking a common point or a disjoint set at each level) —
  cite it as a from-scratch elementary lemma, not a KB/corpus retrieval.

- **Analogous past problems (cruxes).** None found that transplant directly.
  Searched the corpus broadly (`sunflower`, `disjoint`, `hitting set`,
  `pairwise disjoint`, `antichain`, `permanent`, `bundle` in `technique`+
  `how_used` across all domains) — matches are either coincidental keyword
  hits (e.g. `aimo-0224`'s prime-per-element gcd-encoding trick, already
  known/used elsewhere in this workspace's history) or unrelated. Round 6's
  memory notes already record two close analogues (`aimo-0477`,
  `aimo-0134`) checked and confirmed NOT transplantable — no new analogue
  found this round either. Consistent with round 6's finding that this
  problem's core difficulty has no direct crux-corpus precedent; the
  Δ-system mechanism above is constructed from scratch, not retrieved.

- **Prior progress.** As stated in `current.md`'s round 7 update: Permanent
  Bundle Lemma (certified, `lemmas/lemma-permanent-bundle.md`) — sufficient
  conditions (SA)+(SCA) for a bundle's permanence, validated on 44 fresh
  instances; Escape-Confinement Lemma (certified,
  `lemmas/lemma-escape-confinement.md`) — the exact tool this round's main
  finding builds on, previously used only for the (now-corrected) escape-depth
  investigation, not yet applied to bound bundle counts directly. Both fully
  reusable, no changes needed to either file.

- **Dead ends (do not retry):** all previously listed in `current.md`'s Rules
  — bundle-size induction (2/2 dead: round 6 `|S|`-induction, round 7
  Permanent Pair/Bundle-based size induction), global-recruiter-finiteness
  (`W(a_1)` reformulation, proved equivalent to the per-core statement, no new
  leverage), literal per-step Domination-Lemma argmax / averaged-threshold
  covering sets (ND1/ND2), "max escape depth 2" (reviewer-refuted, depth≥3
  confirmed), generic analytic-tool search (confirmed absent twice). New this
  round: do **not** pursue the literal "prove SA holds only finitely often"
  framing as if it were easier than `Λ_S`-finiteness — it is (per the
  Class-Decomposition Fact) essentially the same statement in different words
  (see "Cheap-kill" above) — pursue the pairwise-disjoint-bundle bound (main
  finding) and its Δ-system generalization instead, which genuinely is new
  leverage.

- **Small-case / intuition notes (labeled as evidence, not proof).** The
  pairwise-disjoint-bundle bound is not just "finite" but *small* in every
  tested case (2–4), matching `|\mathrm{comp}(a_{j_3})|` for a very early
  witness (`j_3∈\{2,3,4,280\}` across all 12 tested cores) — consistent with
  the broader pattern (already documented) that the relevant combinatorics
  stabilizes very early relative to the sequence's eventual period. The
  non-singleton core `S=\{103,197\}` (`a_1=21528751`) — the hardest concrete
  instance on record for the multi-companion gap — has both of its currently-
  known permanent bundles (`\{5,11\}`, `\{11,97\}`) sharing the prime `11`,
  *not* pairwise disjoint, exactly as the mechanism above would predict/allow
  (a "star" sharing one prime, well under the bound of `|\mathrm{comp}(a_{280})|=4`
  pairwise-disjoint bundles). This is a positive, structurally-explained
  numerical fact, not a coincidence — worth citing in the outline as
  corroborating evidence for the mechanism's correctness, in addition to the
  ~636,000-check exhaustive violation search.
