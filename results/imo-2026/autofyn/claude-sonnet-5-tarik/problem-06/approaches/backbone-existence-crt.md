## Status
partial

## Round 2 Outline (proof-outliner directive — retargeted)

**CORRECTION — do NOT build on Section 3's literal `H_n` definition below; it is
FALSE.** Round-2 exploration (`/tmp/round-2/math-explorer-alt-framing.md`)
numerically refuted Section 3's "backbone finiteness" target exactly as defined
there (`H_n :=` primes ever co-occurring as a pairwise gcd witness at some pair
`(i,j)`). Even in the *already-solved* `a_1=15` case (eventual `T=8,L=30`, tail
governed by `{2,3,5}`), thousands of *incidental* primes appear as gcd witnesses
between pairs of terms deep in the periodic tail: 2948 found among index pairs
`50≤i<j≤400` alone (e.g. `a_52=204=2^2\cdot3\cdot17` and
`a_324=1224=2^3\cdot3^2\cdot17` share the purely incidental prime `17`, which plays
no causal role in either term's admissibility). `\bigcup_n H_n` is (empirically,
and almost certainly provably) infinite even when the theorem's conclusion already
holds. **Root cause diagnosed**: Section 3's definition of "recruit at `(i,j)`"
accepts *any* prime in `P_i\cap P_j` once `\ell(i)\cap\ell(j)=\emptyset`, not a
*canonical minimal* witness — so it picks up coincidental large shared factors of
two already-fixed integers, not the prime that was actually load-bearing when the
sequence was constructed. (Sanity check confirmed: the *minimal* common prime of
the `a_52,a_324` example above is `\min(\{2,3,17\})=2`, not `17` — using a
canonical/minimal witness instead of "any common prime" avoids this exact failure
mode.) Do NOT spend further builder effort proving `\bigcup H_n` finite as
literally defined in Section 3; that section's target is retired.

**Retargeted claim `(\star)`.** Let `B:=\{p\text{ prime}:p\mid a_n\text{ for
infinitely many }n\}` (the *persistent-divisor* primes — the finite set that
actually governs the sequence's eventual periodic behavior, as opposed to the
unbounded set of primes that merely co-occur incidentally). Prove:
$$(\star)\qquad B\text{ is finite.}$$
Once `(\star)` is established, hand it to sibling approach
`intersecting-family-covering-construction` (see its own Round 2 Outline) to build
the explicit finite covering/periodic construction; this approach's job is
`(\star)` itself, via counting/density — a mechanism distinct from the sibling's
construction-then-verify route (legitimate technique diversity for the same
target lemma, per round-1 memory note).

**New Step 3 skeleton (replaces the old Section 3 target above; Sections 1–2 and 4
below — Lemma P, Lemma P′, Lemma Q, and the Domination Lemma — remain fully valid
and are imported unchanged):**

- **3a. Characterize `B` via `D_n`.** Recall `D_n(q):=|\{i\le n:q\mid a_i\}|`
  (Section 4). Directly from the definition, `q\in B` iff `D_n(q)\to\infty` as
  `n\to\infty` (trivial: `D_n(q)` is non-decreasing in `n`, and `q` divides
  infinitely many terms iff its cumulative count is unbounded). So `(\star)` is
  equivalent to: only finitely many primes `q` have `D_n(q)\to\infty`.

