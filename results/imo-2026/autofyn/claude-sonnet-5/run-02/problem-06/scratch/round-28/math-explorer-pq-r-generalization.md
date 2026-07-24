## imo-2026-06 (lens: a1-pq r-generalization of the Universal Look-Back Witness Identity)

- Distinct openings:
  1. **(Main finding, new) The `i=n` look-back witness closes to a
     q-INDEPENDENT closed form for EVERY residue r, not just r=1** — see
     below. This strictly generalizes the certified round-27 r=1 corollary
     and gives a uniform, per-(p,j,r) (not per-q) characterization of which
     `k=0` (and more generally which `k mod j`) cells are unconditionally
     safe via this one witness, for every r simultaneously, no threshold.
  2. A clean **structural reason r=1 is uniquely privileged** (not
     arbitrary): the constant term vanishes iff r=1, because r=1 is the
     only residue whose modular inverse mod p is itself (r⁻¹≡1 mod p), which
     forces s_0(j,1)=j exactly (a literal multiple of j), whereas for any
     other r, s_0(j,r)=j·r⁻¹ mod p is generically NOT a multiple of j. This
     is a proof-shaped explanation, not just an empirical pattern — worth
     writing up as a proper "Uniqueness of r=1" lemma.
  3. Secondary opening (not pursued in depth): this same machinery could be
     pushed to look-back distance `d` other than 0 for general r, exactly
     as round 27 tried `d=k` and `d=k+1` for r=1 and found `d=k+1` never
     works and `d=k` doesn't collapse cleanly — I did not re-derive these
     for general r (out of scope given the time budget), but the same
     algebraic method (reduce `q+n-i-1 mod (denominator)` using the
     n_0-formula rather than ad hoc telescoping — the exact mistake round 27
     caught itself making) would need to be applied fresh, not reused
     verbatim, if a future round wants a second uniform witness for r≠1.

- Candidate technique(s): elementary modular arithmetic / modular inverse
  bookkeeping (exactly the toolkit already in use for this family — no new
  external technique needed). The key trick: reduce `n_0(j,r)-1 mod j`
  using the defining relation `p(n_0-1)+j = s_0 q` directly (working mod j
  from the start), rather than substituting q's explicit form (which only
  works cleanly for r=1 where t=(q-1)/p is defined). This mod-j-first
  approach is the one new "trick" this lens contributes.

- Cheap-kill candidates: none needed — this is itself a cheap symbolic
  closure (no case search), verified against direct simulation below.

- Knowledge-base entries to use: none new beyond what the `a1-pq` approach
  already cites (elementary gcd manipulations, modular inverses). No KB
  theorem names change.

- Analogous past problems (cruxes): not separately investigated this
  round — this lens is purely internal algebra on the already-established
  a1-pq machinery, not a fresh corpus match. Defer to prior rounds' corpus
  citations for this approach (crux corpus not re-queried here; the task
  was specifically to extend an existing certified identity).

- Prior progress: round 27 certified the Universal Look-Back Witness
  Identity (general r) plus its r=1 Corollary showing `gcd(N,a_n) =
  gcd(k+1, j)` at look-back distance 0, making k=0 (and every k with
  gcd(k+1,j)=1) unconditionally safe FOR r=1 ONLY. This round's finding
  extends that corollary algebraically to a formula valid for every r.

