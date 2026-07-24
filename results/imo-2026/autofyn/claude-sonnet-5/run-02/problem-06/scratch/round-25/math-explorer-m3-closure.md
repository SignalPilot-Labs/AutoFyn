## imo-2026-06 (lens: does a1-3qk-subfamily-theorem's m=3 gap extend routinely, or is it a genuine regime change?)

- Distinct openings:
  1. **Direct transplant of the m=2 template with corrected thresholds** (what the
     current.md "Open gap" section recommends): redo Claim 1 (large-r "auto" branch)
     and Claim 2 (small-r generic-bound threshold) for k=0 with `K_0(q,3)=3q^2+s_0`
     in place of `K_0(q,2)=3q+s_0`, then redo the k≥1 band (B0-B2) analogously. This
     round's numerics (below) show this is entirely tractable and the resulting
     residual table is *comparable in size* to m=2's, not exploding — so this is the
     recommended concrete route, not a research-level obstruction.
  2. **A uniform-in-m argument** proving the whole `a_1=3q^m` family (all m≥1 at
     once) via a single sieve derivation parametrized by m, rather than doing m=3,
     m=4, ... one at a time. Not attempted by any approach yet; would save huge
     duplicated casework if it works, but nobody has written down whether the
     Claim-1/Claim-2 style argument literalizes cleanly with m as a free parameter
     (see point 3 below on why induction-on-m looks awkward).
  3. **Induction on m using the m=2 (or m-1) result as a black box** — investigated
     below (point 3 of the dispatch). Does NOT look available: the K_0(q,m) recursion
     `K_0(q,m)=3q^{m-1}+s_0` does not telescope against `K_0(q,m-1)=3q^{m-2}+s_0` in
     any way that lets the sieve-closure of level m-1 imply level m (they are sieve
     bounds against genuinely different moduli, not nested). No opening found here;
     each m needs its own from-scratch Claim-1/Claim-2 derivation (though the SAME
     technique/template applies each time — see opening 1).

- Candidate technique(s): the certified **Legendre Sieve Gap Bound**
  (`lemmas/legendre-sieve-gap-bound.md`) + **Primorial Floor Bound**
  (`lemmas/primorial-floor-bound.md`), used exactly as in the m=2 closure
  (`lemmas/a1-3q-squared-periodicity-theorem.md`): split on `r=ω(K)` (or `ω(qK)`)
  large (handled unconditionally via a sharpened `(r+1)!≥C·2^r(r+1)+D` induction,
  same shape as the certified corollary, just with a different constant `C` fitted
  to the new `K_0(q,3)~3q^2` vs `L~q/3` growth-rate mismatch) vs small (generic
  constant bound `2^r(r+1)≤` some cap, giving an explicit finite `q`-threshold).
  No new machinery is needed — this is the SAME toolset, re-derived with new
  constants, not a different theorem.

- Cheap-kill candidates: none needed here — this is a closure/bookkeeping task, not
  a search for a disproof. The main "cheap kill" already performed (this round, see
  below) is the numeric sanity check that would have revealed a genuine regime
  change (unboundedly growing residual table) had one existed; it did not.

- Knowledge-base entries to use: none beyond the already-certified in-workspace
  lemmas above (`knowledge_base.md` itself has no sieve/Jacobsthal-type entry — grep
  confirms only a passing mention of "Legendre symbol" in the quadratic-residue
  context, unrelated). This whole toolchain is workspace-local (rounds 22-24), not
  from the generic knowledge base.

- Analogous past problems (cruxes): not applicable — this is a closure step on an
  already-adopted in-house technique (Legendre sieve + primorial bound), not a
  fresh problem-solving move that benefits from the crux corpus. (Consistent with
  round 22's math-explorer note that this sieve bound was found to be self-contained
  and not present in the corpus.)

- Prior progress: `m=1` (certified, `a1-3q-parity-and-k0-window-lemmas.md` +
  the base `a_1=3q` theorem) and `m=2` (certified,
  `lemmas/a1-3q-squared-periodicity-theorem.md`) are both fully closed, unconditional,
  independently re-verified theorems. Parts I-III of the `a_1=3q^m` induction are
  proved `m`-generically already (certified,
  `lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`) — only Part IV (Case (b),
  `n` even) remains open for `m≥3`, exactly as `current.md` states.

- Dead ends (do not retry):
  - Round 23's original diagnosis ("provably insufficient for m≥2 — a systematic
    mismatch of growth rates, not a routine finite check") was **retracted** in
    round 24 as a sieve-modulus bookkeeping bug (wrong modulus `qK_0` used at k=0
    instead of the correct `K_0` alone). Do not resurrect this framing for m=3 —
    the analogous worry ("K_0 quadratic in q now, is this a genuine regime change?")
    is explicitly addressed by this round's numerics and appears to be the SAME kind
    of false alarm: the table stays finite (see below), it is just larger/differently
    shaped than m=1,2's tables.
  - The current.md "Open gap" section's own speculation — "`k*~q^{m-2}` crossover…
    m=3's k≥1 band may need a genuinely two-dimensional (not just larger 1-D) finite
    argument" — is **not supported** by this round's direct numeric test (see below):
    the failing-k values for m=3 stay small (max 7, occurring only at q=7) and
    **zero** failures occur for q≥2000 at any k up to 30, i.e. no growth with q at
    all, contradicting the `k*~q^{m-2}=q^1` growing-threshold conjecture. This
    speculative paragraph in current.md should be corrected/retracted by the next
    builder, not treated as an established obstruction.

