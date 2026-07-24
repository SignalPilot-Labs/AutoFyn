# Round 25 proof-reviewer report — imo-2026-06

Reviewed all 3 built approaches independently, from scratch (own Python/sympy
scripts, distinct from every builder's), per the adversarial protocol.

## 1. `a1-3qk-subfamily-theorem` (m=3 closure)

**Verdict: CHANGES REQUESTED. Status: partial (correctly self-reported).**

Claim: `a_1=3q^3` literal `T=1,L=3` periodicity for every prime `q≥7,q≠5`,
via a threshold-derivation template mirroring the certified `m=1,2` cases
(`r_0=15` for the `k=0` band via a sharpened Primorial-Floor-Bound
induction, `(r+1)!≥g(r):=27·4^r(r+1)^2+36·2^r(r+1)+14` for `r≥15`; a new
"OR-split" device for the `k≥1` band via a second induction,
`(s+1)!≥h(s):=3B(s)^2+(3/7)B(s)+2` for `s≥14`, `B(s):=2^{s+1}(s+2)`), with
26 total residual exceptions (12 at `k=0`, 14 at `k≥1`), each resolved by an
explicit witness.

Independent re-derivation, own scripts:
- Reproduced the exact 12-instance `k=0` exception list
  (`q∈{11,17,19,23,29,41,53,59,61,71,89,479}`) digit-for-digit, and
  extended the exhaustive scan well past the builder's own range to
  `q<60,000` — zero further exceptions, consistent with the proved
  `q≥737,282` threshold.
- Reproduced the exact 14-instance `k≥1` exception list
  (`(q,k)∈{(7,1),(7,2),(7,3),(7,7),(11,2),(13,3),(17,1),(17,2),(17,4),
  (19,1),(23,1),(29,2),(59,2),(71,2)}`) over the full analytically-proved
  finite region `kq<245,760`, exact match.
- Verified all 26 explicit witnesses (`t_i=q^3+i-1` vs `K_0` or `M=qK`) by
  direct `gcd` computation — every one correct.
- Independently re-derived both Primorial-Floor-Bound inductions from
  scratch: base cases `16!≥g(15)` (`20,922,789,888,000 ≥ 7,421,722,361,870`,
  confirmed) and `15!≥h(14)` (correctly computed `h(14)=824,633,945,528.86`,
  `15!=1,307,674,368,000`, confirmed) both hold; confirmed no induction-step
  failure across `r,s∈{4,...,39}` by direct sympy computation.
- **Found one minor write-up error, not load-bearing**: the file states
  `h(14)=1,241,245,707,702`, which is wrong (correct value per the file's
  own formula is `824,633,945,528.86`). Both the correct and the
  mis-stated numbers are `<15!`, so the base case's truth (and hence the
  whole induction and the theorem) is unaffected — a pure arithmetic slip
  in the displayed intermediate number, analogous to the round-21
  precedent of a minor slip that didn't change the conclusion.
- Independently re-simulated the literal greedy recursion (own fresh
  script, the actual "smallest legal integer" rule, not the closed form)
  for 13 primes `q∈{7,...,89}` out to 60-400 terms each (covering every
  exceptional index): zero mismatches.

**No load-bearing gap found.** This is a genuine, complete, gap-free third
instance of the `a_1=3q^m` family (`m=1,2,3` all now fully certified).
Certified as `lemmas/a1-3q-cubed-periodicity-theorem.md`.

**Status/verdict reasoning**: the theorem itself is solved-quality, but per
the exact precedent this same file set one round earlier for `m=2` (Status
stayed `partial`, verdict CHANGES REQUESTED, even though `m=2` was fully
certified, because the approach's own declared target is the general-`m`
family and `m≥3` was still open), the correct call here is again CHANGES
REQUESTED / Status `partial`: `m≥4` remains open, and the file's own "Open
gap" section honestly identifies two genuine per-`m` obstacles (growing
threshold constants; an `m`-specific OR-split re-derivation) not yet closed
for general `m`. The dispatch note's suggestion to treat this as
"APPROVE-class" for the narrow `m=3` claim is honored via full lemma
certification, but flipping the *approach's* own Status to `solved` would
contradict the precedent this exact file established last round and would
misrepresent the file's own stated (general-`m`) scope.

## 2. `a1-pq-subfamily-theorem` (uniform-in-p reduction)

**Verdict: CHANGES REQUESTED. Status: partial (correctly self-reported).**

Claim: a `p`-uniform symbolic reduction (no per-`p` constant refitting) of
the certified `a1-3q` argument to `a_1=pq` for any fixed odd prime `p`,
proving literal `T=1,L=p` periodicity outside a finite `Bad(p)`, but NOT
pinning down `Bad(p)` explicitly for any `p≥5` (only a `p=3` consistency
check against the already-certified `a1-3q` theorem).

Independent re-derivation:
- Re-derived the Generalized gcd-difference Witness Lemma
  (`\gcd(N,a_n)=\gcd(N,j)` via `\gcd(x,y)=\gcd(x,x-y)`) — correct, one line.
