# Lemma: peeling (equal-pair additivity)

## Statement

Let the current piece multiset `S` contain a piece `p_1` and another piece `p_j` with `0 ≤ p_j ≤ p_1`. Xiang splits `p_1` into `p_j + (p_1 − p_j)` (one mark; legal since `p_1 − p_j ≥ 0`), creating a new fragment equal to the existing `p_j`. Then

> `D_final = D_rest`,

where `rest := (S \ {p_1, p_j}) ∪ {p_1 − p_j}` — i.e. remove `p_1` and ONE copy of `p_j` (the original), and add the leftover `p_1 − p_j`.

Equivalently: the two copies of `p_j` (the original piece and the new fragment from the split) jointly contribute `+2` to `j(t)` on `[0, p_j)`, which is EVEN and hence parity-neutral, so removing the equal pair leaves `D` unchanged. This is the unique place where `D` is genuinely additive across a refinement.

## Proof (via the parity-integral lemma)

Let `j_old, j_new, j_rest` be the `j`-functions before the split, after, and on the rest. After the split, the multiset is `(S \ {p_1}) ∪ {p_j (new), p_1 − p_j}` — the original `p_j` is NOT removed, so there are now TWO copies of `p_j`. Thus

`j_new(t) = j_old(t) − [p_1 ≥ t] + [p_j ≥ t] + [p_1 − p_j ≥ t]`.

The rest removes `p_1`, one copy of `p_j`, and adds `p_1 − p_j`:

`j_rest(t) = j_old(t) − [p_1 ≥ t] − [p_j ≥ t] + [p_1 − p_j ≥ t]`.

Subtracting:

`j_new(t) − j_rest(t) = 2 · [p_j ≥ t]`.

This difference is **even for every `t`** (a multiple of 2), so `j_new(t)` and `j_rest(t)` have the **same parity** for every `t`. By the parity-integral lemma (`D = ∫[j odd]`),

`D_final = ∫[j_new odd] dt = ∫[j_rest odd] dt = D_rest`. ∎

## Verification

Independently checked on 20k random configs (multisets of size 2–6, random `p_j`): `|D_final − D_rest|` max error `0` (exact). See proof-reviewer round 3 verification.

## Caveat (circularity of the inductive *use*)

The lemma itself is non-circular. However, its **inductive use** ("peel once, then apply `D_rest ≤ 1/D_{n−1}`") is circular unless the inductive hypothesis is strengthened: the rest config is *derived* (its largest piece is `p_1 − p_j`, inheriting structure from Liu's original config), not an arbitrary `(n−1)`-mark game. The naive hypothesis `D_rest ≤ (rest total)/D_{n−1}` is loose at the dyadic config for `n ≥ 3` (dyadic `n=3`: `13/45 ≫ 1/15`). The lemma is a *computational tool* (e.g. for one-mark strategies and the n=1 bound), not a sound inductive engine for the general upper bound without a strengthened, transferable invariant.

## Source

Proved in `pairing-charging` §4 (round 2) and independently in `alternating-potential` §2.3 (round 2). Canonical location: this file.

## Certification

Reviewer-certified round 3 (proof-reviewer, imo-2026-03). The statement is proved `sorry`-free from the parity-integral; the parity-neutrality of `+2` is exact; the circularity caveat on its inductive use is stated explicitly so importers do not over-apply it. Importable by any approach needing `D`-additivity at an equal-pair split.
