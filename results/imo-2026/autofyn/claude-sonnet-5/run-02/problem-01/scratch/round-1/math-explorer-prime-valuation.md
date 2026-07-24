## imo-2026-01

- Distinct openings:
  1. **Per-prime gcd-of-exponents invariant** (the payoff of this lens): for each prime p, let
     x_1,...,x_2026 be the *current* v_p of the 2026 board numbers. A move on numbers m,n only
     touches the two coordinates a=v_p(m), b=v_p(n) (for every prime p simultaneously) and sends
     (a,b) -> (min(a,b), |a-b|). Since gcd(min(a,b),|a-b|) = gcd(a,b) (the classical Euclidean
     subtraction identity), the *global* quantity g_p := gcd(x_1,...,x_2026) (gcd of all 2026
     exponents of p, with the usual convention gcd(0,...,0)=0, gcd of a set with a nonzero entry
     = gcd of the nonzero entries) is unchanged by every move, for every prime p independently.
     This is a genuine invariant (not just monotone), and it is the natural target for part (b).
  2. **Termination via a two-part monovariant**: Φ := Σ_i Σ_p v_p(n_i)^2 (sum of squares of all
     exponents over the whole board) is non-increasing, and strictly decreases by at least
     min(a,b)·(2·max(a,b) − min(a,b)) ≥ 1 whenever gcd(m,n) > 1 (i.e. whenever some prime divides
     both chosen numbers). When gcd(m,n)=1, Φ is unchanged but K := #{board entries > 1} strictly
     drops by exactly 1 (the pair (m,n), both >1, becomes (1, mn)). Both Φ and K are non-increasing
     nonnegative integers and at least one strictly drops every move ⇒ the pair (Φ,K) is a strict
     monovariant under a lexicographic (or Φ·2027+K) ordering ⇒ finitely many moves total. This
     is the route to part (a)'s "finitely many moves" half.
  3. **Ruling out the all-1s terminal state (existence of a survivor)**: since every original board
     number is >1, some prime p divides at least one of them, so g_p (from opening 1) is >0 at the
     start, hence at *every* time (invariant), hence the exponent vector of that prime can never be
     all-zero, hence some board entry is always >1. Combined with opening 2 (finite termination, and
     termination = state with <2 entries >1, i.e. K ≤ 1), this pins the terminal K to exactly 1 —
     this is the "exactly one" half of part (a), using the *same* invariant as part (b).
  4. **Direct identification of M via opening 1**: at the terminal state (K=1), for each prime p the
     exponent multiset is 2025 zeros plus one value v_p(M); gcd(0,...,0,v_p(M)) = v_p(M). But that
     gcd equals g_p (invariant, computed from the *original* board). Hence v_p(M) = g_p for every p,
     i.e. **M = ∏_p p^{gcd(v_p(n_1),...,v_p(n_2026))}**, an explicit formula depending only on the
     initial board, proving part (b) as an immediate corollary of the invariant — no separate
     "two terminal states must agree" argument needed.

- Candidate technique(s): per-prime factorization + Euclidean-algorithm gcd-invariance identity
  (gcd(min(a,b),|a-b|)=gcd(a,b)); a two-term monovariant (sum-of-squares-of-exponents, count-of-
  survivors) for termination. This is a clean, self-contained elementary number-theory argument —
  no heavy machinery needed. Matches knowledge_base.md "Invariants & monovariants" (line 117) and
  "Invariant / monovariant" (line 191) general entries; no other KB entry (LTE, Zsigmondy, Bertrand,
  etc.) is needed for this problem — those are overkill/irrelevant here.

- Cheap-kill candidates: none needed as a pruning step — the invariant argument above is already a
  near-complete constructive solution, verified numerically (see below). No pigeonhole/parity attack
  is required.

- Knowledge-base entries to use:
  - "Invariants & monovariants" (knowledge_base.md line 117, Combinatorics section) — general
    principle, apply concretely as above.
  - "Invariant / monovariant" (knowledge_base.md line 191, General Proof Methods) — same principle,
    "moves only one way to prove termination."
  - "Divisor analysis" (line 86) is tangentially relevant (gcd structure) but the specific per-prime
    exponent identity is the real engine, not explicitly in the KB — it's the standard fact
    gcd(a,b) = gcd(a−b, b) = gcd(min(a,b), |a−b|), a direct consequence of the Euclidean algorithm,
    which should be cited/proved inline (one line) rather than assumed as a KB citation.

