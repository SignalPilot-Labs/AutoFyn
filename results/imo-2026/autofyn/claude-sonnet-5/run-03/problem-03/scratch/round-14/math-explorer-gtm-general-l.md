## imo-2026-03 (lens: closing GT(m), m>=4 — the two named sub-cases (i) q=1/e>=1, (ii) small-sum GT(k-1) mirror)

- **Distinct openings:**
  1. **Reframe (i) and (ii) as ONE known-but-unclosed generalization, not two
     new problems.** Both sub-cases' targets are strictly below the boundary
     value $2^{k-1}$ (sub-case (i)'s target $2^k-a_1<2^{k-1}$ since $a_1>
     2^{k-1}$ by definition of $q=1$; sub-case (ii) is literally "target
     $<2^{k-1}$" by name). This is exactly the **$G(m,k;V)$ object first
     identified in round 4** ("the natural generalization of $T(m,k)$ to
     arbitrary target $V\in[2^{m-1},2^m]$... proved for $j=0$... left open
     for $V<2^m$ and $j\ge1$, and for $j\ge2$ at any $V$" — see
     `approaches/self-similar-induction-on-n.md` round-4 section, "Current
     best" item 4). Nobody in round 13 connected the two new sub-cases back
     to this old, still-open object; doing so tells the outliner these are
     not extra work items but the SAME single remaining generalization the
     file has carried since round 4.
  2. **A concrete, numerically-and-structurally verified partial mechanism
     for sub-case (ii) when $|D|<m+1$ (room for one more piece):** insert a
     "filler" $f:=2^m-\mathrm{sum}(D)$ to reach $D'':=D\cup\{f\}$ with
     $\mathrm{sum}(D'')=2^m$ exactly (still $|D''|\le m+1$, so the
     **already-certified boundary case of $\mathrm{GT}(m)$ applies**, not a
     circular appeal to the open case), then bound the OddSum change from
     inserting $f$ by $f$ itself. Concluded (see Small-case notes below)
     $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\mathrm{OddSum}(D''\cup\Gamma_{m-1})
     -f\ge2^m-f=\mathrm{sum}(D)$ — closing the not-full-count instance of
     sub-case (ii) essentially for free, *given* the boundary case (which is
     exactly what round 13's Result 2 machinery is trying to establish for
     $m\ge4$ anyway). This turns "prove the small-sum mirror" into "prove
     the boundary case, then get small-sum almost free" for all but the
     full-count sub-sub-case.
  3. **The residual full-count ($|D|=m+1$) instance of (ii) is empirically
     NOT tight** (see numeric notes) — margins of $1$–$5.7$ observed at
     $m=3,4,5$, unlike the not-full-count case where margin $\to0$ exactly
     at the boundary. This suggests the full-count residual is provable by
     literally re-running Round 13's Unified Threshold-Pair-Peeling
     machinery (Result 2) with the target genuinely parametrized by $V$
     instead of fixed at $2^k$: the $q\ge2$ branch trivializes for free
     for ANY $V\le2^k$ (its proof bound $2^{k-1}(q/2+1)$ already exceeds
     $2^k\ge V$, no change needed); only $q=0,1$ need re-deriving with $V$
     threaded through the recursion instead of assuming $V=2^k$ always.
     This is the most promising concrete next step: **generalize Result 2 to
     variable $V\le2^k$**, closing sub-cases (i) and (ii) together as one
     corollary, rather than attacking either sub-case in isolation.
  4. **A crux-corpus analogy supporting the "carry an auxiliary bounded
     companion quantity through the induction" pattern** needed to make a
     variable-$V$ strong induction close (see below) — from `aimo-0377`
     (USA TSTST 2024, digit-sum-parity alternating sums).

- **Candidate technique(s):** Extend the certified **Single-Insertion Lemma**
  / rank-shift machinery (`lemmas/monotonicity-reduction-and-unified-
  threshold-pair-peeling.md`) to a **variable target $V\le2^k$** version of
  the Unified Threshold-Pair-Peeling Lemma; combine with the elementary,
  easily-provable facts $0\le\mathrm{AltSum}(N)\le\max(N)$ (immediate
  induction from the certified Peeling Lemma) to get the filler-insertion
  bound of opening (2). Consider strong induction on $m$ with a
  simultaneously-tracked companion bound (per the `aimo-0377` crux), if the
  bare variable-$V$ recursion alone comes up short by a small margin the
  way Round 4's Case-A circularity did.

- **Cheap-kill candidates:** none found that fully close the gap, but one
  useful pruning: whenever $|D|<m+1$ in sub-case (ii), the gap reduces
  immediately to the (already-targeted) boundary case via opening (2) —
  builders/outliner should not spend effort re-deriving the not-full-count
  instance from scratch; only the full-count sub-sub-case needs new work.

- **Knowledge-base entries to use:** none of `knowledge_base.md`'s
  general-purpose entries were newly implicated beyond what's already cited
  in the certified lemma file (Elementwise Monotonicity, Peeling Lemma,
  Single-Insertion Lemma, Rank-Shift Identity) — this gap is purely
  internal machinery extension, not a new external theorem.

- **Analogous past problems (cruxes):** `aimo-0377` (USA TSTST 2024,
  domain `number_theory`, subtopic `size-bounding-and-descent` /
  `modular-arithmetic-and-CRT`) — proves $\sum(-1)^{s(3i)}>0$ (binary
  digit-sum parity, i.e. structurally an "OddSum vs sign/parity of binary
  digits" statement, very close in flavor to this problem's OddSum-of-a-
  multiset-against-$\Gamma_m$). Its crux move: split the range into blocks
  of strictly decreasing powers of two (matching the binary digits of the
  upper bound $n$, exactly analogous to peeling $D$ against $\Gamma_{m-1},
  \Gamma_{m-2},\dots$ one level at a time), and its Solution 2 crucially
  proves the main lower bound by **strong induction carrying a
  simultaneously-established companion bound** ($|g(n)|\le1$) that supplies
  exactly the slack the main recursion needs — a genuinely analogous
  technique to try if the bare variable-$V$ extension of Result 2 falls
  short by a small, structured amount (as Round 4's Case-A circularity did
  for the fixed-$V$ case). This is a real analogy (same "peel by power-of-2
  blocks, track parity of digit sum" shape), not a forced match. No other
  crux found closer than this one after filtering `combinatorics` +
  `number_theory` cruxes on keywords {alternat, binary, insert, threshold,
  peel, descent, induction}.

- **Prior progress:** see `current.md` / the certified lemma file — GT(m)
  proved unconditionally for $m=0,1,2,3$ (all sums, via Monotonicity
  Reduction removing the large-sum cap); Result 2 (Unified Threshold-Pair-
  Peeling) collapses the case split to $q=0,1,\ge2$ with $q\ge2$ closing
  unconditionally at the fixed boundary target $2^k$; sub-cases (i),(ii) as
  named in round 13 are the two things left.

- **Dead ends (do not retry):**
  - **"Merge the two smallest elements of a full-count $D$ to free a slot,
    then apply the not-full-count filler-insertion argument."** Tested
    numerically (20000 exact-`Fraction` trials, $m=2..7$, full count
    $k=m+1$): merging the two smallest elements changes
    $\mathrm{OddSum}(D\cup\Gamma_{m-1})$ **in both directions** — decreased
    in $\sim90\%$ of trials but **increased** in $\sim10\%$ (min observed
    delta $\approx-2.5$, i.e. no uniform sign) — so this specific reduction
    does NOT give a valid monotone bridge from the full-count case to the
    already-closed not-full-count case. Do not propose "merge two smallest
    elements" as the mechanism for the full-count residual.

- **Small-case / intuition notes (numeric, exact `Fraction`/`scipy`,
  labeled as evidence not proof):**
  - Confirmed by $20000$ exact-`Fraction` random trials (script
    `/tmp/test_smallsum.py`) and $\sim500$ Nelder–Mead global-optimization
    runs (`/tmp/test_opt3.py`, `/tmp/test_opt4.py`): the bare small-sum claim
    $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\mathrm{sum}(D)$ for
    $\mathrm{sum}(D)<2^m$, $\max(D)\le2^m$, $|D|\le m+1$ holds with **zero
    violations** across $m=1,\dots,6$ and all counts $|D|=1,\dots,m+1$ — a
    conjecture strongly supported, matching the field's belief that
    $\mathrm{GT}(m)$ is simply true for all $m$.
  - The margin $\mathrm{OddSum}(D\cup\Gamma_{m-1})-\mathrm{sum}(D)$ is
    minimized (approaching $0$ in the limit) exactly at **count
    $|D|=m$ (one less than the piece cap)** as $\mathrm{sum}(D)\to2^{m-}$
    (continuity with the already-certified boundary case) — e.g. at $m=3$,
    $k=3$: worst margin $\approx0$ at $\mathrm{sum}(D)/2^m=0.99$; at $m=4$,
    $k=4$: same pattern. This is exactly the regime opening (2)'s
    filler-insertion argument covers (adding one piece to reach $k+1=m+1$,
    sum $=2^m$).
  - At the **full piece count** $|D|=m+1$ itself, the worst margin found by
    global optimization is consistently **larger, not smaller** (e.g.
    $\approx1.04$ at $m=3$, $\approx2.58$ at $m=4$, $\approx5.66$ at $m=5$,
    all at $\mathrm{sum}(D)/2^m=0.99$) — i.e. numerically this sub-sub-case
    has genuine slack, not a knife-edge, supporting the conjecture that a
    direct (not filler-based) argument for it exists and is not "as hard as"
    the boundary case itself.
  - Verified (via `/tmp/test_insert_delta.py`, $20000$ exact-`Fraction`
    trials, arbitrary sorted lists $L=0,\dots,8$): the elementary fact
    $0\le\mathrm{OddSum}(Z\cup\{x\})-\mathrm{OddSum}(Z)\le x$ for any $x>0$,
    zero violations — this is the fact that makes opening (2)'s
    filler-insertion argument rigorous (not just numeric): it follows from
    the certified Single-Insertion Lemma plus the elementary corollary
    $0\le\mathrm{AltSum}(N)\le\max(N)$ (itself an easy induction from the
    already-certified Peeling Lemma: $\mathrm{AltSum}(N)=\max(N)-
    \mathrm{AltSum}(\mathrm{rest})$, so by induction $\mathrm{AltSum}\ge0$
    always, hence $\mathrm{AltSum}(N)\le\max(N)$ too). This elementary fact
    is not yet stated/certified anywhere in the lemma files — it is a
    cheap, one-paragraph corollary worth certifying as its own small lemma
    if the outliner pursues opening (2).
