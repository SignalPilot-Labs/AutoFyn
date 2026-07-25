# Proof-reviewer — Round 4 (imo-2026-06)

Two built approaches reviewed independently. Both correctly report Status `partial`; the
theorem is NOT solved (crux/E5 remains open). No overclaim in either file.

Independent simulation (greedy sequence, minimal supports over N≥4000 terms,
seeds {15,105,375,385,1155,9375}) reproduces every numerical claim used: a₁=375 anchor
fibers 𝓐_∞^{(3)}={{2,3},{3,5},{3,7,19}}, 𝓐_∞^{(5)}={{2,5,7},{2,5,19}} (matches
residual-anchor-peeling verbatim); ∏G/a₁≤1.09, ∏(G∖{p_max})/a₁≤0.20, all support-primes ≤a₁,
max|G|≤4 on all seeds. So (W)/E5″/∏G<2a₁ hold on data — but remain UNPROVED, as flagged.

---

## Approach 1: redundant-constraint-antichain (§12 realizer-value pincer)

**Scores.** Correctness 10/10 (of what is claimed proved), Rigor 9/10, Progress 8/10.

**Load-bearing new steps, re-derived from scratch:**

- **R1** (every G-supported m≥a₁ is a term; u(G)=∏G when ∏G≥a₁). Re-derived: E2(⇒) certified ⟹
  G meets every member of 𝓐_∞; F(m)=G ⟹ m meets every member ⟹ m∈A; E1 certified ⟹ m is a
  term. D_G's least element is ∏G; when ∏G≥a₁ it is the least term realizing G. **Correct,
  non-circular** (uses only certified E1/E2). VALID.
- **R2** (u(G)≥∏G≥P_{|G|}; ∏G<X ⟹ |G|≤K(X)). Re-derived: u(G) divisible by all of G ⟹ ≥∏G;
  majorization p_i≤q_i (i-th smallest prime of G) ⟹ ∏G≥P_{|G|}; monotonic K. **Correct.**
  Independently confirmed ∏G≥P_{|G|} numerically. VALID. (This is the aimo-0447 lower jaw,
  correctly transplanted and re-proved, not merely cited.)
- **Prop 12.A** (∏G<a₁ ⟹ |G|≤K(a₁)). Immediate from R2. **Genuinely a fully-closed infinite
  subclass with NO open step.** VALID — this is real unconditional content on {∏G<a₁}.
- **Prop 12.B** (window (W): ∏(G∖{p_max})<a₁ ∀ minimal G with |G|≥2 ⟹ sup|G|≤1+K(a₁) ⟹ E5 via
  certified E4 ⟹ theorem). Re-derived: apply R2 to the (|G|−1)-prime set G∖{p_max}. **Correct,
  sound reduction, non-circular** — it is an unconditional IMPLICATION (W ⟹ E5), and (W) is left
  as an explicit hypothesis, not assumed proved. VALID.

**Residual gap honesty.** (W) holds automatically when ∏G<a₁ (redMax≤∏G<a₁), so the sole open
content is **E5″**: minimal G with ∏G≥a₁ has ∏(G∖{p_max})<a₁. This is stated as an explicit OPEN
GAP (§12.3, §12.4), with the precise wall named (a proper sub-support S=G∖{p_max} is not a
transversal — private witness H_{p_max} blocks it — so ∏S∉A and is not cheaply realizable). The
upper jaw of the pincer (an a₁-only ceiling on u(G)=∏G) is honestly the missing step. **No
overclaim: Status `partial` is correct.** The theorem is NOT solved because E5″ is not closed.

**Certified this round:** `lemmas/realizer-value-pincer.md` (R1, R2, Prop 12.A, Prop 12.B).

**True Status: partial.** Verdict: **CHANGES REQUESTED**. Gap to close next round: **E5″** —
prove ∏(G∖{p_max})<a₁ for every minimal support with ∏G≥a₁ (or the sufficient ∏G<2a₁). The
pincer's upper jaw is the target; realizability + growth (a_n=Θ(n)) + gap bound are the tools in
hand, clutter structure alone is provably insufficient (E4/E5 tight abstractly).

---

## Approach 2: residual-anchor-peeling (NEW pole)

**Scores.** Correctness 10/10, Rigor 9/10, Progress 5/10 (as an independent route: collapses; but
the collapse is itself a certified negative result + one promotable lemma).

**Scaffold, re-derived:**

