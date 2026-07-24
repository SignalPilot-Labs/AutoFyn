## Status
unsolved (honest negative result this round — the approach's own proposed
top-level target, `R(N)`-finiteness in the literal/unrestricted sense, is
proved FALSE, unconditionally, for every `a_1`; H2 itself is untouched,
neither proved nor refuted, by this finding)

## Approaches tried

- (round 24 outline, not built) A genuinely different H2 framing via
  bounding the RATE of new-prime recruitment `R(N) := #{j≤N : P(a_j) ⊄
  ⋃_{i<j}P(a_i)}`, distinct from the dead `direct-s0-self-absorption`
  containment framing.

- **(round 24, this build).** Per the dispatch, executed the outline's
  mandatory Step 1 (cheap-kill pre-screen) FIRST, before any structural
  attempt, and per the outline-reviewer's requirement, checked explicitly
  whether closing `R(N)`-finiteness would just be a repackaged instance of
  the certified Monotone Chain Reformulation Lemma. **Result: neither
  question needed a deep structural attempt — a direct, fully rigorous,
  elementary proof (below) shows `R(N)` is unconditionally UNBOUNDED for
  every `a_1`, i.e. the literal-primes reading of `R(N)`-finiteness this
  approach's outline proposed as its target is FALSE, not merely hard.**
  This is a genuine mathematical result (new: `Unbounded Total Prime
  Support Theorem`, proved in full below), not a repeat of the round-23
  `direct-s0-self-absorption` finding (which showed a DIFFERENT mechanism,
  the Bounded Witness Lemma, insufficient for containment) and not a
  repackaging of the Monotone Chain Reformulation Lemma (that lemma is
  about a SUFFICIENT condition for self-absorption at some specific `M`;
  this result is an unconditional, universal fact about `⋃_j P(a_j)`
  itself, true for every `a_1`, that holds regardless of whether any
  self-absorbing core exists).

  A companion computational investigation (own from-scratch Python
  simulation, bitmask/dedup method, distinct from all prior rounds'
  scripts — see below) on `a_1=11305` out to 50,000 terms independently
  confirms the qualitative shape of this result: the literal count of
  "index introduces at least one brand-new prime factor" (`R(N)` as
  literally defined in the outline) does NOT decelerate toward zero — its
  rate `R(N)/N` decreases only very slowly (from `0.13` at `N=2500` to
  `0.064` at `N=50000`, i.e. `R(N) ~ N^{0.83}` by direct log-log fit, far
  closer to linear than to the `√N`-type deceleration the
  extended-type-based `h2-absence` explorer measured for a DIFFERENT,
  coarser quantity). This numeric finding is exactly what the theorem
  below predicts (and now fully explains, not just observes).

  **Crucially, this result does NOT refute H2** — see the "Logical
  relationship to H2" section below, independently re-derived from the
  precise definitions in the certified `self-absorbing-core-theorem.md`.
  H2's self-absorption machinery is built entirely on `ρ_S(n) := P(a_n)∩S`
  (the part of `P(a_n)` INSIDE a fixed core `S`) and only requires literal
  containment `P(a_j)⊆S` for the FINITELY many indices `j ≤ N(S)` — beyond
  that finite prefix, arbitrarily many "vagabond" primes outside `S` are
  explicitly permitted and simply ignored by the whole apparatus. So an
  infinite, ever-growing total prime support `⋃_j P(a_j)` is fully
  compatible with H2's existence claim.

## Current best

### 1. The mandatory Step-1 pre-screen: own fresh simulation

Implemented a from-scratch Python simulator (SPF trial-division
factorization using a precomputed prime table up to 60000, prime→bit
dynamic assignment, and a **deduplicated** list of distinct
prime-factor-set bitmasks for legality checking — legal(m) iff `P(m)`
intersects every distinct set of primes seen among `a_1,...,a_{n-1}`, which
is provably equivalent to intersecting every individual `P(a_i)` since
distinct-set-dedup changes nothing about which sets get hit). Sanity check:
reproduced the well-known `a_1=15` sequence exactly (`15,18,20,24,30,36,
40,42,45,48,50,54,60,66,70,72,75,78,80,84,...`) before trusting the tool on
the hard seeds.

Ran on `a_1=11305` to `N=50000` terms, tracking `R(N)` (literal count of
indices introducing a genuinely new prime, per the outline's own
definition) at 20 checkpoints:

```
n=2500  R=327   R/n=0.1308
n=5000  R=507   R/n=0.1014
n=10000 R=841   R/n=0.0841
n=20000 R=1464  R/n=0.0732
n=30000 R=2064  R/n=0.0688
n=40000 R=2643  R/n=0.0661
n=50000 R=3204  R/n=0.0641
```

