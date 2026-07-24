## imo-2026-06 (diversity-scout lens)

### Job 1: is there a genuine new angle on `a1-pq-subfamily-theorem`'s r=1 k≥1 residual or general r≠1 closure?

**Verified by independent computation this round** (own script, not read from the
file): for `p∈{5,7,11,13}`, `q≡1 (mod p)` prime, every band `j`, every
`k=1..5` with `gcd(k+1,j)>1` (i.e. exactly the residual cells round 27/28
left open), I directly computed, from the closed-form values `a_i=p(q+i-1)`
(no need to run the full greedy simulation — confirmed separately that the
closed form does hold throughout for these `q`, see below), the smallest
index `i` with `gcd(a_n+j, a_i)=1` (a genuine illegality witness). **Result
(207 cells checked): every single witness is at a SMALL index, `i≤7`**
(values seen: 2,3,4,5 — overwhelmingly `i=3`), never at a `k`- or
`n`-dependent look-back distance. This is exactly the behavior the existing
window/sieve mechanism (Steps 4-5 of the certified derivation: window
`{q+1,...,q+K(k)-1}` contains an element coprime to `K(k)`) predicts — a
small `i` exists because `K(k)=p(k+1)+j` typically has few prime factors, so
a short window suffices. **This is a genuine, honest negative finding: no
new closed-form witness (in the style of round 27's `i=n` or the tried-and-
failed `i=n-k`, `i=n-k-1`) governs these residual cells — they are resolved
exactly by the pre-existing per-`(p,j,r,k)` sieve/threshold machinery,
consistent with (not beyond) what's already certified.** I also
independently re-confirmed, via a full greedy re-simulation (not just the
closed-form shortcut) for `p∈{5,7,11,13}` and 6-10 primes `q≡1 (mod p)` per
`p` out to 40-2700+ terms, that **zero exceptions** occur in the `r=1`
class in every sample tested (consistent with round 26/27's "0/203" and
"0 of 3000+" findings) — this strengthens the r=1-exception-free conjecture
empirically but is still only evidence, not a proof.

**Honest verdict: no genuine new closing angle found this round for either
gap.** The r=1 k≥1 residual is not closable "for free" by any further
uniform witness-identity trick (I confirmed round 27's own negative finding
that `d=k` and `d=k+1` fail, and did not find a third clean distance); it
remains exactly a finite per-`p` computation (now with a strictly smaller
candidate set thanks to round 27/28's closed forms, but still requiring the
same Legendre-Sieve/Primorial-Floor machinery cell by cell). The general
`r≠1` `k=0` closure genuinely needs the per-`p` sieve as before; round 28's
Uniqueness-of-`r=1` Theorem is real content but (as its own file honestly
states) is bookkeeping, not new leverage — I confirm this diagnosis is
correct, not overclaimed.