- Re-derived the Generalized `K_0`-Boundedness Lemma
  (`K_0(j,r)=p+s_0(j,r)`, `s_0(j,r)\in\{1,...,p-1\}` the unique solution of
  `s_0 r\equiv j\pmod p`, independent of `q`'s magnitude) from the modular
  bijection argument — correct.
- Independently computed the full symbolic table for `p=5` (all 12
  `(j,r)` pairs) via `sympy.mod_inverse`, then independently cross-checked
  every entry against a from-scratch brute-force search (own script,
  distinct method: for an explicit smallest prime `q` in each residue
  class, directly searched for the least Case-(b) index `n_0` and computed
  `K_0=(a_{n_0}+j)/q`) — **exact match on all 12 entries**.
- Independently reconfirmed the `p=3` specialization reproduces the
  certified `a1-3q` theorem's exact constants (`K_0∈{4,5}`,
  `n_0=(q+1)/3,(2q+1)/3`).

**No gap found in either lemma.** Certified as
`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`. The
approach's own honest scope statement — that pinning down the literal
`Bad(p)` for `p≥5` requires an intrinsic per-`p` finite computation not
carried out here — is confirmed accurate; this is a real, structural gap
(the same phenomenon that required hand-discovery of `q=5` even at `p=3`),
correctly diagnosed, not a laziness gap. Status `partial` is correct.

## 3. `n1-periodicity-reconciliation` (H2 seed-asymmetry reconciliation)

**Verdict: CHANGES REQUESTED. Status: partial (correctly self-reported).**

Claim: corrects round 24's H2-threatening framing that `a_1=11305`'s
new-extended-type arrival rate "stays flat `~sqrt(N)`" — a larger,
methodologically-corrected (local-exponent, not global-fit) re-simulation
shows both canonical hard seeds (`4807`, `11305`) decelerate, `11305` just
more slowly; explicitly not claimed as evidence for/against H2.

**Verification note (partial-confidence, disclosed):** this review
attempted to independently reproduce the round-25 math-explorer's
large-scale (`~750k`-`1M`-term) `S_0`-restricted extended-type-count
simulation underlying this section, but found doing so correctly requires
first independently recomputing each seed's `S_0` (the Finite-Core-Theorem
enlarged core), itself a nontrivial multi-step absorption computation — not
completed within this review's time budget. A lighter raw-factorization
proxy was tried and found to measure a qualitatively different, much
larger, and non-comparable quantity (near-linear growth, ~35% of terms
already distinct raw types by `n=30,000` — nothing like the file's reported
`132-806`-type counts), so it was correctly discarded rather than used to
draw any conclusion. Consequently this review did **not** fully
independently re-derive this round's specific large-`N` numeric claims —
a genuine limitation of this review, flagged explicitly (unlike the other
two slugs, which were fully re-derived).

What **was** verified: the file's internal logic is sound (the local-exponent
formula `p_local=log(T2/T1)/log(N2/N1)` correctly measures per-interval
growth rate, correctly diagnosed as immune to the early-transient
contamination that biases a single global power-law fit), and the file's
own honesty caveats (§10, "what this section does NOT claim": no bound on
`(N(S_k))_k` follows from simulation; no new H2 mechanism proposed; the
seed's future trajectory past the simulated range is genuinely undetermined)
are accurate and non-overclaiming — this is purely diagnostic documentation,
correctly scoped, matching the workspace's established "diagnostic, not
certified lemma" precedent (no lemma file proposed or certified here).

**Status `partial` is correct** — no proof content on H1 or H2, a genuine
correction of a prior round's numeric framing, H1/H2 both remain fully open.

## Lemmas certified this round

1. `lemmas/a1-3q-cubed-periodicity-theorem.md` — `a_1=3q^3` literal
   periodicity theorem (5th distinct-`m`/family theorem in the workspace's
   floor-deliverable stack).
2. `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md` —
   `p`-uniform `K_0`-boundedness and gcd-difference witness lemmas for the
   `a_1=pq` family.

## current.md

Updated `results/imo-2026-06/current.md` (`## Status` header and a new
round-25 dated entry) to record all three verdicts, the two new certified
lemmas, and the workspace-level `partial` status (H1/FAH now at its 19th
consecutive plateau round, H2 still fully open).

## Summary of routing

- `a1-3qk-subfamily-theorem`: CHANGES REQUESTED (partial) — `m=3` closed
  and certified as a standalone theorem; general `m` still open.
- `a1-pq-subfamily-theorem`: CHANGES REQUESTED (partial) — uniform machinery
  proved and certified; `Bad(p)` for `p≥5` still open.
- `n1-periodicity-reconciliation`: CHANGES REQUESTED (partial) — honest
  diagnostic correction; H1/H2 untouched; this review's own numeric
  verification of this slug is partial-confidence (see note above).

No RETHINK verdicts this round; no APPROVE verdicts this round (workspace
overall Status stays `partial`).
