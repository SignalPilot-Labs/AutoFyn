## imo-2026-06

### Context this round
Two consecutive dedicated H1/FAH fresh-corridor searches (rounds 26, 27) find
nothing new — 20+ plateau rounds on the general theorem, reinforced this round
by a systematic crux-corpus sweep (including the closest un-transplanted analog,
aimo-0907, confirmed dead-on-arrival for the same "no for-free closed-form
orbit-coincidence" reason as the already-dead orbit-merging-additive-offset
mechanism). Per the standing memory rule (round 17: after 3+ exhausted sweeps,
redirect effort to secondary/consolidation content rather than forcing an nth
mechanism), I am NOT opening a new general-H1/H2 approach this round — there is
no fresh lever to hang one on, and forcing one would waste a build slot. The
productive frontier remains exactly where round 26 identified it: the
subfamily-theorem track (near-certain, mechanical, real Elo) and the
Minimal-Window Necessity Conjecture's precisely-diagnosed residual gap. I am
also opening one genuinely new sub-target inside `a1-pq-subfamily-theorem`
(the `r=1` special case) rather than re-proposing the same general-conjecture
mechanism verbatim, per the memory rule against re-patching a stuck gap with
no new idea.

---

### a1-7q-subfamily-theorem: advance
Target: For `a_1=7q`, prime `q≥11`, `q∉Bad(7)={11,13}`: `a_n=7q+7(n-1)` for
every `n≥1` (literal, unconditional periodicity for this restricted `a_1`
subfamily).
Technique: Identical template to the certified `a1-5q-periodicity-theorem`
(round 26 APPROVE) — Generalized `K_0`-Boundedness + gcd-difference Witness
Lemma (`p`-uniform, already certified) + Legendre Sieve Gap Bound + Primorial
Floor Bound, instantiated at `p=7`.
Skeleton:
  1. Build the 30-cell `(j,r)→(s_0,K_0)` table, `j∈{2,...,6}`, `r∈{1,...,6}`,
     via `s_0(j,r)=j·r⁻¹ mod 7`, `K_0=7+s_0` — by the certified Generalized
     `K_0`-Boundedness Lemma.
  2. Compute the `Q_1(7,j,r)=(7(K_0+1)+j)/s_0` threshold per cell and
     enumerate `q≡r (mod 7)`, `q>7`, `q<Q_1` — 29 below-threshold `k=0`
     candidates (explorer-verified this round).
  3. Resolve each of the 29 candidates by an explicit `gcd(N,a_i)` witness,
     `N=qK_0`, `a_i=7(q+i-1)`, `i≤5` — by direct computation. 27 resolve; the
     2 that don't (`(j,r,q)=(4,4,11)`,`(6,6,13)`) are the diagonal (`s_0=1`)
     cells, matching the certified Diagonal Characterization Lemma's
     prediction of where exceptions concentrate.
  4. Prove `Bad(7)={11,13}` genuine: both are `n_0=2` window-exhaustion cases
     — `a_1,a_2` both share a factor with `N=88` resp. `N=104` — the same
     two-term hand check as `a1-5q`'s exceptional-set proof.
  5. Close `k≥1`: derive the `s^*` sieve threshold
     `(s+1)!≥13+(7/12)2^{s+1}(s+2)` inductively (mirrors `a1-5q`'s §5
     induction verbatim, substituting `K_0≤13`, smallest admissible `q=11`);
     verify `s^*=5` (numerically corroborated at `s=5,...,9` this round,
     the induction itself is the write-up task).
  6. Tabulate the residual `k∈{1,...,~27}` band and resolve the below-generic-
     threshold `(j,r,k,q)` quadruples with explicit witnesses (spot-checked
     clean this round for `k≤59,q<500` — zero failures).
  7. Assemble: for every `q∉{11,13}`, every cell/every `k` closes with either
     an explicit witness or falls above the generic sieve threshold — hence
     `a_n=7q+7(n-1)` for all `n`.
  8. State and verify `Bad(7)={11,13}` exactly, both via the mechanism proof
     (step 4) and by direct simulation to `q<2000` (this round's explorer
     independently confirmed both deviate at `n=3` with the exact predicted
     off-values).
Key lemmas (claim + mechanism):
  - Diagonal cells (`j=r`) are exactly the `s_0=1` cells — because
    `s_0(j,r)=1 ⟺ j≡r (mod p)`, a direct congruence identity (already
    certified, `p`-uniform, no re-derivation needed).
  - `Bad(7)={11,13}` exactly — because these are the only two `(j,r,q)`
    triples where the legality window (`i=1,2`) is fully exhausted before
    any witness prime appears, i.e. both `a_1` and `a_2` already share a
    factor with `N=qK_0`.
  - All 27 non-diagonal below-threshold cells and all sampled `k≥1` residuals
    resolve — because the gcd-difference identity supplies an explicit
    shared factor at some `i≤5` in every non-exhausted-window case.
