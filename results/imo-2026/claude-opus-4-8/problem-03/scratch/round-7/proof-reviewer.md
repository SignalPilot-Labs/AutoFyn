# Proof-reviewer report — imo-2026-03 (IMO 2026 P3), round 7

Three approaches built. All three are honest **partial** advances with no overclaim; none is solved
(the problem remains open on both the lower-bound crux and the upper-bound residual). Verdicts:
all **CHANGES REQUESTED**. I independently re-derived and numerically re-verified (exact `Fraction`
arithmetic, joint cut budget `#Q-cuts+#R-cuts ≤ n` enforced) every load-bearing NEW claim this round.

---

## 1. ll-inclusion-gap — Verdict: CHANGES REQUESTED (Status: partial, outcome: advanced)

**Recorded status in the file (`partial`) is CORRECT.** Genuine advance over R6.

### What I verified (independent re-derivation + numerics, 0 violations)
- **SET IDENTITY** `S_{G_{n−1}}∩[0,2^{n−2}) = S_{G_{n−3}}`: exact SET equality (parity), n=3..8. ✓
- **Generalized (ΣQ-free) top-band decomposition**: `A(G_{n−1})−A(Q)=deficit_top+M` with
  `M=A(G_{n−3})−A(Q_lo)`, both ≥0, `h` even — holds for ANY `Q` with `S_Q⊆S_{G_{n−1}}`, |Q|≤n+1, and
  ARBITRARY ΣQ (~2000 configs, n=3..6). The claim that the certified proof "used ΣQ=2^n only to assert no
  S_Q-mass above 2^{n−1}, which is automatic from S_Q⊆S_{G_{n−1}}⊆[0,2^{n−1})" is CORRECT — this is what
  legitimizes re-applying the identity at the perturbed sums in the recursion.
- **Odd-index ε-reformulation** `Claim(n,ε) ⟺ O_Q ≤ O_{G_{n−1}}+ε`: re-derived the algebra, exact. ✓
- **Base cases** Claim(1,ε), Claim(2,ε), T(1), T(2): re-checked the prose, all correct; and
  **Claim(n,ε) verified 0-violation n=1..4**, **T(ℓ) verified 0-violation ℓ=1..4** (1/2 grid,
  budget-enforced). The strengthened IH never invokes ε<0 for `Claim` (2b-ii routes to `T` instead) —
  confirmed; the explorer's "ε<0 is FALSE" is respected.
- **Two-step induction n→n−2**: for n∈{1,2,3,4} it bottoms out only at the four proven base cases
  (Claim(3)←Claim(1),T(1); Claim(4)←Claim(2),T(2)); no circularity (Claim(n) depends on strictly-lower
  Claim(n−2) and the separate T(n−2)). The n=4 unconditional claim does NOT secretly depend on T(3):
  T(3) is only needed from n=5 up. **So G-INC-1 = Claim(n,0) is genuinely PROVEN for n∈{1,2,3,4}.**
- **O_{Q_lo}≤O_{G_{n−3}} replacement (2b-ii via T(n−2))**: this is exactly what the recursion needs
  (`ε'<0` regime); it is NOT circular — T is a distinct, lower-dimensional statement, and Q_lo satisfies
  T(n−2)'s hypotheses via the SET IDENTITY corollary `S_{Q_lo}⊆S_{G_{n−3}}` (verified). ✓

### GAP I FOUND (name the step): Step 12 case split is INCOMPLETE for general n
Step 12 lists only **Case h≥4** and **Case h=2**. But `h` even includes **h=0**, and I found h=0 IS
reachable for n≥5 among valid INC Claim instances (e.g. n=5: `Q={13/2,13/2,6,6,4,3}`, all parts
`< 2^{n−2}=8`, |Q|=6=n+1, ΣQ=32=2^5, S_Q⊆S_{G_4}). The h=0 case is **trivially true** (all parts <thr ⟹
δ_top=0 ⟹ deficit_top=2^{n−2}≥1≥1−ε), but it is NOT written. This is a one-line fix. **It does NOT
affect the n∈{1,2,3,4} unconditional claim** — I verified h≥2 there (h-values seen: n=3→{2,4},
n=4→{2,4}; for n=3,4 the sum constraint forces h≥2). So the headline "G-INC-1 proven n∈{1,2,3,4}" stands.

### Remaining gaps (honestly flagged by builder + the one I add)
- **T(ℓ), ℓ≥3** — the residual lemma; general-n G-INC-1 is conditional on it. Verified true ℓ=3,4, unproven.
- **h=0 case in Step 12** (general n) — trivial to fill, currently missing.
- **G-INC-2** (refined R general n) — open; vacuous at n=3, first nontrivial n=4.
- **G-GAP** (alignment cost, `S_Q⊄S_R`) — open.

### Lemma certified
- `lemmas/set-identity-selfsimilar.md` — **CERTIFIED** (marked in file). Re-derived (I)–(III), verified.

---

## 2. ll-dyadic-symdiff — Verdict: CHANGES REQUESTED (Status: partial, outcome: advanced)

**Recorded status (`partial`) is CORRECT.** Genuine advance.

### What I verified
- **REFL-gen** (relaxed hyp `max(R)≤μ` instead of `μ≥2^{n−1}`): the proof uses the hypotheses only through
  `S_R⊆[0,μ)`, and `max(R)≤μ` gives exactly this. Verified `A(Q∪R)=μ−A(Q'∪R)` 0/2572 WITH the hypothesis,
  and confirmed it FAILS (2430/2461) WITHOUT it — so the relaxed hypothesis is valid and is exactly the
  one used. NOT an overreach. ✓
