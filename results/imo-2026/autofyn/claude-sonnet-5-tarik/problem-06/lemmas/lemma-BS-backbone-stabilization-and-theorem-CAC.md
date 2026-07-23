# Lemma BS (Backbone Stabilization), Lemma BS-Dichotomy, and Theorem CAC
(Case A Closure of Conjecture (JW)) — certified WITH A SCOPE CORRECTION

**Source.** `results/imo-2026-06/approaches/sunflower-inadmissibility-
toolkit.md` §6–8 (round 12, new). Builds on the already-certified
`lemmas/lemma-P-prime-pairwise-intersecting.md` (Lemma P′),
`lemmas/lemma-ERD-realized-blocked-dichotomy.md` (Lemma ERD-C), and
`lemmas/lemma-UCR-universal-class-realization.md` (Lemma UCR, §1 of the
same approach file, unchanged from round 11).

**IMPORTANT — read this before citing anything below.** The proof-reviewer
(round 12) independently re-derived every step and confirms Lemma BS,
Lemma BS-Dichotomy, and Theorem CAC are all correctly proved **as stated**
— but the approach file's own §9–10 claim that this "closes Conjecture
(JW) ... for the entire infinite index classes ... not merely a finite
tested prefix" **for the 5 concrete listed instances** (`2747:(41,67)`,
`21528751:(103,197)`, `4199:(13,19)`, `4199:(17,19)`, `4087:(61,67)`) is
an **overclaim** and is explicitly **not** certified. See "Scope
correction" below — the certified content is strictly the three abstract/
conditional statements, not their claimed verification on any specific
numeric `a_1`.

## Setup / notation

