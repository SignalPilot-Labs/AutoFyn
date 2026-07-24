# Round 14 proof-reviewer report — imo-2026-06

Reviewed all 4 built approaches independently, with maximal adversarial
scrutiny per this workspace's standing rule (round 12's caught overclaim,
round 13's "extraordinary claim requires extraordinary verification").
Wrote fresh, independent Python (own antichain-optimized generator,
cross-validated against brute force; `sympy.factorint` for all
factorizations) — did not reuse any builder's script. **Bottom line: 3
approaches produced genuinely new, fully solved concrete instances (a
strong round); 1 approach produced correct but overstated content. None
RETHINK. Workspace total now 5 fully solved concrete instances of the
whole IMO problem (`a_1=15,247,4199,2747,4087`) plus 1 new channel of the
hardest recurring case (`21528751`). The GENERAL problem (every `a_1`)
remains open — `current.md` Status correctly stays `partial`.**

---

## 1. `forced-primes-well-ordering` (§M) — `a_1=4199` full closure

**Claim.** All 6 disjoint core-pair channels of `P_1=\{13,17,19\}` close
via Lemma WF (already certified round 13), giving `H=\{2,3,13,17,19,83\}`,
`L=2{,}091{,}102` — a second fully solved concrete instance. Claims the
7th proposed witness `a_82` is redundant.

**Independent verification performed.**
- Re-derived Lemma WF's proof from Corollary P″ (unordered Lemma P′) +
  Lemma XC from scratch — correct, no gap, fully general for the entire
  infinite index class (not a finite-prefix claim).
- Wrote a fresh antichain-optimized generator, cross-validated exactly
  against brute force on 200 terms (bit-for-bit match), then generated
  `a_1=4199` to `n=12{,}000` (0.86s).
- Re-derived all 6 witness factorizations via `sympy.factorint`: `a_2=
  4212=2^2\cdot3^4\cdot13`, `a_5=4233=3\cdot17\cdot83`, `a_9=4316=
  2^2\cdot13\cdot83`, `a_{11}=4332=2^2\cdot3\cdot19^2`, `a_{12}=4352=
  2^8\cdot17`, `a_{92}=5967=3^3\cdot13\cdot17` — exact match to the file.
- Confirmed class sizes at `n=12{,}000` exactly match the file's §M.5
  claims: `|I_{13}|=2791`, `|I_{17}|=6156`, `|I_{19}|=1816`,
  `|I_{13,17}|=681`, `|I_{13,19}|=156`, `|I_{17,19}|=343`,
  `|I_{13,17,19}|=57`.
- Independently checked, via a complete (not sampled) `\{2,3,83\}`-
  signature cross-check, all 6 channels: **zero violations** — every
  realized signature pair across every one of the 6 disjoint core pairs
  shares a prime of `\{2,3,83\}`.
- Re-derived the `\binom{7}{2}=21=15\text{ intersecting}+6\text{
  disjoint}` exhaustiveness count by hand — correct.
- Re-derived all 6 Boolean case-split proofs (§M.3) by hand — each is a
  short, exhaustive 2-case argument from the per-class disjunctive facts
  (§M.2), all valid.
- Confirmed `a_82=5746=2\cdot13^2\cdot17` (core `\{13,17\}`, comp `\{2\}`)
  is genuinely redundant: its only possible target is `I_{19}` (the only
  singleton core disjoint from `\{13,17\}`), where it would force `2\mid
  a_k` — already supplied, more directly, by `a_{12}` (singleton core
  `\{17\}`, comp `\{2\}`, also disjoint from `\{19\}`). This is NOT a
  mistake versus the round-14 explorer's 7-witness claim — it's a correct
  simplification; both witness sets close the same 6 channels, the
  builder's is minimal.

**No gap found.** `a_1=4199` is a genuine, complete, unconditional second
solved concrete instance. Certified:
`lemmas/theorem-FW1-full-closure-a1-4199-second-instance.md`.

**Verdict: CHANGES REQUESTED.** File Status `partial` (correct — the
general problem is untouched); this is the strongest possible form of
"real progress," recorded prominently. **Not APPROVE** at the workspace
level since `current.md`'s Status (tied to the general `a_1` claim) stays
`partial` per CLAUDE.md's Status definition — the per-file "solved
instance" content is fully certified and correct.

---

## 2. `sunflower-inadmissibility-toolkit` (§15–18) — `a_1=2747`,
`a_1=4087` full closures

