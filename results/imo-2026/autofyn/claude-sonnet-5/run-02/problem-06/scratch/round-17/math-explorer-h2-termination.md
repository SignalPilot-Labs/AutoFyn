## imo-2026-06 (lens: H2 core-absorption-chain termination — find a DIFFERENT quantity/argument than M_B)

- Distinct openings:
  1. **(Idea 3, executed) Numeric re-probe with corrected methodology** — I
     built a fresh, independent proxy simulation of the absorption chain
     (S_0 = Q, persistent types via a tail-window Counter, N(S) := last index
     whose type isn't in the tail-persistent set, then absorb full
     factorizations of a_1..a_{N(S)} and repeat) and found that round 16's
     "no sign of stabilizing within 15,000 terms" result on a_1=11305 is very
     likely a **methodological artifact**, not evidence of non-termination:
     at N_terms=6000/12000 the proxy pins N(S_0) near the sample boundary
     (5895, 11827 respectively — an obvious "ran out of window" signature),
     but at N_terms=20000/25000/30000 the SAME seed's proxy resolves cleanly
     to N(S_0)=0 (Q itself is immediately self-absorbing, chain terminates
     at round 0, |S|=4 forever). This matches memory rule 30's own warning
     exactly (proxy unreliable near the sample boundary) and shows the
     earlier discouraging finding was premature, not a structural signal.
     Tested seeds 15, 35, 105, 175, 320, 1001, 2431, 4807, 11305 at
     N_terms=20000-25000: **all 9 stabilize at round 0 with S_0=Q** (i.e.
     N(S_0)=0, the absorption chain is trivial/instantly terminates) once
     given enough samples to escape the boundary artifact. Zero
     counterexamples found on any resolvable seed.
  2. **(Idea 3 continued) Stress-test on larger |Q|.** a_1=15015=3·5·7·11·13
     (|Q|=5) genuinely does NOT resolve even at 60,000 sampled terms: round 0
     gives N(S_0) proxy=57080 (borderline, not pinned but very close to the
     boundary), and the resulting absorption jump is enormous (|S| jumps from
     5 to 3574, essentially swallowing almost every prime below ~a_{57080}'s
     magnitude) before pinning again immediately in round 1. This is the
     "proxy breaks down once |S| passes a few dozen primes" failure mode
     memory rule 30 already flags — it is **honestly inconclusive**, not a
     counterexample to H2, but it does show wider-|Q| seeds need much deeper
     runs (consistent with memory rule 11's "wider Q ⇒ much longer
     transients" finding for the unrelated FAH recruitment process) and that
     no cheap numeric check will settle H2 in general.
  3. **(Idea 4, answered — does NOT trivialize) |S_k| is not a priori
     bounded.** Checked directly: the certified/rule-5 fact that the TOTAL
     prime support of the whole sequence (∪_n P(a_n)) is genuinely unbounded
     (grows ~linearly in n, verified in round 2) applies with equal force to
     S_∞ := ∪_k S_k, since S_∞ ⊆ ∪_n P(a_n) has no independent finiteness
     source — there is no "ambient finite universe" the absorption chain is
     confined to a priori. So the naive "|S_k| only grows, and must stay in
     some finite ambient set" framing is FALSE as stated; boundedness of
     S_∞ is exactly equivalent to H2 itself (via the certified Termination
     Criterion Lemma's ⟸ direction, which literally constructs S_∞ ⊆
     S_0 ∪ P*_M from a hypothesized bound M on N(S_k)) — this is a
     restatement, not a bypass. Do not propose this as a cheap-kill; it is
     circular.
  4. **(Idea 1, answered — no bypass found) Direct/compactness-style
     termination without an explicit N(S_k) bound.** Any well-ordering or
     compactness argument for "the chain S_0 ⊆ S_1 ⊆ ... stabilizes" reduces,
     on inspection, to showing S_∞ is finite (a strictly increasing chain of
     subsets of an infinite ambient set of primes need not terminate; the
     only way to force termination without an explicit numeric bound is
     König's-lemma-style "finitely branching" reasoning, but there is no
     finite branching bound here — at each step the chain can in principle
     recruit an unboundedly large new batch of primes, since N(S_k) is
     literally the branching/reach parameter in question). This is the exact
     same wall round 15's dedicated compactness/König's-lemma sweep hit for
     FAH (memory rule 29) — the same diagnosis transfers verbatim to H2's
     absorption chain, since both are "greedy/monotone-enlargement under a
     non-constructive pigeonhole threshold" (already flagged as the
     structural analogy in `termination-criterion-lemma.md`). No new
     leverage found; do not spend a build round re-deriving this.
  5. **(Idea 2, answered — no) No existing certified lemma yields H2.**
     Grepped the full `lemmas/` directory (46 files). None besides
     `termination-criterion-lemma.md` (iff-reduction only) and
     `binary-refinement-and-threshold-recursion.md` (round 16's M_B
     non-constructivity) touch N(S_k)/absorption-chain boundedness at all.
     `finite-core-theorem.md` gives an explicit finite S with the
     persistent-type structure but with NO guarantee of self-absorption
     (its witness-index construction is silent about whether early terms'
     FULL factorizations lie in S — a strictly different, stronger property
     the absorption chain needs). No shortcut available from the existing
     stack.
  6. **A genuinely different, untried angle (flagged, not developed):**
     instead of tracking the numeric threshold N(S) (an index-based "last
     exception"), track the growth of `|𝒫'(S)|` (the NUMBER of S-persistent
     TYPES, bounded by `2^{|S|}-1`) as a function purely of `|S|`, and ask
     whether there's a combinatorial (not index-based) argument that the
     absorption process can only recruit finitely many "genuinely new"
     types before running out of room in `2^{|S|}` — i.e. attack H2 via a
     counting/pigeonhole bound on the type-alphabet SIZE rather than on the
     exception INDEX. This is speculative and UNTRIED (I did not attempt to
     develop it — it may hit the same M_B-style non-constructivity wall, or
     it may not, since it changes the object being bounded from an index to
     a set-size, which is a different flavor of quantity than the whole
     M_B/N(S) family the round-16 non-constructivity proof was about).
     Worth a dedicated round if the outliner wants a fresh corridor for H2.

