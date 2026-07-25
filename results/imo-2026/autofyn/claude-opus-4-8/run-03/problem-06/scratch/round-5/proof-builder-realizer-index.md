# Proof-builder report — realizer-index-joint-double-count (Round 5)

Wrote: /home/agentuser/repo/results/imo-2026-06/approaches/realizer-index-joint-double-count.md
Status: **partial** (scaffold proved; closing lever proved illusory).

## What I proved (rigorous, from certified lemmas only)

**Two-Anchor Witness Separation (TAS) — steps 1–4, NEW and certifiable.**
From the contradiction hypothesis `sup_{G∈𝓐_∞}p_max(G)=∞`:
- Step 1–2: Anchor L1 gives `G∩P≠∅`; Pigeonhole over finite `P` fixes `p*∈P` with `p*∈G_k`,
  `q_k=p_max(G_k)→∞`, and (discarding `q_k≤p*`) `|G_k|≥2`, `p*<q_k`. This also disposes of the
  `|G|=1` case cleanly (an anchored support with unbounded max prime is not a single prime).
- Step 3: E3 private witness `H_k` with `G_k∩H_k={q_k}` forces `p*∉H_k`; Anchor L1 then forces a
  second prime of `P` in `H_k`, distinct from `p*`; Pigeonhole over finite `P∖{p*}` fixes
  `p**∈P∖{p*}` with `p**∈H_k`. Net: `p*∈G_k∖H_k`, `p**∈H_k∖G_k`, `q_k` the unique shared prime.
- Step 4: R1 makes `t_k=u(G_k)`, `t'_k=u(H_k)` genuine distinct terms; Distance–prime L3 gives
  `q_k∣(t_k−t'_k)`, so `|t_k−t'_k|≥q_k→∞`.
Every step justified from certified Anchor L1 / E3 / R1 / L3 / Pigeonhole. Proposed as shared
lemma **TAS**.

## What remains gapped — and why it cannot be closed as pitched

**Lemma J (a₁-only upper bound on the spread) is ILLUSORY.** I reproduced the reviewer's
factor-out argument rigorously as a certified NEGATIVE result (**JSC**):
- For large `k`, `∏G_k≥q_k≥a₁` so R1 gives `t_k=∏G_k` (squarefree), and likewise `t'_k=∏H_k`.
- `t_k=q_k·A_k`, `t'_k=q_k·B_k` with `A_k=∏(G_k∖{q_k})`, `B_k=∏(H_k∖{q_k})` over DISJOINT prime
  sets (because `G_k∩H_k={q_k}`); `p*∣A_k` but `p*∤B_k`, so `A_k≠B_k`, `|A_k−B_k|≥1`.
- Hence `t_k−t'_k=q_k(A_k−B_k)` is a nonzero multiple of `q_k`, so `|t_k−t'_k|≥q_k`, and any
  `a₁`-only bound `|t_k−t'_k|≤C(a₁)` immediately yields `q_k≤C(a₁)` = the magnitude bound itself.
No relational decoupling exists; window routes to J fork into the R4-forbidden
sub-support-realization lever. This confirms the outline-reviewer's verdict: the last un-forked
opening is, on inspection, forked/circular. Recorded honestly; no E5″ overclaim.

## For the reviewer to certify
- **TAS** (Two-Anchor Witness Separation) — new reusable structural lemma, unconditional.
- **JSC** (Joint-Spread Collapse) — certified negative result: joint-spread lever ⟺ magnitude
  bound. Both stated verbatim in the approach file's "## Promotable lemmas".

## Spec concerns
None. All invoked results (Anchor L1, E3, R1, R2, Distance–prime L3, Reduction/E4, Pigeonhole)
are certified in `lemmas/` and named at each use. The scaffold does not assume the Crux.

## Diversity note
The joint-realizer-spread framing — the field's last un-forked pole — is now certified forked.
Every ∏G / |t−t'| bounding route shares the one wall. Next round should not seed another
spread/window variation; a genuinely different top-level route (or the covering-density
"≤1 prime >√a₁ per large support" structural claim, not yet shown to fork) is the only
non-repeating direction.
