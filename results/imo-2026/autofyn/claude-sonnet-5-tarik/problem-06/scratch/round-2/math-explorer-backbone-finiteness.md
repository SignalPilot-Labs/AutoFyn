## imo-2026-06 (lens: backbone-finiteness / Case-II concentration)

### Scope of this report
Only the still-open "concentration" half of the shared gap: prove that only
finitely many distinct primes are ever *dominant* (Domination Lemma sense)
across all `n`, in Case II (no single prime saturates every term; witnessed
by `a_1=15`, stress-tested by `a_1=247`). "Growth control" is done (Lemma 1 +
Domination Lemma, `current.md` point 6) — not re-derived here.

### Distinct openings

1. **New, cheap, unproved-but-easy synergy: an explicit O(log n) size bound
   on the dominant prime itself (not just its count).** The Domination Lemma
   gives a *lower* bound `D_n(q(n)) ≥ n/ω(a_{n+1}) ≥ n/log_2(a_{n+1})` on the
   dominant prime's "load." Nobody has yet paired this with the *trivial
   upper* bound: since `a_1,…,a_n` are `n` distinct integers packed into the
   interval `[a_1,a_n]` of length `a_n-a_1 ≤ (n-1)L` (Lemma 1), any fixed
   prime `q` divides at most `⌊(a_n-a_1)/q⌋+1 ≤ (n-1)L/q + 1` of them, i.e.
   `D_n(q) ≤ (n-1)L/q+1` for *every* prime `q`, unconditionally. Combining
   the two: `n/log_2(a_{n+1}) ≤ D_n(q(n)) ≤ (n-1)L/q(n)+1`, which rearranges
   (for `n` large enough that `n/log_2(a_{n+1})>1`) to
   `q(n) = O(L·log_2(a_{n+1})) = O(log n)`. This is a genuinely new,
   three-line, fully elementary consequence of two *already-certified*
   lemmas (Lemma 1 + Domination Lemma) plus one new trivial interval-packing
   observation — cheap for a builder to certify as its own small lemma next
   round. It does **not** finish backbone finiteness by itself (an `O(log n)`
   bound is not a constant bound — the eligible prime pool could in
   principle keep slowly growing), but it sharply narrows the problem: the
   dominant prime at step `n` is provably *small* relative to `n`, not
   merely finite-per-step. This is the natural next building block before
   attempting concentration proper.

2. **Second-moment / Cauchy–Schwarz concentration (the genuine Turán/Kubilius
   idea), now made concrete.** With opening 1's bound in hand, consider
   `Σ_q D_n(q)^2` over the (now provably `O(log n)`-bounded, but still a
   priori unboundedly large in count) set of primes `≤ C log n`. The
   Domination Lemma's proof already shows `Σ_j D_n(q_j) ≥ n` is witnessed by
   a *union* `{1,…,n}=∪_j S_j`; a Cauchy–Schwarz argument on
   `Σ_q D_n(q)` vs. the *number of distinct q's that have ever been
   dominant* could show: if `r_n` distinct primes have each been dominant at
   least once by step `n`, then `Σ_q D_n(q)^2 ≥ (Σ_q D_n(q))^2/r_n`, and
   since each dominant event contributes `D_n(q(n))≥n/log_2(a_{n+1})` to its
   own prime's running total, `r_n` primes each carrying growing load forces
   `Σ_q D_n(q)^2` to grow at least quadratically in `n/r_n` — this should be
   compared against an upper bound on `Σ_q D_n(q)^2` coming from the
   interval-packing bound of opening 1 (`Σ_{q≤C log n} D_n(q)^2 ≤
   Σ_{q≤C log n} ((n-1)L/q+1)^2`, a convergent-in-shape sum by Mertens'
   second theorem `Σ_{p≤x}1/p^2 = O(1)` and `Σ_{p≤x}1/p = O(log log x)`).
   Nobody has carried this through; it is exactly the "second Turán/Kubilius
   moment bound" flagged as unattempted in `backbone-existence-crt.md`
   Section 5(b), and is the most promising concrete next move — a builder
   should attempt the algebra explicitly (it may show `r_n = O(1)`, or at
   least `r_n = o(log n)`, either of which is new progress).

