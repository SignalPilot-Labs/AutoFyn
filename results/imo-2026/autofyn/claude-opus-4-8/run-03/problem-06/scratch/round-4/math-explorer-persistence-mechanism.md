## imo-2026-06 (IMO 2026 P6)

Lens: persistence mechanism of a shared large witness prime; whether a genuinely new
covering/counting or dichotomy argument can attack Π-finiteness without repeating the
antichain/monovariant/automaton wall.

### Distinct openings

1. **Edge-covering / grid-counting argument (aimo-0447 style), NEW route, not tried before.**
   Build the complete graph on term-indices `{1,...,N}`; for every pair `i≠j`, L4
   (pairwise-intersecting, certified) gives `gcd(a_i,a_j)>1`, so the edge `(i,j)` is "witnessed"
   by some prime `p | gcd(a_i,a_j)`. Since `a_i = Θ(i)` (L2), each vertex `i` has only
   `ω(a_i)=O(log i)` distinct prime divisors, so the total prime-occurrence budget across all `N`
   vertices is `Σ_i ω(a_i) = O(N log N)`. Meanwhile the number of edges a single prime `q` can
   witness is `C(m_q,2)` where `m_q = #{i≤N : q|a_i} ≤ N/q · O(1)` (density of `q`-multiples among
   `Θ(N)`-valued terms). Covering all `C(N,2)=Θ(N²)` edges forces `Σ_q m_q² = Ω(N²)`. I verified
   numerically (below) that this DOES hold with slack (ratio `ΣC(m_q,2)/edges ≈ 1.6–1.9`), and the
   count of distinct primes dividing ANY term among the first `N` is small but **grows with `N`**
   (not bounded) — so a naive "primes dividing some term" covering count does **not** by itself
   bound Π. **Important negative finding:** this route bounds "primes touching many edges" (i.e.
   forces some primes to have positive density — already known via Anchor+pigeonhole, §8.1 of
   `redundant-constraint-antichain`), but it does NOT distinguish minimal-support primes from
   dominated ones, so as stated it collapses onto the same wall unless refined to only count
   ⊆-minimal-support primes (which is exactly the un-closed E5/K-real gap). Flag as a genuinely new
   *technique* (Cauchy–Schwarz / convexity on `Σm_q²` vs `Σm_q`) worth trying **restricted to
   𝓐_∞-witnessing primes only** (i.e. only primes that are the E3 private witness of some pair) —
   not yet attempted by any approach in the population.

2. **Dichotomy à la aimo-0421 (Schubfachprinzip on an infinite pairwise-non-coprime set).** The
   crux corpus's aimo-0421 proves: for an infinite set `S`, either some prime divides infinitely
   many elements of `S` (pigeonhole gives structure), or every prime divides only finitely many
   elements — the latter case is then shown, using pairwise-gcd conditions, to force a specific
   configuration. Applying the SAME dichotomy recursively (not just once, as §8.1 already does) to
   the residual set `R_1 = {n : p_1 ∤ a_n}` (after peeling off the first anchor prime `p_1`) is
   a genuinely unexplored recursive/inductive structure: if `R_1` is finite, `Π` is trivially
   bounded (only finitely many "extra" terms need new primes); if `R_1` is infinite, `R_1` is
   ITSELF pairwise-intersecting (inherited from L4) and finite-prime-per-vertex (inherited from
   L2), so the SAME pigeonhole (§8.1-style) applies to `R_1`, peeling a second anchor prime `p_2`
   witnessing infinitely many of `R_1`. Iterate. **This produces an infinite descending chain of
   residual infinite sets `R_1 ⊇ R_2 ⊇ ...` each contributing one "co-dominant" prime `p_k`.** The
   open question this route raises (not resolved here): does this process TERMINATE (some `R_k`
   finite) — which is exactly equivalent to Π finite via a different, recursive framing — or is
   there a structural reason a *positive-density* residual sequence must eventually be entirely
   swallowed by finitely many primes? This is a genuinely different top-level target: instead of
   proving "𝓐_∞ finite" directly, prove "**the peeling process terminates in finitely many
   rounds**," which converts the crux into an induction/descent statement close in spirit to
   aimo-0421's second solution. Worth flagging to the outliner as a structurally distinct
   attack (recursive residual-set peeling) not tried by any of the three existing approaches.

