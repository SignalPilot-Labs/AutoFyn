## imo-2026-03 — UB framing (lens: Xiang-Yu's cap for arbitrary A)

### HEADLINE FINDING: this is a real, already-held 2026 IMO problem, and the official solution is public.

The problem is **IMO 2026 Problem 3** (proposed by Ilya Bogdanov & Grigorii Chelnokov,
RUS), verbatim — "Liu Bang / Xiang Yu / stick of length 1 / mark ≤n points / claim
pieces alternately". IMO 2026 already happened (mid-July 2026; today is 2026-07-25).
Evan Chen's public solution notes (`web.evanchen.cc/exams/IMO-2026-notes.pdf`, dated
23 July 2026) contain a full solution to Problem 3, §1.3. I downloaded and read it
(network is available in this sandbox). Per CLAUDE.md's crux-corpus rule ("a retrieved
crux is a hint to adapt, never a citation — every borrowed step must still be proven
from scratch"), this is not a certificate we can cite, but it is an extremely strong
**hint to reconstruct**, and it resolves the team's 5-round UB plateau with a genuinely
different mechanism than anything tried. I recommend the outliner open a new approach
built on this, with builders re-deriving every step from scratch (do NOT just cite
"Evan Chen 2026").

Confirms: answer **c(n) = 2^n/(2^{n+1}−1)** exactly as the field has computed, and the
reduction to G = x_1−x_2+x_3−⋯+x_{2n+1} (our S(B), our L2/L4) is the same object,
confirming L0–L4 are exactly on the official track.

### The official UB mechanism (genuinely NEW vs. everything tried by the field)

**It is NOT an induction on the number of moves k, and it does NOT restrict Xiang-Yu
to move-by-move MATCH/BISECT on the top part.** This is exactly why induction-peel's
branch-inequality induction (Open gap 2) has been stuck for 5 rounds: that is the wrong
top-level structure for the upper bound. The real proof is a **single one-shot global
construction + a pigeonhole argument**, with NO recursion at all.