3. **A genuinely different framing: hunt for a monovariant, not a density
   bound (see crux `aimo-0678` below).** All three round-1 approaches (and
   openings 1–2 above) attack concentration via counting/density. A
   structurally different route: define some order-preserved quantity on the
   process — e.g. `w_n := min{m ≥ a_n : m is NOT yet forced-admissible by
   the currently-recruited backbone}` or a "residue-defect" set analogous to
   the `W_n`/`w_n` construction in `aimo-0678` — and try to show it is
   *non-increasing* in `n` (not "bounded", non-increasing — a strictly
   stronger, well-ordering-based argument that sidesteps growth-rate
   estimates entirely). If such a monovariant exists and stabilizes, the
   stabilization point directly freezes the backbone with no density
   argument needed at all. This is unexplored territory for this problem
   and worth opening as a genuinely distinct rival approach (not a
   refinement of the existing three), per the plateau-break rule.

4. **Contrapositive-via-quotient (see crux `aimo-0727` below), run in the
   direction we actually have available.** `aimo-0727`'s proof assumes a
   quotient `b_k` is bounded and derives that all prime factors of the
   sequence are confined to a finite set (contradicting the problem's
   hypothesis of infinitely many primes dividing some term) — the reverse
   direction of what we want, but the *mechanism* — "boundedness of an
   auxiliary integer-valued quotient ⟺ confinement of all prime factors to
   a finite set" — is exactly the shape of statement backbone finiteness
   needs. Since we already have `a_n = O(n)` unconditionally (Lemma 1,
   unlike in `aimo-0727` where the analogous bound is *derived*, not given),
   there may be a natural "quotient" for our problem — candidates: `a_{n+1}/
   \gcd(a_{n+1}, \mathrm{lcm}(\text{current backbone}))`, or `\omega(a_{n+1})`
   itself — whose boundedness (already essentially forced by opening 1's
   `O(log n)` bound on `ω`, since `\omega(a_{n+1})\le\log_2 a_{n+1}=O(\log n)`
   is *not* itself a constant bound, so this needs a genuinely new quotient,
   not `\omega` itself) would directly hand us backbone finiteness by the
   same "confinement" logic. Flagged as promising but not worked out — the
   right quotient has not been identified.

### Candidate techniques
- Combine already-certified Lemma 1 + Domination Lemma with a new trivial
  interval-packing upper bound on `D_n(q)` (opening 1) — cheap, should be
  done first regardless of which deeper route is chosen.
- Second-moment / Cauchy–Schwarz concentration a la Turán/Kubilius on
  `Σ_q D_n(q)^2`, using Mertens' second theorem (`Σ_{p≤x}1/p=O(\log\log x)`,
  `Σ_p 1/p^2=O(1)`) to bound the RHS (opening 2).
- Monovariant / well-ordering search on a "defect set," directly modeled on
  `aimo-0678`'s `W_n`/`w_n` device (opening 3) — a genuinely different
  top-level framing, not a variant of the density approaches.
- Quotient-boundedness-confines-primes mechanism from `aimo-0727`, run with
  Lemma 1 already in hand (opening 4).
- No dedicated "covering system" / Erdős covering-congruence entry exists in
  `knowledge_base.md` — checked explicitly (grepped for "covering system",
  "covering congruence", "Erdős covering"; none found). The closest KB
  entries are **Dirichlet's theorem (primes in AP)**, **Pigeonhole / extremal
  principle**, and the **Order of an element / Fermat–Euler** entry's remark
  "eventual periodicity of products of a sequence mod m" (Number Theory
  section) — these are generic finite-state/pigeonhole tools, not a
  ready-made covering-system machine; any covering-system-flavored argument
  here would have to be built from scratch using Pigeonhole + CRT, not cited
  wholesale.

### Cheap-kill candidates
- The `O(log n)` dominant-prime-size bound (opening 1) is essentially free
  (three lines from two certified lemmas) — worth certifying as its own
  lemma before spending builder time on the harder concentration argument,
  since it may already suffice as a building block or reveal the right
  quotient for opening 4.
