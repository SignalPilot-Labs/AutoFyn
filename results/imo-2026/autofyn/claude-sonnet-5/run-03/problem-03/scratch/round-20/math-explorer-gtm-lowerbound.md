## imo-2026-03 — lens: general GCH(k) matching lower bound

### Precise target
GCH($k$): for $R$ finite multiset, $\max(R)\le\mathrm{cap}=2^{k-1}$, $|R|\le k+1$,
$\mathrm{sum}(R)=S\in[2^k,2^k+1)$, prove
$\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ (equiv. $\mathrm{OddSum}(R\cup\Gamma_{k-1})
\ge(S+2^k)/2$), $\Gamma_{k-1}=\{2^{k-1},\dots,2,1\}$. Achievability (tightness) is
fully proved for all $k\ge2$ (certified, split by $k=2$ vs $k\ge3$, see
`lemmas/gch-achievability-witness-k-geq-3.md` +
`lemmas/sharper-odd-residual-and-k2-cardinality-half-sum.md` Lemma 2). Only the
matching lower bound over *every* feasible $R$ remains open for $k\ge3$ ($k=2$ is
closed, Lemma 2, exhaustive casework).

### Distinct openings (candidate mechanisms)

1. **Two-parameter coupled-family induction (the diagnosed but unattempted fix).**
   Round 18's diagnosis (source file lines ~5526–5561) found the naive
   single-parameter induction on $k$ fails because peeling the tied top
   pair/cap element lands on a residual instance with the *same* cap
   $2^{k-1}$ but a *smaller* $\Gamma$-index $j=k-2$ — i.e. cap is not
   $2^{j}$-shaped relative to the new $j$, so it is not literally a smaller
   GCH($k-1$) instance. The proposed fix (never attempted) is a genuinely
   general family $\mathrm{GCH}(j,\mathrm{cap},b;S)$ with cap **frozen** at
   the *original* $2^{k-1}$ while the $\Gamma$-index $j$ and count budget
   $b$ both decrease by one at each peel. This is a coupled-induction
   structure, not a single recursive shrink — see opening 4 below for a
   structural template from the crux corpus that matches this exact shape.

