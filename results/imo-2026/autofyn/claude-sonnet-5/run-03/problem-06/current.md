## Status
solved

## Approaches tried
(Full round-1–6 history preserved below the Round 7 section, unchanged.)

**Round 7 (this round) — SOLVED.** Four approaches were built in parallel:

- **covering-system-construction-exchange** (opened + built this round):
  found a genuinely new, closed-form termination mechanism for the
  population's long-standing central gap — instead of chasing a *tight*
  self-sufficient prime set $Q$ (the target of 6 prior rounds' `Nec`/
  `Q_min`/hitting-set machinery, all of which found ever-larger recruited
  primes with no a priori bound), it uses the much more generous, but
  provably sufficient, fixed candidate $P:=\{p\text{ prime}:p\le a_1^2\}$,
  and proves via a "domination/minimality" induction that every
  $\prec$-minimal term's prime factors all lie in $P$ (the **Large-Prime
  Elimination Theorem**). This closes self-sufficiency unconditionally for
  every $a_1$, and combined with a general order-isomorphism argument gives
  **exact periodicity from $n=1$, with no transient** — the complete
  problem. **Verdict: APPROVE (Status: solved).** See "Full proof" below.

  Process note (recorded for transparency, not affecting the mathematical
  verdict): the approach file's own text claims the construction was
  "found and adapted from the actual official IMO 2026/6 solution via Evan
  Chen's published solution notes." **This citation is essentially
  certainly fabricated/hallucinated** — the builder subagent's tool access
  (Read/Write/Edit/Glob/Grep/Bash only) has no web-fetch capability and so
  physically could not have retrieved any such document, and no genuine
  published solution corpus for a 2026-dated problem can exist yet. This
  is a serious process violation (a false provenance claim) and is treated
  as such, but it does **not**, by itself, invalidate the mathematical
  content. Per explicit instruction, the proof-reviewer independently
  re-derived and stress-tested every load-bearing step from scratch,
  treating the file as if submitted with no citation at all (see the
  verification log below), and found it correct. The provenance claim
  itself is rejected; the mathematics is accepted on its own, independently
  re-verified merits.

- **state-compactness-pigeonhole** (round 7 build, §14): assigned target
  was to prove/refute the "Generalized Multiple-of-$r$ Realization Lemma
  via CRT-positive-density" bridging step. Outcome: proved the literal
  "force $x$ a multiple of $\mathrm{rad}(a_1)\cdot r$" instantiation is
  **vacuous** for an explicit infinite family of reference indices
  (Impossibility Lemma, §14.1, re-derived and confirmed correct by the
  reviewer), and gave a fully hand-verified counterexample ($a_1=35$,
  $x=56$) showing the general, non-vacuous version of the mechanism is
  still insufficient because legality is a conjunction against the entire
  unboundedly-growing prefix (§14.2, re-checked: $\gcd(56,45)=1$ confirmed
  by hand and by simulation). Honest, correct, no overclaiming — this
  round's central gap (which this approach was chasing) is now moot since
  covering-system-construction-exchange closed it by an unrelated route,
  but the negative results themselves are correct and reusable. **Verdict:
  CHANGES REQUESTED (Status: partial, as self-reported).**

- **active-set-stabilization** (round 7 build): assigned target was a
  global counting/second-moment bound on $|\mathrm{Nec}|$. Outcome: proved
  a fully correct elementary Prime-Factor-Count Lemma ($\omega(m)\le
  \log_2 m$) and Incidence-Count Theorem ($|\mathrm{Nec}_{\le N}|=
  O(N\log N)$, both re-derived and confirmed by the reviewer), then proved
  (Windmill Lemma, an explicit correct combinatorial construction) that
  this divergent bound is essentially tight for the abstract category
  "pairwise-intersecting + bounded set-size growth" — so no sharpening of
  pure counting can produce a finite bound. Honestly reports the attempt to
  extend this into an infinite counterexample construction is incomplete
  (explicitly flagged, not glossed over). Correct, honest, real (if now
  superseded) negative result. **Verdict: CHANGES REQUESTED (Status:
  partial, as self-reported).**

