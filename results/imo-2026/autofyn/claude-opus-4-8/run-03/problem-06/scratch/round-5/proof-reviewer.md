# Proof-reviewer report — imo-2026-06, Round 5

Two approaches reviewed independently. Neither is `solved` (E5″ is the open gap, as expected).
Verdicts: `redundant-constraint-antichain` → CHANGES REQUESTED (partial); `realizer-index-joint-double-count`
→ RETHINK (unsolved as a framing; salvage certified).

---

## Approach 1: realizer-index-joint-double-count  →  RETHINK

**True Status: unsolved as a top-level route** (the closing lever is self-certified illusory).
Builder recorded Status `partial` and self-flagged the closer as forked — that is honest, but the
correct routing verdict is RETHINK: the approach's own new result (JSC) proves its central mechanism
is logically equivalent to the shared crux. This is the classic single-gap-trap / collapse pattern
(cf. value-stream R3, residual-anchor-peeling R4).

### Load-bearing steps re-derived independently

**TAS (two-anchor witness scaffold), steps 1–4 — CORRECT and rigorous.** I re-derived each step
from the certified lemmas (`free-lemmas.md` L1/L3, `enumeration-and-transversal.md` E3,
`realizer-value-pincer.md` R1):
- Step 1–2: L1 gives `G∩P≠∅`; Pigeonhole over finite `P` fixes `p*`; subsequence of `p_max→∞`
  still `→∞`; discarding `q_k≤p*` gives `q_k>p*`, `|G_k|≥2`. Valid.
- Step 3: E3 on `(G_k,q_k)` gives `H_k`, `G_k∩H_k={q_k}`; `p*∉H_k` (else `p*=q_k`); L1 forces
  `H_k∩P≠∅`, and since `p*∉H_k` the prime lies in `P∖{p*}`; Pigeonhole over finite `P∖{p*}` fixes
  `p**`. **This second-anchor pigeonhole is valid** — but it silently needs `|P|≥2` (`a₁` not a
  prime power). The realizer-index file does not state that caveat at Step 3; the sibling antichain
  file §13.2 does, and closes `|P|=1` via the prime-power lock (`𝓐_∞={{p*}}` finite). I verified the
  `|P|=1` disposal: if `P={p*}`, every support meets `{p*}`, `{p*}` is realizable and ⊆-minimal, so
  `𝓐_∞={{p*}}` — Crux holds outright. So no generality is lost. I folded the caveat into the
  certified statement.
- Step 4: R1 makes `t_k=u(G_k)`, `t'_k=u(H_k)` genuine distinct terms; `F(t_k)∩F(t'_k)={q_k}` ⇒
  `q_k∣t_k,t'_k` ⇒ (L3) `q_k∣(t_k−t'_k)`, `|t_k−t'_k|≥q_k`. Valid.

**JSC (Lemma J is illusory) — CORRECT negative result.** For large `k`, `∏G_k≥q_k≥a₁` so R1 gives
`t_k=∏G_k`, `t'_k=∏H_k`; factoring the shared prime `t_k−t'_k=q_k(A_k−B_k)`, `A_k=∏(G_k∖{q_k})`,
`B_k=∏(H_k∖{q_k})` over disjoint prime sets, `p*∣A_k`, `p*∤B_k` ⇒ `A_k≠B_k`, `|A_k−B_k|≥1`. Hence
`|t_k−t'_k|` is a nonzero multiple of `q_k`, and any `a₁`-only spread bound entails the magnitude
bound. I verified the identity numerically on `a₁=375`, `G={2,5,19}`, `H={3,7,19}`:
`190−399=−209=19·(10−21)=q·(A−B)`, `|diff|=209≥19`. Correct.

### Why RETHINK, not CHANGES REQUESTED

The slug's *entire* reason to exist is the joint/relational "bound the difference not the endpoints"
double-count (Lemma J). JSC proves — from the slug's own machinery — that this lever is exactly the
magnitude bound in disguise. So the framing has no independent leverage over the shared wall; it must
go back to the outliner for a genuinely different top-level route. Per role-memory rule (round 3),
an approach whose own new result proves it is logically equivalent to the shared crux is routed
RETHINK and its outcome recorded `dead-end`, with salvage certified.

### Certification
- **TAS** — CERTIFIED (with the `|P|≥2` caveat made explicit and the `|P|=1` prime-power disposal
  added). Written to `lemmas/two-anchor-scaffold.md`.