2. **LNI-based vertex/shape classification, made rigorous (reduces the
   continuous optimization to a genuinely finite combinatorial object).**
   I worked out (not in any file yet) the precise mechanism Lemma LNI
   licenses: any two **distinct-valued**, both-interior ("free") coordinates
   of $R$ with opposite rank parity admit a strictly improving
   sum-preserving perturbation (Lemma LNI, proved). Two **equal**-valued
   free coordinates are *not* covered by LNI's hypothesis ($r_i\ne r_j$
   required) — I checked numerically (exact `Fraction`, $k=3$) that a tied
   pair genuinely is a local min in the natural symmetric slice (perturbing
   $r\pm t$ increases AltSum in *both* directions, since the two labels are
   interchangeable so the local behavior is automatically an even function
   of $t$, not the odd/linear behavior LNI's rate formula describes for
   *distinct* free coordinates) — so ties are correctly exempted, not a
   hidden saddle. Consequence: at any LNI-stable configuration, **any set
   of $\ge2$ distinct-valued, non-Γ-tied free coordinates would contain an
   adjacent (in sorted order) opposite-parity distinct pair** — i.e.
   genuinely free coordinates can only occur as (a) Γ-level ties
   (multiplicities $m_0,\dots,m_{k-1}\ge0$, handled by the already-certified
   Lemma BCF: even $m_j$ contributes 0, odd $m_j$ contributes $\pm2^j$ by
   parity of the count above it), or (b) **at most one additional "free
   block"** consisting of $t\in\{0,1,2\}$ copies of a single new value $r$
   (by TPC, any even count of identical free copies is equivalent to $t=0$,
   any odd count $\ge3$ is equivalent to $t=1$ by peeling matched pairs — so
   WLOG $t\in\{0,1,2\}$ suffices). **This turns GCH($k$)'s lower bound into
   exactly the finite-per-$k$ integer-vector claim the source file already
   names** (round 19, "the discrete combinatorial statement about integer
   vectors $(m_0,\dots,m_{k-1})$"): minimize, over all integer vectors
   $(m_0,\dots,m_{k-1})\ge0$ with $\sum m_j\le k+1-t$ and $t\in\{0,1,2\}$,
   feasibility of a forced leftover value $r\in(0,\mathrm{cap}]$ from the
   sum constraint, the resulting $\mathrm{AltSum}$ (BCF sum over odd-$m_j$
   levels, plus the free block's forced $\pm r$ contribution by its rank
   position) — and show it is always $\ge1$. **This reduction itself is not
   yet written up or certified** — it needs (i) a careful statement that the
   only rank-crossing "walls" a minimizer can be pinned against are exactly
   $\{0,\mathrm{cap}\}\cup\Gamma_{k-1}$-values (i.e. the polytope's vertices
   really are of this form, not just a necessary condition from one
   first-order lemma — a full compactness + boundary argument, not just
   LNI's interior first-order condition, is needed to rule out e.g. a
   3-or-more-distinct-value free block none of whose members happen to be
   adjacent-opposite-parity pairwise — I did NOT find a gap in this for
   $\ge3$ distinct free values, since among $\ge2$ distinct values some
   adjacent pair in sorted order must have opposite parity generically, but
   this needs to be stated and proved as a clean combinatorial fact, not
   assumed), and (ii) the actual finite verification of the resulting
   integer-vector claim for general $k$ (still combinatorial, but now
   genuinely finite and stateable without continuous optimization).

3. **Direct exhaustive/computer-verifiable route once (2) is formalized.**
   Once the reduction to integer vectors $(m_0,\dots,m_{k-1},t)$ is
   established as a *theorem* (not just a diagnosis), the residual claim
   is a concrete Diophantine-flavored statement about binary-weighted
   partial sums and parities — amenable to an explicit combinatorial
   (not computer-search) induction on $k$, since $m_j$'s parities and the
   $C_j$ (count-above) parities are literally bits of a related integer.

4. **Crux-corpus structural template: `aimo-0377`.** IMO-style problem
   "$\sum_{i=1}^n(-1)^{s(3i)}>0$" ($s(k)=$ binary digit-sum). Its Solution 1
   crux move (subtopic `size-bounding-and-descent`, technique: "peel off
   the least-significant binary digit to split a signed digit-parity sum
   into two sums over the halved index range") is proved via a
   **strengthened, coupled triple induction**: instead of inducting on the
   single target sum, it simultaneously tracks three related sums (over
   the three residue classes mod 3), because the digit-peeling recursion
   *permutes* the classes into each other. This is structurally the exact
   shape opening 1 above calls for: GCH($k$)'s naive single-object
   induction fails because peeling changes the object's "type" (cap-vs-level
   ratio); a coupled family of 2–3 related statements (e.g. GCH at level
   $j$ with cap fixed at $2^{k-1}$, for $j=0,\dots,k-1$, each reducible to
   the next by one digit-peel) is the natural fix, directly analogous to
   `aimo-0377`'s residue-class coupling. A second crux from the same
   problem ("pair each number with its bitwise complement inside a
   $2^m$-block so the two digit-sum parities are opposite and cancel
   exactly") is essentially TPC/BCF's own mechanism, already independently
   discovered and certified in this problem's lemma set — a genuine
   convergent confirmation that this family of technique (complementary-pair
   cancellation + coupled digit-peeling induction) is the right one for
   base-2 alternating-parity sums generally.

### Cheap-kill candidates
- None new beyond what's certified (the multi-restart-SLSQP cheap-kill is
  already standard here and passed again, see below).
- A genuine structural cheap-kill worth running before committing to
  mechanism (2): check whether the reduction "free block has size $t\le2$"
  can be falsified by a direct search allowing $t=3,4$ distinct-valued free
  blocks (not just repeated copies) at small $k$ — I did not find a
  violation in the numeric optimizer output (the observed minimizer shape
  at every tested $(k,S)$ is exactly chain+pair or chain+single, never
  $\ge2$ distinct free values), consistent with, but not proof of, the
  reduction in opening 2.

### Knowledge-base entries to use
- No new `knowledge_base.md` entries beyond what prior rounds already
  cited (this problem's technique base is now almost entirely internal
  certified lemmas — TPC, BCF, LNI). Worth checking `knowledge_base.md`'s
  generic "extremal principle / vertex of a polytope" and "parity
  invariant" entries if present, to frame opening 2's reduction in
  standard vertex-enumeration language — I did not find anything beyond
  what the file already self-derived.

### Analogous past problems (cruxes)
- **`aimo-0377`** (best match, `number_theory`/`size-bounding-and-descent`
  + `modular-arithmetic-and-CRT`) — binary digit-parity alternating sum,
  proved by (a) digit-peeling recursion, (b) a **coupled multi-statement
  induction** because peeling permutes related objects into each other,
  (c) complementary-pair cancellation. Directly analogous in both the
  object type (alternating sum over a set built from binary structure)
  and the exact obstruction (a single-parameter induction doesn't close
  because peeling changes the object's type) — strongly recommend the
  outliner read this crux's Solution 1 in full
  (`past_problems_database.json`, `problem_id="aimo-0377"`) as a template
  for constructing GCH($k)$'s missing coupled family.
- Other binary/digit-sum cruxes found (`aimo-0027`, `aimo-0317`,
  `aimo-0382`) are more loosely related (digit-count/valuation arguments,
  not alternating-parity sums) — not recommended as primary templates.

### Prior progress
- Achievability (upper witness): **fully closed for all $k\ge2$**
  (corrected, split-by-$k$ form), certified.
- Lower bound: closed for $k=2$ (exhaustive casework, certified, Lemma 2).
- For $k\ge3$: reduced via certified Lemma BCF to a finite-per-$k$ integer
  multiplicity-vector claim; numerically corroborated $k=3,4,5$ (prior
  rounds) and now also **$k=6,7,8$** (this round, `scipy` multi-restart
  `SLSQP`, `LinearConstraint`+`Bounds`, 25 restarts per $(k,\rho)$,
  $\rho\in\{0.001,0.1,0.3,0.5,0.7,0.9,0.99\}$): minimum found is
  $1.0000000000\ldots$ (machine-precision $1$) at every one of the 21
  new tested points, zero violations — consistent with, not proof of,
  the conjecture. (Not exact-`Fraction` search — a full exact-arithmetic
  vertex enumeration at $k=6,7,8$ was not completed this round; time was
  spent instead on the structural reduction in opening 2, which is the
  higher-value contribution.)
- New structural finding this round (opening 2): a candidate rigorous
  reduction of the lower-bound claim to integer vectors
  $(m_0,\dots,m_{k-1},t)$, $t\in\{0,1,2\}$, via Lemma LNI + Lemma TPC —
  not yet written up as a lemma or verified in full, but the mechanism
  (why free blocks collapse to size $\le2$) is explained above and is a
  concrete, checkable claim, distinct from (sharper than) the source
  file's own looser statement of "the discrete combinatorial claim."

### Dead ends (do not retry)
- Naive single-parameter induction on $k$ (peel top tied pair/cap,
  recurse into $\mathrm{GCH}(k-1)$ directly): **diagnosed as
  structurally broken**, not just unproved — the residual cap does not
  shrink to match the residual $\Gamma$-index (round 18, certified
  diagnosis). Do not re-attempt this exact single-parameter form; use the
  coupled/frozen-cap family (opening 1) instead.
- Believing a tied pair $\{r,r\}$ is an LNI-violating saddle: checked
  numerically this round (exact `Fraction`, $k=3$) and confirmed **not**
  a gap — ties are correctly outside LNI's hypothesis ($r_i\ne r_j$), and
  perturbing a tied pair in either direction strictly *increases* AltSum
  (even function of $t$ by label symmetry), so it is a genuine local min
  as the source file's construction assumes. No correction needed here.

### Small-case / intuition notes (conjecture, not proof)
- The true minimizer at every tested $(k,\rho)$ has shape either
  chain+pair ($\{2^{k-1},\dots,4,r,r\}$) or chain+single depending on
  parity considerations at the boundary $\rho\to0$ vs interior — matches
  the certified achievability witness exactly, no other shape observed.
- The conjecture appears robustly true (no counterexample at any tested
  $k$ up to 8, any tested $S$), so the missing piece is a *proof
  technique*, not a wrong conjecture — opening 2 (LNI-based finite
  reduction) combined with opening 4's coupled-induction template
  (`aimo-0377`) is the most promising concrete next step; opening 1 is
  the same target restated in the source file's own terms.
