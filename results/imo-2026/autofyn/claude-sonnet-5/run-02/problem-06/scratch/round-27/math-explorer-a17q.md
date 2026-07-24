## imo-2026-06 — lens: build-readiness audit of `a1-7q-subfamily-theorem`

### Verdict up front
`a1-7q-subfamily-theorem` is **ready for a routine one-round build**, exactly
mirroring the certified `a1-5q-subfamily-theorem` (round 26 APPROVE). I
independently re-derived the entire `p=7` instantiation from scratch (own
sympy/python scripts, not reusing anything from the approach file's claimed
numbers) and it reproduces the outline's claims exactly, cell for cell. No
new obstruction type, no surprising witness pattern, no case requiring more
than `i=5`. `Bad(7)={11,13}` is confirmed by direct simulation to `q<2000`.

### Independent recomputation (from scratch, own scripts)

**1. The `(j,r)` table, 30 cells (`j∈{2,...,6}`, `r∈{1,...,6}`).** Computed
`s_0(j,r) = j·r⁻¹ mod 7` (mapped to `{1,...,6}`) and `K_0=7+s_0∈{8,...,13}`
via `sympy.mod_inverse`. Diagonal cells (`j=r`) all give `s_0=1,K_0=8`
(matches the certified **Diagonal Characterization Lemma** `s_0(j,r)=1 ⟺
j=r` from `a1-pq-subfamily-theorem` exactly — no re-derivation needed, it's
`p`-uniform and already certified).

**2. `Q_1(7,j,r)` thresholds** computed via the certified formula
`Q_1=(p(K_0+1)+j)/s_0`. For each of the 30 cells, enumerated primes
`q≡r (mod 7)`, `q>7`, `q<Q_1` (29 total below-threshold `k=0` candidates
across all cells — comparable in size to `a1-5q`'s 12-candidate table,
scaled up for the larger 30-cell grid).

**3. Resolved every one of the 29 below-threshold `k=0` candidates** by
direct witness search (`gcd(N,a_i)` for `i=1,...,n_0`, `N=qK_0`,
`a_i=7(q+i-1)`): **27 resolve with an explicit witness** (mostly at `i=2` or
`i=3`, exactly the `a1-5q` pattern), and **exactly 2 have no witness**:
`(j,r,q)=(4,4,11)` and `(6,6,13)` — both **diagonal** cells
(`s_0=1,K_0=8`), `n_0=2` in both cases. These are precisely the two claimed
members of `Bad(7)`.

**4. `k≥1` closure spot-check.** Programmatically swept `k∈{1,...,59}` and
`q<500` per cell using the generic Legendre-sieve threshold
(`2^{ω(K)+1}(ω(K)+2)` vs window length `L`); found 20 below-generic-threshold
`(j,r,k,q)` instances in this range, and **every single one resolves with an
explicit witness** — zero "no witness" cases for `k≥1` in the tested range.
This matches the `a1-5q` pattern where all `k≥1` residuals close (the only
genuine exceptions in that theorem, too, were at `k=0`).

**5. The `s*` threshold (large-`ω(K)` regime).** Re-derived the analogous
inequality to `a1-5q`'s `(s+1)!≥9+(5/7)2^{s+1}(s+2)` for `s≥5`, using `p=7`'s
constants (`K_0≤13`, smallest admissible `q=11`):
`(s+1)!≥13+(7/12)·2^{s+1}(s+2)`. Numerically verified this first holds at
`s=5` (`720≥274.3`) and stays true for `s=6,7,8,9` — so `s*=5` again, same
value as `p=5`'s threshold, not a growing function of `p` in this range.
(An inductive proof analogous to `a1-5q`'s §5 should transfer directly —
same shape of inequality, just different constants.)

**6. Direct simulation confirms `Bad(7)={11,13}` exactly**, `q<2000`
(`math.gcd`-based simulator per workspace rule, cross-checked against the
correct legality semantics): both deviate at `n=3` (`q=11`: `a_3=88` vs
predicted `91`; `q=13`: `a_3=104` vs predicted `105`), matching the mechanism
found in step 3 exactly (`n_0=2` diagonal cells, breaking at the very next
term).

### Distinct openings
This is a single mechanical build task, not really multiple "openings" —
the whole content is: (a) build the 30-cell table (done above, ready to
transcribe), (b) close `k=0` (done above — 27/29 witnesses, 2 genuine
exceptions), (c) close `k≥1` via the sieve toolkit (spot-checked clean; full
symbolic bound derivation is the one remaining write-up task, same shape as
`a1-5q` §5), (d) prove `Bad(7)={11,13}` genuine via the exhausted-window
mechanism (trivial — same two-index/three-index hand check as `a1-5q`'s §7,
already effectively done above for `q=11` at `n_0=2`; need the `q=13` mirror,
also `n_0=2`).

### Candidate technique(s)
Identical to `a1-5q`: certified Generalized `K_0`-Boundedness + gcd-difference
Witness Lemma (`p`-uniform, already certified,
`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`) +
Legendre Sieve Gap Bound + Primorial Floor Bound
(`lemmas/legendre-sieve-gap-bound.md`, `lemmas/primorial-floor-bound.md`).
No new lemma needs to be invented — only the `p=7` numeric instantiation
needs to be written out (table, thresholds, witness list, `s*` induction).

