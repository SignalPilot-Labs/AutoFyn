## imo-2026-06 (lens: fresh mechanism for FAH / Symmetric FAH)

- **Distinct openings surfaced this round:**
  1. **Fixed-Witness Divisor-Chain (new, promising, needs scoping).** Instead of
     tracking the single prime q abstractly, fix the actual witness INTEGER
     a_{n_A} (the earliest occurrence of extended type A') and, for every later
     occurrence n of the same extended type A', study d_n := gcd(a_{n_A}, a_n) —
     a divisor of the FIXED integer a_{n_A}, hence living in a finite lattice
     (Divisor analysis, knowledge_base.md `## Number Theory`; direct structural
     analog of crux `aimo-0477`'s d_n = gcd(a_1,a_n) monovariant, already flagged
     in memory rule 22). This is a genuinely different top-level object than
     anything in the certified toolkit: it controls the factorization of an
     ACTUAL later term relative to the FIXED witness by literal integer
     divisibility, not by an abstractly-constructed competitor (Lemma K's
     problem) and not by re-deriving Free Facts/Bounded Witness/Gap
     Lemmas/Critical Prime Dichotomy. This is exactly ingredient (a) from the
     dispatch ("control the factorization of a constructed [or actual]
     competitor integer relative to the actual witness").
  2. **aimo-0611-style same-type occurrence induction (new, needs scoping).**
     Prove q | a_n for the k-th occurrence of type A' by induction ON THE
     ORDERED OCCURRENCE INDEX k (not on recruitment/refinement stage). This is
     structurally different from the dead "inductive chaining across successive
     same-type occurrences" listed as one of Lemma I's four dead recombinations
     — that dead attempt (per round 6) used only the four certified tools
     (Free Facts / Bounded Witness / Gap Lemmas / Critical Prime Dichotomy) as
     its inductive step. The fresh version proposed here instead anchors the
     induction on gcd-with-fixed-witness data (opening 1 above), giving the
     induction step new content the old attempt didn't have. Crucially, since
     this induction is over occurrences of ONE fixed type A' (not across
     recruitment stages that change the core S₀), it may sidestep the certified
     Witness Discontinuity Obstruction, which specifically concerns the witness
     of "the currently relevant type" being re-selected at recruitment stages —
     here the type A' never changes, only its occurrence index k grows. This
     matches ingredient (b) ("stability of witness selection...that survives
     the...Obstruction") in a way the obstruction doesn't directly forbid,
     since the obstruction is about cross-stage continuity, not same-type,
     same-stage occurrence-to-occurrence continuity.

- **Candidate technique(s):** Divisor-chain-bounded-by-a-fixed-integer
  monovariant (aimo-0477 style), adapted to track FULL integer divisibility
  (not just a single prime) between the earliest witness a_{n_A} and later
  same-extended-type occurrences; combined with induction on occurrence order
  within one fixed type.

- **Cheap-kill candidates:** Test the STRONGEST possible claim first (it's
  cheap and I already did — see below): "a_{n_A} | a_n for every later
  occurrence n of extended type A'." This is FALSE in general (see Small-case
  notes) — a fast falsification that saves the outliner from chasing the naive
  strong form. The correct scoping (restricted to which types, and to what
  degree of divisibility) is exactly what's undetermined and would need to be
  the outliner's actual target, not the full-strength blanket claim.

- **Knowledge-base entries to use:** `## Number Theory` — "Divisor analysis:
  d(n), gcd structure...bounding a finite search by size" (bounding d_n's
  possible values by divisors of the fixed a_{n_A}); "Order of an element,
  Fermat/Euler: periodicity of a^n mod m" (only loosely relevant background,
  not directly usable — the sequence isn't defined by a fixed modulus map).
  No new knowledge_base entry beyond what's already been used (Free Facts /
  Bounded Witness / Gap Lemmas / Critical Prime Dichotomy / Lemma J / Lemma K)
  is a clean fit; the genuinely new ingredient here is imported from the crux
  corpus, not the knowledge base.

