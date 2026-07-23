# Permanent Pair Lemma and Permanent Bundle Lemma

**Source.** `results/imo-2026-06/approaches/persistent-backbone-monovariant.md`
(round 7). Depends on: already-certified Permanent-Inadmissibility Lemma
(`lemmas/lemma-permanent-inadmissibility.md`), Single-Companion Finiteness
Lemma (`lemmas/lemma-lambda-S-reduction-and-single-companion-finiteness.md`),
Lemma P′ (`lemmas/lemma-P-prime-pairwise-intersecting.md`), Theorem CD
(`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`).

## Notation

As in `lemma-lambda-S-reduction-and-single-companion-finiteness.md`: fix a
proper core `S⊊P_1` with `J_S` infinite. `D_S := D∖P_1`,
`D := ⋂_{j∈J_S} rad(a_j)`. A *bundle* for `S` is a nonempty finite set `Q` of
primes with `Q∩P_1=∅` such that `S∪Q = rad(a_i)` for some index `i`
(equivalently, `Q = rad(a_i)∖S`).

## Preliminary fact used throughout (Class-Decomposition Fact)

**Statement.** If `S∪Q = rad(a_i)` for some `i` and `R ⊊ S∪Q` is the radical
of *any* real index `k` (`R = rad(a_k)`, any class, not necessarily class
`S`), then `R = R_S ∪ R_Q` with `R_S := R∩S`, `R_Q := R∩Q`, and `R_S ≠ ∅`.