3. **Sparsity-forces-retirement heuristic (the dispatched lens itself), checked and found
   insufficient alone.** A large witness prime `q` divides terms that are `≥ q` apart in value
   (L3), hence, given `a_n=Θ(n)`, `≥ q/M` apart in index — so `q`-multiples among the terms have
   density `O(M/q) → 0` as `q→∞`. But **this alone does not force `q` to stop appearing in minimal
   supports** — a density-0 set can still be infinite, and (per the certified Obstruction Lemma in
   `monovariants-and-obstruction.md`) an anchored `{p*, q_k}` family with `q_k→∞` shows an
   arbitrarily-sparse large-prime sequence is *combinatorially* consistent with persisting forever
   in an abstract intersecting family. **However that Obstruction family was already shown
   (antichain §7b / E2⇒) to fail the *self-blocking* realizability condition** — i.e. it is not
   realizable as an actual `𝓐_∞` of this greedy sequence. So the sparsity argument by itself is a
   dead end (does not close the gap) UNLESS combined with E1/E2 realizability — which is precisely
   what E3 (Private-witness distance) already extracts (`q ≤ |t-t'|`) and what E5 still needs to
   turn into a genuine finite bound. **Conclusion: the "persistence mechanism" question as posed
   reduces to the SAME wall (E5) once realizability is imposed — sparsity is necessary but not
   sufficient, confirming (not bypassing) the reviewer's diagnosis that the crux needs the greedy
   choice dynamics, not a set/density statistic.**

### Candidate technique(s)
- Cauchy–Schwarz / convexity counting on `Σ_q m_q²` vs edge count (opening 1) — genuinely new to
  this problem's population; cite `knowledge_base.md`'s Pigeonhole/extremal principle and Double
  counting entries (not yet located by name in kb — recommend outliner search kb for
  "double counting" / "convexity" entries directly).
- Recursive dichotomy / residual-set peeling (opening 2), modeled on aimo-0421's Schubfachprinzip
  argument — an induction-on-residual-sets framing, distinct from the antichain's static
  ⊆-minimality framing.
- `Σ 1/p²` convergence covering arguments (aimo-0643, aimo-0447) as a template for turning "large
  primes are individually sparse" into a quantitative bound — but per opening 3 this needs to be
  wired to E1/E2 realizability, not applied to the raw admissible set.

### Cheap-kill candidates
- None found that immediately dispatch the crux. The one cheap numerical check worth running before
  investing in opening 1: confirm (as I did for a₁=375) that "primes dividing ANY term" is
  unbounded in `N` (I verified: 47→74→124→214 distinct primes for `N=200,400,800,1600`, growing
  roughly linearly) — this is a **structural pruning fact**: any covering argument targeting "all
  primes dividing some term" is doomed; it MUST restrict to minimal-support (undominated) primes
  specifically. This should be recorded so future rounds don't waste time on an unrestricted
  covering argument.

### Knowledge-base entries to use
- Pigeonhole / extremal principle (`knowledge_base.md` line ~108) — underlies both opening 1 and 2.
- Dirichlet's theorem (primes in AP) — not obviously needed here but flagged as available if a
  density-of-primes argument on a fixed residue class is later required.
- CRT / modular arithmetic entry — relevant to the certified periodicity endgame (§4-5 of
  `redundant-constraint-antichain`), already in use, not new.

### Analogous past problems (cruxes)
- **aimo-0421** (number_theory, divisibility-and-gcd) — infinite set `S` with a prescribed gcd
  pattern; crux move: dichotomy "some prime divides infinitely many elements of S" vs "every prime
  divides only finitely many," each resolved by pigeonhole. Genuinely analogous in *structure*
  (infinite pairwise-gcd-constrained set, prime-indexed pigeonhole) though the target claim differs
  (they prove existence of a "balanced triangle," we need Π-finiteness). The dichotomy technique
  (opening 2) is directly transplantable as a proof *strategy*, not a citable result.
