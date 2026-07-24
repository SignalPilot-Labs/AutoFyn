## imo-2026-06 — outline review, round 27

### Independent verification performed (own scripts, not reusing outline/explorer numbers)

**1. `p=7` table (30 cells, `s_0(j,r)=j·r⁻¹ mod 7`, `K_0=7+s_0`).** Recomputed from
scratch with `sympy.mod_inverse`. Diagonal cells (`j=r`) all give `s_0=1` — matches
the certified Diagonal Characterization Lemma exactly.

**2. `Q_1` thresholds and the 29-candidate `k=0` list.** Recomputed `Q_1(7,j,r) =
(7(K_0+1)+j)/s_0` and enumerated primes `q≡r (mod 7)`, `q<Q_1`: **got exactly 29
candidates**, matching the outline/explorer count cell-for-cell (my first pass with a
sloppy `≤` boundary gave 33 — the correct strict `q<Q_1` gives 29, confirming the
outline used the right convention).

**3. `Bad(7)={11,13}` — verified by direct greedy simulation, not just the
gcd-difference witness heuristic.** I wrote my own `a_{n+1}` = smallest legal
successor simulator (matching the problem statement literally) and ran it on
`a_1=7q` for **every prime `q<2000`, `q≠7`**: the sequence deviates from
`a_n=7q+7(n-1)` for **exactly** `q∈{11,13}`, both at `n=3` (`q=11`: `a_3=88` vs
predicted `91`; `q=13`: `a_3=104` vs predicted `105`) — an exact match to the
outline's Step 8 claim, independently confirmed by a different method (full
simulation, not just the abstract witness-search). I also traced why the "27 of 29
candidates resolve, 2 don't" bookkeeping is consistent with this: `q=11` and `q=13`
each appear as a `k=0` candidate in *five* different `j`-bands (since fixing
`r=q mod 7` leaves `j` free), but the actual sequence only deviates once per `q`, at
the band with globally minimal `n_0` (here `j=4,r=4` for `q=11` and `j=6,r=6` for
`q=13`, both diagonal `s_0=1` cells) — the other four bands per `q` are moot once
the true deviation occurs earlier, which is exactly what "diagonal band tested
first" (the certified First-Risk Theorem) predicts. This is a correct picture, not
hand-waving — the outline should make this "only the minimal-`n_0` band matters;
later-band resolutions are a corroborating side-check, not independently
load-bearing" point explicit in the write-up, since a careless reader could
otherwise interpret "27 cells resolve, 2 don't" as 27 independent facts rather than
one underlying deviation-set fact plus redundant corroboration.

