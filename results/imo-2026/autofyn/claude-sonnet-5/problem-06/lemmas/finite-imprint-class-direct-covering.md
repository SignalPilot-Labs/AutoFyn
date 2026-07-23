# Finite-Class Direct Covering (strengthens Lemma FX2)

## Status

Certified `solved`-quality (sorry-free), unconditional.

## Statement

If `I_S` is finite (`S` nonempty, `⊆P_1`), then
`H_S:=⋃_{i∈I_S}rad(a_i)` is finite and satisfies
`H_S∩rad(a_i)∩rad(a_j)≠∅` for **every** `i∈I_S` and **every** `j≠i` of the
whole infinite sequence (not merely `j` in some fixed channel partner
class).

## Proof

`H_S` is a finite union (`I_S` finite) of finite sets, hence finite. Fix
`i∈I_S`, `j≠i`. `rad(a_i)⊆H_S` by construction. The already-certified
Lemma P′ gives `\gcd(a_i,a_j)>1`, i.e. `rad(a_i)∩rad(a_j)≠∅`; any element of
this intersection lies in `H_S∩rad(a_i)∩rad(a_j)`. ∎

## Consequence

For every channel `\{S,S'\}` with `I_S` finite (either side),
`(LMRS_{S,S'})` holds automatically, unconditionally — `H_S` alone covers
every pair touching `I_S`, no antichain/local-MS machinery needed. Since
the finitely many `I_S` partition the infinite set `ℕ`, at least one `I_S`
is infinite (pigeonhole); **the only channels whose `(LMRS_{S,S'})` is not
already unconditionally resolved are those between two doubly-infinite
imprint classes.**

## Independent re-verification (proof-reviewer, round 5)

Four-line proof from the already-certified Lemma P′ alone — re-derived from
scratch, no gap. This strictly strengthens the already-certified Lemma FX2
(`lemmas/lemma-FN-FX-FX2-forced-primes-reduction.md`), which only
established finiteness of a "forced primes" set `F_{S,S'}`, not a full
covering-sufficiency statement.

## Certification

Certified `solved`-quality, unconditional. Reusable by any future approach
needing to dispose of finite-imprint-class channels without re-deriving
Lemma FX2's weaker finiteness-only conclusion.

## Source

`results/imo-2026-06/approaches/forced-primes-well-ordering.md` (round 5).
