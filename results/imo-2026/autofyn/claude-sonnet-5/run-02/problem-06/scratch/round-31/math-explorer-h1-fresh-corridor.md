## imo-2026-06

- **Distinct openings (new framings for H1/FAH, both genuinely untried per a full-text
  search of current.md — no hit for "Ramsey", "confluence", "ultrafilter",
  "sunflower", "Erdos-Rado" anywhere in the 3900-line history)**:

  **Opening A — Canonical Ramsey Theorem (Erdős–Rado) on an "unbounded-color"
  pair-coloring, attacking H1 without first fixing a finite core.** Every one of
  the ~32 dead mechanisms (persistent-type pigeonhole, Finite Core Theorem,
  Bounded Witness Lemma, bipartite-network, residue-vector, introduction-order,
  witness-index/depth-bound, etc.) all share one structural move: FIRST fix a
  finite prime alphabet (Q, then S, then S₀, then S*), THEN pigeonhole the
  (finitely many) types over it. The Canonical Ramsey Theorem (Erdős–Rado, 1950)
  is a genuinely different tool because it needs no prior bound on the number of
  colors: for ANY coloring c:[N]^2 -> C (C possibly infinite) there is an
  infinite M subset of N on which c restricted to pairs from M is one of exactly
  4 canonical patterns (constant; depends only on min(i,j); depends only on
  max(i,j); or injective/"rainbow"). Idea: colour pairs {i,j} (i<j) of term-
  indices by c(i,j) := the least prime dividing gcd(a_i,a_j) (well-defined,
  nonempty by the certified Free Facts lemma, `free-facts-gcd.md`) — a coloring
  defined with NO reference to any fixed finite core, so the theorem's power
  (handling unboundedly many colors) is in principle exercised before any
  S₀-fixing move. This reaches for H1 from the outside, rather than routing
  around the same wall (recruitment termination) one step later.

  **Opening B — Sunflower/Δ-system lemma on the family of extended-persistent
  type-sets 𝒫' ⊆ 2^{S₀}, to find a common substructure across ALL rogue pairs
  simultaneously rather than pairwise.** The certified Canonical-Refinement
  Lemma (`lemmas/canonical-refinement-lemma.md`) closes gap (†) pairwise
  whenever at least one of the two types is its own base type's canonical
  refinement, and leaves open exactly the "rogue pairs" (neither side
  canonical). Every attempt so far (round 3's minimal-counterexample
  well-ordering, round 29-30's invariant searches) has tried to attack a
  single rogue pair or a single global invariant. The Erdős–Ko–Rado / sunflower
  toolkit instead asks: does the FAMILY {A' : A' in 𝒫'} (or the family of
  "extra-prime" sets {F_B : B in 𝒫}) contain a sunflower (Δ-system) — a
  subfamily sharing a common core C with pairwise-disjoint petals — whenever
  |𝒫'| is large enough (Erdős–Ko–Rado / Erdős–Szemerédi–Alon-type sunflower
  bounds, quantitative in terms of |𝒫'| and the max set size)? If so, the
  common core C might serve as a replacement "universal linking set" that the
  one-witness-per-type construction in the Finite Core Theorem does not
  provide, potentially giving simultaneous (not just pairwise) intersection —
  which is exactly what (†)/V=∅ needs. This is combinatorial extremal-set-theory
  machinery, structurally unlike every graph/pigeonhole/monovariant mechanism
  tried to date.

- **Candidate technique(s):** Canonical Ramsey Theorem (Erdős–Rado); Sunflower
  Lemma / Δ-systems (Erdős–Ko–Rado family); both from the "extremal set theory"
  and "Ramsey theory" corners of the KB/corpus that have not been invoked here.

- **Cheap-kill candidates / disambiguation performed:**

  1. **Opening A, checked computationally (not just structurally).** I
     simulated `a_1 = 175` (the workspace's own standing rogue-pair witness for
     gap (†)) to 400 terms and computed `c(i,j) := min(P(a_i) ∩ P(a_j))` for
     all 4950 pairs `i<j` in the first 100 terms. Result: **only 5 distinct
     colors ever occur** among 4950 pairs (empirically consistent with the
     certified Free Facts + Bounded Witness Lemma: witnessing primes are
     already drawn from a small finite pool once persistence sets in). This
     means the "unbounded color set" feature that gives the Canonical Ramsey
     Theorem its extra power over ordinary finite pigeonhole is **never
     actually exercised** on this natural coloring — the theorem degenerates
     to plain finite pigeonhole, i.e. it risks reproducing exactly the
     content already in `finite-core-theorem.md` / `bounded-witness-lemma.md`
     with no new leverage. **This is a genuine, checked, negative finding for
     the naive instantiation of Opening A** (not a structural guess) — it
     should not be re-proposed in this exact form. A less naive version would
     need to colour pairs of *recruitment rounds* (not term-indices) by which
     rogue-pair triggered them, where the color set is the (a priori
     unbounded) sequence of recruited primes q_1, q_2, ... — that variant is
     NOT ruled out by this check and remains open; flagging it, not
     recommending it outright.
  2. **Opening B, sanity-checked structurally, not computationally (time did
     not permit a full sunflower-bound computation).** The sunflower lemma
     only bites once |𝒫'| exceeds a bound depending on the max type-set size
     (roughly `r!·(s-1)^r` for sets of size ≤ r with s petals wanted) — for
     the workspace's small test seeds (`a_1=175`, `4807`, `11305`) |𝒫'| is
     likely too small (a handful of types) for this to give anything beyond
     what's already known. The idea would only have force in the fully
     general (`a_1` with many prime factors / large |Q|) regime the H1
     statement actually needs — i.e. it is at best an asymptotic-in-|Q| tool,
     not something a small hard-coded seed can confirm or refute quickly.
     This is an honest scope caveat, not a disambiguation kill.

- **Knowledge-base entries to use:** `knowledge_base.md`'s "Pigeonhole /
  extremal principle" entry (already cited by `generalized-bounded-witness-lemma.md`)
  is the closest existing KB tool; neither Ramsey theory nor sunflower/Δ-system
  results appear to be named KB entries — if the outliner pursues either
  opening, the corresponding theorem (Erdős–Rado canonical Ramsey; sunflower
  lemma) would need to be stated and proved/cited from scratch as an imported
  external result, not merely referenced.

- **Analogous past problems (cruxes):** Searched `combinatorics /
  processes-and-algorithms` (33 problems) and scanned technique/how_used text
  for absorption-, closure-, and termination-of-greedy-process patterns. The
  closest by subject (bipartite closure toward a complete graph, `aimo-1000`)
  is **already cited and killed** in this workspace (`bipartite-network-invariant-fah`,
  round 29, RETHINK — collapses into either the already-known-insufficient
  Generalized Bounded Witness Lemma or the already-open H2). Two more distant
  candidates surfaced but are not genuinely analogous enough to recommend
  as a crux transplant: `aimo-1025` (lower-bounding the initial edge count
  needed for a "friendship needs ≥2 common friends" closure process to reach
  the complete graph) uses a *canonical greedy run + clique-cover bookkeeping*
  to get an extremal LOWER bound, not a termination proof, and its goal
  (minimum starting size) has no analogue in H1 (which needs an unconditional
  upper/termination statement for every `a_1`, not an extremal count).
  `aimo-0916` (stabilizing chain of images of a self-map on a *fixed finite*
  set, then taking a power that acts as identity on the stable core) is
  structurally different because the recruitment process's ambient set
  (S_0, S_1, ...) is not a priori bounded — this is precisely H2's open
  content, so the crux's key hypothesis (finiteness of the underlying set the
  self-map acts on) is exactly what's missing here. **Verdict: no genuinely
  analogous crux found in the corpus for either Opening A or Opening B** — this
  should be stated honestly to the outliner rather than forcing a weak match.