Open gaps: the full symbolic `s^*=5` induction (step 5) is not yet written
out — only numerically spot-checked; this is the one genuine write-up task,
not a new obstruction.
Cases to cover: 30 `(j,r)` cells × (`k=0` vs `k≥1`); all resolved above except
the induction write-up.
Watch out for: do not invoke the still-open Minimal-Window Necessity
Conjecture — this approach does not need it (all 30 cells are directly
verified, sidestepping the conjecture exactly as `a1-5q` did). Do not skip
verifying the non-diagonal cells even though they all empirically resolve —
the conjecture that only diagonal cells can fail is unproved in general.

---

### covering-system-construction: advance (light, capped scope)
Target: (unchanged) general Cofinite/Joint FAH machinery via covering-system
constructions on specific test seeds — this round's addition is a bounded,
low-priority housekeeping close, not new general-theorem content.
Technique: Finite-Window Literalization Lemma (certified, round 26),
reapplied to the `a_1=11305` seed's residual `B'`-side closure.
Skeleton:
  1. State the recomputed setup for `a_1=11305`: `S₀`, rogue pair
     `A'={2,5}`, `B'={3,7}`, canonical witnesses `n_A=7`, `n_B=4` (note the
     order swap vs. `a_1=4807`, where `n_A<n_B` — here `n_B<n_A`).
  2. `A'`-side is already free: `F''_4={11}` singleton at the canonical
     witness `n_B=4` — apply Singleton-Side FAH directly, giving `11|a_n`
     for literally every `n>4` with `ρ(n)=A'`, zero exceptions (verified to
     45,000 terms).
  3. `B'`-side: use the already-certified non-canonical witness `x_2=103`
     (`a_103=12100`, `P(a_103)\S₀={11}` singleton) with Singleton-Side FAH to
     get cofinite `11|a_n` for `ρ(n)=B'`, `n>103`.
  4. Check the finite-window side condition of the Finite-Window
     Literalization Lemma with roles relabeled (`Ã'=B'`, `ñ_B=n_A=7`,
     `x̃_1=103`): is there any `n∈(7,103]` with `ρ(n)=B'`? Exhaustive check:
     no — the `B'`-occurrence list starts `4,119,290,...`, nothing in
     `(7,103]`.
  5. Conclude literal (zero-exception) Joint FAH for `a_1=11305`'s standing
     rogue pair, shared witness `q=11`, from `n>4`, mirroring `a_1=4807`'s
     Step 4h exactly with labels swapped.
Key lemmas (claim + mechanism):
  - The Finite-Window Literalization Lemma applies here despite the
    `n_A`/`n_B` order swap — because its proof only needs a two-case split
    (`n>x_1` vs. finite window) and a canonical-order relabeling absorbs the
    swap without altering the argument's validity.
Open gaps: none beyond transcription — this round's explorer already
verified every claim to 45,000 terms with two independent implementations.
Cases to cover: none beyond the two sides (`A'`, `B'`), both closed above.
Watch out for: do not let the builder blindly substitute into the Lemma's
literal `A'`/`B'`-labeled statement without first checking canonical order —
a careless verbatim substitution (ignoring the `n_B<n_A` swap here) could
silently produce the wrong window interval. Scope explicitly: this closes
ONE more single-seed instance (now 2/2 known hard test seeds), not a general
theorem — do not let the write-up imply otherwise.

---

