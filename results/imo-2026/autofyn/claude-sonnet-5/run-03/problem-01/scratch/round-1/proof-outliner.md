## imo-2026-01

All three round-1 explorers (prime-exponent, sorting-confluence, confluence lenses)
converged independently on the same correct core mechanism: for a prime `p`, a
Confucius move sends the exponent pair `(v_p(m), v_p(n))` to `(min, |diff|)` — one step
of the subtractive Euclidean algorithm, applied simultaneously across all primes at the
two chosen board slots. Two elementary identities carry the whole proof:
`min(a,b)^2+|a-b|^2 \le a^2+b^2` (equality iff min=0) for termination, and
`gcd(min(a,b),|a-b|)=gcd(a,b)` for the invariant behind part (b). This round's field
puts up 4 approaches, all complete end-to-end attempts, diversified by HOW they
organize/present the rigor (per dispatch instructions) plus one genuinely different
proof *strategy* (induction) that currently has an honest, flagged gap.

---

lex-potential-gcd-invariant: new
Target: Prove both (a) termination with exactly one entry `>1`, and (b) that the
survivor `M` is order-independent, for the full 2026-number board.
Technique: Direct invariant/monovariant method (KB "Invariants & monovariants",
knowledge_base.md lines 117, 191). Per-prime reduction to the subtractive Euclidean
step; lexicographic potential `(N, Σ)` for termination; exact gcd-of-exponents
invariant `G_p` for uniqueness.
Skeleton:
  1. Per-prime reduction: a move sends `(v_p(m),v_p(n)) \to (\min,|diff|)` for every
     prime simultaneously — by direct computation of `v_p(gcd)` and `v_p(lcm/gcd)`.
  2. Part (a): `N` = count of entries `>1` never increases, and drops by exactly 1 iff
     `gcd(m,n)=1` — by `gcd(m,n)\cdot lcm(m,n)/\gcd(m,n) = mn > 1$ for `m,n>1$ (not both
     new entries can be 1).
  3. Part (a): `Σ = \sum_i\sum_p v_p(a_i)^2` strictly drops whenever `N` doesn't — by the
     monovariant identity `\min^2+|diff|^2 \le a^2+b^2`, strict when some shared prime
     has `\min>0`.
  4. `(N,Σ)` lex-decreases every move, well-founded on `\mathbb{N}^2`, so the process
     terminates; terminal `N` is exactly 1 (can't skip 2→0) — proves (a).
  5. Part (b): `G_p = \gcd$ of the 2026 `v_p`-exponents is exactly invariant under every
     move — by `\gcd(\min(a,b),|a-b|)=\gcd(a,b)` plus gcd-associativity over a multiset.
  6. At termination (one survivor `M`), the exponent multiset is all-zero except at `M`,
     so `\gcd = v_p(M)$; equating to the invariant `G_p` gives `v_p(M)=G_p` for every
     `p`, i.e. `M=\prod_p p^{G_p}$, fixed by the initial board alone — proves (b).
Key lemmas:
  - `\min(a,b)^2+|a-b|^2 \le a^2+b^2`, equality iff `\min(a,b)=0` — because
    `a^2+b^2-(a^2+(b-a)^2)=a(2b-a)\ge0` for `a=\min\le b=\max`.
  - `\gcd(\min(a,b),|a-b|)=\gcd(a,b)` — the standard Euclidean-algorithm identity
    `\gcd(a,b)=\gcd(a-b,b)`.
  - `gcd(m,n)\cdot lcm(m,n)/\gcd(m,n)=mn>1` for `m,n>1` — forces not-both-1.
Open gaps: none structurally; remaining work is write-up rigor — exhaustive case split
for the N-drop, explicit statement of lex well-foundedness, explicit one-line proof of
gcd-associativity-over-a-multiset-replacement.
Cases to cover: `gcd(m,n)=1` vs `gcd(m,n)>1` (with `m=n` as a sub-case of `>1`);
terminal N=1 not 0.
Watch out for: don't conflate `G_p` (gcd of exponents) with `\min_i v_p(a_i)` (=`v_p` of
gcd of the numbers) — different quantities; counterexample board `{2,3}` gives `M=6`,
not `gcd(2,3)=1`.

---

omega-linear-monovariant: new
Target: same full (a)+(b) claim, using a linear (not quadratic) termination
potential.
Technique: same invariant/monovariant KB entry, but replaces the sum-of-squares
potential with the additive quantity `Ω(x) = total prime factors of x with
multiplicity`, summed over the board — an exact-identity computation rather than a
squares inequality, arguably a cleaner write-up per the round's diversification ask.
Skeleton:
  1. Same per-prime reduction as above.
  2. `T = \sum_i \Omega(a_i) = \sum_p\sum_i v_p(a_i)` — exact identity
     `\Omega(g)+\Omega(q)=\sum_p\max(v_p(m),v_p(n))` for the touched pair, since
     `\min+|diff|=\max` pointwise.
  3. `\max(a,b)\le a+b`, equality iff `\min(a,b)=0`, so `T` is non-increasing, strictly
     decreasing (by `\Omega(\gcd(m,n))\ge1`) exactly when `gcd(m,n)>1`.
  4. Pair with `N` (same as sibling approach): `(N,T)` lex-decreases every move
     (T drops when gcd>1, N drops by 1 when gcd=1) — well-founded, terminates, terminal
     N=1.
  5. Part (b): reuse the `G_p` invariant argument verbatim (identical content to the
     primary approach — this approach's distinguishing content is entirely part (a)).
Key lemmas:
  - Exact identity `\Omega(g)+\Omega(q)=\sum_p\max(v_p(m),v_p(n))` — because
    `\min(a,b)+|a-b|=\max(a,b)` pointwise per prime.
  - `\max(a,b)\le a+b`, equality iff `\min(a,b)=0`.
  - Same `G_p` invariance lemma as the primary approach for part (b) — can import as a
    certified shared lemma from `results/imo-2026-01/lemmas/` once proved once.
Open gaps: write up the `(N,T)` case split fully; confirm `T` is a finite sum (trivial,
finitely many prime divisors across 2026 numbers).
Cases to cover: same two cases as primary approach.
Watch out for: `\Omega(g)+\Omega(q)=\Omega(m)+\Omega(n)` only holds when `gcd(m,n)=1` —
don't overclaim it as a general identity. This approach is a near-twin of the primary
one structurally (both lex-pair a count with a per-move-nonincreasing secondary
quantity); judge on write-up clarity, not as independent confirmation of correctness.

---

token-multiset-crt-reconstruction: new
Target: same full (a)+(b) claim, organized via a bijective "per-prime lane" reframing
that isolates the invariant as a fully self-contained, board-independent lemma.
Technique: same invariant/monovariant mechanism, reorganized: decompose the board state
into independent per-prime exponent-vector "lanes" (bijective via unique factorization),
prove the gcd invariant as an abstract single-lane fact (Lemma A) decoupled from
Confucius/other primes, prove termination via the same `(N,Σ)` potential (Lemma B,
where cross-prime coupling actually enters, via the legality condition), then
reconstruct `M` via unique factorization.
Skeleton:
  1. Bijection: board state ↔ collection of length-2026 exponent vectors, one per
     prime, via `x=\prod_p p^{v_p(x)}`.
  2. Lemma A (single-lane invariant): for one prime's lane alone, under the abstract
     rule "replace two coordinates by `(\min,|diff|)`", `G_p=\gcd$ of the whole lane is
     invariant — proved purely within `\mathbb{Z}_{\ge0}^{2026}`, no reference to other
     primes or actual numbers, via the same (I2)+associativity mechanism.
  3. Lemma B (cross-lane termination = part a): same `(N,Σ)` potential as the primary
     approach, phrased in lane language — this is where cross-prime coupling (shared
     legality condition) genuinely enters.
  4. Reconstruction (part b): at termination every lane is nonzero only at the survivor
     `M`'s position; apply Lemma A independently per prime to get `v_p(M)=G_p` for every
     `p`; reassemble `M=\prod_p p^{G_p}` via unique factorization (not literally CRT —
     flag and correct the "CRT" label to "unique factorization" in write-up).
Key lemmas:
  - Lemma A, decoupled per-prime gcd invariant — same identities as primary approach,
    stated as an abstract sequence fact for auditability.
  - Lemma B — same termination mechanism as the primary approach's part (a).
Open gaps: must state explicitly that Lemma A holds for ANY sequence of coordinate
pairs (order-independent by construction, since it never uses the legality condition) —
without implying it alone gives termination or legality; must correct "CRT" language to
plain unique factorization to avoid an inaccurate citation; Lemma B needs full write-out
(same case split as primary approach), not a "same as sibling" placeholder.
Cases to cover: same two cases as primary approach for Lemma B; primes dividing none of
the `a_i` (contribute `G_p=0`, i.e. `p^0=1`, don't appear in `M`).
Watch out for: this approach's value is purely organizational/expository (isolating the
per-prime argument as an auditable standalone lemma) — if the reviewer judges it adds no
rigor beyond the primary approach, it's a legitimate candidate to fold into or drop in
favor of the primary approach rather than force independent development every round.

---

induction-on-active-count: new
Target: same full (a)+(b) claim, via strong induction on the count of entries `>1`
(a genuinely different proof STRATEGY — induction with a self-contained 2-variable
reduction gadget — rather than a single global potential function over all 2026
entries), currently carrying an honestly-flagged incomplete step for part (a).
Technique: strong induction (KB general proof methods) + a two-entry Euclidean-style
sub-lemma as the reduction gadget; part (b) still supplied by the (strategy-independent)
`G_p` invariant shared with the other approaches.
Skeleton:
  1. Two-entry sub-lemma: isolating any pair `(m,n)`, `m,n>1`, and repeatedly playing
     ONLY that pair terminates (via the k=2 instance of the (I1)/(I2)-based potential)
     with the pair becoming `(1,\gcd(m,n))` in finitely many moves.
  2. Strong induction hypothesis on `k$ = count of entries `>1`: assume the claim (a)+(b)
     holds for any board with fewer than `k` active entries.
  3. Inductive step: isolate any two active entries, reduce them via step 1 to
     `(1,\gcd(m,n))` (case `\gcd>1`: k drops by 1; case `\gcd=1`: k drops by 2), then
     apply the induction hypothesis to the resulting smaller-active-count board.
  4. **Gap**: steps 1–3 as sketched only establish termination for the *particular*
     "finish one pair before starting another" strategy — NOT for arbitrary interleaved
     play, which is what "regardless of the choices of Confucius" requires. Closing this
     needs either falling back to the global `(N,Σ)` potential (redundant with the
     primary approach) or strengthening the induction to bound termination under
     arbitrary interleaving (extra, currently unproven, work).
  5. Part (b): import the `G_p` invariant lemma unchanged (it is strategy-independent by
     construction, so it needs no adaptation for this approach).
Key lemmas:
  - Two-entry self-reduction sub-lemma (a clean, easy special case, useful as a
    warm-up/sanity check regardless of whether the full induction closes).
  - `G_p` invariance (imported, same as sibling approaches).
Open gaps: THE main open gap — the induction as sketched is an existence argument for
one strategy, not a universal termination proof; must be strengthened (interleaving
argument) or conceded to fall back on the global potential, in which case this
approach's independent value for part (a) evaporates and it should be deprioritized.
Cases to cover: `\gcd(m,n)=1` (k drops by 2) vs `>1` (k drops by 1) in the sub-lemma;
arbitrary interleaving patterns for the still-open universality gap.
Watch out for: the classic "prove it works for one strategy, silently assume Confucius
plays that way" trap — the problem is universally quantified over Confucius's choices,
not existentially. If the interleaving gap resists a clean closing in the next round or
two, deprioritize this approach relative to the primary one rather than keep pouring
rounds into it.
