# Lemma: Insertion-Difference Identity

**Status:** CERTIFIED (round 16, proposed by `potential-weighting-upper-bound` §25.3/§26, discovered
by the round-16 `math-explorer-gap1c-halfstep` as an intermediate step of a (still-failed) naive proof
attempt; independently re-derived from scratch via a genuinely different derivation route by both the
round-16 outline-reviewer and this round's builder — no gap found; fully general, no `\mathcal
F`-provenance needed).

**Depends on:** the already-certified **Fact 3** (block extraction,
`lemmas/insertion-and-cascade-facts.md`) and the already-certified **General Rank-Extraction Identity**
(`lemmas/general-rank-extraction-identity.md`), and nothing else.

## Statement

Let `M` be a finite multiset of nonnegative reals and `d\ge0` (not required to be an element of `M`,
or possibly a repeated value already in `M` — no distinctness hypothesis anywhere). Write
```
h := #{ m in M : m > d }        (number of elements of M strictly exceeding d),
tail_d := { m in M : m <= d }   (the elements of M that are <= d, as a sub-multiset).
```
Then
```
e(M u {d}) - e(M) = (-1)^h * ( d - 2 e(tail_d) ),
```
where `e(\cdot)=e_{\mathrm{sorted}}(\cdot)` is the standard sorted-descending alternating sum used
throughout `potential-weighting-upper-bound.md` (`s_1-s_2+s_3-\dots`).

## Proof

Write `\mathrm{head}_d := \{m\in M : m>d\}` (so `|\mathrm{head}_d|=h`) and recall `\mathrm{tail}_d=
\{m\in M:m\le d\}`, so `M=\mathrm{head}_d\sqcup\mathrm{tail}_d` (disjoint multiset union), and every
element of `\mathrm{head}_d` is `>d\ge$ every element of `\mathrm{tail}_d`.

**Step 1 — split `M` via Fact 3.** Since every element of `\mathrm{head}_d$ is `\ge` every element of
`\mathrm{tail}_d` (in fact strictly `>`), Fact 3 (block extraction,
`lemmas/insertion-and-cascade-facts.md`, with `X:=\mathrm{head}_d`, `Y:=\mathrm{tail}_d`) gives
```
e(M) = e(head_d) + (-1)^h e(tail_d).                                              ...(1)
```

**Step 2 — extract `d` from `M\cup\{d\}$ via the General Rank-Extraction Identity.** In the sorted
descending order of `F:=M\cup\{d\}` (inserting the single new element `d`), every element of
`\mathrm{head}_d` (all `>d`) is ranked strictly above `d`, and every element of `\mathrm{tail}_d` (all
`\le d`) is ranked at or below `d`'s own rank; so `d` occupies sorted rank `r=h+1` in `F`, with
`\mathrm{head}_d` exactly the `r-1=h` elements above it and `\mathrm{tail}_d` exactly the `n-r`
elements below it (`n=|M|`). The **General Rank-Extraction Identity**
(`lemmas/general-rank-extraction-identity.md`, applied to `F=M\cup\{d\}`, `x=d`, rank `r=h+1`,
`\mathrm{head}=\mathrm{head}_d`, `\mathrm{tail}=\mathrm{tail}_d`) gives
```
e(M u {d}) = e(head_d) + (-1)^{r-1} d + (-1)^r e(tail_d)
           = e(head_d) + (-1)^h d + (-1)^{h+1} e(tail_d).                          ...(2)
```

**Step 3 — combine (1) and (2).** From (1), `e(\mathrm{head}_d)=e(M)-(-1)^h e(\mathrm{tail}_d)`.
Substitute into (2):
```
e(M u {d}) = e(M) - (-1)^h e(tail_d) + (-1)^h d + (-1)^{h+1} e(tail_d)
           = e(M) + (-1)^h d - (-1)^h e(tail_d) - (-1)^h e(tail_d)          [since (-1)^{h+1}=-(-1)^h]
           = e(M) + (-1)^h d - 2(-1)^h e(tail_d)
           = e(M) + (-1)^h [ d - 2 e(tail_d) ].
```
Rearranging gives exactly `e(M\cup\{d\})-e(M)=(-1)^h(d-2e(\mathrm{tail}_d))`. `\blacksquare`

## Remarks

- The identity holds for **every** `M` and `d\ge0` — no `\mathcal F`-provenance, no distinctness, no
  size restriction. Ties (elements of `M` exactly equal to `d`) are handled correctly by construction:
  `\mathrm{tail}_d` is defined to *include* elements equal to `d` (the `\le` in its definition, not
  `<`), matching exactly how the General Rank-Extraction Identity's own rank-`r` bookkeeping treats a
  newly-inserted value tying with existing elements (any consistent tie-break assignment gives the
  same `e`, per that lemma's own statement).
- This identity was discovered as an intermediate computation inside a (confirmed FALSE) naive proof
  attempt for `potential-weighting-upper-bound.md`'s Gap 1c half-step lemma (the "same witness, just
  drop `d`" transfer, §25.3 Step 2) — the identity itself is correct and general; only that particular
  *application* of it fails to close the half-step. It remains the natural tool for the half-step's
  Step-3 nearest-neighbor construction (see `potential-weighting-upper-bound.md` §25.3/§27).
- **Special case check (consistency with Fact 4).** Fact 4 of `lemmas/insertion-and-cascade-facts.md`
  (`|e(Y\cup\{x\})-e(Y)|\le x`) is an immediate corollary: `d-2e(\mathrm{tail}_d)\in[-d,d]` since
  `0\le e(\mathrm{tail}_d)\le\max(\mathrm{tail}_d)\le d` (the first inequality is Fact 1 of the same
  file, nonnegativity of `e`; the second is Fact 2, `e\le\max`), so
  `|e(M\cup\{d\})-e(M)|=|d-2e(\mathrm{tail}_d)|\le d`, exactly Fact 4's bound. This cross-check
  confirms the identity is consistent with already-certified machinery, not merely numerically
  corroborated in isolation.

## Verification

- **Round-16 discovering explorer:** the identity itself is stated and used (not independently
  stress-tested as a standalone claim beyond its role in the failed Step-2 attempt).
- **Round-16 outline-reviewer:** independent fresh code, `0/3{,}000` violations, arbitrary `(M,d)`
  (`|M|\le6`, mixed alphabets).
- **This round's builder (independent, fresh code, `/tmp/round-16/verify_builder/insertion_diff.py`,
  not reusing the outline-reviewer's or explorer's harness):** `0/20{,}000` random trials
  (`|M|\in\{0,\dots,7\}`, `v_{\max}\in\{3,10,50,200\}`, mixed-denominator rationals) **and** `0/780`
  in an **exhaustive** small-value sweep (`|M|\in\{0,1,2,3\}`, all `M,d` drawn from the 5-value grid
  `\{0,1,2,\tfrac12,\tfrac32\}$, every combination, not sampled) — zero mismatches across both a broad
  random battery and a genuinely exhaustive small-case grid (which specifically stresses ties, since
  the 5-value grid guarantees repeated elements and `d`-equals-`M`-element coincidences appear
  throughout).

## Used by

- `potential-weighting-upper-bound.md` §25.3/§27 (Gap 1c's half-step lemma — both the confirmed-dead
  Step-2 naive transfer and the still-open Step-3 nearest-neighbor construction use this identity as
  their common algebraic tool).
