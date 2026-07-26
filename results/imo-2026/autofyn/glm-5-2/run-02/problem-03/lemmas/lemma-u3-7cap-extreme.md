# Lemma: U(3) — 7-cap extreme-regime contradiction (regime IV, `d < 1/2 ∧ (w < −2α ∨ z < −2α)`)

**Status:** CERTIFIED (round 6, reviewer APPROVE). Proved in `approaches/two-regime-disjunctive.md` §5e. Reviewer (round 6) independently re-derived all 8 sign-triple sub-case contradictions and verified the realizability of the two NEW abs caps (|a+c−d|, |a+b−d|) via the equal-pair cancellation lemma; confirmed 0 violations on 5473 exact-rational extreme configs + LP max t<0 in all 12 sub-cases (`/tmp/round-6/u3_7cap_verify.py`). Closes regime IV of U(3); combined with regimes I–III + certified L(3) gives c(3)=8/15 SOLVED end-to-end.

## Statement

Let `n = 3`, `α := α(3) = 1/15`, `f(3) = 8/15`. For a 4-piece Liu config `(a, b, c, d)`, `a ≤ b ≤ c ≤ d`, `a + b + c + d = 1`, define the **chain excesses**
```
u := a − α,    v := (b − a) − α,    w := (c − a − b) − α,    z := (d − b − c) − α
```
(so `a = α+u`, `b = 2α+u+v`, `c = 4α+2u+v+w`, `d = 7α+3u+2v+w+z`, and the identity `7u + 4v + 2w + z = α` holds; `d < 1/2 ⟺ u > z`). In the **extreme regime**
```
E := {d < 1/2  ∧  (w < −2α  ∨  z < −2α)},
```
Xiang with `≤ 3` marks forces
```
min( a,  b − a,  c − b,  d − c,  |a + b − c|,  |a + c − d|,  |a + b − d| )  ≤  α(3) = 1/15,
```
hence `Liu ≤ 8/15 = f(3)` (via `Liu = (1 + A)/2`, certified Lemma G). The inequality is **strict** in `E` (no config attains `min = α`).

## The seven cap strategies (each ≤ 3 marks, all always-realizable)

The four **chain-difference caps** (certified `lemma-u3-5cap-dominant.md` §5d.1):
- `S_a` (bisect `b, c, d`; 3 marks): `A = a`. (`C1`)
- `S_{b−a}` (match `a` in `b` + bisect `c, d`; 3 marks): `A = b − a`. (`C2`)
- `S_{c−b}` (match `b` in `c` + bisect `a, d`; 3 marks): `A = c − b`. (`C3`)
- `S_{d−c}` (match `c` in `d` + bisect `a, b`; 3 marks): `A = d − c`. (`C4`)

The three **abs-sum caps** (2 marks each):
- `S_{|a+b−c|}` (bisect `d` + match `a` in `c`; 2 marks, certified §5d.1): pairs `(d/2,d/2),(a,a)`; singletons `b, c−a`. `A = |a+b−c|`. (`C5`)
- `S_{|a+c−d|}` (**NEW**, bisect `b` + match `a` in `d`; 2 marks): pairs `(b/2,b/2),(a,a)`; singletons `c, d−a`. `A = |a+c−d|`. (`C6`)
- `S_{|a+b−d|}` (**NEW**, bisect `c` + match `a` in `d`; 2 marks): pairs `(c/2,c/2),(a,a)`; singletons `b, d−a`. `A = |a+b−d|`. (`C7`)

All 7 are always-realizable (the only "match" moves need `b,c,d ≥ a` or `c ≥ b` or `d ≥ c`, all guaranteed by `a ≤ b ≤ c ≤ d`). **None requires `d ≥ b+c`** — this is the correction that overturns round-5's "no 4–7-cap subfamily suffices" ruling (which counted un-realizable cap *values* like `d−b−c`).

The caps in chain-excess form (using `z = α−7u−4v−2w`):
```
C1 = α+u,    C2 = α+v,    C3 = 2α+u+w,    C4 = 4α−6u−3v−2w,
C5 = |α+w|,  C6 = |3α−7u−3v−2w|,  C7 = |5α−6u−3v−w|.
```
Denote `L_6 := 7u+3v+2w`, `L_7 := 6u+3v+w` (so `C6 = |3α−L_6|`, `C7 = |5α−L_7|`, `L_6 − L_7 = u+w`).

## Proof

Assume for contradiction all 7 caps `> α`. The chain caps `C1,C2,C3,C4 > α` give:
```
(I) u > 0,    (II) v > 0,    (III) u+w > −α,    (IV) 6u+3v+2w < 3α,    (∗) d<1/2: u > z.
```
Each abs-cap `Ck` (k=5,6,7) is on one of two sign branches; let `s_k ∈ {+1,−1}` be the sign of its interior (`s_5=+1 ⟺ w>0`; `s_5=−1 ⟺ w<−2α`; `s_6=+1 ⟺ L_6<2α`, `s_6=−1 ⟺ L_6>4α`; `s_7=+1 ⟺ L_7<4α`, `s_7=−1 ⟺ L_7>6α`). The 2³ = 8 sign triples partition `E` (the all-`>α` assumption excludes ties). Key: `s_5 = −1` IS the condition `w < −2α`, so the 4 `s_5=−1` triples cover configs with `w < −2α` (regardless of `z`), and the 4 `s_5=+1` triples cover `w > 0` configs (which force `z < −2α`).

**Group A: `s_5 = −1` (`w < −2α`), by `(s_6, s_7)`.**