- Small-case / intuition notes (all conjectural until formally re-derived, but with
  strong, exhaustive-feeling numeric support — own fresh `sympy`/Python scripts,
  distinct from any prior round's):
  - **k=0 band, m=3**: scanned all primes `q∈[7,60000)`, `q≠5`. Crude sieve bound
    `L≥2^r(r+1)` (`r=ω(K_0)`, `K_0=3q^2+s_0`, `L=n_0-1`) fails at **exactly 12**
    primes, ALL with `q≤479`: `q∈{11,17,19,23,29,41,53,59,61,71,89,479}`. Zero
    further failures up to `q=60000`. Every one of the 12 has an explicit witness
    `i` (mostly `i=3`, one `i=4` at `q=61`) with `gcd(q^3+i-1, K_0)=1`, directly
    verified. This exactly matches the round-24 explorer's earlier scan (same 12
    primes, same max `q=479`) — independently reproduced here with a fresh script.
  - **k≥1 band, m=3**: scanned `q∈[7,20000)`, `k∈[1,30]` (and spot-checked `k` up
    to 100 for smaller `q`). Found **14 additional** `(q,k)` crude-bound-failure
    instances, ALL at `q≤71` and `k≤7` (largest: `q=7,k=7`). Every one of the 14 has
    an explicit small-`i` witness (`i∈{2,3,5,7}`), directly verified by `gcd`. **Zero**
    failures found for `q≥2000` at any `k≤30`, and zero for `q∈[71,2000)` at any
    `k≤100` in the finer spot-check — i.e. the residual `(q,k)` table looks exactly
    as finite and small as m=1's 18-entry table and m=2's 9-entry table (here: 12+14
    = 26 total explicit exceptions, all with `q≤479`, all resolved by direct witness).
    **This directly contradicts current.md's own speculative worry** that the k≥1
    band "may need a genuinely two-dimensional finite argument" — the evidence points
    to a routine, if slightly larger, 1-D-per-branch finite table, structurally
    identical in kind to m=1/m=2.
  - **End-to-end full-theorem check (not just the sieve-criterion, the actual greedy
    recursion)**: simulated the literal IMO recursion (`a_{n+1}` = smallest integer
    `>a_n` with `gcd(a_{n+1},a_i)>1` for all `i≤n`) from scratch, no formula assumed,
    for `a_1=3q^3`, `q∈{7,11,13,17,19,23,29,59,71}`, out to 1000-2200 terms each
    (covering every flagged exceptional `(q,k)` index above with margin). **Zero
    mismatches** against the predicted closed form `a_n=3(q^3+n-1)` in every single
    case. Strong (though still numeric, not a proof) confirmation that the m=3
    theorem is TRUE and that the sieve-witness resolutions found above are correct.
  - **General-m spot check (m=4,5)**: for k≥1, `q<1500`, the max failing-k value
    grows mildly with m (7 at m=3, 12 at m=4, 14 at m=5, each at a small `q`) but
    stays uniformly bounded in `q` for each fixed `m` — no sign of `q`-dependence of
    the threshold at any tested `m`. Consistent with "one finite, `m`-dependent
    (larger for larger `m`) but still-finite table per fixed `m`," i.e. the same
    template genuinely generalizes to arbitrary fixed `m`, just with more work
    (bigger constants/case count) as `m` grows — not a different kind of argument.

- **Concrete answer to dispatch question 4**: this is a **routine finite-table
  close**, structurally identical in kind to the already-solved m=1 and m=2 cases —
  NOT a genuine regime change requiring new machinery. The apparent difficulty
  (`K_0` quadratic instead of linear in `q`) only affects the *constants* in the
  Claim-1/Claim-2-style threshold derivation (the sharpened Primorial-Floor
  corollary `(r+1)!≥C·2^r(r+1)+D` needs re-fitting since `K_0~q^2` while `L~q`,
  a genuine order-of-magnitude gap the current builder correctly flagged as
  needing care) — but this round's exhaustive numeric scan (q up to 60000 for k=0,
  q up to 20000 for k≥1) finds a residual table of comparable size (26 total
  explicit exceptions, all q≤479) to m=1's (18) and m=2's (9), all resolvable by
  direct witness search exactly as before. The next builder should: (1) redo Claim
  1's sharpened factorial-vs-exponential induction with the correct exponent for
  `K_0~3q^2` (the base case and coefficient will differ from m=2's `(r+1)!≥9·2^r(r+1)+8`,
  but the SAME induction pattern works — since `r` grows only like `O(log q)` via the
  primorial floor bound while `L~q/3` grows linearly, the "auto" branch still
  eventually wins); (2) redo Claim 2's finite threshold computation (solve
  `L≥`generic-cap for the worst branch, an easy closed-form inequality in `q`);
  (3) verify the resulting finite residual table (predicted: the same 12 (k=0) + 14
  (k≥1) = 26 instances found numerically here, or a table containing them) via direct
  witness search (all already found above, all succeed, mostly at `i=3`); (4) confirm
  no further residuals exist by pushing the analytic threshold derivation to cover
  `q` beyond 60000/20000 (this round's numeric scan is strong evidence but not a
  proof that the table stops at `q=479`/`q=71`). This is estimated to be comparable
  effort to the m=2 closure (one round), not a multi-round research gap.