- **3b. New Lemma (`O(\log n)` dominant-prime bound — cheap, certify first).** For
  every `n`, let `q(n)` be a prime factor of `a_{n+1}` achieving the Domination
  Lemma's max (`D_n(q(n))\ge n/\omega(a_{n+1})\ge n/\log_2 a_{n+1}`). *Mechanism:*
  combine this LOWER bound with a TRIVIAL interval-packing UPPER bound — since
  `a_1,\dots,a_n` are `n` distinct integers in an interval of length
  `a_n-a_1\le(n-1)L` (Lemma 1, `L=\mathrm{rad}(a_1)`), any fixed prime `q` divides
  at most `\lfloor(a_n-a_1)/q\rfloor+1\le(n-1)L/q+1` of them, i.e.
  `D_n(q)\le(n-1)L/q+1` for *every* prime `q` unconditionally. Combining:
  `n/\log_2 a_{n+1}\le D_n(q(n))\le(n-1)L/q(n)+1`, which rearranges (once `n` is
  large enough that the LHS exceeds `1`) to `q(n)=O(L\cdot\log_2a_{n+1})=O(\log n)`
  (using Lemma 1's `a_n=O(n)` to turn `\log_2a_{n+1}` into `O(\log n)`). This is a
  three-line consequence of two *already-certified* lemmas plus one trivial
  interval-packing observation — certify it as its own small lemma before
  attempting 3c; it sharply narrows the search (the dominant prime at step `n` is
  provably small relative to `n`, not merely finite-per-step).

- **3c. Key open lemma — second-moment concentration (the actual hard gap).** Fix
  `N` large. Let `Q_N:=\{q(n):1\le n\le N\}` (primes that were ever the Domination
  Lemma's dominant witness up to step `N`), `r_N:=|Q_N|`; by 3b, every element of
  `Q_N` is `\le C\log_2a_{N+1}=O(\log N)`. *Attempt:* bound `r_N` via
  Cauchy–Schwarz on `\sum_{q\in Q_N}D_N(q)` (large, driven by the Domination
  Lemma's per-step lower bounds summed over `n\le N` — derive the exact
  bookkeeping) versus `\sum_{q\in Q_N}D_N(q)^2` (bounded above via 3b's range
  `q=O(\log N)` combined with the interval-packing bound of 3b squared, and
  Mertens' second theorem `\sum_{p\le x}1/p^2=O(1)`, `\sum_{p\le x}1/p=O(\log\log
  x)` — KB "standard inequalities"). If the two bounds are incompatible unless
  `r_N=O(1)`, this proves `(\star)`. **Honest risk flag:** a naive
  `\sum_qD_N(q)` over *all* primes (not just dominant ones) is expected to be
  `\Theta(N\log\log N)` by the normal order of `\omega(a_i)\sim\log\log a_i`
  (Erdős–Kac-type heuristic), not `\Theta(N)` — so the inequality chain must be
  built carefully around the *dominant*-prime sum specifically, or the
  second-moment bound will not close. Treat this as genuinely open research-level
  algebra, not a routine verification; if it stalls, use 3c′.

- **3c′. Fallback mechanism — extend Lemma R (certified by sibling
  `intersecting-family-covering-construction`).** Lemma R gives, for each fixed
  index `i`, some prime of `P_i` dividing infinitely many later terms ("eternal
  witness for `i`"). If the eternal witnesses for `i=1,2,3,\dots` can be shown to
  be *eventually always drawn from one fixed finite set* (rather than potentially
  a new prime for every `i`), that directly gives `(\star)`. Not attempted this
  round; flagged as the alternative if 3c's density route does not close.

**Section 6 (periodicity-from-`n=1`) — do not pursue as a separate injectivity
patch.** Round-2 exploration (`/tmp/round-2/math-explorer-periodicity-from-n1.md`)
confirms Lemma Q and Lemma S′ get periodicity-from-1 "for free" because they
strong-induct from `n=1` directly, never invoking pigeonhole; it also confirms
(against the problem's literal statement, and against two independent crux
analogues `aimo-0648`, `aimo-0678`, both of which only demand *eventual*
periodicity, unlike this problem) that "eventually periodic" genuinely does not
suffice here — there is no cheap reinterpretation. Recommend NOT pursuing the
finite-state-injectivity route sketched in Section 6 below as the primary plan
(still logically valid but a strictly harder architecture, and no additional
mechanism for proving injectivity has been found); instead, once `(\star)` is
proved here, hand off to `intersecting-family-covering-construction`'s revised
strong-induction architecture (its own Round 2 Outline), which gets
periodicity-from-1 as a structural byproduct of the same induction that pins down
the covering set, rather than as a separate step. Section 6's injectivity content
below is retained for reference / as a last-resort fallback only.

---

## Approaches tried
- **Backbone-existence via CRT + finite-state pigeonhole** (this round, full build from
  the outliner's skeleton). I fully proved the two "free" preliminary lemmas (stated and
  proved from scratch, not merely cited), proved a strengthening of Free Lemma P to *every*
  pair of indices (not just against `a_1`), formalized the "P_1-label" / backbone framework
  precisely enough to state exactly what a "recruitment" is, and then proved a genuinely new
  counting fact — the **Domination Lemma** — which is the first concrete, fully rigorous
  version of the "rate inequality" the outline-reviewer demanded for Step 3. This lemma shows
  that admissibility of `a_{n+1}` forces *at least one* of its prime factors to already divide
  a `1/ω(a_{n+1})`-fraction of `a_1,...,a_n`. This is real, checked progress on the central
  gap, but it does **not** close it: turning "some prime is locally dominant at each step"
  into "only finitely many primes are *ever* dominant" still requires an a priori control on
  `ω(a_n)` (equivalently, a growth-rate bound on `a_n` in terms of `n`) that this approach has
  not established, and which is itself exactly the open content of the sibling approach
  `bounded-gap-density-covering`. I also examined the actual solution of crux `aimo-0648` in
  the corpus (not just its one-line summary) and found that its Bezout-combination device
  does **not** transfer to the "periodicity from `n=1`" requirement the way the outline
  assumed — that crux propagates an *already-established* periodic maximality property
  backward *within* the periodic regime, not across a genuine pre-periodic transient. I
  replaced it with a more accurate (but still open) target: injectivity of the eventual
  finite-state transition map. Net outcome: real structural progress, both open gaps (backbone
  finiteness, periodicity-from-1) remain honestly unresolved and are now stated more
  precisely than in the outline. Reporting `partial` rather than patching over the gap.

## Current best

### 0. Setup and notation
Throughout, `(a_n)_{n≥1}` is the sequence defined in the problem: `a_1>1` fixed, and for
every `n≥1`, `a_{n+1}` is the least integer `> a_n` with `gcd(a_{n+1},a_i)>1` for every
`i=1,...,n`. For a positive integer `m`, write `rad(m)` for the set of primes dividing `m`,
and `ω(m) = |rad(m)|`. Write `P_1 := rad(a_1) = \{p_1,\dots,p_k\}`, `k=|P_1|\ge 1`.

### 1. Free Lemma P and its strengthening (fully proved)

**Lemma P (permanent hub).** For every `n ≥ 2`, `gcd(a_n,a_1) > 1`.

*Proof.* By definition, `a_n` was chosen (as the `(n-1)`-th successor, i.e. at the step
producing `a_{(n-1)+1}=a_n`) to satisfy `gcd(a_n,a_i)>1` for every `i=1,\dots,n-1`; taking
`i=1` (valid since `n-1\ge 1`) gives `gcd(a_n,a_1)>1`. ∎

**Lemma P′ (every index is a permanent hub for its successors).** For every `1≤i<j`,
`gcd(a_i,a_j) > 1`.

*Proof.* Exactly as in Lemma P: `a_j` is produced at the step defining `a_{(j-1)+1}=a_j`,
which by the problem's definition requires `gcd(a_j,a_m)>1` for every `m=1,\dots,j-1`.
Since `i\le j-1`, taking `m=i` gives `gcd(a_i,a_j)>1`. ∎

Lemma P′ shows the family of finite sets `P_n := rad(a_n)` (`n\ge1`) is **pairwise
intersecting**: `P_i\cap P_j\ne\varnothing` for all `i<j` — a stronger structural fact than
Lemma P alone, since it holds against *every* earlier index, not only against `a_1`.
(Knowledge base: this is a direct application of the problem's own defining recursion, not
an external theorem; recorded here because every later step of this approach uses it.)

### 2. Free Lemma Q (prime-power base case, fully proved)

**Lemma Q.** If `a_1 = p^e` for a single prime `p` (in particular whenever `a_1` is even,
taking `p=2`), then `a_n = a_1 + p(n-1)` for every `n\ge1`; consequently `T=1,\ L=p` satisfy
`a_{n+1}=a_n+L` for every `n\ge1`.

*Proof.* Induct on `n`. The claim holds for `n=1` trivially. Suppose `a_1,\dots,a_n` are all
multiples of `p` (true for `n=1`, and it is the induction hypothesis for general `n`). Since
`P_1=\{p\}`, Lemma P forces every candidate `x>a_n` for `a_{n+1}` to satisfy `p\mid x` (as
`\gcd(x,a_1)=\gcd(x,p^e)>1` iff `p\mid x`). Among `a_n+1,\dots,a_n+p-1`, none is a multiple of
`p` (they lie strictly between two consecutive multiples of `p`, since `p\mid a_n`), so none
is admissible. The next candidate `a_n+p` is a multiple of `p`; since by the induction
hypothesis every one of `a_1,\dots,a_n` is also a multiple of `p`, we get
`\gcd(a_n+p,a_i)\ge p>1` for every `i\le n` — so `a_n+p` is admissible, and it is the least
integer greater than `a_n` that is a multiple of `p`, hence the least admissible candidate.
Thus `a_{n+1}=a_n+p`, completing the induction. ∎

From here on we assume `k=|P_1|\ge 2` (Lemma Q disposes of `k=1` completely, exactly, from
`n=1`).

### 3. The backbone / label framework (definitions, fully rigorous)

By Lemma P, every `a_n` (`n\ge2`) is divisible by at least one prime of `P_1`. Define the
**label** `\ell(n) := P_n\cap P_1` for `n\ge2` (a nonempty subset of `P_1`); this is
well-defined since `P_n=rad(a_n)` is a specific finite set, no choice is made.

Because `\ell(i)\cap\ell(j) = P_i\cap P_j\cap P_1`, we get, for `2\le i<j`:
- if `\ell(i)\cap\ell(j)\ne\varnothing`, the pairwise constraint `\gcd(a_i,a_j)>1`
  (guaranteed to hold by Lemma P′) is **witnessed by a prime of `P_1`**, and no prime outside
  `P_1` is needed to explain that particular pair;
- if `\ell(i)\cap\ell(j)=\varnothing`, then since `\gcd(a_i,a_j)>1` still holds (Lemma P′),
  `P_i\cap P_j` is nonempty but disjoint from `P_1` — the pair is witnessed by some prime
  **outside** `P_1`.

Call a prime `q\notin P_1` a **recruit at the pair `(i,j)`** if `q\in P_i\cap P_j` and
`\ell(i)\cap\ell(j)=\varnothing`. The outline's "backbone growth process" `H_n` is precisely:
`H_n := P_1 \cup \{q : q \text{ is a recruit at some pair } (i,j),\ i<j\le n\}`. This is a
non-decreasing (in `n`) sequence of finite sets by construction (a finite union of finite
sets at each stage). **Backbone finiteness** is exactly the claim `\bigcup_n H_n` is finite.

### 4. The Domination Lemma (new, fully proved this round)

This is the concrete inequality the outline-reviewer required in place of the outline's
unquantified "rate" language.

**Domination Lemma.** For every `n\ge1`, let `x:=a_{n+1}` and let `q_1,\dots,q_r` be the
distinct prime factors of `x` (so `r=\omega(x)`). For a prime `q`, let
`D_n(q):=|\{i\le n : q\mid a_i\}|`. Then
$$\sum_{j=1}^r D_n(q_j) \;\ge\; n, \qquad\text{hence}\qquad \max_{1\le j\le r} D_n(q_j)\;\ge\;\frac n r=\frac{n}{\omega(a_{n+1})}.$$

*Proof.* By admissibility of `x=a_{n+1}`, for every `i\in\{1,\dots,n\}` we have
`\gcd(x,a_i)>1`, i.e. some prime factor of `x` divides `a_i`; equivalently `i` belongs to
`S_j:=\{i\le n: q_j\mid a_i\}` for at least one `j\in\{1,\dots,r\}`. So
`\{1,\dots,n\}=\bigcup_{j=1}^r S_j`, and by the union bound (finite subadditivity of
cardinality),
$$n=|\{1,\dots,n\}|=\Big|\bigcup_{j=1}^r S_j\Big|\le\sum_{j=1}^r|S_j|=\sum_{j=1}^r D_n(q_j).$$
The averaging (pigeonhole) inequality `\max_j D_n(q_j)\ge \frac1r\sum_j D_n(q_j)\ge n/r`
follows immediately. ∎

**Interpretation.** At *every* single step `n`, admissibility of `a_{n+1}` forces at least
one of its own prime factors to already be "load-bearing" for a `1/\omega(a_{n+1})`
proportion of all previous terms. This is exactly the missing explicit rate the
outline-reviewer asked for on one side of the comparison ("rate at which the density bound
resolves [indices]"); the corresponding elementary bound on the other side (the number of
distinct primes recruited) is `\omega(x)\le\log_2 x` (each of the `r` distinct prime factors
of `x` is `\ge2`, so `x\ge2^r`), giving unconditionally
$$\max_{1\le j\le r} D_n(q_j) \;\ge\; \frac{n}{\log_2 a_{n+1}}.$$

### 5. Precisely where this approach's finiteness gap remains open

The Domination Lemma shows that *each* step `n` has a "dominant" prime `q(n)` (one of
`a_{n+1}`'s prime factors) with `D_n(q(n)) \ge n/\log_2(a_{n+1})`. To convert this into
**backbone finiteness** — the claim that only finitely many primes are ever recruited outside
`P_1` and that the recruiting process terminates — one would need, at minimum, both of the
following, and I was not able to establish either within this round's time budget:

(a) **A growth control on `a_n`.** If `a_n = O(n\cdot\mathrm{polylog}(n))` (in particular any
    bound giving `\log_2 a_{n+1}=o(n)`), then `D_n(q(n))\to\infty`, i.e. the dominant prime at
    step `n` divides an unboundedly growing *number* of earlier terms. Without such a bound,
    `\log_2 a_{n+1}` could in principle be comparable to `n` itself (if `a_n` grew, say,
    exponentially), making the Domination Lemma's conclusion vacuous (`D_n(q(n))\ge O(1)`).
    Establishing `a_n=O(n\cdot\mathrm{polylog}(n))` a priori — i.e. a genuine gap bound on
    `d_n=a_{n+1}-a_n` not assuming backbone finiteness already — is precisely the open content
    flagged as Step 2 of the sibling approach `bounded-gap-density-covering`; I confirm from
    this approach's own vantage point that the two approaches' open gaps are the same
    underlying missing fact, approached from different directions (density-of-witnesses here
    vs. direct gap bound there).

(b) **Turning "one dominant prime per step" into "finitely many primes dominant across all
    steps."** Even granting (a), the Domination Lemma only guarantees *existence* of a
    dominant prime at each `n`; it does not by itself bound how many *distinct* primes ever
    play this role as `n\to\infty` (in principle a different prime could dominate at each
    step, provided `D_n(q(n))` still grows — e.g. if new primes `q(n)` are recruited that
    each happen to divide an already-large and growing set of earlier terms, which is not
    ruled out by the lemma as stated). A further argument — e.g. showing `D_n(q)` for a "used
    once" prime `q` cannot itself keep growing without `q` being reused, or a second
    Turán/Kubilius-type second-moment bound on `\sum_p D_n(p)^2` to force concentration on
    `O(1)` primes — would be needed, and is not attempted here beyond this identification.

I want to be explicit that (a)+(b) are **not** minor bookkeeping: they are exactly the
"actual hard inequality" the outline flagged as the open gap in Step 3, now stated with a
concrete, correct, and unconditionally proved partial inequality (the Domination Lemma)
supplying one side of the needed comparison, while the other side (growth control on `a_n`,
and concentration on finitely many dominant primes) remains open.

### 6. Correction to the outline's Step 6 mechanism, and a better-posed replacement target

The outline proposed closing "periodicity holds from `n=1`, not just eventually" via crux
`aimo-0648`'s Bezout-combination device. I checked `aimo-0648`'s actual solution (not only its
one-line summary) in the crux corpus: there, the sequence is *already known* to be eventually
periodic with period `T` over indices reduced mod `T`, and the Bezout combination
`\sum c_id_i\equiv1\pmod T` is used to propagate the property "`x_n` equals the periodic
maximum `M`" **backward by one step within the already-periodic regime** (from `x_n=M` to
`x_{n-1}=M`, both indices already inside the eventually-periodic tail). It is not a device for
extending a periodicity established only from some index `N_0` onward back across the
transient `n<N_0` to indices that may not even be described by the same finite-state
recurrence. So this crux does **not**, on inspection, supply the mechanism the outline
attributed to it, and I flag this as a correction rather than attempt to force the analogy.

A more accurate (but still open) target for the "periodicity from `n=1`" requirement, *given*
that backbone finiteness (Section 5) were established: once a finite backbone `H^\*` and an
associated finite state space `S` are constructed so that the transition `s_n\mapsto s_{n+1}`
is a well-defined deterministic function `F:S\to S` for **all** `n\ge1` (not merely
`n\ge N_0` — the state description would need to be built so it is valid from the start, e.g.
by encoding, alongside the residue of `a_n\bmod L^\*` where `L^\*=\mathrm{lcm}(H^\*)`, the
finite record of exactly which among `a_1,\dots,a_n` are not yet automatically covered by
`H^\*`-divisibility, capped by a bound coming from part (b) above), then: pigeonhole gives
some repeat `s_m=s_{m+T}`; if in addition `F` is **injective on its image** (equivalently, the
forward orbit of `s_1` under `F` never re-enters itself except at a genuine cycle point, i.e.
there is no "tail" leading into the cycle), a standard fact about deterministic maps on finite
sets — every element of a finite set under an injective self-map lies on a cycle, since
injectivity forces the map restricted to any forward orbit to be a bijection onto that orbit —
gives periodicity from `s_1` itself, i.e. from `n=1`. This reduces the "no transient" claim to
an injectivity property of `F`, which I have **not** proved (nor found a counterexample to);
it is a cleaner and more honest open target than the Bezout device the outline suggested, and
is left as the precise remaining content of Step 6.

### Summary of what is and is not established

Fully proved this round: Lemma P, Lemma P′, Lemma Q (complete disposal of `|P_1|=1`), the
pairwise-intersecting structure of `\{P_n\}`, the label/backbone definitions, and the
Domination Lemma. Not established (open, honestly flagged, not papered over): (a) a growth
bound on `a_n` sufficient to make the Domination Lemma's conclusion non-vacuous; (b)
concentration of dominance onto finitely many primes; (c) injectivity of the eventual
finite-state transition map (needed for periodicity from `n=1`, once (a)-(b) are resolved).
Gaps (a)+(b) together constitute "backbone finiteness"; gap (c) is the sharpening step. Both
remain open. No claim beyond what is proved above is asserted as established.

## Full proof
(Not present — Status is `partial`; see Current best for exactly what is proved and what
remains open.)

## Promotable lemmas

- **Lemma P (permanent hub).** For every `n\ge2`, `\gcd(a_n,a_1)>1`. Proved in Section 1
  above from the problem's own recursive definition (one line). Reusable by any approach to
  this problem.
- **Lemma P′ (pairwise global intersection).** For all `1\le i<j`, `\gcd(a_i,a_j)>1`; hence
  `\{P_n=rad(a_n)\}_{n\ge1}` is a pairwise-intersecting family of finite sets. Proved in
  Section 1. Strictly stronger than, and immediately implies, Lemma P (`i=1` case); reusable
  by the `intersecting-family-covering-construction` approach directly (it already assumes
  this fact informally; this file supplies a from-scratch proof of it).
- **Lemma Q (prime-power base case).** If `a_1=p^e`, then `a_n=a_1+p(n-1)` for all `n\ge1`,
  so `T=1,L=p` exactly from `n=1`. Fully proved by induction in Section 2. Disposes of the
  entire `|P_1|=1` family (including every even `a_1`) for every approach.
- **Domination Lemma.** For every `n\ge1`, writing `x=a_{n+1}` with distinct prime factors
  `q_1,\dots,q_r`, and `D_n(q)=|\{i\le n:q\mid a_i\}|`: `\sum_{j=1}^r D_n(q_j)\ge n`, hence
  `\max_j D_n(q_j)\ge n/\omega(a_{n+1})\ge n/\log_2 a_{n+1}`. Proved in Section 4 by a union
  bound / pigeonhole argument, fully elementary and unconditional (no hypotheses beyond the
  problem's own definition). This is new content beyond the round-1 outline and directly
  answers the outline-reviewer's request for an explicit "rate" inequality; any approach
  attacking backbone/covering-system finiteness (this one or `bounded-gap-density-covering`)
  can import it as the starting point for a growth-rate argument.
