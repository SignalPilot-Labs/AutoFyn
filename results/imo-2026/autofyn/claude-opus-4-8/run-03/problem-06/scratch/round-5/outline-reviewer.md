# Outline Review — imo-2026-06, Round 5

Two-slug field: new `realizer-index-joint-double-count` (outliner's primary bet) and advance
`redundant-constraint-antichain` (leader, Elo 1607→1641). No copy/branch requested.

State of play: whole theorem certified-equivalent to a single magnitude bound (primes in minimal
supports ≤ C(a₁), equiv. E5″/E4-cardinality). Four framings bottomed out on one wall; R4 Collapse
theorem forbids any "realize a proper sub-support S⊊G to contradict minimality" lever. Both R5
explorers reconfirmed the wall and found no new non-forbidden lever.

---

## `realizer-index-joint-double-count` — CHANGES REQUESTED (scaffold buildable; closing lever illusory)

**Whole-attempt check: PASS.** Targets the full theorem end-to-end (magnitude bound ⇒ Crux ⇒
§4–§5 certified endgame), not a sub-lemma. Genuinely far in framing from the exhausted sub-support
route (joint system of first-realizers). Good.

**Scaffold (steps 1–4): SOUND and genuinely new.** The two-anchor witness scaffold is rigorous from
certified lemmas:
- Step 2 (Anchor collapse): fix p*∈P, strictly increasing G_k with p*∈G_k, q_k=p_max(G_k)→∞ —
  Anchor + Pigeonhole over finite P. Valid.
- Step 3 (two-anchor): H_k=private witness of q_k (E3), G_k∩H_k={q_k}; p*∈G_k, p*≠q_k ⇒ p*∉H_k;
  Anchor ⇒ H_k∩P≠∅ ⇒ H_k has p'_k∈P∖{p*}; Pigeonhole over finite P∖{p*} ⇒ fixed p**. Valid,
  non-circular, and is real reusable structural content (a two-anchor separation of a witness pair).
- Step 4: t_k=u(G_k)=∏G_k, t'_k=u(H_k)=∏H_k (R1); q_k∣(t_k−t'_k) (L3) ⇒ |t_k−t'_k|≥q_k→∞. Valid.

**Lemma J (step 5): the load-bearing gap FAILS the "genuinely independent lever" test.** The dispatch
asked me to verify HARD that J does not secretly reduce to a forbidden lever. Finding:

- **The "relational spread escapes circularity" premise is mathematically illusory.** Factor out the
  shared prime: t_k=∏G_k=q_k·A_k, t'_k=∏H_k=q_k·B_k, where A_k=∏(G_k∖{q_k}), B_k=∏(H_k∖{q_k}) are
  products of two DISJOINT prime sets (G_k∩H_k={q_k}). By unique factorization A_k≠B_k, so
  |A_k−B_k|≥1. Hence **t_k−t'_k = q_k·(A_k−B_k) is a forced nonzero multiple of q_k.** Therefore
  `|t_k−t'_k| ≤ C(a₁)` immediately gives `q_k ≤ C(a₁)` — Lemma J is equivalent to (in fact stronger
  than, since it also bounds the companions) the magnitude bound it is supposed to reduce to. The
  two-anchor congruence supplies **no decoupling**: you cannot have the spread small while q_k is
  large. The advertised "bound the difference, not the endpoints" leverage does not exist.
- **Numerical corroboration.** On real data (a₁∈{15,375,385,899,867}) ∏G≤1.45·a₁ for every minimal
  support, so |t−t'|≤~2.9·a₁ trivially — but ONLY because each endpoint is bounded (the circular
  quantity). No infinite family exists (theorem true), so J cannot be counterexample-refuted, but the
  algebra above is unique-factorization-certain, independent of data.