- **Analogous past problems (cruxes):**
  - `aimo-0477` (IMO 2015 SL N-something, Mongolia) — **the closest and most
    load-bearing analog**, already flagged in memory rule 22 but NOT YET
    ATTEMPTED as a mechanism in this workspace. Its crux: define
    d_n = gcd(a_1, a_n); show algebraically d_n | d_{n+1} using the problem's
    own recursive identity, so the divisor chain (bounded above by the fixed
    a_1) must stabilize. **Caveat found this round: our problem has no
    algebraic recursion analogous to aimo-0477's telescoping harmonic-sum
    identity — the greedy "smallest integer with gcd>1 to every prior term"
    rule gives no such closed-form relation between gcd(a_{n_A},a_n) and
    gcd(a_{n_A},a_{n+1})**, so a literal transplant of the proof step is not
    available; only the top-level SHAPE (fixed-witness bounded divisor chain)
    transfers, the actual monotonicity step must be found from scratch for
    this problem's greedy structure.
  - `aimo-0611` (Austria, "for each n≥2 there's a prime dividing a_n but none
    of a_1,...,a_{n-1}") — analogous FOR THE INDUCTION-ANCHORING PATTERN
    (Claim 1: propagate a congruence x_{i+m}≡x_i (mod x_m) by induction,
    anchored at x_0=0) but its recurrence is a FIXED polynomial map with
    perfectly regular index spacing (period m), whereas our type-A'
    occurrences are irregularly spaced along n — the induction skeleton
    (anchor + propagate via the recursion) is suggestive but the "regular
    spacing" assumption does not transfer; would need a substitute anchor
    using Free Facts instead of a closed-form recursion.
  - `aimo-0030` ("Banana game" / IMO game of numbers) — already flagged
    (memory rule 20) as a common-factor-upgrade-to-restricted-class descent;
    still relevant background but not a fresh finding this round.

- **Prior progress:** FAH and Symmetric FAH remain open (see current.md ROUND
  6/7). Five certified unconditional lemmas exist (Free Facts, Generalized
  Bounded Witness Lemma, Gap Lemmas, Critical Prime Dichotomy/Lemma H, Lemma J
  Divisor-Restricted Pigeonhole, Lemma K Adjacent-Multiple-Blocking) — all
  confirmed (per Lemma I) unable to promote an existential per-occurrence fact
  to a uniform one. Witness Discontinuity Obstruction (round 7) rules out
  fixed-pair scalar recursions ACROSS recruitment stages specifically.

- **Dead ends (do not retry):** All items in current.md's "do NOT re-attempt"
  lists (Two-Witness Intersection Uniqueness, Lemma-H branch analysis, the
  literal aimo-0678 algebraic-recursion transplant (H), Lemma K's "round down
  to nearest non-divisor multiple" as standalone route, size/index/|open(k)|
  well-orderings). Additionally, established as newly dead THIS round:
  **the blanket claim "the earliest witness of an extended-persistent type
  divides every later occurrence of the same type"** — false in general (see
  below); do not propose it as a portable lemma without the (currently
  undetermined) restriction that makes it true.

- **Small-case / intuition notes (CONJECTURE / mixed empirical evidence, not
  proof):**
  - On a_1=187 (S₀={2,3,11,17}, rogue pair A'={3,11}, B'={2,17}, q=7): checked
    ALL 165 occurrences of extended type A' up to n=5000 — **every single one
    is an exact multiple of the earliest witness a_{n_A}=231=3·7·11** (gcd
    always exactly 231, never less). This is strictly stronger than FAH (which
    only needs 7 | a_n) and trivially implies FAH+SymmetricFAH on this
    specific example if it were provable in general.
  - BUT this blanket strong claim is FALSE for generic (non-rogue-pair)
    persistent types on the SAME seed: e.g. type {2,11} (⊂ S₀, missing 17) has
    gcd(a_2=220, a_n) cycling through {22,44,110,220,...} — NOT always 220.
    Similarly on a_1=175, types {5,7},{2,3,5},{3,7},{2,3,7},{2,5,7},{3,5,7} all
    show non-constant/non-monotone gcd with the earliest witness, while types
    that include the recruited glue prime 13 (e.g. {2,13,7},{2,3,5,7},
    {3,13,7},...) show PERFECTLY constant gcd = full witness value. On a_1=209,
    the picture is MIXED even among plausible "good" types — one type
    ({2,11,7}) alternates between the full witness value and exactly half of
    it (never lower), suggesting a weaker "eventually within a factor of 2"
    version might be the true general statement, not full divisibility.
  - **Conjecture (untested at scale, plausible next target):** the full-witness
    divisibility phenomenon holds cleanly precisely for the types directly
    involved in a Lemma-G rogue pair (A', B' themselves) — worth testing on
    2-3 more rogue-pair seeds (209's three rogue pairs, 4807's |F'|=2 pair)
    before an outliner commits to it as a lemma target, since the 209 "mixed"
    types found above were NOT confirmed to be the actual rogue-pair types
    (they were just other persistent types on the same seed) — this
    distinction was not fully resolved in the time available this round.
  - **Honest flag:** everything found this round is either (i) an
    UN-YET-DISPROVEN new empirical phenomenon (fixed-witness full/partial
    divisibility for rogue-pair types specifically) that is NOT a repackaging
    of the five dead mechanisms — it introduces a new object (the fixed
    witness integer itself as a modulus) not used by any of them — or (ii) an
    explicitly falsified overreach (the blanket "any persistent type" version)
    that should not be pursued as stated. Recommend the outliner scope a new
    approach around (i), with the FIRST task being to re-verify on 2+ more
    seeds with a script that correctly isolates the exact A'/B' rogue types
    (not incidental persistent types) before committing further build effort.