- Analogous past problems (cruxes): searched number_theory subtopics `invariants-and-monovariants`,
  `divisibility-and-gcd`, `p-adic-valuation`, and combinatorics `processes-and-algorithms` /
  `invariants-and-monovariants` for keyword matches on gcd/lcm/board/exponent/valuation (184 hits
  scanned). None found a genuinely analogous "board process replacing a pair by (gcd, lcm/gcd)"
  problem. Closest tangential hits, neither a real analogy: `aimo-0028` (Euclidean-step gcd-stripping
  on two near-equal quadratics — same underlying identity gcd(a,b)=gcd(a-b,b) but totally different
  problem shape, a number-theoretic existence proof, not a process/invariant problem) and `aimo-0662`
  (combinatorics: "periodic multiplicative tower on primes whose consecutive lcm/gcd chains realize
  the extremal..." — uses lcm/gcd chains but for a different extremal-construction problem, not a
  board-reduction invariant). **Verdict: no strong analog in the corpus; this problem's structure
  (global per-prime gcd invariant under a pairwise exchange) does not closely match any indexed crux.**
  The relevant technique is elementary and self-derivable, not corpus-retrievable.

- Prior progress: `results/imo-2026-01/current.md` is empty (Status: unsolved, no approaches yet;
  this is round 1, first exploration of the problem).

- Dead ends (do not retry): none yet recorded (no prior approaches exist to check).
  One thing to flag as a **near-miss, not a dead end**: the *total product* of all board numbers is
  NOT invariant (it strictly decreases by a factor of gcd(m,n) each non-coprime move, unchanged on
  coprime moves) — it is only a monovariant, useless for pinning down M exactly; the per-prime gcd
  of exponents (a genuinely different, finer quantity) is what's invariant. Don't waste a round
  chasing "product is invariant" — verified false: e.g. board {4,6}: product 24 → move gives (2,6),
  new product 12 ≠ 24.

- Small-case / intuition notes (numerically verified, hence still "conjecture-grade" until written
  up as a rigorous proof, but very strong evidence — the algebra above is a full derivation, this is
  a cross-check): ran 20 random boards (sizes 3–8, entries in [2,30]), each played to termination via
  15 independent random legal-move orderings (random.seed=1, script executed via python3, gcd/lcm
  simulation). In every one of the 300 runs, the process terminated in finitely many moves (well
  under the 100000-move cap), left exactly one survivor, and that survivor exactly equalled the
  predicted M = ∏_p p^{gcd_p(v_p over the original board)} computed independently from the initial
  board — confirming both part (a) (existence + uniqueness of survivor) and part (b) (path-
  independence, matching the closed-form invariant) on every trial. This is strong corroborating
  evidence but the algebraic argument above (gcd(min(a,b),|a-b|)=gcd(a,b), sum-of-squares
  monovariant, K-monovariant) is what should be written up as the actual proof, not the numerics.

- Open items for the outliner: the algebra above (opening 1–4) looks like it closes essentially the
  whole problem; remaining work is to write it up with full rigor: (i) prove
  gcd(min(a,b),|a-b|)=gcd(a,b) cleanly (trivial case split a=b, a<b, a>b, and the a=0 or b=0 edge
  cases), (ii) prove g_p invariance carefully handling the convention gcd(0,...,0)=0 and "gcd of a
  multiset with some zero entries," (iii) the Φ/K two-part monovariant termination argument needs
  the strict-decrease computation written out precisely (I verified the arithmetic: difference =
  a(a−2b) for a=min≤b=max, strictly negative when a>0), and (iv) tie termination + "K≥1 always" +
  "K decreases to ≤1" together to conclude K=1 exactly at the end. This is a full solution sketch,
  not yet a certified proof — the outliner should build exactly this as (very likely) the single
  best approach, but should still flag each of (i)-(iv) as an explicit gap until a builder writes
  the complete rigorous text.
