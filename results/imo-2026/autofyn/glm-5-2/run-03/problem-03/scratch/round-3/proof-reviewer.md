# proof-reviewer — round 3 — imo-2026-03 (Chu-Han war)

First review of the round-2 builds (round 2 was force-interrupted before the reviewer ran). Reviewed 3 approaches with new round-2 content; `dyadic-induction` is being rebuilt in parallel this round and is NOT re-reviewed (its round-1 `advanced`/CHANGES REQUESTED stands, pending next pass). All Python checks bounded (≤ 300k trials, < 5s each). I judged the written proof; computation was a red-flag finder.

## 1. pairing-charging — CHANGES REQUESTED (Status: partial)

**Outcome: `advanced`** — round-2 build genuinely advanced the upper bound: closed n=2 rigorously and proved a general-n lemma (equal-halve-n-largest) that closes an entire regime.

**Verification of the round-2 "PROVED" claims (all PASS):**

- **n=2 upper bound CLOSED (the dispatch's tractable milestone).** The 4-member menu `{c, |2a−1|, a−b, b−c}` (each achieved by an explicit ≤ 2-mark Xiang strategy: A=equal-halve a,b → D=c; B′=barely-split a into b+(a−b) → D=|2a−1|; C1=equal-split a → D=b−c; C3=equal-split c → D=a−b) satisfies `min ≤ 1/7`. The 2-case contradiction is airtight:
  - Case B+ (`a > 4/7`): `b > 2/7` (from `b−c > 1/7` and `c > 1/7`) ⇒ `a+b+c > 4/7+2/7+1/7 = 1`. ✓
  - Case B− (`a < 3/7`): `b < a−1/7 < 2/7` (from `a−b > 1/7`); `b+c = 1−a > 4/7` ⇒ `c > 4/7 − b > 2/7`, contradicting `b ≥ c` (which forces `b ≥ c > 2/7`). ✓
  
  Both sub-cases of `|2a−1| > 1/7` yield contradiction; boundary (`= ±1/7`) falls in the `≤` case. **Exhaustive scan: 0/300k configs exceed `1/7`** (worst config = dyadic `(4/7,2/7,1/7)`, tight). The "fewer than 2 Liu marks" sub-cases are handled: 1 mark → equal-halve both ⇒ `D = 0`; 0 marks → marks at `1/2±δ` (`δ ≤ 1/14`) ⇒ `D = 2δ ≤ 1/7`. The Strategy B′ D-value `|2a−1|` verified (5000 configs, 0 errors). **This is a rigorous, correct, tight n=2 upper bound.**

- **Lemma 4 (equal-halve-n-largest, `D = p_{n+1}` for arbitrary Liu marks at every n) — PROVED.** This is the load-bearing general-n claim; I re-derived the parity/rank argument independently. The lone `p_{n+1}` always lands at an odd rank: the `2n` paired ranks form `n` disjoint blocks of 2 consecutive integers, each summing to an odd number; the lone = `Σ_{1}^{2n+1} − Σ(blocks) ≡ (n+1) − n = 1 (mod 2)`. Verified n=1..5 (5000 configs each, max error 0; lone always odd). **The lemma closes the upper-bound regime `p_{n+1} ≤ 1/D_n` for arbitrary Liu marks at every n, tight at dyadic. CERTIFIED** into `lemmas/equal-halve-n-largest.md`.

- **Peeling lemma (Lemma 3) — PROVED from scratch.** The `+2` parity-neutrality derivation is exact; the circularity caveat on its inductive *use* is correctly stated (the naive `D_rest ≤ (1−2p_j)/D_{n−1}` is loose at dyadic n=3: `13/45 ≫ 1/15`). Verified 20k configs (max error 0). **CERTIFIED** into `lemmas/peeling.md`.

- **Parity-integral + parity-XOR toggle (Lemma 2 / Cor. 2.1) — PROVED.** The Fubini/telescoping derivation is standard and correct. **CERTIFIED** into `lemmas/parity-integral.md`.

**Gaps (honestly flagged, not overclaimed):**
- **G2-general (n ≥ 3, complementary regime `p_{n+1} > 1/D_n`): OPEN.** Lemma 4 closes the spiky regime; flat Liu configs (large smallest piece) are not handled. A fixed 1–2-mark menu is verified insufficient for n=3 (outline-reviewer: worst `0.097 > 1/15`). The defining crux (explicit domino/pairing partition for arbitrary Liu marks) is not closed. **Honest GAP.**
- **G1-general (lower bound, n ≥ 3): OPEN** (shared). n=1,2 proved; n ≥ 3 awaits `lemmas/splits-inequality.md` certification (pending dyadic-induction rebuild).

**Status: `partial`.** Real, verified progress (n=2 upper bound closed, Lemma 4 certified, peeling + parity-integral certified); the defining crux G2-general is honestly open. The "PROVED" labels are accurate — no overclaim. **Verdict: CHANGES REQUESTED** — re-dispatch next round to attack G2-general (the complementary regime); the tools (parity-XOR, peeling, Lemma 4) are sound.

---

## 2. minimax-strategy-family — CHANGES REQUESTED (Status: partial)

**Outcome: `partial`** — the n=2 upper-bound THEOREM is true and the family works, but the proof of one member's D-value has an XOR algebra error that must be fixed.

**What is CORRECT:**

- **The n=2 theorem and menu.** The five D-values `{p_3, p_1−p_2, p_2−p_3, p_1−p_3, |2p_1−1|}` are the actual achieved values (verified by sorting: 0/300k configs exceed `1/7` with these values; tight at dyadic with M1/M3/M5 tying at `1/7`). The §3.2 contradiction proof is valid (it uses `p_1−p_2 > 1/7` in step 3, which IS in the actual menu).
- **Unique-worst-at-dyadic for n=2 (§4): PROVED.** The `≥` version correctly forces `p_1=4/7, p_2=2/7, p_3=1/7`; the `p_1 ≤ 3/7` branch is infeasible (`p_2−p_3 = 0 < 1/7`). Correct.
- **Member M5 (split-to-match) D = |2p_1−1|: PROVED.** The full casework (`p_1 ≥ 1/2` vs `p_1 ≤ 1/2`, sub-cases `q ≥ p_2` vs `q ≤ p_2`) is correct and verified.
- **Members M1 (`= p_3`), M3 (`= p_2−p_3`), M4 (`= p_1−p_3`): CORRECT** (verified by sorting, 5000 configs each, 0 errors).
- **n=1 both bounds (§5): PROVED.** The `min(p_2, 2p_1−1) ≤ 1/3` crossover at `p_1 = 2/3` is clean.
- **Parity-XOR toggle (§2): PROVED** (CERTIFIED via `lemmas/parity-integral.md`).

**The flaw — Member M2's toggle derivation has an XOR error (§3.1, lines 99–109).** The builder computes `f' = f ⊕ [0, p_3)` (the first toggle in M2's chain) and writes, on `[p_3, p_2)`: "`f=0, h=0, f'=1`." But `0 ⊕ 0 = 0`, not `1`. The indicator `[0, p_3)` is `0` on `[p_3, p_2)` (it is the indicator of `[0, p_3)`, not of `[0, ∞)`), so `f' = 0` there, not `1`. This wrong intermediate propagates to the derived formula `D = p_1 − p_3` for M2, which is **FALSE**:

  - Direct sort computation at `(p_1, p_2, p_3) = (0.42, 0.37, 0.21)`: M2 pieces `{p_1−ε, p_2, p_3/2, p_3/2, ε}` give `D = 0.05 = p_1 − p_2`, **not** `p_1 − p_3 = 0.21`.
  - Ground-truth check (5000 configs): M2 matches `p_1 − p_2` (0 errors) and does NOT match `p_1 − p_3` (5000/5000 errors).

  **The actual M2 D-value is `p_1 − p_2`** (which is what the §3.3 table and the §3.2 theorem correctly list). So the theorem's menu is right, but the §3.1 *derivation* establishing that M2 achieves `p_1 − p_2` is broken — it derives `p_1 − p_3` by an XOR slip. The build notes (line 109, line 278) repeat the wrong `p_1 − p_3`.

**Impact.** This is a rigor gap, not a fatal flaw: the M2 strategy DOES achieve `p_1 − p_2` (the value the theorem needs), and a correct derivation is a one-line XOR fix (`f' = 0` on `[p_3, p_2)`, giving `∫f' = p_1 − p_2`). The theorem, the contradiction proof, the tightness table, and the unique-worst proof all stand once the M2 derivation is corrected. But as written, one load-bearing step (the M2 D-value formula) is wrong, so the proof is not `sorry`-free.

**Gaps (honestly flagged):**
- **n ≥ 3 upper bound (G2-upper-n≥3): OPEN.** Fixed 1–2-mark menu verified insufficient for n=3 (worst `0.097 > 1/15`, 2875/100k exceed). The family must be adaptive (full n-mark). The combinatorial regime tree / LP-dual handles are sketched but not closed. Honest.
- **G1 (shared lower bound): OPEN** for n ≥ 3.

**Status: `partial`.** The n=2 upper bound is TRUE and PROVABLE (the family works), but the proof as written has a broken M2 derivation (XOR error producing `p_1−p_3` instead of `p_1−p_2`). **Verdict: CHANGES REQUESTED** — re-dispatch next round to fix the M2 XOR derivation (one-line correction: `f'=0` on `[p_3,p_2)`, yielding `D = p_1−p_2`), and to attack the n ≥ 3 crux. The approach is alive and its framing (minimax over explicit family, genuinely distinct from pairing-charging) is preserved.

---

## 3. alternating-potential — CHANGES REQUESTED (Status: partial)

**Outcome: `partial`** — honest, correct concession of the upper bound; kept lower-bound machinery verified and partly certified.

**The upper-bound CONCESSION is honest and correct.** The candidate `Φ = D − λ·Π` (Π = sum of pair-deficits = `D − leftover`) is indeed linear in `D` and the leftover, both of which change by `O(piece/2)` per split (the largest remaining piece halves geometrically under equal-splitting). Hence `Φ` obeys a dyadic-decrement schedule `|ΔΦ_k| ≤ c/2^k`, summing to `O(1/2^n)` — the confirmed factor-of-2 wall (target `1/D_n ≈ 1/2^{n+1}`, ratio → 2). The aimo-0019 structural-inventory invariant ("at most one dyadic interval of each length beyond the frontier") has no analog: toggle-sets `[0, v) ∪ [u, p)` nest at the bottom `[0, v)` and overlap arbitrarily at the top `[u, p)`, with no dyadic-distinctness enforced by the game. **No non-trivial Φ beating the wall was found; the concession is the right call, not a premature give-up.** The wall argument is sound.

**Kept lower-bound machinery — VERIFIED:**
- **Parity-XOR toggle (§2.2): PROVED** (CERTIFIED via `lemmas/parity-integral.md`).
- **Peeling lemma (§2.3): PROVED** (max error 0 on 20k; CERTIFIED via `lemmas/peeling.md`).
- **Peeling corollary `D = |p_a − p_b|` (§2.4): PROVED.** Equal-split one piece + leave two unsplit gives `D = |p_a − p_b|` exactly. Verified 0 errors (5000 configs × 3 split choices). Tight at dyadic (choosing `p_a, p_b` = two smallest dyadic pieces gives `1/D_n`). The §2.4 proof sketch is slightly hand-wavy ("working through the integral") but the result is correct and the direct sort computation confirms it. (Not separately certified — it is a specialization of the peeling lemma + direct computation; noted in current.md as PROVED.)
- **Even-rank-insertion sub-lemma (§3.5, round 1): PROVED** (verified 100k trials round 1). Kept.

**Gaps (honestly flagged):**
- **GAP-L (shared lower bound, n ≥ 3): OPEN.** Awaiting `lemmas/splits-inequality.md` certification by dyadic-induction (rebuilt this round; not yet certified).
- **GAP-U (upper bound, general n): CONCEDED.** Honest; the upper bound is carried by sibling approaches (pairing-charging, minimax-strategy-family).

**Status: `partial`.** The reusable lower-bound + parity-XOR machinery is the approach's genuine, correct contribution (parts now certified). The upper-bound concession is honest and the wall argument is sound. **Verdict: CHANGES REQUESTED** — the approach stays alive on the lower-bound half (and its certified lemmas feed the field); if a sibling closes the upper bound, this approach's contribution is the shared lower-bound machinery. No re-dispatch needed for the upper bound (conceded); a re-dispatch to help close GAP-L (splits-inequality) would be useful but is shared with dyadic-induction.

---

## Certified lemmas (this round, written to `results/imo-2026-03/lemmas/`)

1. **`lemmas/parity-integral.md`** — parity-integral reformulation `D = ∫[j(t) odd]` + parity-XOR toggle. General, foundational, `sorry`-free. (Proved in pairing-charging §3 and alternating-potential §2.)
2. **`lemmas/peeling.md`** — peeling lemma `D_final = D_rest` at an equal-pair split. General, reusable, `sorry`-free; circularity caveat on inductive use stated. (Proved in pairing-charging §4 and alternating-potential §2.3.)
3. **`lemmas/equal-halve-n-largest.md`** — equal-halve-n-largest `D = p_{n+1}` for arbitrary Liu marks at every n. General-n, closes upper-bound regime `p_{n+1} ≤ 1/D_n`, `sorry`-free, tight at dyadic. (Proved in pairing-charging §6.1.)

**Rejected/not certified:** minimax-strategy-family's n=2 menu lemma — the theorem is correct but the M2 derivation has an XOR error; not certifiable as written. Once the builder fixes the XOR, the n=2 upper bound can be imported from `pairing-charging` (which proves the same 4-menu result correctly) — no need for a separate certification.

---

## Overall status

**`partial`.** No approach reached `solved` (G1-general and G2-general both remain open for n ≥ 3). Round-3 advances:
- **pairing-charging**: n=2 upper bound CLOSED + Lemma 4 (general-n) PROVED + peeling + parity-integral PROVED — the strongest progress this round; 3 lemmas certified.
- **minimax-strategy-family**: n=2 theorem true but M2 derivation broken (XOR error); needs a one-line fix.
- **alternating-potential**: upper bound honestly conceded (sound wall argument); lower-bound machinery verified and partly certified.
- **dyadic-induction**: rebuild in progress (pending next pass); round-1 status stands.

The two open walls are unchanged: G1-general (splits-inequality, n ≥ 3, shared lower bound) and G2-general (complementary-regime upper bound, n ≥ 3 — the real IMO wall). The certified lemmas (parity-integral, peeling, equal-halve-n-largest) are now importable by the whole field.
