## imo-2026-06 — lens: closing the a1-3qk residual band (general m)

### Headline finding (the actual opening for this round)

**Round 23's "structurally insufficient for m≥2" diagnosis is an artifact of an
avoidable inefficiency, not a real growth-rate mismatch.** Part IV of
`approaches/a1-3qk-subfamily-theorem.md` tests the certified Legendre Sieve
Gap Bound at `k=0` using `r := ω(qK_0)` (modulus `qK_0`, so `q` is counted as
one of the `r` prime factors). But **Part III of the very same file already
proves, unconditionally and `m`-independently, that coprimality to `q` is
FREE at `k=0`** (`t_i ≡ i-1 (mod q)`, nonzero since `i-1 ∈ {1,…,n_0-1}` and
`n_0 < q`) — so the sieve only needs to find a value coprime to `K_0` itself,
i.e. the correct modulus is `K_0`, giving `r := ω(K_0)`, **one prime factor
fewer**, hence a bound weaker by roughly a factor of 4 (`2^r(r+1)` vs
`2^{r+1}(r+2)`).

I recomputed the round-23 "fails at every tested prime" claim with this one
fix (own `sympy` script, `L ≥ 2^{ω(K_0)}(ω(K_0)+1)` at `k=0`, `q` prime,
`q≥7,q≠5`):

```
m=1, q<2000 (300 primes): 1 failure   (q=11, matches the certified theorem's k=0 exception)
m=2, q<2000 (300 primes): 4 failures  (q=11,17,23,29) -- same 4 failures out to q<20000 (2259 primes)
m=3, q<2000 (300 primes): 12 failures -- 12 failures out to q<20000 (largest at q=479)
m=4, q<20000 (2259 primes): 19 failures (largest at q=419)
```

This is **exactly the finite-residual-band pattern**, not the "every single
prime fails" pattern round 23 reported (which used the inflated `ω(qK_0)`
modulus and found 18/18, 27/43 etc. failures at `m=2,3`). I also re-ran the
full `k≥1` sieve check (`k=0`: modulus `K_0` only; `k≥1`: modulus `qK` since
`q`-coprimality is genuinely not free once `n=n_0+kq≥q`) over `q<300, k<15`:
`m=1` gives **exactly 3 failures** — `(q,k,K_0)=(7,1,·),(11,0,4),(11,2,·)` —
which match, term for term, the certified `a1-3q-subfamily-theorem`'s own
3-instance residual table `(1,5,7),(2,4,11),(3,5,7)` (only relabeling of
which index is called `k`). This is a strong sanity check that the corrected
sieve-modulus bookkeeping is right, not a new formula I invented. For `m=2,3`
the analogous count is 9 and 25 respectively over the same small range —
growing with `m`, but **not exploding**, and not scaling with `q` (i.e. still
looks like a genuine finite table, just a bigger one, consistent with round
23's own reviewer finding "zero failures beyond q=443/1103" in the *actual
truth* check).

### Distinct openings

1. **(Primary, cheapest) Fix the modulus bookkeeping at k=0.** Redo Part IV
   of `a1-3qk-subfamily-theorem.md` using `r=ω(K_0)` (not `ω(qK_0)`) for the
   `k=0` sub-case, since Part III already proves `q`-coprimality is free
   there. This alone should shrink the "fails everywhere" finding to a small,
   genuinely finite table for each fixed `m`, matching the m=1 precedent.
2. **Uniform-in-k closure via Primorial Floor Bound, transplanted.** For
   `k≥1`, `K=K_0+3k` behaves, for `k` large relative to `q^{m-1}`, exactly
   like the `m=1` case's `K~3k` (since `K_0` is a FIXED additive constant
   once `q,m` are fixed, it becomes negligible once `k` is large) — so the
   round-22 argument (`s:=ω(K)≥4 ⟹ K≥(s+1)!` forces `k` large enough that
   `L=n-1≥kq≥7k` beats `2^{r}(r+1)`) should transplant close to verbatim,
   with the only new casework being: the crossover point `k*` beyond which
   "`k` large" kicks in now depends on `m` (roughly `k* = Θ(q^{m-2})`,
   derived below), not a universal constant `~11` as at `m=1`. This is
   **still finite for each fixed `q,m`**, just a bigger table to compute
   than `m=1`'s.
