## imo-2026-06

**Lens: fresh whole-problem framing, ignoring "persistent type"/FAH machinery entirely.**

- Distinct openings (genuinely different top-level targets, not variants of the
  type-reconciliation chain):

  1. **Subword-complexity / Morse–Hedlund reformulation (untried anywhere in the
     workspace — not mentioned in `current.md` or any approach file).** The gap
     sequence `g_n := a_{n+1}-a_n` lives in a FINITE alphabet (Bounded Gap Lemma:
     `1 ≤ g_n ≤ a_1`, already certified). The Morse–Hedlund theorem (combinatorics
     on words) states: an infinite sequence over a finite alphabet is eventually
     periodic **iff** its factor-complexity function `p(k)` (number of distinct
     length-`k` contiguous windows) is bounded independent of `k`, equivalently
     `p(k) < k+1` for some `k` (Morse–Hedlund's exact numeric threshold) or more
     robustly just "does not grow without bound." Since `a_{n+T}=a_n+L` for all
     `n≥N` is EXACTLY "the gap sequence is eventually periodic," this is a full
     reformulation of the problem's actual claim, not a weaker corollary — proving
     bounded subword complexity of `(g_n)` is logically EQUIVALENT to proving the
     goal, so it does not evade the underlying difficulty. What it DOES offer is a
     genuinely different *proof technique* family never attempted here:
     de Bruijn-graph / "special factor" counting arguments, or an amortized
     potential bounding how many NEW length-`k` windows can appear per unit
     length of the sequence, using the already-certified finite alphabet of
     extended-persistent types (`Extended Persistent-Type Pigeonhole`, item 9 in
     Current Best) as the source of "boundedness," rather than trying to pin down
     one absorbing prime per rogue pair. This could sidestep the specific FAH
     formulation (which is *sufficient but perhaps not necessary* for periodicity)
     — i.e. it is conceivable complexity boundedness holds even in scenarios where
     the residual rogue set `V` (Round 6 framing) never literally empties, as long
     as the *ambiguity* it introduces is itself eventually periodic/bounded. I
     ran a quick numeric complexity check (below) that is consistent with, but
     of course does not prove, bounded complexity.

  2. **A genuinely different induction target than the refuted `seed-coupling-induction`.**
     That approach's literal claim (a term-by-term type-correspondence between the
     `ω(a_1)=k` sequence and the `ω(a_1)=k-1` "prime-stripped" sequence) is
     confirmed DEAD (see Dead ends below) — but induction on `ω(a_1)` as a
     *coarser* top-level strategy was only tested via that one specific literal
     correspondence. An unexplored variant: induct not on a term-by-term
     correspondence but on a **quantitative bound that only needs to transfer in
     aggregate** — e.g., "if every seed with `ω(a_1)=k-1` has eventual period
     `T'≤f(k-1)`, then every seed with `ω(a_1)=k` has eventual period
     `T≤f(k)`" via a purely existential compactness argument (not requiring the
     visible-skeleton correspondence to match position-by-position or even have
     matching asymptotic type frequencies, which is exactly where the literal
     version broke). Untried; flagged as a candidate, not vetted for viability.

  3. **Direct pigeonhole on the (already finite, already certified) extended-type
     alphabet `𝒫'` rather than on prime-divisibility.** Since `𝒫'` is finite
     (Extended Persistent-Type Pigeonhole), the TYPE sequence `μ(n):=ρ(n)∈𝒫'` is
     itself a finite-alphabet sequence; Morse–Hedlund could be applied to `μ`
     directly instead of to the gap sequence. This is weaker to establish than
     opening 1 (an easier target: bounded complexity of `μ`, not of `g`) but does
     NOT by itself give periodicity of `(a_n)` — type periodicity does not force
     gap periodicity, since the exact chosen integer within a fixed type could
     still vary. This only has value as a *lemma toward* opening 1, not a
     standalone route; flag as a possible auxiliary step, not a bypass.

- Candidate technique(s): combinatorics-on-words (Morse–Hedlund, subword/factor
  complexity, "special factors," de Bruijn graphs) — a technique family with zero
  prior use in this workspace across 11 rounds. Everything else in the KB relevant
  here (CRT, pigeonhole, Bounded Gap Lemma) is already fully exploited by the
  existing framing.

- Cheap-kill candidates: none obvious for opening 1/3 beyond the complexity
  computation already run (see below) — it did not refute anything, just gave
  mild supportive evidence. No parity/injection/pigeonhole one-liner kills this
  reformulation outright; it stands or falls on whether a genuinely new
  complexity-bounding argument can be built.

- Knowledge-base entries to use: none of the existing KB entries name
  combinatorics-on-words / Morse–Hedlund explicitly — **this is a gap in the KB**
  worth flagging to the outliner: if this direction is pursued, the theorem
  statement and proof sketch should be stated explicitly in the outline (it is
  classical and short: eventually-periodic ⟺ bounded factor complexity, proved
  by a counting/pumping argument on the finite window space). Otherwise, the
  standard toolkit (Pigeonhole/extremal, Invariants & monovariants,
  Modular arithmetic/CRT) remains the base layer underneath any windows-based
  argument.

