## imo-2026-03

### HEADLINE FINDING — a genuinely different, complete-looking framing (found via web search of
the official IMO 2026 solution notes; treat as a HINT TO ADAPT, NOT a citation — every step below
is UNPROVEN by us and must be independently reconstructed from scratch by a builder, per
CLAUDE.md). This is a totally different vocabulary from all 3 live approaches in the field
(none of which work with the layer-cake potential S(B) of the REFINED multiset B — this one works
directly with Liu's n+1 ORIGINAL segments a_1,...,a_{n+1}, never refining to B at all).

Source consulted: `web.evanchen.cc/exams/IMO-2026-notes.pdf`, §1.3 "IMO 2026/3" (verified verbatim
match to `problems.jsonl`'s imo-2026-03 statement — same names Liu Bang/Xiang Yu, same rules).
This is Evan Chen's write-up, crediting "some different ideas from the various shortlisted
official solutions" — so even the source presents it as one of several possible routes, not a
unique canonical proof. Whoever builds from this MUST reprove every claim; nothing here is
citable per CLAUDE.md.

**Reformulation (same as our L0/L1/L2, restated).** Write a_1,...,a_{n+1} for the lengths of
Liu's (LB's) n+1 segments (allow degenerate 0-length "cuts" so LB always uses exactly n marks).
Sort the FINAL refined pieces x_1≥x_2≥...≥x_{2n+1} descending (allow XY's marks to also coincide,
so 2n+1 final pieces always). Liu's score is x_1+x_3+...+x_{2n+1} (greedy-take-largest optimal —
= our L0). Define the **gap** G := x_1−x_2+x_3−x_4+...+x_{2n+1} (= our S(B) exactly, same object,
different name). Target: XY strategy guaranteeing G ≤ 1/D_n for ANY Liu partition; and a Liu
partition (the dyadic 1:2:4:...:2^n one) guaranteeing G ≥ 1/D_n.

**UB mechanism — pigeonhole over subset differences of LIU'S OWN SEGMENTS (not the refined
multiset).** Key claim: *for ANY two disjoint subsets S,T of Liu's n+1 segments, Xiang has a
strategy guaranteeing G ≤ |Σ(S) − Σ(T)|.* Mechanism (sketched in the source, NOT reproven by us):
line up the segments of S against those of T like two sequences to be "matched", have XY cut so
that segments pair off into EQUAL-length pieces (which cancel in the alternating sum, by the same
adjacent-equal-cancellation fact as our certified L4) plus one leftover of length Σ(S)−Σ(T), and
XY bisects every segment not in S∪T (and any part of S beyond the matched prefix). This is a
generalization of the MATCH/BISECT move already in `induction-peel.md` §4 — but crucially applied
per-SEGMENT against a whole chosen SUBSET, not just against the single current top part. Given
this claim, since there are 2^{n+1} subsets of the n+1 segments each with Σ(S) ∈ [0,1], **pigeonhole**
gives two DISTINCT subsets with |Σ(S)−Σ(T)| ≤ 1/(2^{n+1}−1) = 1/D_n (2^{n+1} points, D_n = 2^{n+1}−1
gaps in [0,1]) — after pruning common elements from S,T this differences is unchanged. Hence G ≤
1/D_n for EVERY Liu partition A, with NO case-split on the shape of A at all. This is entirely a
DIFFERENT mechanism from the field's MATCH/BISECT branch-inequality induction (Open gap 2 in
induction-peel.md) — no induction on n, no value-function recursion U_k; it's a single mirroring
construction plus counting.