- **aimo-0447** (number_theory, size-bounding-and-descent) — grid of primes witnessing
  `gcd(a+i,b+j)>1` for `i,j∈{0,...,n}`; crux move: bound cells a single prime occupies by
  `(N/p)²`, then use `Σ1/p²` convergence to force most primes to be large, yielding a size lower
  bound. Analogous in *technique* (covering count via `Σ C(m_q,2)`) for opening 1, though their
  target (lower-bounding `min(a,b)`) is the reverse direction of what we need (we want an UPPER
  bound on the number of distinct primes, they want a LOWER bound on term size) — the transplant is
  partial; the numerical check above shows the naive version does not close our gap.
- **aimo-0643** (number_theory / geometry-flavored, size-bounding-and-descent) — sublattice
  covering a disk, sum of small-prime contributions via `Σ1/p²`; same convergence-counting
  technique family as aimo-0447, reinforcing that this is a recognized crux pattern, not ad hoc.
- **aimo-0224** (already flagged by antichain approach as a cautionary note) — confirms that
  intersecting + anchored structure alone (no realizability) is consistent with an infinite prime
  alphabet; consistent with opening 3's negative conclusion.

### Prior progress
Everything through the certified endgame (periodicity from `n=1` given Π finite) is proved; the
sole open gap across ALL three live approaches is finiteness of `Π` / `𝓐_∞`, now sharpened to
`sup|G|<∞` (E4, certified) or equivalently the K-real / companion-pool realization bound
(monovariant-witness-descent, open) or the ERW window bound (antichain §10, open). See
`results/imo-2026-06/current.md` for the full certified lemma list.

### Dead ends (do not retry)
- **Unrestricted covering-count on "all primes dividing some term"** (opening 1's naive form):
  refuted numerically this round — that prime set is unbounded in `N` (47→74→124→214 for
  `N=200,400,800,1600`, `a₁=375`), so any argument that doesn't first restrict to minimal-support
  (undominated) primes cannot bound Π. Record this so future covering-style attempts start from the
  restricted set.
- **Sparsity-of-large-primes alone (opening 3 / the dispatched lens's core idea)**: confirmed to be
  insufficient by itself — the certified Obstruction Lemma family `{p*,q_k}` already shows an
  arbitrarily sparse infinite large-prime sequence is combinatorially consistent with persisting in
  an intersecting/anchored family; only the (already-known, still open) E1/E2 realizability
  constraint rules it out, so this is not a bypass of E5 but a restatement of why E5 is hard.
- **M-threshold confinement `p|L ⇒ p≤M`**: previously refuted (recorded in current.md); do not
  revisit under any framing (19 > M=15 persists in `L` for `a₁=375`).

### Small-case / intuition notes (conjectural, numerically checked only)
- `Π_total` (all primes ever dividing any term) grows roughly linearly in `N` — clearly unbounded;
  contrast with `Π` (minimal-support primes only), which stabilizes at small finite sets in every
  tested seed (`|Π|∈{1,4,5,6}` across seeds in current.md's §11.3 table). This gap between
  "unbounded total primes" and "conjectured-bounded minimal-support primes" is the crux's real
  content, and no counting argument that doesn't isolate ⊆-minimality will succeed.
- The edge-covering ratio `ΣC(m_q,2)/C(N,2)` stays in a narrow band (`1.6–1.9`) across seeds and
  grows very slowly if at all with `N` — mild evidence (not proof) that the "effective" prime
  budget used by the sequence is tightly controlled, encouraging but not resolving opening 1.
- No new evidence found that changes the E4/E5 picture already established; this exploration
  primarily (a) surfaces two new candidate technique families (grid-counting, recursive dichotomy)
  for the outliner to consider as genuinely different top-level attacks, and (b) rules out the
  naive forms of both as immediate closers, saving a round of wasted build effort.
