## imo-2026-06 (lens: routine subfamily extensions via p-uniform machinery)

- Distinct openings:
  1. **a1=9q is NOT a new opening** — 9=3^2 is not prime, so it does not
     instantiate the `a1-pq` machinery (which requires `p` an odd *prime*).
     But `a_1=9q=3^2 q` is already the `a=2` instance of the **already
     certified** `a1-3aq-subfamily-theorem` (round 24 APPROVE, `a∈{1,...,5}`,
     `q≥7` outside a tiny `a`-dependent exceptional set — for `a=2` the sole
     exception is `q=11`). No new work is needed or possible here; flag this
     to the outliner so no build slot is wasted re-deriving something already
     solved.
  2. **a1=11q**: direct instantiation of the certified `a1-pq` p-uniform
     machinery (Generalized `K_0`-Boundedness + gcd-difference Witness Lemma,
     `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`) at
     `p=11`. This is the natural next member of the family
     (`p=3,5,7` already closed → `p=11` next, following the exact template
     that closed `a1-5q`/`a1-7q`).
  3. **a1=13q**: same machinery at `p=13`, an alternative/parallel next
     member (larger table, fewer exceptions — see below).
  4. **a1-3qk, m=4**: a genuinely different axis (fixed `p=3`, growing
     exponent on `q`) — already has `m=1,2,3` certified; `m=4` needs new
     per-`m` sieve constants (`K_0(q,4)~3q^3+s_0`, quartic-in-`q` modulus vs.
     the already-quadratic `m=3` case), not a fresh reduction.

- Candidate technique(s): For openings 2–3, the fully-certified,
  fully-`p`-uniform reduction in `a1-pq-subfamily-theorem` (Steps 0–6 of its
  "Full derivation") plus the round-27 **Universal Look-Back Witness
  Identity** (`lemmas/universal-look-back-witness-identity.md`) — the latter
  gives a **free, unconditional, threshold-free closure of the entire `k=0`
  layer for the `r=1` residue class** (and every `gcd(k+1,j)=1` cell, for
  every `p`), which shrinks the remaining table work for `p=11`/`p=13`
  relative to what `a1-5q`/`a1-7q` had to do by hand for their `r=1` cells.
  For opening 4, the Legendre Sieve Gap Bound + Primorial Floor Bound
  template (as used for `m=1,2,3`), with `m`-specific threshold refitting.

- Cheap-kill candidates: none needed — the machinery already reduces each
  case to a finite, mechanical (script-verifiable) table; no further
  structural pruning beyond what's already certified (Diagonal
  Characterization `s_0=1⟺j=r`, First-Risk Theorem) is required to attempt
  the table.

- Knowledge-base entries to use: none beyond the workspace's own certified
  lemma stack (this problem's KB is entirely the workspace's `lemmas/`
  directory; no generic `knowledge_base.md` entry adds anything new here
  beyond what's already cited by the `a1-pq` file).

- Analogous past problems (cruxes): not applicable — this is pure
  continuation of in-workspace certified machinery, not a fresh crux-corpus
  match; the relevant "analogy" is entirely internal (the `a1-5q`/`a1-7q`
  builds are the templates to follow).

- Prior progress: `a1-pq-subfamily-theorem` has the full `p`-uniform
  symbolic reduction proved (Steps 0–6) plus the `r=1`-layer `k=0`-closure
  (round 27). `p=3,5,7` are each fully closed as standalone certified
  theorems. `p=11,13` have NOT been instantiated by any prior round — this
  is genuinely new per-`p` work, not yet attempted.

- Dead ends (do not retry): the round-26 "Minimal-Window Necessity
  Conjecture" (that only diagonal `s_0=1` cells can ever be genuine
  exceptions) remains **unproved** (do not assume it and skip verifying
  non-diagonal cells symbolically) — however, my own fresh greedy
  simulation below is fully consistent with it (every genuine exception
  found for `p=11,13` is diagonal), so it remains safe to use as a strong
  *search heuristic* (check diagonal cells first) but not as a substitute
  for the actual per-cell threshold verification the certified template
  requires.

