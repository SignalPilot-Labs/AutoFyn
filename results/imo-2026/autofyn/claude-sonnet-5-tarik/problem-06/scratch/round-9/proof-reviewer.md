# Round 9 proof-reviewer report — imo-2026-06

Reviewed all 3 built approaches in full. Independently re-derived and
re-simulated the load-bearing claims from scratch (own Python, own
generator validated against brute force on small cases, not reused from
any builder's script). Also applied the round's flagged current.md
correction (round-8 "max ω(a_n) stays single-digit" numbers superseded).

## 1. sunflower-bundle-closure.md — §6, "Full refutation of (UB_S)"

**Verdict: CHANGES REQUESTED. Status: `partial` (correctly self-reported by
the file already — no downgrade needed).**

This is the high-stakes claim of the round: a complete, unconditional proof
that `(UB_S)` (the round-8 sole reduction target: `sup{|rad(a_i)∖S|:i∈I_S}
<∞` for every proper core `S⊊P_1`) is FALSE in Case II. I scrutinized this
with maximum rigor as instructed, since it retires a 5-round-old (rounds
4-8) target family.

**Independent verification performed (all found correct, zero
discrepancies):**

1. **The chain of citation is legitimate, not hand-waved.** §6 assumes
   `(UB_S)` for every proper core, and via the already-certified
   `theorem-UBS-sufficiency.md` (round 8, itself already reviewer-verified
   line-by-line — I re-confirmed the specific equivalence used, §4c's
   "`(UB_S)` for every S ⟺ `B:=sup_{n∉I_{P_1}}ω(a_n)<∞`", by hand: both
   directions of the max-over-finitely-many-cores argument check out) gets
   exact periodicity `a_{n+T}=a_n+L` for every `n≥1`.

2. **Imprint Periodicity Lemma (§6.1).** Given exact periodicity, derives
   that "`n∈I_{P_1}`" is an exactly `τ`-periodic property of `n`, via a
   mod-`p` case split (`p∣L`: period `T`; `p∤L`: period `pT`, using `L`
   invertible mod `p` since `p` prime). I re-derived this case split
   completely independently by hand, then verified it numerically on a toy
   periodic sequence (own Python, `T=3,L=30`, 6 test primes `2,3,5,7,11,13`)
   — exact match to the predicted periods in every case. The corollary
   (`R≠\{0,…,τ-1\}` in Case II, giving explicit `c=1/(2τ)>0` with
   `|I_{P_1}∩[1,N]|≤(1-c)N` for `N≥2τ²`) — I re-derived the arithmetic by
   hand (`(τ-1)⌈N/τ⌉≤(1-1/τ)N+(τ-1)`, etc.) and it matches exactly.

3. **Euler's divergence of `Σ1/p` (§6.2).** Standard classical
   smooth/rough-number-split proof (essentially Erdős's elementary proof).
   Checked the logical structure line by line — correct, no gap.

4. **Landau Count Lemma via Turán's 1934 second-moment argument (§6.3).**
   This is the crux mathematical content. I independently re-derived the
   mean identity `Σ_{m≤X}ω(m)=Σ_{p≤X}⌊X/p⌋` and the second-moment identity
   `Σ_{m≤X}ω(m)²=Σ_{p≤X}⌊X/p⌋+Σ_{p≠q≤X}⌊X/(pq)⌋` **and checked both hold
   EXACTLY (not asymptotically) by direct brute-force enumeration at
   `X=2000`**: `Σω(m)=4454=Σ⌊X/p⌋` (exact), `Σω(m)²=11104` matching the
   right-hand side exactly. Then re-derived the variance bound
   `Σ(ω(m)-S(X))²≤3XS(X)` by hand (the algebra telescopes correctly to
   `3XS` — I redid the expansion independently and it matches the file's
   claimed simplification exactly) and the Chebyshev-type extraction
   `A_k(X)≤3XS(X)/(S(X)-k)²` for `S(X)>k`. **Numerically verified this
   derived bound actually holds** at `X=2×10⁶` for `k=1,2` (the only `k`
   with `S(X)≈2.94>k` reached at that scale, since `S(X)~loglog X` grows
   extremely slowly) — bound held in both cases with substantial margin.
   The proof correctly avoids needing the precise Mertens rate, using only
   qualitative divergence — a genuine simplification, verified sound.

5. **Assembling the contradiction (§6.4) and non-circularity check (the
   dispatch's specific concern).** This is a standard proof by
   contradiction, NOT circular: assume `(UB_S)`-for-every-`S`; this yields
   TWO consequences via one-directional certified implications — (i)
   `B<∞` directly (trivial restatement of the hypothesis via the already-
   proved §4c equivalence) and (ii) exact periodicity `(⋆)` (via the
   already-certified sufficiency chain). The Density Sub-Lemma is then
   derived FROM `(⋆)` (itself a consequence of the standing assumption),
   combined with the *unconditional* Growth Lemma (Lemma 1, `a_n≤a_1+
   (n-1)rad(a_1)`, no dependence on the assumption) and the *unconditional*
   Landau Count Lemma (proved from scratch, no dependence on the
   sequence at all) — these two independent-of-the-assumption facts,
   combined with the two consequences of the assumption, produce
   `c≤o(1)→0` for a fixed positive `c`, a genuine contradiction. At no
   point does the argument assume `(UB_S)` false, or its own conclusion, to
   derive a step — this is legitimate mathematics (the "unusual structure"
   flagged by dispatch is simply: derive two consequences of a hypothesis,
   show they conflict — a completely standard proof-by-contradiction
   pattern, not a hidden circularity).

**Conclusion: I find no flaw. This is a complete, rigorous, independently
re-verified proof that `(UB_S)` is false in Case II.** This is exactly the
kind of high-value "kill" finding CLAUDE.md values (analogous to round
2/3's refutation of `H_n`/`W`-finiteness) — it definitively closes an
entire multi-round research thread.

**However — and this is the crux of the dispatch's routing instruction —
this does NOT solve the whole problem.** `(UB_S)` was proven sufficient
(round 8) but never proven necessary for FCBC/the whole problem — Lemma W1
(already certified) shows FCBC only needs a fixed prime set to intersect
every pair, a strictly weaker requirement than bounding companion-bundle
size. `sunflower-bundle-closure`'s own file already, correctly, self-reports
`Status: partial` at the top (line 1-2) and its own §6 "Honest scope note"
explicitly states this refutation does not resolve FCBC or the whole
problem — no overclaim to correct here; the builder got this exactly
right. Per this workspace's standing rule (a real, certified result keeps
the verdict at CHANGES REQUESTED, not RETHINK, even when the specific
route dies), and since the whole-problem Status is genuinely `partial` (not
`solved`), the routing verdict is **CHANGES REQUESTED**, not APPROVE — the
"changes requested" here is really "pivot away from `(UB_S)` entirely
going forward, which the file has already correctly done by handing FCBC
to its siblings." I record the outcome as `verified-milestone` (not
`dead-end`) because the proved content itself is a complete, valuable,
independently-verified theorem — the *research thread* it retires is a
dead end, but this file's own round-9 output is a genuine proof, not a
failed attempt.

**Certified:** `lemmas/theorem-UBS-false-case-II.md` (new) — Imprint
Periodicity Lemma, Euler's divergence, Landau Count Lemma, and the main
refutation theorem, all bundled together since they were built and are
used as one unit this round. Full independent-verification notes embedded
in the lemma file.

## 2. explicit-window-backbone-construction.md — round 9 build

**Verdict: CHANGES REQUESTED. Status: `partial` (correctly self-reported).**

No proof this round (honestly reported as such). The file's own framing is
accurate: Step 3 is correctly downgraded from "free consequence" to "open
empirical claim" (a real self-correction, not overclaimed), and Step 4 is
correctly diagnosed as exactly as hard as FCBC itself (already-certified
Pool Lemma equivalence) — the file does not misrepresent empirical
convergence as a reduction in difficulty.

**Independent verification performed:**

- Built a fresh, independent greedy-sequence generator using the
  certified minimal-radical-antichain method (Lemma W3), validated first
  against a naive brute-force all-prior-terms-gcd generator on
  `a_1∈\{15,247,2747\}` (exact match) before trusting it at scale — this
  caught a real bug in my first antichain-update implementation
  (incorrectly removing an existing antichain member when a duplicate
  radical was re-derived), fixed and re-validated before use.
- **Reproduced the `a_1=9674419` violation exactly**: `a_{12}=9675525`
  (radical `\{3,5,23,71,79\}`, H-signature `\{3,5,79\}`), `a_{15}=9675778`
  (radical `\{2,7,23,151,199\}`, H-signature `\{2,7,151\}`), disjoint
  H-signatures, `\gcd(a_{12},a_{15})=23` exactly — matches the file's
  claim exactly (initially I mis-read "H-signature" as "full radical" and
  thought I'd found a discrepancy; re-reading the definition and
  recomputing correctly resolved this — the file's claim is accurate).
- **Reproduced the `a_1=21528751` violation exactly**: `a_{596}=21612570`
  (radical `\{2,3,5,7,97,1061\}`, H-signature vs `H_0`: `\{2,3,5,7,1061\}`),
  `a_{863}=21650497` (radical `\{11,97,103,197\}`, H-signature
  `\{11,103,197\}`), disjoint, `\gcd=97` exactly.
- **Independently extended the `H_{100}` zero-violation check** for
  `a_1=21528751` to `N=60000` (builder tested to `3{,}000{,}000` — I did
  not reproduce the full scale for time reasons, but found zero
  discrepancy at the scale tested: `4336` distinct `H_{100}`-signatures,
  zero empty signatures, zero pairwise-disjoint-signature pairs).

**Conclusion: all reported findings check out exactly. The gap (Step 4) is
correctly diagnosed** — no overclaim, no hidden gap, honest and accurate
empirical report. No new certifiable lemma this round, correctly
self-assessed by the builder (nothing added to `lemmas/`).

## 3. intersecting-family-covering-construction.md — Part 8, Theorem SW

**Verdict: CHANGES REQUESTED. Status: `partial` (correctly self-reported).**

Theorem SW claims FCBC reduces unconditionally to the Stabilization
Conjecture restricted to doubly-infinite disjoint core pairs. I checked
specifically for missed cases as instructed.

**Independent re-derivation of the case split.** For any pair `i<j` with
cores `S:=S(i)`, `S':=S(j)` (both nonempty, by the already-certified
Theorem CD):
- Case 1 (`S∩S'≠∅`, includes `S=S'`): covered by `P_1` via Lemma SW1 (I
  re-derived this 3-line argument independently — correct).
- Case 2 (`S∩S'=∅`, one side finite): covered by the already-certified
  Finite-Class Direct Covering lemma. I checked this lemma's own certified
  statement (`lemmas/finite-imprint-class-direct-covering.md`) applies to
  ANY nonempty `S` with `I_S` finite, no hidden restriction to proper
  cores — confirmed, so its use here (for `S` ranging over all cores, not
  just proper ones) is valid.
- Case 3 (`S∩S'=∅`, both infinite): the open Stabilization Conjecture.

**These three cases are genuinely exhaustive and non-overlapping in
application** — I checked in particular the edge case `S=P_1` (or
`S'=P_1`): since any nonempty `S'⊆P_1` has `P_1∩S'=S'≠∅`, this always
falls into Case 1 automatically, correctly recovering the already-certified
"top core is free" fact (Lemma TC) with no special-casing needed — I looked
for exactly this kind of missed edge case per the dispatch instruction and
found none. I also checked the finiteness bound on `H` (`≤(2^k-1)+
\binom{2^k-1}{2}` further finite sets beyond `P_1`, via Theorem CD's core
count) — correct.

**Numerical re-verification, fresh generator (same one built and validated
for approach 2 above):**

- `a_1=247`, channel `(\{13\},\{19\})`, `N=8000`: independently found
  `|I_{13}|=4305,|I_{19}|=2764`, `W=\{2,3,5,7\}` covers all
  `11{,}899{,}020` cross pairs, **zero** failures — consistent with (a
  smaller-scale, but zero-discrepancy, subset of) the builder's own
  `N=60000`/`669`M-pair claim.
- Reproduced the shared `a_1=21528751` bridge-prime-`97` finding
  independently (same computation as approach 2's cross-check) — the
  three-way agreement between this file, `explicit-window-backbone-
  construction`, and my own independent computation on the exact same
  numeric fact (`a_{596}`, `a_{863}`, bridging prime `97`) is a strong
  consistency signal.

**Conclusion: Theorem SW's logic is correct, the case split is genuinely
exhaustive with no missed case, and the reported numerics check out.** The
Stabilization Conjecture itself is honestly and correctly left open — the
file does not overclaim it as proven or as equivalent to any
already-resolved statement (explicitly and correctly distinguishes it from
the round-5 `(LMRS_{S,S'})` machinery, noting only a one-directional
implication is established).

**Certified:** `lemmas/theorem-SW-stabilization-sufficiency.md` (new) —
Theorem SW, Lemma SW1, Lemma SW3 (the Stabilization Conjecture itself is
explicitly NOT certified — it remains open).

## Cross-approach synergy check

Checked whether `sunflower-bundle-closure`'s refutation of `(UB_S)`
combines with either sibling's open gap to close anything: it does not —
`(UB_S)` was never necessary for FCBC, so its refutation removes a
(now-abandoned) potential shortcut but leaves both live FCBC-attacking
mechanisms (Stabilization Conjecture; universal-window search) completely
unaffected, exactly as all three files themselves correctly state. Checked
whether `intersecting-family-covering-construction`'s Theorem SW and
`explicit-window-backbone-construction`'s `H_{100}` empirical finding
combine: both independently identify the *same* hard instance
(`a_1=21528751`, bridge prime `97` at the `\{1061\}×\{103,197\}`
doubly-infinite core pair) as the crux difficulty — this is a genuine,
non-trivial convergence (two independent techniques landing on the
identical hardest sub-case) worth flagging for round 10, though it does not
by itself close either gap.

## Round-8 numeric correction applied

Per dispatch instruction, `current.md`'s round-8 claim "max ω(a_n) stays
single-digit: 247→6, 2747→6, 21528751→7" is corrected in the new Round 9
section: round 9 explorers found `247→8` (at `n=408816`) and `2747→8` (at
`n=374037`); `21528751` has not yet been pushed past `7` (search
incomplete). This does not affect any certified lemma (no proof depended on
the specific single-digit values), but corrects the empirical record — the
true growth behavior of `ω(a_n)` off the top core remains unknown.

## Summary of verdicts

| Approach | Verdict | Status | Outcome recorded |
|---|---|---|---|
| sunflower-bundle-closure | CHANGES REQUESTED | partial | verified-milestone |
| explicit-window-backbone-construction | CHANGES REQUESTED | partial | partial |
| intersecting-family-covering-construction | CHANGES REQUESTED | partial | advanced |

None RETHINK. No APPROVE (whole-problem Status remains `partial`). 2 new
lemma files certified (`theorem-UBS-false-case-II.md`,
`theorem-SW-stabilization-sufficiency.md` — 48 total in `lemmas/`).
`current.md` updated with a full Round 9 section (headline placed above the
Round 8 section, per this workspace's append convention) including the
required round-8 numeric correction.

## Overall assessment for the run

This round produced its most decisive single-round finding since round 3:
a definitive kill of the entire `(UB_S)`/`(MRS)`/`𝓥_S`-finiteness research
thread that has occupied rounds 4-8, PLUS a genuine new reduction (Theorem
SW) that narrows the live FCBC target further than any previous round.
Round 10 should attack the Stabilization Conjecture directly (per Lemma
SW3's tail-confinement) and/or seek a magnitude-bound mechanism for the
universal-window approach — both are now the sharpest live targets, with
`(UB_S)` definitively removed from consideration.
