## imo-2026-06 (lens: a_1=4199 channel-counting + witness-chaining extension)

### Headline finding (read this first)

**Strong evidence (rigorous case-split derivation, not just numerics) that ALL 6
of a_1=4199's disjoint core-pair channels close with the SAME small witness
set the certified Lemma WF already licenses — using witnesses that are
literally the same 4 (`a_2,a_5,a_9,a_12`) Theorem FW1 already certified, plus
3 more (`a_11,a_82,a_92`), all at index ≤92.** If this survives builder/
reviewer scrutiny, `a_1=4199` becomes a second fully-solved concrete
instance (and a bigger one, since |P_1|=3 with 6 channels vs. `a_1=247`'s
1 channel) using zero new lemmas beyond what's already certified
(`lemma-WF-witness-forcing-and-theorem-FW-instances.md`,
`theorem-XC...`, `theorem-CD...`, `theorem-SW...`, `theorem-5.1...`). This
is exploration-level (I derived and numerically stress-tested the logic,
I did NOT write a reviewer-grade proof) — treat as a strong lead for the
outliner/builder, not a certified result.

### 1. Channel-counting convention, verified

Per `theorem-SW-stabilization-sufficiency.md` + `theorem-CD-core-
decomposition-and-lemma-TC.md`: a "channel" is an unordered pair `{S,S'}`
of **nonempty disjoint subsets of `P_1`** (both sides need `I_S` infinite
to be a live "doubly-infinite" channel requiring the open Stabilization
Conjecture; intersecting cores or a finite-`I_S` side are auto-covered by
already-certified Lemma SW1 / Finite-Class Direct Covering). For
`P_1={13,17,19}` (7 nonempty subsets), enumerating unordered disjoint pairs
by hand gives exactly **6**: `({13},{17})`, `({13},{19})`, `({17},{19})`,
`({13},{17,19})`, `({17},{13,19})`, `({19},{13,17})` — matching current.md's
own count exactly. Cross-check on `a_1=247` (`P_1={13,19}`, 3 nonempty
subsets): only 1 disjoint pair, `({13},{19})` — matches the dispatch's
"only one nonempty-subset pair" and Theorem FW2/Corollary FW2-FCBC's scope
exactly. Convention confirmed correct before applying it to 4199.

Channel 1 `({13},{17})` is already closed: **Theorem FW1**, `W={2,3,83}`,
certified in `lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`
(round 13). The other 5 were open coming into this round.

### 2. Generated data (own fast generator, cross-validated)