- **JSC** — CERTIFIED as a concrete negative guardrail (the identity + "spread bound ⟹ magnitude
  bound"). I **rejected** the broader slogan "every concrete window route forks to the R4-forbidden
  sub-support lever" as a theorem — it has no formal content (no definition of "every route"); it is
  recorded as heuristic only, companion to the R4 Collapse guardrail. (Role-memory rule R2:
  certify the concrete witness, not the universal slogan.)

Scores — Correctness 5/5 (TAS + JSC both valid); Rigor 4.5/5 (the `|P|=1` caveat was implicit in
this file, repaired in certification); Progress: real but self-negating — new certifiable structure,
zero net movement on E5″, framing proven exhausted.

---

## Approach 2: redundant-constraint-antichain  →  CHANGES REQUESTED

**True Status: partial (correct, no overclaim).** Matches the builder's recorded Status.

### Consolidation §13 checked
- **§13.1 reduction chain** — every link verified against the certified lemmas:
  No-transient/Endgame (`no-transient-fixed-successor.md`), E1/E2/E3 (`enumeration-and-transversal.md`),
  E4 (`size-bound-reduction.md`), R1/R2/Prop 12.A/12.B (`realizer-value-pincer.md`). The chain
  `No-transient ⇒ E1/E2/E3 ⇒ Crux⟺E4 ⇒ R1/R2 ⇒ Prop12.A(∏G<a₁ closed) / Prop12.B(W) ⇒ E5″` is
  correct and non-circular; the only open arrow is `E5″ ⟹ E5`. The theorem is genuinely
  certified-equivalent to E5″. No overclaim.
- **§13.2 two-anchor scaffold** — same object as the sibling's TAS, re-derived here, correctly
  labelled auxiliary (NOT a closer of E5″), with the `|P|≥2` caveat and prime-power disposal stated.
  Certified (shared file `lemmas/two-anchor-scaffold.md`).
- **§13.3 negative findings** — the formation-window fork, the density/covering certified dead end,
  and the joint-spread illusion are all recorded honestly. The "at most one prime `>√a₁` per
  large-regime support" numeric observation is correctly flagged CONJECTURE, unproved, not used.

### Rigor audit
No skipped case, no hand-waving, no conjecture-as-fact. The single open gap E5″ is stated explicitly
as a GAP throughout. `## Full proof` remains conditional on the Crux, exactly as the file declares.

### The gap (for the next round)
**E5″ (OPEN):** every ⊆-minimal support `G` with `∏G ≥ a₁` satisfies `∏(G∖{p_max}) < a₁`
(equiv. `p_max > ∏G/a₁`; sufficient stronger form `∏G < 2a₁`). This is the sole missing step; the
complementary regime `∏G < a₁` is fully closed (Prop 12.A). Both R5 explorers and both builders now
report the E5″ wall is structural across all five framings tried (window/growth forks to the
R4-forbidden sub-support lever; density/covering is the certified obstruction; joint-spread is the
JSC illusion). Recommendation for the outliner: seed ≥1 approach on a genuinely different TOP-LEVEL
framing — not another `∏G`/`|t−t'|` spread or window lever, all of which share this wall.

Scores — Correctness 5/5; Rigor 5/5 (honest partial, gap precisely located); Progress: consolidation
+ one new certified auxiliary lemma (TAS), no gap closed.

---

## Goal Progress (for run_state.md)

- **Status: partial** (unchanged). Leader `redundant-constraint-antichain` remains certified
  furthest-forward; whole theorem certified-equivalent to the single open inequality **E5″**.
- **Post-record Elo ranking:** redundant-constraint-antichain **1640.7** (partial, LIVE, leader);
  realizer-index-joint-double-count **1544.8** (dead-end, RETHINK, salvage certified).
- **Certified this round:** `lemmas/two-anchor-scaffold.md` — TAS (two-anchor witness separation,
  unconditional, `|P|≥2`) + JSC (joint-spread collapse guardrail: `t−t'=q(A−B)`, `A≠B` ⇒ any
  `a₁`-only spread bound = magnitude bound). Rejected the universal "every route forks" slogan as
  non-formal; certified only the concrete negative.
- **Open:** E5″ — `∏(G∖{p_max}) < a₁` for minimal `G` with `∏G ≥ a₁`. Wall now confirmed structural
  across all `∏G`/`|t−t'|`/window/density framings. Next round needs a genuinely different top-level
  route (not another spread/window lever).
- **Routing:** redundant-constraint-antichain → CHANGES REQUESTED (stays live);
  realizer-index-joint-double-count → RETHINK (back to outliner).