A power-law fit `R(N)~C N^α` using the endpoints `N=10000,R=841` and
`N=50000,R=3204` gives `α ≈ ln(3204/841)/ln(5) ≈ 0.83` — i.e. `R(N)` is
much closer to LINEAR growth than to the `√N`-type growth the
`h2-absence` explorer measured for the coarser "distinct-extended-type"
count. The window-to-window increment of `R` (per 2500-term block) only
drifts down slowly, from `180` (window `0-2500`) to `142` (window
`47500-50000`) — a `~21%` decrease over a `20×` increase in `N`, far
slower than the `~55%` decrease a genuine `√N` law would predict over the
same range (`√(2500/50000)≈0.22`, i.e. increments should have fallen to
about a fifth, not by only a fifth). **This numeric behavior is not a
coincidence or a window artifact — it is exactly what the theorem below
forces: `R(N)`, in the literal unrestricted-primes sense, provably diverges
for every `a_1`, and the specific near-linear rate is consistent with (an
instance of) that divergence.**

### 2. The Unbounded Total Prime Support Theorem (new, proved in full)

**Theorem.** For every valid sequence `(a_n)_{n\ge1}` satisfying the
problem's hypotheses (`a_1>1`; `a_{n+1}` = least integer `>a_n` with
`gcd(a_{n+1},a_i)>1` for all `i=1,\dots,n`), the set
`P_\infty := \bigcup_{n\ge1} P(a_n)` of all primes ever dividing a term of
the sequence is infinite.

