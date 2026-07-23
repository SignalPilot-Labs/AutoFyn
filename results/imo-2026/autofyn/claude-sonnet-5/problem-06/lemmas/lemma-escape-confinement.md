# Escape-Confinement Lemma

**Source.** `results/imo-2026-06/approaches/forced-primes-well-ordering.md`
(round 7, §G, Step 1). Depends only on the already-certified Lemma P′
(`lemmas/lemma-P-prime-pairwise-intersecting.md`) and the already-certified
Companion-Disjointness Coarsening Lemma's notation
(`lemmas/lemma-companion-disjointness-coarsening.md`).

## Setup (notation)

Fix a proper nonempty core `S⊊P_1` with `I_S≠∅`. For any index `j`, write
`comp(a_j):=rad(a_j)∖P_1`. A *bare value* `κ=S∪Q` (`Q` a finite set of primes
disjoint from `P_1`) is **blocked** by witness `j_3` if `rad(a_{j_3})∩κ=∅`
(then, by the already-certified Permanent-Inadmissibility Lemma, `κ` can
never be realized exactly at any index `>j_3`). An **escape** from a blocked
`κ` is an index `i∈I_S` with `rad(a_i)⊋κ` (a realized radical of class `S`
that properly contains the blocked bare value).

## Statement

Let `κ=S∪Q` be blocked by witness `j_3`. Then for **every** escape `i`
(`i∈I_S`, `rad(a_i)⊋κ`), there exists a prime `p∈comp(a_{j_3})` with
`p∈rad(a_i)`.

## Proof

By the already-certified Lemma P′ (unconditional, holds for every pair of
indices of the whole infinite sequence), `rad(a_i)∩rad(a_{j_3})≠∅`. Since
`i∈I_S`, `rad(a_i)∩P_1=S`. Since `S⊆κ` and `κ∩rad(a_{j_3})=∅` (the blocking
hypothesis), `S∩rad(a_{j_3})=∅`. Hence the nonempty intersection
`rad(a_i)∩rad(a_{j_3})` cannot be witnessed by any element of
`S=rad(a_i)∩P_1`; it must come from `comp(a_i):=rad(a_i)∖P_1`. So there is
`p∈comp(a_i)∩rad(a_{j_3})`. Since `p∉P_1`, `p∈rad(a_{j_3})∖P_1=comp(a_{j_3})`,
as claimed. ∎

## Iterated form (immediate corollary, not a new proof)

If `κ'=κ∪{p}` (for `p` as furnished by the Lemma) is itself blocked by some
witness `j_3'`, the Lemma applies again verbatim with `κ'` in place of `κ`
(nothing in the proof used any property of `κ` beyond `κ⊇S` and
`κ∩rad(a_{j_3})=∅`, both of which persist under the substitution). This
defines an escape-recursion `κ=κ_0⊊κ_1⊊⋯`, each obtained from the last by
adjoining one confinement prime.

## Independent verification (proof-reviewer, round 7)

Re-derived from scratch (matches the source's proof exactly, no gap found).
Independently re-simulated (fresh Python, own greedy-sequence generator,
cross-validated against a brute-force all-pairs-gcd checker at small `N`
before trusting larger runs) and spot-checked the four populated
`a_1=21528751,S={197}` escape chains cited by the source:
`{3,41,197}→{2,3,41,197}→{2,3,7,41,197}` (realized exactly at `a_1291`,
confirmed: `a_1291=21710976={2,3,7,41,197}`), `{2,193,197}→…→a_5844`
(confirmed `a_5844=22356348={2,3,7,193,197}`), `{2,19,197}→…→a_7831`
(confirmed `a_7831=22637664={2,3,7,19,197}`), `{2,3,197}→a_?` (depth 1,
realized value `{2,3,7,197}` confirmed present in the final,
independently-computed global antichain at `n=100000` and `n=400000`) — all
exact matches.

## Certification

Fully proved, general-purpose (holds for any proper core of any sequence
satisfying this problem's hypotheses, independent of `a_1`), no
circularity. Certified `solved`-quality for the Lemma and its iterated
form.

**Honest scope note (unchanged from the source, and reinforced by the
proof-reviewer's round-7 correction to the source's depth data — see
`current.md`'s Round 7 update).** This Lemma sharpens what an escape can
look like (confined to one witness's fixed companion set, not an arbitrary
new prime) but is **not** by itself sufficient to bound escape-recursion
depth uniformly. Do not cite "Escape-Confinement applies" as if it implied
"escape depth is bounded" — it does not; a uniform depth bound remains
unproved, and the proof-reviewer independently found the round's specific
depth-bound data claim ("max depth 2, zero depth-≥3 instances") to be
incorrect once the search range is extended even modestly (see
`current.md`).