**LB mechanism (general A, not just dyadic) — a spanning-tree/bipartite-cut argument, giving a
DIFFERENT proof of Lemma A's target than the field's (PM)/(CB) casework.** Define
Δ(A) := min over (ε_1,...,ε_{n+1}) ∈ {−1,0,1}^{n+1}, not all zero, of |Σ ε_i a_i|. Claim: **G ≥
Δ(A) regardless of XY's play.** Mechanism (sketched, NOT reproven by us): let d_1,...,d_n be the
successive "gap" contributions x_{2i−1}−x_{2i} (each ≥0) and d_{n+1}:=x_{2n+1}; build a multigraph
on the n+1 segments plus one dummy vertex (n+2 vertices), with one edge per d_i joining the two
ORIGINAL segments the two pieces x_{2i-1},x_{2i} came from (and the dummy edge for the odd
leftover); since this graph has n+2 vertices and only n+1 edges, some connected component is a
TREE, hence bipartite S⊔T; then |Σ(S)−Σ(T)| is exactly ±d_{i1}±d_{i2}±...(edges of that
component) ≤ Σ d_i over that component ≤ G. Since |Σ(S)−Σ(T)| is one of the terms Δ(A) minimizes
over, Δ(A) ≤ |Σ(S)−Σ(T)| ≤ G.
For the SPECIFIC dyadic profile a_i=2^{i-1} (scaled to sum D_n), Δ(A) = 1 exactly: any nonzero
{−1,0,1}-combination of powers of 2 is a nonzero INTEGER, so |combination| ≥ 1, and ε=(1,0,...,0)
attains exactly 1 — so Δ = 1 with NO analytic casework at all (this is a one-line consequence of
superincreasing/binary uniqueness, not the field's e/(PM)/(CB) machinery). This would give G ≥ 1
in the unnormalized game, matching our certified target exactly, via a wholly different (and
apparently much shorter) route than induction-peel's Lemma A.

**A second, independent LB proof for the dyadic case is also sketched** (§ "Converse direction for
the specific powers-of-two division"): prove by induction on k that x_2+x_4+...+x_{2k} ≤
2^{n-1}+...+2^{n-k} (the running EVEN-rank/matched-pair sum after 2k claims is capped by a partial
dyadic tail) — a strong-induction argument on PARTIAL prefix sums rather than the whole game value,
using a clean contradiction (if violated at the first bad k, all 2k claimed pieces came from the k
largest original segments, forcing x_1+...+x_{2k} ≥ 2(x_2+...+x_{2k}) > (dyadic tail sum), a direct
size contradiction). This is yet a THIRD distinct mechanism (prefix/partial-sum induction), giving
a possible alternate route to the LB if the graph-tree argument proves hard to reconstruct
rigorously.

**Equality-case remark (source claims, unverified by us):** the dyadic 1:2:4:...:2^n division is
the UNIQUE optimal Liu opening; any other A lets XY force G strictly below 1/D_n. This would
resolve the round-5 finding that S(B)=1 holds on an open plateau of configs — that plateau is
about which XY-REFINEMENTS B are extremal for a FIXED dyadic A, not about which A's are optimal;
these are different equality questions and are not in tension.

**Also of direct value: an explicit COUNTEREXAMPLE to the field's whole MATCH/BISECT branch-
inequality program.** The source explicitly refutes exactly the induction-peel §4 mechanism
("Common failed approach... Xiang runs an algorithm of n steps, at each step takes the two
longest pieces a,b and either bisects or cuts a=(a−b)+b"): for n=5, stick (12.80, 6.42, 5.35,
4.34, 2.09)/31 (five numbers, presumably +one more to total 31, or read as the top-scale
profile), EVERY one of the 2^5=32 execution branches of such a top-two-greedy algorithm yields
G > 1 (i.e. fails the target). This independently CONFIRMS the field's own F1 finding (round 3/5:
"no one-pass/local greedy rule works") — it is not merely a heuristic warning, it is the source's
own explicit rejection of the entire match/bisect-on-the-two-largest family, which is structurally
what `induction-peel.md`'s Open gap 2 (§4) is trying to prove a bounded version of. **This should
raise real doubt about whether induction-peel's Lemma B (branch inequalities restricted to
top-part MATCH/BISECT) is provable at all as stated** — the true XY strategy needs the whole-subset
mirroring construction above, not a two-largest-parts-only local rule.

### Distinct openings
1. **[PRIMARY] The subset-difference / pigeonhole-plus-spanning-tree framing above**, adapted and
   independently reproven — attacks UB via pigeonhole over 2^{n+1} segment subsets and LB via a
   graph/tree argument giving Δ(A) ≤ G, with Δ(dyadic) = 1 by pure integer-combination minimality.
   This dissolves BOTH of the field's current walls simultaneously IF the "mirrored-cut" and
   "spanning-tree" constructions can be made rigorous from scratch — a genuinely different
   framing, far from the field's layer-cake/(PM)/interlacing machinery, exactly as requested.
2. The prefix-partial-sum induction (x_2+x_4+...+x_{2k} ≤ dyadic tail) as a backup/independent LB
   route if the graph-tree argument is hard to reconstruct.
3. (Weaker, secondary, explored before finding the above) A "joint exact-recursion" reframing:
   D_n = 2D_{n−1}+1 suggests running Lemma A and Lemma B as ONE two-sided induction sharing the
   mid-scale truncation split — largely superseded by opening 1, which needs no induction on n at
   all for the UB (pure pigeonhole) and reduces the LB to one integer-minimality fact for the
   dyadic case.

