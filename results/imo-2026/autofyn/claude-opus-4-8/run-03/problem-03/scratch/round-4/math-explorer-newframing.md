## imo-2026-03

**Lens:** hunt for a whole-problem framing genuinely far from the layer-cake potential S (L2–L4)
that could close BOTH the lower-bound overlap-W cap and the upper-bound Xiang-Yu construction
with a single argument. Verdict up front: I could not find one that escapes the shared crux
without importing equivalent content — the alternating-sum-of-sorted-values object forces the
layer-cake identity (it IS the natural integral representation of S, not an arbitrary choice: L3
is essentially definitional, not a lemma one can route around). What follows are the candidate
orthogonal framings I actually tested, with their concrete obstruction, plus one genuinely new
*technique* (not just reframing) worth putting on the table.

- **Distinct openings surfaced (with verdicts):**
  1. **Discrete binary-tree / node-counting reformulation.** The numerology c(n) =
     2^n/(2^{n+1}−1) = (# depth-n leaves)/(# nodes, depths 0..n) of a complete binary tree is
     suggestive of a purely combinatorial (integer, no measure theory) proof: model dyadic
     refinement as tree-node activation and hope the whole game reduces to a leaf/node ratio
     invariant provable by structural tree induction. **Obstruction, verified:** this requires
     XY's optimal replies to always be tree-respecting bisections, but the upper-bound analysis
     (induction-peel §4) already proved MATCH (splitting a_1 into (a_2, a_1−a_2), NOT a bisection)
     is essential — "pure bisection of the global max fails badly (17–75% of trials exceed
     target)". MATCH is exactly a non-tree-respecting cut. So the naive tree/leaf-count framing
     is refuted by evidence already in the field; a corrected version would need its own
     structure theorem for which cuts are "tree-like enough," which is not obviously easier
     than the current branch-inequality gap. **Not recommended as stated** — record so no one
     re-tries the naive version.
  2. **Complementary-role duality.** Note 1 − c(n) = (2^n−1)/D_n = D_{n-1}/D_n exactly (since
     D_{n-1} = 2^n − 1 by definition of D). This looked like it might give a second, easier
     "recursive" statement about XY's own guaranteed value to induct on jointly with LB's. I
     checked this carefully: because the claiming phase is exactly zero-sum (every one of the
     finitely many final pieces is claimed by exactly one player, total length 1), LB's value
     + XY's-own-maximizing value = 1 is an automatic tautology of any deterministic
     complete-information constant-sum game — it carries **no independent content** and cannot
     be used as a second inductive lever. **Checked and discarded** — do not re-propose "duality"
     framings that only restate c(n)+(1−c(n))=1.
  3. **Self-similar fixed-point on the value functional via compactness.** Formalize
     f(n) := max_A min_B S(B) over the compact set of profiles A (≤ n+1 parts, sum 1); Extreme
     Value Theorem (KB: "Lagrange multipliers / EVT on a compact manifold") guarantees the max
     and min are attained (S is continuous, the profile simplex is compact), so f(n) is
     well-defined and a genuine Bellman/DP recursion f(n) = f(n−1)/(2+f(n−1)) *could* be derived
     if one can show the optimizer A is self-similar (peel one part, recurse on the rest scaled).
     **Obstruction:** proving that self-similar shape is exactly the content of induction-peel's
     Open gap 2 (the branch inequalities / F1 finding: "the value function genuinely depends on
     the whole profile, not just (a_1, sum)"). So this is not independent leverage — it is a
     restatement of the existing open gap in variational-calculus language, with EVT/compactness
     buying only "the max and min exist," which was never in doubt. **Low promise as a
     bypass**, but the EVT framing is legitimate if the outliner wants a cleaner existence
     argument as scaffolding (not a route around the two walls).
  4. **Amortized charging / credit scheme on the cut budget (genuinely new *technique*, not just
     reframing).** The one candidate that is a different *tool* rather than a different *lens*:
     treat XY's ≤(n−1) cuts spent inside Rest as a discrete resource and bound the layer-cake
     overlap W by a credit argument — "each cut used inside Rest can enlarge the odd-overlap
     region W by at most a fixed credit; W's total is capped by (cuts used)·(credit per cut)."
     This is the amortized-analysis / banker's-method idea (crux corpus: aimo-0012's
     merge-pigeonhole-induct-unmerge mechanism, already cited and tried in
     `alternating-sum-potential.md §4` for the **upper-bound** MATCH/BISECT charging — but NOT
     yet tried for the **lower-bound** W-cap (GAP-LB / A-res)). Concretely: has anyone bounded W
     by "at most 1 unit of odd-overlap-measure created per cut spent on Rest, and Rest has only
     n−1−(other cuts) budget left, capping W ≤ (n−1)−(cuts already spent elsewhere)"? This is
     NOT in any of the three live approaches' write-ups for the lower bound — they use the
     induction hypothesis S(Rest) ≥ 1 (a value bound) but never a *cut-count* bound on W
     directly. This is worth flagging to the outliner as an unexplored lever distinct from all
     three current approaches' treatment of GAP-LB/A-res: **bound W by counting XY's remaining
     cut budget, not by measure-theoretic interval bounds** (which are proven too weak per L 15
     in memory / induction-peel §3.3).

