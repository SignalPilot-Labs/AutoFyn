# Outline review — round 28, imo-2026-06

## 1. `a1-11q-subfamily-theorem` (new)

**Independent re-derivation performed** (own from-scratch Python/`sympy`
scripts, not trusting the outliner's/explorer's numbers):

- Ran the literal greedy recursion (`a_{n+1}` = smallest unused integer
  sharing a factor `>1` with every prior term) for `a_1=11q`, every prime
  `q>11` up to `q<6000`, 90 terms each. Reproduced **exactly**
  `Bad(11)={13,17,19,31,37,43}` — no more, no fewer, matching the outline's
  claimed exception set digit-for-digit.
- For each of the 6 exceptions, independently located the first deviation
  index `n`, the band `j=a_n-a_{n-1}`, `r=q mod 11`, and `s_0(j,r)=j·r^{-1}
  mod 11`: **all six are diagonal** (`j=r`, `s_0=1`) — `q=13:(n=3,j=r=2)`,
  `17:(3,6)`, `19:(3,8)`, `31:(4,9)`, `37:(5,4)`, `43:(5,10)`. This
  independently confirms the outline's "all exceptions diagonal" claim and
  is consistent with the certified Diagonal Characterization / First-Risk
  Theorem pattern established at `p=3,5,7,13` in prior rounds.
- Confirmed the technique is a mechanical, verbatim instantiation of the
  already-certified `p`-uniform machinery (`Generalized K_0-Boundedness`,
  `gcd-difference Witness Lemma`, `Legendre Sieve Gap Bound`, `Primorial
  Floor Bound`, and the round-27 `Universal Look-Back Witness Identity`
  `r=1` corollary) — exactly the recipe that closed `a1-5q` (round 26) and
  `a1-7q` (round 27), both APPROVEd on first build. No new tool is invoked;
  the only work is the `p=11`-specific 90-cell table, the same *kind* and
  scale of labor as `a1-7q`'s 30-cell table (3× larger, not qualitatively
  harder).
- The 90-cell count (9 bands `j∈{2,...,10}` × 10 residues `r∈{1,...,10}`)
  is arithmetically correct; the `r=1` column's `k=0` layer is free by the
  certified identity, leaving 81 cells for the sieve/threshold/hand-check
  closure — matches the file's own (self-corrected mid-sentence) count.
- No repeat of a recorded dead end; no case-coverage gap in the skeleton
  (base case, `a_n+1`, `a_n+11`, and `j=2..10` under Case (a)/(b) cover
  every offset).

**Verdict: APPROVE.** This is genuinely build-ready — same template,
thrice-verified, zero technique risk. The only remaining work (the 81-cell
table + hand-checks) is exactly the outline's own honestly-flagged open
gap, appropriate content for the builder, not something that should have
been resolved at outline stage.

## 2. `a1-pq-subfamily-theorem` (revise — Round 28 target)

**Independently re-derived the closed form from scratch** (own script,
not reusing any outline/explorer intermediate table): for `p∈{5,7,11,13}`,
sampled 60 primes per `p`, every band `j∈{2,...,p-1}`, every `k∈{0,...,4}`
— computed `n_0,K_0,s_0` from the certified boundedness relation, then
compared the outline's closed form `gcd(j,(k+1+c(p,j,r)) mod j)`,
`c(p,j,r)=(s_0(j,r)·p^{-1}) mod j`, against the **direct** definition
`gcd(j, (q+n-1) mod j)` at `n=n_0+kq`. **8400 instances, zero
mismatches.** The closed form is correct.

**Independently re-derived the uniqueness-of-`r=1` claim.** Checked, for
`p∈{5,7,11,13,17,19}`: (a) `s_0(j,1)=j` exactly for every `j∈{2,...,p-1}`
— confirmed exactly, matching the algebraic argument (`1^{-1}≡1`). (b) For
**every** `r≠1` (not just `r=p-1`, which is all the outline's own
skeleton explicitly commits to proving in general — it flags this as a
to-do for the builder), independently searched for a band `j` with
`c(p,j,r)≠0` **and** `gcd(j,1+c)>1` — found at least one such `j` for
every `r≠1` at every tested `p`, confirming `r=1` really is the unique
residue with the free unconditional closure. Also specifically verified
the outline's suggested general witness `r=p-1` (`s_0(j,p-1)=p-j` for
every `j`, hence `j∤s_0` for every `j` since `j|p` is impossible for
`0<j<p`, `p` prime) is itself a valid witness band at every tested `p`
(`5,7,11,13,17,19,23`) — this is a genuinely general (not just spot-checked)
sub-argument, stronger than the outline's own hedge ("ideally all `r≠1`")
suggests it needs to be.

