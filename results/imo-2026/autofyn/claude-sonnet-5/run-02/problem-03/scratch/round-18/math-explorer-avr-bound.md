## imo-2026-03 (lens: fresh technique for the A(R'_{>v}) bottleneck)

### Precise restatement of the target (verified by re-reading Theorem 32 Step 4)
Fix level $m=n-2$. $R'$ is any legal refinement of the $m$-ladder tail
$\{p_3,\dots,p_{n+1}\}$ (total $s$), $v\in(0,s)$ a threshold. Write
$u_{R'}$ for the odd-parity indicator, $A(R'_{>v})$ the alternating sum of
the sub-multiset exceeding $v$. **Key reformulation I verified myself and
that is NOT spelled out explicitly in the approach file**: since every
element of $R'_{>v}$ exceeds every element of $R'_{\le v}$, $R'_{>v}$ is
literally the **top-$k$ prefix of $R'$ sorted descending**, where
$k=|R'_{>v}|$. So $A(R'_{>v})=L_1-L_2+L_3-\cdots\pm L_k$ is a **partial
alternating (prefix) sum of the sorted sequence**, not an integral object —
this is a purely rank-combinatorial quantity. Elementary fact (I verified):
the odd-length partial sums $g_1\ge g_3\ge g_5\ge\cdots$ are decreasing and
the even-length ones $g_2\le g_4\le\cdots$ are increasing, both sandwiched
by $g_1=L_1=\max(R')$ — this reproduces the already-certified vertex-max
fact $\max_{R'}A(R'_{>v})=q_1^{(m)}$ (top piece of the $m$-ladder) from a
one-line argument, no LP machinery needed. Confirms round-15/16's finding
that this crude ceiling is real but too weak; it is not new information,
but it is a much cheaper derivation of the same fact worth citing instead
of re-deriving via vertex-minimum-theorem machinery.

What Theorem 32 Step 4 *actually* needs is **not** a context-free bound on
$A(R'_{>v})$ alone — it needs a **lower bound on the middle-band integral**
$I_1=\int_{v_2}^{v_1}u_{R'}$ (equivalently an *upper* bound on
$A(F_2\cup G')$, i.e. on $\Psi(v_2)$ from above), for the *actual* legally
coupled $(v_1,v_2,P,R')$ arising from a single legal split of $p_1$. This
is a genuinely joint/coupled inequality, not an independent single-variable
extremal fact — flag this precisely to the outliner, since "bound
$A(R'_{>v})$" as a standalone slogan is a simplification of what's really
required.

### Distinct openings (fresh, not yet tried per current.md/rules)
1. **Direct strong induction on $m$ stated purely on the truncated
   quantity.** Define $C_m(w):=\sup A(R_{>w})$ and (separately) the
   *coupled* quantity actually needed, $D_m(w_1,w_2):=\sup A(F_2\cup G')$
   over legal splits with $F_2,R'$ tied by $F$'s own mass conservation.
   Peel the $m$-ladder's own top piece $q_1$: if $q_1$ untouched,
   $R_{>w}=\{q_1\}\cup(\text{tail})_{>w}$ for $w<q_1$, and by
   `sharp-dominant-removal-identity`, $A(R_{>w})=q_1-A(\text{tail}_{>w})$ —
   an exact recursion linking $C_m$ to $C_{m-1}$ (or its dual, a *floor* on
   the tail's truncated sum, which is again the "need a floor and a ceiling
   simultaneously" recursive shape flagged as the historical wall in
   rounds 2–5). If $q_1$ IS cut, need `peel-decomposition-identity`/Lemma 25
   recursively. **Caution — numerically checked, this is likely to hit the
   SAME two-sided-induction wall** (see below); still worth trying since it
   has never been set up explicitly as an induction on this exact object
   rather than via Proposition-30-style peel/truncation.
2. **Constrained vertex-maximization** (new, not yet tried per approach
   file's own diagnosis, which only tried the *unconstrained* max):
   maximize $A(R_{>v})$ subject to the inductive floor $A(R)\ge f(m)$
   (=1 in unnormalized ladder units, i.e. $1/D_m$ normalized) added as an
   extra linear constraint on the same polytope that `vertex-minimum-theorem`
   already triangulates — by LP theory the constrained optimum is still at
   a vertex of the intersection. **I tested this numerically (see below)
   and it does NOT sharpen the bound**: the floor $A(R)\ge f(m)$ is so weak
   relative to typical values of $A(R)$ that it barely restricts the
   maximizer, so $\sup A(R_{>v})$ under the floor constraint is still
   $\approx q_1$ (top piece) at every $n$ tested. **This is a genuine,
   cheap negative finding — do not re-try the plain "add the floor as an
   LP constraint" idea as stated; a tighter, joint (not just floor-added)
   constraint set would be needed.**
3. **Rank-counting bypass via prefix-sum monotonicity + explicit charge
   argument** (genuinely different vocabulary from the integral/alternating-
   sum machinery used everywhere else in the population): since
   $A(R'_{>v})=g_k(R')$ is a partial alternating sum, and $R'$ arises from
   splitting a *specific* geometric ladder tail, try bounding $g_k(R')$ via
   a **charging/pairing argument on individual cuts** (in the spirit of
   crux `aimo-0388`'s pairing of sorted sequence entries, and `aimo-0146`'s
   exchange-smoothing of a weighted sum of a sorted sequence under a sum
   constraint) rather than via the integral identities. Concretely: each
   cut Xiang Yu makes on a tail piece either (a) increases $k$ by 1 (an
   extra fragment crosses above $v$) or (b) leaves $k$ unchanged — charge
   each cut's effect on $g_k$ directly and bound the total charge, rather
   than going through $u_{R'}$'s integral form. Not attempted by any
   approach on file; may or may not evade the two-sided-induction wall, but
   it is a structurally different proof vocabulary (combinatorial charging
   vs. integral identity), satisfying the "genuinely new mechanism" bar.
4. **Try the certified Half-Dominance Split Bound (Theorem 29) directly on
   the whole $F\cup G'$ before splitting via Lemma 25** — I checked this by
   hand: $\mathrm{Total}(F)=p_1$ exactly (mass conservation, $F$ refines
   $p_1$ in full), and $\max(G')=p_2=p_1/2$, so Theorem 29's hypothesis
   $\max(R)\le M/2$ holds with **equality** when $M=\mathrm{Total}(F)=p_1$,
   $F_2=F$, $R=G'$ — giving $A(F\cup G')\le p_1-A(G')=p_2+A(R')$
   *unconditionally, with no case split at all*. This is a genuine, cheap,
   previously-unexploited fact, but it is an **upper** bound on
   $A(F\cup G')$, the wrong direction for Claim B's lower-bound target — so
   it does not directly close the gap, but it may be useful as a
   consistency/sharpness check (it pins the extremal case) or repurposed
   for the upper-bound front (`lp-duality-certificate`) if that front ever
   needs an upper bound on this exact configuration. Flagging as a checked,
   documented fact rather than a route to the lower bound.

### Cheap-kill candidates
- None that close the gap outright; item 4 above is a cheap 3-line
  unconditional fact worth recording even though it doesn't resolve Claim B
  (wrong direction), and item 2's numeric refutation is a cheap kill that
  prevents wasted builder effort on the naive constrained-LP idea.

### Candidate technique(s)
- Two-sided/coupled strong induction directly on the pair
  $(C_m(w),\,\text{floor}_m)$ tracked jointly (item 1) — highest expected
  value but carries real risk of re-hitting the historical "need floor and
  ceiling simultaneously" wall (rounds 2–5); if attempted, the outliner
  should explicitly budget a round to detect this early via a numeric
  check of whether the induction step's required inequality is itself
  self-referential before committing full effort.
- Charging/pairing argument on individual Xiang-Yu cuts (item 3) — the
  most genuinely novel vocabulary shift; recommended first target since it
  has not been tried in any form and the crux corpus (`aimo-0146`,
  `aimo-0388`) supports pairing/exchange-smoothing as viable for
  "bound a functional of a sorted, constrained sequence."

### Knowledge-base entries to use
- `sharp-dominant-removal-identity`, `dominant-element-removal-identity`
  (for peeling $q_1$ in item 1's recursion).
- `vertex-minimum-theorem` / `exchange-smoothing-vertex-maximization`
  (for item 2, though numerically shown insufficient in its naive form).
- `truncated-alternating-sum-floor` and `upper-truncation-identity`
  (already certified, the algebraic backbone any new attempt should still
  reduce to / be consistent with).
- `half-dominance-split-bound` (Theorem 29) — new application found (item
  4), unconditional but wrong-direction for this front.

### Analogous past problems (cruxes)
- `aimo-0146` (combinatorics, `extremal-principle`/`double-counting`):
  bound a weighted sum of a sorted, sum-constrained sequence via
  exchange-smoothing toward high-coefficient positions — genuinely
  analogous in *shape* (bounding a rank-weighted functional of a sorted
  sequence under a total-mass constraint) though the target problem here
  (2026-03) is continuous/game-theoretic rather than a fixed finite graph
  degree sequence; the transplant is a technique analogy, not a literal
  reduction. Worth reading in full if item 3 is pursued.
- `aimo-0388` (combinatorics, `telescoping-and-summation`): pairs
  consecutive sorted entries so the difference telescopes to non-positive
  gaps plus isolated boundary terms — same flavor as the already-certified
  `odd-run-reduction-lemma`/`pair-cancellation-identity`, confirming the
  existing machinery is the right family; not a source of new technique.
- No crux found that specifically handles a *truncated/prefix* alternating
  sum under a superincreasing/geometric structural constraint — this
  precise combination appears to be genuinely novel to this problem, not
  covered by the corpus (checked `extremal-principle`,
  `size-bounding-and-descent`, `inequalities-SOS-and-convexity` subtopics
  for "prefix"/"truncat"/"threshold" keywords, no close match beyond the
  two above).

### Prior progress
Front 1 (greedy-halving-adversary): Theorem 32 closes $\ell(F)=2$ sub-case
(b) unconditionally for $v_1\le s$ (Theorem 32(i)); the complementary
$v_1\in(s,p_2)$ range (Theorem 32(ii)) reduces exactly to the standing
"upper bound on $A(F_2\cup G')$" crux (equivalent, per Proposition 30, to a
bound on $A(R'_{>v_2})$) — confirmed from 4 independent angles across
rounds 15–17 to be THE single bottleneck (closes Target B, Theorem 32(ii),
and items 1/2/3 of Claim B simultaneously if resolved).

### Dead ends (do not retry)
- The plain "unconstrained vertex-max of $A(R'_{>v})$ alone" ceiling
  ($=q_1$, top piece) is confirmed (again, independently, by my own numeric
  probe) too weak — already on file, re-confirmed here.
- **New this round**: adding the inductive floor $A(R')\ge f(m)$ as a
  single extra LP constraint to the vertex-maximization of $A(R'_{>v})$
  does NOT sharpen the bound — numerically the floor is far too weak
  relative to typical $A(R')$ values to move the constrained maximum below
  $q_1$ at $m=2,3,4,5$ (checked with 60k–80k random legal-refinement trials
  per $m$, `/tmp/probe_arv3.py`). Do not propose this exact idea again
  without a strictly tighter joint constraint.
- Half-Dominance Split Bound applied directly to $F\cup G'$ gives an
  unconditional *upper* bound $p_2+A(R')$ — correct but wrong-direction,
  does not close Claim B; don't expect it to close the lower-bound target
  without further work repurposing it.

### Small-case / intuition notes (all conjecture/numeric, not proof)
- Verified numerically (Fraction-free float random search, $m=2,3,4,5$,
  60k–80k trials, cut budget capped at $m$): the inductive floor
  $A(R)\ge f(m)=1$ (unnormalized units, $=1/D_m$ normalized) holds with
  worst observed values $\approx1.0$–$2.0$ (consistent, never violated) —
  corroborates but does not re-prove the already-certified Claim (A)/(B)
  floor.
- The maximum of $A(R_{>v})$ over legal refinements, for $v<q_1$, is
  numerically $=q_1$ at every $m$ tested (matches the certified exact
  vertex-max closed form from Theorem 31's own writeup) — confirms no
  slack is being missed by my probe, i.e. the crude ceiling really is
  exactly $q_1$, not an artifact of insufficient sampling.
- No numeric evidence found (in the time available) for a sharper
  *joint* bound; a targeted search directly minimizing the coupled
  quantity $A(F\cup G')$ over $(v_1,v_2,P,R')$ with $v_1\in(s,p_2)$ enforced
  and mass conservation to $p_1$ enforced, to inspect the true worst-case
  witness's $(R',v_2)$ structure, was not completed this round (time-boxed)
  — recommend this as the fastest next diagnostic: find the exact extremal
  witness for Theorem 32(ii) numerically (exact-Fraction, small $n$) and
  read off whether its $R'$ is the same "leave $q_1$ untouched, halve
  everything else" cascading vertex family already characterized, which
  would suggest the needed bound has an explicit closed form reachable by
  direct computation rather than a fresh general inequality.