- **Lemma A (Partition).** α(G)=min(G∩P) well-defined (Anchor L1 ⟹ G∩P≠∅; P finite ordered).
  Fibers partition 𝓐_∞; Π=⋃_{p∈P}Q_p finite union ⟹ Π finite ⟺ each Q_p finite ⟺ each fiber
  finite (Q_p finite ⟺ fiber = family of subsets of finite set). **Rigorous; map well-defined,
  terminating, into finite P.** VALID — a genuine new unconditional equivalent form of the crux.
- **Lemmas B, C, D.** B trivial/correct. C small-part pigeonhole over ≤2^{π(M)} values of
  G∩{primes≤M} — correct; p*≤M ⟹ p*∈S₀. D: infinitely many distinct large primes among an
  infinite antichain 𝓗 of finite sets (else ⋃𝓗 finite ⟹ 𝓗 finite); distinct G_k extractable.
  **All sound.**

- **Proposition (Collapse) — the critical claim, verified as a THEOREM.**
  Part 1: common core B={p*}∪S₀ has B⊊G ∀G∈𝓗; if B were a transversal, certified Lemma 11.0 ⟹
  B⊇G₀∈𝓐_∞ ⟹ every G∈𝓗 has G⊇G₀ ⟹ antichain forces G=G₀ ⟹ 𝓗 finite, contradiction. So B is
  **not** a transversal ⟹ no dominating B-support term is realizable (E2 realization). **Correct.**
  Part 2: B not transversal ⟹ ∃W∈𝓐_∞, W∩B=∅; every G∈𝓗 meets W (E2⇒) in W∖B; pigeonhole ⟹
  r∈W∖B in infinitely many G ⟹ B'=B∪{r}, 𝓗' infinite — **exactly one step of the certified E4
  chain-descent**, seeded at B. Iterating ⟹ cores of unbounded size iff members unbounded ⟺
  sup|G|<∞ = E5, with p* contributing no independent bound. **Re-derived both parts: correct.**

  This is a valuable **certified negative result**: the anchor-partition pole provably CANNOT
  bypass the shared wall via a common non-transversal sub-support — it reduces verbatim to E5. The
  builder reports this honestly ("collapse rather than re-deriving E5").

**Certified this round:** `lemmas/anchor-partition.md` (Lemma A + sub-support non-transversality
guardrail: any plan to "force a dominating common sub-support term" is provably an attack on E5,
not a bypass).

**True Status: unsolved as an independent pole** (partial content: Lemma A is real, but it is a
lateral reformulation like E4, and the pole is proven to share the wall). Verdict: **RETHINK** —
the anchor-partition framing collapses onto E5, so it cannot advance the problem as an independent
route; it goes back to the outliner. The salvage (Lemma A equivalent form + guardrail) is certified
and reusable. The file's own conclusion agrees; no overclaim.

---

## Goal Progress (raw, for state file)

- Status: **partial** (unchanged flip; real reduction progress).
- Ranking (Elo, post-record): redundant-constraint-antichain **1607.4** (advanced, LIVE, leader,
  expanded=4); residual-anchor-peeling **1530.1** (dead-end, expanded=1, proven-collapse pole).
- redundant-constraint-antichain: 4 new certified lemmas (R1,R2,Prop12.A,12.B). E5 reduced to
  single residual **E5″** (∏(G∖{p_max})<a₁ for ∏G≥a₁); subclass ∏G<a₁ FULLY closed (|G|≤K(a₁)).
  Sole open gap = E5″ (⟺ a₁-only ceiling on u(G)=∏G). CHANGES REQUESTED.
- residual-anchor-peeling: RETHINK. Proven-collapse to E5 (certified). Salvage: Lemma A (anchor
  partition, new equivalent form) + sub-support non-transversality guardrail, both certified.
- New certified lemma files: `lemmas/realizer-value-pincer.md`, `lemmas/anchor-partition.md`.
- Plateau note persists: E5/crux unclosed 4 rounds; both R4 poles reduce to the same wall
  (E5″/E5). Both antichain-family reformulations (E4, Lemma A, pincer) are proven-equivalent
  lateral moves. The one un-attacked lever is the pincer's UPPER jaw (a₁-only ceiling on u(G)=∏G
  via realizability+growth) — the only route not yet shown to collapse. Persistence-mechanism
  framing (why a shared large witness prime cannot sit in unboundedly many mutually-blocking
  supports) still not attacked head-on.

---

**Verdicts:**
- `redundant-constraint-antichain: CHANGES REQUESTED`
- `residual-anchor-peeling: RETHINK`