- **Candidate technique(s):** amortized charging / credit scheme keyed to cut-count (not measure)
  for the lower-bound overlap cap (opening 4); EVT/compactness only as existence scaffolding, not
  a bypass (opening 3). Tree/leaf-count (opening 1) and role-duality (opening 2) are refuted or
  empty — record as dead ends, do not re-open.

- **Cheap-kill candidates:** none new found. The existing field already has the strong structural
  kills (A0 "at most one large shard," Lemma H "h≥1 ⟹ S≥1", the truncation identity). One
  additional cheap check worth running before investing in opening 4: verify numerically, on the
  40 000-trial GAP-LB regime already generated by induction-peel/global-max-peel, whether
  W / (cuts spent on Rest) stays ≤ a fixed constant (e.g. ≤ 1/2) across all trials — a 10-line
  numeric probe that would validate or kill opening 4 before an outliner commits an approach to
  it.

- **Knowledge-base entries to use:** "Invariants & monovariants" and "Constructive / incremental"
  (Combinatorics section) for the credit-scheme framing; "Extreme value theorem / Lagrange
  multipliers on a compact manifold" only for existence scaffolding (opening 3), not for closing
  a gap. No new KB entry directly supplies a "credit/amortized" theorem by name — it is a proof
  technique, not a citable theorem, so any use must be proven from scratch (per repo rules).

- **Analogous past problems (cruxes):** `aimo-0012` (algebra/combinatorics bin-packing,
  `size-bounding-and-descent`-flavored): "greedy fill... charge the total against per-part
  surplus" and "merge an adjacent pair by pigeonhole, induct, un-merge" — genuinely analogous
  *mechanism* (charge a resource against a count, not a measure) but a different problem
  (bin-packing capacity, not alternating-sum games); already cited and partially used in
  `alternating-sum-potential.md` for the upper bound. I found no crux in
  `games-and-strategy` (searched combinatorics AND number_theory subtopics) or
  `generating-functions` that resembles this specific "cut-then-alternately-claim, guarantee a
  fraction" game — the corpus's games-and-strategy entries are almost all discrete
  pairing/parity/mirroring strategies on graphs or boards, not continuous-interval Stackelberg
  cut games; none is a close analog. **Best 1: aimo-0012** (charging/amortized-merge mechanism,
  for opening 4 only). No other close matches — do not force a match to the games-and-strategy
  subtopic entries surveyed (aimo-0019/0066/0077/0115/0117/0196/0225/0236/0262/0445/0461/0521/
  0560/0596/0631/0653/0663/0746/0766/0854), none share the "cut a continuum then alternately
  claim pieces" structure.

- **Prior progress:** unchanged from `current.md` — answer c(n) = 2^n/(2^{n+1}−1) established
  numerically for n=1,2,3 and proved in full for n=1; L0–L8 certified; both remaining gaps
  (A-res/GAP-LB for the lower bound, branch inequalities for the upper bound) open across all
  three live approaches, both sitting on layer-cake machinery.

- **Dead ends (do not retry):** (a) naive tree/leaf-count framing assuming tree-respecting cuts
  suffice — refuted by the proven necessity of MATCH over pure BISECT; (b) "complementary
  1−c(n)=D_{n-1}/D_n duality" as an independent proof lever — it's a zero-sum tautology with no
  extra content; (c) all prior dead ends already logged in `current.md` (smoothing-extremal,
  Hall's-theorem framing, β-vs-S relabeling) — unaffected by this round's search, still dead.

- **Small-case / intuition notes (conjecture only):** the D_{n-1}=2^n−1 identity is exact algebra,
  not a conjecture, but its *usefulness* as a second inductive statement is nil per opening 2's
  analysis. The tree/leaf-count ratio matching c(n) exactly is a genuine numerical coincidence of
  the recursion D_n=2D_{n-1}+1 with 2^n doubling — it does not, on inspection, encode extra
  combinatorial structure beyond what's already in the D_n recursion itself (confirmed by opening
  1's obstruction: the actual extremal strategy needs MATCH, which breaks the pure-tree picture).