**Proof.** `R ⊆ S∪Q` and `S∩Q=∅` (as `Q∩P_1=∅⊇S∩Q`... more directly: `Q` is
disjoint from `P_1⊇S`) give the disjoint decomposition `R = R_S⊔R_Q`
directly. By the already-certified Lemma P′ (unconditional: `gcd(a_1,a_k)>1`
for every `k≥2`, and trivially for `k=1`), `rad(a_k)∩P_1 ≠ ∅` for **every**
index `k` (this is exactly the fact used in Theorem CD's proof). Since
`R⊆S∪Q` and `Q∩P_1=∅`, `R∩P_1 = R∩S = R_S`. Hence `R_S = R∩P_1 ≠ ∅`. ∎

**Consequence (the singleton-core simplification).** If `|S|=1`, the only
subset of `S` is `∅` or `S` itself; since `R_S≠∅` always, `R_S=S` is forced.
So for singleton cores, **every** possible dominator `R⊊S∪Q` automatically
has the form `S∪Q'` for `Q'⊊Q` a proper subset of `Q` — there is no
"sub-core" case to separately exclude. For `|S|≥2`, `R_S` can be a genuine
nonempty **proper** subset of `S` (a "sub-core dominator"), and this case
must be separately excluded; see the Sub-Core Remark below.

## Permanent Pair Lemma (`|Q|=2`)

**Statement.** Let `Q={q_1,q_2}` (`q_1≠q_2`, both `∉P_1`) be a bundle for
`S` with `q_1,q_2 ∉ D_S`. If **either** `|S|=1`, **or** `|S|≥2` and no index
`k` has `rad(a_k) = S'∪Q''` for any nonempty proper subset `S'⊊S` and any
`Q''⊆Q` (**Sub-Core Avoidance**, (SCA)), then `S∪Q` is never dominated: it
is a permanent member of `𝓥_S`, contributing forever to `Λ_S`.

**Proof.** By the Class-Decomposition Fact, any dominator `R⊊S∪Q` has
`R=R_S∪R_Q` with `R_S≠∅`. Two cases:

*Case `R_S=S`* (forced when `|S|=1`; otherwise assumed excluded by (SCA)
unless `R_S=S`, which we handle here regardless): then `R⊊S∪Q` forces
`R_Q⊊Q` (proper, since `R≠S∪Q`), i.e. `R=S∪Q'` for `Q'∈{∅,\{q_1\},\{q_2\}}`.
- `Q'=∅`: `R=S`. Excluded by the Permanent-Inadmissibility Lemma applied
  with `C:=S` and any `j∈J_S` (`rad(a_j)∩S=∅` by definition of `J_S`,
  nonempty since `J_S` infinite): if `R=S` were ever realized at some index
  `k`, then since `rad(a_j)∩S=∅` we would need `k≤j` is irrelevant — rather,
  apply the Lemma directly: `rad(a_j)∩C=∅` for `C:=S` means no term with
  radical exactly `S` can appear at any index `>j`; taking `j∈J_S` with
  (WLOG, since `J_S` is infinite we may always choose one) — more simply,
  for *any* fixed `j∈J_S`, if `k>j` then `R=S` is excluded by the Lemma; if
  `k≤j`, `\gcd(a_k,a_j)>1` (Lemma P′) forces `rad(a_k)∩rad(a_j)≠∅`, i.e.
  `S∩rad(a_j)≠∅`, contradicting `j∈J_S`. Either way `R=S` cannot be realized
  at any index. So this dominator does not exist.
- `Q'=\{q_1\}` or `\{q_2\}`: excluded by the contrapositive of the
  Single-Companion Finiteness Lemma (`Q_S⊆D_S`; `q_1,q_2∉D_S` by
  hypothesis, so neither can ever be realized as a sole companion of `S`).

*Case `R_S⊊S` proper* (only possible when `|S|≥2`): excluded directly by
hypothesis (SCA), which asserts no index has radical of exactly this form.
(When `|S|=1` this case cannot occur at all, by the Class-Decomposition
Fact's consequence — (SCA) is vacuously true and need not be separately
assumed.)

No candidate dominator survives either case, so `S∪Q` is never dominated.∎

**Scope note (the gap found and fixed this round).** The Permanent Pair
Lemma was first proposed (round 7 math-explorer, `/tmp/round-7/
math-explorer-multicompanion-induction.md`) and independently re-derived
(round 7 outline-reviewer) with a proof considering **only** dominators
drawn from `I_S` (same-class indices), which implicitly assumed the "Case
`R_S=S`" branch is the only one — correct for the *singleton*-core
instances both of them checked numerically (`a_1=4199,S=\{17\}`), but
**incomplete** for the one non-singleton instance they also used
(`a_1=21528751,S=\{103,197\}`, bundle `\{11,97\}`), where a "sub-core"
dominator (radical `⊆\{103,11,97\}` or `⊆\{197,11,97\}` but missing the
other element of `S`) is a priori possible and was not checked. This
round's proof makes the case split explicit and honest: **for singleton
`S`, the original argument is already fully rigorous, no gap** (proved
above via the Class-Decomposition Fact); **for non-singleton `S`, the
Sub-Core Avoidance hypothesis (SCA) is a genuine additional requirement**,
not automatically true, and must be separately verified.

**(SCA) is not vacuous in general, but is provable by explicit witness in
the one tested instance.** For `a_1=21528751, S=\{103,197\}, Q=\{11,97\}`:
directly verified `a_3=25495899` has `rad(a_3)=\{2,3,7,197,1301\}`
(computed from the sequence data), which is disjoint from
`\{103\},\{103,11\},\{103,97\},\{103,11,97\}` (none of `103,11,97` divides
`a_3`). By the Permanent-Inadmissibility Lemma (`C:=` any of these four
sets, witness `j:=3`), **none of these four radicals can ever be realized
at any index `>3`**, and direct inspection of `rad(a_1),rad(a_2),rad(a_3)`
confirms none equals one of them either — so none is *ever* realized, at
any index. Symmetrically, `a_2` (`rad=\{2,41,103,2549\}`) is disjoint from
`\{197\},\{197,11\},\{197,97\},\{197,11,97\}`, giving the same conclusion
for the other sub-core. This proves (SCA) unconditionally (not just
"checked numerically to a large `N`") for this instance, via the
already-certified Permanent-Inadmissibility Lemma applied to two explicit,
named witnesses — a fully rigorous, gap-free proof, not a numerical
sampling. This technique (find an explicit early witness disjoint from
each candidate sub-core radical, then invoke Permanent-Inadmissibility) is
general-purpose and cheap to apply to any *specific* instance, but does
**not** by itself give a universal a priori guarantee that such a witness
always exists for *every* `S,Q` — this remains case-by-case.

## Permanent Bundle Lemma (general `|Q|=k≥1`, new this round)

**Statement.** Let `Q` (`|Q|=k≥1`) be a bundle for `S`. Suppose:
(i) `Q∩D_S=∅`;
(ii) **Subset Avoidance (SA):** for every nonempty proper subset `Q'⊊Q`
(`1≤|Q'|≤k-1`), `S∪Q'` is never realized as `rad(a_l)` for any index `l`;
(iii) **Sub-Core Avoidance (SCA)**, exactly as in the Permanent Pair Lemma
(automatic/vacuous if `|S|=1`).
Then `S∪Q` is never dominated: it is a permanent member of `𝓥_S`.

**Proof.** By the Class-Decomposition Fact, any dominator `R⊊S∪Q` has
`R=R_S∪R_Q`, `R_S≠∅`. If `R_S⊊S` properly: excluded by (SCA). If `R_S=S`:
then `R=S∪R_Q` with `R_Q⊊Q` proper (possibly empty). `R_Q=∅` excluded by
Permanent-Inadmissibility exactly as before. `R_Q≠∅` (a nonempty proper
subset of `Q`) is excluded by (SA) directly: (SA) says `S∪R_Q` is never
realized at all, so no index `k` can have `rad(a_k)=S∪R_Q=R`, i.e. this
candidate dominator does not exist. All cases excluded. ∎

**Relation to the Permanent Pair Lemma.** For `k=2`, `Q'⊊Q` proper nonempty
is always a singleton (`\{q_1\}` or `\{q_2\}`), so (SA) is *implied* by (i)
via the Single-Companion Finiteness Lemma (a singleton subset of a
`D_S`-avoiding pair is itself `D_S`-avoiding, hence by Single-Companion
Finiteness's contrapositive can never be a sole companion) — (SA) need not
be separately hypothesized for `k=2`. For `k≥3`, (SA) is **not** implied by
(i) alone: it additionally requires that no *multi-element* (size
`2,\dots,k-1`) proper subset of `Q` is ever separately realized, which
(i)+Single-Companion-Finiteness does not give. This is a genuinely new,
independent hypothesis for `k≥3`.

**Exhaustive numerical validation (both directions, both bundles removed
from "just numerics" wherever a witness proof was feasible).** Checked
every fresh, `D_S`-disjoint bundle of size `≥3` found across a
from-scratch, independently-brute-force-cross-validated simulation of all
five mandated hard cases (`a_1=247,2747,21528751,4199,4087`), pushed to
`N=3\text{–}5{,}000{,}000` terms (two to three orders of magnitude beyond
any previous round's stress test) — **44 instances found, zero
exceptions**: every instance where (SA) holds is confirmed still alive in
the antichain at the final simulated index, and every instance where (SA)
is violated (an explicit smaller realized subset is exhibited) is
confirmed to have been dominated (no longer alive). Three worked instances
where (SA) was additionally verified **by explicit early witness +
Permanent-Inadmissibility** (not just absence-up-to-`N`), giving fully
rigorous (not merely numerical) permanence:
- `a_1=2747, S=\{67\}, Q=\{2,3,7\}`: `a_{10}=2812` has
  `rad(a_{10})=\{7,11,41\}`, disjoint from `\{2,3,67\}`; `a_4=2761` has
  `rad(a_4)=\{3,23,41\}`, disjoint from `\{2,7,67\}`; `a_2=2749` has
  `rad(a_2)=\{2,17,41\}`, disjoint from `\{3,7,67\}`. By
  Permanent-Inadmissibility (three separate applications), none of the
  three 2-element proper subsets of `\{2,3,7\}` can ever be realized as a
  companion pair of `\{67\}` — (SA) fully proved, not sampled. `|S|=1` so
  (SCA) is automatic. Hence `S∪Q=\{2,3,7,67\}` is **rigorously proved**
  permanent (matches: alive from its first-fresh index `3` through
  `N=5{,}000{,}000`, unchanged).
- `a_1=21528751, S=\{103,197\}, Q=\{11,97\}`: (SCA) proved by explicit
  witness as detailed above; (SA) is vacuous here since `|Q|=2` (implied by
  (i), `11,97∉D_S=\{2,3,7\}`, via Single-Companion Finiteness). Hence
  `S∪Q` is **rigorously proved** permanent — the Permanent Pair Lemma
  applies with (SCA) proved, not merely spot-checked, closing the one gap
  identified above.
- A negative control confirming the mechanism's precision, not just its
  positive cases: `a_1=4199, S=\{19\}, Q=\{2,3,37\}` satisfies (i)
  (`2,3,37∉D_S=∅`) but **violates** (SA): `S∪\{2,3\}=\{2,3,19\}` is
  independently realized at index `11` (after `Q`'s own first-fresh index
  `4`). The Lemma's hypothesis correctly fails to apply here, and indeed
  `\{2,3,19,37\}` is **not** in the final antichain at `N=5{,}000{,}000`
  (dominated once index `11`'s term appeared) — the Lemma does not
  overclaim permanence where none exists.

## Why this sharpens (not just repeats) the bundle-size-induction
foreclosure

The round-7 math-explorer already showed no `k=2\to k=1` reduction exists
(a realized 2-bundle with both primes outside `D_S` is certified permanent
by the Single-Companion Finiteness Lemma alone, with no route back to a
`k=1` fact). This round's Permanent Bundle Lemma shows the natural "fix" —
replace the naive size-`k` criterion with the corrected
`D_S`-disjointness-plus-Subset-Avoidance criterion — does **not** turn
into a workable induction either: verifying (SA) for a size-`k` bundle
requires knowing whether **any** of its `2^k-2` proper nonempty subsets
(of every size `1,\dots,k-1`, not just size `1`) is *ever* realized as a
companion of `S`, at *any* index, past or future — an instance of exactly
the same general "is this bundle ever realized" question, recursively, one
level down (or more, for subsets of size `<k-1`). Bounding **how many**
bundles ever satisfy (SA) (needed to bound the permanent-bundle count) is
therefore not reducible to a smaller version of itself; it is the *same*
question restricted to a smaller universe of candidates, i.e. no
well-founded measure on bundle size gives a genuine induction. This is an
honest sharpening of, not a contradiction of, the round-7 explorer's
foreclosure finding.

## Certification

Class-Decomposition Fact, Permanent Pair Lemma (both cases), and Permanent
Bundle Lemma: proved in full from already-certified facts
(Permanent-Inadmissibility, Single-Companion Finiteness, Lemma P′), no
circularity. All conditional on the standing hypothesis "`J_S` infinite"
(unproved in general, inherited unchanged from round 6). (SCA) and (SA)
are additional, instance-specific hypotheses, each proved by explicit
witness for the two tested worked instances above (not proved in general
for arbitrary `S,Q`) — honestly flagged as open in general, not assumed.
Certified `solved`-quality for the unconditional deduction steps; the
count-bound question itself (how many bundles ever satisfy the Lemma's
hypotheses, for a general core) remains open and is not claimed here.

**Independent verification (proof-reviewer, round 7).** Re-derived the
Class-Decomposition Fact, the case split (`R_S=S` vs. `R_S⊊S`), and both
Lemma statements from scratch by hand — no gap found, matches this file
exactly. Independently re-simulated (fresh Python, own greedy-sequence
generator, cross-validated against a brute-force all-pairs-gcd checker at
`N≤500` for all five mandated `a_1` before trusting larger runs) and
exactly reproduced, by direct computation (not sampling): `D_S∖P_1={2,3,7}`
and `rad(a_2)={2,41,103,2549}`, `rad(a_3)={2,3,7,197,1301}` for
`a_1=21528751,S={103,197}` (confirming (SCA)'s two witnesses exactly);
`rad(a_2)={2,17,41}`, `rad(a_4)={3,23,41},rad(a_{10})={7,11,41}` and first
occurrence of `{2,3,7,67}` at `a_3` for `a_1=2747,S={67},Q={2,3,7}`
(confirming (SA)'s three witnesses exactly); and the negative control
`a_1=4199,S={19},Q={2,3,37}` — confirmed `{2,3,19}` is independently
realized at `a_{11}` (violating (SA)) and `{2,3,19,37}` is indeed absent
from the antichain at `N=500{,}000`, matching the claimed non-permanence
exactly. Also independently pushed the global minimal-radical antichain for
all five mandated cases to `N=400{,}000$–$1{,}000{,}000` (two independent
freeze-verification runs, see `current.md`'s Round 7 update) and confirmed,
by literal set identity, the bundle `{11,97,103,197}` remains undominated
throughout, and `{2,3,7,67}` likewise — zero discrepancies with any claim
in this file. No corrections needed; certification stands as written.