3. **A genuinely uniform (m-independent) argument.** Do NOT expect one single
   argument-plus-constant that covers all `m≥1` simultaneously with a FIXED
   finite exceptional table independent of `m` — the crossover scaling
   `k*~q^{m-2}·const` (see below) shows the residual table's *size* (not just
   its existence) genuinely grows with `m`. What IS uniform is the *proof
   strategy* (Legendre Sieve Gap Bound + Primorial Floor Bound, correctly
   applied with `r=ω(K)` not `r=ω(qK)` whenever q-coprimality is already
   free) — i.e., a single template proof with an `m`-dependent finite
   verification, not `m`-many genuinely different proofs. This matches
   the workspace's own successful `m=1` precedent (round 22 took 3 rounds to
   assemble one template + one 18-entry table); expect `m=2,3,...` to each
   need their own (larger) table under the same template, not one universal
   closed-form residual set.

### Why the crossover scales like `q^{m-2}` (back-of-envelope, not a proof)

Need (heuristically) `L ~ K` for the trivial pigeonhole to start working
without invoking the crude sieve bound at all: `L=n_0+kq-1 ~ kq` for `k≥1`,
`K=K_0+3k ~ 3q^{m-1}` while `k` is still small (`K_0` dominates), so setting
`kq ~ 3q^{m-1}` gives `k* ~ 3q^{m-2}`. For `m=1`: `k*=O(1/q)→` bounded
constant (matches the actual `~11` cutoff, independent of `q`). For `m=2`:
`k*=O(1)`, i.e. still a BOUNDED constant, not growing with `q` — this is
consistent with the numeric finding above (`m=2`'s failures stop growing
past `q=29` in the small sweep, and the `q<443` cutoff the round-23 reviewer
found in the *actual truth* check is a genuinely finite, `q`-bounded band).
For `m≥3`: `k*` genuinely grows with `q` (like `q^{m-2}`), meaning the
*number of `k`-values* that need hand/table-checking at a fixed `q` grows
with `q` — this is qualitatively different from `m≤2` and is where a
single finite 2-D table (over `(q,k)` jointly) might need a genuine
argument bounding `k*(q)` rather than brute enumeration. This conjectural
scaling is **not proved** — it is a heuristic explaining the observed
numeric residual-table growth, offered to help the outliner decide how much
casework to budget for `m=3+` versus `m=2`.

### Candidate technique(s)

- **Legendre Sieve Gap Bound** (`lemmas/legendre-sieve-gap-bound.md`) and
  **Primorial Floor Bound** (`lemmas/primorial-floor-bound.md`) — both
  already certified, `M`-generic, reusable verbatim; the fix needed is in
  *how* they're applied (correct modulus, dropping the redundant `q` factor
  at `k=0`), not new machinery.
- **`m`-generalized Parity Witness / n_0,K_0 bookkeeping**
  (`lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`) — already certified,
  directly reusable, no changes needed.
- No Robin/Nicolas-style uniform bound on `ω(N)` for highly composite `N` is
  present in `knowledge_base.md` (checked: no entry mentions `ω`, "distinct
  prime factors" growth-rate bounds, Robin's inequality, or
  highly-composite-number theory at all — Number Theory section is grep-
  confirmed to have zero hits for these terms). **Not needed anyway** given
  finding (1) above — the existing crude tools suffice once applied
  correctly.

### Cheap-kill candidates

- **The modulus fix above is itself the cheap kill**: before doing ANY new
  casework for `m≥2`, redo the existing crude-bound computation with
  `r=ω(K_0)` at `k=0` (dropping `q`). This alone converts "fails everywhere"
  into "fails at ~4–19 primes for `m=2,3,4` up to `q<20000`" — i.e. Part IV's
  entire "provably insufficient" conclusion should be retracted and replaced
  with "insufficient only in a small, computable, finite band," matching
  the round-23-reviewer's independent full-truth-check finding exactly.
- No other cheap structural kill found (no parity/pigeonhole shortcut beyond
  what's already in Part I–III).

### Knowledge-base entries to use

- None beyond what's already cited (Legendre/Möbius sieve identity is the
  generic technique underlying the certified Legendre Sieve Gap Bound;
  `knowledge_base.md`'s "Divisor analysis" and "Modular arithmetic, CRT"
  entries are the closest generic headings, already implicitly in use).

