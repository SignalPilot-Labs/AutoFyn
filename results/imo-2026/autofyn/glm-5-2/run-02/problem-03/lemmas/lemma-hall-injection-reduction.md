# Lemma — Reduction `L(n+1)` ⟺ sum-level Hall injection `φ` (PROPOSED)

**Status: REJECTED (round 6, reviewer).** The claimed equivalence `L(n+1) ⟺ φ-existence`
is FALSE in the direction `e_M ≤ o_R ⟹ φ-existence`. The proof conflates the TOTAL sum
inequality `(Match) Σ_MM m_even ≤ Σ_RR r_odd` (which is what `e_M ≤ o_R` reduces to by
self-compensation) with Hall's per-subset condition `|N(S)| ≥ |S|` (which is what
φ-existence requires). Counterexample: left L={3,3}, right R={5,1}: Σ m = 6 ≤ 6 = Σ r,
but no injective matching with r ≥ m exists (only one right vertex ≥ 3). So `(Match)` is
NECESSARY but NOT SUFFICIENT for φ. The correct statement is one-directional:
**φ-existence ⟹ L(n+1)** (sufficient condition). The reverse is unestablished. The
builder should downgrade the lemma to the one-directional implication. NOT certified.

**Original PROPOSED statement (retained for reference, INCORRECT as an equivalence):**

## Setup

Level-`(n+1)` dyadic config (`M ⊎ R` decomposition: `M = 2^{n+1}/D(n+1)`,
`R` refined by Xiang into `R'`). Merge the `M`-sub-pieces with the
`R'`-pieces into the global sorted-desc list `p_1 ≥ p_2 ≥ …`. Recall
(CERTIFIED `lemma-em-or-reduction`):
- `e_M` = sum of `M`-sub-pieces at global EVEN ranks,
- `o_R` = sum of `R'`-pieces at global ODD ranks,
- `L(n+1)` (the lower bound `oddsum ≥ M = f(n+1)`) is EXACTLY `e_M ≤ o_R`.

And (CERTIFIED `lemma-self-compensation`): pairing the merged list as
`(p_1,p_2),(p_3,p_4),…`, every pair of type `RM` (odd = `R'`-piece,
even = `M`-sub-piece) self-compensates (`r_odd ≥ m_even` by within-pair
sortedness), so `e_M ≤ o_R` reduces to the residual
**(Match)** `Σ_{MM pairs} m_even ≤ Σ_{RR pairs} r_odd`.

## Statement (Reduction D)

`L(n+1)` is equivalent to the existence of a **sum-level Hall injection**

> `φ :` {`M`-sub-pieces at global even ranks} `⟶` {`R'`-pieces at global odd ranks},  injective,  with `φ(m) ≥ m` for every `m` in the domain.

Applied *sum-level* (NOT per-position: the per-position bound `s_{2j} ≤ a_{j+1}`
is FALSE — counterexample `b = (4/3,4/3,4/3)` at `n = 2`).

## Proof

By `lemma-em-or-reduction`, `L(n+1)` ⟺ `e_M ≤ o_R`. Build the bipartite
graph `G` with left vertices `L =` {`M`-sub-pieces at global even ranks} and
right vertices `R* =` {`R'`-pieces at global odd ranks}, edge `m ↔ r` iff
`r ≥ m`. A matching saturating `L` is exactly an injection `φ` with
`φ(m) ≥ m`; if it exists, summing `m ≤ φ(m)` over `m ∈ L` gives
`e_M ≤ o_R` (unmatched odd-rank `R'`-pieces only add to `o_R`). Conversely,
if `e_M ≤ o_R` holds for every configuration in the family, Hall's condition
(sum of any sub-family of `L` ≤ sum of its `G`-neighborhood in `R*`, which
is bounded by `o_R` for the worst sub-family) is precisely the
self-compensation residual (Match) summed over every sub-family —
establishing the matching. The self-compensation lemma
(`lemma-self-compensation`) reduces the residual to `(Match)`
`Σ_{MM} m_even ≤ Σ_{RR} r_odd`, which is Hall's condition on the
`MM`-pair smaller halves vs `RR`-pair larger halves. By **Hall's marriage
theorem**, `(Match)` ⟺ existence of the matching `φ`. ∎

## Reusability

Any approach using the `M ⊎ R` decomposition may import this to reframe the
general-`n` lower bound `L(n+1)` as a SINGLE matching-existence question on
the merged sort, bypassing per-`k` classification. The structural lever for
proving `φ` exists is the geometric-ratio-2 structure `a_j = 2·a_{j+1}`
(sharpening the certified `lemma-superincreasing-R` to the dyadic-geometric
form). **The existence of `φ` for general `n` is OPEN** (the Hall matchings
(H1), (H2) of `pairing-partner` §E); this lemma records only the
equivalence.

## Scope

- The equivalence is rigorous for all `n` and all `k` (no per-`k`
  classification, no WLOG-`k` exchange).
- Does NOT prove `φ` exists — the existence is the open step.
- Verified (NOT a proof): `e_M ≤ o_R` holds with 0 violations on
  exact-rational samples `n = 2..6` (slack `o_R − e_M` grows with `n`),
  consistent with `φ` existing but not a substitute for the analytic
  construction.

## Where proved

`approaches/pairing-partner.md` (round 6, §D).
