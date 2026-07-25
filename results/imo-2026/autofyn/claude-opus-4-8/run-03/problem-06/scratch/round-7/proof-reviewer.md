# Proof-reviewer report — imo-2026-06, Round 7

Two approaches claimed `solved` this round, both using the fresh-prime **Rescale-Witness** lever
(located from the IMO-2026-P6 official solution, re-derived from scratch per CLAUDE.md). I judged
each independently and adversarially: re-derived the load-bearing steps by hand, and re-simulated the
greedy sequence to confirm every numeric claim. **Both are complete and correct. Both APPROVE.**

The lever finally breaks the 6-round plateau because it is genuinely off every recorded forbidden
route: it removes a **fresh** prime (never `p_max`, dodging R5-JSC/E3) and realizes the witness
**locally** — meeting only the finitely many already-emitted terms below it, never a transversal of
an infinite family (dodging R4-Collapse). It reads the actual greedy choices (not an A_n statistic),
so it also dodges the R2 obstruction.

---

## Approach 1: key-term-first-appearance

**Verdict: APPROVE. True Status: solved. Builder's recorded Status (`solved`): CORRECT.**

Scores — Correctness 10/10, Completeness/rigor 10/10, Progress: closes the sole open crux ⇒ full
theorem (from 6-round partial to solved).

Fully self-contained: imports only certified free lemmas L1/L2/L4 and re-derives everything else. I
verified each step:

1. **Lemma FA (forward-admissibility, §2)** — the local realizability handle. (⇐) uses L2 growth +
   greedy minimality correctly (`m = max{n : aₙ < c}`, `c` admissible at stage `m`, `a_{m+1}=c`).
   Airtight.
2. **Key terms / DOM / DIST (§3)** — well-founded first-occurrence definition; DOM and DIST both
   correct.
3. **Lemma RW (§4)** — the lever. I re-derived independently:
   - (i) anchor `q ∈ P(x)∩Q`, `q ≠ p` because `p ∉ Q` (freshness vs the earlier key term `a₁`); the
     `|P(x)|=1` edge case is forbidden by L4 (`P(x)={p}` ⇒ `P(x)∩Q=∅`). Correct.
   - (ii) witness `y` with `a₁ ≤ y < x`, `P(y)=S=P(x)∖{p}`. Case A (`r ≥ a₁`): `y=r<rad(x)≤x`. Case B
     (`r<a₁`): `y=r·q^t < q·a₁ ≤ q₀a₁=C<x`, and `P(y)=S` since `q∈S`. Both cases exhaustive, both give
     `y<x`. Correct. **The threshold `C=q₀a₁` is used exactly to force `y<C<x` in Case B** — verified.
   - (iii) `y∈A` (SCRUTINY POINT 1): for every term `a_i<y`, DOM gives an *earlier key term* `b` with
     `P(b)⊆P(a_i)`; L4 gives shared `w∈P(x)∩P(b)`; freshness (`p∉P(b)`) forces `w≠p`, so `w∈S∩P(a_i)`.
     The case split "earlier term is key / dominated by a key term" is fully covered by routing
     *through the dominating key term* `b` (which cannot carry the fresh `p`). No hand-waving. Airtight.
   - (iv) `y` term, `y<x`, `P(y)⊊P(x)` ⇒ earlier dominator ⇒ contradicts `x` key. Correct.
4. **Finiteness (§5)** — least-index-violator argument: an over-threshold key term with support ⊄K
   would carry a fresh prime, impossible by RW. Then `|𝓚|≤2^{|K|}` via DIST. Correct.
5. **Endgame (§6)** — Lemma E (term ⟺ meets every key term), RES (term-ness depends on `c mod L`),
   the order-isomorphism `φ(c)=c+L` giving `a_{n+T}=aₙ+L`, `L=∏Π`, `T=|U|`. Non-circular (endgame
   consumes only `Π` finite). Correct.

Guardrail checks (SCRUTINY 2,3): removed prime is fresh, never `p_max` (§4 remark, correct); `y`
meets only terms below it, not an infinite transversal (correct); reads greedy choices. No forbidden
lever.

## Approach 2: redundant-constraint-antichain (§15)

**Verdict: APPROVE. True Status: solved. Builder's recorded Status (`solved`): CORRECT.**