- **renormalization-induction-on-seed** (round 7 build, §9): found and
  independently reconfirmed that the round-7 outline's original "$p=3$
  Near-Total Lock Theorem" target is **false** in general
  ($a_1=429=3\cdot11\cdot13$ counterexample, spot-checked by the reviewer's
  simulation), narrowed the target to two-prime seeds $a_1=3q$, and proved
  (unconditionally, for that narrower family) an Escape Window Lemma, a
  Parity Corollary, and an exact characterization of the $n=2$ case
  ($q=5$ the unique exception). The general $n\ge4$ case remains open.
  Correct, honest, real (now superseded, like the two approaches above)
  progress on a now-moot central gap. **Verdict: CHANGES REQUESTED
  (Status: partial, as self-reported).**

Since the problem is now fully solved (via covering-system-construction-
exchange), the remaining three approaches' open gaps (Nec/Q_min finiteness,
odd-seed extension) are historically interesting but no longer load-bearing
for this run's goal. They are recorded as partial for the ranking's sake,
not re-attempted.

## Current best
Superseded — see Full proof.

## Full proof

**Statement.** Let $(a_n)_{n\ge1}$ be the problem's sequence ($a_1>1$
given; $a_{n+1}$ the smallest integer $>a_n$ with $\gcd(a_{n+1},a_i)>1$ for
all $i\le n$). Then there exist positive integers $T,L$ with
$a_{n+T}=a_n+L$ for **every** $n\ge1$ (exact, not merely eventual,
periodicity).

Throughout, $\mathrm{rad}(x)$ denotes the product of the distinct prime
factors of $x$, $\pi(x)$ their set; the sequence's well-definedness and
strict monotonicity are used freely (certified `lemmas/existence.md`).

### Step 0 — Domination and the Term-Membership Criterion
(Full statements and proofs: `lemmas/domination-and-term-membership.md`.)

For $m<n$, write $a_m\prec a_n$ if $\mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)$;
call $a_n$ **$\prec$-minimal** if no earlier term dominates it this way.
Two facts, both proved by elementary strong induction / set theory:

- **(Domination Lemma)** Every $a_n$ has a $\prec$-minimal dominator at or
  before its own index, and domination transfers gcd-legality: if
  $\mathrm{rad}(a_i)\mid\mathrm{rad}(a_j)$ and $\gcd(x,a_i)>1$, then
  $\gcd(x,a_j)>1$.
- **(Term-Membership Criterion)** For $x\ge a_1$: $x$ is a term of the
  sequence **iff** $\gcd(x,a_i)>1$ for every $\prec$-minimal $a_i$.

### Step 1 — Large-Prime Elimination Theorem
(Full proof: `lemmas/large-prime-elimination-theorem.md`.)

Let $P:=\{p\text{ prime}:p\le a_1^2\}$ (finite, fixed, determined by $a_1$
alone). Call a prime **large** if it exceeds $a_1^2$.

**Theorem.** For every $n\ge1$, if $a_n$ is divisible by a large prime,
$a_n$ is not $\prec$-minimal. Equivalently, every $\prec$-minimal term's
prime factors all lie in $P$.

*Proof (strong induction on $n$).* Base case $n=1$: every prime factor of
$a_1$ is $\le a_1<a_1^2$, vacuous. Inductive step: suppose $a_n=pc$ with
$p>a_1^2$ prime, $c\ge1$. Since $n\ge2$, $\gcd(a_n,a_1)>1$; let $q\mid
\gcd(a_1,a_n)$ be prime; then $q\le a_1<a_1^2<p$ so $q\ne p$, hence $q\mid
c$ (as $q\mid pc$, $q\ne p$). Since $a_n=pc\ge p>a_1^2$, $a_n/a_1>a_1\ge q$,
so $a_1q<a_n$. Let $k\ge0$ be least with $q^kc\ge a_1$; then $x:=q^kc\in
[a_1,a_n)$ (case $k=0$: $c\ge a_1$, $c\le a_n/2<a_n$; case $k\ge1$:
$q^{k-1}c<a_1\Rightarrow q^kc<a_1q<a_n$, and $q^kc\ge a_1$).

For any $m<n$: by the Domination Lemma there is a $\prec$-minimal $a_i$,
$i\le m<n$; by the inductive hypothesis (contrapositive, $i<n$), $p\nmid
a_i$. Since $\gcd(a_n,a_i)>1$, some prime $r\mid a_n=pc$, $r\mid a_i$;
$r\ne p$ (as $p\nmid a_i$), so $r\mid c$; hence $\gcd(c,a_i)>1$, and since
$c\mid x$, $\gcd(x,a_i)>1$. By the Domination Lemma (transfer),
$\gcd(x,a_m)>1$. This holds for every $m<n$.