### Candidate technique(s)
- Pigeonhole on subset sums (2^{n+1} subsets of [0,1] values, D_n = 2^{n+1}−1 gaps) — a clean,
  standard combinatorial counting argument, technique name "pigeonhole" (present in KB and in the
  crux corpus's `pigeonhole` subtopic across all three domains).
  - Graph/multigraph spanning-tree + bipartite 2-coloring argument (excess-edges-over-vertices ⟹
  a tree component exists) — "graph-theory-and-connectivity" / "invariants-and-monovariants" style
  crux, standard technique (n+2 vertices, n+1 edges ⟹ some component is a tree).
- Superincreasing/binary-uniqueness minimality (nonzero {−1,0,1}-combination of a superincreasing
  sequence has absolute value ≥ smallest element) — related to our own certified **L4** min-pairing
  identity and the "superincreasing key" already used in `induction-peel.md` §3 ("2^n = 1 + sum of
  smaller"), but applied as an INTEGER-VALUE argument instead of a layer-cake/measure argument.

### Cheap-kill candidates
- Before committing a full build round to opening 1, do a fast numeric check (< 30s, Fraction
  arithmetic, n ≤ 4): simulate the claimed XY mirroring strategy on a handful of random Liu
  partitions A and verify it actually achieves G ≤ min_{S,T} |Σ(S)−Σ(T)| as claimed (this
  construction is NOT verified by us — the PDF sketch is compressed and elides how "any part of S
  beyond the matched prefix" is handled, exactly the kind of bookkeeping trap that bit round 2's
  MATCH move). Likewise numerically verify Δ(1,2,4,...,2^n) = 1 (trivial, but worth confirming the
  ε∈{−1,0,1}^{n+1} minimization is over ALL of them, not a restricted subset) and separately verify
  the graph/tree claim (build the specific multigraph for a random XY play against dyadic A at
  n=3,4 and check some component actually is a tree and that |Σ(S)−Σ(T)| for that component's
  bipartition really is ≤ G).
- If the mirrored-cut construction turns out to need genuinely n cuts of specific fractional
  lengths that don't obviously exist as valid segment subdivisions (i.e. if "pair off S and T into
  equal segments" requires cutting MORE finely than the claimed cut budget), that is an immediate
  kill — check the cut-count arithmetic first (source claims XY needs only n−1 cuts when T≠∅,
  which is a strong, checkable, specific claim).

### Knowledge-base entries to use
- Pigeonhole principle (general technique, likely present in `knowledge_base.md`'s combinatorics
  section — recommend the outliner re-scan for the exact entry name).
- Graph/tree existence from edge-vertex count (a spanning-forest / cycle-rank argument) — check
  `knowledge_base.md` for a named "excess edges force a cycle / component with fewer edges than
  vertices is a tree" entry.
- Our own certified **L0-L2, L4** (claiming lemma, order-irrelevance, alternating-sum identity,
  min-pairing/adjacent-cancellation) are directly reusable: the mirrored-cut UB construction's
  "equal segments cancel in the alternating sum" step is exactly L4's adjacent-pairing-cancels-at-
  zero-cost fact, already certified — this can be imported rather than reproven.

### Analogous past problems (cruxes)
Re-searched `games-and-strategy` and `pigeonhole` subtopics in both `combinatorics` and
`number_theory` for a genuine pigeonhole-on-subset-sums + spanning-tree combination; found
individual pigeonhole-on-subset-sum cruxes (generic Erdős–Ginzburg–Ziv-style) but none combining
it with a spanning-tree/bipartite argument on a claiming game. **No strong match — the mechanism
above appears to be a genuinely specific construction for this problem, not a templated crux move
from the corpus.** Do not force a match.

### Prior progress
Unchanged from `current.md`: LB residual narrowed to Case B (k_C=0) reduced to (CB), numerically
confirmed, open; k_C≥1 aggregate open. UB (Lemma B branch inequalities) untouched since round 4,
and the official source's explicit counterexample (n=5, all 32 branches of top-two-greedy fail)
strongly suggests induction-peel's Lemma B as currently scoped (MATCH/BISECT restricted to the two
largest parts) may not be salvageable in that form — the true UB strategy needs whole-subset
mirroring (opening 1), not a two-part local rule.

### Dead ends (do not retry)
All previously recorded field dead ends stand (per `current.md`'s KNOWN-FALSE list and
`/tmp/memory/math-explorer.md`): averaging/randomized/huffman UB, cut-count cap on C, pointwise
per-level charging, smoothing-toward-cascade, β-relabeling as a "new" opening (confirmed pure
relabeling, round 3 rule). **Newly reinforced by the official source (independent confirmation,
not just our own numerics):** any XY strategy that only ever acts on the CURRENT two largest
pieces (match-or-bisect-the-top) is refuted — n=5 explicit counterexample with ALL 32 execution
branches failing, not just some.

### Small-case / intuition notes
- The pigeonhole bound 2^{n+1} subsets vs D_n=2^{n+1}−1 gaps is EXACT — it is the direct source of
  the 2^{n+1}−1 in the answer's denominator, unifying "why 2^{n+1}−1 and not some other constant"
  in one line, unlike the field's current derivation which reaches D_n only via the recursive
  peeling structure. This is a strong sign the pigeonhole framing is the "intended" structure
  behind the closed form, not a coincidence.
- Conjectural (unverified by us): Δ(A) for non-dyadic A is generically LARGER than what dyadic
  achieves is false in general — Δ is a min over exponentially many sign patterns, so generic A
  can have Δ(A) forced small by adversarial near-cancellations; the source's uniqueness remark
  (dyadic is the unique Liu optimum) is consistent with Δ(A) < 1/D_n for every non-dyadic A, but we
  have not verified this ourselves.
