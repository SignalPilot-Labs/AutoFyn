## imo-2026-06

**Population-level correction (applies to all approaches below):** round-3
exploration (`/tmp/round-3/math-explorer-backbone-conjecture.md`) found
strong numerical evidence that `(\star\star)` — the canonical witness set `W`
itself finite — is **FALSE** (`|W|` grows past 21 distinct primes with no
plateau for `a_1=4199`, similarly unbounded for `a_1=4087`). This sharpens
NC1/NC2 from "no simple closed form for `W`" to "do not let any argument
secretly assume `W` finite." The correctly-scoped, well-supported target for
every "Gap 1" approach remains the strictly weaker **Finite Covering Backbone
Conjecture (FCBC)**: exists finite `H` with `H\cap\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\ne\varnothing` for every `i<j`, which (per the
reviewer-generalized `theorem-2.2-H-hitting-characterization.md`) is already
sufficient, on its own, to invoke the certified Theorem 2.2 + Lemma 2.3 +
Theorem 2.4 chain for conditional eventual periodicity — `W` finiteness is
not needed. FCBC passed every stress test this round (24 diverse `a_1`
values, up to 20,000 terms / `~2\times10^8` pairs), including on the two
`W`-unbounded cases.

---

persistent-backbone-monovariant: revise
Target: there exist `T,L` with `a_{n+T}=a_n+L` for every `n\ge1` (whole
problem). Case I (single saturating prime) fully solved via imported Lemma
Q/Lemma S′; this approach addresses Case II via FCBC.
Technique: inductive-invariant / growth-rate reduction — reduce FCBC to
boundedness of `\omega(a_n)` (number of distinct prime factors), a sharper,
more concrete target than the previous `O(\log n)` dominant-prime bound.
Skeleton:
  1. Import Lemma P, P′, Q, S′, Proposition D, Lemma C, NC1, NC2, Domination
     Lemma, Lemma 1 (all certified, no re-proof).
  2. Certify a small algebra lemma: since `a_n/n\to L` (Lemma 1, a genuine
     constant, not growing), all `O(\log n)` growth in the dominant-prime
     bound `q^*\le r\cdot a_n/n` (`r=\omega(a_{n+1})`) comes from `r` alone —
     so `\omega(a_n)\le M` (constant) `\Rightarrow` `q^*(n)\le M(a_1+L)` for
     every `n`, a uniform bound.
  3. Attempt the hard sub-target: `\omega(a_n)=O(1)`, via an inductive
     invariant (not density/counting) — minimality of the greedy rule in a
     window of length `\le L` forces reuse of a few already-recruited primes
     rather than many one-off small ones. Numerically supported (`\le6`-`7`
     over 40,000 terms on the hardest case `a_1=247`) but not proved.
Key lemmas (claim + mechanism):
  - `\omega`-bound lemma — `\omega(a_n)\le M\Rightarrow` dominant prime
    uniformly bounded, because `a_n/n\to L` isolates all growth into
    `\omega(a_{n+1})` (already-certified algebra, three lines).
  - `\omega(a_n)=O(1)` (open) — because the greedy rule's minimality in a
    bounded window structurally favors reusing high-density primes over
    introducing new ones (mechanism sketched, not proved).
Open gaps: `\omega(a_n)=O(1)` itself; also (separate, flagged) that even a
finite set of ever-dominant primes must be shown *sufficient* as an FCBC
covering set, not just necessary.
Cases to cover: Case I solved (imported); Case II is this approach's target.
Watch out for: `\omega(a_n)=O(\log\log n)` (Hardy-Ramanujan-typical, still
unbounded but very slow) is a live alternative the numerics don't yet rule
out — do not silently accept "grows slowly" as "bounded."

