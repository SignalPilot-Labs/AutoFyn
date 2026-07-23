# proof-builder report — round 11, `potential-weighting-upper-bound`

## Task
Prove the Refined Delete-Recovery Conjecture (§15.4) and use it to close the Match-Recovery Lemma
/ `OPT(Y,p-1)=NC(Y,p-1)`, which per the file's own accounting would close the entire remaining
upper-bound gap of the whole theorem.

## Outcome: NOT solved. Status: partial (unchanged for the theorem as a whole).

**The conjecture is neither proved nor refuted this round.** No counterexample was found at its
correctly-stated scope (`|B|\le1`). A genuine proof was attempted via three different routes (direct
exchange/swap argument, generalized strong induction, averaging), all documented honestly as
incomplete or refuted in their tested forms. This is real, if incomplete, progress — not a
closure, and I am not overclaiming it as one.

## What was actually accomplished (all written into
`results/imo-2026-03/approaches/potential-weighting-upper-bound.md` §16, appended in place, plus a
Status-section note and an `Approaches tried` entry)

1. **A strictly sharper reformulation, Sharp Argmin Recovery (SAR):** recovery of the tagged/
   non-crossing optimum, when the match branch beats deleting `z_1`, always happens at the SAME
   argmin match partner — not merely at *some* partner as the raw conjecture's existential form
   allows. This is a cleaner target than RDRC itself (SAR ⟹ RDRC trivially). Verified with `0`
   violations across ~13,000+ fresh trials this round, including a purpose-built adversarial attack
   (embedding the already-certified-dead `|B|=2` Match-Recovery failure as the specific sub-instance
   SAR's own argmin branch would compute) — 92 triggering embedded instances, all held. This goes
   beyond the outline-reviewer's own equivalent attack on the weaker (existential) RDRC form.

2. **A new lemma, fully proved (not conjectural): the Forced Swap Inequality.** For any background
   (any size — no restriction needed) and any global argmin match partner `k*`, any local
   re-pairing that reassigns `z_1`'s match to "fix" a crossing is provably no better than the
   value already established by `k*`'s global optimality. Proof is a direct minimality/witness
   argument (construct a valid, not-necessarily-optimal alternative selection, use that any
   candidate value upper-bounds its own branch's optimum, chain through the global-argmin
   inequality). Independently re-verified computationally (3336/3336 clean checks) after a
   self-caught test-harness bug (not a lemma bug — documented in the file per this repo's
   convention of recording such catches).

3. **Three precise negative results narrowing the search for a correct general argument:**
   - Averaging the Forced Swap Inequality's two alternatives does NOT recover the optimum (0/81
     successes in cases with an actual crossing) — rules out the most natural way to use the new
     lemma to close SAR.
   - SAR's natural generalization to arbitrary background size is FALSE (exact `|B|=3`
     counterexample found: `B=(0,6,4), Z=(10,8,5,4,3,1)`) — confirms the `|B|\le1` restriction in
     the conjecture's own statement is load-bearing, not a simplifying convenience.
   - The most natural "one-step compatible winner" strong-induction skeleton for SAR is FALSE in
     general (exact counterexample even at `|C|\le1`: `C=[6], W=(8,7,7,4,1), s=3`) — precisely
     diagnoses *why* a naive induction on list size doesn't close this: the correct invariant must
     certify split-compatibility recursively all the way down a *specific* (not arbitrary) family
     of sub-instances arising from repeatedly peeling an argmin branch, not an arbitrary
     background/split/list triple.

## Self-assessment

- **Status for this approach: partial** (unchanged from before this round's build — no regression,
  but also no promotion to solved). Correctly not overclaimed: the file's Status section, the new
  §16, and this report all explicitly state the conjecture is open.
- **For the theorem as a whole: still partial.** The lower bound (round 8's milestone, fully
  unconditional for `D_m`, every `m`) is untouched. The upper-bound gap (Match-Recovery / RDRC /
  SAR) remains the single blocking item, now with one new certified-quality lemma and three
  precise negative findings to hand to the next round, plus a sharper (SAR) target than RDRC.
- **Confidence the conjecture is TRUE but hard, not false:** high — every test this round
  (including the most adversarial one built for it) passed at the stated scope; every failure
  found was outside that scope (background size ≥2, or an over-generalized induction skeleton),
  which if anything is consistent with the conjecture's stated restriction being exactly right.
- **Concerns for the reviewer:** please double-check the Forced Swap Inequality proof in §16.2
  (I re-verified computationally after catching my own harness bug, and I'm confident in the hand
  proof, but it's worth independent scrutiny since it's being proposed as a new general lemma).
  Also worth double-checking that my "SAR" and "RDRC" bookkeeping (which index plays which role,
  `k-1` vs `k*-1` split conventions) exactly matches §13.2/§15.4's own conventions — I restated
  them carefully but this is exactly the kind of place an off-by-one could hide.
- **Concrete next steps recorded in §16.4** for whichever round picks this back up: formalize the
  "recursive compatible family" invariant (§16.3.3's diagnosis) rather than an arbitrary-triple
  induction; look for a global/injective witness construction (in the spirit of the untried
  `aimo-0558` charge-to-distinct-witness lead) rather than a local swap/repair, since local
  swap-based repair is now conclusively ruled out as the mechanism (§16.2, §16.3.1).

All code archived at `/tmp/round-11/work/` (`defs.py` plus driver scripts named after each finding:
`explore.py`, `explore3.py`, `check_all_optima.py`, `embed_search.py`, `embed_search2.py`,
`deeper_check.py`, `verify_fsi_lemma2.py`, `averaging_test.py`, `sar_general_bg.py`, `gml_test.py`).