**Claim.** New Lemma SCF (Singleton-Chain Forcing, elementary aggregation
of Lemma WF) closes `a_1=2747` (`W=\{2,3,7\}`, 4 witnesses) and
`a_1=4087` (`W=\{2\}`, 2 witnesses) — 3rd/4th solved concrete instances —
via a mechanism that bypasses the still-open Backbone Permanence route
entirely (no running intersection, no permanence claim; round 13's
Theorem TLL-Refuted counterexamples are irrelevant here since this
mechanism never invokes permanence).

**Independent verification performed.**
- Re-derived Lemma SCF's proof (`r` independent Lemma WF applications,
  intersected) from scratch — correct, no interaction/case-split needed
  between the `r` applications (each is unconditionally true for the
  whole infinite class independently).
- Confirmed `2747=41\times67`, `4087=61\times67` by direct computation.
- Re-derived all 6 witness factorizations via `sympy.factorint` and the
  fresh generator: `a_3=2814=2\cdot3\cdot7\cdot67`, `a_{13}=3321=
  3^4\cdot41`, `a_{14}=3362=2\cdot41^2`, `a_{163}=11767=7\cdot41^2`
  (for 2747); `a_5=4288=2^6\cdot67`, `a_{54}=7442=2\cdot61^2` (for
  4087) — exact match.
- Re-generated both sequences to `N=20{,}000` (5.6s / 6.6s): class sizes
  exactly match claims — `2747`: `|I_{41}|=19{,}203`, `|I_{67}|=389`,
  `|I_{41,67}|=408`; `4087`: `|I_{61}|=10{,}312`, `|I_{67}|=9{,}375`,
  `|I_{61,67}|=313`. **Zero violations** of the derived unconditional
  divisibility facts across all members of both disjoint-core classes in
  both instances.
- Re-derived both 4-step FCBC-assembly proofs by hand (§16/§17 Steps
  1–4) — each is correct, exhaustive (the `|P_1|=2\Rightarrow` unique
  disjoint core pair template, reused correctly from round 13's `a_1=247`
  precedent).

**No gap found.** Both instances are genuine, complete, unconditional
solved concrete instances. This is the workspace's simplest closure to
date (`a_1=4087`, single shared prime `2`). Certified:
`lemmas/lemma-SCF-and-instances-2747-4087.md`.

**Verdict: CHANGES REQUESTED.** File Status `partial` (correct, general
problem untouched); real, complete, gap-free progress on two additional
concrete instances via a genuinely new (not previously certified)
mechanism.

---

## 3. `witness-chaining-universal-existence` (first build) — Corollary
MSF + `a_1=21528751` channel closure

**Claim.** Corollary MSF, a new general corollary of the Chaining
Sufficiency Theorem + Lemma WF, valid for arbitrary `a_1` and disjoint
core pair. Applied to close `a_1=21528751`'s pair `\{197\}` vs. `\{103\}`
(this workspace's longest-standing hardest recurring test case, flagged
rounds 6–11) with `W=\{2,3,7\}`. Part 2 honestly reports the "Small-
Companion Existence Lemma" as open/likely-false and replaces it with a
weaker "Bounded Forced-Set Existence Conjecture."

**Independent verification of Corollary MSF's generality.** Re-derived
the 3-step proof from scratch, independent of the file's write-up:
- Step 1: `r` independent Lemma WF applications give `P\subseteq
  \mathrm{comp}(a_k)` for every `k\in I_S` (aggregation of unconditional
  facts, no case split).
- Step 2: one more Lemma WF application (roles reversed) gives
  `\mathrm{comp}(a_j)\cap P\ne\varnothing` for every `j\in I_{S'}`, using
  `\mathrm{comp}(a_{j_0})\subseteq P` (hypothesis (ii)).
- Step 3: any `p\in\mathrm{comp}(a_j)\cap P` is also in `\mathrm{comp}
  (a_i)` (since `P\subseteq\mathrm{comp}(a_i)`), giving the shared prime.

This is a valid, fully general logical implication for **any** `a_1` and
disjoint core pair satisfying the two hypotheses — the hypotheses
(existence of the witnesses) are what varies per instance, not the
corollary's proof. **No silent instance-specific assumption found.**
Confirmed it is a strict instantiation of the already-certified Chaining
Sufficiency Theorem (the file's own cross-check, re-derived and
confirmed).

**Independent verification of the `21528751` instance.**
- Confirmed `P_1=\mathrm{rad}(21528751)=\{103,197,1061\}`
  (`103\times197\times1061=21{,}528{,}751`, hand-verified).
