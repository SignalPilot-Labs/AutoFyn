## imo-2026-03

Answer to prove: **c(n) = 2^n / (2^{n+1} − 1)** (n=1: 2/3, n=2: 4/7, n=3: 8/15).
Find-all/compute: need BOTH lower bound (LB strategy) AND upper bound (XY strategy).

Shared reductions used by ALL three approaches (build these as certified lemmas first,
cache in `lemmas/`):
- **L0 Claiming lemma** — greedy "take largest" optimal for both ⇒ first player (LB) gets
  the odd-rank sum of the descending-sorted final multiset. Exchange argument. GAP.
- **L1 Order irrelevance** — value depends only on the final MULTISET, not positions on
  the stick (immediate from L0). So the whole problem = one-shot multiset game: LB picks a
  multiset of ≤ n+1 parts summing to 1; XY refines with ≤ n cuts; value = odd-rank sum.
  This is a big simplification the explorers only half-stated; make it explicit.
Numeric check this round: brute force confirms for LB=dyadic {1,2,4}/7, the min odd-rank
sum over ALL XY refinements = exactly 4/7. Lower-bound lemmas are on solid ground.

Field of three rival approaches (kept FAR apart in framing):

induction-peel: new
Target: c(n)=2^n/(2^{n+1}−1), both bounds.
Technique: strong induction on n, peeling LB's largest piece; self-similar dyadic
  (rest of G_n = scaled G_{n−1}); scalar recurrences for LB/XY shares.
Open gaps: L0; Lemma A (lower-bound recursion: superincreasing forces small parts to even
  ranks / IH on scaled rest); Lemma B (upper-bound recursion: XY match-vs-bisect min caps
  LB, equalization pins dyadic). Lemma B is the hardest.
Cases: n=1 base (done by explorers); #XY cuts on top piece 0..n; partitions with <n+1
  parts or tied largest.
Watch: match-only is WRONG ({0.9,0.1} → 0.9); min over match AND bisect essential.
  Homogeneity/scaling of the sub-game (mass (2^n−1)/D_n, not 1).

alternating-sum-potential: new
Target: c(n)=2^n/(2^{n+1}−1), both bounds.
Technique: reframe entirely via potential S = Σ(−1)^{i+1}p_(i); LB total=(1+S)/2. Game
  value in S = 1/(2^{n+1}−1) = smallest dyadic piece. Monovariant/telescoping control of
  S under cuts — no induction on n, no explicit interleaving.
Open gaps: L0; L2 potential identity (easy); Lemma C (S ≥ 1/D_n for every refinement of
  dyadic — reserve/telescope); Lemma D (XY match-and-carry-with-bisect contracts the
  reserve by ≤1/2 per cut ⇒ S ≤ 1/D_n after n cuts for ANY partition). Lemma D hardest.
Cases: XY cuts top vs small part; match vs bisect per cut; <n+1 parts; ties; slivers.
Watch: telescoped form S=p_(1)−Σgaps needs ODD final count — track parity m=k+#cuts.
  The per-cut contraction must be a real inequality, not "S contracts".

explicit-certificate: new
Target: c(n)=2^n/(2^{n+1}−1), both bounds.
Technique: explicit optimal object each side + direct order-statistics inequality; no
  induction, no abstract potential. Lower: dyadic + Hall/marriage injection of the n small
  parts into distinct even ranks. Upper: XY explicitly splits largest LB part(s) into
  interleaving sub-pieces + majorization/Schur-convexity cap.
Open gaps: L0; Lemma E (Hall inequality |{final pieces ≥ g_j}| fits the available odd
  ranks for every XY refinement, incl. small-part cuts + slivers); Lemma F (a) prove XY
  "concentrate cuts on largest, don't spread" is optimal; (b) explicit split filling even
  ranks for arbitrary partition; (c) majorization cap = 2^n/D_n. Lemma F hardest.
Cases: XY concentrated/spread/small-part/sliver/fewer cuts (lower); LB dominant-part
  (bisect), tied (cancel), <n+1 parts, near-geometric (match) (upper).
Watch: "invariance of LB total under any top split" holds ONLY while interleaving forced —
  that IS the content, don't assume it. "Concentrate don't spread" is unproven (obligation).
  Slivers sort to GLOBAL bottom — rank arguments must be sliver-robust.

Why these three are far apart (not one wall): induction-peel recurses on n; potential
works with the scalar invariant S abstractly, never peeling n; explicit-certificate builds
concrete Hall/majorization certificates with no recursion. They share ONLY the L0/L1
foundation (which the n=2 brute force supports). If one bound's mechanism stalls, the
other two attack it by a genuinely different route.

Recommended build set: all three new approaches (they need a first build pass to seed
Elo and surface which bound-mechanism closes fastest). If forced to prioritize:
induction-peel and alternating-sum-potential first (cleanest routes to a full closed
form); explicit-certificate as the diversity hedge. The lower-bound lemmas (A/C/E) look
tractable and numerically confirmed; the upper-bound lemmas (B/D/F) are the shared crux —
worth a focused build. Note for reviewer: these three files are written but NOT yet
registered (register_approach is the outline-reviewer's tool) — please register all three.