- No parity/pigeonhole one-line kill of the whole gap is visible; the gap is
  genuinely a counting/structural argument, not a short trick.

### Knowledge-base entries to use
- **Order of an element, Fermat/Euler** (`knowledge_base.md`, Number Theory
  section): "periodicity of `aⁿ mod m`; eventual periodicity of products of a
  sequence mod `m`" — generic finite-state justification once a backbone
  modulus is fixed.
- **Dirichlet's theorem (primes in AP)** — not directly load-bearing for
  concentration, but relevant if the outliner wants to *construct* a
  specific finite covering set once finiteness is known.
- **Pigeonhole / extremal principle** (Combinatorics section) — the raw tool
  behind the Domination Lemma and Lemma R; the second-moment argument
  (opening 2) is an averaging refinement of the same family.
- **Standard inequalities: Cauchy-Schwarz** (KB opening lines) — needed
  explicitly for opening 2's `Σ D_n(q)^2` argument.

### Analogous past problems (cruxes)
- **`aimo-0678`** (IMO Shortlist 2015 N4: prove `a_n` eventually periodic for
  `a_{n+1}=\gcd(a_n,b_n)+1,\ b_{n+1}=\mathrm{lcm}(a_n,b_n)-1`). **Best analog
  found** — same top-level target (eventual periodicity of a deterministic
  greedy/arithmetic integer sequence) via a completely different mechanism
  than any of our three approaches: define `s_n=a_n+b_n`,
  `W_n=\{m\ge a_n: m\nmid s_n\}`, `w_n=\min W_n`; prove `(w_n)` is
  **non-increasing** (a genuine monovariant, not a density bound), hence
  eventually constant `=w`; then show a secondary quantity
  `g_n=\gcd(w,s_n)` is *also* eventually constant, giving a fully
  finite-state description and periodicity by direct construction (no
  pigeonhole-on-density needed at all). This is the crux move behind opening
  3 above — genuinely worth trying to adapt (find the analogous "forbidden
  defect set" for our problem) as a fourth, structurally distinct approach,
  not a patch to the existing three.
- **`aimo-0727`** (IMO Shortlist 2023, N-numbered: `a_{k+1}\mid
  2(a_1+\cdots+a_k)`, prove "infinitely many primes divide some term" implies
  "every `n` divides some term"). Crux move: define quotient
  `b_k=2(a_1+\cdots+a_{k-1})/a_k`; prove `b_{k+1}\le b_k+1` (almost
  monotone) and that boundedness of `(b_k)` would confine all prime factors
  of the `a_k` to a finite set. The "bounded quotient ⟺ finite prime
  confinement" mechanism (opening 4) is the closest corpus match to what
  backbone finiteness itself asserts, run in the direction we'd want
  (finite prime set) rather than the direction the crux proves it in
  (contradiction from assumed infinitude) — worth studying closely for the
  right quotient to define on our sequence.
- **`aimo-0447`** (USAMO 2014: `\gcd(a+i,b+j)>1` for `0\le i,j\le n` implies
  `\min(a,b)>(cn)^{n/2}`). Weaker analogy — different top-level target (a
  size lower bound, not periodicity) — but its proof technique (bound each
  individual prime's occupancy of an `N\times N` grid by
  `(\lceil N/p\rceil)^2`, then sum over primes using
  `\Sigma_p 1/p^2 <\frac12` and PNT to bound the count of small primes) is
  structurally the *same shape* as opening 1/2's interval-packing +
  Mertens argument, giving independent corpus confirmation that this
  "per-prime occupancy bound, then sum via Mertens" technique is a standard,
  provable move — not a novel risk. Cite as a technique precedent, not as a
  problem-level analog.
- Not analogous (checked and rejected): `aimo-0514` (USAMO 2021 planar-graph
  turning walk — "reversibility ⟹ purely periodic" mechanism is about a
  *bijective* finite-state map, which is exactly the *other* open gap
  (periodicity-from-`n=1`), not this lens's concentration gap; flagging for
  whichever future round attacks that gap instead) and `aimo-0916` (IMO-SL
  2020 saddle pairs — same-subtopic keyword hit only, no real structural
  match).

### Prior progress
See `current.md` points 1–7 (not repeated in full here). Relevant to this
lens specifically: Domination Lemma (`lemmas/domination-lemma.md`) and
Lemma 1 (`lemmas/lemma-1-uniform-gap-bound.md`) are both certified and
reusable; their combination already gives `D_n(q(n))\to\infty`
unconditionally (current.md point 6, already done, not to be re-derived).
Nothing yet establishes finiteness of the *set* of primes that ever attain
the role of `q(n)`.

### Dead ends (do not retry)
- `bounded-gap-density-covering`'s original Step 3 (trace/hitting-set
  refinement, "backbone-agnostic" upgrade of boundedness) — self-proven dead
  end (collapses to the same backbone-finiteness question, illustrated by
  `a_1=65`). Per dispatch instructions, not retried here, and I confirm on
  inspection this is a real dead end, not a hasty one: the refinement's
  failure mode (singleton traces `{5}`,`{13}` forcing the hitting set back
  to all of `P_1`) is a correct diagnosis, and the primes that empirically
  rescue the process (2, 3) are exactly outside `P_1`, which the
  trace-on-`P_1`-only refinement structurally cannot see.