Generated `a_1=4199` to `n=20{,}000` terms (`sympy.factorint` per candidate,
O(n) admissibility check per candidate against all prior radicals — simple
but fast enough: 15s for 20,000 terms, terms up to ~400,000). Class sizes at
this depth: `I_13`=4652, `I_17`=10260, `I_19`=3028, `I_{13,17}`=1136,
`I_{13,19}`=259, `I_{17,19}`=570, `I_{13,17,19}`(top core)=95 — all growing
steadily, consistent with all 6 proper cores being infinite (not proven here,
but per the note below this doesn't actually matter for the argument).

### 3. The witness-chaining argument for the 5 remaining channels

Using the **already-certified Lemma WF** (`comp(a_k)∩comp(a_{i_0})≠∅` for
every `k∈I_S`, whenever `S(i_0)=S'` and `S,S'` disjoint — this holds for
literally every `k`, finite or infinite index set, no separate finiteness
argument needed), I found 7 low-index witnesses (all ≤ index 92, exact
factorizations independently checked via `sympy.factorint`):

- `a_2=4212=2^2·3^4·13` (`S={13}`, comp=`{2,3}`)
- `a_5=4233=3·17·83` (`S={17}`, comp=`{3,83}`)
- `a_9=4316=2^2·13·83` (`S={13}`, comp=`{2,83}`)
- `a_11=4332=2^2·3·19^2` (`S={19}`, comp=`{2,3}`)
- `a_12=4352=2^8·17` (`S={17}`, comp=`{2}`)
- `a_82=5746=2·13^2·17` (`S={13,17}`, comp=`{2}`)
- `a_92=5967=3^3·13·17` (`S={13,17}`, comp=`{3}`)

(First 4 are exactly Theorem FW1's own witnesses — no new witnesses needed
for 4 of the 5 remaining channels; only channel 6 needs `a_11,a_82,a_92`.)

Applying Lemma WF to each witness (valid for every class disjoint from the
witness's own core) gives these **consolidated, unconditional/disjunctive
facts per class** (pure deduction, not numerics):

- `I_13`: `2` (from `a_12`) **and** `(3∨83)` (from `a_5`)
- `I_19`: `2` (from `a_12`) **and** `3` (from `a_92`) — i.e. **both
  unconditional**, the strongest case
- `I_17`: `(2∨3)` (from `a_2`) **and** `(2∨83)` (from `a_9`) — equivalently
  `2∨(3∧83)`
- `I_{13,19}`: identical shape to `I_13` (same witnesses apply, `{17,19}∩
  {13,19}` disjointness check not needed — `a_12,a_5` have core `{17}`,
  disjoint from `{13,19}`): `2` and `(3∨83)`
- `I_{17,19}`: identical shape to `I_17` (`a_2,a_9` have core `{13}`,
  disjoint from `{17,19}`): `(2∨3)` and `(2∨83)`
- `I_{13,17}`: only `(2∨3)` (from `a_11`, core `{19}`, disjoint from
  `{13,17}`) — the weakest of the 6, but sufficient since its only partner
  channel is against `I_19`, which has BOTH `2` and `3` unconditionally

**Case-split closure of all 5 remaining channels** (all elementary,
verified by hand):

- `({13},{19})`: both sides always have `2` (from `a_12`) → trivial, `W={2}`.
- `({17},{19})`: `i∈I_17` has `2∨(3∧83)`; `j∈I_19` has `2∧3`. If `i` has 2,
  matches `j`'s 2. Else `i` has both 3,83, matches `j`'s 3. `W={2,3}` even
  suffices (83 not actually needed for this specific channel, though
  `{2,3,83}` still works).
- `({17},{13,19})`: `i∈I_17` has `2∨(3∧83)`; `j∈I_{13,19}` has `2∧(3∨83)`.
  If `i` has 2, matches `j`'s 2. Else `i` has both 3,83; `j` has at least one
  of 3,83 — match. `W={2,3,83}`.
- `({19},{13,17})`: `i∈I_19` has `2∧3` (both, unconditional); `j∈I_{13,17}`
  has `2∨3`. Whichever of `{2,3}` `j` has, `i` has it too. `W={2,3}`.
- `({13},{17,19})`: `i∈I_13` has `2∧(3∨83)`; `j∈I_{17,19}` has `2∨(3∧83)`
  (same shape as `I_17`). If `j` has 2, matches `i`'s 2. Else `j` has both
  3,83; `i` has at least one — match. `W={2,3,83}`.

All 6 channels (incl. Theorem FW1's own) close under the single set
`H_extra = {2,3,83}` (channel `({19},{13,17})` only needs `{2,3}⊂{2,3,83}`).
Combined with `P_1`, candidate covering set for the WHOLE sequence:
**`H = {2,3,13,17,19,83}`** — this is exactly the identical set 3
independent methods converged on in round 4 for `a_1=4199`
(`current.md` round-4 entry: "a_1=4199 → {2,3,13,17,19,83} from all three
methods"), now backed by an explicit deductive mechanism rather than only
numerics. `L=lcm(2,3,13,17,19,83)=2,091,102` (if `H` is confirmed to
satisfy FCBC, Theorem 5.1 gives explicit `T=|Good|` and this `L`).

### 4. Numerical stress test of the whole candidate `H={2,3,83}∪P_1`

Independent check (not relying on the hand-derived logic above): built
per-index `H`-signatures (`rad(a_i)∩{2,3,83}`) over the full `N=20,000`
generated sequence and checked **every pair of realized signatures across
each of the 6 channels intersects** — complete (not sampled) check.
**Zero violations across all 6 channels** (largest: `I_17`×`I_13`, 10260×
4652 ≈ 47.7M signature-pairs, only 5×3=15 distinct signature pairs to check
since signatures collapse to few values — `I_17` has 5 distinct
`H`-signatures, `I_13` has 3). Also independently confirmed the "always"
claims used in the hand proof (`I_13`,`I_{13,19}` always have 2:
0/4652,0/259 violations; `I_19` always has 2 AND 3: 0/3028 violations for
each) with zero exceptions at this scale.

### 5. What's NOT yet done / risks for the outliner-builder

- This is a **derivation + numerical stress-test by an explorer**, not a
  reviewer-verified proof. The logic is elementary (finite case splits on
  disjunctions) but should be independently re-derived by the builder from
  scratch, the way the round-13 proof-reviewer did for Theorem FW1/FW2 —
  a subtle miscount of which witness's core is disjoint from which target
  class is an easy mistake (I made and caught exactly one such error while
  deriving channel `({19},{13,17})` — initially tried to reuse `a_2,a_9`
  which turned out invalid since `{13}∩{13,17}≠∅`, and only the pair-core
  witnesses `a_82,a_92` work).
- Formally, Theorem SW's 3-way case split (intersecting / one-side-finite /
  doubly-infinite) requires knowing whether each `I_S` is finite or
  infinite to know which certified lemma to cite. **This turns out not to
  matter for this specific argument**: Lemma WF's conclusion holds for
  literally every `k∈I_S` regardless of whether `I_S` is finite or
  infinite, so the witness-chaining case-split above directly gives
  `H∩rad(a_i)∩rad(a_j)≠∅` for every `i,j` in the relevant classes without
  first resolving finiteness — worth having the builder state this
  explicitly as a shortcut past Theorem SW's classification step (still
  correctly using Theorem SW's exhaustive case split as the umbrella, just
  skipping determining which of its 3 cases applies since the disjunctive
  facts subsume all of them).
- I did NOT re-derive Corollary FW2-FCBC-style final assembly (the 2-line
  argument combining Lemma SW1 for intersecting cores with these 6
  channel closures for disjoint cores) — this is direct and short (same
  shape as the already-certified Corollary FW2-FCBC for `a_1=247`) but
  should be written out formally.
- Did not compute `T` explicitly (needs Theorem 5.1's `|Good|`
  construction) — flagged as builder work, same as the `a_1=247` case.

### Candidate technique(s)

Extend the already-certified **Lemma WF (Witness Forcing) + Corollary P″**
mechanism (`lemma-WF-witness-forcing-and-theorem-FW-instances.md`) — no new
lemma needed, just more witness instantiations and a slightly more
elaborate (but still finite, elementary) case-split per channel than
Theorem FW1's single 2-case split.

### Cheap-kill candidates

None needed here — this is a positive/constructive lead, not a target to
prune. (For future reference: the pattern "does this witness's core
actually stay disjoint from the target class" is the one cheap check that
kills a wrong witness choice immediately — no need for heavy computation,
just an intersection check on 3-element sets.)

### Knowledge-base entries used

None new beyond what's already cited in the certified lemma files
(`lemma-P-prime-pairwise-intersecting.md`, `lemma-XC-NIDF-FT-cross-
companion-transversal.md`, `theorem-CD...`, `theorem-SW...`,
`theorem-5.1...`, `lemma-WF...`). This round's work is pure instantiation/
extension of already-certified machinery, not new KB retrieval.

### Analogous past problems (cruxes)

Not separately searched this round (dispatch was numerically/structurally
focused on the existing in-workspace mechanism) — round 6/9/11 already
did thorough crux-corpus sweeps for this problem family and found nothing
transplantable beyond what's already certified; no reason to expect a new
match specific to this narrow instantiation task.

### Prior progress

`a_1=247` fully solved (round 13, Theorem FW2 + Corollary FW2-FCBC).
`a_1=4199`'s channel `({13},{17})` fully solved (round 13, Theorem FW1).
The other 5 channels of `a_1=4199` were open coming into this round — see
above for this round's proposed closure of all 5.

### Dead ends (do not retry)

- Do not re-attempt Early/Bounded Stabilization ("two-in-a-row locks it")
  for Backbone Permanence — refuted round 13 (a_1=375, and TWO a_1=4199
  plateau counterexamples: core `{13,19}` 24-member plateau breaks, core
  `{17,19}` 108-member plateau breaks). Not relevant to this round's
  mechanism (witness-chaining needs no permanence/plateau argument at all —
  structurally different, this is why it succeeds where Backbone Permanence
  stalled on these exact same `a_1=4199` core pairs).
- Do not re-attempt Realized-Backbone/UCR or Matched-Witness for
  `4199:(13,17)` — both killed unconditionally in round 12 (Sandwich
  Uniqueness Lemma; hand counterexamples). Not relevant here either
  (witness-chaining is a 3rd, different mechanism, already the one that
  DID close this exact pair via Theorem FW1).

### Small-case / intuition notes (labeled as conjecture where not proven)

- **Conjecture-turned-likely-fact**: all 6 proper cores of `a_1=4199` are
  infinite (numerically: thousands of members each by `n=20,000`,
  steadily growing) — consistent with, but not required by, the argument
  above (Lemma WF doesn't care about finiteness).
- **Pattern worth flagging for the outliner**: the "pair-core" witnesses
  (`a_82,a_92` with core `{13,17}`, singleton comps `{2}`,`{3}`) were the
  key unlock for the one channel (`{19}` vs `{13,17}`) that the original 4
  Theorem-FW1 witnesses couldn't close alone — a 2-element core's
  complement in a 3-element `P_1` is a single element, so ANY witness with
  small/singleton comp in a 2-element core gives an unusually strong
  (fully unconditional, not just disjunctive) fact about the single
  complementary singleton class. For future `|P_1|=3` instances, searching
  specifically for singleton/small-comp witnesses among the **pair-core**
  classes (not just the singleton-core classes Theorem FW1 originally
  used) looks like a generally useful heuristic, not a `4199`-specific
  accident.
- The fact that `H={2,3,13,17,19,83}` matches round 4's independent
  3-method convergence (found via completely different tools — the
  minimal-radical-antichain/(MRS) machinery, not witness-chaining) is
  strong cross-validation that this really is the correct finite covering
  set for `a_1=4199`, not an artifact of the specific witnesses chosen.