Fix a sequence satisfying the problem's hypotheses, `P_1:=\mathrm{rad}
(a_1)`. For any index `i`, `S(i):=\mathrm{rad}(a_i)\cap P_1` (nonempty,
by the already-certified Theorem CD) and `\mathrm{comp}(a_i):=\mathrm{rad}
(a_i)\setminus P_1`. `I_S:=\{i:S(i)=S\}`.

## Lemma BS (Backbone Stabilization) — a pure EXISTENCE statement

**Statement.** Fix a proper core `S'\subsetneq P_1` with `I_{S'}` infinite.
Enumerate `I_{S'}` in increasing order `j_1<j_2<j_3<\cdots` and define
`B_k:=\bigcap_{t=1}^k\mathrm{comp}(a_{j_t})` for `k\ge1`. Then there
**exists** a finite `k_0$ with `B_k=B_{k_0}` for **every** `k\ge k_0`, and,
writing `B(S'):=B_{k_0}`,
$$B(S')=\bigcap_{j\in I_{S'}}\mathrm{comp}(a_j)\ \text{exactly, so}\quad
B(S')\subseteq\mathrm{comp}(a_j)\ \text{for every single }j\in I_{S'}.$$

**Proof.** `B_1=\mathrm{comp}(a_{j_1})` is finite, and `B_{k+1}\subseteq
B_k` for every `k`, so `|B_1|\ge|B_2|\ge\cdots\ge0` is a non-increasing
sequence of non-negative integers, hence eventually constant at some
finite `k_0\le|B_1|+1`. For `k\ge k_0`, `B_k\subseteq B_{k_0}` and
`|B_k|=|B_{k_0}|`, so `B_k=B_{k_0}`. Then `\bigcap_{j\in I_{S'}}
\mathrm{comp}(a_j)=\bigcap_{k=1}^\infty B_k=B_{k_0}` by the standard
nested-intersection identity (the tail is constant at `B_{k_0}`, and the
head consists of supersets of `B_{k_0}`). `\blacksquare` This proof is
correct, elementary, and genuinely says nothing about *which* `k_0` works
for a given `S'` — only that *some* finite `k_0` exists.

## Lemma BS-Dichotomy

**Statement.** Suppose `B(S')\ne\varnothing`. Let `C:=S'\cup B(S')`. By
Lemma ERD-C, exactly one of: (A) **Realized** — some index `j_0` has
`\mathrm{rad}(a_{j_0})=C` exactly (then automatically `j_0\in I_{S'}` and
`\mathrm{comp}(a_{j_0})=B(S')` exactly); (B) **Blocked** — some index
`j_3` has `\mathrm{rad}(a_{j_3})\cap C=\varnothing`, and `C` is never
realized. **Proof.** Direct application of Lemma ERD-C to `C` (nonempty by
hypothesis), with the branch-(A) core computation `S(j_0)=(S'\cup B(S'))
\cap P_1=S'` (using `S'\subseteq P_1`, `B(S')\cap P_1=\varnothing`).
`\blacksquare` **This dichotomy, applied to the abstract, true `B(S')`, is
exhaustive and correct** — but note it presupposes `B(S')` is already
known, which (per the scope correction below) is exactly the un-established
step for any concrete `a_1`.

## Theorem CAC (Case A Closure of Conjecture (JW)) — a CONDITIONAL theorem

**Statement.** Let `(S,S')` be a doubly-infinite disjoint core pair.
Suppose `B:=B(S')\ne\varnothing` and `S'\cup B` is realized at some
`j_0\in I_{S'}` (i.e. `(S,S')` is "Case A via the `S'`-side," §above).
Then Conjecture (JW) holds for `(S,S')` with witness set `W:=B`:
`\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap B\ne\varnothing` for every
`i\in I_S,\,j\in I_{S'}`.

**Proof.** Apply Lemma UCR with `"S":=S'`, `"C":=B` (valid: `B\cap P_1=
\varnothing`, `S'\cup B` realized at `j_0`), giving `B\cap\mathrm{comp}
(a_i)\ne\varnothing` for every `i\in I_S`. Fix `i\in I_S`, pick `p\in
B\cap\mathrm{comp}(a_i)`. By Lemma BS, `B\subseteq\mathrm{comp}(a_j)` for
**every** `j\in I_{S'}`; since `p\in B`, `p\in\mathrm{comp}(a_j)` too.
Hence `p\in\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap B` for every
`i\in I_S,j\in I_{S'}` simultaneously. `\blacksquare` This proof is correct
and genuinely avoids the previously-stuck `u=w` rigidity wall (the witness
`p` depends on `i` alone, and is guaranteed in `\mathrm{comp}(a_j)` for
*every* `j` by Lemma BS's unconditional containment — no two independently
-derived witnesses ever need to be shown equal).

## SCOPE CORRECTION (proof-reviewer, round 12) — the actual state of the
gap, and why the approach file's §9–10 overclaims

**The flaw.** Lemma BS proves stabilization *exists* at *some* finite
`k_0` — it does **not** tell us, for a specific proper core `S'` of a
specific `a_1`, what `k_0` is, nor does checking finitely many members
(e.g. observing `B_1=B_2=\{2,3,7\}` for `a_1=2747`'s `\{67\}`-class, using
only `a_3,a_{54}`) establish that this observed value equals the *true*
`B(S')`. A non-increasing sequence of subsets of a finite set can stay
constant for arbitrarily many steps and then still drop (elementary
counterexample: `\{2,3,7\},\{2,3,7\},\{2,3,7\},\{2,3\},\{2,3\},\{2\},
\dots` is a valid non-increasing chain, constant for 3 steps before
dropping) — Lemma BS gives no bound on how long such a "false plateau" can
last. This is the **identical** logical shape as this workspace's own
round-7 correction (a "zero exceptions through the tested range" claim for
escape depth was overturned by a counterexample found just past the tested
cutoff) and the round-11 UCR/WRP overclaim-hazard the approach file itself
explicitly (but, on this specific point, ineffectively) tried to guard
against.

**Why the file's own defense (§6, "why this is not the round-12 lemma-UCR
file's own overclaim-hazard") does not actually address this.** That
defense correctly shows Lemma BS **itself**, as an abstract existence
statement, makes no reference to a numerical bound `N` — true, and not in
dispute. But §9's *application* of Lemma BS to concrete instances
("`a_1=2747,(S,S')=(\{41\},\{67\})`: literal generation to `n=60` gives
exactly two class-`\{67\}` members ... both with `\mathrm{comp}=\{2,3,7\}`
exactly — confirms `B(\{67\})=\{2,3,7\}`") **does** commit exactly the
finite-prefix-to-infinite-class inference the defense claims to avoid:
checking that 2 (or, in the `21528751` case, up to `2929`) members agree
is consistent with, but does not prove, that the *true* `k_0` for that
class has already been reached.

**What this means for the Case A/Case B classification.** The dichotomy
itself (every doubly-infinite pair falls into exactly one of: `B(S')=
\varnothing`; nonempty+realized [Case A]; nonempty+blocked [Case B]) is a
correct *abstract* classification of the *true* `B(S')`. But **which**
branch a *specific* pair (e.g. `2747:(41,67)`) actually falls into is
**not established** by this round's work — only *numerically consistent
with* Case A. The negative instances (`247:(13,19)` both sides empty,
`4199:(13,17)`'s `\{17\}`-side empty) **are** rigorously established,
because proving `B(S')=\varnothing` (or `B(S')\subseteq` some specific
small set) needs only two or three disjoint/shrinking observed members — a
trivial, always-valid subset argument, not a permanence argument (see
`lemmas/lemma-sandwich-uniqueness.md`'s `4199:(13,17)` resolution, which
is **unaffected** by this correction for exactly this reason: it never
needs to pin down a *specific nonempty* value, only that the value is
*confined to* an already-observed small set, which is always immediate).
**Positive claims (`B(S')` equals a specific nonempty value, hence usable
as a witness set `W`) require ruling out all future shrinkage — this is
`Backbone Permanence` in its original (round-12-outline) sense, and it
remains exactly as open as before this round.** The outline-reviewer's own
pre-build assessment ("the crux, open, not proved... consistent with, not
a proof of, permanence") was correct and is not superseded by this round's
build.

## Certification (corrected scope)

**Certified, `solved`-quality, as pure abstract/conditional statements:**
Lemma BS (an existence-of-stabilization fact, general-purpose, no
dependency on any open hypothesis) and Theorem CAC (a conditional
implication: IF a doubly-infinite pair is Case A via one side THEN
Conjecture (JW) holds for it — fully proved, reusable). Lemma BS-Dichotomy
is certified as a correct abstract classification, with the caveat above
that determining which branch a concrete pair falls into is not addressed
by it alone.

**NOT certified — remains open, exactly as before this round:** that any
of the 5 listed concrete pairs (`2747:(41,67)`, `21528751:(103,197)`,
`4199:(13,19)`, `4199:(17,19)`, `4087:(61,67)`) is actually Case A. This
means Conjecture (JW), the Stabilization Conjecture, and hence the whole
problem's conclusion, remain **open** for every one of these specific
instances (including `a_1=2747` and `a_1=4087`, whose entire remaining
content — by the elementary fact that `|P_1|=2` leaves only one possible
disjoint core pair — reduces *exactly* to whether their respective
backbones are permanent; this is a genuine, valuable, and much sharper
reduction of the open content for these two instances specifically, but it
is a reduction, not a closure).

**What a future round needs to close Case A for a specific pair**: a
genuine Backbone Permanence proof — i.e. rule out, for the *specific*
observed candidate value `C` (e.g. `\{2,3,7\}` for `2747`'s `\{67\}`-side),
that any future member of `I_{S'}` ever has a companion set missing an
element of `C`. This is exactly the outline's original Step 2, still
unresolved; the outline's suggested routes (adapting Escape-Confinement/
Permanent-Inadmissibility to a single class) remain the concrete
unexplored next step, not superseded by anything in this round's build.
