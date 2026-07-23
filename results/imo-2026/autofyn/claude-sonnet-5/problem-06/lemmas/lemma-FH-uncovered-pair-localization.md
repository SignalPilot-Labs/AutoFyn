# Lemma FH (uncovered-pair localization)

## Notation

`P_1:=rad(a_1)`, `G_i:=rad(a_i)∩P_1` (the `P_1`-imprint of index `i`; by the
already-certified Lemma P, `G_i≠∅` for every `i≥1`).

## Statement

Let `H` be *any* set of primes with `P_1⊆H`. If a pair `i<j` satisfies
`H∩rad(a_i)∩rad(a_j)=∅` (i.e. `H` fails to cover this pair), then
`G_i∩G_j=∅`.

## Proof

Contrapositive. Suppose `G_i∩G_j≠∅`; pick `q∈G_i∩G_j`. By definition
`G_i=rad(a_i)∩P_1` and `G_j=rad(a_j)∩P_1`, so `q∈rad(a_i)`, `q∈rad(a_j)`,
and `q∈P_1⊆H`. Hence `q∈H∩rad(a_i)∩rad(a_j)`, so this intersection is
nonempty. `∎`

## Discussion

This is a completely general, unconditional fact about *any* candidate
covering set containing `P_1` (not specific to the forced-primes set `F`):
the entire content of "does `H` cover every pair?" is confined to **channel
pairs** (`G_i∩G_j=∅`, in the sense of the already-certified Lemma FX's
`≤3^k`-channel partition, `lemmas/lemma-FN-FX-FX2-forced-primes-reduction.md`).
This unifies the necessity direction (Lemma FN/FX, already certified) and
the sufficiency question under one combinatorial skeleton.

## Independent re-verification (reviewer, round 4)

One-line contrapositive proof, checked directly — correct, no gaps, no
hidden hypotheses beyond `P_1⊆H`.

## Source

`results/imo-2026-06/approaches/forced-primes-well-ordering.md` (round 4).

## Certification

Certified `solved`-quality (sorry-free), fully unconditional (no dependency
on FCBC, on Lemma FF, or on any other open hypothesis). Reusable by any
future approach reasoning about sufficiency of a candidate covering set that
contains `P_1` — reduces "check every pair" to "check every channel pair,"
for any such candidate, not just the specific set `F` used in the source
file.
