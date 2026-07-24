## imo-2026-06

- Distinct openings (all attack the SAME certified nucleus — finiteness of Π = sole-connector
  primes / the MCL/HS statement — but via greedy minimality rather than counting; these are
  candidate mechanisms, not outlines, and are mutually distinct enough to seed separate slugs):

  1. **S₀-coloring finite-class reduction.** Every term aₙ is divisible by some prime of the
     FIXED finite set S₀ = supp(a₁) (proved already in both round-1 approaches, Lemma A /
     Lemma 3's proof-ingredient — re-surface it explicitly, it is under-used). Color each term
     by τ(aₙ) := supp(aₙ)∩S₀, a nonempty subset of S₀. There are only ≤2^|S₀|−1 possible colors,
     a FIXED finite number independent of n. Any two SAME-color terms are automatically connected
     by an S₀ prime — no extra connector ever needed. So (HS)/MCL reduces from "connect ALL
     pairs" to the strictly smaller task: "connect all CROSS-color pairs between the finitely
     many *disjoint* color classes that both occur infinitely often." This shrinks the crux from
     an unbounded pairwise statement to a bounded (≤ C(|S₀|,2)) family of class-pair sub-problems
     — a genuine reduction the round-1 approaches only partially used (essential-prime-counting's
     P2 gestures at this via "cross-class pairs" but never names the finite color-class structure
     explicitly or exploits its finiteness combinatorially).

  2. **Gap-divides-difference bound on connector size (extremal/pigeonhole route).** If p is
     the (sole) connector of a pair (aᵢ,a_j), i<j, then p | gcd(aᵢ,a_j) | (a_j − aᵢ) — the crux
     move behind aimo-0503 ("bound the gap between two consecutive terms from below by their
     gcd, since the gcd divides their positive difference"). Combined with the bounded-gap fact
     a_{n+1}−aₙ ≤ R = rad(a₁) (Lemma 3/A, ABSOLUTE constant, independent of n — this is the
     load-bearing greedy-minimality fact, since it comes from "every multiple of R is admissible
     w.r.t. every term," a direct consequence of the greedy rule's universality), we get
     p ≤ a_j − aᵢ ≤ (j−i)·R. So a LARGE sole-connector prime can only ever serve a pair that is
     FAR APART in index. Framing: assume Π infinite, take an increasing sequence of
     sole-connector primes p₁<p₂<⋯→∞ witnessing pairs (i_m,j_m) with j_m−i_m→∞ forced. Then
     argue (extremal principle / minimal counterexample, KB "Pigeonhole / extremal principle";
     "Contradiction") that by the time the index gap is that large, the finitely-many-colors
     structure (opening 1) must ALREADY have produced a shared small connector for that pair
     (because only finitely many color combinations exist, so far-apart same/compatible-colored
     terms recur), contradicting p_m being the *sole* connector, OR show the greedy choice at
     index j_m would have preferred a smaller candidate built from an already-recruited small
     prime, so a_{j_m} would not equal what it does. Neither direction is closed here — this is
     the concrete shape of the missing "greedy forces smallness" lemma, to be attempted by the
     outliner/builder.

  3. **Extremal "first fresh recruitment" argument.** Define the recruited-prime set at step n,
     𝒩ₙ = (primes that have served as a sole/needed connector among a₁,…,aₙ) \ S₀. Look at the
     LEAST index n₀ (extremal principle, KB "Pigeonhole/extremal principle": take the minimal
     witness) at which a_{n₀} is forced to use a prime p ∉ 𝒩_{n₀−1} ∪ S₀ as its ONLY way to
     satisfy some earlier constraint. By minimality of a_{n₀} (the greedy rule), every integer in
     (a_{n₀−1}, a_{n₀}) failed some admissibility constraint. Since the window has length ≤ R
     (bounded, opening 2's key fact) there are at most R−1 candidates to rule out — a FIXED finite
     number of "reasons for failure" per recruitment event. The open question (not resolved here)
     is whether the number of DISTINCT recruitment events (n₀'s of this kind) is itself bounded —
     numerically (see below) it is always small (≤ 3–5 extra recruited primes beyond S₀, always
     the SMALLEST available primes 2,3,5,7,… in increasing order, never a "skip" to a larger
     prime) — suggesting a mechanism "each recruitment event permanently retires one disjoint
     color-class-pair obligation, and there are only finitely many such obligations" (ties back to
     opening 1). This is the sharpest lens: turn (HS) into "the recruitment process terminates,"
     an induction/monovariant statement (KB "Invariants & monovariants," "Induction / infinite
     descent") on the (finite!) poset of unresolved class-pairs, rather than a counting bound.

- Candidate technique(s): Pigeonhole/extremal principle on a MINIMAL counterexample (first
  recruitment index, or smallest witnessing large sole-connector prime) — KB "Pigeonhole /
  extremal principle," "Contradiction," "Invariants & monovariants." The S₀-coloring is a
  divisibility/CRT-flavored finite partition (KB "Modular arithmetic, CRT," "Divisor analysis").
  The gap-divides-difference fact is elementary divisibility (KB "Divisor analysis" /
  aimo-0503-style gcd bound). None of these are the counting/density family already ruled
  insufficient (Σ1/p²) — they are structural/extremal, matching the assigned lens.

- Cheap-kill candidates:
  - **Finite-color pigeonhole is free and strengthens every approach immediately**: since
    every term is divisible by a prime of the FIXED finite set S₀, (HS) already reduces to
    finitely many (≤2^|S₀|−1 choose 2) class-pair sub-problems before any hard work — cheap,
    rigorous, should be grafted into the leader approach regardless of whether the harder
    "each class-pair needs ≤1 connector" claim is closed this round.
  - Gap-divides-difference (p | a_j−aᵢ) is a one-line elementary fact, cheap to verify and
    immediately rules out ANY sole-connector prime exceeding the index-gap×R bound — worth
    stating as a lemma even if the finiteness conclusion needs more.
  - Parity/small-prime-first check: numerically, recruited primes beyond S₀ always appear in
    increasing order 2,3,5,7,… (never "jump" past an unused small prime to reach a larger one) —
    consistent with, and testable via, minimality of the greedy step at the recruitment index.

- Knowledge-base entries to use: "Modular arithmetic, CRT" (S₀-coloring / L-periodicity, already
  used in the certified reduction); "Pigeonhole / extremal principle" and "Invariants &
  monovariants" (General Proof Methods + Combinatorics sections) for the minimal-counterexample /
  recruitment-terminates framing; "Divisor analysis" (gcd divides difference); "Contradiction"
  (assume Π infinite, derive impossibility from minimality).

- Analogous past problems (cruxes):
  - `aimo-0503` (number_theory, divisibility-and-gcd) — crux "Bound the gap between two
    consecutive terms from below by their gcd, since the gcd divides their positive difference."
    Directly the mechanism behind opening 2 (p | a_j−aᵢ). Genuinely analogous move, not just
    same-subtopic; adapt, do not cite as a black box.
  - `aimo-0447` (already used by essential-prime-counting) — "gcd>1 for every pair" ⇒ prime-grid
    covering encoding. Relevant background for the reduction, but its counting corollary is the
    PROVEN-INSUFFICIENT dead wall; only the raw encoding move is reusable, not its conclusion.
  - `aimo-0421` (number_theory, divisibility-and-gcd) — "gcd of a fixed element with a varying
    one takes only finitely many values [divisors of the fixed element], so over an infinite
    family infinitely many partners give the same gcd value" — a pigeonhole-on-finitely-many-
    divisors move. Loosely analogous: could motivate treating gcd(aᵢ, a₁) (which only takes
    values among the finitely many divisors of a₁ that are >1) as a finite coloring — this IS
    essentially the S₀-coloring in opening 1, giving it independent crux-corpus support. Worth
    the outliner's attention as corroboration, not a new idea.
  - No crux found that solves a genuinely equivalent "greedy pairwise-gcd sequence is eventually
    linear-periodic" problem; the corpus's "greedy" hits are almost all combinatorics
    (packing/selection games), not number-theoretic gcd-sequences — none is a close structural
    match beyond the three above.

- Prior progress: Whole problem reduced (reviewer-certified, exact from n=1) to (HS)/MCL:
  finiteness of Π = sole-connector primes. Certified lemmas in `lemmas/enumeration-and-bounded-
  gaps.md`, `lemmas/finite-hitting-set-periodicity.md`. Do not re-derive; import directly.
  New facts surfaced this round (not previously stated as standalone lemmas, but provable in
  ≤1 line from existing Lemma 1/3 or Lemma A): (i) every term is divisible by some prime of the
  fixed finite S₀ = supp(a₁) [buried inside admissible-set-periodicity Lemma 3's proof / Step
  "(P2)" of essential-prime-counting, never isolated]; (ii) sole-connector p divides the
  difference of its pair, hence p ≤ (index-gap)×R.

- Dead ends (do not retry): Pure counting/density (Σ1/p² interval-occupancy, "no two disjoint
  heavy types") — PROVEN insufficient in round 1 (cannot exclude sparse density-zero disjoint
  essential prime families); confirmed by re-reading essential-prime-counting.md, the gap is
  real and correctly diagnosed, not a mistaken dead-end label. `finite-state-reversible`'s
  reversibility mechanism targets EXACTNESS (already fully solved by the static-set approach,
  Lemma C/6) — it is not attacking (HS) at all and should not be prioritized as a finiteness
  route; if reused, only its Step-2/"finite live-constraint window" idea overlaps with opening 1
  above and could be merged, but its "GAP D / L2" is literally the same open (HS) crux, not a
  different attack.

- Small-case / intuition notes (CONJECTURE, numerically checked, not proved): ran the greedy
  process in Python (sympy) for a₁ ∈ {15,105,143,1001,858,30,210,21,33,55,77,6,10,14,35,91,221},
  up to 150–250 terms, computing ALL pairwise sole-connector primes (not just nearby-index
  pairs). In every case the sole-connector set stays small and fixed: e.g. a₁=15 → {2,3,5} even
  checked over all pairs among the first 200 terms (max sole-connector prime observed = 5); a₁=
  143 → {2,3,11,13} (max = 13 = max(S₀)); a₁=221 (S₀={13,17}) → recruits exactly {2,3,5} in
  addition, never a larger fresh prime; a₁=35 (S₀={5,7}) → recruits {2,3}. Two clean regularities
  observed: (a) recruited primes beyond S₀ are always among the SMALLEST unused primes
  (2,3,5,7,… in increasing order — never "skips" to recruit a larger prime while a smaller one
  is still unused), consistent with opening 3's minimal-recruitment-index framing; (b) no sole-
  connector prime ever exceeds roughly max(S₀) or a small multiple of it, i.e., Π ⊆ {primes ≤ some
  bound depending only on a₁'s small factors, NOT growing with sequence length} — strong
  numerical support for (HS)/MCL finiteness itself (as expected, since it's a certified-true
  theorem), and specifically for the "recruitment terminates after finitely many small events"
  shape of opening 3 over the "large coincidental prime" shape ruled out by opening 2's bound.