- Analogous past problems (cruxes): searched `number_theory` domain broadly
  (subtopics `sequences-and-recurrences`, `invariants-and-monovariants`,
  `divisibility-and-gcd`, `processes-and-algorithms` does not exist as a listed
  subtopic) for "eventually periodic," "greedy," "gcd," "smallest integer greater
  than" — the only real hit is **`aimo-0678`** (coupled `a_{n+1}=gcd(a_n,b_n)+1,
  b_{n+1}=lcm(a_n,b_n)-1`, prove `(a_n)` eventually periodic), whose crux is an
  invariant-sum trick (`s_n=a_n+b_n` frozen during a divisibility phase). This was
  **already tried and killed** in round 7 of this workspace (the "algebraic-
  recursion transplant," refuted by an exact counterexample + the certified
  **Witness Discontinuity Obstruction** — do not retry). No other crux in the
  corpus is a genuine structural analog of a self-referential greedy gcd-chain
  sequence; nothing else resembling "smallest legal successor" constructions
  turned up. Report: no further analogous cruxes found for the fresh angles above
  (the combinatorics-on-words idea has no crux-corpus analog either — it is
  outside this corpus's represented technique set).

- Prior progress: (unchanged from `current.md`) Free Facts, Bounded Gap Lemma,
  Generalized Bounded Gap Lemma, Persistent-Type / Extended Persistent-Type
  Pigeonhole, Finite Core Theorem, Generalized Bounded Witness Lemma +
  Recruitment Corollary, Canonical-Refinement Lemma, Collateral-Safety Theorem
  (reduces (†) to base-type-pair-level termination on a FIXED finite index set),
  |Q|=1 fully solved. The single open gap is FAH/Symmetric FAH ("Cofinite FAH"),
  with 14 confirmed-dead mechanisms across 6 rounds, zero counterexamples found
  in 500+ tested seeds.

- Dead ends (do not retry):
  - All 14 mechanisms cataloged in `current.md` rounds 6–11 (existential/pigeonhole,
    magnitude-sandwich, tautological-minimality, CRT-glue/competitor-construction
    in every modulus variant, aggregate density/sieve-counting) — confirmed dead,
    verified by this exploration's re-read, not re-tested.
  - **`seed-coupling-induction`'s literal term-by-term correspondence** (round 8):
    cleanly and reproducibly falsified — for `a_1=105` removing `p=7` gives a
    STABLE 55% mismatch density (not shrinking, checked at N=100..8000) and,
    decisively, the two type sequences have DIFFERENT limiting frequencies
    (16%/56%/28% vs 25%/50%/25%), so no realignment of the correspondence map can
    ever fix it. Any future induction-on-`ω(a_1)` attempt MUST use a different,
    non-positional coupling — do not re-propose literal skeleton matching.
  - **`reversible-transition-map`'s finite-automaton bypass** (round 5): proven
    LOGICALLY EQUIVALENT to gap (†) at any fixed core level `S` — "S-sufficiency"
    ⟺ "V=∅ at level S." This means an unconditional finite-automaton/compactness
    argument built directly on the existing `S₀`-signature state space cannot
    bypass FAH; it would have to reprove FAH in different language. I extend this
    caution explicitly to opening 3 above (type-sequence periodicity alone is
    insufficient) but NOT necessarily to opening 1 (the gap-sequence complexity
    claim is about `g_n` directly, not about `S₀`-signatures, so it is not the
    same object this equivalence was proved for — worth the outliner's own
    scrutiny before assuming it inherits the same equivalence).
  - `aimo-0678`-style algebraic-recursion transplant (round 7): refuted by exact
    counterexample + Witness Discontinuity Obstruction, certified.

- Small-case / intuition notes (all labeled conjecture/observation, not proof):
  - Ran a quick, independently-coded (not reusing any approach's script) greedy
    generator and computed subword/factor complexity `p(k)` of the gap sequence
    for `a_1 ∈ {105, 175, 4807}` up to `N=4000` terms. For `a_1=105`, `p(k)`
    plateaus exactly at 58 for `k≥8` (strong evidence of eventual periodicity
    with a moderate period, consistent with everything already believed about
    this seed). For `a_1=4807` (a seed the workspace already treats as a
    "genuinely open |F'|≥2" hard case), complexity is still slowly growing at
    `k=20` (3948→3979→3986, nearly flat) but not exploding — mildly consistent
    with eventual periodicity at a large but finite period, not informative
    enough to distinguish "true" from "very slow drift." This is weak supportive
    evidence only, not a new result.
  - My own from-scratch attempt to detect "rogue pairs" and directly test FAH on
    ~30 fresh seeds (including untested `ω(a_1)∈{3,4,5,6}` combinations like
    2310, 2730, 3003, 30030) using a simplified heuristic (persistence = ≥3
    occurrences in the second half of a 3000-term window) found **zero rogue
    pairs at all** on every seed tried, including seeds (187, 209, 247, 385, 175)
    the workspace's own history reports DO have rogue pairs. This strongly
    suggests my simplified detector does not match the workspace's precise
    minimal-witness/extended-type convention (rather than being new evidence that
    rogue pairs don't exist) — **flag this explicitly so the outliner does not
    mistake it for a refutation of prior rogue-pair findings**; it is inconclusive
    due to a likely detector-calibration mismatch, not a finding. If a future
    round wants a truly independent large-seed FAH stress test, it should port
    the exact minimal-witness/`S₀` construction from `covering-system-construction`
    rather than re-deriving a shortcut heuristic as I did here under time
    pressure.
  - Overall assessment: I did not find a way to prove periodicity that avoids
    reconstructing something logically equivalent to FAH — the Morse–Hedlund
    reformulation (opening 1) is honestly an equivalence, not an escape hatch,
    but it is a technique family (combinatorics on words) genuinely never tried
    here, and per CLAUDE.md's plateau-breaking rule this is worth one build slot
    given six rounds of stall on the divisibility-machinery framing — but the
    outliner should treat it as "different tools on the same wall," not as a
    proven-lower-difficulty bypass, and should require the build to identify a
    CONCRETE new complexity-bounding argument (e.g. an explicit pumping/potential
    scheme) before claiming progress, not just restate Morse–Hedlund as if citing
    it were a proof.