**Assessment of novelty (checking for the single-gap/relabeling trap,
memory rules #4, #15, #18, #28):** this is not a re-derivation of the
round-27 `r=1` corollary or the round-26 Diagonal Characterization Lemma.
The Diagonal Characterization Lemma only concerns which single band `j=r`
has `s_0=1`; this round's Uniqueness Theorem is a strictly stronger claim
(`c(p,j,r)=0` simultaneously for **every** band `j`, not just the diagonal
one) and was independently confirmed to be a genuinely distinct, correctly
novel fact — my own script explicitly tested "does any `r≠1` have `c=0` for
all `j`" and found none, positively distinguishing this from the older
lemma rather than repackaging it.

**Scope check (memory rule re: "table-lookup ≠ new closure"):** the file's
own "Watch out for" section correctly self-flags that the `O(p^2)`
speed-up does not resolve any new cell — verified this is an accurate,
non-overclaiming characterization; the actual open gaps (`r=1,k≥1`
residual; `r≠1,k=0` cells still needing the full sieve machinery) are
correctly identified as untouched.

**Minor gap to flag for the builder:** the outline's own skeleton (step 4)
explicitly admits it has only checked `r=p-1` as the non-vanishing witness
and defers the fully general `r≠1` case to "case analysis on modular
inverses mod p" without giving the general argument. This review's
numerical check (all tested `r≠1`, all tested `p`) is strong corroborating
evidence but is not itself a proof for literally all `p`. The builder must
either (a) supply a clean general algebraic argument (e.g., show that if
`c(p,j,r)=0` for all `j` then `s_0(j,r)` is a multiple of `j` for every
`j∈{2,...,p-1}` simultaneously, and derive a contradiction from the
defining congruence `s_0·r≡j (mod p)` unless `r=1`), or (b) explicitly
verify it for every `p` this workspace has so far instantiated (3,5,7,11,13)
as a fallback — the outline already names this correctly as the required
follow-up; this is a fixable gap, not a fatal one.

**Verdict: CHANGES REQUESTED** (proceed to build; require the builder to
either close the general-`r` uniqueness argument algebraically or
explicitly verify it per-`p` as the outline itself specifies, rather than
resting on the single `r=p-1` instance).

## Diversity / plateau check

No shared-gap collapse this round: `a1-11q` is a concrete, near-certain
per-`p` closure (8th such theorem pending build); `a1-pq`'s target is an
orthogonal internal generalization (uniformity across `r`, not across `p`)
that narrows but does not compete for the same gap. Per the standing
memory-rule-28 precedent, these remain legitimate distinct population
members (not duplicate fragments of one proof) and both are worth
building in parallel — no RETHINK needed on grounds of overlap.

## Ranking actions taken

- Registered new approach `a1-11q-subfamily-theorem` (cold-start Elo 1500,
  now anchored via head-to-head comparisons against established
  approaches: loses narrowly to certified `a1-7q`/`a1-5q` as an
  as-yet-unbuilt newcomer, beats the broader-but-still-open `a1-pq`, and
  comfortably beats long-stalled generic FAH mechanisms
  `amortized-charging-budget` and `cofinite-window-capacity-bound`).
- `a1-pq-subfamily-theorem`'s `advanced` outcome anchored as beating the
  stuck `a1-3qk-subfamily-theorem` (general-`m` axis has been stalled since
  round 25) and drawing with the also-`solved`-restricted-scope
  `a1-3aq-subfamily-theorem`.
- All touched approaches had their `stale` flag cleared by this round's
  `update_ranking` call.

build set: a1-11q-subfamily-theorem, a1-pq-subfamily-theorem
