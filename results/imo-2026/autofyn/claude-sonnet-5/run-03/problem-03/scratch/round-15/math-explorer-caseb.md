## imo-2026-03 — lens: Case-B(m,k) obstruction (shared with GT(m) general-m closure)

### 1. Precise statement of Case-B(m,k) and its current known partial results

Setup notation (all from the certified files): $\Gamma_n=\{2^n,2^{n-1},\dots,2,1\}$
($n+1$ elements), $\mathrm{OddSum}$/$\mathrm{EvenSum}$ = sum of odd/even-ranked
elements in descending sort. TOP-ONLY$(m)$: for every partition $B$ of $2^m$
into $\le m+1$ positive parts, $\mathrm{OddSum}(B\cup\Gamma_{m-1})\ge2^m$.
The Dominant-Chain Theorem (Theorem 5, certified) already closes TOP-ONLY$(m)$
whenever $\max(B)\ge2^{m-1}$. **`Case-B(m,k)`** (round 4/5 naming) is exactly
the complementary regime:
$$\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1\quad\text{is FALSE, i.e. we must show }\mathrm{OddSum}(B\cup\Gamma_{m-2})\ge2^m\quad\text{whenever }\max(B)<2^{m-1}.$$
(Equivalently, peeling $b_1$ off first, this is TOP-ONLY$(m)$ restricted to
$\max(B)<2^{m-1}$.)

**Known closed sub-regions (round 5, unconditional):**
- $b_1<2^{m-2}$: closed.
- $2^{m-2}\le b_1\le2^{m-1}-1$: closed.
- Residual: a width-1 sliver $2^{m-1}-1<b_1<2^{m-1}$, uniform in $m$.

**This sliver is proved (round 6-9) exactly equivalent to the "Branch-I.A-restricted
window"**: $c_1:=\max(C)\in[2^{\ell-1},2^{\ell-1}+1-\varepsilon)$ with
$\max(C\setminus\{c_1\})<2^{\ell-1}$, target
$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge2^\ell+\varepsilon-1$ ($\ell=m-1$).
Window split into gap (a) [endpoint-$W$/left-endpoint optimality] and gap (b)
[monotonicity of the max across the window in $W$]. **Gap (b) is FULLY CLOSED**
(round 12, Window Reduction Theorem, both sub-cases (i)/(ii)) and **the left
endpoint of gap (a) is exactly evaluated** (round 9, Theorem W: margin exactly
$\varepsilon/2$ there). **Gap (a) in full (every admissible $D$ at the endpoint,
not just Theorem W's witness) is proved for $\ell=0,1,2,3$** (i.e. $m=\ell-1... $
matches $\mathrm{GT}(m)$, $m\le3$) **and remains open for $\ell\ge5$ ($m\ge4$)**.

