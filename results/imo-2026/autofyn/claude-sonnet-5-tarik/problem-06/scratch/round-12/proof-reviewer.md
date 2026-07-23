# Proof-reviewer report — imo-2026-06, round 12

Reviewed all 4 built approaches end-to-end, independently re-deriving the
load-bearing step of each from scratch and re-simulating every numeric
claim with fresh, from-scratch Python (own generators — never reused a
builder's or explorer's script). Read `results/imo-2026-06/current.md`,
`/tmp/round-12/outline-reviewer.md`, all 4 approach files in full, all 4
build reports, and every cited certified lemma file.

**Headline finding: sunflower-inadmissibility-toolkit's central claim
("Lemma BS closes Backbone Permanence, hence Theorem CAC unconditionally
closes Conjecture (JW) for 5 concrete instances") is an overclaim, caught
and corrected.** Lemma BS and Theorem CAC are both independently verified
correct **as abstract/conditional statements**, and are certified as such
— but the claim that this establishes the hypothesis for any specific
numeric `a_1` is not justified by the proof given, and is retracted. See
Finding 1 below for the full derivation of why. The other 3 approaches'
results (Sandwich Uniqueness Lemma, Matched-Witness refutation, Theorem
PD-Conditional) are all independently verified correct and are unaffected
by this correction.

## Finding 1 — sunflower-inadmissibility-toolkit: Lemma BS / Theorem CAC
are correct abstract facts; the claimed closure for 5 concrete instances
is an overclaim (CHANGES REQUESTED)

**Re-derivation of Lemma BS from scratch.** Fix a proper core `S'` with
`I_{S'}` infinite, enumerate `I_{S'}` as `j_1<j_2<\cdots`, `B_k:=
\bigcap_{t\le k}\mathrm{comp}(a_{j_t})`. `B_1` is finite (a positive
integer has finitely many prime factors), `B_k` is non-increasing, so
`|B_k|` is a non-increasing sequence of non-negative integers, hence
eventually constant at some finite `k_0`. Standard nested-intersection
identity then gives `\bigcap_{j\in I_{S'}}\mathrm{comp}(a_j)=B_{k_0}`. This
proof is **correct and elementary** — I re-derived it independently and
found no gap. It is a pure **existence** statement: *some* finite `k_0`
exists. It gives **no information about which `k_0`**, and in particular
does not certify that a `k_0` reached within a finite computational check
is the true one.

**Why this matters — the exact logical gap.** A non-increasing chain of
subsets of a finite set can stay constant for arbitrarily many steps and
then still drop. I confirmed this trivially in Python:
```
B = [{2,3,7}, {2,3,7}, {2,3,7}, {2,3}, {2,3}, {2}]
# valid non-increasing chain, constant for 3 steps, then drops.
```
So "we checked 2 (or `2929`) members and the intersection didn't change"
is **consistent with, but does not prove**, that the true, infinite-class
intersection equals the observed value — exactly the same logical gap this
workspace corrected in round 7 (a "zero exceptions, deliberately extended
search" escape-depth claim was overturned by a counterexample found just
past the tested cutoff) and flagged in round 11 (UCR/WRP's overclaim
hazard, which this very file's §6 explicitly (but ineffectively) tries to
guard against).

**Re-derivation of Theorem CAC's proof (checking the Lemma UCR
substitution carefully, since a parameter mismatch here would break
everything).** Theorem CAC invokes Lemma UCR with `"S":=S'`, `"C":=B(S')`.
Lemma UCR's actual hypothesis: `S,S'` disjoint subsets of `P_1`, `C`
nonempty finite disjoint from `P_1`, `S\cup C` realized. Substituting:
need `B(S')\cap P_1=\varnothing` (true, `B(S')\subseteq\mathrm{comp}
(a_{j_1})` by construction) and `S'\cup B(S')` realized at `j_0` (assumed
hypothesis). Lemma UCR's conclusion: for every `j` with `S(j)\cap S'=
\varnothing`, `B(S')\cap\mathrm{comp}(a_j)\ne\varnothing`. Since `S\cap
S'=\varnothing`, this covers every `i\in I_S`. Combined with Lemma BS's
`B(S')\subseteq\mathrm{comp}(a_j)$ for every `j\in I_{S'}` unconditionally
(the *specific* witness prime `p\in B(S')\cap\mathrm{comp}(a_i)` found for
a fixed `i` works for *every* `j\in I_{S'}` simultaneously, since `p\in
B(S')\subseteq\mathrm{comp}(a_j)` regardless of which `j`) — this correctly
and cleanly avoids the previously-stuck `u=w` rigidity wall (no two
independently-derived witnesses ever need to be shown equal). **This part
of the proof is correct, no gap.**

**Why the concrete instance claims are not established.** §9 of the
approach file computes, for `a_1=2747`, `(S,S')=(\{41\},\{67\})`: only 2
members of `I_{\{67\}}` within the tested range (`a_3,a_{54}`), both with
`\mathrm{comp}=\{2,3,7\}`, and states "confirms `B(\{67\})=\{2,3,7\}`."
This is **exactly** the finite-prefix-to-infinite-class inference that
Lemma BS's abstract proof does not license. I independently re-verified
the 2 raw facts (`a_3=2814=2\cdot3\cdot7\cdot67`, comp `\{2,3,7\}`;
`a_{54}`'s comp also `\{2,3,7\}` — reproduced with my own fresh generator,
extended to `n=200`, finding `I_{67}=\{3,54,103,154\}`, all four with
`\mathrm{comp}\supseteq\{2,3,7\}`, joint (JW) check zero violations across
all `764` cross pairs) — the **numerics are correct and match exactly**,
but numerics, however extensive, are not a proof (per CLAUDE.md's own
rule, explicitly invoked by this very workspace multiple times before).
The round-12 outline-reviewer's own **pre-build** assessment (`/tmp/
round-12/outline-reviewer.md`, Central finding 1) already correctly
identified this: *"The one open item — Backbone Permanence (does the
frozen prefix-intersection stay fixed over the whole infinite class, not
just the tested prefix) — is correctly and honestly labeled as the crux,
open, not proved. My extended run ... is consistent with, not a proof of,
permanence."* The builder's claim to have closed this via Lemma BS is a
genuine mathematical misstep (conflating an abstract existence-of-
stabilization fact with an instance-specific verification-of-the-
stabilization-point fact), not a minor wording slip — I checked whether
there is some other route that would make the finite check sufficient
(e.g. using the Realized/Blocked dichotomy directly on the observed
candidate, or some minimality property of the greedy construction) and
found none in the file or in the already-certified lemma cache.

**Consequence, checked concretely: `a_1=2747` and `a_1=4087` would have
been FULLY, unconditionally solved instances of the IMO problem had this
claim held up** (since `|P_1|=2` for both, the only possible disjoint core
pair is the single singleton pair, and Theorem SW's case split means
*either* one side is finite [automatic] *or* both are infinite [needing
exactly the Stabilization Conjecture for that one pair, which Theorem CAC
would supply]) — I verified this case-exhaustiveness by hand from
`lemmas/theorem-SW-stabilization-sufficiency.md`'s statement. Since the
Case A hypothesis is not actually established, this consequence does
**not** go through; `a_1=2747`/`a_1=4087` remain open, exactly as before
this round, though now with a much sharper, precisely-stated residual
question (Backbone Permanence for one specific class) instead of the
vaguer "prove Conjecture (JW)."

**Certification decision.** Certified Lemma BS, Lemma BS-Dichotomy, and
Theorem CAC into `results/imo-2026-06/lemmas/lemma-BS-backbone-
stabilization-and-theorem-CAC.md`, **explicitly scoped as abstract/
conditional statements only** — with the overclaim and its precise reason
documented in the certified file itself, and a matching correction note
inserted directly into `results/imo-2026-06/approaches/sunflower-
inadmissibility-toolkit.md` §10 so a future round reading that file
directly is not misled (per this workspace's standing practice of
repairing and re-scoping rather than rejecting outright when the
underlying lemma is sound but its application is overclaimed).

**Why this is not a wasted round.** The reduction itself has real value:
Conjecture (JW) for a numerically-Case-A pair now reduces to *exactly* one
precise, well-defined open question (does a specific observed value
survive forever) rather than the vaguer original target, and the Sandwich
Uniqueness Lemma (Finding 2 below) shows this same abstract machinery
*does* give a fully rigorous negative result when applied to prove
*emptiness*/*confinement* rather than *permanence* — clarifying exactly
which direction of claim this workspace's current toolkit can and cannot
establish. This distinction (negative/subset claims are easy; positive/
permanence claims are hard) is the key structural lesson of the round and
is recorded in `current.md` for future rounds.

## Finding 2 — forced-primes-well-ordering: Sandwich Uniqueness Lemma +
`4199:(13,17)` resolution — verified correct, unaffected by Finding 1
(APPROVE-worthy content, overall verdict CHANGES REQUESTED)

Re-derived the Sandwich Uniqueness Lemma from scratch: if `W` witnesses
(JW) via the Realized-Backbone/UCR mechanism (full-class containment on
side `z` + exact realization on side `z`), then `W\subseteq B_{\mathrm{full}}
(z)` (containment) and `B_{\mathrm{full}}(z)\subseteq W` (since the
witness index `m\in I_z` is itself one of the sets intersected), so `W=
B_{\mathrm{full}}(z)` exactly. Correct, elementary, no gap.

Independently re-generated `a_1=4199` from scratch (own trial-division
generator, `sympy.factorint`) and reproduced exactly: `a_2=4212=2^2\cdot
3^4\cdot13` (core `\{13\}`, comp `\{2,3\}`), `a_3=4216=2^3\cdot17\cdot31`
(core `\{17\}`, comp `\{2,31\}`), `a_5=4233=3\cdot17\cdot83` (core `\{17\}`,
comp `\{3,83\}`), `a_8=4290=2\cdot3\cdot5\cdot11\cdot13` (core `\{13\}`,
comp `\{2,3,5,11\}`), `a_9=4316=2^2\cdot13\cdot83` (core `\{13\}`, comp
`\{2,83\}`) — all match the file exactly. Confirmed `\mathrm{comp}(a_3)
\cap\mathrm{comp}(a_5)=\{2,31\}\cap\{3,83\}=\varnothing`, so
`B_{\mathrm{full}}(\{17\})=\varnothing`. Confirmed the running `\{13\}`-side
intersection `\{2,3\}\to\{2,3\}\to\{2\}` (positions 2,8,9), so
`B_{\mathrm{full}}(\{13\})\subseteq\{2\}` — this containment is **always
valid regardless of whether the true intersection has stabilized** (it is
simply the trivial fact that an intersection over all of `I_{13}` is a
subset of an intersection over any 3 of its members), which is exactly
why this argument, unlike Finding 1's, is not affected by the finite-
prefix-vs-infinite-class gap: it only ever needs *subset*/*emptiness*
facts, never a *permanence* fact. Confirmed `\mathrm{rad}(a_5)\cap\{2,13\}=
\{3,17,83\}\cap\{2,13\}=\varnothing` exactly, so the already-certified
Lemma ERD-C correctly kills the `\{2\}` sub-case (`\kappa=\{2,13\}` blocked,
hence never realized at any index). The 2-case dichotomy (`\{2\}` or
`\varnothing`) is exhaustive since `\{2\}` has exactly one element. **No
gap found anywhere in this argument.** This is a complete, unconditional,
correctly-scoped proof that the Realized-Backbone/UCR mechanism cannot
close (JW) for `4199:(13,17)` via either anchor — correctly stated as
disposing of *this mechanism*, not as disproving (JW) for the pair.

Certified: `results/imo-2026-06/lemmas/lemma-sandwich-uniqueness.md`.

## Finding 3 — sunflower-bundle-closure: Row-Restriction Obstruction +
Matched-Witness refutation — verified correct, no new general lemma this
round (correctly self-assessed) (CHANGES REQUESTED)

**Row-Restriction Obstruction.** Re-read the argument carefully: for a
fixed `j_0\in I_{S'}^{\tau'}`, Lemma P′+XC give a witness in `\mathrm{comp}
(a_{j_0})\setminus\Pi` for *every* `i\in I_S^\tau` — this genuinely works
(fixed `j_0`, `i` ranges freely). But the target needs the union over
*all* `j\in I_{S'}^{\tau'}`, and nothing in the certified toolkit (Lemma
P′, XC, NIDF, FT, CB, Escape-Confinement) relates `\mathrm{comp}(a_j)` to
`\mathrm{comp}(a_{j'})` for two *different* indices `j\ne j'` — every
certified lemma is a "one side fixed, other side free" statement, never a
"both sides range together" boundedness statement. I checked each cited
lemma's actual statement to confirm none secretly provides this — correct,
this is an honest, precise diagnosis, not a stall dressed up as a proof.

**Matched-Witness construction and refutation — independently re-verified
the two counterexample factorizations and gcds exactly, as specifically
requested by the dispatch.** Fresh Python (own generator + `sympy`), for
`a_1=247`: `a_2=260=2^2\cdot5\cdot13` (core `\{13\}`, comp `\{2,5\}`),
`a_5=285=3\cdot5\cdot19` (core `\{19\}`, comp `\{3,5\}`), `\gcd(260,285)
=5`, `5\notin\{2,3\}` — **exact match**. For `a_1=4199`: `a_9=4316=2^2
\cdot13\cdot83` (core `\{13\}`, comp `\{2,83\}`), `a_5=4233=3\cdot17\cdot
83` (core `\{17\}`, comp `\{3,83\}`), `\gcd(4316,4233)=83`, `83\notin
\{2,3\}` — **exact match**. Also independently confirmed the "matched
witness" construction itself: `a_7=342=2\cdot3^2\cdot19` (comp `\{2,3\}`,
`13\notin\mathrm{rad}`) and `a_6=312=2^3\cdot3\cdot13` (comp `\{2,3\}`,
`19\notin\mathrm{rad}`) for `247`; `a_{11}=4332=2^2\cdot3\cdot19^2` (comp
`\{2,3\}`, `13\notin\mathrm{rad}`) and `a_2=4212=2^2\cdot3^4\cdot13` (comp
`\{2,3\}`, `17\notin\mathrm{rad}`) for `4199` — all exact matches. This is
a genuine, fully rigorous negative result (not a numeric stall): both
mandatory Case B instances' natural "matched witness via symmetry" idea is
now proved false by explicit, hand-verifiable counterexample, closing off
a plausible next-round idea before it wastes a session.

No new general-purpose lemma proposed or needed certification this round
— correctly self-assessed by the builder (the two new results are
instance-specific/diagnostic, not reusable general facts).

## Finding 4 — intersecting-family-covering-construction: Theorem
PD-Conditional — verified correct, fully and honestly scoped (CHANGES
REQUESTED)

Re-derived Lemma BRL-from-Periodicity by hand (the periodic-sequence
pigeonhole argument: for `n>n_0`, `G(n)=G(n_0+\varphi(n))` where `\varphi
(n)\in\{1,\dots,T\}`; if `S'` doesn't appear among `G(n_0+1),\dots,
G(n_0+T)`, `I_{S'}` would be finite, contradiction; occurrences after
`n_0` form a union of arithmetic progressions with common difference `T`;
any window of length `R+1=n_0+T+1` hits one) — correct, no gap. Re-derived
Lemma PD-from-BRL's block-partition pigeonhole bound and the algebraic
substitution giving `c=1/(2(R+1))`, `i_0=2R+4` by hand — correct
arithmetic, verified the two inequality steps (`\lfloor x\rfloor\ge x-1`;
`i-R-2\ge i/2$ for `i\ge2R+4`) independently.

**Independently re-simulated with fresh code** (own generator + period
finder, not reusing the math-explorer's KMP-based one or the outline-
reviewer's): `a_1=247`, exact period `T=1806` found (brute-force check up
to `maxT=2200`), max run avoiding `\{13\}`: **3**, avoiding `\{19\}`:
**5** — **exact match** to the file's claimed numbers. Confirmed
Proposition 9.4's exact hypothesis wording in `lemmas/lemma-RD-restricted-
domination-and-magnitude-bound.md` matches what Theorem PD-Conditional
supplies (`|I_{S'}\cap[1,i)|\ge ci` for `i\ge i_0`) exactly, with no
scope mismatch.

Correctly, honestly conditional throughout — never claims periodicity
itself is established, states the numerical support precisely (4/5
instances, `21528751` inconclusive), and the negative Lemma-W3-based
attempt at closing periodicity directly is a genuine, targeted negative
finding (not a mere restatement of round 11's circularity diagnosis) —
confirmed by checking `lemmas/lemma-W2-W3-patch-and-minimal-radical-
reduction.md`'s own "Discussion" section does record `|M_n|` growing
unboundedly for `a_1=221` (`|M_{199}|=42`), exactly as cited.

No overclaim found anywhere in this build.

## Cross-approach synergy — explicitly checked, as the dispatch requested

1. **Do Case A + Case B partition ALL doubly-infinite pairs?** Yes, as an
   *abstract* classification (every pair's true `B(S')` is either empty,
   nonempty+realized, or nonempty+blocked — exhaustive and mutually
   exclusive by Lemma BS + the already-certified Lemma ERD-C, verified by
   hand). But — per Finding 1 — *which* branch a *specific* pair actually
   falls into is not established for any of the 5 "Case A" instances; only
   the negative instances (`247` both sides empty, `4199:(17)` empty) are
   rigorously pinned down, because those are subset/emptiness claims, not
   permanence claims.
2. **Does sunflower-inadmissibility-toolkit's Case A + forced-primes'
   negative result leave `4199:(13,17)` fully resolved?** No — partially.
   Two independent mechanisms (Realized-Backbone/UCR via Sandwich
   Uniqueness; NIDF-pigeonhole via Row-Restriction Obstruction) are both
   rigorously proved unable to close it, but neither proves Conjecture
   (JW) *false* for this pair. It remains open to a not-yet-tried
   mechanism.
3. No combination of this round's 4 results closes any part of the
   Stabilization Conjecture unconditionally for a general `a_1`. Checked
   directly: Sandwich Uniqueness (forced-primes) applied to a Case A pair
   would just reconfirm the (already-known, trivial) fact that the
   realized witness set must equal `B_{\mathrm{full}}`, no new leverage;
   Row-Restriction Obstruction (sunflower-bundle-closure) explicitly does
   not apply to Case A pairs (no per-class backbone problem there);
   Theorem PD-Conditional's hypothesis (periodicity of `G`) is not implied
   by, and does not imply, Backbone Permanence for a specific class — these
   remain the same 3 non-combining sub-questions identified in rounds
   10–11, now each sharpened but none closed.

## Verdicts (per approach, independent — CLAUDE.md's per-approach routing)

- **sunflower-inadmissibility-toolkit** — Status `partial` (unchanged from
  builder's self-report, but for a corrected reason — see Finding 1).
  **CHANGES REQUESTED.** Real, certified content (Lemma BS, Theorem CAC as
  abstract/conditional facts); the overclaimed "closure for 5 instances"
  is corrected in both the certified lemma file and the approach file
  itself. Next round should attack Backbone Permanence directly via the
  outline's original routes (a)/(b) (Escape-Confinement/Permanent-
  Inadmissibility adapted to a single class), not repeat the finite-
  descent argument.
- **forced-primes-well-ordering** — Status `partial`. **CHANGES
  REQUESTED.** Genuine, fully rigorous, unaffected-by-Finding-1 negative
  result (Sandwich Uniqueness Lemma + complete resolution of
  `4199:(13,17)` for this mechanism). Certified.
- **sunflower-bundle-closure** — Status `partial`. **CHANGES REQUESTED.**
  Genuine, independently-verified negative content (Row-Restriction
  Obstruction, Matched-Witness refutation), correctly no new lemma
  proposed. Case B (`247:(13,19)`, `4199:(13,17)`) remains open.
- **intersecting-family-covering-construction** — Status `partial`.
  **CHANGES REQUESTED.** Genuine, fully rigorous, honestly-scoped
  conditional theorem (Theorem PD-Conditional). Periodicity of `G` itself
  remains the open hypothesis.

None RETHINK — every approach's underlying technique remains viable and
each produced independently-verified genuine content this round (even
sunflower-inadmissibility-toolkit's corrected result is real progress: a
much sharper reduction of Case A's open content, just not a closure).
None APPROVE — the whole problem (Status `solved`) is not reached this
round.

## Lemmas certified this round

- `results/imo-2026-06/lemmas/lemma-BS-backbone-stabilization-and-theorem-
  CAC.md` — Lemma BS, Lemma BS-Dichotomy, Theorem CAC, certified **with an
  explicit scope correction** (abstract/conditional only; concrete-instance
  claims not certified, retracted).
- `results/imo-2026-06/lemmas/lemma-sandwich-uniqueness.md` — Sandwich
  Uniqueness Lemma, certified in full, including the worked `4199:(13,17)`
  resolution as reusable content.

57 total lemma files now in `results/imo-2026-06/lemmas/`.

## current.md

Updated with a new "Round 12 update" headline section at the top (pushing
round 11's headline down, unchanged), covering all findings above,
including the overclaim correction, the cross-approach synergy checks, and
the recommendation for round 13 (attack Backbone Permanence directly via
the outline's original mechanism; do not re-attempt "pure finite descent
alone suffices").

## Recommendation for round 13

Attack **Backbone Permanence** directly for at least one Case-A-consistent
pair (e.g. `2747:(41,67)`, backbone candidate `\{2,3,7\}`): adapt the
already-certified single-family Escape-Confinement Lemma / Permanent-
Inadmissibility Lemma to show that once a class's running intersection
reaches a candidate value `C` at some concrete finite point, no later
member of that same class can ever have a companion set missing an element
of `C` — this is exactly the open content the round-12 outline originally
specified (routes (a)/(b)) and that this round's Lemma BS does not
supply. If this can be established for even one instance, combined with
the already-certified Theorem CAC it would give a genuine, complete,
unconditional solve of that instance (e.g. `a_1=2747` or `4087`, both of
which reduce to exactly this one question). Separately, `(PD_{S,S'})`
now depends on periodicity of `G` (Theorem PD-Conditional) — a dedicated
attempt at proving periodicity (or the weaker Bounded-Run-Length property
directly) for a specific `a_1` is the sharpest concrete unexplored target
for that sub-question.