- **A1 `(−,+,+)`** (`L_6<2α`, `L_7<4α`): `w<−2α` ∧ (III) ⟹ `u>α`. `L_6<2α` ∧ (II) ⟹ `7u+2w<2α`. (III) ⟹ `7u+2w = 5u+2(u+w) > 5u−2α`. So `5u−2α < 2α` ⟹ `u < 4α/5 < α`, contradicting `u>α`. ∎
- **A2 `(−,+,−)`** (`L_6<2α`, `L_7>6α`): `u+w = L_6−L_7 < 2α−6α = −4α`, but (III) `u+w > −α`. Contradiction. ∎
- **A3 `(−,−,+)`** (`L_6>4α`, `L_7<4α`): `u+w = L_6−L_7 > 0`; with `w<−2α` ⟹ `u>2α`. Identity `2L_7 = L_6+5u+3v` gives `2L_7 > 4α+10α+0 = 14α`, but `L_7<4α` ⟹ `2L_7<8α`. `14α < 8α`, contradiction. ∎
- **A4 `(−,−,−)`** (`L_6>4α`, `L_7>6α`): (IV) ∧ `L_7>6α` ⟹ `w = (6u+3v+2w)−L_7 < 3α−6α = −3α`. Then (III) `6(u+w)>−6α` ⟹ `6u+2w = 6(u+w)−4w > −6α+12α = 6α`. (IV) ⟹ `3v < 3α−(6u+2w) < 3α−6α = −3α < 0`, so `v<0`, contradicting (II). ∎

**Group B: `s_5 = +1` (`w > 0`, sign-constraint `w ≥ −α`), only in `z < −2α` sub-regime (use `(S2): 7u+4v+2w > 3α`).**

- **B1 `(+,+,+)`** (`w>0`, `L_6<2α`, `L_7<4α`, (S2)): (S2) ∧ `L_6<2α` ⟹ `v = (7u+4v+2w)−L_6 > 3α−2α = α`. `w>0` ∧ `L_6<2α` ⟹ `7u+3v < 2α`. `v>α` ⟹ `7u < 2α−3v < −α` ⟹ `u < −α/7 < 0`, contradicting (I). ∎ *(Tightest: global extremum `12α/13 = 4/65`.)*
- **B2 `(+,+,−)`** (`L_6<2α`, `L_7>6α`): `u+w = L_6−L_7 < −4α`, vs (III) `u+w > −α`. Contradiction. ∎ (Same as A2.)
- **B3 `(+,−,+)`** (`L_6>4α`, `L_7<4α`): (IV) ∧ `L_6>4α` ⟹ `u = L_6−(6u+3v+2w) > 4α−3α = α`. `L_7<4α` ∧ `u>α` (so `6u>6α`) ∧ (II) `v>0` ⟹ `L_7 = 6u+3v+w > 6α+w`, so `4α > 6α+w` ⟹ `w < −2α`. But `s_5=+1` requires `w ≥ −α`. Contradiction. ∎
- **B4 `(+,−,−)`** (`L_6>4α`, `L_7>6α`): (IV) ∧ `L_7>6α` ⟹ `w < −3α` (as in A4). `s_5=+1` requires `w ≥ −α`. `−3α < −α`, contradiction. ∎

All 8 sub-cases contradict. The 8 triples exhaust `E`, so "all 7 caps `> α`" is infeasible in `E`: at least one cap `≤ α`. Strictness: the LP-per-subcase optimum `max t < 0` strictly in all 8 (global max `min-cap = 4/65 < α`), so no config in `E` attains `min = α`. ∎

## Verification

(`/tmp/round-6/u3_7cap_verify.py`, exact `Fraction` + scipy `linprog`.) (a) 5473 exact-rational extreme configs (random + chain-excess grid `N=18`): **0 violations**, worst `min = 0.0582 < α = 0.0667`. (b) LP `max t < 0` strictly in all 8 sign-triples; global extremum `min-cap = 4/65 = 12α/13` at the vertex `u=w=−α/13, v=12α/13, z=−2α` (sub-case B1), margin `α/13 = 1/195`. (c) Drop-one (coarse grid): `C1,C2,C3,C4,C6` unambiguously load-bearing; `C5`/`C7` appear droppable on the coarse grid but the explorer's 2M-sample search confirmed drop-`C7` fails by ~0.002 (the 7th cap `|a+b−d|` is genuinely load-bearing on fine samples). The proof does not rely on minimality.

## Reusability

The direct `n=3` generalization of the certified `U(2)` four-strategy lemma and the round-5 5-cap dominant-regime lemma. Closes regime IV (the extreme sub-cases) of `U(3)`. Combined with `lemma-u3-5cap-dominant.md` (regime I, `d ≥ 1/2`), `lemma-u3-sliver-gap.md` (regime II, gap `G`), the regime-III caps `|a+b−c|`/`|b+c−d|`/`a`/`b−a` (with `|b+c−d|` realizable via "bisect `a` + match `c` in `d`", §5e.4 of the approach), and the CERTIFIED `L(3)` (cell-complex, `lemma-vertex-principle-advantage.md`), yields **`c(3) = 8/15` end-to-end** (both bounds, equality iff the dyadic `(1,2,4,8)/15`).

## Scope

- **`n = 3` only**, and **the extreme regime `E` only** (regime IV of `U(3)`).
- Does NOT cover regimes I–III (handled by the 5-cap, sliver, and `|a+b−c|`/`|b+c−d|`/`a`/`b−a` caps).
- Does NOT generalize to `n ≥ 4` (the cap family grows combinatorially; no inductive structure identified).
- The all-7-caps-realizable property is essential: the family is NOT a list of algebraic *values* but of *strategies*. The un-realizable values `d−b−c` (needs `d ≥ b+c`) and `2d−1` (needs `d ≥ 1/2`) are correctly EXCLUDED.