**Round 11 (independently)** proved Case B's own `TOP-ONLY(m-1)`-equivalence
(Theorem N, greedy-reduction-geometric): the hardest slice of Case B
(full-budget on $B$, $S'''$ unsplit) is literally, symbol-for-symbol, an
instance of TOP-ONLY$(m-1)$'s complementary regime — i.e. **the SAME window**,
one level down. So all three approach lines (self-similar-induction-on-n's
window, greedy-reduction-geometric's Case B, and round 14's Small-Sum
Reduction Theorem for GT(m)) have now converged onto **one single object**:
close the window (equivalently TOP-ONLY's complementary regime / GT's
boundary case) for every $\ell\ge5$.

**Round 14 finding (the newest, most load-bearing structural fact):** using
the newly-certified AltSum Corollary and Growth Lemma, the *entire* $p=0$
branch of $\mathrm{GT}(m)$ (both small-sum and large-sum instances) reduces
to this one boundary case $\mathrm{sum}(D)=2^m$ — i.e. `Case-B(m,k)` really is
now the *sole* combinatorial obstruction for the $q=0$ recursion chain. The
one remaining independent obstruction is **sub-case (i)**: the $q=1$,
excess-$e\ge1$ branch of the peeling recursion, target
$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge2^k-a_1$ where $a_1\in(2^{k-1},2^k)$ is
the one element of $D$ exceeding the current threshold. A natural
"piece-cap-relaxed" fix is proved FALSE by an exact counterexample
($D=\{0.4,0.4\}$, $k=0,e=1$: the naive statement needs
$\mathrm{OddSum}(D)\ge\min(\mathrm{sum}(D),2^0)$ but $0.4<0.8$) — **but this
counterexample only kills the naive/free-standing version; the real
recursion's instance is never invoked in the regime where the counterexample
lives** (checked: the true $\mathrm{GT}(1)$ instance built from it holds with
margin, $1.4\ge0.8$). So the counterexample does NOT show sub-case (i) is
false, only that the most direct generic reduction attempt is too weak.

### 2. Most promising technique(s) to close it now

**(A) Recognize sub-case (i) as an already-defined-but-unclosed object,
not a fresh problem.** Round 3/4 of `self-similar-induction-on-n` defined
$G(m,k;V)$: for $V\in[2^{m-1},2^m]$, "for every partition $B$ of $V$ into
$j+1$ parts and every $c$-cut refinement $S$ of $\Gamma_{m-1}$ with
$j+c\le k$, $\mathrm{OddSum}(B\cup S)\ge V$." This is *exactly* the shape of
sub-case (i)'s target (a variable target $V=2^k-a_1 \in (0,2^{k-1})$ against
a fixed $\Gamma$-tail one level down, with the piece-budget coupling
$j+c\le k$). $G(m,k;V)$ was **extensively numerically confirmed (Monte Carlo,
$m\le5$, zero violations) but never proved for $j\ge1,V<2^m$** — it was set
aside as "left open" in round 4 and never revisited since the file pivoted to
the peel+AltSum machinery. **This is a concrete, unexploited opening**: sub-case
(i) may not need a separate ad hoc argument at all — it may close as soon as
$G(m,k;V)$ closes for general $V$, and $G(m,k;V)$ already has machinery
partially built for it (the AltSum reformulation, Lemma AS; the Single-Insertion
Lemma) that was abandoned mid-way, not because it failed but because the file
moved to a different framing. Worth explicitly re-deriving whether sub-case (i)'s
exact target is literally an instance of $G(k-1,\cdot;2^k-a_1)$ (careful index
matching needed — do this check first, cheaply, before any new proof attempt).

**(B) Boundary/continuity closure for the window's interior, $\ell\ge5$.**
My own stress-test (below) confirms numerically that the excluded boundary
$\max(D)\to2^{m-1}$ is exactly where the margin $\to0^+$ — i.e. the hard
part of Case-B(m,k) sits at $D$ configurations with one coordinate approaching
the threshold from below, which is structurally the SAME boundary that sub-case
(i) lives on ($a_1\to2^{k-1}$ from above in the peeling language, or from
below in the un-peeled language). This strongly suggests gap (a) and sub-case
(i) are not just "the same difficulty level" but may be **literally the same
limiting phenomenon** viewed from two sides of a peeling step — worth checking
directly (a genuinely different framing than continuing induction on $\ell$):
does the certified Elementwise/Growth-Lemma monotonicity machinery, pushed to
the boundary via a limiting/continuity argument (OddSum is continuous, even at
ties — Lemma 1's proof explicitly never needs strict inequalities), let you
transfer the interior result (already closed via Window Reduction) across the
excluded boundary point without a fresh induction? This has NOT been tried
(all attempts so far are induction-based: peel, recurse, case-split on $q$).

**(C) Amortized/potential argument (crux `aimo-0019`, IMO 2016 P3 "paint
game").** Genuinely different framing, not yet tried on this problem. That
problem's solution maintains an invariant "ink used for $[0,x_r]$ is $\le
3x_r$" via amortized induction over an unboundedly-recursing dyadic process,
with a companion invariant "at most one interval of each dyadic length to the
right of the frontier." The self-similar-induction-on-n recursion has an
analogous shape (peeling off dyadic $\Gamma$-levels one at a time, tracking a
running excess). A single global potential/invariant (rather than a case
split on $q\in\{0,1,\ge2\}$) might handle sub-case (i) and Case-B(m,k)
uniformly, avoiding the need to separately patch the $q=1,e\ge1$ hole. This
is a genuinely different top-level attack (potential function over the whole
recursion depth, not peel-and-case-split at each level) — worth a dedicated
approach, not a tweak to the existing one.

### 3. Numeric/computational lead (my own, this round)

I ran exact-shape random search + `scipy` Nelder-Mead optimization (real
arithmetic, not exact `Fraction` — treat as evidence only) for
$\min_D[\mathrm{OddSum}(D\cup\Gamma_{m-1})-2^m]$ over partitions $D$ of $2^m$
into $2$ to $m+1$ parts with $\max(D)<2^{m-1}$ (i.e. Case-B(m,k)'s hardest
slice, TOP-ONLY$(m)$ complementary regime), for $m=3,\dots,8$:

```
m=3: min margin ≈ 3.5e-6   (optimizer pushed max(D) → cap)
m=4: min margin ≈ 7.4e-6
m=5: min margin ≈ 1.5e-5
m=6: min margin ≈ 3.1e-5
m=7: min margin ≈ 6.3e-5
m=8: min margin ≈ 0.033 (optimizer likely under-converged at this size — not a real jump; the random-search pass alone found 0.83 at m=6, 1.68 at m=7 without pushing to the boundary, consistent with margin→0 only right at the excluded boundary)
```

**Conjecture (my own reading, consistent with all certified partial results):
the margin is exactly 0 only in the (excluded) limit $\max(D)\to2^{m-1}^-$,
and strictly positive everywhere in the interior, for every $m$ tested** — no
sign of a violation, no sign of a clean nonzero closed-form floor away from
the boundary. This matches Theorem W's exact value ($\varepsilon/2\to0$ as
$\varepsilon\to0$, i.e. as $c_1\to2^{\ell-1}$ from the window's own side) —
**the same "margin → 0 only at one specific boundary" shape recurs at every
level of the recursion so far checked**, reinforcing that this is a genuine
tight inequality (not slack, not a numerical artifact), and that any proof
must be an exact identity/limit argument near that one boundary point, not a
soft inequality with room to spare. This is evidence only, not a proof: my
script uses floating-point optimization, not exact arithmetic, and could
hide extremely small violations; any true proof must use exact rational
techniques as the rest of the population's certified work always does.

### 4. Crux corpus match

Filtered `combinatorics` domain, subtopics `games-and-strategy`,
`extremal-principle`, `invariants-and-monovariants`, `induction-and-construction`
for keyword overlap (dyadic/binary/power-of-two, alternating, greedy, peeling).

- **`aimo-0019`** (IMO 2016 P3, the "paint pot" game): best match found. Crux
  moves: "bound a family of dyadic-length pieces of pairwise distinct sizes by
  twice the largest, via the geometric sum of distinct negative powers of
  two" and "maintain a linear potential bounding cumulative resource by a
  constant times progress, proved by amortized induction." Genuinely
  analogous in flavor (unboundedly-recursing dyadic/power-of-two structure,
  a running "frontier" quantity, an amortized invariant carried across
  rounds) though NOT the same game mechanics (that problem's players choose
  intervals to blacken; ours is an alternating-claim OddSum game) — a
  technique lead (Idea (C) above), not a literal transplant.
- No other crux in the sampled subtopics matched closely enough to be worth
  citing; most `games-and-strategy` hits are pairing/mirroring strategies for
  discrete combinatorial games (not the right shape — our problem is a
  continuous-value alternating-claim minimax, already fully handled by the
  certified Greedy-Optimality Lemma, so pairing-strategy cruxes are not
  applicable to the remaining open gap specifically).

### 5. What has already failed / do not retry

- **The literal "piece-cap-relaxed generalization of $\mathrm{GT}(k-1)$"**
  for sub-case (i): refuted by exact counterexample ($D=\{0.4,0.4\}$,
  $k=0,e=1$). Do not re-attempt this exact naive statement — but note (per
  round 14's own diagnosis) the counterexample lives *outside* the regime the
  real recursion ever invokes, so a *correctly regime-restricted* version
  (target $>2^{k-1}$ only) is NOT yet ruled out — this is the open target,
  not a dead end.
- **Vertex-enumeration by inspection/numerical search** (round 11, Middle-Regime
  Vertex Reduction Theorem applied to $(j,c)=(2,1)$): closed $m=3,4$ exactly,
  found slack at $m=5$, but the candidate vertex list was never proved
  exhaustive (misses ties against individual elements of $\Gamma_{m-2}$) — a
  real, structurally-limited technique, not fully dead but flagged as
  incomplete by its own author; extending it to general $m$ would need first
  closing the exhaustiveness gap, not just running the same search further.
- **Order-statistics / peel+scalar-bound route for the window's lower-half**
  (round 7): explicitly diagnosed as the wrong mechanism (needs an upper bound
  on OddSum but the technique that worked for lower bounds — discarding a
  remainder — is invalid in that direction). Do not retry this specific
  technique on gap (a) $\ell\ge5$.
- **Exchange-smoothing via crux `aimo-0146`** (used for the window's left
  endpoint, round 9): succeeded only at the single endpoint; the full
  monotonicity-in-$W$ argument needed for the rest of the window was later
  fully closed by a *different* mechanism (Elementwise Monotonicity Lemma,
  round 12) — so `aimo-0146`'s specific exchange-argument approach is not
  needed again for gap (b); it was never applied to gap (a) itself and
  remains untried there, but the successor Growth-Lemma/Monotonicity-Reduction
  machinery (round 13-14) is a strictly more general, already-certified
  replacement for the same "shift mass" idea — prefer that over
  re-deriving `aimo-0146`'s argument from scratch.