- Wrote a fresh antichain generator and pushed it to `n=27{,}832`
  (~69–71s runtime, values up to `~25.5M`) — a genuinely difficult
  computation given the scale; verified against the same generator
  cross-validated on small cases earlier in this review.
- Confirmed all 4 witness factorizations exactly via `sympy.factorint`:
  `a_{1405}=21{,}727{,}232=2^{11}\cdot103^2`, `a_{11812}=23{,}201{,}883=
  3^7\cdot103^2`, `a_{27832}=25{,}472{,}209=7^4\cdot103^2` (all core
  `\{103\}`, singleton comps `2,3,7`), `a_{2575}=21{,}893{,}004=
  2^2\cdot3^4\cdot7^3\cdot197` (core `\{197\}`, comp `\{2,3,7\}\subseteq
  P=\{2,3,7\}`) — bit-for-bit match to the file's table.
- Confirms the closure is genuinely valid: this is a real, striking
  finding — the pair closes via Corollary MSF's `\{103\}`-side singleton
  chain despite `I_{\{197\}}` having no small-`|\mathrm{comp}|` members
  in an extensive search.

**Scope check (no overclaim found).** The file explicitly and repeatedly
states this closes only 1 of `a_1=21528751`'s 6 disjoint core-pair
channels — the instance as a whole is **not** claimed solved (correctly
not a "5th solved instance"). Part 2's honest framing ("no proof found;
no genuine refutation found; gap narrowed, not closed") is accurate — the
Bounded Forced-Set Existence Conjecture is explicitly and correctly
labeled open, not proved. **No disguised overclaim.**

**Process note (not a correctness issue).** The certified lemma file
`lemmas/corollary-MSF-multi-singleton-forcing.md` was written directly by
the builder into `lemmas/` rather than via the normal
propose-then-reviewer-certifies flow. Content independently re-verified
in full above and retained; added a reviewer verification note to the
file documenting this deviation and the independent re-check.

**Verdict: CHANGES REQUESTED.** File Status `partial` (correct); genuine
new general-purpose corollary plus a striking, correctly-scoped concrete
channel closure on the workspace's hardest recurring case; Part 2 is
honest, not overclaimed.

---

## 4. `intersecting-family-covering-construction` (Part 13) — Theorem MO
(Minimality Obstruction)

**Claim.** Theorem MO "rigorously proves an entire technique family
(bounded-modulus/CRT minimality selection) cannot resolve
`BRL(S')`/`G`-periodicity" — via new Lemma WO++ (Joint CRT Independence),
Theorem MO itself, and Proposition MO-2 (Enrichment Collapse).

**Independent verification of the three individual results.**
- Lemma WO++: re-derived the CRT-bijection proof by hand — correct,
  elementary extension of the already-certified Lemma WO. Independently
  numerically verified: `P_1=\{13,19\}`, `S'=\{19\}` (`c_{S'}=12`), `q=5`
  — computed exactly `12` integers of type `\{19\}` in each of the 5
  residue classes mod `5` in the window `(1000,1000+1235]`, exact match
  to the claimed formula.
- Theorem MO: re-derived the composition (Lemma XC + Lemma WO++'s
  Corollary) by hand — correct, no gap. This is an exact, airtight
  statement: for one **fixed** witness `a_i`, the type of a candidate `y`
  carries zero information (in the exact CRT-frequency sense) about
  whether `y` is admissible against `a_i`.
- Proposition MO-2: re-derived the trivial specialization argument by
  hand — correct (a universally-quantified-over-every-`y`-of-type-`S'`
  hypothesis restricts validly to the subset of actual sequence members).

**Scope problem found (the load-bearing issue for this file).** The three
individual results are each correct, but they establish only a
**two-point dichotomy**: (1) the bare `P_1`-alphabet is powerless against
one fixed witness (Theorem MO), and (2) a companion-enriched set strong
enough to guarantee admissibility for **every** type-`S'` integer against
**every** `i\in I_S` collapses to the covering-witness condition itself
(Proposition MO-2, "full strength" case). **Not formally addressed**: an
intermediate mechanism — a fixed `W_0` combined with a pigeonhole/density
argument establishing only that *some* type-`S'` candidate in each
bounded window is admissible against the accumulated history (weaker than
"every candidate," and not restricted to one fixed witness either). The
file's own Part 13.3 "Remark" and "Weaker version" paragraphs give a
plausible, but explicitly informal (not theorem-formalized), argument for
why this intermediate case likely also collapses — this is discussion,
not a proof. **The headline "retires an entire technique family" claim is
therefore an overstatement of what is formally proven** — it retires the
two tested extremes with a well-reasoned but not fully rigorous argument
for why the space between them is empty, not a complete impossibility
proof.