**Recommendation for the outliner:** the only concrete next step on this
approach that is NOT "more bookkeeping" is to actually carry out the finite
per-`p` residual verification for a SPECIFIC `p` restricted to `r=1` (e.g.
`p=5` or `p=7`), which — per round 27's own note — is a strictly smaller
task than a full `a1-5q`/`a1-7q`-style closure since it excludes not only
`k=0` but every `(j,k)` with `gcd(k+1,j)=1`. This would produce a genuinely
new, narrower certified theorem ("`a_1=pq`, `q≡1 (mod p)`: literal
periodicity, unconditionally, no exceptions" for one fixed small `p`) rather
than another symbolic-machinery pass. I did not attempt this closure myself
(out of scope for exploration), but flag it as the one concrete, non-
bookkeeping next move on this file. Otherwise, this approach genuinely looks
like a 3-round plateau on the same wall (round 26 conjecture attempt, round
27 r=1 partial closure, round 28 bookkeeping) — worth deprioritizing next
round in favor of a fresh `a1-Nq` instance (see Job 2) which delivers a
guaranteed new APPROVE at known, bounded cost.

### Job 2: scout for a genuinely new subfamily-theorem candidate

**Tried and REJECTED (confirms prior refutations, does not re-open them):**
- `a_1=6q` (`=2·3·q`): DEVIATES immediately (`n=2`) from the naive `L=6`
  closed form for every tested `q∈{5,...,43}` — because `a_1` is **even**,
  so it is already fully covered (and solved) by the certified `2|a_1`
  family with its own (different, period-2-style) closed form. Not a new
  target; just a special already-solved case, confirmed not worth
  reproposing.
- `a_1=15q` (`=3·5·q`, first genuinely new **three-distinct-odd-prime-factor**
  test): DEVIATES immediately (`n=2`) from the naive `L=15` closed form for
  every tested `q∈{7,...,47}` (12 primes, own greedy simulation). Inspected
  the actual sequence for `q=7`: `[105,108,110,112,114,120,126,130,...]` —
  no simple arithmetic-progression pattern is visible at all; the gaps
  between consecutive terms are irregular (3,2,2,2,6,6,4,2,6,...), unlike
  the clean `+p` steps of the `pq`-family. **This is concrete numeric
  evidence that the 3-distinct-prime-factor family does NOT follow the same
  closable pattern as `a1-pq`** — it looks qualitatively harder (more like
  the general open FAH problem), not a cheap extension. I do not recommend
  pursuing `a_1=q_1q_2q_3`-type families; this is a genuine negative finding,
  not a laziness call.
- Re-confirmed (by re-reading, not re-deriving) that `a1-p²q` was already
  correctly refuted at round 19 (reduces to the same `K_0`-growth-with-`q`
  obstruction that already blocks `a1-3q^m`, `m≥2`, in a different
  parametrization) and that `a1-3qk` for `m=4` was already correctly found
  FALSE at `q=17,k=0` (round 26) — both dead ends, do not re-attempt.

**Viable candidate found (same technique, new instance — not structurally
novel, but concrete and cheap):** continuing the `a1-pq` uniform machinery
to the next uninstantiated prime, `a_1=17q`. I computed `Bad(17)` by direct
greedy simulation (own script, primes `q<2000`, 40 terms each): **`Bad(17)
= {19,23,29,31,37,43,61,67}`** (8 exceptions, all deviating at `n=3,4,` or
`5`, exactly mirroring the `a1-5q/7q/11q` pattern in size and shape — e.g.
`q=19` deviates at `n=3` with `a_3=342=18·19`). This is a legitimate,
concrete, bounded-cost next APPROVE candidate using the already-certified
`p`-uniform machinery (same template as `a1-11q`), independent of whatever
prime the `a1-13q` explorer is covering — `p=17` (or `19`, `23`, ...) is
available as a distinct next target if `a1-13q` doesn't pan out or if the
outliner wants a second parallel `pq`-family build this round.

**Conclusion:** I did not find any structurally different (non-`pq`,
non-`3q^m`, non-`3^a q`) family that shows the same clean closable pattern
under quick numeric probing — every genuinely different structure tried
(even `a_1`, 3-distinct-prime-factor `a_1`) either reduces to an
already-solved family or looks qualitatively harder, not cheaper. The
honest recommendation is: no new structural family this round; if a fresh
`pq`-instance slug is wanted, `a_1=17q` (`Bad(17)={19,23,29,31,37,43,61,67}`,
numerically confirmed) is ready to build.

### Distinct openings
1. On `a1-pq-subfamily-theorem`: carry out the finite `r=1`-restricted
   residual check for one fixed small `p` (e.g. `p=5`) as a genuinely new,
   narrower, non-bookkeeping closure — the only concrete non-repeat move
   identified.
2. A fresh `pq`-instance build, `a_1=17q` (`Bad(17)` numerically pinned down
   above), as a bounded-cost alternative/parallel to `a1-13q`.
3. (Negative, but useful to record) 3-distinct-odd-prime-factor `a_1`
   (e.g. `15q`) is NOT a cheap extension — do not propose it as a shortcut
   family.

### Candidate technique(s)
Same certified `p`-uniform machinery (Generalized `K_0`-Boundedness,
gcd-difference Witness Lemma, Legendre Sieve Gap Bound, Primorial Floor
Bound, Universal Look-Back Witness Identity/closed form) — no new tool
needed for either viable opening.

### Cheap-kill candidates
Parity check (`a_1` even ⟹ already the solved `2|a_1` family, don't
reinvestigate); quick 40-60 term greedy simulation to see if the naive
`a_n=a_1/q·(q+n-1)`-style closed form survives past `n=2` before investing
in symbolic derivation — this killed `15q` in one script run.

### Knowledge-base entries to use
`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`,
`lemmas/universal-look-back-witness-identity.md`,
`lemmas/universal-look-back-closed-form-and-r1-uniqueness.md`,
`lemmas/legendre-sieve-gap-bound.md`, `lemmas/primorial-floor-bound.md`,
`lemmas/diagonal-characterization-and-first-risk-theorem.md` (all already
certified in this workspace; knowledge_base.md's generic sieve/Legendre
entries underlie the certified Legendre Sieve Gap Bound but the reusable
form here is the workspace's own certified lemma files).

### Analogous past problems (cruxes)
Not queried this round — the relevant "prior work" is entirely internal
(the workspace's own certified lemma stack), not the external crux corpus;
a corpus query for "greedy gcd-avoidance sequence periodicity" is unlikely
to surface anything more specific than what's already been mined in past
rounds (per `run_state.md`, this avenue has been exhausted repeatedly).

### Prior progress
See `results/imo-2026-06/approaches/a1-pq-subfamily-theorem.md` — 8th
certified APPROVE overall is `a1-11q`; this file (the `pq`-family machinery
host) stays `partial`, now with two fully proved general lemmas (Universal
Look-Back Closed Form for all `r`, Uniqueness of `r=1`) that narrow but do
not close either residual gap.

### Dead ends (do not retry)
- `a1-p²q`: reduces to the same `K_0`-growth-with-`q` obstruction as
  `a1-3q^m`, `m≥2` — refuted round 19, reconfirmed by re-reading (not
  re-derived this round, no reason to doubt it).
- `a1-3qk`, `m=4`: FALSE at `q=17,k=0` — round 26, do not retry.
- `d=k` and `d=k+1` look-back witnesses for the `r=1` k≥1 residual: both
  fail in general (round 27, independently spot-checked consistent this
  round via the witness-index computation above finding no clean formula).
- `a_1=6q`, `a_1=15q` (this round, new): `6q` is just the already-solved
  even family in disguise; `15q` deviates immediately with no visible simple
  pattern — do not pursue 3-distinct-odd-prime-factor families as a cheap
  `pq`-style extension.

### Small-case / intuition notes (conjectural)
- Conjecture (strengthened numerically this round, not proved): for every
  odd prime `p` and every prime `q≡1 (mod p)`, `a_1=pq` has literal
  `T=1,L=p` periodicity with **no exceptions at all** — zero counterexamples
  found in ~30 fresh `(p,q)` pairs across `p∈{5,7,11,13}`, `q` up to several
  hundred, consistent with round 26's 203-pair and round 27's independent
  sweeps.
- Conjecture (numeric only): `Bad(17)={19,23,29,31,37,43,61,67}` for the
  `a_1=17q` family, `q<2000` — matches the same qualitative shape (small
  deviation indices `n∈{3,4,5}`, exceptions clustered among the smallest
  admissible primes) as every previously certified `Bad(p)`.
