## imo-2026-01 — lens: per-prime exponent-vector analysis

The move on (m, n) sends it to (gcd(m,n), lcm(m,n)/gcd(m,n)). Factor m, n
prime-by-prime. For a prime p let the two exponents be (a, b). After the move
the exponents become (min(a, b), |a − b|) — because gcd carries min and
lcm/gcd carries max − min = |a − b|. This is exactly **one step of the
subtractive Euclidean algorithm** on the exponent pair (a, b) → (b, a − b) up
to order. The whole board therefore decomposes into 2026 exponent-tuples,
one per prime, each evolving independently under a Euclidean step applied to
two chosen coordinates. This factorization is the load-bearing crux of the
lens: the 2026-board problem reduces to many parallel 2-number Euclidean
games, one prime at a time.

### Distinct openings under this framing

1. **GCD-of-exponents invariant (the b-killer).** For two exponents (a, b),
   gcd(min(a,b), |a−b|) = gcd(a, b) — the standard Euclidean step preserves
   the pair's gcd. Since all other coordinates are untouched, the gcd of the
   *entire* multiset of v_p across the board, call it g_p, is invariant. In a
   terminal state (one M > 1, rest 1) the exponents of p are (e_p(M), 0, …, 0),
   whose gcd is e_p(M). Hence e_p(M) = g_p and
   **M = ∏_p p^{g_p}**, where g_p = gcd over all 2026 initial entries of v_p.
   This pins M uniquely — it is a function of the initial board only. (Checked:
   [12,18]→6, [9,27]→3, [4,8]→2, [100,72,45]→90, [2,3,5,7]→210.)
   Note gcd(0, k) = k, so g_p = gcd of the *nonzero* v_p (zeros contribute
   nothing); g_p = 0 only when no entry is divisible by p. Every prime that
   divides any initial entry has g_p ≥ 1, so M > 1 automatically.

