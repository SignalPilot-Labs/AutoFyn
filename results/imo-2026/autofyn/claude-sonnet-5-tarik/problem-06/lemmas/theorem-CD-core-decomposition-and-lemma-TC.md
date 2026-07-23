# Theorem CD (Core Decomposition of 𝓥) and Lemma TC (Top Core is Trivial)

## Status

Certified `solved`-quality (sorry-free), unconditional.

## Notation

As in `theorem-V-veto-finite-iff-MRS.md`. `P_1:=rad(a_1)`, `k:=|P_1|`.

## Theorem CD

**Statement.** Every `C∈𝓥` satisfies `C∩P_1≠∅`. Writing `S(C):=C∩P_1` and
`𝓥_S:=\{C∈𝓥:S(C)=S\}` for nonempty `S⊆P_1`:
`𝓥=⨆_{∅≠S⊆P_1}𝓥_S` (a partition into at most `2^k-1` parts, fixed once
`a_1` is fixed), and `𝓥` is finite iff `𝓥_S` is finite for each of these
`≤2^k-1` values of `S`.

**Proof.** Every `C∈𝓥` is `C=P_i` for an actual index `i`. If `i=1`,
`C∩P_1=P_1≠∅`. If `i≥2`, the already-certified Lemma P′ gives
`\gcd(a_1,a_i)>1`, i.e. `C∩P_1≠∅`. So `S(C)` is well-defined, nonempty,
`⊆P_1` — one of `2^k-1` fixed values. The `𝓥_S` are pairwise disjoint
(unique `S(C)` per `C`) with union `𝓥`. Finite unions of finite sets are
finite and subsets of finite sets are finite, giving the stated
equivalence. ∎

## Lemma TC

**Statement.** `𝓥_{P_1}=\{P_1\}` — the top core (`S=P_1`) contributes only
`P_1` itself.

**Proof.** If `C∈𝓥_{P_1}` (`C⊇P_1`) is realized at index `i∈M_n` for some
`n`, and `C≠P_1`, then `C⊋P_1` strictly. Index `k=1≤n` witnesses
`P_1⊊C`, contradicting `i∈M_n`. So `C=P_1`. Conversely `P_1∈𝓥_{P_1}`
trivially (`i=1`). ∎

**Consequence.** This closes exactly one of the `≤2^k-1` cores
unconditionally: `𝓥` finite iff `𝓥_S` finite for each of the remaining
`≤2^k-2` **proper** nonempty cores `S⊊P_1`.

## Independent re-verification (proof-reviewer, round 5)

Re-derived both proofs from scratch — both are short, correct consequences
of the already-certified Lemma P′ and Lemma W3's `n`-minimality definition,
no gaps. Independently re-simulated (fresh Python, `sympy.primefactors`,
exact greedy rule, no reuse of any builder script) `𝓥` directly (as the
union of all `𝓜_n` computed incrementally, cross-checked against the
Record Characterization Lemma's "fresh index" definition for consistency)
for `a_1=91` (`𝓥_{P_1}=\{\{7,13\}\}` ✓, single element, matches `P_1`) and
`a_1=247` (`𝓥_{P_1}=\{\{13,19\}\}` ✓). Zero violations of Lemma TC found in
every case checked.

## Certification

Certified `solved`-quality, unconditional. Combined with Theorem V
(`theorem-V-veto-finite-iff-MRS.md`), gives:
`(MRS)⟺𝓥`finite`⟺𝓥_S`finite for each of the `≤2^k-2` remaining proper
nonempty cores `S⊊P_1` — the sharpest known unconditional reduction of
(MRS) as of round 5. Does **not** close (MRS) itself; the per-core
finiteness for `S⊊P_1` remains open.

## Source

`results/imo-2026-06/approaches/imprint-automaton-periodicity.md` (round
5).