### Cheap-kill candidates
None needed — the Diagonal Characterization Lemma (already certified, from
`a1-pq-subfamily-theorem`) is a genuine shortcut: it immediately identifies
which 6 of the 30 cells are "at risk" (`s_0=1`) without computing all 30
modular inverses by hand; a builder can cite it to justify checking the
diagonal cells first/most-carefully, though the full witness search of all
30 cells is still needed for rigor (the Minimal-Window Necessity Conjecture
that ONLY diagonal cells can fail is still open — do not skip the
non-diagonal cells' verification even though empirically they all resolve).

### Knowledge-base entries to use
Same as `a1-5q`: none of `knowledge_base.md`'s generic entries are directly
cited (this is an in-workspace certified-lemma chain, not a KB citation) —
the load-bearing certified facts are all in `results/imo-2026-06/lemmas/`:
`generalized-k0-boundedness-and-gcd-difference-witness.md`,
`legendre-sieve-gap-bound.md`, `primorial-floor-bound.md`.

### Analogous past problems (cruxes)
None newly needed — this is a direct re-instantiation of already-solved
in-workspace machinery (`a1-3q`, `a1-5q`), not a fresh crux-corpus query.

### Prior progress
`a1-7q-subfamily-theorem.md` (outline only, held out of round 26's build set
purely for capacity reasons). This round's independent recomputation
confirms every claim in that outline is correct: the 30-cell table, the
`Q_1` thresholds, `Bad(7)={11,13}` exactly, and the diagonal-cell exception
mechanism. Nothing in the outline needs correcting.

### Dead ends (do not retry)
None specific to `a1-7q` — it has not been attempted as a build yet. (General
workspace dead ends on H1/H2/FAH are irrelevant here; this subfamily theorem
is fully unconditional, no FAH/H1/H2 machinery needed, exactly like `a1-3q`
and `a1-5q`.)

### Small-case / intuition notes (labeled as conjecture where not proved)
- **Proved-here-empirically, consistent with certified theory:** all 27
  non-diagonal below-threshold `k=0` candidates resolve with a witness; only
  the 2 diagonal candidates (`q=11,13`) are genuine exceptions. This is
  strong (though not itself a proof for literally every prime — only a
  `q<2000` / bounded-`k` sweep) corroboration that the general symbolic
  closure (Legendre sieve + primorial floor, `s*=5`) will work exactly as it
  did for `p=5`.
- **Conjecture (unproved, flagged in `a1-pq-subfamily-theorem`):** the
  Minimal-Window Necessity Conjecture (only `s_0=1`/diagonal cells can ever
  be genuine exceptions) is NOT needed to close `a1-7q` — the direct
  approach (build all 30 cells, resolve each with an explicit witness or
  confirm genuine exception) sidesteps it entirely, exactly as `a1-5q` did.
  Do not let the builder get sidetracked trying to invoke or prove that
  conjecture — it is irrelevant to closing this specific theorem.
- No new obstruction type versus `p=3,5`: same 3 ingredients (gcd-difference
  witness, `K_0`-boundedness, Legendre-sieve-gap + primorial-floor), same
  qualitative pattern (small number of diagonal-only genuine exceptions,
  handful of near-threshold non-diagonal cells resolved by hand,
  overwhelming majority closed by the generic sieve bound for large `q`/`k`).
  The `s*` threshold happens to come out the same (`s*=5`) as `p=5`'s, though
  the builder should not assume this without re-deriving the induction (my
  check above is numerical spot-verification, not the inductive proof
  itself — that write-up is the one piece of real work remaining, and it's
  the same shape as `a1-5q`'s §5 induction, just with `K_0≤13` instead of `≤9`).

### What a builder needs to do (concretely)
1. Transcribe the 30-cell `(j,r)→(s_0,K_0)` table (verified above).
2. Transcribe the `Q_1(7,j,r)` thresholds and below-threshold prime lists
   per cell (29 candidates verified above).
3. Write out the 27 explicit witness computations (all reproduced above,
   `gcd(N,a_i)=1` for some `i≤5`) and the 2 genuine-exception mechanism
   proofs for `q=11,13` (both `n_0=2`, window `i=1,2` exhausted — need to
   write the 2-line check: `a_1,a_2` both share a factor with `N=88` resp.
   `N=104`).
4. Write out the `k≥1` closure: derive the `s*=5` threshold inductively
   (mirror `a1-5q` §5's induction, substitute `K_0≤13`, smallest prime
   `q≥11`), then tabulate the residual `k∈{1,...,~27}` band (`K(k)=K_0+7k`)
   and resolve the handful of below-threshold `(j,r,k,q)` quadruples with
   explicit witnesses (spot-checked clean above for `k≤59,q<500` — no
   genuine failures found, all resolve).
5. Assemble exactly as in `a1-5q` §6, and state+verify `Bad(7)={11,13}` via
   both the mechanism proof and the numeric confirmation (`q<2000`, this
   round).

This is capacity-bound, not obstruction-bound: everything needed is either
already certified (the `p`-uniform lemmas) or verified by this round's
independent recomputation. Recommend this be placed in next round's build
set as a near-certain 7th APPROVE, exactly as `a1-5q` was flagged and then
closed in round 26.