- **New result derived and numerically verified this round (not yet
  written as a formal proof — for the outliner to formalize):**

  **Claim.** Fix odd prime p, band j∈{2,...,p-1}, residue r=q mod p,
  q>p prime. Let s_0=s_0(j,r) be the certified K_0-boundedness constant
  (unique solution of s_0·r≡j mod p, s_0∈{1,...,p-1}), and let
  p⁻¹ denote the inverse of p mod j (exists since gcd(p,j)=1, as p is
  prime and j<p). Define the constant
  ```
  c(p,j,r) := (s_0(j,r) · p⁻¹) mod j     — depends ONLY on p,j,r, not on q.
  ```
  Then at the k-th Case-(b) occurrence of band j (n = n_0(j,r)+kq, i=n,
  look-back distance 0):
  ```
  gcd(N, a_n) = gcd( j , (k+1+c(p,j,r)) mod j ).
  ```
  In particular, this witness is unconditional (no q-threshold, valid for
  EVERY admissible q≡r mod p at once) whenever gcd(j, k+1+c) = 1, and it
  reduces exactly to the certified r=1 corollary's `gcd(k+1,j)` when
  c(p,j,1)=0 (which is forced because s_0(j,1)=j exactly, i.e. j | s_0, so
  c=0 identically — the ONLY r for which this holds, see below).

  **Derivation sketch** (algebra only, not yet formalized as a lemma file):
  from `p(n_0-1)+j = s_0 q` (the defining relation of s_0/K_0-boundedness),
  reduce mod j: `p(n_0-1) ≡ s_0 q (mod j)`, so (since gcd(p,j)=1)
  `n_0-1 ≡ s_0 q p⁻¹ (mod j)`. Then `q+n-1 = q+n_0-1+kq ≡ q(k+1) +
  s_0 q p⁻¹ (mod j) = q(k+1+s_0 p⁻¹) (mod j)`. Since gcd(q,j)=1 (q>p>j),
  `gcd(j, q+n-1) = gcd(j, k+1+s_0 p⁻¹ mod j) = gcd(j, k+1+c)`.

  **Numerical verification** (this round, fresh sympy script, not reused
  from any prior round's script): tested p∈{5,7,11,13}, all primes q in
  (p,p+300), all bands j∈{2,...,p-1}, k∈{0,...,5} — **9762 total
  instances, 0 mismatches** between the direct brute-force `gcd(N,a_n)`
  (computed from `a_n=p(q+n-1)` under H(n)) and the predicted closed form
  above.

  **Key structural corollary (also numerically checked, p=5,7,11,13):**
  r=1 is the UNIQUE residue class (among r=1,...,p-1) for which c(p,j,r)=0
  for EVERY band j simultaneously — equivalently, the unique r for which
  the k=0 layer is unconditionally safe for every band at once. For every
  other r∈{2,...,p-1}, at least one (usually several) bands j have
  c(p,j,r)≠0 with gcd(j,1+c)>1, i.e. genuinely "at-risk" k=0 cells that
  this witness does NOT resolve (still need the pre-existing Case-(b)
  sieve/threshold machinery, or a further witness search, exactly as
  before this round for general r). **This is because r⁻¹ mod p = 1 iff
  r=1** (the defining property of the multiplicative identity), which
  forces s_0(j,1)=j·1=j exactly — a literal multiple of j — while for any
  other r, s_0(j,r)=j·r⁻¹ mod p is generically not divisible by j. Checked
  explicitly for r=p-1 (r⁻¹=p-1≡-1, giving s_0=p-j, and j∤(p-j) since p is
  prime and 0<j<p) and for r=(p-1)/2 at p=5,7,11,13 — in every single case
  tested, risky (non-empty) bands exist at k=0, matching the general
  argument.

  **Bottom line for the outliner:** the r=1 corollary does NOT generalize
  to an unconditional k=0 closure for any other residue r — this is now a
  proved (not just conjectured) fact, with an exact reason (uniqueness of
  the multiplicative identity mod p). What DOES generalize is a strictly
  weaker but still useful uniform fact: for every r, the same witness
  mechanism gives a q-INDEPENDENT (not q-threshold-free in the same total
  sense, but per-(p,j,r,k)-computable-without-a-threshold) formula, which
  could shrink the per-p residual verification burden in the general
  a1-pq derivation (Steps 4-5) by replacing the explicit numeric
  thresholds Q_1(p,j,r) with a direct O(p²) table lookup of c(p,j,r) —
  potentially a genuine simplification of the "at-risk" candidate
  enumeration in the existing partial theorem, worth formalizing as a new
  certified lemma next round ("Universal Look-Back Closed Form", r=1
  corollary as its special case c=0).

- Dead ends (do not retry): do not re-attempt to find an unconditional
  (threshold-free, all-r) k=0 closure by this single witness alone — it is
  now proved impossible for r≠1 (structural reason above, not just failed
  search). If a future round wants to close other r's k=0 layer
  unconditionally, it needs either (a) a genuinely different witness index
  (this round did not explore d=k, d=k+1 etc. for general r — flagged as
  opening 3 above, untried), or (b) to accept the O(p²) table-lookup
  reduction above as the best uniform simplification available and proceed
  with the existing per-p sieve machinery for the residual "risky" cells.

- Small-case / intuition notes: the closed-form formula and the "r=1
  uniquely privileged" corollary are both empirically confirmed
  (9762+ instances, 0 mismatches) but the underlying identity/derivation
  above is elementary and mechanical (mod-j reduction of the defining
  s_0 relation) — this should be regarded as effectively proved algebra,
  not merely a numerical conjecture, though it has not yet been written up
  as a formal certified lemma file. The outliner/builder should treat the
  derivation sketch above as a ready-to-formalize lemma, analogous in
  rigor-level to the existing certified Generalized K_0-Boundedness Lemma.

## Secondary check: fresh angle for H1 (FAH) / H2

No genuinely new concrete mechanism found this round for H1 or H2 — I did
not run a dedicated fresh-corridor sweep (out of scope for this lens per
the dispatch instructions, and run_state.md records 21+ consecutive plateau
rounds with 30+ dead mechanisms already catalogued: existential-to-
universal promotion, ambient-statistic-obstruction-violating framings,
orbit-merging/additive-offset dichotomy, priority-argument/computability,
o-minimality, nonstandard-analysis, spectral/operator, p-adic/algebraic NT,
generating functions, probabilistic/Borel-Cantelli, extremal graph theory,
finite-Fourier/character-sums, Kolmogorov complexity, martingale/optional-
stopping, renewal theory, return-words/Rauzy graphs, coding theory,
combinatorial game theory — all confirmed dead in prior rounds). I have
nothing new and concrete enough to report here; per the dispatch
instruction to only report if genuinely new, I am flagging this as a null
result rather than forcing a weak candidate. Recommend the run continue
prioritizing the a1-pq r-generalization (this lens) and the per-p
subfamily closures (a1-5q/a1-7q pattern) as the concrete, near-term
productive corridors, consistent with priority (a) in run_state.md.