### a1-pq-subfamily-theorem: revise (new sub-target: r=1 special case)
Target: (unchanged, general) the Minimal-Window Necessity Conjecture for the
`a_1=pq` family — but this round's gap re-plan narrows to a genuinely cleaner
first sub-case rather than re-attempting the full conjecture with the same
tools that already stalled.
Technique: Direct verification restricted to `r=1` (i.e. `q≡1 (mod p)`), the
cleanest falsification/proof target identified in round 26's gap report —
because when `r=1`, no `j∈{2,...,p-1}` satisfies `j≡r (mod p)` (the diagonal
band requires `j≡r`, but `j` never equals `1` in its range), so **there is no
diagonal band at all** for `r=1`. This eliminates the exact masking effect
(diagonal-band-tested-first) that made the general conjecture hard to close,
turning "prove no non-diagonal band ever produces a genuine exception" into
a self-contained, diagonal-free question for this one residue class.
Skeleton:
  1. Restrict to `q≡1 (mod p)`. By the certified Diagonal Characterization
     Lemma, every band `j∈{2,...,p-1}` has `s_0(j,1)=j≠1` (mod `p`, since
     `j` ranges over `2..p-1`), so no band is diagonal — the First-Risk
     Theorem's "diagonal tested first" statement is vacuous here; all bands
     are on equal footing.
  2. For each band `j`, compute `s_0(j,1)=j` directly (since `r⁻¹=1` when
     `r=1`), so `K_0(j,1)=p+j` — a clean, fully explicit closed form (no
     modular inverse needed), unlike the general `r` case.
  3. Compute `Q_1(p,j,1)=(p(K_0+1)+j)/j` per band and enumerate below-
     threshold primes `q≡1 (mod p)`, `q<Q_1` — a finite, explicit table with
     `p-2` bands (fewer than the general `p-1`-residue case, since `r` is
     fixed).
  4. Attempt to resolve every below-threshold `(j,q)` cell with an explicit
     gcd-difference witness (same mechanism as `a1-5q`/`a1-7q`, `i≤s_0(j,1)+
     const`), aiming to show NONE produce a genuine exception (window never
     exhausted) — the concrete falsification test round 26's gap report
     asked for.
  5. If step 4 succeeds (zero genuine exceptions for `r=1` across a swept
     range of `p`), this proves the Minimal-Window Necessity Conjecture's
     `r=1` special case unconditionally (a full sub-theorem: "for `q≡1
     (mod p)`, `a_1=pq` has no exceptions at all") — a genuine, checkable,
     narrower target than the full conjecture, and real Elo-worthy content
     either way (proof or a precisely located `r=1` counterexample, which
     would itself refute the general conjecture cleanly, without any
     diagonal-masking ambiguity).
Key lemmas (claim + mechanism):
  - No diagonal band exists for `r=1` — because diagonal means `j≡r`, and
    `j` ranges over `{2,...,p-1}`, never equal to `1`; this is immediate
    from the certified Diagonal Characterization Lemma's exact statement.
  - `K_0(j,1)=p+j` in closed form — because `s_0(j,r)=j·r⁻¹ mod p` and
    `r=1 ⟹ r⁻¹=1`, so `s_0(j,1)=j` directly, no modular inverse computation
    needed.
Open gaps: whether all below-threshold `(j,q)` cells for `r=1`, across a
representative sweep of `p`, resolve with a witness (step 4) is unproved —
this is the actual new content to build this round. If a genuine exception
IS found for some `r=1` cell, that refutes the general Minimal-Window
Necessity Conjecture cleanly (no diagonal-masking confound), which is itself
valuable information, not a failure.
Cases to cover: `j∈{2,...,p-1}` for a swept range of small primes `p`
(`p=5,7,11,13,...`), `r=1` fixed, `k=0` and `k≥1` bands.
Watch out for: do not conflate "zero exceptions found for `r=1` up to a
finite sweep" with "proved for all `p`" — the builder must either give the
general symbolic argument (using the closed-form `K_0=p+j`) or explicitly
flag the result as a computational sub-result, exactly per the round-26
memory rule on not letting numeric confirmation stand in for proof.

---

### a1-3qk-subfamily-theorem: advance (breadth, low priority)
Target: (unchanged) `a_1=3q^m` for general `m≥1` — `m=1,2,3` are already
certified standalone theorems; this round nominates continued work on
`m=4` to keep the population from narrowing entirely to the `pq`-family
track.
Technique: Same Legendre Sieve Gap Bound + Primorial Floor Bound machinery
as `m=1,2,3`, re-derived (not copy-pasted) for `m=4`'s specific numeric
thresholds, per the standing memory rule that prime-support-only steps
transfer but numeric exceptional tables must be redone from scratch.
Skeleton: unchanged from the existing file's `m=4` open-gap section — growing
threshold constants and the `m`-specific OR-split re-derivation are the two
named obstacles.
Key lemmas: none new this round (no explorer touched this front) — nominated
purely to preserve breadth in the build set at low cost; if capacity is tight,
this is the first to drop in favor of the three above.
Open gaps: growing threshold constants for `m=4`; the `m`-specific OR-split.
Cases to cover: `m=4`'s residual `(q,k)` table, analogous to `m=1,2,3`.
Watch out for: do not copy `m=3`'s exceptional witness table verbatim — the
actual integers being gcd-checked change with `m`.
</content>