- `minimal-witness-index-descent` — cut pre-build in round 1 (Tight(n)
  degenerates to the trivial singleton `{n}` since the recursion already
  forces `\gcd(a_n,a_{n+1})>1`). Confirmed still correctly dead; irrelevant
  to this lens's gap in any case (it targeted periodicity-from-1, not
  concentration).

### Small-case / intuition notes (numerically verified this round, all
labeled conjecture, not proof)
- Simulated `a_1\in\{15,65,105,247,1001\}` (up to 4000–6000 terms each,
  `math.gcd`-based greedy, `sympy`-free trial-division factoring). In
  **every** case, the set of primes that ever attain the Domination Lemma's
  argmax role (`q(n)`) **stabilizes to a small fixed finite set very early**
  — e.g. `a_1=247`: dominant primes `\{2,19,13,3\}`, all first-seen by step
  `n=19`, then *no new dominant prime for the remaining ~5980 simulated
  steps*; `a_1=1001=7\cdot11\cdot13`: dominant primes `\{2,11,7\}`, last new
  one (`7`) first-seen at `n=282`, none after; `a_1=15`: `\{2,5,3\}`, all by
  `n=3`. This is strong empirical support for backbone finiteness itself
  (as opposed to the different, already-refuted claim that *all* primes
  ever dividing some term are finite — confirmed false again this round:
  for `a_1=247` over 4000 terms, 233 distinct primes divide *some* term,
  confirming the round-1 memory note that only the *dominant*-prime notion,
  not "any prime factor," can be finite).
- Verified numerically that the new `O(\log n)` bound of opening 1 holds
  with a small constant in practice: for `a_1=247`, `q(n)/\log_2(a_{n+1})`
  never exceeds `\approx2.36` over 3000 simulated steps (and that peak
  occurs at `n=2`, i.e. very early — the ratio does not grow with `n` in
  practice, suggesting the true bound is far tighter than the `O(\log n)`
  the elementary argument gives, consistent with the empirical
  early-stabilization above).
- Interesting and slightly surprising: the eventual dominant-prime set is
  **not** always all of `\mathrm{rad}(a_1)` plus a few extras — for
  `a_1=1001=7\cdot11\cdot13`, the eventual dominant set `\{2,11,7\}`
  *excludes* `13\in\mathrm{rad}(a_1)` entirely. This suggests any
  construction-based approach (opening 3/`aimo-0678`-style, or the existing
  `intersecting-family-covering-construction`) should not assume the
  backbone must contain all of `P_1`; some hub primes of `a_1` may become
  permanently "dormant" (never dominant, though still occasionally dividing
  some later term) once other primes take over.