- **Collapse check against the four forbidden levers:** J does NOT literally invoke (b) an A_n-only
  statistic, (c) M-threshold confinement, or (d) the value-stream automaton — good. But it does NOT
  escape (a): since J ⟺ the magnitude bound, its only concrete proof routes are exactly those that
  bound ∏G, and this round's `formation-window` explorer independently reconfirmed (a different route
  than R4's anchor framing) that **every window/growth argument bounding ∏G forks into the R4 Collapse
  sub-support-realization lever.** The candidate mechanism ("if the double-count forces the
  index-intervals to overlap / share a bounded region…") is a hope, not a mechanism — a fixed finite
  resource Z/(p*·p**) has no identified reason to bound an unbounded difference q_k·(A_k−B_k), and
  neither R5 explorer nor the outliner found one.

**What to change / build scope.** Do NOT pursue Lemma J via the "relational joint-spread double-count"
as pitched — it is the magnitude bound in disguise (proven above) and its realistic routes fork to the
forbidden lever. The builder's honest, valuable deliverable this round is: (1) **certify the two-anchor
witness scaffold** (steps 1–4) as a shared lemma (`lemmas/`), genuinely new reusable structure; (2)
**record the Lemma J finding** — the last un-forked opening, on inspection, is forked/circular
(t−t'=q(A−B) forces any spread bound to be the magnitude bound; window routes collapse to R4). Per the
outliner's own contingency clause, that is a legitimate RETHINK-finding on the lever, reported honestly
rather than forcing the forbidden move. If the builder finds a genuinely resource-static double-count
that bounds q_k without any rejection-timing step, that would be a real breakthrough — but the burden is
on producing it, and I judge it unlikely given the factorization obstruction.

---

## `redundant-constraint-antichain` — CHANGES REQUESTED (leader, stays live)

Unchanged, certified-furthest-forward (Elo 1641). Complete conditional on E5″; §4–§5 endgame certified.
No new E5″ lever this round — both explorers confirmed every companion-radical attempt forks to
sub-support realization. Nominated to stay LIVE as furthest-forward, not because a lever was found. Do
NOT re-attempt the R4-forbidden sub-support closure, and do NOT reframe E5″ as "bound u(G)≤U(a₁)"
(circular, memory rule). Building it this round is low-yield; its one non-forbidden micro-target
coincides with certifying the sibling's two-anchor scaffold.

---

## Field / diversity note for the orchestrator

The field has collapsed to ONE wall (magnitude bound / E5″) across five rounds and every framing tried
(antichain endgame, anchor-partition, value-stream, formation-window, and now joint-realizer-spread).
This round's "un-forked opening" turned out, on factorization, to be forked (Lemma J ⟺ the bound; window
routes → R4 Collapse). Both R5 explorers returned NEGATIVE: no non-forbidden lever exists in the
window/growth or covering/density directions, and every candidate different-framing pole provably
collapses to the sub-support lever. Per the plateau rule, next round should NOT seed another variation
that bounds ∏G/|t−t'| (all such share the wall). The genuinely different targets not yet attacked:
(i) the covering-density explorer's numeric sharpening "at most one prime >√a₁ per large-regime support"
as a *distinct* structural statement (unproved, but not yet shown to fork), or (ii) an entirely different
top-level route to the ORIGINAL periodicity claim that never passes through the finite-alphabet crux —
though memory records that every such weaker-target reframing (A-periodic, sole-witness Q, automaton)
has so far collapsed onto the crux. Recommend the orchestrator flag this as a hard plateau and consider
whether a fundamentally new top-level framing (not another E5″ lever) can be found.

## Ranking (updated this round)

redundant-constraint-antichain 1641 (leader, live) · realizer-index-joint-double-count 1545 (new,
scaffold live / closing lever illusory) · residual-anchor-peeling 1511 (dead-end) ·
value-stream-double-freeze 1472 (dead) · monovariant-witness-descent 1460 (retired) ·
anomaly-count-terminates 1371 (dead). Stale flags cleared on leader and residual-anchor-peeling.

build set: realizer-index-joint-double-count, redundant-constraint-antichain
