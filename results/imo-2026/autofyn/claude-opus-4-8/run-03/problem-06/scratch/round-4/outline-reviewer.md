# Outline review — imo-2026-06 (R4)

Everything through the certified endgame (E1–E4 + no-transient) is done and correct; the whole
field shares the single crux **Π finite ⟺ sup|G|<∞ (E5)**. I numerically re-derived the minimal
supports and their minimal realizers for a₁∈{375, 9375, 1155, 15015, 385} before ruling (sim in
`/tmp/sim.py`). Key data:

```
a1=9375 M=15 P={3,5}: minimal supports and minimal realizers
    {3,5}         realizer 9375  (=a1)
    {2,5,7,67}    realizer 9380  (=a1+5)  radical 4690, ONE prime>M (67)
    {3,67}        realizer 13467          radical 201,  ONE prime>M (67)
    {2,3}  10368   {3,7} 11907
a1=375  M=15 P={3,5}:  {2,5,19} realizer 380 (=a1+5), {3,7,19} realizer 399, {2,5,7} 490 ...
```

Two facts that drive the review: **(a)** the minimal realizer `u` of even a large support is
`≈ a₁` (9380 = a₁+5 for the size-4 support), NOT `≈ ∏G` "late by growth"; supports form *early*.
**(b)** every tested support has **at most one** prime `> M` (67 in the size-4 support for 9375;
19 for 375) — Opening 4's cheap-kill is not refuted by current data, worth a builder check.

---

## redundant-constraint-antichain — CHANGES REQUESTED (advance, build)

Standing leader (Elo 1607). E1–E4 + endgame certified; a whole-problem attempt with one honest
gap (E5). Sound to build. But the outliner's **E5-★ "minimality-preemption" framing is a
mislabel, not a new lever**, and its watch-out is inverted. Builder must be told this:

1. **"Preemption" is logically equivalent to E5, not a mechanism for it.** The stated event —
   "a term with support `⊊ G` occurs before `u`, contradicting `G∈𝓐_∞`" — can *never* occur for a
   minimal `G`: any term's support is a transversal (L4 + domination), and a transversal `⊊ G`
   contradicts `G` being a minimal transversal (certified E2⇒). So "preemption occurs" ⟺ "`G` is
   not minimal" ⟺ E5 itself. The chain "`r` large ⇒ `∏G` huge ⇒ `u` late by growth ⇒ sub-support
   term appears" has an **unjustified middle step** and its premise "`u` late" is numerically false
   (realizers sit at `a₁+5`). This is a relabel of the gap, supplying no independent handle.

2. **The outliner's watch-out is backwards.** It says *"do NOT try to bound the G-realizer
   directly; use preemption."* In fact bounding the realizer value is the **honest, non-circular**
   target: `∏G ≤ u ≤ U(a₁)` forces `r` bounded (primorial grows super-exp), and it is *not* circular
   — it is the R2 target `∏G < 2a₁` restated, strongly supported numerically (every realizer above
   ≈ a₁; `∏G=4690 < 2·9375`). "Circular" was the wrong word: `u` and `∏G` being comparable makes the
   value-bound and size-bound *equally hard*, not circular. The genuine open content is an **a₁-only
   UPPER bound on the minimal realizer** `u` — exactly the aimo-0447 product-vs-window pincer the
   explorer flagged (`t ≥ ∏G` present; the matching upper bound on `t` is missing).

3. **Where non-vacuous, "preemption" = the R3 ERW exchange argument that already stalled** (§10:
   "the greedy rule chose a q-multiple over the next multiple of M because M's multiple failed some
   G'"). The missing quantitative lemma is the **per-window support-independence** bound (bound the
   number of *simultaneously active* minimal supports in an M-window, n-independently). That is the
   real E5; the builder should either produce it (via the aimo-0447 pincer on the realizer value) or
   report the same wall — do not re-narrate "preemption."

The aimo-0447 distinctness pincer *is* applicable (private witnesses give distinct large primes
whose product lower-bounds a realizing term); it is missing only the matching upper bound. Build to
close E5 via the realizer-value bound, not via the preemption relabel.

## residual-anchor-peeling — APPROVE (new persistence pole, build)

Registered (Elo 1530). A genuinely different *route* to Π-finite and the mandated persistence-
mechanism pole. Verified:

- **Non-circular / well-founded.** Step 1 is a *finite partition* `𝓐_∞=⊔_{p∈P}𝓐_∞^{(p)}`, not an
  iterated peel; "termination in |P| rounds" is just the finiteness of `P` (Anchor makes `α(G)`
  total). It explicitly does **not** peel infinite-fiber primes (the `11 | ` inf-many-terms dead end
  for a₁=105 is correctly excluded). Confirmed on data: for 9375, `α`-fibers are 3↦{{2,3},{3,5},
  {3,7},{3,67}}, 5↦{{2,5,7,67}} — well-defined, and `Q_p` may share large primes across fibers
  (67 in both) with no ill effect. Sound.
- **Not a verbatim collapse onto sup|G|.** Step 5 targets `|Q_{p*}|` (count of distinct large primes
  in one anchor fiber), not `sup|G|`. These are equivalent only *through* E4; the direct attack is on
  the count/obstruction shape `{p*}∪S₀∪{q_k}, q_k→∞` — which the explorer confirms is the
  *empirically dominant* failure mode ("many small supports, not one giant"). Localizing to a fixed
  `{p*}∪S₀` is a real, cleaner combinatorial target. Not a collapse.

**But flag (shared-wall risk — for the orchestrator, plateau round 4).** Step 5's load-bearing move
(5a) is "E2⇐ realizability forces a common `{p*}∪S₀`-support term early, preempting cofinitely many
`G_k`." Since `{p*}∪S₀` is a proper sub-support of the `G_k`, it is (by the same E2⇒ argument above)
**not a transversal**, so forcing its realization is the *same quantitative wall* as antichain's E5:
"force a common small-support term via realizability + growth." The two poles differ in framing and
target quantity (size vs per-anchor count) but **share this core lever**. Diversity is real but
partial; if both stall on it next round, the field has hit the single-gap trap again and the
orchestrator should seed a pole that does *not* route through "force a non-transversal small support
to be realized" (e.g. the aimo-0421 recursive-dichotomy or the aimo-0447 Σ1/p² covering restricted
to minimal-support primes — both surfaced by the explorers, neither yet tried).

Builder must keep step 5 honest: (5b) packing alone is provably insufficient (sparsity ≠ finiteness,
recorded dead end); the content must genuinely use the shared anchor `p*` + E2⇐. If step 5 reduces
verbatim to "bound sup|G|" with no use of `p*`, report collapse rather than re-deriving E5.

## monovariant-witness-descent — RETIRE (do not build)

Concur with the outliner. K-real refuted R3 (a₁=375: companions {2,5},{3,7} never realized, supports
persist via shared witness 19). Every non-circular re-plan of it *is* residual-anchor-peeling, so
building both is the single-gap trap. Its certified assets (Lemmas A/B, obstruction) survive in
`lemmas/monovariants-and-obstruction.md` and are reusable. Ranked below the two live poles
(Elo 1474, dead-ended vs both).

## value-stream-double-freeze / anomaly-count-terminates — remain dead

Automaton collapses to crux (R3); M-threshold confinement false (R1). Ranked at the bottom.

---

build set: redundant-constraint-antichain, residual-anchor-peeling
