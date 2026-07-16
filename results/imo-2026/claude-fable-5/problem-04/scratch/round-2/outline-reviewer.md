# Outline review — round 2 — imo-2026-04

Field: two new approaches (population was empty). Both target the full characterization (Mulan wins iff θ = 180°/n, n ≥ 2 integer) end to end — sufficiency (explicit Mulan strategy) and necessity (Shan-Yu survival) in each file. Neither is a fragment, and their sufficiency engines are genuinely distinct routes, so they are legitimate rivals, not one proof split across slugs. I independently re-derived the key algebra and ran exact-rational checks (below).

## Verdict: remainder-forcing — APPROVE

The route is sound end to end. I verified each load-bearing step independently:

- **Cut formula (G0).** Cutting to A with t = ∠BAP ∈ (0, a) gives pieces (b, t, a+c−t) and (c, a−t, b+t) — checked by direct angle sums; the two P-angles are supplementary. Correct.
- **Forcing Lemma (G2 mechanism + validity).** Re-verified by exact rational arithmetic this round: for n = 2, 3, 5, 7, 12 on 200 random safe triangles each, the cut t = θ − r_companion at the prescribed vertex makes BOTH pieces contain a positive multiple of θ, 0 failures. The validity argument checks out by hand: n ≥ 3 gives t < θ ≤ 60° ≤ a (largest angle); n = 2 acute uses a + b ≥ 120° > 90° so t = 90° − b ∈ (0, a); n = 2 obtuse cuts to c > 90° with t = 90° − b ∈ (0°, 90°) ⊂ (0, c) and both P-slots land exactly on 90°. All sub-cases are present in the outline.
- **Descent Lemma (G1).** Strong induction on m is valid: t = θ ∈ (0, mθ), T₁ carries θ, T₂ carries (m−1)θ, and crucially the induction needs only that the kept piece has SOME angle m′θ with m′ ≤ m − 1 — it holds regardless of the companion labeling and regardless of other multiples present. m ≤ n − 1 since mθ < 180° = nθ. Bound telescopes to ≤ n − 1 total. Sound.
- **Safety Preservation (G5).** I re-did the four cases by hand: (i) a ≡ 0, (ii) b ≡ 0, (iii) c ≡ 0 each contradict safety of T; (iv) (a+c−t) + (b+t) = 180° forces 180 ≡ 0 (mod θ), impossible when 180/θ ∉ ℤ. The disjunction structure is exactly right because each piece inherits one old angle (b resp. c), not a multiple by safety. Not circular; covers every vertex choice and every t; handles θ > 90° and irrational θ uniformly.
- **Safe start (G4).** Isoceles family dodging a finite exclusion set — fine.
- **Case coverage.** Both directions present; the Direction A trichotomy (has θ / has multiple / safe) is exhaustive; θ = 90° (n = 2) is explicitly sub-cased; θ > 90° correctly folded into Direction B (180/θ ∈ (1,2) is never an integer).

Notes for the builder (not blockers):
1. In the Direction A assembly, state explicitly why the multiple created by the Forcing cut has index m′ ≤ n − 1 (any angle < 180° = nθ) before invoking Descent — this is where the ≤ n − 1 total comes from.
2. In G5, define congruence mod θ over ℝ ((x−y)/θ ∈ ℤ) BEFORE the case split, and state once that a positive angle with residue 0 is a positive multiple — the outline flags this; do it.
3. In G2, write the companion-relabeling sentence (B ↔ C swaps t ↔ a − t) so the "choose companion B" step is a legal Mulan choice via P's position.

## Verdict: descending-chain — CHANGES REQUESTED

The overall route (three-phase explicit strategy + closed family) is capable of proving the claim, and the ignition identity is verified (kept piece (x, θ−x, 180°−θ) independent of the other angles; validity sub-cases n ≥ 3 via z ≥ 60° ≥ θ and n = 2 via y < 90° both check out). But the outline contains one genuine error and one mis-stated boundary case:

