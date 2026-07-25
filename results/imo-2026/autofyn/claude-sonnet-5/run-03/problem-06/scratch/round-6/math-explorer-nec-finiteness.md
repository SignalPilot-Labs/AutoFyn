## imo-2026-06 (lens: Q_min / Nec-finiteness central gap)

- Distinct openings (new mechanisms, not yet tried by any dead-mechanism list):
  1. **Bounded-witness-index conjecture (new, numerically strong).** Instead
     of attacking "is Nec finite" as an abstract existence question, attack
     the sharper, concrete, likely-more-tractable claim: *every prime of
     Nec\R(a_1) is witnessed by some pair (i,j) with j bounded by an explicit,
     computable function of a_1 alone* (not of the eventual period/type
     stabilization index, which is itself unbounded and circular). If provable,
     this immediately gives Nec-finiteness (only a bounded, explicit prefix of
     the sequence need ever be examined) and hands the outliner an actual
     terminating algorithm/certificate for Q_min, sidestepping the abstract
     "does a finite Q exist" existential entirely. This is a genuinely
     different target from all 7 dead mechanisms: it is an index bound on
     *when Nec stops growing*, not a size/threshold bound on Q or a
     recruited prime, and not a covering-gap or automaton argument.
  2. **Class-pair-count reformulation (new, but numerically REFUTED as a clean
     bound — report as a checked negative, not a live opening).** One might
     hope each unordered pair of "owning classes" {p,q}⊆R(a_1) (via the
     Same-Class-Free/Class-Partition Reduction) contributes only O(1) Nec
     elements, giving Nec-finiteness via C(|R(a_1)|,2) class-pairs times a
     constant. This is FALSE: a single class-pair can carry many distinct
     Nec\R(a_1) elements (e.g. a_1=35's single class-pair {5,7} carries 3 of
     its 4 Nec\R1 elements: 7,2,3 — see data below). Do not re-propose "bound
     Nec by counting class-pairs"; the real bound (if it exists) must come
     from the witness-index angle (opening 1), not a per-class-pair counting
     angle.
  3. **Trivial-witness filtering.** A subtlety worth flagging to the outliner:
     naive "first index a new Nec prime appears" statistics are contaminated
     by trivial witnesses of primes already in R(a_1) (any pair (0,j) where
     a_j shares with a_1 exactly one of a_1's own prime factors just re-derives
     a known element of R(a_1), contributing nothing to the open finiteness
     question). Any future mechanism/statistic MUST filter to Nec\R(a_1)
     only — conflating the two produced a spurious "index 191" false alarm
     in my own first pass (see Small-case notes).

- Candidate technique(s): direct combinatorial/inductive bound on the
  smallest prefix length N(a_1) (function of ω(a_1) or of a_1's structure,
  NOT of the type-stabilization index n_1(Q_0) which is empirically
  unbounded/uncorrelated) such that no pair (i,j) with j>N(a_1) can ever be a
  *first* witness of a new element of Nec\R(a_1). This would likely proceed
  by an early-term structural argument (e.g. about which small integers are
  forced to appear among a_2,...,a_k by the Multiple-of-R Realization Lemma
  and pairwise-non-coprimality) rather than anything touching the
  self-sufficiency/covering machinery the population has been stuck on.

- Cheap-kill candidates: check whether last-growth-index correlates with
  |R(a_1)| (checked: does NOT cleanly scale — omega=6,7 seeds mostly show
  index 0-2, while one omega=4 seed (20735) shows index 69, and no
  seed exceeded index ~9 among 20+ random multi-prime tests except that one
  outlier) — so a simple closed-form N(a_1)=f(ω(a_1)) is not obviously the
  right shape; the outlier needs case-by-case understanding (see below)
  before conjecturing an exact formula.

- Knowledge-base entries to use: none of `knowledge_base.md`'s generic
  theorems appear to bear directly on this specific numeric-witness-index
  question (it is closer to an elementary but delicate combinatorial-number-
  theory fact about early greedy-sequence terms than to a named theorem);
  Sperner's theorem and CRT (already used elsewhere in the population) are
  the only classical tools plausibly relevant, and neither was needed for
  this experiment.

