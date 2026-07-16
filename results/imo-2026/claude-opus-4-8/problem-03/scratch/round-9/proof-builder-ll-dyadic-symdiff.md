# Build report — ll-dyadic-symdiff (R9), imo-2026-03

Status: **partial** (advance). Target was bucket (iii) top-cut refined `R` + the required termination gap.

## Spec concerns
None material. The outline's step 4 ("n=3 base by parity casework") is achievable but the parity split it
proposed (|Q|=3 odd vs |R|=4 even ⟹ S_Q⊄S_R) is NOT how I closed it — I closed the whole n=3 top-cut
regime by a measure/merge argument (Lemma Q3 + regime split on the top-cut parameter `a`), which is cleaner
and subsumes the residual. One correction to the outline framing: "termination of the REFL telescoping" is
*trivially* well-founded (piece-count descent); the genuinely open piece is the **base-object lower bound**,
not termination. I proved termination rigorously and flagged the base bound honestly as the open crux — do
not treat termination as the blocker.

## What I closed rigorously this round
- **K1 (small-overlap kill), all `n`:** `2·measure(S_Q∩S_R) ≤ A(Q) ⟹ A(Q∪R) ≥ A(R) ≥ 1` (incl. disjoint).
- **K2 (difference kill), all `n`:** `A(Q∪R) ≥ |A(Q)−A(R)|`, so `|A(Q)−A(R)| ≥ 1 ⟹ A(Q∪R) ≥ 1`.
- **n=3 bucket (iii) COMPLETELY CLOSED** (the whole `max(Q),max(R)<4` top-cut regime, all configs):
  budget forces `c_Q=2, c_R=1`, `R={4−a,2,a,1}`; closed-form `S_R` in two `a`-regimes; single `Q`-only
  Lemma Q3 (`2·measure(S_Q∩[2,∞)) ≤ A(Q)`, from forced `q_2>2`) drives both regimes. Regime II uses a
  `q_3`-trichotomy with K2. Verified `1/16`-grid, budget: 10912 configs, `min A = 1`, 0 violations.
- **REFL-telescope termination (the required gap), rigorously:** deleting the running global max is a
  finite well-founded descent (piece-count ↓ by 1, `Σ` ↓ by `μ_i>0`), terminating in `m` steps; each step
  is certified REFL-gen; gives the double-REFL cancellation `A(Q∪R)=max(Q)−max(R)+A(Q'∪R'')`.

## Honest open gap (not overclaimed)
General-`n` bucket (iii): termination is proved but only *recomputes* `A(P)`; the bottom object
`A(Q'∪R'') ≥ 1` is the **refined-`R` alternating-tail crux** (no `2^{n−1}` anchor, no refined SET
IDENTITY), OPEN for `n ≥ 4`. Only `n=3` is closed. The all-`n` cheap-kills K1/K2 partially cover `n ≥ 4`.

## Promotable lemmas (for reviewer certification)
K1, K2, Lemma Q3, Lemma REFL-telescope — all proved in full in the approach file's Promotable section.

Proof work written to results/imo-2026-03/approaches/ll-dyadic-symdiff.md.