forced-primes-well-ordering: new (copy-of persistent-backbone-monovariant, distinct technique for the same target — two viable ways to fill the FCBC gap)
Target: same as above (whole problem, via FCBC in Case II).
Technique: well-ordering / minimal-counterexample on an explicit "forced
primes" invariant `F`, via Domination-Lemma tension — distinct from the
sibling's inductive-invariant technique (per round-3 explorer opening 1,
strongly numerically supported: `F_M` stabilizes by index `\le12` across 24
diverse `a_1` values, never grows again).
Skeleton:
  1. Import same lemma set as above.
  2. Define `F_M:=\{p:\exists i<j\le M,\ \mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)=\{p\}\}`
     (unique common factor of some pair); `F:=\bigcup_M F_M` (monotone union).
  3. Lemma FN (necessity, cheap): every valid covering `H` contains `F`,
     because a singleton-intersection pair has no other candidate witness.
  4. Lemma FF (open, hard): `F` is finite. Mechanism: well-order `F` by
     first-forced index `m(p)`; if `F` infinite, extract an infinite strictly
     increasing sequence of newly-forced, distinct primes `p_k`; seek a
     contradiction from tension with the Domination Lemma (each `p_k` is a
     "single-use" recruit, numerically correlated with but not proved to
     force `\omega`-growth along the subsequence).
  5. Separate open sub-gap: even if `F` finite, must separately show `F` (or
     a bounded augmentation) actually *covers* every pair (sufficiency),
     not just the singleton-intersection pairs used to define it — do not
     conflate with Lemma FF.
Key lemmas: Lemma FN (necessity, proved by the covering definition itself);
Lemma FF (finiteness of `F`, open, well-ordering + Domination-Lemma tension
sketched but not completed).
Open gaps: Lemma FF itself; the sufficiency step (5) is logically
independent and also open.
Cases to cover: Case I solved (imported); Case II is the target.
Watch out for: do not assume `\omega(a_{j_k})\to\infty` along the forced-index
subsequence without proof — this is exactly the missing link.