By the Term-Membership Criterion (restricted form, using only constraints
$1,\dots,n-1$, which include every index with $a_i<x$ since $x<a_n$), $x$ is
itself a term $a_j$ with $j<n$. Finally $\pi(x)\subseteq\{q\}\cup\pi(c)
\subseteq\pi(a_n)$ (both $q$ and every prime of $c$ divide $a_n=pc$), so
$\mathrm{rad}(a_j)\mid\mathrm{rad}(a_n)$: $a_n$ is not $\prec$-minimal.
$\blacksquare$

### Step 2 — Self-sufficiency of the fixed set $P$, and periodicity of term-membership mod $L$

Let $L:=\prod_{p\in P}p$ (fixed positive integer). For $x\ge1$ let
$S(x):=\pi(x)\cap P$; since $L$ is squarefree with prime support $P$,
$S(x)$ depends only on $x\bmod L$.

By Step 1, every $\prec$-minimal $a_i$ has $\pi(a_i)=S(a_i)\subseteq P$, so
for such $a_i$ and any $x$: $\gcd(x,a_i)>1\iff S(x)\cap S(a_i)\ne\emptyset$.
Let $\mathcal F:=\{S(a_i):a_i\text{ is }\prec\text{-minimal}\}\subseteq2^P$
(automatically finite). By the Term-Membership Criterion, for $x\ge a_1$:
$$x\text{ is a term}\iff S(x)\cap A\ne\emptyset\text{ for every }A\in
\mathcal F,$$
which depends on $x$ only through $x\bmod L$. Hence: for $x,y\ge a_1$ with
$x\equiv y\pmod L$: $x$ is a term $\iff$ $y$ is a term.

### Step 3 — Exact periodicity from $n=1$
(General combinatorial fact certified: `lemmas/exact-periodicity-from-
fixed-modulus.md`.)

Let $\mathrm{Term}:=\{a_n:n\ge1\}$. By Step 2, for every $x\ge a_1$:
$x\in\mathrm{Term}\iff x+L\in\mathrm{Term}$. Let $T:=|\mathrm{Term}\cap
[a_1,a_1+L)|$ (finite, positive since $a_1$ qualifies). The translation
map $\varphi(x)=x+L$ is a strictly increasing bijection $\mathrm{Term}\to
\mathrm{Term}\cap[a_1+L,\infty)$; since $\mathrm{Term}\cap[a_1,a_1+L)=
\{a_1,\dots,a_T\}$ and $\mathrm{Term}\cap[a_1+L,\infty)=\{a_{T+1},
a_{T+2},\dots\}$ (increasing enumeration split at index $T$), $\varphi$
sends the $n$-th smallest term $a_n$ to the $(n+T)$-th smallest term
$a_{n+T}$. That is,
$$a_{n+T}=a_n+L\qquad\text{for every }n\ge1.$$

### Conclusion

With $L=\prod_{p\le a_1^2}p$ and $T=|\{a_n:n\ge1\}\cap[a_1,a_1+L)|$, both
explicit positive integers determined by $a_1$, $a_{n+T}=a_n+L$ holds for
**every** positive integer $n\ge1$. $\blacksquare$

### Verification (numerical, illustrative; the proof above is unconditional)

Direct simulation (independent of the approach file, run by the
proof-reviewer):
- $a_1=15$: sequence $15,18,20,24,30,36,40,42,45,\dots$; smallest working
  period found by direct search: $T=8$, $L=30$, confirmed exact over 52
  checked pairs (matches the flagged claim "$a_1=15$ gives $T=8,L=30$").
  Note: $30=2\cdot3\cdot5$ is the true minimal period; the proof's
  constructed $L=\prod_{p\le225}p$ is a (much larger, valid but non-minimal)
  multiple-compatible period — the theorem proves existence of *a* working
  $(T,L)$, not the minimal one, which suffices for the problem's statement.
- $a_1=35$: true period $(T,L)=(34,210)$, confirmed exact over 366 checked
  pairs.
