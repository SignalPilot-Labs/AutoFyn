## imo-2026-06 (lens: readiness verification for a1-13q subfamily build)

- Distinct openings:
  1. **a1-13q is genuinely build-ready** — a routine mechanical instantiation
     of the fully certified `p`-uniform machinery
     (`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`,
     `lemmas/legendre-sieve-gap-bound.md`, `lemmas/primorial-floor-bound.md`,
     `lemmas/universal-look-back-witness-identity.md` `r=1` corollary),
     exactly mirroring the `a1-5q`/`a1-7q`/`a1-11q` template. I independently
     recomputed **every** piece of the recipe from scratch (not reading off
     round-28's numbers) and it all closes with no new obstruction type.
  2. One genuine (but harmless, routinely-handleable) new bookkeeping wrinkle
     appears at `p=13` that did **not** occur at `p=11`: a single prime
     (`q=19`) has **two** distinct below-threshold `k=0` candidate bands with
     no witness (`(j,r)=(6,6)` at `n_0=2`, **and** `(j,r)=(12,6)` at
     `n_0=3`), because both bands share residue `r=q\bmod13=6`. The first
     (`n_0=2`) is the genuine, actually-occurring deviation; the second
     (`n_0=3`) is vacuous in the real sequence (its premise `H(3)` never
     holds for `q=19`, since the sequence already broke at `n=2`) and must
     be explicitly flagged **moot** in the writeup — exactly the same
     "moot because `q\in\mathrm{Bad}(p)`" bookkeeping already used for the
     `k\ge1` layer in `a1-11q` §7, just needed one layer earlier (`k=0`)
     here. This is a routine documentation point, not a proof gap — flag it
     to the builder explicitly so the writeup doesn't silently drop this
     cell or (worse) miscount it as a 5th distinct exceptional prime.

- Candidate technique(s): identical to `a1-11q-subfamily-theorem.md` — Steps
  0–8 of that file's structure, substituting `p=13`. No new technique
  needed.

- Cheap-kill candidates: none needed — same as round-28's assessment, the
  machinery already reduces everything to a finite, script-verifiable table.

- Knowledge-base entries to use: none beyond the workspace's own certified
  lemma stack (as with `a1-11q`); this is pure internal-machinery
  instantiation, no external KB entry applies.

- Analogous past problems (cruxes): not applicable — internal continuation
  of already-certified in-workspace machinery, same as round-28's finding.

- Prior progress: `a1-pq-subfamily-theorem` (general-`p` machinery,
  certified) + `a1-5q`, `a1-7q`, `a1-11q` (all APPROVEd instantiations).
  `a1-13q` has NOT been built by any prior round — round 28's explorer only
  ran the greedy simulation to get `Bad(13)`, not the table/threshold/
  witness work. This round supplies that missing table-level verification.

- Dead ends (do not retry): none new. The round-26 "Minimal-Window
  Necessity Conjecture" remains unproved in general but is (again)
  consistent with all 5 genuine exceptions found here being on the diagonal
  band `j=r` (see below) — usable as a search heuristic only, not a
  substitute for the full per-cell check (already done below, so this is
  moot for the actual build).

- Small-case / intuition notes — **all independently recomputed from
  scratch this round** (fresh Python/`sympy` scripts, distinct from
  round-28's), full details below (conjectural in the sense that the greedy
  resimulation is numeric evidence, but the table/witness computations are
  exact, deterministic finite verifications matching the a1-11q proof
  method exactly, not conjectures):

  **1. Fresh greedy resimulation** (`a_1=13q`, every prime `q\in(13,6000)`,
  777 primes, 10 terms each, literal "legal iff `\gcd>1` against ALL prior
  terms" semantics): **exactly reproduces round-28's claim**,
  `\mathrm{Bad}(13)=\{17,19,23,47\}`, deviating at:
  - `q=17`: `n=3`, `a_3=238` (closed form would give `247`).
  - `q=19`: `n=3`, `a_3=266` (closed form would give `273`).
  - `q=23`: `n=3`, `a_3=322` (closed form would give `325`).
  - `q=47`: `n=5`, `a_5=658` (closed form would give `663`).

  **2. The 132-cell `(s_0,K_0)` table** (`j\in\{2,\dots,12\}`,
  `r\in\{1,\dots,12\}`, `s_0=j\cdot r^{-1}\bmod13`, `K_0=13+s_0`):
  independently built via `sympy.mod_inverse`. `K_0\in\{14,\dots,25\}`
  throughout (min `14` on the diagonal `j=r`, max `25`). Diagonal cells all
  give `s_0=1,K_0=14`, matching the Diagonal Characterization Lemma.

  **3. `k=0` layer closure.** Sufficient-window threshold
  `Q_1(j,r)=(13(K_0+1)+j)/s_0`; below-threshold `(j,r,q)` `k=0` candidates:
  **116** total (vs `a1-11q`'s 76, `a1-7q`'s 29, `a1-5q`'s 12 — consistent
  scaling with table size). Direct witness search (`i=1,\dots,n_0`) resolves
  **111** of these; exactly **5** have no witness:
  `(4,4,17)` `n_0=2,N=238`; `(6,6,19)` `n_0=2,N=266`; `(10,10,23)`
  `n_0=2,N=322`; `(8,8,47)` `n_0=4,N=658`; and **`(12,6,19)` `n_0=3,N=285`**
  — all diagonal (`j=r`) **except** the last, which shares residue class
  `r=6` with `(6,6,19)` (both have `q=19\equiv6\pmod{13}`). The first four
  correspond exactly, one-to-one, to `\mathrm{Bad}(13)=\{17,19,23,47\}`
  (matching the resimulation's deviation indices/values exactly, e.g.
  `q=19`: `n_0=2\Rightarrow` deviation at `n=n_0+1=3`, `a_3=266` — matches).
  The fifth, `(12,6,19)`, is the **moot duplicate** described above: since
  `q=19` already deviates at the smaller `n_0=2` (band `j=6`), the premise
  needed for the `j=12,n_0=3` analysis (`H(3)`) never actually holds in the
  real sequence — this cell is vacuous, not a 5th distinct exceptional
  prime. **Confirmed no other prime has this duplicate-band pathology**: a
  full duplicate-band audit (any `q` appearing in `\ge2` below-threshold
  bands) found 20 such primes, but for every one except `q=19` **all** of
  its multiple bands resolve with an explicit witness (e.g. `q=71` has
  three below-threshold bands `(5,6),(6,6),(12,6)`, all `r=6`, all
  witnessed).

  **4. `k\ge1` residual band.** Re-derived the `s^*=5` threshold analog:
  `(s+1)!\ge25+\tfrac{13}{17}\cdot2^{s+1}(s+2)` for `s\ge5` (`K_0\le25`,
  least admissible prime `q_{\min}=17`) — verified numerically `s=5,\dots,11`
  (holds with wide margin, same induction template as `a1-11q` applies
  unchanged, since it only uses `s^2+2s-2\ge0` for `s\ge1`). Generic bound
  (`\omega(K)\le4\Rightarrow` bound `192`) forces `k\ge12` to be uniformly
  safe (`17\times12=204\ge192`), so the **residual band is `k\in\{1,\dots,
  11\}`** (vs `a1-11q`'s `\{1,\dots,14\}`, smaller here since `q_{\min}=17>13`
  shrinks it faster). Sweeping all `132\times11=1452` cell/`k` combinations
  (skipping `r=1` cells with `\gcd(k+1,j)=1`, free by the Universal
  Look-Back Corollary) finds exactly **29** below-threshold `(j,r,k,q)`
  quadruples: **19 moot** (`q\in\mathrm{Bad}(13)`) and **10 non-moot**
  (`q\in\{29,31,37,41,43,53,59,61\}`) — all 10 independently resolved by
  explicit witness search (e.g. `(2,5,2,31)`: `n=70,N=1302,` witness `i=7`;
  full list of all 10 witnesses computed and verified).

  **5. Full 200-term literal-periodicity spot-check** for 15 sample primes
  `q\in\{29,\dots,97\}\setminus\mathrm{Bad}(13)`: zero mismatches against
  `a_n=13(q+n-1)` throughout, consistent with the theorem.

- **Readiness verdict**: **YES, build-ready**, following the exact
  `a1-11q-subfamily-theorem.md` template with `p=13` substituted throughout.
  `\mathrm{Bad}(13)=\{17,19,23,47\}` — confirmed exactly matching round 28's
  simulation-only claim, now backed by the full table/threshold/witness
  verification round 28 had NOT yet done. **One extra care point for the
  builder** (not present in the `a1-11q` writeup, and not mentioned in
  round 28's note): when resolving the `k=0` layer, band `(j,r)=(12,6)` at
  `q=19` (`n_0=3`) is a second no-witness cell that must be explicitly
  labeled **moot** (vacuous premise, since `q=19` is already excluded via
  its smaller `n_0=2` deviation in band `(6,6)`) — otherwise a careless
  writeup might either (a) miscount `\mathrm{Bad}(13)` as having 5 elements
  with two "reasons" for `19`, muddying the exception list, or (b) skip
  checking `(12,6,19)` at all under the wrong assumption that once a prime
  is confirmed bad via one band, no other band needs auditing (which
  happens to be true for the *conclusion* but was not obviously true a
  priori — the audit above found it needed to be checked and IS moot, not
  assumed moot). No other new obstruction type, no algebraic surprises, no
  discrepancy from round 28's headline numbers (Bad(13) set and table size
  132 both confirmed exactly).