explicit-window-backbone-construction: new
Target: same as above (whole problem, via FCBC in Case II).
Technique: direct explicit construction (`H_K:=\bigcup_{i\le K}\mathrm{rad}(a_i)`
for a fixed window `K`) plus a structural pigeonhole reduction — a third,
constructive (not growth-rate, not contradiction-based) technique for the
same target. Round-3 numerics: zero failures for `K\in[10,15]` across
thousands to tens of thousands of terms, including the two `W`-unbounded
adversarial cases `a_1=4199,4087`.
Skeleton:
  1. Import same lemma set.
  2. Fix `K\ge1`, `H_K:=\bigcup_{i=1}^K\mathrm{rad}(a_i)`.
  3. (Free, via Lemma P) every term meets `H_K`, since `\mathrm{rad}(a_1)
     \subseteq H_K` and Lemma P gives `\gcd(a_j,a_1)>1` for `j\ge2`.
  4. (Free, pigeonhole) since each signature `\sigma_K(j):=\mathrm{rad}(a_j)
     \cap H_K` is a nonempty subset of the fixed finite `H_K`, at most
     `2^{|H_K|}-1` distinct signature values are ever realized, for any `n`.
  5. Key open Lemma: for some finite `K=K(a_1)` (conjecturally bounded by a
     function of `\omega(a_1)` alone, empirically `\le12`), every two
     realized signature values intersect — equivalently `H_K` satisfies the
     full FCBC covering property. This does NOT follow from Lemma P′ alone
     (which only guarantees a common prime in the *full* radicals, not
     inside the smaller `H_K` window — exactly why NC1/NC2 refuted simpler
     candidates). Mechanism to attempt: a second Lemma-C-style finite-descent
     argument on the cumulative set of realized signature values (analogous
     to Lemma 2.3's `\Sigma_n` stabilization), plus a further argument ruling
     out ever-disjoint realized values or bounding `K` explicitly by
     `\omega(a_1)`.
Key lemmas: step 3 (free, Lemma P corollary); step 4 (free, pigeonhole);
step 5 (open — the approach's entire remaining content).
Open gaps: step 5's Key Lemma in full.
Cases to cover: Case I solved (imported); Case II is the target.
Watch out for: "finitely many signature values realized" (free) is not the
same claim as "realized values pairwise intersect" (open) — do not conflate.
The `K\le12` bound is purely empirical; report any proof honestly as
"finite but not shown uniform" if a clean bound isn't found.

intersecting-family-covering-construction: revise
Target: same whole-problem claim, this approach's job is Gap 2 (periodicity
from `n=1`, not just eventually) — conditional on `(\dagger')`, a finite
covering `H` supplied by one of the three sibling approaches above.
Technique: strong induction (coincidence lemma) + an adapted permutation/
injectivity argument (crux `aimo-0577`) — two sequential, logically
independent steps within one proof architecture (not split across slugs,
since both are necessary parts of the same route to periodicity-from-1).
Round-3 finding: round 2's negative result used the WRONG covering set
(`\mathrm{rad}(a_1)`, guessed); using the TRUE covering set, both steps hold
with zero exceptions across 7 examples (`a_1=15,35,65,105,143,221,1001`).
Skeleton:
  1. Import Theorem 2.2, Lemma 2.3, Theorem 2.4 unchanged (certified,
     already generalized to any covering `H`).
  2. Obstruction 1 (coincidence lemma): prove `\min\{x>a_n:x\text{ hits
     }\Sigma_n\}=\min\{x>a_n:x\text{ hits }\Sigma_\infty\}` for **every**
     `n\ge1`, via strong induction using Lemma 1's gap bound plus a
     divisibility/density argument (constraints in the narrow window
     `(a_n,a_n+L]` tend to force the fuller constraint set too, since `L` is
     a bounded lcm) — not yet a proof, numerically confirmed (60/60 checks).
  3. Obstruction 2 (no pre-period): adapt `aimo-0577`'s technique — show the
     transition map `G:\mathbb Z/L\mathbb Z\to\mathbb Z/L\mathbb Z` is
     injective on the reachable orbit (no closed-form inverse available
     here, unlike `aimo-0577`; needs an adapted argument, e.g. minimality of
     the greedy rule forces distinct histories to have distinct residues).
     If injective, a permutation's forward orbit is periodic with zero
     pre-period, for free.
  4. Combine 2+3 with Theorem 2.4's pigeonhole run from `n=1` directly:
     `a_{n+T}=a_n+L_{\mathrm{per}}` for every `n\ge1`, conditional only on
     `(\dagger')`.
Key lemmas: coincidence lemma (open, mechanism: strong induction + window
density); injectivity of `G` (open, mechanism: adapted `aimo-0577`
permutation argument, no ready-made inverse).
Open gaps: both steps 2 and 3 — genuinely independent, both required; do not
claim Gap 2 closed from only one.
Cases to cover: Case I solved (imported, unconditional, no Gap-2 issue since
Lemma S′ already gives periodicity from `n=1` directly for Case I). Case II
is the target, conditional on `(\dagger')`.
Watch out for: obstruction 1 and obstruction 2 were tested independently in
round-3 numerics and both held on the same 7 examples, but closing one does
not imply the other — a builder must not skip either.

---

**Parked, not part of this round's build set** (per dispatch): `backbone-
existence-crt` (RETHINK on Step 3 only, round 1) — its original `H_n`/`(\star)`
targets are both refuted; its content (Lemma P, P′, Q, Domination Lemma) is
already imported by all four active approaches above, so no unique value is
lost by leaving it parked this round. `bounded-gap-density-covering` — Lemma
1 (imported everywhere above) is its only reusable content; its Step 3
strategy remains a confirmed dead end, not revived.

**Field summary for the outline-reviewer**: 4 approaches, all live, all
building on the same certified lemma cache (Lemma P/P′/Q/S′/C/R, Domination
Lemma, Lemma 1, Theorem 2.2/2.3/2.4 — all imported unchanged, no
re-derivation needed). Three attack Gap 1 (FCBC) via three genuinely
different techniques (inductive-invariant, well-ordering/contradiction,
explicit construction) — `persistent-backbone-monovariant` (revise),
`forced-primes-well-ordering` (new), `explicit-window-backbone-construction`
(new). One attacks Gap 2 (periodicity-from-`n=1`) conditionally —
`intersecting-family-covering-construction` (revise), newly reopened as
tractable by corrected round-3 numerics, with two required sub-steps
(coincidence lemma + injectivity) kept in one file since they are
complementary, not alternative, routes. Build set recommendation: all four
(each is a complete, non-overlapping unit of open work; none share a single
gap in a way that would make them die together — three independent mechanisms for
Gap 1, one for Gap 2).