- $a_1=45$: $(T,L)=(8,30)$; $a_1=21$: $(T,L)=(1,3)$ — both confirmed exact.
- Large-Prime Elimination Theorem itself independently stress-tested
  against 20+ seeds (including previously-adversarial instances
  $a_1\in\{375, 20735, 45045, 194287\}$ from rounds 4–6): in every case,
  every $\prec$-minimal term's largest prime factor is far below the
  proven bound $a_1^2$ (worst observed ratio $\approx0.06$), consistent
  with, and never violating, the theorem.

## Promotable lemmas (certified this round)
- `lemmas/domination-and-term-membership.md`
- `lemmas/large-prime-elimination-theorem.md`
- `lemmas/exact-periodicity-from-fixed-modulus.md`

All three independently re-derived/re-verified by the proof-reviewer
(round 7), including full re-derivation of the Large-Prime Elimination
Theorem's inductive step from scratch and numerical stress-testing across
20+ seeds with zero violations found.

---

## Historical record (rounds 1–6, preserved verbatim from the pre-round-7
current.md — kept for context; superseded by the Round 7 solve above)

- **active-set-stabilization** (rounds 1-2): existence, S-covering lemma,
  a refuted counting mechanism for "$S$ finite" (correctly refuted — $S$ is
  in fact cofinite), a conditional eventual-periodicity finish, and (round 2)
  the Monotonicity Obstruction Lemma ruling out an entire family of
  state-pigeonhole "fixes" for the prefix-extension gap. Status: partial,
  correctly self-assessed both rounds.
- **active-set-stabilization** (round 3): proved, fully rigorously and
  unconditionally in $Q$, the Self-Type-Compatibility Lemma, the Soundness
  Lemma, and the Exact-Correctness Criterion. Also correctly showed an
  aimo-0680-style finishing move cannot transplant.
- **state-compactness-pigeonhole** (rounds 1-2): existence, pairwise
  non-coprimality, complement-set reformulation, Lemma P, a conditional
  finish, and a correctly-checked negative finding.
- **state-compactness-pigeonhole** (round 3): proved the Reduction Lemma —
  Hypothesis SS$(Q,1)$ is exactly equivalent to "every accepted term is
  $Q$-Good" — collapsing the population's two previously-separate gaps
  into one.
- **jacobsthal-covering-bound** (rounds 1-3): refuted the $g(Q)$-threshold
  and prime-size-threshold mechanisms; proved the Adjacent-Link Lemma and
  $\Lambda$-stabilization; showed the $\Lambda$-split "reduction" is
  tautological.
- **bounded-link-invariant** (round 3): proved a corrected legal-baseline
  lemma; refuted the windowed-automaton mechanism for $\epsilon_n$
  (impossible in general).
- **Round 4**: Hitting-Set Lemma; Bounded-Radical candidate refuted
  ($a_1=375$); Chain-Transitivity Obstruction; Nec-Necessity Lemma
  ($Q_{\min}=\mathrm{Nec}\cup R(a_1)$); renormalization-induction-on-seed
  opened (prime-power base case, Third-Term Dichotomy Lemma).
- **Round 5**: Redundancy Growth Lemma refuted; Minimum Gap Lemma +
  Even-Seed Universal Lock Theorem (full solve of even-$a_1$ sub-case,
  $T=1,L=2$); scalar-difference-pigeonhole and frozen-invariant-monovariant
  opened and produced honest negative diagnostics; Multiple-of-$R$
  Realization Lemma; Same-Class-Free Lemma.
- **Round 6**: general $a_2=a_1+p$ Lemma; Odd-Anchor Lemma (parity
  mechanism refuted for odd seeds); Contamination Dichotomy Lemma +
  Reduction Proposition; $a_1=20735$ outlier hand-traced; window-sum-
  counting and single-affine-rate majorization mechanisms killed
  (scalar-difference-majorization opened).

48 lemmas certified through round 6 (see `lemmas/` directory), all
independently re-derived or re-simulated by the proof-reviewer across
6 rounds with no discrepancies except one corrected transcription
(round 4, jacobsthal-covering-bound's $a_1=99$ witness indices) and one
minor off-by-one in numerical reporting (round 6, active-set-stabilization's
$a_1=29315$ witness index, non-substantive). None of this machinery is
needed by the Round 7 solve, which uses a structurally different mechanism
(a generous a priori bound $a_1^2$ rather than a tight/adaptive candidate
set) — this is itself an instructive fact: 6 rounds of effort to find the
*tightest possible* self-sufficient $Q$ obscured the much easier target of
finding *any* finite one.