- Small-case / intuition notes (all conjectural / computational, own
  fresh greedy simulation, `math.gcd`, exact recurrence semantics
  "legal iff gcd>1 against ALL prior terms"):

  **Bad(11)** (search: every prime `q∈(11,6000)`, 80 terms/pair):
  `Bad(11) = {13, 17, 19, 31, 37, 43}` (6 exceptions), each deviating at a
  small `n∈{3,4,5}`:
  - `q=13`: dev at `n=3`, band `j=2`, `r=q mod 11=2` → diagonal (`s_0=1`).
  - `q=17`: dev at `n=3`, `j=6`, `r=6` → diagonal.
  - `q=19`: dev at `n=3`, `j=8`, `r=8` → diagonal.
  - `q=31`: dev at `n=4`, `j=9`, `r=9` → diagonal.
  - `q=37`: dev at `n=5`, `j=4`, `r=4` → diagonal.
  - `q=43`: dev at `n=5`, `j=10`, `r=10` → diagonal.
  All six are exactly the `s_0(j,r)=1⟺j=r` diagonal cells (Diagonal
  Characterization Lemma), matching the pattern from `p=3,5,7` (`Bad(3)=
  {5}`, `Bad(5)={7,13,19}`, `Bad(7)={11,13}`) but larger (6 vs 2-3), roughly
  consistent with `|Bad(p)|` scaling with `p`'s number of nonzero residues
  (`p-1=10` possible diagonal cells for `p=11`, of which 6 are realized as
  genuine deviations within `q<6000` — no proof that this is complete,
  purely a large-range computational sweep, same standing as the round-26
  explorer's original `Bad(5)`/`Bad(7)` sweeps before hand-verification).
  Table size for the full closure: `j∈{2,...,10}` (9 bands) `×`
  `r∈{1,...,10}` (10 residues) `=90` `(j,r)` cells, roughly `3×` the `p=7`
  table (30 cells) — a bigger but same-kind mechanical task; the `r=1`
  column's `k=0` layer is free (round-27 Universal Look-Back Corollary), so
  effectively `~81` cells need the full threshold treatment, plus per-`k`
  residual-band work analogous to `a1-7q`'s 510-cell `(j,r,k)` sweep (here
  scaled up proportionally, likely ~1500 combinations before reduction).

  **Bad(13)** (same search, `q∈(13,6000)`):
  `Bad(13) = {17, 19, 23, 47}` (4 exceptions), all diagonal:
  - `q=17`: dev `n=3`, `j=4`, `r=4`.
  - `q=19`: dev `n=3`, `j=6`, `r=6`.
  - `q=23`: dev `n=3`, `j=10`, `r=10`.
  - `q=47`: dev `n=5`, `j=8`, `r=8`.
  Table size: `j∈{2,...,12}` (11 bands) `×` `r∈{1,...,12}` (12 residues)
  `=132` cells, `~4.4×` the `p=7` table — larger mechanical burden than
  `p=11` despite fewer confirmed exceptions.

  **Recommendation on 1.**: `p=11` is the better next build target — same
  proof template as `a1-5q`/`a1-7q` (proof-reviewer has now certified this
  exact recipe three times), smaller table (90 vs 132 cells) than `p=13`,
  and `Bad(11)` is already pinned down computationally above (6 genuine
  exceptions, all diagonal, all deviating within `n≤5`, exactly analogous
  in kind to prior `Bad(p)` — **this is build-ready**: a builder can follow
  the `a1-7q-subfamily-theorem.md` file line-by-line, substituting `p=11`,
  re-deriving the `s_0(j,r)`/`K_0(j,r)` table (formula already certified,
  purely mechanical), and confirming the 6 diagonal exceptions above have
  no witness (by direct `gcd` check, as done for `q=7,13,19` at `p=5` and
  `q=11,13` at `p=7`) while every other `(j,r,k)` cell gets a threshold or
  explicit witness. `p=13` is a legitimate parallel/later target if
  capacity allows, but is more work for a similar payoff (one more certified
  subfamily instance).

  **m=4 for `a1-3qk`** (own fresh greedy simulation, `a_1=3q^4`, primes
  `q∈(7,600)`, 60 terms): **only one exception found**, `q=17` (deviates at
  `n=7`, `a_7=250580≠250581=3(17^4+6)`) — this independently **confirms**
  the round-26 rejection: any m=4 closure attempt asserting "no exceptions
  below a crude threshold" is false as stated, since `q=17` (well below any
  `~2×10^{11}`-scale threshold) is a genuine, permanent deviation. No other
  exception found up to `q<600` (a much smaller residual band than `m=2,3`
  needed relative to the range searched — plausible but not proof that
  `q=17` is the *only* exception). Pursuing `m=4` requires: (a) confirming
  `q=17`'s exception is genuinely irrecoverable (a short direct witness
  check, cheap), (b) refitting the Legendre-Sieve/Primorial-Floor threshold
  constants for the quartic-in-`q` modulus growth (`K_0(q,4)` involves
  `q^3` scaling analogous to `m=3`'s `q^2`), which the current file's own
  lines ~563-621 already flag as the known per-`m` obstacle (growing
  threshold constants, not a new obstruction in kind). This is a similar
  cost to what `m=3` took (one dedicated build round), i.e. **not cheaper**
  than `p=11`/`p=13`, and it does **not** open any new structural
  shortcut — recommend **deprioritizing m=4 this round** in favor of
  `a1-11q`, unless the outliner wants a second, parallel build track (the
  `a1-3qk` and `a1-pq` approaches are independent files, so both could be
  worked in parallel by different slugs without collision).

- **Bottom line for the outliner**: the build-ready item is **`a1-11q`**
  (exact `Bad(11)={13,17,19,31,37,43}` table above, all diagonal, all
  deviating by `n=5`, ready for a builder to reproduce the `a1-7q`-style
  30-cell-analog (here 90-cell) table and close it). `a1-13q` is a valid,
  slightly-more-expensive alternative (`Bad(13)={17,19,23,47}`). `a1-9q`
  needs no work (already covered by certified `a1-3aq`, `a=2`). `m=4` for
  `a1-3qk` is a real but not-cheaper alternative target; its round-26
  "false at `q=17`" diagnosis is independently confirmed correct here, and
  any viable m=4 statement must exclude `q=17` explicitly.