- **Prior progress:** Unchanged from round 30's `current.md`: 11 certified
  `a_1`-subfamily theorems (`2|a_1`, `a_1=p^k`, `a1-3q/3q^2/3q^3/3aq`,
  `a1-5q/7q/11q/13q/17q/19q`); Master Conditional Theorem reduces the fully
  general problem to H1 (FAH at the terminal self-absorbing core) + H2
  (absorption-chain termination); the concrete open target is gap (†): the
  set V of "rogue pairs" (A', B') with neither side its base type's canonical
  refinement is empty at every recruitment stage. `a_1=175` is the standing
  minimal witness that V ≠ ∅ at the zero-round stage (still open whether the
  process that follows ever re-closes).

- **Dead ends (do not retry, per current.md's graveyard — verified, not just
  copied):** bipartite-network-invariant-fah (collapses into Generalized
  Bounded Witness Lemma / open H2); introduction-order permutation invariant
  and residue-vector-mod-core-prime invariant (both independently
  re-confirmed dead — the residues hit *every* class, giving zero
  discriminating power); orbit-merging-additive-offset; reversible-transition-map;
  scalar-well-ordering-lock-in; witness-index/depth-bound descents (proved
  the target, even if achieved, would not close (†) as framed); sieve/density
  arguments (Density-Argument Vacuity Corollary, Selection-Rule Class-Blindness);
  subword-complexity/Morse-Hedlund; triangle-consistency-pigeonhole family
  (Same-Type Triangle Vacuity); integer-monovariant/difference-identity family
  (5 candidates, all restate certified content or are class-blind); CRT/
  competitor-construction/covering-glue family (Minimal-Modulus Generalization
  closes the whole family as dead); Seed-Coupling Lemma (falsified by
  computation); minimal-counterexample well-ordering on V directly (round 3 —
  the natural size measure |A'|+|B'| is non-decreasing under recruitment, and
  the recruitment corollary's pigeonhole only certifies the recruited prime's
  recurrence on the reconciling side, not the fixed witness side).