- **Double-REFL formula (II)** `A(Q∪G_{n−1})=2^{n−1}−q₁+A(Q'∪G_{n−2})` (branch q₁>2^{n−2}): the two
  reflections (certified REFL on the global max 2^{n−1}, then REFL-gen on q₁ with R=G_{n−2}, valid since
  max(G_{n−2})=2^{n−2}<q₁) compose correctly. Verified 0 mismatch, n=3 (4000) and n=4 (4000). ✓
- **B3a** (`q₁≤2^{n−2}`): `A(Q∪G_{n−2})≤2^{n−2}` ⟹ `A(Q∪G_{n−1})≥2^{n−2}≥1`. Correct. ✓
- **B3b** (`2^{n−2}<q₁≤2^{n−1}−1`): (II) + `A(Q'∪G_{n−2})≥0` ⟹ `≥2^{n−1}−q₁≥1`. Correct. Both hold ALL n.
- **B3c reduced to (B2*)** `A(Q'∪G_{n−2})≥1`, **proved at n=3**: exhaustive |Q'|∈{2,3} on 1/8 grid,
  reviewer re-ran — **min = 1, 0 violations**. The prose casework matches. ✓

### Honest scope (no overclaim)
- General-n (B2*)/GAP-A explicitly left open = the shared alternating-tail crux (same as G-INC-1). ✓
- Refined R (min A=3/2) explicitly open. ✓
- The FALSE "max(Q)<2^{n−1}⟹A≥2" stays deleted; B3-anchor min A=3/2 (not the Sub-3a "A=1" witness). ✓

### Remaining gaps
- **(B2*) general n** and **GAP-A** = the shared crux (import when either route closes it).
- **Refined R** for GAP-B.

### Lemmas certified
- `lemmas/ll-reflection-identity-gen.md` — **CERTIFIED** (I wrote the file; verified as above).
- (dyadic-level-parity, ll-case1-high-interval, ll-reflection-identity already certified prior rounds.)

---

## 3. geometric-selfsimilar — Verdict: CHANGES REQUESTED (Status: partial, outcome: advanced)

**Recorded status (`partial`) is CORRECT.** Real advance; the SB-obstruction is a valid negative result.

### What I verified
- **Threshold identity** `2τ−Σ=Σ/D_b` exact (b=1..7). ✓
- **Case A.A** (`p₁>Σ/2`): subtract-all chain (m−1≤b cuts via the budget invariant |X|≤b+1) doubles every
  non-p₁ piece and leaves `L_m=2p₁−Σ>0`, so `A(final)=2p₁−Σ`. Verified 0/9098 distinct-piece configs.
  With `p₁<τ` and the threshold identity, `A(final)<Σ/D_b` strictly. Correct and CLOSED. ✓
- **SB-obstruction theorem** `Σ'/D_{b−1}≤Σ/D_b ⟺ q≥τ/2`: one-line arithmetic from `D_b−D_{b−1}=2^b`.
  Verified 0/21000. ✓ **Scope check (the key adversarial point):** the theorem is a NEGATIVE result. It
  correctly precludes only **SB-monotone reductions** (those whose sole guarantee is the reduced instance's
  sum-bound) — the write-up is careful to say "any proof of the residual must track the actual alternating
  sum." It does NOT claim to preclude all approaches. **Not over-broad.** The corollary (every gap-case
  pairing piece q≤p₂<τ/2 ⟹ Σ'/D_{b−1}>Σ/D_b) is correct.

### Honest scope
- Residual `p₁≤Σ/2` (the bulk of the gap case) explicitly OPEN; numerically μ·D_b≤1/2 there (SB true,
  proof missing). No overclaim of solve. ✓
- No decertified Structural Lemma or false "A≥2" reappears. ✓

### Remaining gap
- **Residual gap case p₁≤Σ/2** — needs an actual-A potential (the round-6 dead-end, now rigorously
  explained by the SB-obstruction theorem). This is the single remaining upper-bound gap in this route.

### Lemmas certified
- `lemmas/gap-caseAA-subtract-chain.md` — **CERTIFIED** (I wrote the file; verified).
- `lemmas/sb-obstruction.md` — **CERTIFIED** (I wrote the file; verified; correctly scoped negative result).

---

## Summary

| slug | verdict | status | outcome | key advance | main open gap |
|------|---------|--------|---------|-------------|---------------|
| ll-inclusion-gap | CHANGES REQUESTED | partial | advanced | G-INC-1 proven n∈{1,2,3,4}; general n ⟸ T(ℓ) | T(ℓ) ℓ≥3; + write the trivial h=0 case (general n) |
| ll-dyadic-symdiff | CHANGES REQUESTED | partial | advanced | REFL-gen + double-REFL; B3a/b all n; B2* at n=3 | B2*/GAP-A general n (= shared crux); refined R |
| geometric-selfsimilar | CHANGES REQUESTED | partial | advanced | Case A.A closed; SB-obstruction theorem | residual p₁≤Σ/2 (needs actual-A potential) |

**Lemmas certified this round (5):** set-identity-selfsimilar, ll-reflection-identity-gen,
gap-caseAA-subtract-chain, sb-obstruction (all new); nothing rejected.

**Shared-gap watch:** both LL routes still bottom on the same alternating-tail `+1` bound
(T(ℓ)=GAP-A=(B2*) general n). R7 is the FIRST round this crux was *broken at small n* (n≤4 via
ll-inclusion-gap's two-step induction). It is now a clean, lower-dimensional residual `T(ℓ)` — push it
next; the two routes import each other when either closes it. If T(ℓ) stalls unchanged next round, scout
a bypass per CLAUDE.md.

**No overclaim found in any approach; no builder mis-stated its own Status.** The one substantive gap I
add beyond the builders' own honest flags is the missing (trivially-true) h=0 case in ll-inclusion-gap's
general-n Step 12 — it does not touch the n∈{1,2,3,4} unconditional result.