- Candidate technique(s): none beyond the certified Termination Criterion
  Lemma + Binary Refinement/Threshold Recursion machinery; the type-alphabet-
  size counting angle (opening 6) is the one genuinely fresh, unexplored
  technique surfaced this round.

- Cheap-kill candidates: none found that actually work. The seemingly cheap
  "|S_k| stays in a fixed finite ambient set" argument (idea 4) is circular
  with H2 itself — explicitly checked and rejected, do not re-propose.

- Knowledge-base entries to use: none beyond what's already certified in the
  workspace (`termination-criterion-lemma.md`,
  `binary-refinement-and-threshold-recursion.md`, `finite-core-theorem.md`,
  `extended-persistent-type-pigeonhole.md`); generic `knowledge_base.md`
  pigeonhole/compactness entries were considered (per idea 1) and found to
  offer no additional leverage beyond what's already certified.

- Analogous past problems (cruxes): none newly identified this round —
  H2 is a workspace-internal reduction target (not a standard competition
  claim), and the closest corpus analogs for "greedy/monotone threshold
  boundedness" (aimo-0016, aimo-0051, aimo-0514, aimo-0678, aimo-0134,
  aimo-1019) were already mined exhaustively for the sibling FAH crux across
  rounds 5–15 and found not to transplant (see memory rules 12, 19, 21, 24,
  27, 28). No fresh corpus mining was warranted for this specific lens given
  the time budget; if a future round wants to mine specifically for H2 (as
  opposed to FAH), the closest subtopic would be "greedy/monotone processes
  with non-constructive termination thresholds" — not yet searched
  specifically for H2 as distinct from FAH.

- Prior progress: `core-growth-monotonicity.md` (round 16) — Binary
  Refinement Lemma + Threshold Recursion Bound Lemma (exact one-prime
  recursion for N(S)), both certified; M_B proven non-constructive
  (Proposition 3, a genuine "two consistent finite-prefix extensions"
  argument, toolkit-independent). `n1-periodicity-reconciliation.md`
  (rounds 13-16) — Master Conditional Theorem reducing the whole problem to
  H1 (FAH) + H2 (this gap); Termination Criterion Lemma (iff: terminates iff
  N(S_k) bounded).

- Dead ends (do not retry):
  - Making M_B constructive (round 16, proven impossible in general via the
    "two consistent extensions" argument — genuinely toolkit-independent,
    not a workspace gap).
  - "|S_k| bounded by a fixed ambient set" as a standalone cheap-kill (this
    round — circular with H2 itself, no independent finiteness source
    exists for S_∞).
  - Compactness/König's-lemma-style termination argument without an
    explicit bound (this round, re-confirmed — no finite branching bound
    exists; same wall as round 15's FAH compactness sweep).
  - Treating N(S_0) proxy values from short simulation windows (<~10,000
    terms on |Q|≥4 seeds) as real signal — confirmed artifact-prone this
    round (a_1=11305 flipped from "not stabilizing" to "N(S_0)=0" purely by
    quadrupling the sample size).

- Small-case / intuition notes (all labeled conjecture — numeric evidence
  only): On every seed where the proxy resolves cleanly (15, 35, 105, 175,
  320, 1001, 2431, 4807, 11305 — 9/9 with |Q| ≤ 4), the absorption chain
  terminates IMMEDIATELY at round 0 with S_0 = Q itself already
  self-absorbing (N(S_0)=0). This is stronger and more uniform positive
  evidence for H2 than round 16 found (round 16 reported non-stabilization
  within 15,000 terms as discouraging; this round's larger runs reverse that
  specific reading, though the underlying open question is unchanged). The
  one genuinely unresolved seed (a_1=15015, |Q|=5) shows the proxy breaking
  down exactly as memory rule 30 warned, not a counterexample. Net
  conjecture: H2 is very likely TRUE (bounded, and empirically often
  trivially N(S_k)=0), matching the pattern seen with FAH (extensive
  positive numeric support, no proof found) — the outliner should treat H2
  as "probably true, not yet provable with current tools" rather than a
  live candidate for falsification, and should prioritize either (a) the
  type-alphabet-size counting angle (opening 6, untried) or (b) accepting H2
  as a second honestly-disclosed open hypothesis alongside H1 if no new
  corridor is found in the next 1-2 rounds.
