# Round 12 build report: greedy-reduction-geometric

## Target
Attack the shared window (Theorem N's residual = `self-similar-induction-
on-n`'s Branch-I.A-restricted window): $c_1\in[2^{\ell-1},2^{\ell-1}+1-
\varepsilon)$, $\max(C\setminus\{c_1\})<2^{\ell-1}$, $\mathrm{sum}(C)=
2^\ell+\varepsilon$, $|C|\le\ell+1$, target $\mathrm{OddSum}(C\cup
\Gamma_{\ell-1})\ge2^\ell$.

## Result: gap (b) (monotonicity in $c_1$) fully closed; gap (a) still open

Wrote Section 16 of `approaches/greedy-reduction-geometric.md`. Summary:

1. **Elementwise Monotonicity Lemma** (new, general-purpose): for a fixed
   multiset $N$, $\mathrm{OddSum}(N\cup\{x\})$ is non-decreasing in $x$.
   Proved from scratch (rank-gap + continuity argument). Stress-tested
   20,000 exact-`Fraction` trials, 0 violations.
2. **Transfer Monotonicity Theorem**: since $c_1$ is always the weak max
   of the window's multiset ($c_1\ge2^{\ell-1}=\max(\Gamma_{\ell-1})>
   \max(D)$), Peel-the-Max plus the Elementwise lemma shows moving mass
   from any $D$-coordinate (existing or a fresh slot) into $c_1$ never
   decreases OddSum. Proved in full.
3. **Headroom subtlety (found and fixed):** naively "grow an existing
   $D$-element to absorb the transfer" has headroom short by exactly
   $\varepsilon$ when $|D|=1$ — caught this by direct computation before
   trusting it, then fixed by using the "insert a fresh slot" mechanism
   instead whenever $|D|<\ell$ (always available, no headroom needed);
   only the cardinality-saturated case $|D|=\ell$ needs the "grow
   existing" mechanism, and there headroom is always ample (proved).
4. **Window Reduction Theorem**: chaining these transfers shows the full
   window target is *equivalent* to the single left-endpoint statement,
   for every admissible $D$ there (not just Theorem W's witness) — i.e.
   exactly gap (a) alone. This fully subsumes and generalizes the
   certified Lemma TPI (which only handled the piece-cap-unsaturated
   sub-case via a different, insertion-based mechanism) and additionally
   closes the previously-untouched saturated sub-case (b)(ii).
5. **Cross-check**: independently re-derived, via a one-step Peel-the-Max
   + Companion-Peeling computation (a different route than the sibling
   file's sum/EvenSum algebra), that gap (a) is symbol-for-symbol the same
   target as the sibling's own certified endpoint-reduction identity
   (`OddSum(D∪Γ_{ℓ-2})≥2^{ℓ-1}`). This confirms, from an independent
   direction, that gap (a) — not gap (b) — is the field's one remaining
   bottleneck on this shared window.
6. **Gap (a) not closed.** Exact-rational grid search (denominators up to
   24, $\ell=2,3,4$, several $\varepsilon$) found the true minimum margin
   at the endpoint is exactly $\varepsilon/2$ at every tested instance,
   always at a tied-pair-shape witness generalizing Theorem W's — strong
   evidence gap (a) is true and that Theorem W's family is the actual
   extremal shape, but this is grid-search evidence at finitely many
   rational points, not a proof for general $\ell$/continuous $D$. Route
   (a) from the round's explorer report (strong induction on $\ell$) is
   still the recommended next step; not attempted this round for lack of
   time after closing gap (b).

## Honesty check
All reduction-mechanism claims (Elementwise Monotonicity, both Transfer
Monotonicity mechanisms individually, and the full mixed-mechanism
reduction algorithm) were stress-tested in exact `Fraction` arithmetic
(never floats), with thousands of trials each and zero violations,
*before* being written up as proved. No claim beyond gap (b)'s closure is
asserted as proved; gap (a) is explicitly flagged as open with only
computational evidence. Status of this approach remains `partial` — no
new "solved" claim. Coordinating note for `self-similar-induction-on-n`:
this round's Window Reduction Theorem is a genuinely new, general result
(not previously in either file) that narrows the shared window down to
gap (a) alone; the sibling's own round-12 attack (if it made progress on
gap (a) via strong induction) should be checked against this file's
Section 16.4 corollary, which gives an independent re-derivation of the
same target.

## Files touched
- `results/imo-2026-03/approaches/greedy-reduction-geometric.md` (Round 12
  target block updated with Result; new "Approaches tried" bullet;
  new Section 16, ~230 lines).
- No files written to `lemmas/` (per instructions, not self-certified —
  proposing the Elementwise Monotonicity Lemma and the Window Reduction
  Theorem to the reviewer for certification).

## Scripts (scratch, not committed)
`/tmp/round-12/search1.py`, `search2.py`, `search3.py`, `search4.py`,
`gapA.py`, `verify_reduction.py`, `verify_k1.py`, `verify_EM.py`,
`verify_ksat.py`, `verify_full_reduction.py` — all exact `Fraction`
arithmetic, available for the reviewer to re-run or adapt.