This is analogous in shape (though smaller in stakes) to round 12's
overclaim pattern flagged in this workspace's standing memory rules: an
individually-correct result whose headline synthesis outruns what was
actually proven. Unlike round 12 (which would have flipped 2 concrete
instances from open to solved), here the affected claim is a negative/
impossibility result about a *sub-technique*, not the main problem or any
solved instance — the practical consequence is smaller, but the
overclaim pattern is the same and worth catching and correcting.

**Certified at corrected scope**: Lemma WO++, Theorem MO, Proposition
MO-2 exactly as individually stated, with an explicit scope-correction
note explaining the gap between what's proven and the file's broader
headline. `lemmas/theorem-MO-minimality-obstruction.md`.

**Verdict: CHANGES REQUESTED** (not RETHINK — three genuine, individually
correct, reusable certified lemmas were produced; the issue is a scope
overstatement in the synthesis, not a broken approach or fatally flawed
mechanism). File Status `partial`. **Gap for next round**: formalize (or
refute) the intermediate pigeonhole/density mechanism explicitly to
either complete the impossibility proof or find a genuine counterexample
route living in that gap.

---

## Cross-approach checks performed

- Confirmed `forced-primes-well-ordering`'s §M, `sunflower-inadmissibility-
  toolkit`'s §15–18, and `witness-chaining-universal-existence`'s
  Corollary MSF all build on the identical certified Lemma WF, converging
  independently on structurally similar mechanisms — genuine convergence,
  not redundant work (each closes a distinct instance/channel).
- Confirmed Corollary MSF is a strict generalization of Lemma SCF (the
  latter is the special case where the "subset witness" `j_0`'s companion
  set already equals, rather than merely is a subset of, `P`) — both
  correctly kept as separate lemma files reflecting two builders'
  independent routes.
- Confirmed Theorem MO/Proposition MO-2 (targeting `BRL(S')`/`G`-
  periodicity) are fully orthogonal to the 3 new solved-instance results
  (targeting Conjecture (JW)/(WCE) via witness-chaining) — no interaction
  either direction.
- **Explicitly checked the dispatch's "does this suggest the general
  theorem is close" pressure and declined to let it affect scoping.** All
  5 solved instances (`15,247,4199,2747,4087`) plus the new `21528751`
  channel were closed by manually finding specific low-index witnesses,
  not by any general existence argument. The general existence question
  (Bounded Forced-Set Existence Conjecture / Conjecture WCE) remains
  completely untouched — no proof attempt beyond restating it this round.
  `current.md`'s Status correctly stays `partial`.

## Certifications this round (4 new lemma files, 65 total in `lemmas/`)

1. `lemmas/theorem-FW1-full-closure-a1-4199-second-instance.md` — full
   6-channel closure of `a_1=4199`, second solved concrete instance.
2. `lemmas/lemma-SCF-and-instances-2747-4087.md` — Lemma SCF + full
   closures of `a_1=2747`, `a_1=4087`, 3rd/4th solved concrete instances.
3. `lemmas/corollary-MSF-multi-singleton-forcing.md` — Corollary MSF
   (general) + `21528751` channel closure; reviewer verification note
   added (builder wrote the file directly, content independently
   re-verified in full).
4. `lemmas/theorem-MO-minimality-obstruction.md` — Lemma WO++, Theorem
   MO, Proposition MO-2, certified at a reviewer-corrected narrower scope
   than the approach file's own headline.

`results/imo-2026-06/current.md` rewritten with a full Round 14 update
section (headline first, per dispatch instructions), Status remains
`partial`.

## Outcomes recorded

- `forced-primes-well-ordering` — `advanced` (a_1=4199 second solved
  instance, 6-channel closure verified gap-free).
- `sunflower-inadmissibility-toolkit` — `advanced` (a_1=2747, 4087
  3rd/4th solved instances via new bypass mechanism, verified gap-free).
- `witness-chaining-universal-existence` — `advanced` (general Corollary
  MSF verified genuinely general; striking 21528751 channel closure
  verified; no overclaim in Part 2).
- `intersecting-family-covering-construction` — `partial` (3 individually
  correct new lemmas, but headline "retires an entire technique family"
  claim scope-corrected to the two proven extremes only; real but
  incomplete negative result).