2. **ΣΩ + count monovariant (the a-killer).** Let Ω(x) = total prime factors
   of x (with multiplicity). One move changes the pair's Ω-sum from
   Ω(m)+Ω(n) to Ω(gcd)+Ω(lcm/gcd) = Σ_p (min + |a−b|) = Σ_p max(a,b).
   The drop is Σ_p min(a,b) = Ω(gcd(m,n)). So:
   - m = n: drop = Ω(m) ≥ 1, count of >1 drops by 1 (two m's → m, 1).
   - m ≠ n, coprime: drop = 0, count drops by 1 (m, n → 1, mn).
   - m ≠ n, share a prime: drop = Ω(gcd) ≥ 1, count unchanged (both > 1).
   Define **F = (Σ_board Ω) + (#{entries > 1})**. In every case ΔF ≤ −1
   (≥ −2 when m = n). F is a nonneg integer, so the process terminates after
   finitely many moves. At termination no two entries are > 1, i.e. ≤ 1 entry
   > 1. It cannot be 0 entries > 1, because then every v_p would be 0 on the
   whole board, forcing g_p = 0 for all p — contradicting the invariant
   (initially some prime divides some entry, so some g_p ≥ 1, and g_p is
   preserved). Hence **exactly one M > 1**, and by opening 1 its value is
   ∏ p^{g_p}. Both parts done.

3. **Per-prime independent Euclidean game (structural view).** Because each
   prime's exponent-vector evolves by its own subtractive-Euclidean steps and
   the steps for different primes are coupled only through the *choice* of
   which two board positions to operate on, one may also argue directly: the
   subtractive Euclidean algorithm on a multiset of nonneg integers terminates
   with the gcd of the multiset concentrated in one coordinate and zeros
   elsewhere. Stacking this per prime gives the same M. This is a cleaner
   re-derivation of opening 1 but needs the coupling argument (a move that is
   "legal" globally is legal for every prime simultaneously — including primes
   on which it acts trivially, i.e. with one exponent 0).

4. **Product-of-all-entries monovariant (weaker, useful as cross-check).**
   Π_board x_i is non-increasing (drops by a factor gcd(m,n) when shared
   prime; unchanged when coprime). Confirms termination in the shared-prime
   case but does not by itself handle the coprime case, so it cannot replace
   F. Use only as a sanity invariant, not the main engine.

### Candidate technique(s)
- **Invariants & monovariants** (knowledge_base: "Invariants & monovariants"
  under Combinatorics, and "Invariant / monovariant" under General Proof
  Methods). The gcd-of-exponents is the invariant; F = ΣΩ + count is the
  monovariant.
- **Euclidean algorithm** per prime (subtractive form). The standard fact
  gcd(a, b) = gcd(b, a − b) is the only number-theoretic input.
- The factorization Ω(gcd) + Ω(lcm/gcd) = Σ_p max(a_p, b_p) and the drop
  Σ_p min(a_p, b_p) = Ω(gcd(m,n)) — a double-counting identity on the
  exponent pairs.

### Cheap-kill candidates
- The invariant g_p = gcd of all v_p kills part (b) in one line once stated.
- The combined monovariant F = ΣΩ + count kills part (a); no casework on the
  global structure, just the three local cases of the move.
- v_p / multiplicity bookkeeping (the Σ_p min identity) is the only
  computation; no heavy machinery.

### Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics section).
- "Invariant / monovariant" and "Direct proof" (General Proof Methods).
- "Divisor analysis: d(n), gcd structure…" (Number Theory) for the
  gcd/Ω bookkeeping.
- (Euclidean algorithm itself is not a named KB entry, but gcd(a,b)=gcd(b,a−b)
  is the standard fact the proof invokes; the outliner should state it by
  name.)

### Analogous past problems (cruxes)
- **None genuinely analogous.** The number-theory subtopics
  `invariants-and-monovariants` (only 2 cruxes) and `divisibility-and-gcd`
  were scanned. The closest in *spirit* (per-prime / squarefree-part
  monovariant for a board game) is **aimo-0324** — "Assign each board
  position the squarefree part S(n) = product of primes with odd exponent
  and use it as a one-sided monovariant." It shares the per-prime-exponent
  viewpoint but the game (n → n^k) and conclusion are different; it is a
  hint-to-adapt, not a template. **aimo-0098** ("evaluate at prime powers to
  turn an existential prime condition into a forced equation") is thematically
  adjacent (per-prime pinning) but not structurally the same. No crux in the
  corpus performs the subtractive-Euclidean-on-exponents move that is central
  here.

### Prior progress
- None — round 1, workspace empty.

### Dead ends (do not retry)
- None yet. One caution: do **not** try to use the product-of-all-entries as
  the sole termination argument — it is constant in the coprime case (m,n →
  1, mn) and so cannot by itself prove termination. It only witnesses the
  shared-prime decrease.

### Small-case / intuition notes (conjecture, but verified by computation)
- Formula M = ∏_p p^{g_p} verified numerically on
  [12,18]→6, [9,27]→3, [4,8]→2, [100,72,45]→90 (g_2=1, g_3=2, g_5=1),
  [2,3,5,7]→210, [8,8,8]→8 (g_2 = gcd(3,3,3)=3 → 2^3 = 8). All match direct
  simulation of the move sequence. This is evidence, not proof; the proof is
  the invariant argument above.
- Intuition: the process is "running the Euclidean algorithm in parallel on
  each prime's exponent column"; termination + unique normal form of the
  subtractive Euclidean algorithm is exactly what (a) and (b) assert.

### Hard steps / where the outliner must be careful
- The invariant g_p uses gcd with 0 (numbers not divisible by p). The proof
  must state gcd(0, k) = k and argue that g_p is well-defined and preserved
  *including* the coordinates that are 0 (a Euclidean step on (a, 0) gives
  (0, a), whose gcd is still a — preserved). This is the one place a sloppy
  write-through gets caught.
- Termination + "exactly one" needs both halves: F gives "at most one > 1";
  the invariant gives "not zero" (some g_p ≥ 1). Omit the second half and
  part (a) is incomplete (could end at all 1s).
- Rigor rule: name gcd(a,b)=gcd(b,a−b) (Euclidean algorithm) explicitly;
  name "invariant" and "monovariant"; no "clearly".
