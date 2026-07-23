# Sandwich Uniqueness Lemma

**Source.** `results/imo-2026-06/approaches/forced-primes-well-ordering.md`
§K Step 1 (round 12, new).

## Statement

Fix a doubly-infinite disjoint core pair `(S,S')` (`I_S,I_{S'}` both
infinite, `S\cap S'=\varnothing`). Fix `z\in\{S,S'\}` and let `y` be the
other core. Suppose `W` is a nonempty finite set of primes disjoint from
`P_1` witnessing Conjecture (JW) for `(S,S')` **via the Realized-Backbone/
UCR mechanism** (Theorem CAC, `lemmas/lemma-BS-backbone-stabilization-and-
theorem-CAC.md`), i.e.:

(a) `W\subseteq\mathrm{comp}(a_k)` for every `k\in I_z` (full-class
containment on side `z`), and

(b) `W` is *exactly realized* on side `z`: `\mathrm{comp}(a_m)=W` for some
`m\in I_z`.

Then `W=B_{\mathrm{full}}(z):=\bigcap_{k\in I_z}\mathrm{comp}(a_k)` exactly.

## Proof

By (a), `W\subseteq\mathrm{comp}(a_k)` for every `k\in I_z`, hence
`W\subseteq\bigcap_{k\in I_z}\mathrm{comp}(a_k)=B_{\mathrm{full}}(z)`.
Conversely, `m\in I_z` (by (b)), so `B_{\mathrm{full}}(z)` (an intersection
over *all* of `I_z`, in particular over the single index `m`) satisfies
`B_{\mathrm{full}}(z)\subseteq\mathrm{comp}(a_m)=W` (using (b) again).
Combining both containments: `W=B_{\mathrm{full}}(z)`. `\blacksquare`

This needs no appeal to Backbone Permanence/Lemma BS, No-Resurrection, or
any other conditional machinery — it is a two-line consequence of the
mechanism's own two defining hypotheses (a), (b). Note `B_{\mathrm{full}}
(z)` is exactly the object Lemma BS proves equals the stabilized running
intersection `B(z)` (so in practice, given Lemma BS, `B_{\mathrm{full}}(z)
=B(z)` and this Lemma states the mechanism has no freedom to choose `W` to
be anything other than that specific stabilized set).

## Consequence (mechanism rigidity)

For the Realized-Backbone/UCR mechanism to close (JW) for `(S,S')` via
anchor `z`, `W` is *forced* to equal `B_{\mathrm{full}}(z)` — there is no
freedom to pick a smaller or different realized set. Hence the mechanism
succeeds via anchor `z` **if and only if** `B_{\mathrm{full}}(z)` is (i)
nonempty and (ii) exactly realized as some `I_z`-member's full companion
set. Both conditions must be checked; failing either kills that anchor
choice for that pair.

## Worked application (certified alongside, round 12): `a_1=4199`'s pair
`(\{13\},\{17\})` is unconditionally out of reach for this mechanism

Both possible anchors fail:

- `z=\{17\}`: `\mathrm{comp}(a_3)=\{2,31\}`, `\mathrm{comp}(a_5)=\{3,83\}`
  (indices `3,5\in I_{\{17\}}`), disjoint, so `B_{\mathrm{full}}(\{17\})
  \subseteq\{2,31\}\cap\{3,83\}=\varnothing`. Fails condition (i)
  unconditionally, from two concrete already-computed terms — no
  asymptotic argument needed.
- `z=\{13\}`: the running prefix intersection reaches `\{2\}` by the 3rd
  realized class-`\{13\}` member (`i=2`: `\mathrm{comp}=\{2,3\}`; `i=8`:
  `\{2,3,5,11\}`; `i=9`: `\{2,83\}`; running intersection `\{2,3\}\to
  \{2,3\}\to\{2\}`) and stays `=\{2\}` through all `2791` tested members to
  `N=12{,}000`. Since `B_{\mathrm{full}}(\{13\})\subseteq\{2\}` (a subset
  of any already-computed prefix intersection), it is either `\{2\}` or
  `\varnothing` — no third possibility. If `\{2\}`: condition (ii) would
  need `\mathrm{rad}(a_m)=\{2,13\}` exactly for some `m`; but the
  already-certified Lemma ERD-C, applied to `\kappa=\{2,13\}` with witness
  `j=5` (`\mathrm{rad}(a_5)=\{3,17,83\}`, disjoint from `\{2,13\}`), proves
  `\kappa` is blocked, hence *never* realized at any index — condition (ii)
  fails. If `\varnothing`: condition (i) fails, same as the `z=\{17\}` case.
  Both sub-cases fail; the dichotomy is exhaustive and mutually exclusive,
  so this resolution needs no determination of whether Backbone
  Permanence/Lemma BS's stabilized value actually equals `\{2\}` on this
  side — the mechanism fails either way.

**Conclusion**: the Realized-Backbone/UCR mechanism (Theorem CAC) cannot
close Conjecture (JW) for `4199:(13,17)`, unconditionally and exhaustively
over both anchors. This does **not** prove Conjecture (JW) false for this
pair — only that this specific mechanism cannot establish it; the pair
remains open, to be attacked (if at all) by a different mechanism (e.g.
`sunflower-bundle-closure`'s NIDF-pigeonhole route, itself also not yet
successful on this pair — see `current.md`'s round 12 update).

## Certification

Independently re-derived by the proof-reviewer (round 12): re-proved the
two-line sandwich argument from scratch; independently re-generated
`a_1=4199` (own generator, `sympy.factorint`) and confirmed exactly:
`a_2=4212=2^2\cdot3^4\cdot13` (`\mathrm{comp}=\{2,3\}`, core `\{13\}`),
`a_3=4216=2^3\cdot17\cdot31` (`\mathrm{comp}=\{2,31\}`, core `\{17\}`),
`a_5=4233=3\cdot17\cdot83` (`\mathrm{comp}=\{3,83\}`, core `\{17\}`),
`a_8=4290=2\cdot3\cdot5\cdot11\cdot13` (`\mathrm{comp}=\{2,3,5,11\}`, core
`\{13\}`), `a_9=4316=2^2\cdot13\cdot83` (`\mathrm{comp}=\{2,83\}`, core
`\{13\}`) — all factorizations, cores, and companion sets match exactly.
Verified the running intersection `\{2,3\}\to\{2,3\}\to\{2\}` for the
`\{13\}`-side and the disjointness `\{2,31\}\cap\{3,83\}=\varnothing` for
the `\{17\}`-side directly. Verified Lemma ERD-C's hypothesis (`\mathrm{rad}
(a_5)\cap\{2,13\}=\{3,17,83\}\cap\{2,13\}=\varnothing`) exactly. No gap
found.

Fully proved, general-purpose (the abstract Sandwich Uniqueness Lemma, not
just the worked `4199` application), no dependency on any open hypothesis
in this workspace. Certified `solved`-quality.