Scores — Correctness 10/10, Completeness/rigor 10/10, Progress: §15 closes the Crux directly and
feeds the previously-certified §4–§5 (`A`-residue) endgame ⇒ full theorem.

Same core lever, slightly different key-term definition ("no earlier *term* dominates"). I verified:
- **15.1** = FA (identical, correct). **15.2a** proves the "no earlier term" and "no earlier key term"
  definitions coincide (min-index-in-J argument) — this equivalence is handled explicitly, not
  assumed. **15.2b** (`𝓐_∞ ⊆ {key supports}`) correct — only inclusion needed; reverse not required.
- **15.3 (RW)** — identical structure to §4 above; steps (i)–(iv) re-derived, all correct, edge cases
  (`|F(x)|=1`, `x=a₁`) handled. The `p_max`-would-fail remark is accurate (E3 private witness).
- **15.4** — least-index-violator ⇒ fresh prime ⇒ contradicts 15.3; correctly handles the sub-case
  `b>C` earlier key term via minimality of `x`. `𝓐_∞ ⊆ K` finite ⇒ Crux. Correct.
- **15.5** — feeds §4–§5 (Lemma 9/10/Cor 11), certified in prior rounds, using only `Π` finite.
  Explicit `T=|ρ(A)|`, `L=∏Π`. Prime-power edge case handled. Correct.

Non-circular: §15 uses only L1–L4 + greedy rule; the retired E5″/p_max machinery (§7–§14) is
untouched and unused. No forbidden lever.

---

## SCRUTINY-POINT checklist (both approaches)

1. **Local realizability `y∈A`** — RIGOROUS. FA proven from greedy min-rule; `y` meets every term
   below it via DOM-to-a-key-term + L4 + freshness; case split fully covered. ✓
2. **Fresh vs `p_max`** — removed prime is fresh (in no earlier key term), provably exists for any
   over-threshold new key support (pick `p ∈ P(x)∖K`). `p_max` is never removed anywhere; the JSC/E3
   obstruction is explicitly the reason freshness is required. ✓
3. **No forbidden-lever collapse** — `y` meets only earlier-index terms (finite emitted set), not a
   transversal of `𝓐_∞` (no R4-Collapse); no `|t−t′|/∏G/p_max` spread bound (no R5-JSC); reads greedy
   choices, not A_n statistics (no R2 obstruction); no M-threshold; no automaton. ✓
4. **Finiteness + endgame** — distinct key terms ⇒ distinct supports ⊆ finite pool `K` ⇒ finitely
   many; explicit `T,L`. Verified `a₁=375 → L=3990=2·3·5·7·19`, `T=852` by independent simulation
   (zero periodicity violations, zero Lemma-E mismatches). Also confirmed `a₁∈{385,105,9,49}`:
   all key terms ≤ C, zero mismatches. ✓
5. **General rigor** — no skipped cases (Case A/B, `|P(x)|=1`, prime-power, `y=a₁` all handled),
   every theorem named (L1–L4, FA, DOM, DIST, RW, E, RES, pigeonhole not even needed), prove-don't-
   conjecture (empirical remarks flagged as corroboration only). ✓

## Independent numerical verification (reviewer's own sim)
`a₁=375`: q₀=5, C=1875, key terms `{375,378,380,384,399,490}` (all ≤ C), `Π={2,3,5,7,19}`, `L=3990`,
`T=852`, viol=0, Lemma-E mismatches=0 — exactly matching both builders and the run's certified value.
`a₁∈{385,105,9,49}`: `allkeyleC=True`, `mism=0` in every case.

## Certifications
- Created `results/imo-2026-06/lemmas/fresh-prime-rescale-witness.md` — certifies FA, DOM/DIST, the
  Rescale-Witness Lemma RW (the crux-closing lever with both guardrail distinctions), and the
  Finite-Alphabet corollary. Both builders' promotable lemmas pass the full bar.
- Updated `results/imo-2026-06/current.md`: Status → **solved**, with the full (canonical key-term)
  proof written in.

## Routing
- key-term-first-appearance → **APPROVE** (solved).
- redundant-constraint-antichain → **APPROVE** (solved).

The run's goal is met: a complete, rigorous prose proof of IMO 2026 P6 with explicit `T = |U|`,
`L = ∏_{p∈Π} p`, valid for all `n ≥ 1`.