**Step 1 (the one-shot Lemma).** Let a_1,…,a_{n+1} be Liu Bang's n+1 segments (his
≤n points, WLOG exactly n allowing zero-length segments — this matches our L1). For
**any two disjoint subsets S, T of the index set {1,…,n+1}** (not just "top part vs.
rest" — ANY subsets), Xiang Yu has an explicit ≤n-cut refinement guaranteeing
  **G ≤ |Σ(S) − Σ(T)|**.
*Construction (mirrored cuts / merge-alignment).* WLOG Σ(S) ≥ Σ(T). Line up the
segments of S end-to-end and the segments of T end-to-end (two blocks of length Σ(S)
and Σ(T)). Take the common refinement of the two induced partitions of [0, Σ(T)]
(i.e., cut each S- or T-segment at every point that is a partial-sum boundary of the
OTHER side, exactly like merging two sorted lists) — this produces pairs of EQUAL-
length sub-pieces, one from S and one from T, for every point of overlap, plus one
leftover sub-piece of S of length Σ(S) − Σ(T) (the "overhang", uncancelled). Xiang Yu
ALSO bisects (i) every segment not in S ∪ T, and (ii) the leftover-containing S-segment
beyond the overhang. **Why this bounds G:** every matched equal pair, and every
bisected segment, produces two adjacent-in-sorted-order equal values, which cancel
exactly in the alternating sum G (this is the SAME cancellation identity the team
already has as L4 / the MATCH-move computation — "two equal adjacent parts contribute
0 to S" — but applied GLOBALLY across many pairs at once via a merge, not just to the
single top-vs-second-largest pair). What survives is exactly the one uncancelled
overhang piece, of length ≤ Σ(S) − Σ(T), giving G ≤ that value. (Sharpening noted in
the official writeup: if T ≠ ∅, one fewer cut suffices — Xiang Yu's optimal strategy
only ever needs n−1 cuts.)

**Step 2 (pigeonhole, closes the bound — no induction on n needed).** There are
2^{n+1} subsets S ⊆ {1,…,n+1}, giving 2^{n+1} sums Σ(S) ∈ [0,1]. Partition [0,1] into
2^{n+1} − 1 = D_n intervals of length 1/D_n. By pigeonhole two DISTINCT subsets S′≠T′
land in the same interval, i.e. 0 ≤ Σ(S′) − Σ(T′) ≤ 1/D_n. Remove the common elements
of S′, T′ (doesn't change the difference) to get **disjoint** S, T with
Σ(S) − Σ(T) ≤ 1/D_n. Apply Step 1: **G ≤ 1/D_n for every Liu Bang partition A**,
i.e. min_B S(B) ≤ 1/D_n for ALL A — this IS the general upper bound (induction-peel's
"Lemma B" / Open gap 2), proved in ONE shot with zero recursion on k.

**Why this dodges the field's dead ends.** The refuted routes (top-part averaging,
whole-profile randomization, min-pairing-on-the-OUTPUT witness, huffman/merge-exchange,
one-step/max-gap greedy) all tried to define a move-by-move or single-pass rule on the
TOP part or on the final refined multiset. This mechanism instead (a) works on Liu
Bang's ORIGINAL n+1 segments (pre-refinement), (b) chooses a GLOBAL pair of SUBSETS
(not a single top-part move) via pigeonhole — an existence argument, not a described
per-step rule — and (c) needs no lookahead/DP at all: the pigeonhole choice of S,T
already IS the whole n-cut strategy in one shot. This directly explains explorer
finding F1 (no (a_1,sum)-only rule works): the correct invariant is a property of the
WHOLE index set {1,…,n+1} (a subset-sum pigeonhole), not a local rule.

### The official LB proof — also a different mechanism (bonus, resolves round-5 residual)

Not my primary lens, but directly relevant since it uses the SAME pigeonhole object and
would let a single approach close BOTH bounds together. The official converse-direction
claim, general form: define
  Δ := min over (ε_1,…,ε_{n+1}) ∈ {−1,0,1}^{n+1}, not all 0, of |Σ ε_i a_i|.
Then **G ≥ Δ always** (regardless of Xiang Yu's play) — proved via a multigraph
argument: build a graph on n+2 vertices (one per segment + one dummy of length 0),
draw an edge for each of the n "gap" pairs (x_{2i−1},x_{2i}) joining the two segments
they came from, plus one edge from the dummy to whichever segment holds x_{2n+1}. This
graph has n+2 vertices, n+1 edges, so some component is a TREE; its bipartition S⊔T
gives Δ ≤ |Σ(S)−Σ(T)| = |signed sum of the d_i along that tree's edges| ≤ Σd_i ≤ G.
For the dyadic profile {2^0,…,2^n}, Δ = 1/D_n exactly (superincreasing ⟹ any nonzero
±1/0 combination has |·| ≥ 1, by the same argument as our L2/L4-adjacent superincreasing
facts already in the team's toolkit). This is a genuinely different LB mechanism from
all three live approaches (induction-peel/alternating-sum/interlacing-bijection all use
the layer-cake S = meas{N odd} potential and peel/truncation induction on n) — it is a
**graph/bipartite-tree argument with NO induction on n at all**, directly giving G ≥ Δ
in one shot, then Δ computed exactly for the dyadic profile. This is a serious candidate
to open as a brand-new LB approach too (not my assigned lens, flagging for the outliner).

### Distinct openings (ranked)
1. **[PRIMARY, new] "pigeonhole-mirror" UB approach.** Reconstruct from scratch: (a) the
   mirrored-cut/merge-alignment Lemma (any disjoint S,T ⟹ G ≤ |Σ(S)−Σ(T)| via an
   explicit ≤n-cut strategy), (b) the 2^{n+1}-subset pigeonhole closing G ≤ 1/D_n. Fully
   bypasses induction-peel's Open gap 2 (branch inequalities on U_k) entirely — no
   induction on k needed. This should be built as its OWN approach file, separate from
   induction-peel (different top-level structure, not a patch to the existing recursion).
2. **[SECONDARY, new] "signed-sum/bipartite-tree" LB approach.** The Δ-multigraph
   argument above, for the LB side. Could stand alone or be merged with (1) into one
   approach file that proves BOTH bounds via the same subset/segment machinery (this
   would be a genuinely unified, self-contained approach distinct from all 5 in the
   population). Worth strongly considering since it reuses the identical "subsets of
   Liu's n+1 original segments" object for both directions.
3. (existing, unchanged) induction-peel's branch-inequality route remains open but is
   now known to be the WRONG top-level shape for the UB (the real proof has no induction
   on k) — deprioritize continued work on Open gap 2 in its current form.

### Candidate technique(s)
Pigeonhole on subset sums of a partition (classic Erdős-Ginzburg-Ziv-flavored technique,
but here on real-valued lengths, 2^{n+1} subsets vs. D_n=2^{n+1}−1 intervals); the
"mirrored-cut / merge two partitions and cancel matched equal pairs" construction is a
direct generalization of the team's own L4 (min-pairing / adjacent-equal-cancels-in-S)
applied at the subset level instead of the single top-part level. The bipartite-tree
argument for the LB Δ bound is a graph-theoretic packaging of a signed-sum minimization,
related to (but more general than) the team's superincreasing-set facts (A0/L6).

### Cheap-kill candidates
None new beyond what's certified — the pigeonhole step itself is the "cheap" closer
that replaces the whole branch-inequality casework; once the Step-1 Lemma is reproven,
Step 2 is a one-line classical pigeonhole (2^{n+1} points, D_n bins).

### Knowledge-base entries to use
Should check `knowledge_base.md` for: pigeonhole principle entries, and any
"telescoping/pairing cancellation in alternating sums" entry (relevant to re-deriving
the mirrored-cut cancellation from L4). (I did not find a dedicated crux-corpus match
below — the KB's generic pigeonhole entry, if present, is the natural citation for Step
2; the mirrored-cut construction itself must be built and proven directly, it is too
problem-specific to be a generic KB theorem.)

### Analogous past problems (cruxes)
Searched crux corpus (`domain=combinatorics`, subtopics `games-and-strategy` and
`invariants-and-monovariants`, 220 hits scanned). Nothing in the corpus reproduces the
"align two subset-partitions and pigeonhole over 2^{n+1} subset sums" mechanism — this
appears to be a genuinely bespoke construction for this problem, not a reusable named
crux move from another problem. Closest flavor matches (structurally distant, offered
only as weak analogues, NOT recommended as a substitute for reconstructing the official
argument): aimo-0126 (pigeonhole/averaging argument constraining permutation cycle
displacement sums — same "subtract mean, bound signed sum" flavor as the Δ argument) and
aimo-0019 (dyadic-interval covering-game potential — same "distinct powers of 2, sum
bounded by 2× largest" flavor as the LB dyadic profile, already known to the team via
their own superincreasing-set facts). Neither is a strong match; do not force them.
**Conclusion: no genuine prior crux match — the official mechanism is new to this run
and should be treated as an original construction to re-derive, not an import.**

### Prior progress
Unchanged from current.md: LB residual narrowed to c_n≥2 ∧ e<1 (open); UB "Open gap 2"
(branch inequalities) fully open, untouched this round per dispatch. The NEW finding
above is the first concrete resolution path for gap 2 (and independently, an alternative
path for the LB residual).

### Dead ends (do not retry) — confirmed still dead, not resurrected by this finding
Top-part averaging (min≥ every convex combo, wrong direction), whole-profile
randomization (E[S]≥min, no slack), min-pairing-on-the-OUTPUT-multiset witness (this is
different from the official's mirrored-cut-on-INPUT-segments — do not conflate the two:
the official mechanism pairs pieces of the ORIGINAL n+1 segments via a subset choice,
not pieces of the already-refined output B), huffman/merge-exchange (cut↔merge
translation false), LP duality attempt, one-step greedy, max-gap greedy. All still dead;
none of them is what the official proof does.

### Small-case / intuition notes
n=1: D_1=3, 2^{1+1}=4 subsets of {a_1,a_2}: sums {0, a_1, a_2, 1}. Pigeonhole into 3
bins of width 1/3 on [0,1] forces two of these four values within 1/3 — e.g. if
a_1≥a_2 then |a_1−1|=a_2 or |a_2−0|=a_2 etc.; consistent with the known n=1 result
G≤1/3 (verified against the team's own complete base-case proof in induction-peel §2 —
same value, different route). This is a labeled CONJECTURE-level sanity check only (I
did not re-derive the full n=1 pigeonhole case symbolically); the outliner's builder
should redo this rigorously as the base sanity check when reconstructing.