1. **Phase D's monovariant as stated is FALSE (H2 — must be fixed).** "The largest multiple present drops by θ each cut" fails. Counterexample (verified by exact computation this round): θ = 15° (n = 12), T = (75°, 60°, 45°) = (5θ, 4θ, 3θ). Cut to the largest multiple 75° with s = θ and companion 60°: the kept piece p₂ = (w, v−s, u+s) = (45°, 60°, 75°) — the SAME triangle; the largest multiple did not drop, and with that companion choice Phase D loops forever. The mechanism is that u + s = u + θ can be a multiple with index ≥ k when u is itself a multiple. **Fix (cheap, keeps the phase structure):** replace the monovariant with strong induction on k for the statement "T has an angle kθ ⟹ Mulan wins within k − 1 cuts": cut to ANY vertex with angle kθ, s = θ; p₁ carries θ (kept ⟹ win at the next check), p₂ carries (k−1)θ, so the induction hypothesis applies to whichever piece survives — companion-independent, other multiples irrelevant. (Equivalently: run the induction on the minimal multiple index present.) This is exactly remainder-forcing's Descent Lemma; the builder should adopt it and drop the "largest multiple" language.
2. **H4's boundary case x − θ = θ cannot arise (restate, don't case-split).** Case (III) requires T safe, so x = 2θ is excluded a priori. What the outline actually needs — and currently only implies — is that **the grind preserves safety**: the kept piece (u, x−θ, w+θ) has residues (r_u, r_x, r_w) unchanged mod θ, all nonzero, so it is safe; hence the phase re-enters (III) or (II) and never accidentally needs case (I) mid-grind. Write that one line and the phase is airtight. (Also: the "check w + θ < 180°" worry in the watch-list is vacuous — three positive angles summing to 180° are each < 180° automatically.)
3. **Step-count bookkeeping (H5).** With the fixed Phase D, the honest bound is: grind ≤ n − 3 cuts (x < 180° − 2θ = (n−2)θ in case (III)), ignition 1 cut, descent from (n−1)θ ≤ n − 2 cuts — total ≤ 2n − 4 for n ≥ 4, and ≤ n − 1 for n ∈ {2, 3}. Any finite bound suffices for the problem; just make the arithmetic consistent.

Everything else (trichotomy exhaustiveness, ignition validity including n = 2, Direction B) is sound. The trichotomy is genuinely exhaustive: unsafe ⟹ some kθ with k ≥ 2 (k = 1 ends the game), safe ⟹ x ≠ θ.

## Shared-lemma plan (safe-piece-exists = G5 = H7) — allowed, with a condition

The outliner proposes both necessity directions import one certified lemma. Assessment: **allow it.** Reasons: (a) I verified the four-case algebra independently by hand this round — it is five lines of congruence arithmetic with no hidden geometry, the lowest-risk kind of shared line; (b) there is no genuinely different necessity route to diversify into — any Shan-Yu invariant family must be closed under the cut algebra, and the closure of "avoid θ" is exactly "avoid all positive multiples of θ" (the only proposed alternative, the doubling orbit {2^k θ}, is refuted by the recorded θ = 40°, T = (120°, 25°, 35°) counterexample — correctly killed, do not revive). Forcing two independent necessity proofs would duplicate identical mathematics with zero added robustness.

**Condition:** the lemma is short enough that each builder writes the four-case proof INLINE in its own approach file this round (so neither approach dangles on an uncertified import), and one of them additionally files `lemmas/safe-piece-exists.md` — self-contained: define ≡ mod θ over ℝ, define "positive multiple"/"safe", state the cut formula with the relabeling remark, quantify over EVERY vertex choice and every t — for the proof-reviewer to certify. From next round on, imports may replace the inline copies. This is lemma-cache reuse per the file contract, not proof-splitting: each slug still proves the whole claim.

## Dead ends confirmed (record stands)

- Doubling-orbit invariant {2^k θ}: not closed under the cut algebra (θ = 40° counterexample) — correctly excluded from the field.
- Binary-halving descent: a presentation variant of Phase D, not a rival — correctly not opened.

## Ranking

Registered both new approaches (cold start) and ranked head-to-head:

- remainder-forcing **beats** descending-chain: its crux algebra is fully verified with zero outline errors, one lean engine per direction; descending-chain shipped a false monovariant statement (H2) and has more boundary surface. Post-update Elo: remainder-forcing 1516, descending-chain 1484.

Both stay live: descending-chain's error is fixable in one paragraph and its phase structure hedges remainder-forcing's G2 (already verified, but independence is cheap insurance while the field is only two deep).

## Build instructions

- **remainder-forcing** builder: fill G0–G6 as outlined; include the three notes above; write the four-case proof inline AND file `lemmas/safe-piece-exists.md` for certification.
- **descending-chain** builder: apply fixes 1–3 above (mandatory — the H2 monovariant as written is false); write the four-case closure proof inline this round; import the lemma only after certification.

build set: remainder-forcing, descending-chain
