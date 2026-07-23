## imo-2026-06

### Field-wide correction applied this round
Round-2 exploration (`math-explorer-alt-framing.md`) numerically refuted
`backbone-existence-crt`'s literal Section-3 "backbone finiteness" target
(`H_n` = primes ever co-occurring as *any* pairwise gcd witness): even in the
already-solved `a_1=15` case, 2948 incidental cross-pair primes appear among
index pairs 50–400 alone (root cause: the definition accepts *any* common
prime of two already-fixed integers, not a canonical/minimal witness — a
sanity check confirms the *minimal* common prime for the offending example is
`2`, not the incidental `17`). Both revised approaches below retarget at
`(\star)`: **`B := {p prime : p | a_n for infinitely many n}` is finite** — the
persistent-divisor set, which is what actually governs eventual periodicity.
I also caught and fixed my own over-claim while drafting the new 4th approach:
an initial "explicit bound `N_0 ≤ |P_1|+1`" on when the global intersection
`∩_{i≤n} rad(a_i)` first empties is **false** (`a_1=65` collapses at `N_0=4 >
|P_1|+1=3`, verified numerically) — the corrected lemma (Lemma C below) only
claims finite stabilization, not a small explicit bound. Recorded as a rule
for next round.

---

backbone-existence-crt: revise
Target: there exist `T,L>0` with `a_{n+T}=a_n+L` for every `n\ge1`.
Technique: counting/density — Domination Lemma (union bound / pigeonhole) +
interval-packing + second-moment (Cauchy–Schwarz + Mertens' second theorem),
distinct in mechanism from the sibling's explicit-construction route.
Skeleton:
  1. Lemma P, P′, Q (imported, certified, unchanged) — the permanent-hub facts
     and the prime-power base case, disposing of Case I's prime-power
     sub-family.
  2. Domination Lemma (imported, certified, unchanged) — at every step, some
     prime factor of `a_{n+1}` divides `\ge n/\omega(a_{n+1})` of the previous
     terms, by a union-bound/pigeonhole argument.
  3. NEW — retarget at `(\star)`: `B` finite, via
     3a. `q\in B \iff D_n(q)\to\infty` (trivial monotonicity observation).
     3b. `O(\log n)` dominant-prime bound (cheap, 3 lines from 2 certified
         lemmas + 1 new trivial interval-packing bound `D_n(q)\le(n-1)L/q+1`):
         combine with the Domination Lemma's lower bound to get
         `q(n)=O(L\log_2 a_{n+1})=O(\log n)`.
     3c. Second-moment concentration (open, the hard gap): Cauchy–Schwarz on
         `\sum_{q\in Q_N}D_N(q)` vs `\sum_{q\in Q_N}D_N(q)^2`, bounding the
         latter via Mertens' second theorem restricted to the `O(\log N)`-
         bounded prime range from 3b, to force `r_N=|Q_N|=O(1)`.
     3c′. Fallback: extend Lemma R (import from sibling) — show eternal
         witnesses for `i=1,2,\dots` eventually confine to one fixed finite
         set.
  4. Once `(\star)` holds, hand off to `intersecting-family-covering-
     construction`'s Step 5 (strong induction from `n=1`) rather than pursuing
     a separate finite-state-injectivity argument for periodicity-from-1.
Key lemmas (claim + mechanism):
  - `O(\log n)` dominant-prime bound — because the Domination Lemma's
    per-step lower bound on load and a trivial interval-packing upper bound
    (at most `(n-1)L/q+1` terms in an `O(n)`-length interval are divisible by
    a fixed prime `q`) together force `q(n)` small relative to `n`.
  - Second-moment concentration (open) — because Cauchy–Schwarz turns a large
    total "dominance budget" (`\sum D_N(q)` over dominant primes only, not all
    prime factors — the Erdős–Kac-type `\Theta(N\log\log N)` growth of the
    *all-prime-factor* sum is a genuine trap to avoid) against a Mertens-
    bounded second moment into a bound on the *count* of distinct dominant
    primes.
Open gaps: 3c (second-moment concentration itself — genuinely open,
research-level algebra, not routine); 3c′ as fallback if 3c stalls.
Cases to cover: none beyond the existing Case I / Case II dichotomy (Case I
already fully solved by Lemma Q/S′, imported).
Watch out for: do not resurrect the literal `H_n` definition (falsified); do
not let the second-moment sum run over *all* prime factors instead of
*dominant* ones (the Erdős–Kac trap above); do not treat 3c as a quick
verification — flag honestly if it doesn't close and route to 3c′.

---

intersecting-family-covering-construction: revise
Target: there exist `T,L>0` with `a_{n+T}=a_n+L` for every `n\ge1`.
Technique: explicit construction + strong induction from `n=1`, mirroring
Lemma S′'s own architecture (distinct in mechanism from the sibling's
counting/density route for the same target lemma).
Skeleton:
  1. Lemma P, Q, Lemma R, Lemma S′ (imported, certified, unchanged) — the
     dichotomy fully solving Case I from `n=1`.
  2. Case II dichotomy diagnosis (imported, unchanged) — the "reduce `k`"
     induction terminates only in Case I; correct, no revision needed.
  3. NEW — construct `H` (persistent covering set): import `(\star)`
     from `backbone-existence-crt` once proved, or attempt independently via
     Lemma R extended across all indices (shared fallback 3c′ above — do not
     duplicate effort with the sibling without checking its latest state).
     Watch out: `H` need not equal `P_1\cup\{$extras$\}` — round-2 simulation
     shows `a_1=1001`'s eventual dominant set `\{2,7,11\}` *excludes*
     `13\in P_1` entirely; a hub prime of `a_1` can become permanently
     dormant.
  4. NEW — construct `R` (periodic residue pattern mod `L_H=\mathrm{lcm}(H)`)
     constructively (read off from the sequence once `H` and its early
     behavior are known), then prove **by strong induction from `n=1`** the
     invariant `I(n)`: "`a_n\bmod L_H` matches `R`'s pattern, AND every
     admissibility check up to `n` is witnessed by a prime in `H`, not an
     incidental outside prime." This single induction gets periodicity-from-1
     "for free," exactly as Lemma S′ already does for the single-prime case —
     no separate injectivity/backward-propagation step needed (confirmed by
     round-2 exploration against `aimo-0648` and `aimo-0678`: neither crux's
     own official solution eliminates a pre-period, because neither crux's
     own problem statement demands one — this problem does).