**4. `r=1` diagonal-masking logic (`a1-pq-subfamily-theorem` new sub-target).**
Confirmed the algebra is correct and trivial: diagonal means `j≡r (mod p)`; for
`r=1` this needs `j≡1`, but `j` ranges over `{2,...,p-1}`, so no diagonal band
exists — hence `s_0(j,1)=j` directly (no modular inverse needed, since `r⁻¹=1`).
I then ran the actual falsification test the outline proposes (direct greedy
simulation, `a_1=pq`, `q≡1 (mod p)`, for `p∈{5,7,11,13}`, primes `q<3000`): **zero
genuine exceptions found for any `p` in this range** — a clean, non-trivial
empirical corroboration that this sub-case may indeed close with NO exceptional
set at all (stronger than `a1-5q`/`a1-7q`'s nonempty `Bad(p)`). This is exactly
the "cleanest falsification target" the outline claims it is, and my check adds
real weight beyond the outline's own reasoning.

**5. `a_1=11305`/`x_2=103` reapplication.** Recomputed independently: `a_1=11305=
5·7·17·19`; `a_7=11330=2·5·11·103` (not singleton, `F'={11,103}`, matches); `a_4=
11319=3·7³·11` (singleton `{11}` at canonical witness `n_B=4`, matches); `a_103=
12100=2²·5²·11²`, `ρ(103)={2,5}=A'`, singleton `{11}` (matches). Confirmed no
`B'`-occurrence in the window `(4,103]` by direct enumeration (`B'`-occurrence list
starts `4, 119`). All four claims check out exactly — this is a routine, correctly-
scoped reapplication of the certified Finite-Window Literalization Lemma with labels
swapped, and the swap is handled correctly (the outline's own "watch out for" note
on this is warranted and should be kept in the builder's dispatch verbatim).

### Per-approach verdicts

**`a1-7q-subfamily-theorem` — APPROVE (build).** Technique is identical to the
certified `a1-5q` template (same three certified lemmas, `p`-uniform), independently
re-derived by me from scratch and it matches at every checkpoint: the 30-cell
table, the 29-candidate threshold list, and — going beyond the outline's own
witness-based check — a full greedy-simulation confirmation of `Bad(7)={11,13}`
to `q<2000`. No fatal gap. The one open item (`s*=5` inductive proof, step 5) is
correctly flagged as a write-up task, not an obstruction — it mirrors `a1-5q`'s §5
verbatim with different constants, already numerically spot-checked. Ready for a
routine build, same shape as the round-26 `a1-5q` APPROVE.

**`covering-system-construction` (11305 reapplication) — APPROVE (build, capped
scope).** Verified independently; correct application of the certified lemma with
labels swapped for the `n_B<n_A` order. Correctly scoped as a second single-seed
data point, not a general theorem — the outline's explicit warning against
overclaiming here is right and should stay in the builder's brief. Low intrinsic
value (does not move H1 forward, per the explorer's own ceiling assessment) but
cheap, correct, real Elo — worth a build slot if capacity allows.

**`a1-pq-subfamily-theorem` (r=1 sub-target) — APPROVE (build), with an explicit
guardrail.** The diagonal-masking-elimination logic is sound (verified above) and
this is a genuinely narrower, well-motivated target, not a rehash of the stalled
general conjecture. My own falsification sweep (p=5,7,11,13, q<3000) found no
counterexample, consistent with a full closure being achievable. Guardrail (per
CLAUDE.md's rigor rules and the outline's own note): the builder must NOT let a
finite computational sweep stand in for the general symbolic argument — either
give the closed-form `K_0=p+j` sieve argument for ALL `p` (the actual `partial`→
possible-`solved` path), or explicitly report it as `partial`/computational-only if
the symbolic step doesn't close this round. Do not accept "zero exceptions to
q<N" as a substitute for a proof in the final write-up.

**`a1-3qk-subfamily-theorem` (m=4) — CHANGES REQUESTED / low priority, drop from
this round's build set.** No explorer touched this front this round; the outline
itself flags it as "first to drop if capacity is tight." I concur — nothing new to
verify, and the field is better served this round by the three fresher, higher-
confidence targets above. Keep it registered and ranked (still a live, previously-
advanced approach — `m=1,2,3` are certified standalone theorems), just not in this
round's build set.

### Diversity note
The build set is entirely the `pq`/`3q^m`-subfamily-theorem track (mechanical,
certified-machinery instantiations) plus one single-seed covering-system
housekeeping item — there is no live H1/H2-general approach in this round's build
set, because two consecutive dedicated fresh-corridor searches (rounds 26, 27)
found nothing new (confirmed independently unremarkable this round — the
`aimo-0907` analog is correctly diagnosed as dead for the same reason as the
already-dead `orbit-merging-additive-offset-dichotomy`). This is not a new
plateau-of-one-framing problem (the subfamily track and the general-H1 track are
genuinely different framings, and the subfamily track keeps producing real,
verifiable APPROVEs), but the orchestrator should note that if the subfamily track
also plateaus (e.g. once `a1-7q`, `a1-pq` r=1 close), a fresh H1 corridor search
will be needed again with a still-more-different lens than combinatorics/algebra
crux mining (already twice exhausted).

### Ranking
Registered: no new slugs this round (all four discussed approaches were already
registered from prior rounds; the `a1-pq` r=1 sub-target is a revision within the
existing `a1-pq-subfamily-theorem` slug, not a new approach — correctly not
registered separately). No `copy_approach` calls needed — the outline did not
propose branching one approach into two rival paths this round.

`update_ranking` submitted, reflecting this round's evidence: `a1-7q` and
`a1-pq`(r=1) and `covering-system-construction`(11305) each beat the
currently-inert `a1-3qk`(m=4, no fresh content, explicitly deprioritized by the
outline itself); `a1-7q` (near-certain, most thoroughly re-verified this round)
drawn against `covering-system-construction` (both solid, mechanical closures) and
ranked above `a1-pq`(r=1) (still genuinely open, less certain to close this round).

build set: a1-7q-subfamily-theorem, a1-pq-subfamily-theorem, covering-system-construction