- **Small-case / intuition notes (labeled conjecture/empirical only):**
  - The 5-color empirical finding on `a_1=175`'s first-100-term gcd-witness
    coloring (Opening A's disambiguation, above) is a *computed fact about
    this one seed*, not a proof that the same collapse happens for every
    `a_1` — but it is suggestive: it is consistent with the certified claim
    that, once persistence sets in, gcd-witnesses are drawn from an
    already-bounded pool (`finite-core-theorem.md`), which is exactly the
    reason ordinary pigeonhole already "sees" what Canonical Ramsey would see
    on this coloring — i.e. no informational gain from the fancier theorem
    *on this particular coloring choice*.
  - No new counterexample to FAH/H1 was sought or found this round (that is
    `fah-counterexample-hunt`'s live lane, not this report's); this round's
    round-30 finding that 2 of its 6 claimed "singleton near-misses" for
    `a_1=7402395` were factually wrong (they recur) is noted here only as
    context — it does not bear on Openings A/B.
  - **Honest overall assessment:** after a real search (corpus + full-text
    scan of current.md + one computational disambiguation), I did not find a
    framing that clearly escapes the "collapses into already-certified
    pigeonhole/bounded-witness content" trap that has killed the last several
    rounds' invariant attempts. Opening A's most natural instantiation is
    empirically dead-on-arrival (5-color collapse); its "colour recruitment
    rounds, not term-indices" variant and Opening B (sunflower on 𝒫') are the
    two least-explored, most structurally distinct candidates I can surface,
    but both need real work before they can be judged live or dead — neither
    is a repeat of any of the ~32 named-dead mechanisms, but neither is yet
    disambiguated as certainly new leverage either. This is itself useful
    negative information for a 26th consecutive plateau round.
