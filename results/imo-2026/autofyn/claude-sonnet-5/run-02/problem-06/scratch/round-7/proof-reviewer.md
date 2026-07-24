# Round 7 proof-review — imo-2026-06

Problem: IMO 2026 P6. Claim: the greedy-avoid-coprime sequence a_n has eventually
periodic gaps (a_{n+T}=a_n+L for all n≥1). Answer type: none (proof-only). Crux
carried into this round: prove FAH (Full-Absorption Hypothesis) and Symmetric FAH,
the sole remaining open gap after round 6's Collateral-Safety Theorem reduced (†)
to base-type-pair-level termination.

All three built approaches reviewed independently below, per CLAUDE.md's
per-approach routing (a mixed result is normal, not a failed round).

## 1. greedy-exchange-cost-potential — Verdict: CHANGES REQUESTED (Status: partial)

**Retraction check (genuine, not just asserted).** The file retracts the dispatched
"Two-Witness Intersection Uniqueness via joint Critical-Prime-Dichotomy" mechanism.
I independently checked both halves of the retraction:

- *Abstract argument*: re-read Lemma H's certified proof
  (`lemmas/critical-prime-dichotomy.md`) line by line. It derives branch (b) only
  from a magnitude fact (c > a_{n-1}) plus Free Facts giving
  P(a_i)∩P(a_n) = {q'} — an S₀-external prime-set fact. It never touches ρ(i) or
  τ(i). Confirmed: there is genuinely no route from "a_i shares exactly {p} with
  a_{n_B}" to "a_i has S₀-type B," so the outline's proposed missing link cannot be
  extracted from Lemma H's proof as written.
- *Computational check on a_1=4807*: I regenerated the sequence from scratch
  (trial-division factorization, no shared code with any builder):
  a_1..a_10 = 4807, 4818, 4826, 4830, 4840, 4845, 4862, 4864, 4884, 4902, matching
  the file's reported factorizations exactly. Recomputed Q={11,19,23},
  S={2,3,5,7,73,127}, S₀={2,3,5,7,11,19,23,73,127}, ρ(6)={3,5,19}, ρ(7)={2,11},
  F'={13,17}, F''={17}. Applied Lemma H to q'=13 (c=374) and q'=17 (c=286): both
  ≪ a_6=4845, so both trivially land in the uninformative branch (a). This matches
  the file's claim exactly — the retraction is genuine.

**Lemma J (Divisor-Restricted Pigeonhole).** Re-derived from scratch: nonemptiness
of D(n) follows directly from the certified Generalized Bounded Witness Lemma;
recurrence of a fixed D*⊆F' follows from infinite pigeonhole over the finite set
2^{F'}\{∅}. Correct, unconditional, no gap. **Certified**
(`lemmas/divisor-restricted-pigeonhole.md`).

**Lemma K (Adjacent Multiple Blocking).** c := q·⌊a_n/q⌋ for q∤a_n. If c>a_{n-1},
then a_{n-1}<c<a_n is a smaller-than-a_n candidate, and minimality of a_n (the
literal greedy defining rule) forces some j<n with gcd(c,a_j)=1. Direct, correct,
one-paragraph minimality argument — structurally analogous to but genuinely
distinct from Lemma H (Lemma H strips a divisor with an EXACT resulting
factorization P(c)=P(a_n)\{q'}; Lemma K rounds down to a non-divisor multiple,
whose factorization has NO controlled relationship to a_n). **Certified**
(`lemmas/adjacent-multiple-blocking.md`).

**Why Blocking-Data Bridging still fails.** The file's diagnosis is precise and I
confirm it: even when Lemma K's branch (b) fires, giving a blocking index j with
gcd(c,a_j)=1, Free Facts only guarantees SOME prime r shares a_n and a_j — nothing
forces r=q or excludes r=q, because c and a_n are different integers with no
divisor relationship (unlike Lemma H's construction, where P(c) is exactly known).
This is a real, structurally different obstruction from Lemma F/Lemma I's prior
diagnoses (magnitude too large vs. type-uncontrolled vs. this round's
factorization-uncontrolled) — genuinely new content, not a repackaging.

**Verdict.** Real progress: a confirmed-dead sub-mechanism correctly retracted (not
just claimed), two new certified lemmas, the first use of illegality data in this
workspace, a precisely diagnosed stall. FAH/Symmetric FAH remain open. Status
correctly self-reported as `partial`. **CHANGES REQUESTED.**

## 2. covering-system-construction — Verdict: CHANGES REQUESTED (Status: partial)

**Step 8.7 (Canonicalization).** Claims Step 8.5's finish only needs a single prime
q_i ∈ F'_i∩F''_i witnessing BOTH sides' full-absorption ("Joint FAH"), not
uniqueness of F'∩F''. Re-read Step 8.5's proof of Case 2: it indeed only uses one
fixed q_i on both sides, never comparing it to other candidates or invoking
uniqueness. The fix — canonically defining q*_i := min(F'_i∩F''_i) — makes "same
prime both sides" automatic by construction. I checked this is honestly scoped: it
is a SUFFICIENT (not necessary, and not "easier") reformulation — it does not make
FAH itself easier to prove, it only removes an unneeded dependency on the sibling's
now-dead Two-Witness Uniqueness target. The file states this caveat explicitly and
does not overclaim. Correct, no gap.

**Step 8.8 (Symmetry-Transfer Check).** Checks whether the sibling's proposed
(stalled) Blocking-Data Bridging mechanism is side-symmetric. Confirmed by
inspection: the mechanism's only inputs are (i) an arbitrary fixed index n and its
own predecessors, (ii) the Finite Core Theorem's side-agnostic S₀ — neither is
specific to n_B's status as B's earliest occurrence, unlike the (now-dead)
Two-Witness-Uniqueness mechanism which explicitly used n_B's minimality. The
claimed cutoff-equivalence (n>n_B for A'-side vs "m>n_A, i.e. effectively m≥n_B"
for B'-side) is also correct: every B'-occurrence has m≥n_B>n_A by definition of
n_B as B''s own earliest occurrence, and m=n_B itself is already handled
unconditionally by Lemma G. No gap found.

**Certification decision on 8.7/8.8.** Both are correct but are meta-statements
about THIS file's own proof structure/target (what Step 8.5 needs; whether the
sibling's specific stalled mechanism is symmetric) — not portable mathematical
facts independent of this proof, matching the round-3 Lemma F / round-6 Lemma I
precedent for correct-but-non-portable content. **NOT certified** as standalone
shared lemmas; recorded in current.md as in-file guidance instead.

**Step 9 (secondary n=1 gap).** Step 9.1 (Exact-Equality Reduction Lemma) is a
trivial, correct case-split: literal periodicity from n=1 holds iff finitely many
explicit equalities (i=1,...,N₀−1) hold, given eventual periodicity from N₀.
Fully general, no gap. **Certified.**

Step 9.2 (Non-Automaticity of Prefix Folding) claims the outline's proposed
period-rescaling fix (T':=T·k) is NOT automatic in general, via an explicit
counterexample: a_1:=1, a_2:=5, a_n:=997+n for n≥3. I independently re-verified:
this sequence is strictly increasing (1<5<1000<1001<...) and eventually periodic
(T=1,L=1 from N₀=3, trivially since a_{n+1}=a_n+1 for n≥3). I re-derived the
non-existence proof by hand: for any candidate (T'',L'') valid at all n≥1,
restricting to n≥3 forces a_{n+T''}=997+n+T''=a_n+L''=997+n+L'', so T''=L''.
Applying at n=1: a_{1+T''}=a_1+T''=1+T''. Case T''=1 needs a_2=2 (false, a_2=5).
Case T''≥2 needs 1+T''≥3, so a_{1+T''}=997+(1+T'')=998+T'' by the n≥3 formula,
forcing 998+T''=1+T'', i.e. 998=1 (false). Both cases contradict — no such
(T'',L'') exists. Confirmed correct, no gap. **Certified.**

Step 9.3 honestly documents an open candidate strategy (residue-driven rule from
i=1) with a precisely identified point of failure (whether every off-G residue is
already blocked among a_1,...,a_{i-1} for i<N₀) — correctly left open, not
smoothed over.

**Verdict.** Real, correct, honestly-scoped incremental progress on both fronts
(narrowing/decoupling the primary gap's dependency structure; giving the secondary
gap its first genuine treatment with 2 new certified lemmas). No gap found in any
claimed-proved step; every "still open" claim checks out under independent
verification. **CHANGES REQUESTED.**

## 3. scalar-well-ordering-lock-in — Verdict: RETHINK (Status: partial)

**Section 1 (w_k well-definedness).** Standard bookkeeping using the certified
Collateral-Safety Theorem's Corollary (fixed finite list of disjoint base-type
pairs) and Extended Persistent-Type Pigeonhole. Tie-breaking via a fixed
lexicographic order is correctly handled (A∩B=∅ forces min(A)≠min(B), so no ties
within a pair). Correct, no gap.

**Section 2 (refutation of hypothesized recursion (H)).** I independently
regenerated a_1=175's sequence from scratch:
a_1..a_6 = 175, 180=2²·3²·5, 182=2·7·13, 189=3³·7, 195=3·5·13, 210=2·3·5·7 — matches
the file exactly. Recomputed: S₀^(0)=Q={5,7}; A_0'={5} witnessed at n=2 (a_2=180),
B_0'={7} witnessed at n=3 (a_3=182); Lemma G applied gives gcd(180,182)=2 (confirmed:
180=2²·3²·5, 182=2·7·13, shared factor exactly 2), so q_0=2, S₀^(1)={2,5,7}.
Recomputed ρ_1(3)=P(182)∩{2,5,7}={2,7}≠{7}, so index 3 no longer witnesses pure
type {7} at level S₁; ρ_1(4)=P(189)∩{2,5,7}={7} (189 odd), giving the new earliest
witness m'=4, w_1=a_4=189. Since 189 is odd, q_0=2∤189 — (H) genuinely fails, exactly
as claimed. The generalization (Witness Discontinuity Obstruction) is exactly this
example restated as an existence claim, which is trivially valid given the fully
verified example. Correct, no gap. **Certified**
(`lemmas/witness-discontinuity-obstruction.md`).

**Section 3 (honest assessment of repairs).** Both natural repairs (fixed-pair
variant; weaker |open(k)| scalar) are shown to collapse into the already-open
FAH/Symmetric-FAH question. I checked the fixed-pair argument: since Lemma G's
recruited prime q always divides BOTH n_A and n_B by construction, the same
discontinuity phenomenon reoccurs at the very next stage for the same pair whenever
it stays open — correct, and the file honestly does not oversell this as an
independent route.

**Verdict rationale (RETHINK, not CHANGES REQUESTED).** This round's genuinely new
proof *style* — transplanting aimo-0678's algebraic-recursion mechanism — is now
shown, via a fully verified counterexample and a general (if narrowly-scoped)
structural argument, to be dead: the hypothesized recursion (H) is false, and the
file's own honest Section 3 shows every natural repair reduces to the same open FAH
question rather than providing an independent bypass. This matches the workspace's
established precedent for RETHINK (round 5 witness-index-descent, round 6
recruitment-round-charging): when a whole approach's core mechanism is shown, by
its own builder's honest analysis, to have no surviving independent route to the
target, it should return to the outliner for a genuinely different mechanism
rather than being incrementally patched. The produced Witness Discontinuity
Obstruction is valuable, certified, reusable content (round 7 achieved a genuine
"advanced" byproduct even under an overall RETHINK verdict) — but the approach as
scoped should not be re-built as-is; any revival needs a proof style that does not
assume continuity of witness selection across recruitment stages.

## Lemma certification summary (round 7)

Certified (unconditional, independently re-verified, no gap):
- `lemmas/divisor-restricted-pigeonhole.md` (Lemma J)
- `lemmas/adjacent-multiple-blocking.md` (Lemma K)
- `lemmas/exact-equality-reduction-lemma.md`
- `lemmas/non-automaticity-of-prefix-folding.md`
- `lemmas/witness-discontinuity-obstruction.md`

NOT certified (correct but non-portable meta-statements about a specific proof's
own structure, per the round-3 Lemma F / round-6 Lemma I precedent):
- Canonicalization Lemma (`covering-system-construction` Step 8.7)
- Symmetry-Transfer Check (`covering-system-construction` Step 8.8)

## current.md

Updated: `## Status` (still partial, round-7 summary), new `## ROUND 7` section
with independent verification notes, `## Lemma certification this round (round 7)`,
`## ROUND 7 — approach verdicts`, and `## Next-round guidance (current, round 7)`.
No `## Full proof` — the problem remains unsolved; FAH/Symmetric FAH (equivalently
the single canonical-prime Blocking-Data Bridging Lemma) is still the sole open
gap after this round's narrowing.

## Bottom line

- greedy-exchange-cost-potential: CHANGES REQUESTED / partial.
- covering-system-construction: CHANGES REQUESTED / partial.
- scalar-well-ordering-lock-in: RETHINK / partial (dead-end as scoped; certified
  byproduct lemma retained).

No approach reaches `solved` this round. The problem's Status remains `partial`.
Round 7's genuine contribution: closed off two more specific dead-end mechanisms
(joint Lemma-H analysis, aimo-0678 recursion transplant) with rigor (not just
assertion), added 5 newly certified unconditional lemmas, and gave the long-dormant
secondary n=1 gap its first real, non-trivial treatment. The core crux (FAH /
Symmetric FAH) is unchanged in substance and still needs a genuinely new mechanism
per the accumulating diagnosis (Lemma I, and now this round's Lemma K obstruction
and Witness Discontinuity Obstruction all independently point at the same missing
ingredient: control over a constructed competitor's factorization relative to the
actual witness, or a stability property of witness selection under core
enlargement).