- Analogous past problems (cruxes): none identified as genuinely analogous
  for this specific sub-question (bounding a witness index in a greedy
  gcd-covering recursion) — the corpus's closest known analog for the whole
  problem, `aimo-0678`/`aimo-0680`, was already checked exhaustively by
  prior rounds and found not to transplant (see
  `aimo-0678-mechanism-inapplicability.md`,
  `frozen-invariant-monovariant`'s round-5 negative result); I did not find
  a new corpus entry specific to "bound the index at which a derived
  necessary-witness set stops growing" — flag this as a real corpus gap
  rather than force a weak match.

- Prior progress: `nec-necessity.md` (Nec⊆every valid Q, hence Q_min is the
  unique minimal candidate — certified) and
  `same-class-free-class-partition-reduction.md` (only cross-class pairs
  can witness Nec\R(a_1) — certified) are the relevant certified facts this
  lens builds on. Both remain correct and are the right starting point for
  opening 1's mechanism (the bounded-witness-index search need only ever
  scan cross-class pairs, per the Class-Partition Reduction — this halves
  the work any future proof attempt needs to do).

- Dead ends (do not retry): the 7 already-listed dead mechanisms (g(Q)
  threshold, prime-size threshold, Λ-split tautology, windowed ε_n
  automaton, Q={primes≤rad(a_1)}, chain-transitivity,
  ρ(n)≥2 redundancy growth) — confirmed still dead, no new information
  found that revives any of them. Additionally, this round's own checked-
  and-refuted idea: "each cross-class pair contributes O(1) Nec elements"
  (opening 2 above) — a genuinely new idea, tried and killed this round,
  should be added to the dead-mechanism list going forward.

- Small-case / intuition notes (all conjecture/evidence, not proof):
  - Across ~30 tested seeds (ω(a_1) from 2 to 7, including three
    "adversarial" seeds specifically chosen to stress multi-prime and
    large-prime structure: 194287=37·59·89, 385=5·7·11, 20735=5·11·13·29),
    **Nec\R(a_1) always stabilizes by a small index** — verified by
    re-running to 3000-5000 terms with zero further growth in every case —
    but the stabilization index is **not** a clean, monotone function of
    ω(a_1): most seeds stabilize by index ≤9, but one outlier (a_1=20735,
    ω=4) needs index 69 (confirmed stable through 4000 terms). This
    outlier's structure: R(a_1)={5,11,13,29}; the four Nec\R1 elements
    {2,3,7,19} appear at witness indices 3,3(?),and later ones up to 69 —
    worth a future round's hand-trace to find the combinatorial reason (my
    time budget did not allow tracing exactly why 20735 is slow — this is
    the single most useful concrete "hard instance" for a future round to
    hand-analyze in detail, more informative than any of the previously
    circulated adversarial seeds since it isolates slow Nec-stabilization
    specifically, not slow period-length or large recruited-prime size).
  - Concrete corrected data table (index = j of first pair (i,j) witnessing
    a new element of Nec\R(a_1); trivial R(a_1)-self-witnesses filtered
    out): a_1=15→idx2([2]); a_1=35→idx3([2,3]); a_1=65→idx3([2,3]);
    a_1=99→idx4([2,5]); a_1=385→idx6([2,3,19]); a_1=194287→idx9
    ([2,3,17,103]); a_1=1716099 (ω=6)→idx4([2,5]); a_1=20735 (ω=4)→idx69
    ([2,3,7,19]). This is the cleaned-up version of round 5's "24. ALWAYS"
    memory note (which used a depth-window check, not witness-index
    tracking, and did not filter trivial R(a_1)-witnesses) — recommend the
    outliner use this corrected/sharper metric, not the older one.
  - Per-class-pair breakdown (opening 2's refutation data): for a_1=35,
    class-pair {5,7} alone carries Nec primes [7,2,3] (all three post-R1
    elements) — a single class-pair is not limited to O(1) contributions.
    For a_1=194287, class-pair {37,59} alone carries [59,2,3,103,17] (5 of
    7 total Nec elements) while {37,89} carries only [89]. No visible
    regularity in which class-pair "does the work," beyond it usually being
    the pair of the two *smallest* primes of R(a_1) (true in every example
    checked) — a possible (untested-as-a-bound) structural hint: the
    dominant cross-class pair is (min R(a_1), second-min R(a_1)), worth a
    future round checking as a genuine pattern vs. coincidence.