Key lemmas (claim + mechanism):
  - Invariant `I(n)`'s inductive step — because the greedy process's
    minimality forces the `H`-predicted candidate to be admissible (every
    earlier term's covering prime is by hypothesis already in `H`) and every
    strictly-smaller candidate to fail; ruling out intermediate candidates can
    require appeal to a *specific* non-`a_1` earlier index (confirmed by the
    `a_1=33` trace: candidate `44` passes the `i=1` check yet is correctly
    rejected via `a_3`), so `I(n)` must carry the *full* per-index history,
    not a compressed residue-only Markov state.
Open gaps: (1) finiteness of `H` (shared with `backbone-existence-crt`'s
`(\star)`); (2) the `I(n)` inductive step in general — not yet attempted for
any genuine multi-prime `H`.
Cases to cover: Case I done (Lemma S′); Case II is the target. Concrete first
test case for a builder: `a_1=15`, conjectured `H=\{2,3,5\}`, `T=8`, `L=30`
(work this by hand before generalizing).
Watch out for: assuming `H\supseteq P_1` with all of `P_1` permanently active
(false, see `a_1=1001`); compressing `I(n)` to a bounded-window state (shown
insufficient by the `a_1=33` trace).

---

persistent-backbone-monovariant: new
Target: there exist `T,L>0` with `a_{n+T}=a_n+L` for every `n\ge1`.
Technique: well-ordering / minimal-counterexample argument (adapted from crux
`aimo-0678`'s "min of a currently-forbidden set" device), a third, genuinely
different mechanism attacking the same `(\star)` target lemma — neither
counting/density nor explicit constructive verification. Opened per CLAUDE.md's
plateau-break rule: all three round-1 approaches shared exactly one wall
(concentration onto finitely many dominant primes).
Skeleton:
  1. Import Lemma P, P′, Q, S′, Lemma 1, Lemma R (free, all already certified).
  2. NEW Lemma C (Global Intersection Collapse) — `C_n:=\bigcap_{i=1}^n
     \mathrm{rad}(a_i)` is non-increasing (subsets of finite `P_1`), so
     stabilizes at some finite `N_0` to a limit `C_\infty`; `C_\infty\ne
     \emptyset \iff$ Case I. In Case II, `C_\infty=\emptyset` — global
     `P_1`-only agreement breaks by a finite, explicit-if-not-small index.
     Proof given in full in the approach file; cheap for a builder to certify.
  3. Define canonical minimal witness `w(i,j):=\min(\mathrm{rad}(a_i)\cap
     \mathrm{rad}(a_j))` (correcting the "any common prime" overcounting bug
     diagnosed in the `backbone-existence-crt` correction above — verified
     `w(52,324)=2`, not the incidental `17`, for the `a_1=15` example).
  4. OPEN — prove `\bigcup_n\{w(i,n):i<n\}` finite via minimal-counterexample
     / well-ordering: take the least step `n^\ast` at which a canonical
     witness larger than every previously-used one is forced to appear, and
     derive a contradiction from the greedy process's minimality (using Lemma
     1's gap cap and Lemma C's early-collapse structure). **Not completed —
     this is the approach's entire load-bearing content and is honestly
     exploratory**, on par with the still-open Step 3c/Step 5 gaps of the
     other two approaches. Fallback sub-goal (weaker, may be more tractable):
     show `\mu_n:=\max\{w(i,m):i<m\le n\}` is eventually constant.
  5. Once closed, hand off to `intersecting-family-covering-construction`'s
     Step 5 machinery to finish periodicity, as with the other routes.
Key lemmas (claim + mechanism):
  - Lemma C — because `C_n` is a nested decreasing sequence of subsets of the
    finite set `P_1`, hence stabilizes by finite descent, and `p` in the
    stable limit for all sufficiently large `n` forces `p` into *every*
    `\mathrm{rad}(a_i)`, i.e. Case I.
  - Well-ordering step (open) — proposed mechanism only, not proved: minimal
    counterexample on the canonical-witness sequence, using Lemma 1's gap cap
    to argue the greedy process cannot be "forced" into a genuinely new large
    witness without first exhausting smaller-witness options.
Open gaps: Step 4 in full (the core content of this approach).
Cases to cover: none beyond Case I/II (Case I imported, solved).
Watch out for: do NOT restate the false `N_0\le|P_1|+1` bound (caught and
corrected this round — verified false on `a_1=65`); use the canonical
*minimal* witness `w(i,j)`, never "any common prime" (that is exactly the bug
that falsified `backbone-existence-crt`'s original `H_n`).

---

bounded-gap-density-covering: parked (not advanced this round)
Reasoning: round 1's builder rigorously self-demonstrated the approach's
distinguishing Step 3 strategy (upgrade Lemma 1's boundedness to a finite
state "backbone-agnostically," without identifying which extra primes get
recruited) is a dead end — the natural refinement collapses onto exactly the
same backbone-finiteness question the other approaches attack (`current.md`,
Rules). Round-2 exploration did not surface a new mechanism specific to this
approach's original "density-only, backbone-agnostic" promise, and per the
dispatch instructions its original Step 3 strategy must not be re-opened.
Lemma 1 (`a_{n+1}-a_n\le\mathrm{rad}(a_1)`) remains certified, reusable, and is
already imported by all three active approaches above (it underlies the
interval-packing bound in `backbone-existence-crt`'s Step 3b and Lemma C's
finiteness argument in `persistent-backbone-monovariant`). No new skeleton is
proposed for this slug this round; leave it at its current Elo/status and
revisit only if a genuinely new mechanism for its original promise is found.