### Analogous past problems (cruxes)

Searched `past_crux_moves_database.json` across `number_theory` subtopics
`divisibility-and-gcd`, `p-adic-valuation`, `pigeonhole`, keyword-filtered
for `omega`/`prime factors`/`sieve`/`gap`/`highly composite`/`Jacobsthal`/
`Robin`/`Nicolas`. **No crux found that proves a uniform bound on `ω(N)`
in terms of `log N` beyond the trivial `2^{ω(N)}≤N`**, and no crux
resembling "gap between consecutive integers coprime to a growing modulus."
The two closest hits, `aimo-0098` and `aimo-0138` (both
`divisibility-and-gcd`), use induction on the number of prime factors to
extend a closed form or lower-bound `Ω(n)` by peeling off known composite
cofactors — a genuinely different mechanism (they don't bound `ω` from
above in terms of size, they lower-bound `Ω` via explicit factorization
witnesses), not directly transplantable here. **Verdict: no closely
analogous crux; this gap is bespoke to the workspace's own sieve
machinery**, confirming round 21/22's prior conclusion that no citable
external tool exists — but this round's finding is that no such tool is
actually needed once the sieve is applied to the right (smaller) modulus.

### Prior progress

- Certified `m=1` theorem (`lemmas/a1-3q-parity-and-k0-window-lemmas.md`,
  `legendre-sieve-gap-bound.md`, `primorial-floor-bound.md`) — complete.
- Certified `m`-generalized Parity Witness + `n_0,K_0` bookkeeping
  (`lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`) — Parts I–II of
  `a1-3qk-subfamily-theorem.md`, fully `m`-independent, no further work
  needed.
- Part III's pigeonhole criterion (`m`-independent in form) — correct,
  reusable as-is.
- Part IV's "provably insufficient" conclusion — **this round's finding is
  that this is WRONG as diagnosed** (it used the wrong sieve modulus at
  `k=0`); the corrected computation above shows the certified tools likely
  DO close `m=2,3,4` (and probably general `m`) with a finite residual
  table whose size grows with `m` but remains genuinely finite and
  computable, exactly matching the round-23 proof-reviewer's independent
  "zero failures beyond q=443/1103" full-truth-check finding.

### Dead ends (do not retry)

- **Do not re-attempt "search for a uniform Chebyshev/Robin-strength bound
  on `ω(M)` vs `log M`"** — confirmed (again) absent from both
  `knowledge_base.md` and the crux corpus (round 21/22 already established
  this; this round's independent corpus search confirms it again). This
  route is closed for good reason, but **is also unnecessary** given finding
  (1): the crude elementary tools already in hand suffice once applied to
  the correct (smaller) modulus.
- **Do not re-cite Part IV's `r=ω(qK_0)` computation as evidence of
  structural insufficiency** — it is the artifact identified above, not a
  real obstruction. The round-23 proof-reviewer already flagged the
  conclusion as wrong; this round's finding pins down exactly *why* (the
  redundant `q` factor in the sieve modulus) and shows the fix is a small,
  mechanical correction, not new machinery.

### Small-case / intuition notes (conjecture, not proof)

- Numerically (own `sympy` script, primes `q<20000`), the corrected crude
  bound at `k=0` fails only at `q ∈ {11,17,23,29}` for `m=2` and at 12 named
  primes up to `q=479` for `m=3` — small, apparently complete finite lists
  (no failures found beyond these in the tested range), consistent with,
  but not a proof of, the conjecture that the full residual band (`k=0` and
  `k≥1` combined) is finite for every fixed `m≥1`.
- The `k≥1` check (own script, `q<300,k<15`) reproduces the certified `m=1`
  theorem's exact 3-instance residual table when relabeled — a strong
  correctness check on this round's method, not a new independent result.
- Conjectured (not proved) crossover scaling `k*~q^{m-2}`: explains why
  `m=1,2` have `q`-independent-size residual tables but `m≥3` may need
  `k`-ranges that grow with `q`, i.e. a genuinely 2-dimensional (not merely
  larger 1-D) finite table for `m≥3`. The outliner should budget accordingly
  — `m=2` is likely closeable with an `m=1`-style small table; `m≥3` may
  need an argument bounding `k` as a function of `q` before enumerating.