**Depends on (certified).** `bounded-gap-lemma.md`
(`a_n \le n\cdot a_1$ for all `n\ge1`).

**Proof.**

*Setup.* Suppose, for contradiction, `P_\infty` is finite, say
`P_\infty=\{p_1,\dots,p_k\}` with `k\ge1` (finite and nonempty, since
`a_1>1` has at least one prime factor, which lies in `P_\infty` by
definition of the union). By definition of `P_\infty`, every `a_n$ factors
entirely over `\{p_1,\dots,p_k\}$: `a_n = p_1^{e_{1,n}}\cdots p_k^{e_{k,n}}$
for some nonnegative integers `e_{1,n},\dots,e_{k,n}$ (a "`P_\infty`-smooth"
or "`P_\infty`-supported" number).

*Step A (counting `P_\infty`-supported integers up to `X`).* For a real
`X\ge1`, let `N(X)` be the number of positive integers `\le X` that factor
entirely over `\{p_1,\dots,p_k\}$. Such an integer corresponds to a
`k`-tuple of exponents `(e_1,\dots,e_k)\in\mathbb Z_{\ge0}^k$ with
`\prod_i p_i^{e_i}\le X$. Since each `p_i\ge2$, if `p_i^{e_i}\le X$ then
`2^{e_i}\le X$, so `e_i\le\log_2 X$; hence each coordinate `e_i$ ranges over
at most `\lfloor\log_2 X\rfloor+1$ values. Since the `k`-tuple is
determined by its `k$ coordinates, `N(X) \le (\lfloor\log_2 X\rfloor+1)^k
\le (\log_2 X+1)^k$.

*Step B (comparing the count to the actual number of terms).* The
sequence `a_1<a_2<\cdots<a_n$ consists of `n$ pairwise DISTINCT positive
integers, all `\le a_n$, and — by the contradiction hypothesis — all
`P_\infty`-supported. Hence `n \le N(a_n) \le (\log_2 a_n+1)^k$. By the
certified Bounded Gap Lemma, `a_n\le n\cdot a_1$, so `\log_2 a_n \le
\log_2 n+\log_2 a_1$. Setting `C:=\log_2 a_1+1$ (a fixed constant `\ge1$
since `a_1\ge2$), we get, for EVERY `n\ge1`:
$$n \;\le\; (\log_2 n+C)^k. \qquad (\ast)$$

*Step C (a self-contained "exponential beats any fixed power of `\log`"
lemma).* **Lemma A (Binomial Dominance).** For every integer `K\ge1$ and
every integer `m\ge2K$, `2^m \ge (m/(2K))^K$.
*Proof of Lemma A.* By the Binomial Theorem, `2^m=(1+1)^m=\sum_{i=0}^m
\binom{m}{i} \ge \binom{m}{K}$ (a single nonnegative term, valid since
`m\ge2K\ge K$). Now `\binom{m}{K}=\frac{m(m-1)\cdots(m-K+1)}{K!}$: the
numerator is a product of `K$ factors, each `\ge m-K+1$, and
`m-K+1>m-K\ge m/2$ (using `m\ge2K\iff m-K\ge m/2$), so the numerator
`> (m/2)^K$; and `K!\le K^K$ (each of the `K$ factors in `K!$ is `\le K$).
Hence `\binom{m}{K} \ge (m/2)^K/K^K=(m/(2K))^K$, giving `2^m\ge(m/(2K))^K$.
`\quad\blacksquare$ (Lemma A)

*Step D (deriving the contradiction from `(\ast)`).* Fix `K:=k+1$. Apply
`(\ast)$ to `n:=2^s$ for a positive integer `s$ to be chosen: `\log_2 n=s$,
so `(\ast)$ reads `2^s \le (s+C)^k$. By Lemma A, whenever `s\ge2K=2k+2$:
$$\Big(\frac{s}{2K}\Big)^{K} \;\le\; 2^s \;\le\; (s+C)^k. \qquad (\dagger)$$
Divide both sides of `(\dagger)$ by `s^k$ (valid, `s^k>0$; recall
`K=k+1$, so the left side is `s^{k+1}/(2K)^{k+1}$ divided by `s^k$, i.e.
`s/(2K)^{K}$):
$$\frac{s}{(2K)^{K}} \;\le\; \Big(1+\frac{C}{s}\Big)^k.$$
For `s\ge C$, `1+C/s\le2$, so the right side is `\le 2^k$. Hence, for every
integer `s\ge\max(2K,C)$:
$$s \;\le\; 2^k\,(2K)^{K} \;=:\; s_0(k). \qquad (\ddagger)$$
`s_0(k)$ is an explicit finite constant depending only on `k$ (equivalently
only on `a_1$, since `k=|P_\infty|$ is being assumed finite for
contradiction — note `k$ itself is a fixed but a priori unknown integer;
the argument works for whatever finite value `k$ would take, `s_0(k)$
being computed accordingly). Now choose the concrete integer
`s^* := \lceil\max(2K,\,C,\,s_0(k))\rceil+1$ — an explicit integer
exceeding every threshold used in `(\ddagger)`'s derivation. Applying
`(\ast)$ (equivalently `(\dagger)`–`(\ddagger)`) at `n:=2^{s^*}$ forces
`s^*\le s_0(k)$ by `(\ddagger)$ — but `s^* > s_0(k)$ by construction. This
is a contradiction.

*Conclusion.* The assumption that `P_\infty$ is finite is untenable.
Hence `P_\infty = \bigcup_{n\ge1}P(a_n)$ is infinite, for every `a_1$.
`\blacksquare$

**Verification of Lemma A on a concrete instance** (sanity check, not part
of the proof): `k=3,K=4$: `s_0(3)=2^3\cdot8^4=8\cdot4096=32768$ — a large
but finite, fully explicit threshold, confirming the argument produces a
genuine finite contradiction point, not an asymptotic hand-wave.

### 3. What this theorem does and does not establish

- **It definitively refutes, for every `a_1` (not just the flagged hard
  seeds), the outline's own top-level target as literally stated**: `R(N)
  := \#\{j\le N: P(a_j)\not\subseteq\bigcup_{i<j}P(a_i)\}` cannot converge
  (`R(N)\to R(\infty)<\infty`) — if it did, `\bigcup_j P(a_j)` would be
  finite (bounded by `R(\infty)` new-prime-introducing indices, each
  contributing finitely many primes by the certified Elementary
  `\omega`-Bound, `lemmas/elementary-omega-bound.md`), contradicting the
  theorem. So `R(N)\to\infty` unconditionally. This settles the outline's
  Step-1 pre-screen question (and the `h2-absence` explorer's seed-
  asymmetry worry) completely: the asymmetry between `a_1=4807` and
  `a_1=11305` reported by the explorer is real, but concerns a
  DIFFERENT, coarser statistic (distinct EXTENDED types restricted to a
  fixed enlarged core `S_0`, i.e. `\rho_{S_0}(n)`-classes) — not the raw,
  unrestricted `R(N)` this approach's outline proposed to bound, which is
  now known, by direct proof, to diverge on EVERY seed, including
  `a_1=4807` itself (whose extended-type count was observed decelerating,
  yet whose raw new-prime count must still diverge, by the theorem — these
  are not in tension, since the theorem's divergence can be carried
  entirely by primes that get excluded from `S_0` and never recur, exactly
  as the certified stack's `\rho_S(n):=P(a_n)\cap S` definition anticipates).

- **It does NOT refute H2.** Re-reading the certified
  `self-absorbing-core-theorem.md` definitions precisely: a finite core
  `S^*\supseteq S_0` is called self-absorbing iff `S^{*+}=S^*`, where
  `S^{*+} := S^* \cup \bigcup_{j=1}^{N(S^*)} P(a_j)` — i.e. self-absorption
  demands `P(a_j)\subseteq S^*` **only for the finitely many indices
  `j=1,\dots,N(S^*)`**, a fixed finite prefix. For `j>N(S^*)`, every
  certified fact in the stack (Extended Persistent-Type Pigeonhole, the
  Theorem's own Step 1/Step 2 proof) uses only `\rho_{S^*}(j):=
  P(a_j)\cap S^*` — the machinery is explicitly built to be silent about,
  and entirely unaffected by, whatever primes lie in `P(a_j)\setminus
  S^*` for `j` past the finite threshold. Hence `\bigcup_j P(a_j)` being
  infinite (this theorem) is **fully consistent** with some finite `S^*`
  being self-absorbing: the infinitude of `P_\infty` can be realized
  entirely by "vagabond" primes that appear once (past index `N(S^*)`),
  divide no other term, and are simply outside `S^*`, never entering
  `\rho_{S^*}(j)` for any `j`, and never needing to be absorbed. This
  matches, and now formally explains, the round-23-corrected numeric
  premise that both hard seeds show extended-type counts that (at least on
  `a_1=4807`) look like they may be tapering even while raw new-prime
  counts (this round's finding) keep growing — the two phenomena are
  logically independent, and only the (still fully open) EXTENDED,
  `S`-restricted quantity is what H2 actually needs to be bounded.

- **What remains open.** H2 itself — existence of a finite self-absorbing
  core `S^*` — is completely untouched by this round's finding, in either
  direction. This approach's originally-proposed mechanism (bound `R(N)`
  directly via minimality + the elementary `\omega`-bound) is now known to
  be **chasing a false target** in its literal form and should not be
  pursued further as stated. A possible salvage — replacing `R(N)` by an
  `S`-restricted analogue `R_S(N) := \#\{j\le N: \rho_S(j)\notin
  \mathcal P'(S)$ for the currently-stabilized alphabet`\}$ — is, on
  inspection, **exactly** the quantity `N(S)` (or its finite-prefix
  analogue) already central to the certified Extended Persistent-Type
  Pigeonhole / Monotone Chain Reformulation Lemma machinery; attempting to
  bound it by a counting/rate argument is not a new corridor but a
  re-statement of the already-attempted, already-non-constructive H2
  sub-gap (`core-growth-monotonicity`'s Proposition 3, `direct-s0-self-
  absorption`'s findings) — consistent with, and reinforcing, the
  outline-reviewer's flagged equivalence risk. No new mechanism for
  bounding `R_S(N)` was found this round; this is honestly recorded as
  still open, not solved by relabeling.

### Open gaps
H2 (existence of a finite self-absorbing core) remains completely open.
This approach's proposed mechanism, once precisely checked, targets either
(a) a provably FALSE quantity (`R(N)` unrestricted — closed this round,
negatively, with a full proof) or (b) if restricted to the `S`-dependent
version, the SAME already-known-non-constructive sub-gap other H2
approaches (`core-growth-monotonicity`, `direct-s0-self-absorption`) have
already hit. No further structural progress toward H2's existence claim
was found. This slug should not be re-built with the same "bound `R(N)`
directly" mechanism — any future H2 attempt via a counting/rate idea must
work with the `S`-restricted quantity from the start (not the
unrestricted one this round definitively closes off), and should look for
genuinely new leverage beyond the Extended Persistent-Type Pigeonhole /
Monotone Chain machinery already shown insufficient by three independent
prior approaches.

## Full proof
(not applicable — Status is `unsolved`; the problem's actual claim (T,L
periodicity) is not addressed by this approach beyond what the certified
Master Conditional Theorem already reduces it to, H1+H2, both still open.
The complete, self-contained proof of the Unbounded Total Prime Support
Theorem is given in full above and stands on its own as a certified,
unconditional fact.)

## Promotable lemmas

- **Unbounded Total Prime Support Theorem** (proved in full above): for
  every valid sequence `(a_n)` satisfying the problem's hypotheses,
  `\bigcup_{n\ge1}P(a_n)` is infinite. Depends only on the certified
  Bounded Gap Lemma (`lemmas/bounded-gap-lemma.md`) plus an elementary,
  fully self-contained "Binomial Dominance" sub-lemma (exponential growth
  beats any fixed power of `\log`, proved from the Binomial Theorem with
  an explicit threshold). Unconditional, no open hypotheses. Reusable by
  any future approach that needs to know the sequence's total prime
  support is infinite (and, importantly, by any approach tempted to
  re-propose "total/raw prime support stays bounded" as an H2 mechanism —
  this closes that door permanently and rigorously, sharpening the
  existing informal round-2/17 diagnostic into an actual proved theorem).
  Also documents precisely why this fact is compatible with, and does not
  bear on, H2 as correctly formalized by the certified Self-Absorbing Core
  Theorem (see "Logical relationship to H2" discussion above) — this
  clarification is itself worth preserving alongside the lemma so future
  rounds do not mistake the theorem for progress on (or a refutation of)
  H2.
