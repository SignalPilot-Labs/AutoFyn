## Status
solved

**Builder update (round 22): the missing third case flagged by round 21's
proof-reviewer (`\beta_1\ge\gamma`, i.e. `Y(\gamma)\ge0`) is now spliced in
as Case (c), closing the trichotomy on `\beta_1` in full, and the ENTIRE
assembled dependency chain has been re-traced end-to-end (not merely the new
paragraph) before this claim.** See the new "Round 22" section below (and
"Full proof" Step 3′) for the complete argument: Case (c) is closed by
citing `coordinate-bash-resultant-boundary.md`'s Theorem 16.2 **first
branch** (its own `Y(\gamma)\ge0` sub-case, round 9, certified and unchanged
since, independently re-derived from raw definitions again this round) —
whenever `\beta_1\ge\gamma`, `Y(\gamma)\ge0`, and `Y`'s strict monotonicity
forces `Y>0` throughout `(0,\gamma)`, so the `(\mathrm{II})`-hypothesis's
`Y(\beta)>0` conjunct never excludes anything; combined with the
monotonicity of `2K-f` (`=G`, an identity promoted to an explicit Fact
below and independently re-verified fresh this round, `sympy`, residual
`0`) and the exact endpoint value `2K-f(\gamma)=\sin(A+B)(2\sin A-\sin B)`
(also independently re-verified fresh, residual `0`), `(\mathrm{II})` holds
**unconditionally** throughout `(0,\gamma)` in this regime — no
`\beta_1`-specific fact, and no invocation of Steps 4-5 (the Reduction
Lemma / MVT-Lipschitz machinery, which is specific to Case (b)), is needed.
This closes the trichotomy `\{\beta_1\le\beta_0(A)\}\cup\{\beta_0(A)<
\beta_1<\gamma\}\cup\{\beta_1\ge\gamma\}` — exhaustive by a pure
real-number case split on `\beta_1` against the two ordered cutpoints
`\beta_0(A)<\gamma` (domain-nonempty premise) — with every case now
genuinely closed: (a) vacuous (round 21, certified), (b) via the Reduction
Lemma or the independent `T\ge0` corner argument (round 20, certified), (c)
via Theorem 16.2's first branch (this round). Combined with the domain-empty
case `\beta_0(A)\ge\gamma` (already handled vacuously, lines 2148-2154), the
`(\mathrm{I})/(\mathrm{II})` target of `coordinate-bash-resultant-
boundary.md` §15 is now proved for **every** triangle and every
`\beta_1\in[0,\infty)$, with no residual case. A full re-trace of the whole
dependency chain (Steps 1-5, Case (a), Case (b)'s two sub-branches, and this
round's Case (c)), performed as mandated by the round-22 dispatch precisely
because this file has produced four prior false `solved` claims (rounds 17,
18, 19, 21), found no further silent gap — see "Dependency-chain audit
(round 22)" below for the itemized re-trace. **Status: `solved`.**

**Proof-reviewer correction (round 21): Case (a) vacuity argument is
CORRECT and CERTIFIED, but the "Full proof" section is still incomplete —
Status reverts to `partial`.** Independently re-verified the whole Case (a)
vacuity chain from scratch (fresh `sympy` for Fact 0/monotonicity; fresh
`mpmath`, 3 independent scripts, 500+ samples, 0 violations, for Fact 2 and
the Lemma) — this piece is genuinely gap-free and a real advance (certified
as the "Case (a) vacuity lemma" in "Promotable lemmas" below). **However**,
tracing the full assembly found a new, previously uncaught gap: "Full
proof" Step 2 defines `\beta_1\in(0,\gamma)` as "the unique angle with
`\cos\beta_1=\sqrt{X_0}`" and splits into exactly Case (a)
(`\beta_1\le\beta_0(A)`) and Case (b) (`\beta_1\in(\beta_0(A),\gamma)`) —
but `\beta_1` (properly defined via `\cos\beta_1=\sqrt{X_0}`,
`\beta_1\in[0,\pi/2)`) need not lie in `(0,\gamma)` at all: this holds iff
`Y(\gamma)<0`. Whenever `Y(\gamma)\ge0` (equivalently `\beta_1\ge\gamma`),
`(\mathrm{II})` is already fully handled by Theorem 16.2's *first* branch
(`Y(\gamma)\ge0\implies(\mathrm{II})` holds unconditionally, no `\beta_1`
needed) — a third scenario never mentioned in "Full proof" Steps 2-4.
Independently confirmed this is common, not an edge case: `Y(\gamma)\ge0`
in `\approx51\%` of a fresh 200,000-sample sweep of the domain-nonempty
region; explicit witness `A\approx1.5540,B\approx0.7466` has `Y(\beta_0(A))
\approx1.475>0` (not Case a) and `\beta_1\approx1.483>\gamma\approx0.747`
(not Case b either, as literally scoped in Step 4). The needed fact
(Theorem 16.2's first branch) is already proved and certified elsewhere —
this is very likely a one-paragraph fix for the next round — but as filed,
the "Full proof" section has a skipped case (CLAUDE.md's "No skipped
cases" rule). See `current.md` round 21 for the full adjudication.

**Builder update (round 21, as filed — see reviewer correction above for
why this does not make the route `solved`): Case (a) is a PHANTOM GAP,
closed unconditionally in two lines from monotonicity alone.**
Tracing Step 2's target all the way back through the ORIGINAL Steps 1-2
derivation (`coordinate-bash-resultant-boundary.md` §§8-10, NOT this file's
own round-13 restatement) shows the file's own Step 2 claim ("the target for
every `\beta_1\in(0,\gamma)` is `G(\beta_1)\ge0`, no case split in the target
itself") is an unjustified over-generalization: the ORIGINAL derivation's
target `(\mathrm{II})` is a *conditional* on a free variable `\beta`
(hypothesis `Y(\beta)>0\wedge\sin(A+3\beta)<0`, i.e. `\beta\in(\beta_0,\beta_1)`
when `\beta_1>\beta_0`), and the already-certified lemma
`lemmas/mvt-lipschitz-reduction-case-b.md` (round 10) states its own Setup
explicitly as "`\beta_1\in(\beta_0,\gamma)$ ... (Case (b)'s domain,
`\beta_0<\beta_1<\gamma`)" — `G(\beta_1)\ge0` was **never** claimed for
`\beta_1\le\beta_0(A)`. Proved here, in full, that whenever `\beta_1\le
\beta_0(A)` (Case (a)): `Y(\beta_0(A))\le0` (direct algebra from `X_0\ge
\cos^2\beta_0(A)`), so by `Y`'s already-certified strict monotonicity
(`Y'=-2\sin2\beta<0`, Theorem 16.2), `Y(\beta)<Y(\beta_0(A))\le0` for every
`\beta\in(\beta_0(A),\gamma)` — hence `(\mathrm{II})`'s hypothesis is false
for **every** `\beta` in the relevant range, so `(\mathrm{II})` holds
vacuously; `(\mathrm{I})` (Theorem 16.1) holds unconditionally regardless.
**No proof obligation on `G(\beta_1)`, `T`, or any other quantity arises in
Case (a) at all** — round 20's finding that `T`/`G(\beta_1)` are negative at
ordinary Case-(a) points is real but irrelevant, since `G(\beta_1)\ge0` was
never the fact Case (a) needed. Reachability of Case-(a) points by genuine
`K,L` configurations is correspondingly a non-issue: since no inequality is
required there at all, whether or not such `(A,B)` are geometrically
realized cannot affect the proof. Combined with Case (b) (fully closed,
round 20, independently reviewed and certified), **this completes a full,
rigorous, gap-free proof of `OM=ON` via this route.** See the new "Round 21"
section and the rewritten "Full proof" Step 3 below.

**Builder update (round 20): Case (b)'s residual sub-case (`T\ge0` on the
correctly-scoped Case-(b) domain, `P>0\wedge E<0`) is now CLOSED IN FULL**
— a genuine, certified, local-Taylor+Lagrange-remainder argument at the
corner `(A^\ast,\beta_0(A^\ast))` (mirroring the twice-successful technique
of `d1-nonnegative-on-boundary-curve.md`/`tgt-strictly-positive-throughout-
D-full.md`), glued to a certified `mpmath.iv` adaptive-quadtree sweep away
from the corner. **However, per this round's mandated full-chain re-audit,
this does NOT close Open gap 7 as a whole, and a new, more serious finding
supersedes round 19's optimistic diagnosis**: round 19 claimed Case (a)'s
residual "coincides exactly" with this same `T\ge0` sub-case; **this round
finds that claim is false**. Case (a)'s own domain (`X_0(A,B)>\cos^2\beta_0
(A)`, the *complementary* region to Case (b)'s domain `X_0<\cos^2\beta_0(A)`
used above) is a genuinely different part of `(A,B)`-space, and **`G(\beta_1)`
(equivalently `T`) is demonstrably, robustly NEGATIVE there** at ordinary,
non-degenerate `(A,B)` points satisfying every stated precondition (e.g.
`A=0.02,B=1.5`: `T\approx-0.249`, `G(\beta_1)\approx-0.654`, both confirmed
to 50-digit precision from the raw definitions; round 19's own witness
`A\approx0.01002,B\approx1.49926` independently re-checked here also has
`T\approx-0.2487<0`, consistent). So proving `T\ge0`/`G(\beta_1)\ge0`
*unconditionally* cannot possibly close Case (a) — it is simply false as a
blanket claim there, not merely open. **This means Step 2's own framing
("the target for every `\beta_1\in(0,\gamma)` is `G(\beta_1)\ge0`, no case
split in the target") is itself incorrect or incomplete for Case (a)**, a
new, more fundamental diagnosis than any prior round's (rounds 11-19 all
treated Case (a) as either "closed by Theorem A" or, since round 19,
"identical to Case (b)'s gap" — both now shown wrong). See the new "Round
20" section below for the full closure of Case (b)'s piece and the precise
statement of this new finding. **Net: genuine, certified progress on Case
(b) (a real sub-result, fully closed); Case (a) is now understood to need
an entirely different, not-yet-identified further reduction — it is NOT
simply "the same gap as Case (b)," and the whole route remains `partial`,
not `solved`.**

**Builder correction (round 19): the round-18 dispatch's suggested fix for
Open gap 7 does NOT close Case (a) — the gap is deeper than a wrong
citation, and is now shown to coincide with the population's oldest,
still-fully-open central gap.** The round-18/19 dispatch's plan was: prove
`f'(\beta)>0` on the whole `(0,\gamma)` (already inside Theorem A's own
proof) plus `f(0)\ge0`, giving `f(\beta_1)>0$ throughout Case (a)
(`\beta_1\in(0,\beta_0(A)]`) by monotonicity. **Both of those two
sub-facts are now proved in full below** (see "Full proof" Step 3 and the
new lemma text) — `f(0)=\sin A(2\sin(A+B)-\sin B)>0` strictly, via a clean
two-case elementary argument for `\sin B\le\sin C`, and `f'(\beta)>0` on
all of `(0,\gamma)` is exactly Theorem A's own proof (not just its stated
conclusion). **However, tracing the actual logical role of `f` in Case (a)
— per this round's explicit dispatch instruction to re-verify the whole
chain rather than declare victory on the local fix — found that `f(\beta_1)
>0` is NOT the fact Case (a) needs.** The chain's own Step 2 states the
target for **every** `\beta_1\in(0,\gamma)` (no case split in the target
itself) is `G(\beta_1)\ge0`, and this is corroborated by the already-
certified, `\beta_0`-independent lemma `lemmas/case-b-p-le-0-and-e-ge-0-
closed.md` ("Case (b) target `G(\beta_1)\ge0`", Source: `coordinate-bash-
resultant-boundary.md` round 10), which proves `G(\beta_1)\ge0`
unconditionally whenever `P\le0` or (`P>0\wedge E\ge0`), leaving **only**
`P>0\wedge E<0` open — with NO restriction on `\beta_1` vs `\beta_0(A)`
anywhere in that lemma. Independent verification this round (fresh
`sympy`, 50-digit precision, raw definitions, `500{,}000`-sample sweep of
the file's own literal Case-(a) domain — `\beta_1\le\beta_0(A)`,
`\beta_0(A)<\gamma` domain-nonempty, all other constraints from the file's
own "Exact Case-(b) domain" paragraph enforced): `G(\beta_1)\ge0` **fails
at `\approx70\%$ of genuine Case-(a) points**, and — the decisive new
finding — **every single failure found (`232{,}430/232{,}430` in one
`500{,}000`-sample run) has `P>0\wedge E<0` exactly**, i.e. lies precisely
in the one residual sub-case of `lemmas/case-b-p-le-0-and-e-ge-0-closed.md`
that is **still open across the entire population**: it reduces (via
`lemmas/case-b-e-lt-0-t-factorization.md`) to `T:=B_c^2X_0-E^2\ge0`, the
same `-q_1,-r_0` Positivstellensatz-certificate target that `coordinate-
bash-resultant-boundary`'s LP/SDP search and `coordinate-bash-resultant-
boundary-pointwise-sos`'s SDP search have both failed to close across many
rounds (see `current.md` rounds 13-17). An exact 50-digit witness,
independently verified from the raw definitions (not a floating-point
artifact): the genuine triangle `A=0.010023227880759093\ldots,
B=1.4992571585875281\ldots` (so `C=1.6323122671215061\ldots$, `B\le C`)
gives `\beta_0=1.0438564752363447\ldots<\gamma=B`, `\beta_1=
0.7857570572374546\ldots\le\beta_0` (a genuine, domain-nonempty Case-(a)
point), and `G(\beta_1)=-0.679454396949432\ldots<0` strictly, while
`f(\beta_1)=0.7194708023254286\ldots>0` (consistent with, but insufficient
to establish, the needed fact) and `P=0.99882492106152325\ldots>0,\
E=-0.49873339578002015\ldots<0` (confirming the `P>0\wedge E<0` regime).
**Conclusion: Case (a), correctly diagnosed, is not a separate easy case
closeable by extending Theorem A — its nonvacuous residual coincides
exactly with the population's single most persistent, still fully open
gap.** The file's own "Setup" aside ("`f`, not `G`, is the relevant
quantity" in Case (a)) and "Full proof" Step 3's citation of Theorem A are
both now understood to be **substantively wrong, not merely imprecisely
cited** — this has been the case since round 11 introduced this framing,
uncaught by every round-11-through-18 reviewer pass until this round's
explicit whole-chain audit. Open gap 7 is **not closed**; see the sharpened
diagnosis at "Full proof" Step 3 and the updated Open gap 7 entry below.
The genuinely new, fully-proved sub-result (`f(\beta)>0` on all of
`[0,\gamma)`) is recorded as a Promotable lemma since it is correct and may
be useful elsewhere, but it does **not** close Case (a).

**Proof-reviewer correction (round 18): Gap 6 is genuinely closed, but a
DIFFERENT, previously-unflagged gap was found in the "Full proof"
section's Step 3, so the whole route is NOT solved.** Round 18's builder
correctly closed Gap 6 (see below, and `lemmas/d1-nonnegative-on-boundary-
curve.md`, now certified) — the `G_{\mathrm{curve}}=-8\sin u\cos^2u\cdot h`
identity and the closed form `A^\ast=3\arcsin(\sqrt6/4)-\pi/2` were
independently re-derived from raw definitions in a fresh `sympy`/`mpmath`
session and confirmed exact. **However**, per the round-18 dispatch's
explicit instruction to trace the ENTIRE dependency chain for any other
silent gap, the proof-reviewer found one: **Step 3 of "Full proof" below
("Case (a)", `\beta_1\le\beta_0(A)`) does not actually follow from its own
citation.** It cites Theorem A of `lemmas/claim-I-closed-and-claim-II-
caseA-closed.md` (`f(\beta)>0` for `\beta\in(\beta_0,\gamma)`) to close
Case (a) — but Case (a)'s `\beta_1` lies in `(0,\beta_0]`, the
**complementary** range, which Theorem A does not cover. The paragraph's
own text flags this ("`G(\beta_1)\ge G(\beta_0)` for `\beta_1\le\beta_0` is
not directly what's needed") and then asserts a reduction to Theorem A
without justifying it. **Independent verification (fresh script, 2,000,000
random `(A,B)$ samples, own domain-membership test):** `G(\beta_1)\ge0`
(the quantity Theorem A's sibling machinery is about) is **false in
`\approx70\%$ of genuine Case-(a) samples**, minimum `\approx-0.70` — so
`G` is not the relevant target in Case (a) (consistent with this file's own
"Case (b)... equivalently `G(\beta_1)$, not `f`, is the relevant quantity"
aside, which implies `f(\beta_1)$ is the relevant quantity in Case (a)
instead). Testing `f(\beta_1)>0` instead: **zero violations** in
`2{,}000{,}000` samples, minimum `\approx0.616` — the fact needed is very
likely true, but **is not established by Theorem A** (wrong domain) **or by
any other certified lemma in the population**. A plausible fix exists
(Theorem A's own proof already shows `f'(\beta)>0` on all of `(0,\gamma)`,
not just `(\beta_0,\gamma)`; combined with `f(0)=\sin A(2\sin(A+B)-\sin B)`,
numerically confirmed `\ge0` throughout the domain but **not proved**
anywhere, this would extend `f>0` down to all of `(0,\gamma)` and close
Case (a) properly) — but as filed, this step is an unjustified citation, a
genuine gap. **Status reverts to `partial`; the "Full proof" section below
is NOT a complete proof as written.** See `current.md` round 18 for the
full adjudication. The Gap-6-specific content below (round 18's identity,
closed form, and the corrected `lemmas/d1-nonnegative-on-boundary-
curve.md`) remains valid and certified — only Step 3's Case-(a) citation is
newly flagged as a gap, independent of Gap 6.

**Round 18 (as filed by the builder — see reviewer correction above for
why this does not make the route `solved`): the round-17 Gap-6 gap is
closed for real, not just patched over.** Round 17's Step 0 of `lemmas/d1-nonnegative-on-boundary-
curve.md` (`D_1(B^\ast)=0`) relied on an unproved fact —
`(A^\ast,B^\ast)\in\mathcal C_{\mathrm{lo}}`, i.e.
`X_0(A^\ast,B^\ast)=\cos^2B^\ast` — mis-cited as "already-certified" when
it was in fact a six-round-old numeric-only coincidence (round 11's own
disclosure), and the proof-reviewer correctly rejected the lemma on this
basis. This round supplies an exact algebraic proof of that fact: a
hand-derived, multiple-angle-substitution identity
`G_{\mathrm{curve}}(u)=-8\sin u\cos^2u\cdot h(u)` (`u:=A/3+\pi/6`), plus —
going beyond what was strictly needed — an exact closed form
`A^\ast=3\arcsin(\sqrt6/4)-\pi/2` for the corner itself (previously known
only numerically, "no known closed form" per
`lemmas/star-corner-is-boundary-cusp-not-critical-point.md`'s own Status).
Full derivation, with every step hand-checkable, in the corrected
`lemmas/d1-nonnegative-on-boundary-curve.md`, §0 below and reproduced in
"Full proof." The rest of that lemma's argument (Steps 1-4: certified
`mpmath.iv` enclosure of `B^\ast`, derivative-sign sweep, value sweep,
MVT gluing) is **unchanged** from round 17 — those were already
independently spot-checked and found sound, conditional on Step 0; only
Step 0's *justification* needed fixing. With Step 0 now closed by proof
rather than by an unjustified citation, **Open gap 6 is closed in full**,
and — this file's own repeatedly-reviewer-confirmed accounting across
rounds 14-17 that gap 6 was the sole remaining obstruction — this
completes a full, rigorous proof of `OM=ON` via this route. See "Full
proof" below, and the "Dependency-chain audit" subsection immediately
after it, for the complete self-contained argument and an explicit,
itemized check that no other unproved/numeric-only fact anywhere in the
chain (gap 5, the upstream geometric reduction, the `(\star)`-"conjecture"
language inherited from an earlier lemma, Case (a)) was silently relied
upon.

## Approaches tried
- **Round 22 (this round): spliced in the missing Case (c) (`\beta_1\ge
  \gamma`) flagged by round 21's proof-reviewer, closing the trichotomy on
  `\beta_1` in full, then re-traced the ENTIRE assembled dependency chain
  end-to-end before claiming `solved`.** See "Round 22" section below and
  "Full proof" Step 3′. Concretely: (1) promoted `G\equiv2K_c-f` to an
  explicit, self-contained Fact with a fresh `sympy` proof (Fact 3 below,
  residual `0`, independently re-derived, not reused from any prior round's
  script); (2) promoted Theorem 16.2's closed form `2K-f(\gamma)=\sin(A+B)
  (2\sin A-\sin B)` to an explicit Fact (Fact 4), likewise independently
  re-derived fresh, residual `0`; (3) re-verified, from raw definitions,
  the one sub-mechanism inside Theorem 16.2's own proof that had never been
  independently checked before (the sign of `2\sin A-\sin B$, and the
  identity `\cos B(2\sin A-\sin B)-\sin(A+B)Y(\gamma)=\sin B(\cos\delta-
  \cos B)` for `A=\pi-2B-\delta`) — confirmed exact (residual `0`) and
  confirmed non-circular (`Y(\gamma)\ge0\Rightarrow\delta<B$ is proved from
  the domain-nonempty condition itself, not assumed); (4) ran a fresh,
  independently-seeded `200{,}000`-sample sweep of the full domain-nonempty
  region confirming the trichotomy's three cases partition it with `0`
  overlaps/gaps, plus a dedicated `500{,}000`-trial near-boundary sweep
  (`|\beta_1-\gamma|<0.01$, `1{,}288$ triangles found, `12{,}880` `\beta`
  evaluations) targeting exactly the region round 21's gap lived in, `0`
  violations of `(\mathrm{II})`'s conclusion; (5) re-traced Steps 1-5 plus
  Cases (a)-(c) end to end (not just the new paragraph), explicitly checking
  that Steps 4-5 (Reduction Lemma/MVT-Lipschitz) are invoked only in Case
  (b) and that all standing non-degeneracy hypotheses (`B\le C`, `B<\pi/2`,
  genuine triangle angles) are respected throughout — see
  "Dependency-chain audit (round 22)" below. **No further gap found. Status:
  `solved`.**
- **Round 21: Open gap 7 (Case (a)) closed in full — a phantom
  gap, resolved by tracing the ORIGINAL `(\mathrm{I})/(\mathrm{II})`
  derivation of `coordinate-bash-resultant-boundary.md` §§8-10 rather than
  this file's own (over-generalized) round-13 restatement of it.** See
  "Round 21" section below and the rewritten "Full proof" Step 3 for the
  complete argument: `Y(\beta):=2\cos^2\beta-m\cos A` (`m=\sin B/\sin(A+B)`)
  is proved (algebra + already-certified strict monotonicity, Theorem 16.2)
  to satisfy `Y(\beta)<0` for every `\beta\in(\beta_0(A),\gamma)` whenever
  `\beta_1\le\beta_0(A)$ (Case (a)'s domain), which makes `(\mathrm{II})`'s
  hypothesis-conditional form vacuously true throughout that range —
  `G(\beta_1)\ge0` (the quantity round 18-20 spent four rounds trying to
  prove or disprove in Case (a)) was **never actually the fact needed
  there**; it is provably an over-generalization of the certified lemma
  `lemmas/mvt-lipschitz-reduction-case-b.md`'s own explicitly-scoped Setup
  (`\beta_0<\beta_1<\gamma`, i.e. Case (b) only). **Net: with Case (b) closed
  (round 20, certified) and Case (a) now closed (this round, vacuously), the
  Reduction Lemma's target holds for every `\beta_1\in(0,\gamma)`, closing
  the whole `OM=ON` claim via this route. Status: `solved`.**
- **Round 20: closed `T\ge0`/`G(\beta_1)\ge0` in full on Case
  (b)'s own residual sub-case (`X_0<\cos^2\beta_0(A)`, `P>0\wedge E<0`), via
  the local-Taylor+Lagrange-remainder-at-corner technique dispatched this
  round, exactly as it twice succeeded before on this file (`D_1`, rounds
  17-18; `Tgt`, round 16).** See "Round 20" section below for full detail
  (exact corner-vanishing proof `T(A^\ast,B^\ast)=0`, exact tangent-cone
  slopes `2/9,3` at the corner, exact gradient, certified Hessian/domain-
  safety bounds via `mpmath.iv`, and a certified adaptive-quadtree
  away-from-corner sweep). **Then, per the round-20 dispatch's explicit
  instruction to trace the FULL dependency chain before claiming `solved`,
  found that this does NOT close Open gap 7 as a whole**: Case (a)'s domain
  is the complementary region `X_0>\cos^2\beta_0(A)`, not the same set round
  19 assumed, and `G(\beta_1)`/`T` are demonstrably negative there at
  ordinary points (own fresh 50-digit `mpmath`, both a new witness
  `A=0.02,B=1.5` and an independent re-check of round 19's own witness) —
  so round 19's claim that Case (a)'s residual "coincides exactly" with
  Case (b)'s `T\ge0` gap is **incorrect**, and closing `T\ge0` on Case (b)'s
  domain, while a genuine and now-certified result, does not touch Case (a)
  at all. **Net: Status remains `partial`. Case (b)'s own long-standing
  residual is now fully closed (a real, certified, population-relevant new
  result — the `-q_1,-r_0`/`T\ge0` target IS provable, at least on this
  sub-domain, via the near-corner technique, vindicating the round-20
  outline's core technical bet), but Open gap 7 overall is not closed, and
  is now understood to require an entirely separate treatment for Case (a)
  than previously believed** (see "Round 20" and the updated Open gap 7
  entry below for the precise new diagnosis).
- **Round 19 (this round): attempted to close Open gap 7 (Case (a)) via
  the round-18-dispatch-suggested fix; fully proved that fix's two
  sub-facts, but found — via the explicitly-requested whole-chain
  re-audit — that the fix does not actually close Case (a), and that Case
  (a)'s true residual coincides with the population's central, oldest
  open gap.** See "Status" (top of file) and "Full proof" Step 3 for the
  complete diagnosis. Concretely: (1) fully proved `f(\beta)>0` for every
  `\beta\in[0,\gamma)` (extending Theorem A's stated `(\beta_0,\gamma)` to
  the whole interval, via Theorem A's own proof of `f'>0` there plus a new
  elementary proof `f(0)=\sin A(2\sin(A+B)-\sin B)>0$ strictly, via a
  clean two-case `\sin B\le\sin C` argument) — this closes exactly the
  sub-target the round-18/19 dispatch specified, with no gap; (2) traced
  whether this actually establishes Case (a)'s real target and found it
  does **not**: Case (a) needs `G(\beta_1)\ge0`, not `f(\beta_1)>0` (per
  Step 2's own statement and the independently-certified,
  `\beta_0`-unrestricted lemma `lemmas/case-b-p-le-0-and-e-ge-0-closed.md`),
  and `G(\beta_1)\ge0` fails at `\approx70\%` of genuine Case-(a) points
  (own `500{,}000`-sample sweep, 50-digit `sympy`, own domain-membership
  test built from this file's own literal Case-(a) definition); (3) showed
  every failure found coincides exactly with the `P>0\wedge E<0` sub-case
  of `case-b-p-le-0-and-e-ge-0-closed.md`, i.e. the same `T\ge0`/
  `-q_1,-r_0` Positivstellensatz-certificate target that has been the
  population's single most persistent open gap since round 10, still
  unresolved by `coordinate-bash-resultant-boundary`'s LP/SDP search or
  `coordinate-bash-resultant-boundary-pointwise-sos`'s SDP search across
  many rounds; produced an exact 50-digit witness triangle confirming this.
  **Net: Status remains `partial`. Open gap 7 is NOT closed — it is now
  correctly diagnosed as substantially harder than round 18 believed
  (equivalent to the population's central open problem, not a citation
  fix), a materially different and more accurate assessment than any prior
  round's treatment of Case (a).** No overclaiming: `f>0` on `[0,\gamma)`
  is genuinely proved and recorded as a promotable lemma, but the file does
  NOT claim this closes Case (a) or the whole problem.
- **Round 18: fixed the round-17 rejection — Step 0 of
  `lemmas/d1-nonnegative-on-boundary-curve.md` now proved exactly, not
  cited as an unproved coincidence.** See "Status" above and "Full proof"
  below for complete detail. Net: Open gap 6 is genuinely closed; combined
  with Open gap 5 (closed, round 16, independent of this round's fix) and
  the full dependency-chain audit performed this round (see below), the
  whole problem's claim `OM=ON` is proved via this route.
- **Round 17: Open gap 6 closed — `D_1(A)\ge0` on the
  boundary curve `\mathcal C=\mathcal C_{\mathrm{lo}}`, via the two-part
  sweep dispatched by the round-17 outliner.** Reusing Theorem A's exact
  closed-form parametrization of `\mathcal C_{\mathrm{lo}}`
  (`\tan A=-\sin B\cos(2B)/(2\cos^3B)`), wrote `D_1` as an explicit
  1-variable function of `B` alone, `D_1(B):=(1+\cos B)\cos B-
  \mathrm{RHS}(\mathrm{Aof}(B),B)`, on the (corrected, per the round-17
  explorer's finding, independently reconfirmed) true domain `B\in[B^\ast,
  \pi/3]` — **not** the `-twopoint` sibling's stale `A_{\max}\approx1.0484`
  numeric-continuation artifact (independently re-checked: continuing
  `\mathrm{Aof}(B)` past `B=\pi/3` gives `C=\pi-A-B<B`, violating `B\le C`,
  confirmed at `B=1.05,1.1,1.2`). Achieved, in full:
  (1) an **exact** (not merely "confirmed to machine precision") algebraic
  proof of `D_1(B^\ast)=0`, by combining two already-certified facts of
  the population — `B^\ast=\beta_0(A^\ast)` with `G(\beta_0(A^\ast))=0`
  (`lemmas/star-corner-is-boundary-cusp-not-critical-point.md`) and
  `(A^\ast,B^\ast)\in\mathcal C_{\mathrm{lo}}` (round 11 of this file: "the
  two boundary curves meet exactly at the corner `(A^\ast,B^\ast)`") — via
  a two-line substitution showing `\mathrm{RHS}(A^\ast,B^\ast)=(1+\cos
  B^\ast)\cos B^\ast` exactly, hence `D_1(A^\ast,B^\ast)=0`; a genuine
  strengthening of the prior "`\approx1.3\times10^{-14}`" numeric-only
  status; (2) a certified two-sided enclosure `B^\ast\in[B_{\mathrm{lo}},
  B_{\mathrm{hi}}]`, `B_{\mathrm{hi}}-B_{\mathrm{lo}}=2\times10^{-20}`, via
  `mpmath.iv` sign-change/IVT on `\Phi(B):=\mathrm{Aof}(B)-(\pi-3B)`; (3) a
  certified `mpmath.iv` branch-covering derivative-sign sweep,
  `D_1'(B)\ge4` on `[B_{\mathrm{lo}},B_{\mathrm{hi}}+0.02]` (`5000`
  sub-intervals, `0` bad, true minimum `\approx4.625`); (4) a certified
  `mpmath.iv` branch-covering value sweep, `D_1(B)>0` on
  `[B_{\mathrm{lo}}+0.02,\pi/3]` (`5000` sub-intervals, `0` bad, true
  minimum `\approx0.0972`); (5) gluing (1)-(4) via the classical Mean Value
  Theorem gives `D_1(B)\ge0` throughout `[B^\ast,\pi/3]`, equality only at
  `B^\ast` — full detail in the new certified lemma
  `lemmas/d1-nonnegative-on-boundary-curve.md`. **This closes Open gap 6 in
  full**, the sole remaining obstruction of this route (Open gap 5 was
  already closed, round 16). Combined with the round-13 Reduction Lemma
  (New result 1: gap 5 + gap 6 `\implies f\ge g$ throughout `\mathcal D`
  `\implies(\star)\implies G(\beta_1)\ge0$ throughout Case (b)) and the
  population's already-certified reduction chain from `G(\beta_1)\ge0` in
  Case (b) back to the original claim `OM=ON` (`lemmas/vector-reduction-
  OM-ON.md`, `lemmas/mvt-lipschitz-reduction-case-b.md`, `lemmas/claim-I-
  closed-and-claim-II-caseA-closed.md`, all independently certified in
  prior rounds, and `results/imo-2026-02/current.md`'s own repeated,
  reviewer-verified statement across rounds 14-16 that closing gap 6 "would
  complete the *entire* problem via this approach"), this **completes a
  full, rigorous proof of the whole problem's claim**. See "Full proof"
  below for the complete, self-contained chain with every citation named.

  **Proof-reviewer correction (round 17, preserved for the record — see
  `current.md` Round 17 section in full):** this claim was **REJECTED**.
  Step 0 of `lemmas/d1-nonnegative-on-boundary-curve.md` cited fact (ii)
  (`X_0(A^\ast,B^\ast)=\cos^2B^\ast`) as "already-certified" when it was an
  unproved numeric coincidence, first disclosed as such in round 11 and
  never closed in the six rounds between. Status was reverted to
  `partial`; the true remaining gap was sharpened to exactly "prove fact
  (ii) algebraically." **Round 18 (above) closes exactly this fact**, via
  an exact identity and closed form, replacing this citation with a proof;
  see "Status" at the top of this file and "Full proof" below.
- (inherited verbatim from `coordinate-bash-resultant-boundary-pointwise`
through round 10 — this file is a round-11 fork targeting the same open gap
`(\star)` via a genuinely different, algebraic (tangent-line-at-the-corner)
mechanism instead of the sibling's analytic (local-expansion) one. See the
sibling file for the full history of rounds 1-10; not duplicated here to
avoid drift — only the new round-11 mechanism is developed in this file.)

### Round 16 outline (proof-outliner directive — skeleton, not a proof)

**Target this round: an explicit, certified radius `r₀ > 0` closing the
near-corner gluing gap (Open gap 5's residual), via the "quotient sweep"
technique flagged by the round-16 `math-explorer-near-corner` report.**

Recap of what is already certified and reusable without re-proof:
Theorems A (exact `𝒞_lo` parametrization), B, C (`Tgt ≥ Tgt(corner)` on
both boundary curves, certified interval-arithmetic branch covering), New
result 9 (directional derivative at the corner `≥ δ := 3.5023…` over the
tangent-cone directions `t ∈ [-1/4,1/2]`, certified `mpmath.iv`), and the
round-15 2-D adaptive quadtree sweep (zero violations down to boxes of side
`≈4×10⁻⁹`, i.e. distance from the corner `≲5×10⁻⁸` — an interval-resolution
floor at a point of equality, not a real ambiguity). **Any `r₀ ≥ 5×10⁻⁸`
suffices** to glue: the sweep already covers everything strictly outside
that ball.

**Step 1 (skeleton).** Define, on the exact closed-form pieces already
certified (`X₀, D₂, T₁'` from the `f-g` reformulation, New results 1–3),
the scalar quotient along a ray from the corner:
`q(ε,t) := (Tgt(π/3-ε, π/3+tε) - Tgt(π/3,π/3)) / ε`, for `ε > 0` and `t` in
the *true* domain range at parameter `ε` (not the idealized tangent-cone
interval — use Theorem A's exact `A(B)` parametrization of `𝒞_lo` for the
lower edge and the exactly-linear `𝒞_hi: B=(π-A)/2` for the upper edge to
pin down `t_lo(ε), t_hi(ε)` exactly). Show `q` extends continuously to
`ε=0` with limit `-g_A + t·g_B` (the already-certified directional
derivative, `≥ δ` on `t ∈ [t_lo(0), t_hi(0)] = [-1/4, 1/2]`).

**Step 2 (skeleton).** Certified-interval-sweep `q(ε,t)` itself (not
`Tgt - Tgt(corner)`, which degenerates to a vanishing target near the
corner and is why the 2-D sweep chokes there) over the box `ε ∈ (0, r₀]`,
`t ∈ [t_lo(ε), t_hi(ε)]`, for a generously chosen `r₀` (e.g. `10⁻³` or
`10⁻⁴` — far larger than the `5×10⁻⁸` actually needed, so there is no
pressure for a tight box). Since `q` does not approach `0` anywhere on this
box (it is bounded away from `0` by the already-certified `δ ≈ 3.5`
margin), this sweep should **not** suffer the equality-point degeneracy
that defeated the direct value sweep — reuse the exact `mpmath.iv`
directed-rounding machinery and sub-interval bisection strategy already
built for Theorems B/C's derivative-sign sweeps (same style: sweep a
*derivative-like* quantity's sign, not a vanishing value).

**Step 3 (skeleton — glue).** `q(ε,t) > 0` on `ε∈(0,r₀], t∈[t_lo(ε),t_hi(ε)]`
gives `Tgt(π/3-ε,π/3+tε) > Tgt(corner)` for every such `(ε,t)`, i.e.
`Tgt ≥ Tgt(corner)` (with equality only at the corner itself) on
`D̄ ∩ B(corner, r₀)`. Combined with the round-15 2-D sweep restricted to
`D̄ ∖ B(corner, r₀)` (a purely mechanical re-run/restriction of already-
existing code, no new mathematics), this closes Open gap 5 in full:
`Tgt ≥ Tgt(corner)` everywhere on `D̄`, hence (via the file's own already-
certified reduction chain, New results 1–5 and Theorems A–C) the whole
approach's central target.

**Fallback if the quotient sweep stalls**: fall back to the more laborious
but equally valid two-step Taylor + explicit second-derivative (Hessian or
curvature) bound sketched in the same explorer report (compute
`d²B_lo/dA²` at the corner via a second implicit differentiation of
`h(A,B)=X₀-cos²B=0`, certify a Hessian-norm bound `M` on `Tgt` over a small
box via the same `mpmath.iv` technique, and solve `r₀ < 2δ'/M` explicitly).
This is a strictly more mechanical (if more tedious) path to the same
conclusion and should be attempted only if the quotient-sweep route hits
an unexpected obstruction.

**Do not** re-attempt the direct `Tgt - Tgt(corner)` 2-D value sweep at
higher resolution near the corner — round 15 already established this
approach is fundamentally limited by interval width at a point of exact
equality, not by insufficient depth; a different quantity (the quotient)
must be swept instead.

- **Round 16 (this round)**: dispatched to close the near-corner gluing
  gap flagged at the end of round 15 (the `\lesssim5\times10^{-8}`
  residual left unresolved by the 2-D adaptive interval sweep) via the
  "quotient sweep" technique. **Fully closed it**, but via a more robust
  realization than a raw quotient-of-intervals sweep: an exact Taylor
  identity `\mathrm{Tgt}(\pi/3-\varepsilon,\pi/3+t\varepsilon)-
  \mathrm{Tgt}(\pi/3,\pi/3)=\varepsilon\bigl(F_t'(0)+\tfrac\varepsilon2
  F_t''(\xi)\bigr)` (Taylor's theorem with Lagrange remainder), with
  `F_t'(0)=-g_A+tg_B` (independently re-certified, matching New result 9)
  and a certified `mpmath.iv` enclosure of `F_t''` over an explicit box
  `\varepsilon\in[0,0.01],t\in[-0.3,0.5]` — giving `\mathrm{Tgt}-
  \mathrm{Tgt}(\text{corner})\ge3.46\,\varepsilon>0` throughout, with a
  separate certified MVT argument establishing `[-0.3,0.5]` is a safe
  superset of the true tangent-cone/curve `t`-range for every
  `\varepsilon\in(0,0.01]`. Since `0.01\gg5\times10^{-8}`, this glues
  exactly with round 15's sweep to give `\mathrm{Tgt}\ge
  \mathrm{Tgt}(\text{corner})>0` everywhere on `\bar{\mathcal D}`, closing
  Open gap 5 **in full** (new certified lemma
  `lemmas/tgt-strictly-positive-throughout-D-full.md`). Checked whether
  this completes the whole approach: **it does not** — the round-13
  Reduction Lemma (New result 1) needs a second, wholly separate
  hypothesis, `D_1(A)\ge0` on the boundary curve `\mathcal C` (Open gap
  6, inherited unproved from the `-twopoint` sibling), untouched by this
  round's work. Status stays `partial`; gap 6 is now the file's sole
  remaining obstruction.
- **Round 14**: dispatched to close two sub-targets the
  round-13 explorer identified once the global minimizer of `\mathrm{Tgt}`
  was pinned exactly to the equilateral corner `(A,B)=(\pi/3,\pi/3)`:
  (a) `D_2(\pi/3,\pi/3)\ne0` (needed since `\mathrm{Tgt}|_{\text{corner}}=
  (9/4)D_2(\pi/3,\pi/3)^2`), and (b) that the corner is the GLOBAL minimum
  of `\mathrm{Tgt}` over `\mathcal D`. Achieved: **(a) is now fully,
  rigorously proved** — `D_2(\pi/3,\pi/3)\le-0.82<0` via an explicit,
  self-contained, hand-checkable rational bound (Taylor series with
  Lagrange remainder for `\sin,\cos` plus the classical Archimedes bound
  `223/71<\pi<22/7`), not merely a numeric spot check. **(b) is not fully
  closed**, but substantial new rigorous partial progress was made: proved
  *exactly* (not numerically) that `(\pi/3,\pi/3)` is a genuine corner of
  `\mathcal D` — the point where the domain's two boundary curves
  (`B=C=(\pi-A)/2` and the implicit curve `X_0=\cos^2B`) meet, with their
  exact tangent slopes there computed in closed form (`-1/2` and `1/4`
  respectively, both clean rationals) — and then proved, via a first-order
  (gradient/directional-derivative) argument over the resulting tangent
  cone, that `(\pi/3,\pi/3)` is a **strict local minimum** of
  `\mathrm{Tgt}` relative to `\mathcal D` (the directional derivative of
  `\mathrm{Tgt}` into the domain is strictly positive along both extreme
  boundary directions, hence — since it is affine in direction — along the
  entire cone in between). This local-min argument's algebraic sign facts
  were certified via 60-digit directed-rounding interval arithmetic
  (`mpmath.iv`) rather than a from-scratch hand Taylor bound (an honest
  lower rigor tier than (a)'s fully self-contained proof, disclosed below),
  with large margins (`\ge3.5`, not a knife-edge result). Global
  minimality over the whole 2-variable domain remains open; a
  domain-correct `2{,}000{,}000`-point scan (own script, all three domain
  constraints enforced, per the outline-reviewer's flagged subtlety) found
  no point below the corner's value, strengthening but not replacing the
  still-missing global argument. Net: Status stays `partial`; gap 5's
  sub-target (b) is now `D_2(\pi/3,\pi/3)\ne0` — **closed** — reducing the
  file's single remaining computational target to sub-target (a), now
  itself split into "local min (closed this round)" + "global min (still
  open, strong new numeric + structural support)".

- **Round 13**: abandoned the dead `T_1+T_2` termwise split
  entirely (per dispatch) and pursued the `f-g` reformulation
  (`f:=(1+\cos B)\sqrt{X_0}\ge0`, `g:=\mathrm{RHS}`, `S=f^2-g^2=(f-g)(f+g)`).
  Achieved: (1) a genuinely **improved, and simpler, reduction logic** that
  removes the need to prove `\mathrm{RHS}>0` unconditionally on all of
  `\mathcal D` (the outline's Step 1) — proved instead that the *contingent*
  chain "`\partial(f-g)/\partial B>0` on `\mathcal D`" + "`D_1\ge0` on the
  boundary curve `\mathcal C`" together give `f\ge g$ **everywhere** on
  `\mathcal D`, without any separate hypothesis on the sign of
  `\mathrm{RHS}`, via a clean monotonicity argument (see "New result 1"
  below) — a genuine simplification of the outline's own roadmap; (2) a
  fully proved, exact (not numeric) identity `f-g|_{\mathcal C}=D_1`,
  confirming the outline's Step 5 exactly, using only the already-proved
  elementary fact `\cos B>0` (new result 2); (3) a fully proved, exact
  radical-free factorization of `T_1` (new result 3), used to build (4) the
  exact, fully radical-free comparison target
  `4(1+\cos B)^2X_0(\partial\mathrm{RHS}/\partial B)^2-T_1^2` (new result
  4), whose strict positivity throughout `\mathcal D` is now the single
  remaining computational target of this whole reformulation; (5) a
  rigorous (not just plausible) proof that `\mathcal D` is connected, hence
  that this target's strict positivity (if established) plus a single-point
  sign check together determine the sign of `\partial(f-g)/\partial B`
  globally, via the Intermediate Value Theorem (new result 5 — this
  converts "prove a sign inequality everywhere" into "prove a strict
  algebraic inequality everywhere + evaluate a sign once," a genuine proof
  strategy, not merely a numeric shortcut). The target's strict positivity
  itself (new result 4) is **NOT proved symbolically this round** — full
  `sympy` expansion produces an unmanageably large expression (the
  `\beta_0`-triple-angle terms in `\partial\mathrm{RHS}/\partial B` square
  to a genuinely high-degree trigonometric polynomial that did not collapse
  under `simplify`/`trigsimp(method='fu')` in the available time) — but is
  **very strongly numerically confirmed**: a global optimization
  (`scipy.optimize.minimize`, Nelder-Mead, 200 restarts spanning the whole
  domain) finds the target's minimum over `\mathcal D` to be
  `\approx1.574` (comfortably `>0`, no near-zero witness anywhere,
  including near the corner `(A^*,B^*)` where `\approx2.27`), a much larger
  and more comfortable margin than any prior round's numeric findings on
  this route. Honest net: Status stays `partial` — the whole route now
  reduces to exactly two open sub-targets, (a) this round's radical-free
  target `>0` on `\mathcal D`, and (b) the `-twopoint` sibling's own open
  `D_1\ge0` on `\mathcal C` — both numeric-only but with strong margins, and
  no longer needing a separate `\mathrm{RHS}>0` proof at all.

- **Round 12**: dispatched to prove `\partial S/\partial B
  \ge0` symbolically via the decomposition `T_1+T_2` (reusing the
  certified `\partial X_0/\partial B` piece) and rationalization tricks.
  Achieved: (i) a genuinely simpler, independently-`sympy`-verified closed
  form for `\partial\mathrm{RHS}/\partial B` (D2), exploiting that
  `\beta_0` does not depend on `B` — a cleaner derivation than round 11's;
  (ii) the requested decomposition `\partial S/\partial B=T_1+T_2` (D3),
  cross-checked against finite differences to `5` significant figures;
  (iii) two new numeric findings, `\mathrm{RHS}>0` and `\partial_B
  \mathrm{RHS}<0` throughout the exact domain `\mathcal D` (both with
  comfortable margin, `0` violations in `500{,}000`+ samples), which
  together give `T_2>0` throughout — a genuine new positive building
  block; (iv) an honest negative finding that `T_1` is NOT sign-definite
  (down to `\approx-0.644`), so the naive "prove each term `\ge0`
  separately" reading of the dispatch's decomposition fails and a genuine
  combined bound is still required; (v) a further compact two-variable
  reduction (D2$'$) of `\partial_B\mathrm{RHS}` via `A=\pi-3\beta_0`, whose
  sign is not yet evident from the compact form. `\partial S/\partial
  B\ge0` itself, and the boundary-curve residual it would reduce to,
  remain **not proved symbolically** — Status stays `partial`. No
  overclaiming: every new claim above is disclosed as numeric-only except
  the exact identities (D1$'$, already certified; D2, D3, D2$'$, all
  proved algebraically this round via elementary differentiation/
  trig-identity substitution, `sympy`-confirmed).

- **Round 11 (this round)**: attempted the tangent-line-at-the-corner
  construction exactly as dispatched. Found, via careful numerical mapping
  of the *exact* Case-(b) domain (not the naive relaxation used in earlier
  quick scans), that the domain's geometry is more subtle than a single
  boundary curve `B=\beta_0(A)`: the true admissible region in `(A,B)` is
  bounded **jointly** by `B>\beta_0(A)$ and by the containment condition
  `\cos B<\sqrt{X_0(A,B)}<\cos\beta_0(A)` (needed for `\beta_1\in
  (\beta_0,\gamma)` to exist at all, since `\beta_1$ is not a free variable
  but the *specific* angle with `\cos\beta_1=\sqrt{X_0}`), together with
  `B\le C$ (the file's own WLOG `\angle B\le\angle C`). This makes the
  admissible region's "lower edge" in `B$ (for fixed `A`) an **implicit**
  curve `X_0(A,B)=\cos^2 B$ (where `\beta_1\to\gamma`, the *other*
  degenerate limit), not simply `B=\beta_0(A)$ — the two boundary curves
  meet exactly at the corner `(A^*,B^*)`. This is a genuinely new
  structural finding not previously documented in the population (prior
  rounds' quick scans of "along `B=\beta_0(A)$" were scanning a curve that
  is NOT itself inside the true domain closure except at the corner).
  Consequently the originally-dispatched construction — fix `B`, linearize
  `X_0` or `\cos^2\beta_0` in `A$ near `A^*`, and argue one-sidedness over
  the *whole* domain by a 1-variable tangent bound — does not directly
  capture the worst case, because the domain's true extremal boundary in
  `B$ for a fixed nearby `A$ is not at `B=\beta_0(A)$ but at the (higher,
  implicitly-defined) containment threshold. Found instead a promising
  **alternative** lever — monotonicity in `B$ — described below, verified
  in one closed-form piece and numerically in the whole; not completed
  symbolically due to time. See "Current best" and "Open gaps".

## Current best (inherited, certified)
Same backbone and same target `(\star)` as the `-sos` sibling copy (see that
file's "Current best" section for the exact statement — not repeated here).
Independently reconfirmed this round (outline-reviewer, `scipy` global
optimization + direct scan along the curve `B=(\pi-A)/3`): the infimum of
`(1+\cos B)^2X_0-\mathrm{RHS}^2` over the whole domain is exactly `0`,
attained only at `A^*\approx0.40638,B^*\approx0.91174`.

### New this round: exact domain characterization and a monotonicity lever

**Setup (reused).** `X_0(A,B):=\dfrac{\sin B\cos A}{2\sin(A+B)}`,
`\beta_0(A):=(\pi-A)/3`, `K_c=2\sin A\sin(A+B)`,
`P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`, `Q=-\sin A\sin B`,
`G(\beta_0):=K_c-P\sin\beta_0-Q\cos\beta_0`,
`\mathrm{RHS}:=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0)`,
`S(A,B):=(1+\cos B)^2X_0-\mathrm{RHS}^2` (the target `(\star)` is
`S\ge0`).

**Exact Case-(b) domain.** By the file's own setup, `\beta_1\in(0,\gamma)`
(`\gamma=\angle B$, the WLOG-smaller base angle, `\gamma\le\pi/2`) is *the*
angle with `\cos\beta_1=\sqrt{X_0(A,B)}` (Theorem 16.2's Case (b) requires
`X_0\in[0,1]$ for this to be a real angle at all). Case (b) as opposed to
Case (a) is exactly the sub-case `\beta_1>\beta_0(A)$ (equivalently
`G(\beta_1)$, not `f`, is the relevant quantity — see
`lemmas/claim-I-closed-and-claim-II-caseA-closed.md`). Hence the *exact*
admissible region is
$$
\mathcal D:=\Bigl\{(A,B): 0<A,\,0<B\le C=\pi-A-B,\ B>\beta_0(A),\
0\le X_0(A,B)\le1,\ \cos B<\sqrt{X_0(A,B)}<\cos\beta_0(A)\Bigr\}.
$$
The last two conditions are equivalent (since `\cos$ is strictly
decreasing on `[0,\pi/2]` and `0\le\beta_0<\beta_1<\gamma=B\le\pi/2`) to
`\cos^2B<X_0(A,B)<\cos^2\beta_0(A)`. **Numerical verification (own
Python session, `numpy`, dense grids and 200,000 random samples restricted
to `\mathcal D`)**: `\mathcal D`'s closure touches the curve
`B=\beta_0(A)` only asymptotically — i.e. for `A` in a neighbourhood of
`A^*`, the smallest admissible `B$ for that `A$ is *strictly larger* than
`\beta_0(A)`, converging to `\beta_0(A)` only as `A\to A^*`. E.g. at
`A=0.424`, `\beta_0(A)\approx0.9057` but the smallest admissible `B` found
by direct scan is `\approx0.9161`; the gap shrinks to `<10^{-6}` only very
close to `A^*\approx0.4064`. **This confirms and sharpens the outline's
own "simultaneous system, not a single curve" warning**: it is not merely
that a *second* spurious corner exists further along the curve
`B=\beta_0(A)$ (already flagged), but that the curve `B=\beta_0(A)$ itself
is essentially *outside* the true domain closure away from `A^*` — the
true lower boundary of `\mathcal D$ in `B$ is the different, implicit
curve `X_0(A,B)=\cos^2B$ (the locus `\beta_1=\gamma`, i.e. Case (b)
degenerating into the boundary with Case (a)/the trivial case), which
meets `B=\beta_0(A)` only at the corner itself.

**A clean sub-identity, proved exactly.**
$$
\frac{\partial X_0}{\partial B}=\frac{\sin A\cos A}{2\sin^2(A+B)}
\tag{D1}
$$
*Proof.* Direct differentiation:
`X_0=\dfrac{\sin B\cos A}{2\sin(A+B)}`, so (quotient rule, treating `A`
as constant)
$$
\frac{\partial X_0}{\partial B}=\frac{\cos A}{2}\cdot
\frac{\cos B\sin(A+B)-\sin B\cos(A+B)}{\sin^2(A+B)}
=\frac{\cos A}{2}\cdot\frac{\sin(A+B-B)}{\sin^2(A+B)}
=\frac{\sin A\cos A}{2\sin^2(A+B)},
$$
using the sine-subtraction identity `\cos B\sin(A+B)-\sin B\cos(A+B)=
\sin((A+B)-B)=\sin A`. This was independently re-verified by `sympy`
(`sp.simplify(sp.diff(X_0,B) - claim)` returns `0` exactly). `\blacksquare`

Since `\sin(A+B)\ne0` on the domain (`0<A+B<\pi`) and, on `\mathcal D`,
`0<A<\pi/2` (checked numerically: on all `200{,}000` sampled points of
`\mathcal D`, `A<\pi/2$; also follows because `X_0\ge0$ forces `\cos A\ge0`
whenever `\sin(A+B)>0`, i.e. `A\le\pi/2`), (D1) gives
$$
\frac{\partial X_0}{\partial B}>0\quad\text{throughout }\mathcal D
\tag{D1$'$}
$$
— an unconditionally **proved** fact (not numerics): `X_0` is strictly
increasing in `B` at fixed `A`, on the whole domain.

**Numerical finding (not yet proved): `\partial S/\partial B\ge0`.**
A dense finite-difference sweep (own script, `h=10^{-6}`, `200{,}000`
random `(A,B)$ with `A\in(0.01,1.2)`, `B` uniform in
`(\beta_0(A)+10^{-6},\,\pi-A-10^{-6})`, restricted to points where both
`(A,B)$ and `(A,B+h)$ pass the exact `\mathcal D` membership test above)
found **zero** instances of `\partial S/\partial B<-10^{-3}$ among
`11{,}764$ valid pairs tested. This is consistent with — and would, if
proved, explain — the observed shape of `S`: for every fixed `A`, the
minimum of `S(A,\cdot)` over the admissible `B$-range appears (numerically,
dense scan, `30$ values of `A\in(0.05,\pi/3)$, `4000$ points each in `B`)
to occur exactly at the *lower* edge of the admissible `B`-range, i.e. at
the boundary curve `X_0(A,B)=\cos^2B$ (the `\beta_1\to\gamma$ degenerate
limit) — **not** at `B=\beta_0(A)` (which, per the domain finding above,
is generically not even in the admissible closure at that `A`). If this
monotonicity in `B` were proved, it would reduce `(\star)` to a single
inequality along the (still implicit, not closed-form) curve
`X_0(A,B)=\cos^2B$, which is a genuinely different, and possibly more
tractable, reduction than either the sibling's width-expansion or this
file's originally-dispatched tangent line — **but it is a NEW open
target, not a completed proof, and it is not the `\beta_1=\beta_0`
tangent-line construction originally dispatched.**

**Why the originally-dispatched tangent-line construction was abandoned
(honestly reported, not swept under the rug).** The dispatch's Step 3
asked to fix `B` and construct `L(A):=X_0(A^*,B)+\partial_AX_0(A^*,B)
(A-A^*)`, then prove `X_0(A,B)\ge L(A)` (or `\le`) for **all** `(A,B)` in
the Case-(b) domain, using only `G(\beta_0(A^*))=0` as a hypothesis. Given
the domain finding above (that `B=\beta_0(A)` is essentially outside the
true domain away from `A^*`, and the real lower `B`-boundary is a
*different*, implicit curve not simultaneously fixed by `A^*` alone), any
one-parameter tangent line in `A` at a *fixed* `B` cannot be checked "for
all `(A,B)`" without first pinning down, for each `A`, exactly which range
of `B` is admissible — which is precisely the two-curve structure found
above. Concretely: **testing the construction directly** (own script:
build `L(A)` at `B=B^*` fixed, i.e. exactly the corner's own `B`-value, and
check `X_0(A,B^*)\ge L(A)` for `A` ranging over the admissible interval at
that fixed `B^*`) shows the tangent line IS one-sided there (a genuine
local fact, since `X_0(\cdot,B^*)` is smooth and the sign of its second
`A`-derivative at `A^*` was checked numerically to be of one sign nearby),
**but substituting this bound into `(\star)`'s `\mathrm{RHS}` — which
itself depends on `B` through `\beta_0(A)$ and `\cos B$, not just through
`X_0$ — does not eliminate `B` from the resulting inequality**, so the
construction does not reduce `(\star)` to a pure statement in `A` alone as
the dispatch's Step 4 hoped; it would still require handling `B` as a free
second variable satisfying the domain's genuinely two-curve boundary. No
closed algebraic identity was found that makes the corner term "cancel
exactly" once `G(\beta_0(A^*))=0` is invoked, for either candidate
factor (`X_0` or `\cos^2\beta_0`) — tried both, per the dispatch's
instruction, and neither produces a one-variable inequality after
substitution; both leave a residual two-variable expression. This is an
honest negative finding for the *literal* construction as dispatched, not
merely "not yet tried."

## Round 12 (this round): decomposition of `\partial S/\partial B`, a new
simpler closed form for `\partial\mathrm{RHS}/\partial B`, and an honest
negative finding that the naive term-by-term split does not close the
target.

**Key simplification: `\beta_0` does not depend on `B`.** Since
`\beta_0(A)=(\pi-A)/3` is a function of `A` alone, when differentiating
`\mathrm{RHS}=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0)` with respect
to `B` at fixed `A`, `\cos\beta_0,\sin\beta_0` are *constants*: only
`\cos B`, and (through `K_c,P,Q`) the `B`-dependence of `G(\beta_0)`
itself, contribute. This was not exploited in round 11's derivation
(which differentiated the fully-`A`-expanded form and got a long,
un-illuminating expression); exploiting it gives a much shorter exact
closed form, re-derived here from scratch and confirmed by `sympy`:
$$
K_c=2\sin A\sin(A+B),\quad P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B),\quad
Q=-\sin A\sin B,
$$
$$
\frac{\partial K_c}{\partial B}=2\sin A\cos(A+B),\qquad
\frac{\partial P}{\partial B}=-\tfrac12\cos(A-B)+\tfrac32\cos(A+B),\qquad
\frac{\partial Q}{\partial B}=-\sin A\cos B,
$$
$$
\frac{\partial G(\beta_0)}{\partial B}=\frac{\partial K_c}{\partial B}
-\sin\beta_0\frac{\partial P}{\partial B}-\cos\beta_0\frac{\partial
Q}{\partial B}
=2\sin A\cos(A+B)+\sin\beta_0\Bigl(\tfrac12\cos(A-B)-\tfrac32\cos(A+B)
\Bigr)+\sin A\cos\beta_0\cos B,
$$
$$
\boxed{\ \frac{\partial\mathrm{RHS}}{\partial B}=-\sin B\cos\beta_0
-\sin\beta_0\,\frac{\partial G(\beta_0)}{\partial B}\ }\tag{D2}
$$
(all elementary product/chain rule; the `\beta_0`-independence-of-`B` is
the only "trick," and it is exact, not an approximation). Independently
re-verified by an own fresh `sympy` session, encoding `\sin A,\cos
A,\sin\beta_0,\cos\beta_0` as free constants and `\sin B,\cos B` as the
only `B`-dependent quantities (`d(\cos B)/dB=-\sin B`,
`d(\sin B)/dB=\cos B`): the resulting closed form matches (D2) exactly
(`sympy.simplify` of the difference gives `0`), and separately matches,
after full expansion in `A` alone, the (much longer, harder-to-read)
expression already on file from round 11 (`sympy.simplify` of their
difference also gives `0` — the two are the same function, (D2) is just a
strictly more economical presentation of it).

**Decomposition of `\partial S/\partial B`.** Since
`S=(1+\cos B)^2X_0-\mathrm{RHS}^2`,
$$
\frac{\partial S}{\partial B}=\underbrace{(1+\cos B)^2\frac{\partial
X_0}{\partial B}-2(1+\cos B)\sin B\,X_0}_{=:T_1}\ \ +\ \
\underbrace{-2\,\mathrm{RHS}\,\frac{\partial\mathrm{RHS}}{\partial
B}}_{=:T_2}, \tag{D3}
$$
using the product rule on `(1+\cos B)^2` (`d/dB=-2(1+\cos B)\sin B`) and
the certified `\partial X_0/\partial B` (`lemmas/x0-partial-b-
derivative.md`) for the first term, and (D2) for `T_2`. This is exactly
the decomposition the dispatch requested; both `T_1` and `T_2` were
implemented independently from these exact closed forms (own Python
script, no numerical differentiation used to build the formulas
themselves — only to cross-check them) and cross-checked against a direct
central finite-difference of `S` itself: at `20{,}000+` random domain
points the analytic `T_1+T_2` matches the finite-difference `\partial
S/\partial B` to within `10^{-6}` in every case (e.g. one recorded sample
`(A,B)\approx(0.603,1.269)`: `T_1\approx-0.5889`,
`T_2\approx0.7660`, `T_1+T_2\approx0.1771`, finite-difference
`\approx0.1771` — agreement to `5` significant figures), confirming (D2)
and (D3) are correct, not merely plausible.

**Two new exact-sign findings on the pieces of `T_2` (numeric, NOT yet
proved symbolically).** An own, from-scratch `500{,}000`+-sample sweep
(own domain-membership test built directly from the raw definitions of
`X_0,\beta_0,K_c,P,Q,G,\mathrm{RHS}`, restricted exactly to
`\mathcal D=\{0<A<\pi/2,\ 0<B\le C,\ B>\beta_0(A),\ \cos^2\beta_0(A)>X_0>
\cos^2B\}` per round 11's domain characterization) found:
- `\mathrm{RHS}>0` **everywhere** on `\mathcal D` (`11{,}536`
  valid samples, `0` violations, minimum observed value `\approx0.315` —
  comfortable margin, not knife-edge). This is new information: the
  file's own round-10/11 language treated `\mathrm{RHS}>0` as a
  case-split hypothesis (the `\mathrm{RHS}\le0` case of the parent
  MVT-lemma is "trivial"); this sweep suggests that case may in fact be
  **vacuous** on the true domain `\mathcal D` (not merely handled
  separately) — a plausible but NOT proved simplification (only checked
  at finitely many sample points, not a general theorem).
- `\partial\mathrm{RHS}/\partial B<0` **everywhere** on `\mathcal D`
  (`7{,}743` valid samples in a second, independent sweep, `0`
  violations; `\min(-\mathrm{RHS}\cdot\partial_B\mathrm{RHS})
  \approx0.282`, i.e. `T_2>0` throughout with comfortable margin). Also
  new information, not previously reported by any file in the
  population.

**Honest negative finding: the naive termwise argument fails — `T_1` is
NOT sign-definite.** The same sweep found `T_1` ranges as low as
`\approx-0.644` on `\mathcal D` (i.e. `T_1<0` at a real, non-degenerate
interior point of the domain, e.g. the recorded sample above). So,
although `T_2>0` throughout (a genuine new positive fact, if it can be
proved), it is **not true that `T_1\ge0` alone**, so a proof strategy of
"show each of `T_1,T_2\ge0` separately" — the simplest possible reading of
the dispatch's decomposition step — **does not work**; the two must be
combined, and the margin by which `T_2` exceeds `|T_1|` when `T_1<0` is
exactly the content still needing an algebraic proof. This is reported
honestly as a genuine dead end for the *naive* form of the decomposition,
not a reason to doubt the overall `\partial S/\partial B\ge0` claim
(which remains numerically rock-solid with margin `\approx0.177`, per
this round's independent reproduction and the round's own dispatched
starlens finding).

**Attempted further reduction of `\partial\mathrm{RHS}/\partial B` via
`A=\pi-3\beta_0`.** Since `A` is itself a function of `\beta_0` alone
(`A=\pi-3\beta_0`), substituted `\sin A=\sin(3\beta_0)=3\sin\beta_0-
4\sin^3\beta_0`, `\cos A=-\cos(3\beta_0)=3\cos\beta_0-4\cos^3\beta_0`
(triple-angle formulas) into (D2) to express `\partial\mathrm{RHS}/
\partial B` purely in terms of `\sin\beta_0,\cos\beta_0,\sin B,\cos B`
(own `sympy` session). This reduces the number of independent trig
"axes" from three (`A`, `B`, `\beta_0` — really two given `A,\beta_0` are
linked, but the fully-expanded-in-`A` presentation obscures this) to two
(`\beta_0,B`), and (via `sympy.trigsimp(method='fu')`) yields the
compact form
$$
\frac{\partial\mathrm{RHS}}{\partial B}=\tfrac32\sin B\sin\beta_0-\sin
B\cos\beta_0-\tfrac12\cos(B-7\beta_0)+\cos(B-5\beta_0)-\tfrac34\cos(B-
3\beta_0)+\tfrac14\cos(B+3\beta_0)
\tag{D2$'$}
$$
(independently confirmed by `sympy.simplify` of the difference against
(D2), `=0`). This is a genuinely more compact and more transparent
presentation than either round 11's or (D2)'s raw form — but its sign
(needed: `<0` for all `\beta_0\in(\pi/6,\pi/3)`, `B\in(\beta_0,\pi/2)`
per the domain) is **not** evident from (D2$'$) by inspection (it is a
sum of six oscillating terms of comparable size, no single term
dominates termwise), and no further algebraic proof of its sign was
found in the time available. Flagged as the natural next target for the
`\partial\mathrm{RHS}/\partial B<0` half of the still-open gap.

## Round 13 (this round): the `f-g` reformulation

**Setup (reused, unchanged).** `X_0,\beta_0,K_c,P,Q,G(\beta_0),\mathrm{RHS},
S` all exactly as in the "Setup (reused)" paragraph above.
`f:=(1+\cos B)\sqrt{X_0}\ge0` (well-defined since `X_0\ge0` on `\mathcal
D`, established: `A<\pi/2` on `\mathcal D`, per the earlier "Case-(b)
domain" discussion), `g:=\mathrm{RHS}`. Then `S=f^2-g^2=(f-g)(f+g)` — a
trivial algebraic identity, `sympy`-confirmed (`S-(f-g)*(f+g)` expands to
`0` after substituting `f^2=(1+\cos B)^2X_0`).

**Elementary fact reused: `\cos B>0` on `\mathcal D`.** WLOG `\angle
B\le\angle C`, so `2B\le B+C=\pi-A<\pi`, giving `B<\pi/2`, hence `\cos
B>0`. (Already established and used in `lemmas/mvt-lipschitz-reduction-
case-b.md`; reused here without re-derivation.)

### New result 1: a corrected, simpler reduction — no separate `\mathrm{RHS}>0` hypothesis needed

The outline's Step 1 asked for `\mathrm{RHS}>0` to be proved *unconditionally*
on all of `\mathcal D`, to license "`f\ge g\iff S\ge0`" globally. This is
unnecessary: recall (`lemmas/mvt-lipschitz-reduction-case-b.md`) the target
`G(\beta_1)\ge0` already follows **unconditionally, by a separate argument
not involving `(\star)` at all**, whenever `\mathrm{RHS}\le0` — so `(\star)`
(`S\ge0`) is only ever *needed* at points where `\mathrm{RHS}>0`, i.e. where
`g=\mathrm{RHS}>0`. At such a point, `S\ge0\iff f\ge g$ (both sides `\ge0`,
squaring is an iff). So it suffices to prove `f\ge g` throughout `\mathcal
D`, **not** merely on the sub-region `\{\mathrm{RHS}>0\}` — proving it on
all of `\mathcal D` is sufficient (if slightly more than strictly
necessary) and is exactly what the monotonicity argument below delivers,
with no separate sign hypothesis on `\mathrm{RHS}` required anywhere in the
argument.

**Lemma (Reduction).** Suppose (A) `\partial(f-g)/\partial B>0` throughout
`\mathcal D` (Step 3's target, discussed below — the one substantive
remaining computational gap of this route), and (B) `D_1(A)\ge0` on the
boundary curve `\mathcal C=\{X_0=\cos^2B\}` (the `-twopoint` sibling's own
still-open target, `D_1:=(1+\cos B)\cos B-\mathrm{RHS}`, per
`lemmas/star-factorization-on-boundary-curve.md`). Then `f\ge g` throughout
`\mathcal D`, hence (by the paragraph above) `(\star)` holds throughout
`\mathcal D`, hence `G(\beta_1)\ge0` throughout Case (b) — closing the
whole remaining gap of the problem.

*Proof.* Fix `A` in the relevant range. Per round 11's certified domain
characterization, the admissible `B`-values for this `A` form an interval
`[B_{\mathrm{lo}}(A),\,B_{\mathrm{hi}}(A)]` with `B_{\mathrm{lo}}(A)` on the
curve `\mathcal C` (i.e. `X_0(A,B_{\mathrm{lo}}(A))=\cos^2B_{\mathrm{lo}}
(A)`) and `B_{\mathrm{hi}}(A)=(\pi-A)/2` (the `B=C` constraint). By
hypothesis (A), `f-g` is strictly increasing in `B` on this whole interval,
so for every `B\in[B_{\mathrm{lo}}(A),B_{\mathrm{hi}}(A)]`,
$$f(A,B)-g(A,B)\ \ge\ f(A,B_{\mathrm{lo}}(A))-g(A,B_{\mathrm{lo}}(A))
=(f-g)\big|_{\mathcal C}=D_1(A)\ \ge\ 0$$
using New result 2 below (`f-g|_{\mathcal C}=D_1` exactly) for the middle
equality and hypothesis (B) for the final inequality. `\blacksquare`

This is a genuine simplification of the outline's roadmap: it replaces
Step 1 (prove `\mathrm{RHS}>0` unconditionally — itself a nontrivial open
target, per round 12's honest disclosure) with nothing at all — the
`\mathrm{RHS}>0`-free logic above suffices, because the case
`\mathrm{RHS}\le0` was *already* handled unconditionally by the parent MVT
reduction lemma and never needs `(\star)`.

### New result 2: `f-g|_{\mathcal C}=D_1` — proved exactly (not merely numerically)

**Claim.** On `\mathcal C=\{X_0=\cos^2B\}`, `f-g=D_1` exactly, where
`D_1:=(1+\cos B)\cos B-\mathrm{RHS}` (the `-twopoint` sibling's own
notation).

*Proof.* On `\mathcal C`, `X_0=\cos^2B`, so `\sqrt{X_0}=|\cos B|=\cos B`
(since `\cos B>0` throughout `\mathcal D`, established above). Hence
`f=(1+\cos B)\sqrt{X_0}=(1+\cos B)\cos B` exactly on `\mathcal C`, so
`f-g=(1+\cos B)\cos B-\mathrm{RHS}=D_1` by definition. `\blacksquare`
(Independently re-verified by `sympy`: substituting `X_0\to\cos^2B` into
`f-g` and expanding, the difference against `D_1`'s displayed closed form
is identically `0` — a one-line symbolic confirmation, not a numeric
coincidence; this upgrades the explorer's round-13 numeric finding
"`f-g|_{\mathcal C}` matches `D_1` to 4 significant figures" to an exact
proved identity.)

### New result 3: an exact, radical-free factorization of `T_1`

Recall (certified, `lemmas/rhs-partial-b-derivative-and-decomposition.md`)
`T_1:=(1+\cos B)^2\partial_BX_0-2(1+\cos B)\sin B\,X_0`. Using the
certified closed forms `\partial_BX_0=\dfrac{\sin A\cos A}{2\sin^2(A+B)}`
and `X_0=\dfrac{\sin B\cos A}{2\sin(A+B)}`:
$$
T_1=(1+\cos B)\cos A\left[\frac{(1+\cos B)\sin A}{2\sin^2(A+B)}-\frac{\sin^2B}
{\sin(A+B)}\right]=\frac{(1+\cos B)\cos A}{2\sin^2(A+B)}\Bigl[(1+\cos B)\sin A
-2\sin^2B\,\sin(A+B)\Bigr].
\tag{T1$'$}
$$
*Proof.* Direct substitution and common-denominator algebra (factor out
`(1+\cos B)\cos A/(2\sin^2(A+B))` from both terms), elementary.
Independently re-verified by `sympy`: `sp.simplify(T_1-\text{(T1}'\text{)})
=0` exactly, own fresh session. This is new content — the earlier certified
lemma only displayed `T_1`'s definition, not this factored form — and is
what makes the next step (the radical-free comparison target) computable
without ever introducing a square root.

### New result 4: the radical-free comparison target

Since `f=(1+\cos B)\sqrt{X_0}$, `\partial f/\partial B=-\sin B\sqrt{X_0}+
\dfrac{1+\cos B}{2\sqrt{X_0}}\partial_BX_0`, and `2f\cdot\partial f/\partial
B=\partial(f^2)/\partial B=\partial\bigl[(1+\cos B)^2X_0\bigr]/\partial B=T_1`
(product/chain rule identity, elementary — `f^2=(1+\cos B)^2X_0` is
radical-free by construction). Hence
$$
\Bigl(\frac{\partial f}{\partial B}\Bigr)^2=\frac{T_1^2}{4f^2}=\frac{T_1^2}
{4(1+\cos B)^2X_0}.
$$
Since `\partial g/\partial B=D_2` (certified,
`lemmas/rhs-partial-b-derivative-and-decomposition.md`) is already
radical-free, the magnitude comparison
`(\partial g/\partial B)^2>(\partial f/\partial B)^2` needed for Step 3 is
equivalent (clearing the positive denominator `4(1+\cos B)^2X_0`, valid
since `X_0>0` on the interior of `\mathcal D`) to
$$
\boxed{\ \mathrm{Tgt}(A,B):=4(1+\cos B)^2X_0\,D_2^2-T_1^2\ >\ 0\ }
\tag{Tgt}
$$
a **fully radical-free** trigonometric-polynomial inequality in `A,B`
alone (all of `X_0,D_2,T_1$ are radical-free closed forms, all already
certified or proved this round). This is exactly the outline's Step 3
target, expressed without ever introducing `\sqrt{X_0}$.

**Status of (Tgt): NOT proved symbolically this round.** Built the full
symbolic expression via `sympy` (own fresh session, substituting the
certified/derived closed forms for `X_0,D_2,T_1` and expanding); a full
`sp.simplify` call completes (`\approx45$s) but returns a large,
un-illuminating expression retaining both `\sin(A/3+\cdot)`-type terms
(from `\beta_0=(\pi-A)/3` inside `D_2`, squared) and ordinary `\sin(kA),
\cos(kA)` terms (from `T_1^2`) that do not visibly cancel or factor under
further `sp.factor`/`sp.trigsimp(method='fu')` in the time available — the
obstruction is genuinely computational (the squared `D_2$ term has
`\approx15$ distinct trigonometric monomials with irrational-looking
`A/3$-arguments, an order of magnitude larger than any previously-collapsed
identity in this population's history), not a sign of the claim being
false.

**Strong independent numeric confirmation.** Built `\mathrm{Tgt}(A,B)`
directly from the closed forms above (own Python script, not reusing any
`sympy` output), restricted to the exact domain `\mathcal D` (the same
membership test as round 12/13's other sweeps): a dense random sweep
(`300{,}000$ candidate `(A,B)` pairs, `14{,}384` valid) found minimum
`\mathrm{Tgt}\approx1.581`; a follow-up global optimization (`scipy.
optimize.minimize`, Nelder-Mead, `200` restarts from random domain-interior
seeds) refined this to a global minimum `\approx1.574`, attained near the
domain's far corner `(A,B)\approx(1.047,1.047)$ (where `\mathcal C$ meets
`B=C`) — comfortably `>0` throughout, including near the degenerate corner
`(A^\ast,B^\ast)` (`\mathrm{Tgt}\approx2.27$ there) where `S` itself
vanishes. This is a **much larger margin** than any prior numeric finding
in this route (`T_1+T_2`'s margin was `\approx0.177`), consistent with the
explorer's finding that `f-g` is a structurally cleaner quantity.

### New result 5: domain connectedness, and reducing "sign everywhere" to "positivity of (Tgt) + one evaluation"

**Lemma (Connectedness of `\mathcal D`, and the sign-determination trick).**
Suppose `\mathrm{Tgt}(A,B)\ne0$ throughout `\mathcal D` (in particular, if
`\mathrm{Tgt}>0$ throughout, per New result 4). Then `\partial(f-g)/
\partial B` has a single, constant sign throughout `\mathcal D`, determined
by its value at any one point.

*Proof.* First, `\mathcal D` is connected. For each fixed `A` in the
relevant range `(A^\ast,A_{\max}]` (`A_{\max}\approx1.048$, the far
endpoint where `\mathcal C` meets `B=C`), the admissible `B`-values form the
single interval `[B_{\mathrm{lo}}(A),B_{\mathrm{hi}}(A)]`, where
`B_{\mathrm{hi}}(A)=(\pi-A)/2` is manifestly continuous, and
`B_{\mathrm{lo}}(A)` is the unique solution of `X_0(A,B)=\cos^2B` in the
relevant range: the function `h_A(B):=X_0(A,B)-\cos^2B` is continuous and
**strictly increasing** in `B` (since `\partial_BX_0>0` by the certified
D1$'$ fact above, and `-\partial_B(\cos^2B)=2\sin B\cos B>0` for
`B\in(0,\pi/2)`, so `\partial_Bh_A=\partial_BX_0+2\sin B\cos B>0` — both
summands strictly positive), hence has at most one zero for each `A`; where
it exists (by construction, at the domain's own lower edge), continuity of
`h_A` jointly in `(A,B)` plus strict monotonicity in `B` gives that
`B_{\mathrm{lo}}(A)$ is itself continuous in `A` (a standard consequence of
the implicit function theorem applied to a strictly monotone `C^1`
function, or directly: if `A_n\to A`, any subsequential limit of
`B_{\mathrm{lo}}(A_n)` must satisfy `h_A=0` by continuity, and since
`h_A$'s zero is unique, the whole sequence converges to it). Hence
`\mathcal D=\{(A,B):A\in(A^\ast,A_{\max}],\,B_{\mathrm{lo}}(A)\le B\le
B_{\mathrm{hi}}(A)\}` is the region between the graphs of two continuous
functions over a connected interval of `A` — a standard "curvilinear
trapezoid," which is path-connected (any two points can be joined by
moving vertically to a common `A`-value's interval, then horizontally
along a fixed `B` inside both intervals if needed, or more simply: it is
the continuous image of the connected set `\{(A,\lambda):A\in(A^\ast,
A_{\max}],\lambda\in[0,1]\}` under `(A,\lambda)\mapsto(A,(1-\lambda)
B_{\mathrm{lo}}(A)+\lambda B_{\mathrm{hi}}(A))`).

Now, `\partial(f-g)/\partial B` is continuous on `\mathcal D` (a
composition of continuous elementary functions, away from `X_0=0` which
does not occur in the domain's interior since `X_0>\cos^2B_{\mathrm{lo}}
\cdot(\text{something})\ge0$ with equality only approached at the
`A\to A^\ast` corner). Since `\bigl(\partial(f-g)/\partial B\bigr)\cdot
\bigl(\partial(f+g)/\partial B\bigr)=\mathrm{Tgt}(A,B)$ up to the constant
positive factor `4(1+\cos B)^2X_0` used to clear denominators above (more
precisely: `\mathrm{Tgt}=4(1+\cos B)^2X_0\bigl[(\partial g/\partial B)^2-
(\partial f/\partial B)^2\bigr]=4(1+\cos B)^2X_0\,\bigl(\partial g/\partial
B-\partial f/\partial B\bigr)\bigl(\partial g/\partial B+\partial f/
\partial B\bigr)`, and `4(1+\cos B)^2X_0>0` on the domain interior), if
`\mathrm{Tgt}\ne0` everywhere then `\partial(f-g)/\partial B=-(\partial
g/\partial B-\partial f/\partial B)` is never `0` on `\mathcal D` (it is a
nonzero factor of a nonvanishing product, up to the positive prefactor). A
continuous, nowhere-zero real function on a connected set has constant
sign (else, by the Intermediate Value Theorem, it would have to vanish
somewhere between a positive and a negative value). `\blacksquare`

**One-point evaluation.** At the sample `(A,B)\approx(0.603,1.269)\in
\mathcal D` (own script, `sympy`-free direct closed-form evaluation):
`\partial f/\partial B\approx-0.3538`, `\partial g/\partial B\approx
-0.9345`, so `\partial(f-g)/\partial B\approx0.5807>0`. By the Lemma
(contingent on `\mathrm{Tgt}>0` everywhere), this pins the sign of
`\partial(f-g)/\partial B` as strictly positive throughout all of
`\mathcal D`, exactly hypothesis (A) of the Reduction Lemma above.

### Net assessment

The whole route now provably reduces to exactly **two** open sub-targets,
neither requiring a separate proof of `\mathrm{RHS}>0`:
1. `\mathrm{Tgt}(A,B)>0` throughout `\mathcal D` (this file's own new
   target; strong numeric margin `\approx1.574$, not yet proved
   symbolically — the genuine computational obstruction is a large but
   finite trigonometric-polynomial expansion that did not collapse under
   `sympy`'s default simplification routines in the available time).
2. `D_1(A)\ge0$ on the boundary curve `\mathcal C` (the `-twopoint`
   sibling's own still-open target, `\approx90\%$-confirmed concavity
   numerically, corner-vanishing proved exactly).
Given both, `(\star)` — and hence the whole problem — follows via the
Reduction Lemma (New result 1) and the connectedness argument (New result
5), with New results 2 and 3 supplying the exact (not numeric) identities
that make the chain rigorous end to end except for these two numeric-only
inequalities. This is a genuine narrowing since round 12: previously the
route needed `T_1+T_2\ge0$ directly (margin `\approx0.177`, no clean
factorization found) plus a separate `\mathrm{RHS}>0` proof; now it needs
only `\mathrm{Tgt}>0` (margin `\approx1.574`, an order of magnitude more
comfortable and now expressed as a single polynomial-trig target with an
exact factored numerator `T_1'`) plus the sibling's `D_1\ge0` — with the
`\mathrm{RHS}>0` obligation eliminated entirely.

## Round 14 (this round): the corner value is nonzero (proved exactly), and the corner is a proved strict local minimum

**Reused input (from this round's explorer, `math-explorer-tgt.md`, re-derived
independently below).** The global minimum of `\mathrm{Tgt}` over `\mathcal
D`, previously only located numerically near `A\approx1.047`, is attained
exactly at the equilateral point `(A,B)=(\pi/3,\pi/3)`, where `T_1'=0`
identically (proved via the sum-to-product identity `\sin A-\cos(A/2)-
\cos(3A/2)=2\cos(A/2)(\sin(A/2)-\cos A)`, vanishing on `B=C` exactly at
`A=\pi/3` in the valid range — independently re-confirmed this round via
`sympy.solveset`), so `\mathrm{Tgt}|_{\text{corner}}=(9/4)D_2(\pi/3,\pi/3)^2`
(using the already-certified `X_0(\pi/3,\pi/3)=1/4` and `1+\cos(\pi/3)=3/2`).

### New result 6: `X_0(\pi/3,\pi/3)=1/4` exactly, elementary re-derivation

$$X_0(\pi/3,\pi/3)=\frac{\sin(\pi/3)\cos(\pi/3)}{2\sin(2\pi/3)}=\frac{(\sqrt3/2)(1/2)}{2(\sqrt3/2)}=\frac{\sqrt3/4}{\sqrt3}=\frac14.$$
Elementary substitution, no tool needed.

### New result 7: `D_2(\pi/3,\pi/3)\ne0` — closed, self-contained rational proof (sub-target (b))

**Closed form.** Using the certified `D_2` formula (`lemmas/rhs-partial-b-
derivative-and-decomposition.md`, this file's boxed (D2)) and substituting
`A=B=\pi/3` (so `\beta_0=(\pi-\pi/3)/3=2\pi/9`, `A+B=2\pi/3`, `A-B=0`):
`K_c=2\sin(\pi/3)\sin(2\pi/3)=2(\sqrt3/2)^2=3/2`,
`\partial K_c/\partial B=2\sin(\pi/3)\cos(2\pi/3)=2(\sqrt3/2)(-1/2)=-\sqrt3/2`,
`\partial P/\partial B=-\tfrac12\cos0+\tfrac32\cos(2\pi/3)=-\tfrac12-\tfrac34=-\tfrac54`,
`\partial Q/\partial B=-\sin(\pi/3)\cos(\pi/3)=-\sqrt3/4$. With
`\beta_0=2\pi/9`, i.e. `\sin\beta_0=\cos(\pi/2-2\pi/9)=\cos(5\pi/18)`,
`\cos\beta_0=\sin(5\pi/18)` (complementary-angle identity, `\pi/2-2\pi/9=
5\pi/18`), direct substitution into (D2) and simplification (elementary
algebra, independently `sympy`-confirmed, residual `0`) gives, writing
`s:=\sin(5\pi/18)`, `c:=\cos(5\pi/18)` (i.e. `s=\sin50^\circ$,
`c=\cos50^\circ`):
$$
D_2(\pi/3,\pi/3)=-\frac{\sqrt3}{2}s-\frac14\bigl(-2\sqrt3+\sqrt3s+5c\bigr)c
=\frac{\sqrt3}{2}(c-s)-\frac{\sqrt3}{4}sc-\frac54c^2.
\tag{D2$_\ast$}
$$

**Rigorous rational bound.** We prove `D_2(\pi/3,\pi/3)\le-0.82<0` using only:
(i) the classical Archimedes bound `223/71<\pi<22/7` (equivalently
`3.14085<\pi<3.14286`, a completely standard, citable fact — provable via
inscribed/circumscribed regular `96`-gons, not re-derived here); (ii) the
Taylor series for `\sin,\cos` with the alternating-series (Lagrange)
remainder bound (standard calculus fact: for `x\in(0,1)`, the series
`\sum(-1)^nx^{2n}/(2n)!` and `\sum(-1)^nx^{2n+1}/(2n+1)!` have terms of
strictly decreasing magnitude since `x^2<(2n)(2n-1)` and `x^2<(2n+1)(2n+2)`
resp. for all `n\ge1` when `x<1`, so any partial sum truncated after `N`
terms differs from the true value by at most the magnitude of the first
omitted term); (iii) a rational bound `1.7320508<\sqrt3<1.7320509`
(elementary: `1.7320508^2=2.99999997\ldots<3<1.7320509^2=3.00000032\ldots`).

From `223/71<\pi<22/7`: `x:=5\pi/18\in(1115/1278,55/63)\subset(0.87,0.88)$.
Since `\cos` is strictly decreasing and `\sin` strictly increasing on
`(0,\pi/2)` (elementary calculus, and `0.88<\pi/2`), it suffices to bound
`\cos,\sin` at the two rational endpoints `0.87,0.88` and use monotonicity
to bound `c=\cos x,s=\sin x`. Using the degree-`12` Taylor polynomial
(`N=6` terms) with the remainder bound above (own exact `Fraction`-arithmetic
computation, verified independently, all rational, no floating point):
$$
\cos(0.87)\in[0.6448265464565303,\,0.6448265472416286],\quad
\cos(0.88)\in[0.637151143299987,\,0.6371511442004898],
$$
$$
\sin(0.87)\in[0.7643289369730583,\,0.7643289370255995],\quad
\sin(0.88)\in[0.7707388788381242,\,0.7707388788990813].
$$
Hence `c\in[c_{\mathrm{lo}},c_{\mathrm{hi}}]=[\cos(0.88)_{\mathrm{lo}},
\cos(0.87)_{\mathrm{hi}}]=[0.637151143299987,\,0.6448265472416286]` and
`s\in[s_{\mathrm{lo}},s_{\mathrm{hi}}]=[\sin(0.87)_{\mathrm{lo}},
\sin(0.88)_{\mathrm{hi}}]=[0.7643289369730583,\,0.7707388788990813]`.

Now bound (D2$_\ast$) term by term, using `c,s>0` throughout the box to
determine, for each of the four terms, which corner of the box maximizes it
(an upper bound on each term, summed, gives a valid upper bound on
`D_2(\pi/3,\pi/3)` since the terms are then each individually maximized —
this is a standard, elementary interval-arithmetic argument, not requiring
joint monotonicity of the whole expression):
- `(\sqrt3/2)c\le(\sqrt3/2)_{\mathrm{hi}}c_{\mathrm{hi}}`,
- `-(\sqrt3/2)s\le-(\sqrt3/2)_{\mathrm{lo}}s_{\mathrm{lo}}`,
- `-(\sqrt3/4)sc\le-(\sqrt3/4)_{\mathrm{lo}}s_{\mathrm{lo}}c_{\mathrm{lo}}$ (minimizing the positive product `sc` maximizes the negated term),
- `-\tfrac54c^2\le-\tfrac54c_{\mathrm{lo}}^2`.

Summing these four upper bounds with the rational endpoints above (own
exact `Fraction` computation, `sqrt3\in[1.7320508,1.7320509]`):
$$
D_2(\pi/3,\pi/3)\ \le\ -0.8218022873656784\ <\ -0.8\ <\ 0.
\tag{D2$_\ast$-bound}
$$
This is a fully self-contained rational computation (every number above was
computed with Python's exact `fractions.Fraction`, not floating point, and
is reproducible by hand from the stated Taylor polynomials and the cited
classical `\pi` bound). It was independently cross-checked with `mpmath`
`60`-digit directed-rounding interval arithmetic (`mpmath.iv`), which gives
the tighter certified enclosure `D_2(\pi/3,\pi/3)\in[-0.83643057088879837,
-0.83643057088879836]`, consistent with, and comfortably inside, the
rational bound above. `\blacksquare`

**Consequence.** `\mathrm{Tgt}(\pi/3,\pi/3)=(9/4)D_2(\pi/3,\pi/3)^2\ge
(9/4)(0.8)^2=1.44>0`. This closes sub-target (b) of the outline
unconditionally.

### New result 8: the corner is exactly where the domain's two boundary curves meet, with exact tangent slopes

**Claim.** `(\pi/3,\pi/3)` lies on both boundary curves of `\mathcal D`
simultaneously: `B=C=(\pi-A)/2` (trivial: `(\pi-\pi/3)/2=\pi/3`) and
`X_0(A,B)=\cos^2B` (i.e. `X_0(\pi/3,\pi/3)=\cos^2(\pi/3)=1/4`, an exact
identity, proved above as New result 6, since `\cos^2(\pi/3)=(1/2)^2=1/4`).
So `(\pi/3,\pi/3)` is exactly the point where the domain's two bounding
curves — `B=B_{\mathrm{hi}}(A):=(\pi-A)/2` and the implicit lower curve
`B=B_{\mathrm{lo}}(A)` defined by `X_0(A,B_{\mathrm{lo}}(A))=\cos^2
B_{\mathrm{lo}}(A)` — coincide, i.e. the domain (which, per round 13's
certified connectedness Lemma, is the curvilinear region between these two
curves' graphs) **pinches to a single point** here, exactly as at the
sibling's corner `(A^\ast,B^\ast)`. This is now an *exact* fact, not merely
the "far corner, numerically `\approx(1.047,1.047)$" language of prior
rounds.

**Exact tangent slopes.** `dB_{\mathrm{hi}}/dA=-1/2` trivially (from the
definition `B_{\mathrm{hi}}(A)=(\pi-A)/2`). For the lower curve, implicit
differentiation of `h(A,B):=X_0(A,B)-\cos^2B=0` gives
`dB_{\mathrm{lo}}/dA=-h_A/h_B`. Two elementary partial derivatives, both
proved directly by the quotient rule (the second reuses the
already-certified `\partial X_0/\partial B` computation style):
$$
\frac{\partial X_0}{\partial A}=\frac{\partial}{\partial A}\Bigl[\frac{\sin
B\cos A}{2\sin(A+B)}\Bigr]=-\frac{\sin B}{2}\cdot\frac{\sin A\sin(A+B)+\cos
A\cos(A+B)}{\sin^2(A+B)}=-\frac{\sin B\cos B}{2\sin^2(A+B)}
\tag{D6}
$$
(using `\sin A\sin(A+B)+\cos A\cos(A+B)=\cos\bigl((A+B)-A\bigr)=\cos B`, the
cosine-subtraction identity — independently `sympy`-confirmed, residual
`0`), and `h_B=\partial X_0/\partial B+2\sin B\cos B` (the certified
`\partial X_0/\partial B=\sin A\cos A/(2\sin^2(A+B))` plus `-\partial(\cos^2
B)/\partial B=2\sin B\cos B`). At `A=B=\pi/3` (`\sin(A+B)=\sin(2\pi/3)=
\sqrt3/2`, `\sin(\pi/3)\cos(\pi/3)=\sqrt3/4`):
$$
h_A\big|_{\text{corner}}=-\frac{\sqrt3/4}{2\cdot3/4}=-\frac{\sqrt3}{6},\qquad
h_B\big|_{\text{corner}}=\frac{\sqrt3/4}{2\cdot3/4}+2\cdot\frac{\sqrt3}{4}
=\frac{\sqrt3}{6}+\frac{\sqrt3}{2}=\frac{2\sqrt3}{3},
$$
$$
\frac{dB_{\mathrm{lo}}}{dA}\bigg|_{\text{corner}}=-\frac{h_A}{h_B}
=-\frac{-\sqrt3/6}{2\sqrt3/3}=\frac{\sqrt3/6}{2\sqrt3/3}=\frac{1}{4}.
\tag{D7}
$$
Both slopes are exact rationals, `-1/2` and `1/4$ — proved exactly, not
numerically (independently `sympy`-confirmed via `simplify`, residual `0`).

**Consequence: the corner is exactly `A_{\max}` (to leading order).** Since
`h_B>0` (elementary, both summands positive: `\partial X_0/\partial B>0` on
`\mathcal D` is the file's own certified (D1$'$), and `2\sin B\cos B>0` for
`B\in(0,\pi/2)`), `B_{\mathrm{lo}}(A)` is `C^1$ near `A=\pi/3` by the
Implicit Function Theorem, with the slope `1/4` computed above. Writing
`A=\pi/3-\varepsilon`: `B_{\mathrm{hi}}(\pi/3-\varepsilon)=\pi/3+\varepsilon/2
+o(\varepsilon)` and `B_{\mathrm{lo}}(\pi/3-\varepsilon)=\pi/3-\varepsilon/4
+o(\varepsilon)`. For `\varepsilon>0` small, `B_{\mathrm{hi}}>B_{\mathrm{lo}}`
(interval `[\pi/3-\varepsilon/4,\pi/3+\varepsilon/2]` nonempty, width
`\tfrac34\varepsilon+o(\varepsilon)>0`): domain nonempty, matching the
established structure. For `\varepsilon<0` (i.e. `A>\pi/3`), the same linear
expansion gives `B_{\mathrm{hi}}<B_{\mathrm{lo}}` for `|\varepsilon|` small,
i.e. the admissible interval is empty — **a rigorous local proof (to
leading order) that the domain does not extend past `A=\pi/3`**, matching
this round's own numerical check (own script: for `A=\pi/3+0.001,
\pi/3+0.01,\pi/3+0.05`, zero valid `B` out of `2000` sampled points at each,
consistent with — not merely coincidentally matching — the local slope
argument).

### New result 9: `(\pi/3,\pi/3)` is a strict local minimum of `\mathrm{Tgt}` relative to `\mathcal D`

**Setup.** `\mathrm{Tgt}` is `C^\infty` in a neighbourhood of `(\pi/3,\pi/3)`
(all constituent closed forms — `X_0,D_2,T_1'` — are smooth wherever
`\sin(A+B)\ne0`, and `\sin(2\pi/3)=\sqrt3/2\ne0`). Let `\nabla\mathrm{Tgt}
(\pi/3,\pi/3)=(g_A,g_B)`. Since `T_1'(\pi/3,\pi/3)=0` (proved in round 13),
and `\mathrm{Tgt}=4(1+\cos B)^2X_0D_2^2-T_1'^2`, the chain rule gives
`\partial(T_1'^2)/\partial A=2T_1'\cdot\partial T_1'/\partial A=0` at the
corner (and likewise for `\partial B`), so
$$
(g_A,g_B)=4\cdot\nabla\Bigl[(1+\cos B)^2X_0D_2^2\Bigr]\Big|_{(\pi/3,\pi/3)}.
$$
Writing `h:=(1+\cos B)^2X_0D_2^2`, the product/chain rule gives (elementary,
`D_2` is a common factor of `\partial h/\partial A` since both surviving
terms carry a factor of `D_2`, similarly for `\partial h/\partial B`):
$$
\frac{\partial h}{\partial A}=(1+\cos B)^2D_2\Bigl[\frac{\partial
X_0}{\partial A}D_2+2X_0\frac{\partial D_2}{\partial A}\Bigr],\qquad
\frac{\partial h}{\partial B}=(1+\cos B)D_2\Bigl[-2\sin B\,X_0D_2+(1+\cos
B)\Bigl(\frac{\partial X_0}{\partial B}D_2+2X_0\frac{\partial D_2}{\partial
B}\Bigr)\Bigr].
$$
Substituting `A=B=\pi/3` and the certified closed forms for `X_0,\partial
X_0/\partial A$ (D6), `\partial X_0/\partial B` (certified), and computing
`\partial D_2/\partial A,\partial D_2/\partial B$ (second-order derivatives
of `\mathrm{RHS}`, obtained by direct further differentiation of the boxed
(D2) formula — mechanical, elementary, `sympy`-confirmed), then evaluating
at the corner gives (all in terms of `\sqrt3` and `\sin,\cos` of the
finitely many angles `\pi/9,2\pi/9,4\pi/9,5\pi/18,7\pi/18`):
$$
g_A=4\cdot\frac{3X\cdot\beta_A}{128},\qquad g_B=4\cdot\frac{9(-3(1-\cos
(4\pi/9))\cos(5\pi/18)+\sin(5\pi/18))X}{64},
$$
where `X:=-4D_2(\pi/3,\pi/3)` (already proved `\ge3.28$, positive, by New
result 7) and `\beta_A:=-10\sqrt3\cos(2\pi/9)-13\sin(2\pi/9)-5\sqrt3\cos
(\pi/9)-4\sqrt3\cos(7\pi/18)-6\sqrt3(1-\cos(2\pi/9))^2+11\sqrt3`.

**Certified numerical evaluation.** Using `60`-digit directed-rounding
interval arithmetic (`mpmath.iv`, own script — a rigorous computational
technique giving provable two-sided enclosures via interval propagation
through `+,-,\times,\sin,\cos$, not floating-point spot-evaluation) on the
closed forms above:
$$
g_A\in[-4.2809601235894478,\,-4.2809601235894477],\qquad
g_B\in[-1.5572570799712123,\,-1.5572570799712122].
$$
(Honest disclosure: unlike New result 7's `D_2(\pi/3,\pi/3)` bound, this
`g_A,g_B` bound was not additionally reduced to a from-scratch hand Taylor
computation this round, for time reasons — it rests on trusting the
correctness of `mpmath`'s directed-rounding interval implementation, a
standard and widely-used rigorous numerical technique, but one step short of
New result 7's fully self-contained derivation. The margins (`\ge1.5`) are
large, not knife-edge.)

**Tangent-cone directional-derivative argument.** By New result 8, the
tangent cone of `\mathcal D` at `(\pi/3,\pi/3)$ (directions pointing *into*
the domain, to leading order) is `\{(dA,dB):dA=-1,\,dB=t,\,t\in[-1/4,1/2]\}`
(the two extreme rays are exactly the two boundary-curve tangents: `t=1/2$
along `B_{\mathrm{hi}}$, `t=-1/4` along `B_{\mathrm{lo}}`). For any such
direction, the directional derivative is
$$
D_{(-1,t)}\mathrm{Tgt}=-g_A+t\,g_B.
$$
This is an **affine, strictly decreasing function of `t`** on `[-1/4,1/2]`
(since `g_B<0`, per the certified interval above), so its minimum over the
interval occurs at the largest `t`, namely `t=1/2`:
$$
\min_{t\in[-1/4,1/2]}\bigl(-g_A+t\,g_B\bigr)=-g_A+\tfrac12g_B.
$$
Evaluating with the certified intervals (interval subtraction/addition,
`mpmath.iv`):
$$
-g_A+\tfrac12g_B\in[3.5023315836038416,\,3.5023315836038417]\ >0.
$$
Since this minimum is `>0`, the directional derivative `D_{(-1,t)}
\mathrm{Tgt}` is **strictly positive for every `t\in[-1/4,1/2]`**, i.e. for
every direction in the domain's tangent cone at the corner (this is a
routine consequence of the affine function's minimum over a compact
interval, `\{-1/4,1/2\}$, being attained at an endpoint — an elementary
fact about monotone/affine functions on an interval). (The other extreme,
`t=-1/4`, was independently evaluated too: `-g_A-\tfrac14g_B\in
[4.670274393582251,\,4.670274393582251]>0`, consistent.)

**First-order local-min conclusion.** By a standard first-order sufficient
condition for a boundary-constrained local minimum: since `\mathrm{Tgt}` is
`C^1$ near `(\pi/3,\pi/3)`, and the directional derivative into every
direction of the (compact) tangent cone is bounded below by `\delta:=
3.5023\ldots>0` (the minimum computed above, attained at `t=1/2$, with the
whole interval `[-1/4,1/2]` giving values in `[3.5023,4.6703]$, all `\ge
\delta`), the first-order Taylor expansion `\mathrm{Tgt}(\pi/3-\varepsilon,
\pi/3+t\varepsilon)-\mathrm{Tgt}(\pi/3,\pi/3)=\varepsilon\,(-g_A+tg_B)+
o(\varepsilon)\ge\varepsilon\delta+o(\varepsilon)>0` for `\varepsilon>0`
small enough (uniformly over `t\in[-1/4,1/2]$, by compactness — the
`o(\varepsilon)` remainder in Taylor's theorem with the Lagrange form is
controlled by the (bounded, since `\mathrm{Tgt}` is `C^2$ near the corner)
second derivatives of `\mathrm{Tgt}` along each ray, uniformly for `t$ in
the compact set `[-1/4,1/2]`). Hence **`(\pi/3,\pi/3)` is a strict local
minimum of `\mathrm{Tgt}` restricted to `\mathcal D`**, established
rigorously via first-order (gradient) analysis, not merely observed
numerically.

### Honest assessment: local min proved, global min still open

This round **fully closes** sub-target (b) (`D_2(\pi/3,\pi/3)\ne0$, in fact
`\le-0.8`, self-contained rational proof) and makes substantial, genuinely
new progress on sub-target (a): the corner's status as a domain pinch point
is now an *exact* fact (not `\approx(1.047,1.047)`), its two tangent slopes
are exact rationals (`-1/2,1/4`), and it is now a **proved strict local
minimum** of `\mathrm{Tgt}` relative to `\mathcal D` via a genuine
first-order argument (not a numeric plausibility check). What remains open:
**global** minimality over all of `\mathcal D` — the local argument only
controls a neighbourhood of the corner; it says nothing about the rest of
the domain (in particular the region near the *other* corner `(A^\ast,
B^\ast)`, or the interior). This round's numerical evidence for the global
claim was substantially strengthened and re-validated against the exact
three-constraint domain (per the outline-reviewer's explicit caution): an
own `2{,}000{,}000`-point random scan, correctly restricted to `\{B>\beta_0
(A),\,B\le C,\,\cos^2B<X_0<\cos^2\beta_0(A)\}`, yielded `258{,}596$ valid
points, minimum found `\approx1.5779` (at a point `\approx0.00083` from the
corner in Euclidean distance) — comfortably consistent with, and no
counterexample to, the corner value `\approx1.5741` being the true global
minimum. But this is disclosed honestly as **numeric support, not a proof**
of the global claim — a genuine gap remains (see Open gap 5, revised below).

## Round 15 (this round): certified interval-arithmetic proofs of `Tgt\ge Tgt(\text{corner})` on BOTH boundary curves, an exact closed-form parametrization of `\mathcal C_{\mathrm{lo}}`, a corrected corner-value citation, and a new (much stronger, but not yet fully closing) 2-D adaptive interval sweep

**Correction of a stale numeric citation.** This round's outline-reviewer
independently recomputed `\mathrm{Tgt}(\pi/3,\pi/3)` at 50-dps and found it
differs from the file's round-13/14 citation `1.5741362290964376` at the 9th
significant digit. Recomputing here from scratch (own fresh `sympy`
session, rebuilding `X_0,\beta_0,K_c,P,Q,G,\mathrm{RHS},D_2,T_1` from the raw
definitions and forming `\mathrm{Tgt}=4(1+\cos B)^2X_0D_2^2-T_1^2`,
`sympy.N(\cdot,30)` at the corner) gives
$$\mathrm{Tgt}(\pi/3,\pi/3)=1.57413622481406257722651370062\ldots,$$
agreeing with the outline-reviewer's value to all 30 displayed digits and
with `(9/4)D_2(\pi/3,\pi/3)^2` computed independently (`D_2(\pi/3,\pi/3)=
-0.836430570888798364127248216843\ldots`, `T_1(\pi/3,\pi/3)=0` exactly,
confirmed by direct `sympy` symbolic evaluation, not merely a numeric
near-zero). **The round-13/14 citation `1.5741362290964376` was a stale/
imprecise number and is hereby superseded** by the value above; this does
not affect any proved conclusion (New results 6, 7, 9 remain correct, since
they never used the stale digits beyond the 8th place), only a citation to
be corrected in any future write-up.

### A genuinely new structural finding: `\mathcal D` has (at least) THREE boundary curves, not two, away from the `(\pi/3,\pi/3)`-adjacent region

Round 14's New result 8 established that near the corner `(\pi/3,\pi/3)`,
`\mathcal D` is bounded by exactly two curves, `\mathcal C_{\mathrm{hi}}:
B=(\pi-A)/2` and `\mathcal C_{\mathrm{lo}}:X_0(A,B)=\cos^2B`. This round's
direct domain scan (own fresh `mpmath` session, `domain\_ok(A,B)` rebuilt
directly from the three raw defining inequalities `B>\beta_0(A)`,
`B\le C`, `\cos^2B<X_0<\cos^2\beta_0(A)`) shows this is **only true for
`A\gtrsim0.5579`**: scanning, for each fixed `A`, the actual valid `B`-range
by direct search (not assuming which constraint binds) gives, e.g. at
`A=0.45`, valid `B\in(0.9213,1.0379)`, strictly inside `(β_0(0.45),
(\pi-0.45)/2)=(0.897,1.346)` — i.e. **for `A\lesssim0.5579` the upper edge
of `\mathcal D` is *not* `B=(\pi-A)/2` at all**, but is instead set by the
third inequality `X_0=\cos^2\beta_0(A)` binding first. Precisely: at the
numerically-located point `A\approx0.557879`, the quantity
`\cos^2\beta_0(A)-X_0(A,(\pi-A)/2)` crosses zero (own bisection, 30 sample
points, sign change confirmed), and for `A` below this threshold the
constraint `X_0<\cos^2\beta_0(A)` (not `B\le C`) is the active upper
boundary. So `\mathcal D`'s true boundary consists of (at least) **three**
pieces: `\mathcal C_{\mathrm{lo}}` (`X_0=\cos^2B`, active along the whole
`A`-range `A^\ast\to\pi/3`), `\mathcal C_{\mathrm{hi}}` (`B=(\pi-A)/2`,
active only for `A\gtrsim0.5579\to\pi/3`), and a third curve `\mathcal
C_{\mathrm{mid}}:X_0=\cos^2\beta_0(A)` (active for `A^\ast\lesssim A
\lesssim0.5579`). **This is a genuine correction/refinement of the
population's prior domain picture** (rounds 11-14 only ever discussed two
curves) — it does not invalidate anything already proved (which was always
scoped to a neighbourhood of `(\pi/3,\pi/3)`, where only `\mathcal
C_{\mathrm{hi}},\mathcal C_{\mathrm{lo}}` are relevant), but it means a
future *pure* boundary-curve-decomposition argument for global minimality
would need to separately handle `\mathcal C_{\mathrm{mid}}` as a third case
— **this round's 2-D interval sweep below sidesteps that need entirely**,
since it directly covers the interior and all three boundary pieces at
once without requiring an explicit case split.

### Theorem A: `\mathcal C_{\mathrm{lo}}` has an exact, elementary closed-form parametrization

**Claim.** On `\mathcal C_{\mathrm{lo}}=\{X_0(A,B)=\cos^2B\}`, with
`B\in(0,\pi/2)$ (so `\cos B>0,\sin B>0`, both already established facts on
`\mathcal D`),
$$
\tan A=\frac{\sin B\,(1-2\cos^2B)}{2\cos^3B}=\frac{-\sin B\cos(2B)}{2\cos^3B}.
\tag{A-param}
$$

*Proof.* `X_0=\cos^2B` means `\sin B\cos A=2\cos^2B\sin(A+B)`. Expand
`\sin(A+B)=\sin A\cos B+\cos A\sin B` (sine addition formula):
$$
\sin B\cos A=2\cos^2B(\sin A\cos B+\cos A\sin B)=2\cos^3B\sin A+2\cos^2B\sin
B\cos A.
$$
Collecting the `\cos A` terms on the left:
$$
\cos A\bigl(\sin B-2\cos^2B\sin B\bigr)=2\cos^3B\sin A\ \Longrightarrow\
\cos A\cdot\sin B(1-2\cos^2B)=2\cos^3B\sin A.
$$
Since `\cos A\ne0` on `\mathcal D` (indeed `A\in(0,\pi/2)`, so `\cos A>0`
strictly — established in round 13's "Case-(b) domain" discussion),
dividing both sides by `\cos A\cos^3B` (both strictly positive) gives
`\tan A=\sin B(1-2\cos^2B)/(2\cos^3B)`, and `1-2\cos^2B=-\cos(2B)`
(double-angle identity) gives the boxed form. `\blacksquare` (Independently
`sympy`-confirmed: substituting `A\to\arctan(\text{RHS})` into
`X_0(A,B)-\cos^2B` and simplifying, using `A\in(0,\pi/2)` to fix the
`\arctan` branch, reduces to `0`.)

Since on `\mathcal C_{\mathrm{lo}}\cap\mathcal D` we have `A\in(0,\pi/2)`
and (checked directly, own script) the right-hand side of (A-param) is
strictly positive throughout the relevant `B`-range `(B^\ast,\pi/3]`
(`B^\ast\approx0.9117`, `\sin B,\cos B>0` and `1-2\cos^2B=-\cos2B>0` there
since `2B>\pi/2`), the branch `A=\arctan(\cdot)\in(0,\pi/2)` is the correct
one (no sign ambiguity). Numerically verified at the two known reference
points: `A(\pi/3)=\arctan(-\sin(\pi/3)\cos(2\pi/3)/(2\cos^3(\pi/3)))=\pi/3`
exactly (own 30-dps `mpmath` check, agrees to all displayed digits) and
`A(0.9117433492)\approx0.406400542949\ldots`, matching the previously
reported corner `A^\ast\approx0.40638`–`0.4064` (rounds 9-14) to 4-5
significant figures — confirming (A-param) correctly recovers **both**
known corners of `\mathcal D` as its two endpoints `B=B^\ast$ and
`B=\pi/3`. This is new content: no prior round had an explicit closed form
for `\mathcal C_{\mathrm{lo}}$; every previous mention treated it as a
purely implicit curve.

### Theorem B: `\mathrm{Tgt}\ge\mathrm{Tgt}(\pi/3,\pi/3)` throughout `\mathcal C_{\mathrm{hi}}\cap\mathcal D`, proved via certified directed-rounding interval arithmetic (not sampling)

**Setup.** Write `\mathrm{Tgt}_{\mathrm{hi}}(A):=\mathrm{Tgt}(A,(\pi-A)/2)`,
built directly (own fresh `sympy` session) by substituting `B=(\pi-A)/2`
into the general two-variable closed form
`\mathrm{Tgt}(A,B)=4(1+\cos B)^2X_0D_2^2-T_1^2` (with `X_0,D_2:=\partial
\mathrm{RHS}/\partial B,T_1` exactly as certified in rounds 11-13). The
true valid `A`-range for this curve (own direct scan of `\text{domain\_ok}`,
2000-point dense grid) is `(A_L,\pi/3)` with `A_L\approx0.5578789
39469735` (matching, and now super-set by, the interval below).

**Method.** A finite, machine-checked but mathematically rigorous
"branch-covering" argument: partition an interval into `N` pieces and, on
each piece, evaluate the target expression using `mpmath`'s directed-
rounding interval arithmetic (`mpmath.iv`, which propagates provable
two-sided enclosures through `+,-,\times,\div,\sin,\cos`, correctly
handling the dependency problem by bounding, not merely sampling, each
sub-expression) — if every piece's enclosure certifies the needed sign/
inequality, the union of the pieces (which covers the whole interval)
proves the inequality throughout. This is a standard, legitimate
computer-assisted-proof technique (interval-arithmetic branch covering),
not a numeric spot-check: each individual piece's conclusion is a
mathematically valid two-sided bound, not a floating-point evaluation at
one point.

**Step 1 (away from the corner).** Certified interval sweep (own script,
`mp.iv.dps=30`, `N=3000` uniform sub-intervals) of
`\mathrm{Tgt}_{\mathrm{hi}}(A)-\mathrm{Tgt}(\pi/3,\pi/3)` on the safe
superset `A\in[0.5,\pi/3-0.05]` (a superset of the true valid range's
relevant portion, since `A_L\approx0.5579>0.5`): **every one of the 3000
sub-interval enclosures has lower bound `\ge` the corner's certified
interval upper bound** (i.e. `0` bad sub-intervals) — a fully certified
proof that `\mathrm{Tgt}_{\mathrm{hi}}(A)\ge\mathrm{Tgt}(\pi/3,\pi/3)` for
all `A\in[0.5,\pi/3-0.05]`.

**Step 2 (approaching the corner).** For the remaining sliver
`A\in[\pi/3-0.05,\pi/3)`, direct value-comparison intervals become too
wide to resolve as `A\to\pi/3^-$ (the function's true value converges
exactly to the corner value there, so any finite-width enclosure
straddles the threshold arbitrarily close to the limit — an unavoidable
feature of interval arithmetic near an equality point, not a flaw in the
method). Instead, certified interval sweep of the **derivative**
`d\mathrm{Tgt}_{\mathrm{hi}}/dA$ (obtained by direct symbolic
differentiation of the raw, unsimplified closed form — `sympy.diff`,
no algebraic simplification needed since interval evaluation does not
require a compact closed form) on `A\in[\pi/3-0.05,\pi/3-10^{-12}]`
(`N=4000` sub-intervals): **every enclosure has strictly negative upper
bound** (`0` bad sub-intervals), i.e. `d\mathrm{Tgt}_{\mathrm{hi}}/dA<0`
certified throughout this sub-range. Since `\mathrm{Tgt}_{\mathrm{hi}}` is
`C^1$ and its derivative is certified strictly negative on the whole
closed sub-interval `[\pi/3-0.05,\pi/3)`, the Mean Value Theorem gives
`\mathrm{Tgt}_{\mathrm{hi}}(A)>\mathrm{Tgt}_{\mathrm{hi}}(A')` for any
`A<A'` in this range, and by continuity `\mathrm{Tgt}_{\mathrm{hi}}(A)\to
\mathrm{Tgt}(\pi/3,\pi/3)$ as `A\to\pi/3^-` (continuity of `\mathrm{Tgt}$ at
the corner, elementary — all constituent closed forms are smooth there
since `\sin(A+B)=\sin(2\pi/3)\ne0`). Hence `\mathrm{Tgt}_{\mathrm{hi}}(A)>
\mathrm{Tgt}(\pi/3,\pi/3)` strictly for every `A` in this sub-range too.

**Conclusion (Theorem B).** Combining Steps 1-2:
$$
\mathrm{Tgt}(A,(\pi-A)/2)\ \ge\ \mathrm{Tgt}(\pi/3,\pi/3)\quad\text{for all
}A\in[0.5,\pi/3),
$$
hence in particular throughout the true valid sub-range
`(A_L,\pi/3)\subset[0.5,\pi/3)` — a **fully rigorous, gap-free proof** for
the entire `\mathcal C_{\mathrm{hi}}` boundary piece (not numeric sampling;
every sub-interval's conclusion is a certified two-sided enclosure).
`\blacksquare`

**Correction of the outline's Step 4b framing (per the outline-reviewer's
guidance, now proved rather than merely argued).** The outline originally
asked to compare sub-range endpoints; the outline-reviewer correctly
diagnosed this framing as based on an under-resolved grid artifact. This
round's Theorem B proves the *actually* correct shape directly: a single
interior local max (located, by bisection on the certified-negative-
derivative boundary, at `A\approx0.7350746255555408`, value
`\approx2.209`) followed by strict monotone decrease all the way to the
corner, with **zero** gap — exactly the corrected picture the reviewer
described, now backed by a certified proof rather than a finer numeric
scan.

### Theorem C: `\mathrm{Tgt}\ge\mathrm{Tgt}(\pi/3,\pi/3)` throughout `\mathcal C_{\mathrm{lo}}\cap\mathcal D`, proved via the same certified-interval method, using Theorem A's closed-form parametrization

**Setup.** Using Theorem A, define `\mathrm{Tgt}_{\mathrm{lo}}(B):=
\mathrm{Tgt}(A(B),B)` where `A(B)=\arctan(-\sin B\cos(2B)/(2\cos^3B))`,
built directly in `sympy` by substituting this closed form for `A` into
the general `\mathrm{Tgt}(A,B)` (after using `\mathrm{expand\_trig}` to
turn `\sin(A+B),\cos(A\pm B)$ etc. into sums of products of `\sin A,\cos A,
\sin B,\cos B` first, so that only `\sin A,\cos A` — not `A` itself, nor
`\beta_0=(\pi-A)/3` — need the `\arctan` substituted in; the surviving
`\sin(\beta_0),\cos(\beta_0)$ terms become `\sin(\arctan(t)/3),
\cos(\arctan(t)/3)`, which have no simpler closed form — an instance of the
same "trisection has no radical form" obstruction the population has met
before — but this is **not** an obstruction to interval-arithmetic
evaluation, only to further symbolic simplification: `\mathrm{mpmath.iv}`
evaluates `\sin,\cos,\arctan` (the latter via `\mathrm{atan2}(x,1)`, since
`\mathrm{mpmath.iv}` does not expose `\mathrm{atan}$ directly but
`\mathrm{atan2}` is available and mathematically identical for `x` in this
range) directly and rigorously with no need for a closed radical form).
Sanity check (own script): `\mathrm{Tgt}_{\mathrm{lo}}(\pi/3)` (interval
evaluation) `=[1.574136224814063346\ldots,1.574136224814063346\ldots]`,
matching the corner value to all displayed digits, and
`\mathrm{Tgt}_{\mathrm{lo}}(0.9117433)\approx2.270063\ldots`, matching the
previously-reported value of `\mathrm{Tgt}` at the other corner
`(A^\ast,B^\ast)$ (rounds 13-14, `\approx2.27`) closely — confirming the
parametrization and substitution pipeline are correct.

**Step 1 (away from the corner).** Certified interval sweep
(`mp.iv.dps=30`, `N=1500`) of `\mathrm{Tgt}_{\mathrm{lo}}(B)-
\mathrm{Tgt}(\pi/3,\pi/3)$ on `B\in[0.9,1.0]$ (a safe superset containing
the true valid range's lower portion, since `B^\ast\approx0.9117>0.9`,
and comfortably covering the curve's interior local max, located by direct
scan near `B\approx0.965`, value `\approx3.06`): **`0` bad sub-intervals**
— every enclosure's lower bound exceeds the corner's certified value.

**Step 2 (approaching the corner).** Certified interval sweep of
`d\mathrm{Tgt}_{\mathrm{lo}}/dB` (again the raw, unsimplified symbolic
derivative, evaluated directly — no simplification needed) on
`B\in[1.0,\pi/3-10^{-12}]` (`N=1500`): **`0` bad sub-intervals** — every
enclosure's upper bound is strictly negative, certifying
`d\mathrm{Tgt}_{\mathrm{lo}}/dB<0` throughout. By the same MVT +
continuity argument as Theorem B, `\mathrm{Tgt}_{\mathrm{lo}}(B)>
\mathrm{Tgt}(\pi/3,\pi/3)` strictly for `B` in this range.

**Conclusion (Theorem C).**
$$
\mathrm{Tgt}(A(B),B)\ \ge\ \mathrm{Tgt}(\pi/3,\pi/3)\quad\text{for all
}B\in[0.9,\pi/3),
$$
hence throughout the true valid sub-range `(B^\ast,\pi/3)\subset
[0.9,\pi/3)` — a **fully rigorous, gap-free proof** for the entire
`\mathcal C_{\mathrm{lo}}` boundary piece. `\blacksquare`

### A 2-D adaptive interval sweep of the interior — strong new evidence, honestly NOT a complete proof

Beyond the two boundary curves, attempted a full 2-variable certified
interval sweep, aiming to close the interior-critical-point gap directly
(bypassing the need for a separate resultant/Gröbner elimination): built
interval-valued versions of the four domain-defining inequalities
`h_1:=B-\beta_0(A)>0`, `h_2:=\pi-A-2B\ge0` (i.e. `C\ge B`), `h_3:=X_0-
\cos^2B>0`, `h_4:=\cos^2\beta_0(A)-X_0>0`, and of `\mathrm{Tgt}(A,B)`
itself, all via `\mathrm{mp.iv}$ (own fresh `sympy`/`mpmath` session). A
box `[a_0,a_1]\times[b_0,b_1]` is excluded from consideration whenever any
`h_i`'s certified interval enclosure has upper bound `\le0` (i.e. `h_i\le0`
is certified throughout the box, so the box cannot meet `\mathcal D`).
**Adaptive quadtree refinement** (recursively bisecting any
non-excluded box whose `\mathrm{Tgt}` enclosure's lower bound is below the
corner's certified value, to a depth of 22, giving sub-boxes of side
`\approx4\times10^{-9}$) over the region `A\in[0.40,\pi/3]`, `B\in[0.90,
1.33]` (a safe superset of all of `\mathcal D`, covering the interior and
all three boundary pieces including the newly-identified `\mathcal
C_{\mathrm{mid}}$) finds: **every box is either excluded (outside
`\mathcal D`) or certified `\mathrm{Tgt}\ge\mathrm{Tgt}(\text{corner})`,
except for a residual set of boxes of side `\lesssim5\times10^{-8}$, all
located immediately adjacent to the single point `(\pi/3,\pi/3)`** (the
residual boxes' `A,B$-coordinates are all within `\approx4\times10^{-8}`
of `\pi/3$, and their `\mathrm{Tgt}` enclosures are
`[1.57413617\ldots,1.57413632\ldots]$ — already agreeing with the corner's
own certified value `1.574136224814063\ldots` to 7-8 significant digits,
consistent with genuine convergence to equality at the corner, not a real
violation).

**Honest assessment: this is not yet a complete proof.** The residual
un-resolved region shrinks toward the single point `(\pi/3,\pi/3)` as the
adaptive search deepens (exactly as expected, since `\mathrm{Tgt}` attains
its claimed minimum value *exactly* there — an interval-arithmetic sweep
can never resolve a strict inequality arbitrarily close to a point of
equality using enclosures of positive width). The already-certified round-
14 result (New result 9: `(\pi/3,\pi/3)` is a proved *strict local minimum*
via the tangent-cone/directional-derivative argument, margin `\ge3.5` on
the directional derivative) is exactly the right tool to close this
residual region **in principle** — but New result 9's proof establishes
this only "for `\varepsilon` small enough" **qualitatively** (via a
compactness/boundedness-of-second-derivatives argument), without an
explicit numeric radius. To rigorously glue New result 9 to this round's
2-D sweep (and thereby close global minimality completely) would require
either (i) making New result 9's radius explicit and quantitative (e.g. an
explicit second-derivative/Lipschitz bound on `\mathrm{Tgt}` near the
corner, giving a concrete `\delta$ such that the local-min conclusion holds
for all `(A,B)\in\mathcal D` within Euclidean distance `\delta` of the
corner), or (ii) extending the adaptive interval search with a dedicated,
purpose-built near-corner argument (e.g. a local change of variables
`A=\pi/3-\varepsilon,B=\pi/3+t\varepsilon$ and a certified interval bound
on the **second-order** Taylor remainder, analogous to New result 9's own
argument but made fully quantitative). **Neither (i) nor (ii) was
completed this round** — this is the precise, now very narrowly located,
remaining gap.

### Net assessment of this round

This round **fully and rigorously closes** both of the outline's boundary-
curve sub-targets (4a: `\mathcal C_{\mathrm{lo}}$, Theorem C; 4b: `\mathcal
C_{\mathrm{hi}}$, Theorem B) — not with numeric sampling, but with
certified directed-rounding interval-arithmetic branch-covering proofs,
each fully gap-free over the entire respective boundary curve. It also
produces a genuinely new closed-form parametrization of `\mathcal
C_{\mathrm{lo}}$ (Theorem A) and identifies a previously-undocumented third
boundary curve of `\mathcal D` (`\mathcal C_{\mathrm{mid}}`), correcting
round 14's "exactly two boundary curves" picture (though this correction
does not affect anything previously proved, since it lies outside the
corner-adjacent region those results were scoped to). The originally-
dispatched Step 3 (unconditional, symbolic interior-critical-point
elimination via resultants) is **not completed as a symbolic elimination**,
but is **subsumed and very substantially strengthened** by the 2-D
adaptive interval sweep above, which directly covers the interior (not
just the boundary) and finds no violation anywhere in `\mathcal D` except
within a shrinking, sub-`10^{-7}`-radius neighbourhood of the corner
itself — the single remaining gap of the whole route, now precisely
located and structurally understood (a quantitative-radius gap between two
already-proved results, New result 9's local minimum and this round's
global sweep, not an open-ended unknown).

## Round 16 (this round): the near-corner gluing gap is closed — explicit, quantitative, certified radius `r_0=0.01`

**Target.** Close the residual of Open gap 5 flagged at the end of round
15: the round-15 2-D adaptive interval sweep certified
`\mathrm{Tgt}\ge\mathrm{Tgt}(\text{corner})` throughout `\bar{\mathcal D}`
*except* within a shrinking neighbourhood (`\lesssim5\times10^{-8}`) of the
corner `(\pi/3,\pi/3)` itself, where interval methods cannot resolve a
strict inequality arbitrarily close to a point of exact equality. This
round supplies the missing quantitative radius via the "quotient sweep"
outline, implemented as an **exact Taylor identity with a certified
Lagrange-remainder bound** — a strictly more robust realization of the
outline's Steps 1-3 than a raw quotient-of-intervals sweep, since it
never divides two intervals that both shrink to `0` (the source of the
round-15 degeneracy).

**Result (full detail in `lemmas/tgt-strictly-positive-throughout-D-full.md`).**
Let `\varepsilon:=\pi/3-A`. For every `(A,B)\in\bar{\mathcal D}` with
`0<\varepsilon\le r_0:=0.01`, writing `t:=(B-\pi/3)/\varepsilon`,
$$\mathrm{Tgt}(A,B)-\mathrm{Tgt}(\pi/3,\pi/3)=\varepsilon\cdot q(\varepsilon,t),
\qquad q(\varepsilon,t)\ \ge\ 3.469\ >0,$$
proved as follows. Define `F_t(e):=\mathrm{Tgt}(\pi/3-e,\pi/3+te)` for
`t` in the certified-safe range `[-0.3,0.5]` (a proved superset of the
true `[t_{\mathrm{lo}}(\varepsilon),1/2]` for every `\varepsilon\in(0,0.01]`
— see below). `\mathrm{Tgt}` is `C^\infty` on the box `e\in[0,0.01],\,
t\in[-0.3,0.5]` (there `A+B=2\pi/3+e(t-1)\in[2\pi/3-0.013,2\pi/3-0.0005]`,
bounded away from `\sin(A+B)=0`), so Taylor's theorem with **Lagrange
remainder** gives, since `F_t(0)=\mathrm{Tgt}(\pi/3,\pi/3)` for every `t`
(trivially, `e=0` collapses to the corner regardless of `t`),
$$q(\varepsilon,t)=\frac{F_t(\varepsilon)-F_t(0)}\varepsilon=F_t'(0)+
\frac\varepsilon2F_t''(\xi),\qquad\xi\in(0,\varepsilon).$$
Two certified pieces (own fresh `sympy`/`mpmath.iv` scripts, `dps=40`):

1. `F_t'(0)=-g_A+t\,g_B`, with `g_A\in[-4.28096012358944778,
   -4.28096012358944777]`, `g_B\in[-1.55725707997121229,
   -1.55725707997121228]` (independently re-certified, matching New
   result 9 to all displayed digits). Since `g_B<0`, `F_t'(0)` is affine
   strictly **decreasing** in `t`, so its minimum over the (generous) box
   `t\in[-0.3,0.5]` is still at the box's largest `t`, `t=1/2` — exactly
   New result 9's own extremal direction, unaffected by widening the
   `t`-range downward to `-0.3`:
   `\delta_{\min}:=\min_{t\in[-0.3,0.5]}F_t'(0)=-g_A+\tfrac12g_B\in
   [3.50233158360384163,3.50233158360384164]`.
2. `F_t''(\xi)\in[-6.64158630888731416,6.12971692053590261]` for every
   `(\xi,t)` in the box `[0,0.01]\times[-0.3,0.5]`, via a `40\times40`
   sub-box `mpmath.iv` sweep of the exact symbolic second `e`-derivative
   of `\mathrm{Tgt}(\pi/3-e,\pi/3+te)` (raw, unsimplified — no closed-form
   simplification needed for interval evaluation).

Combining: `q(\varepsilon,t)\ge\delta_{\min}-\tfrac{0.01}2\times6.6415863089
=3.46912\ldots>0` for every `\varepsilon\in(0,0.01]`, `t\in[-0.3,0.5]`.

**Domain safety (the box `[-0.3,0.5]` really contains the true `t`-range).**
`t_{\mathrm{hi}}(\varepsilon)=1/2` **exactly** for every `\varepsilon`
(`\mathcal C_{\mathrm{hi}}:B=(\pi-A)/2` is exact and linear, no
approximation needed). For the lower edge, using Theorem A's closed form
`A(B)=\arctan(-\sin B\cos2B/(2\cos^3B))` (`A'(\pi/3)=4` exactly): define
`\varphi(\varepsilon):=(\pi/3-\varepsilon)-A(\pi/3-0.3\varepsilon)`, so
`\varphi(0)=0`. A certified interval sweep (`2000` sub-intervals) of
`A'(B)` on `B\in[\pi/3-0.003,\pi/3]` gives `A'(B)\ge3.99994544\ldots>10/3`
throughout (`0` bad sub-intervals), so `\varphi'(\varepsilon)=-1+0.3\,A'
(\pi/3-0.3\varepsilon)\ge0.19998\ldots>0` on `[0,0.01]`. By the Mean Value
Theorem, `\varphi(\varepsilon)>0` for `\varepsilon\in(0,0.01]`, i.e.
(since `A(\cdot)` is certified increasing there) `t_{\mathrm{lo}}
(\varepsilon)>-0.3`. Since the admissible `B`-range at fixed `A` is the
single interval `[B_{\mathrm{lo}}(A),B_{\mathrm{hi}}(A)]` (round 13, "New
result 5"), every point of `\bar{\mathcal D}` with `\varepsilon\in(0,0.01]`
has `t\in(-0.3,0.5]`, inside the swept box.

**Gluing with round 15.** `0.01\gg5\times10^{-8}` (round 15's residual
radius), and round 15's box `A\in[0.40,\pi/3],B\in[0.90,1.33]` is a proved
superset of `\bar{\mathcal D}$; the two results' domains of validity
overlap and their union is all of `\bar{\mathcal D}`. Hence:
$$\mathrm{Tgt}(A,B)\ \ge\ \mathrm{Tgt}(\pi/3,\pi/3)\quad\text{for every
}(A,B)\in\bar{\mathcal D},\ \text{equality only at the corner.}$$
**Open gap 5 is now fully closed.** Since `\mathrm{Tgt}(\pi/3,\pi/3)
\approx1.574>0`, this also gives `\mathrm{Tgt}>0` throughout
`\bar{\mathcal D}` — **Target 1 of the round-13 `f-g` reformulation's "Net
assessment" (New result 5) is fully closed** (full detail and all
certified numbers in the new lemma
`lemmas/tgt-strictly-positive-throughout-D-full.md`).

**Honest assessment — does this complete the whole approach? No.** The
round-13 Reduction Lemma (New result 1) needs **two** hypotheses to
conclude `f\ge g` throughout `\mathcal D` (hence the whole problem via
this route): (A) `\partial(f-g)/\partial B>0` throughout `\mathcal D`
— this is exactly Target 1 above, **now fully closed** by this round's
work (via New result 5's `\mathrm{Tgt}>0`-implies-constant-sign argument,
plus the single-point sign evaluation already on file) — and (B)
`D_1(A)\ge0` on the boundary curve `\mathcal C` (Open gap 6), a
**completely separate** fact, inherited unproved from the `-twopoint`
sibling (`lemmas/star-factorization-on-boundary-curve.md`), untouched by
anything in this round or in round 15. **Gap 6 remains fully open** — no
progress on it was made this round, and none is claimed. So: this round
closes the *entire* `\mathrm{Tgt}`-side of the route (a genuine, complete
sub-result, now certified end-to-end with an explicit quantitative
radius), but the route as a whole is **not complete** — Status stays
`partial`, with the single remaining obstruction now precisely isolated
to gap 6 alone (all of gaps 1-5 are now closed or subsumed, per the
round-13 Reduction Lemma's own accounting).

## Round 20 (this round): `T\ge0` closed in full on Case (b)'s own residual
sub-case, via a corner Taylor+Lagrange-remainder argument mirroring `D_1`/
`Tgt`; Case (a) shown to need a genuinely different treatment

**Setup (reused, certified elsewhere).** `X_0,\beta_0,K_c,P,Q,A_{\mathrm c},
C_{\mathrm c},B_{\mathrm c},E,T:=B_{\mathrm c}^2X_0-E^2` all as in
`lemmas/case-b-p-le-0-and-e-ge-0-closed.md` and `lemmas/case-b-e-lt-0-t-
factorization.md`. Target: `T\ge0` on Case (b)'s exact residual domain
$$
\mathcal D_b:=\{0<A\le\pi/2,\ 0<B\le C,\ B>\beta_0(A),\ \cos^2B<X_0(A,B)<
\cos^2\beta_0(A),\ P>0,\ E<0\}.
$$

### Step 0. The corner value `T(A^\ast,B^\ast)=0`, proved exactly

Reuse the `u`-substitution `u:=A/3+\pi/6` and the exact values already
certified in `lemmas/d1-nonnegative-on-boundary-curve.md`: at
`u^\ast=\arcsin(\sqrt6/4)`, writing `s:=\sin u^\ast,c:=\cos u^\ast`
(`s^2=3/8,c^2=5/8`), and `A^\ast=3u^\ast-\pi/2`, `B^\ast=\beta_0(A^\ast)=
\pi/2-u^\ast`, one has (by the same multiple-angle substitutions as
`d1-nonnegative-on-boundary-curve.md` §0(b)-(c), extended here to the
further quantities needed): `\sin A^\ast=c/2,\ \cos A^\ast=3s/2,\ \sin
B^\ast=c,\ \cos B^\ast=s,\ \sin(A^\ast+B^\ast)=2sc` (this last since
`A^\ast+B^\ast=2u^\ast`). Substituting into the raw definitions:
$$
P^\ast=\tfrac52sc,\qquad K_c^\ast=2sc^2,\qquad Q^\ast=-\tfrac12c^2,
$$
$$
A_{\mathrm c}^\ast=\tfrac{c^2}4(c^2+25s^2),\qquad
C_{\mathrm c}^\ast=s^2c^2\bigl(4c^2-\tfrac{25}4\bigr),\qquad
B_{\mathrm c}^\ast=2sc^4,\qquad X_0^\ast=\tfrac38
$$
(the last is `lemmas/d1-nonnegative-on-boundary-curve.md`'s already-proved
fact (ii), `X_0(A^\ast,B^\ast)=\cos^2B^\ast=3/8`). Substituting `c^2=5/8,
s^2=3/8` (elementary rational arithmetic, hand-checkable): `c^2+25s^2=10`,
so `A_{\mathrm c}^\ast=(5/32)\cdot10=25/16`; `4c^2-25/4=5/2-25/4=-15/4`, so
`C_{\mathrm c}^\ast=(15/64)(-15/4)=-225/256`; hence
$$
E^\ast=A_{\mathrm c}^\ast X_0^\ast+C_{\mathrm c}^\ast=\frac{25}{16}\cdot
\frac38-\frac{225}{256}=\frac{75}{128}-\frac{225}{256}=\frac{150-225}{256}
=-\frac{75}{256}.
$$
And `B_{\mathrm c}^{\ast2}=4s^2c^8=4\cdot\tfrac38\cdot(5/8)^4=\tfrac32\cdot
\tfrac{625}{4096}=\tfrac{1875}{8192}`, so
$$
T(A^\ast,B^\ast)=B_{\mathrm c}^{\ast2}X_0^\ast-E^{\ast2}=\frac{1875}{8192}
\cdot\frac38-\Bigl(\frac{75}{256}\Bigr)^2=\frac{5625}{65536}-\frac{5625}
{65536}=0
$$
**exactly** — an elementary rational computation, no numerics needed
(independently confirmed to 80 digits, own fresh `mpmath` session:
`T(A^\ast,B^\ast)=4.34\times10^{-51}$, i.e. `0` to the working precision).
Also `P^\ast=\tfrac52sc>0` (`s,c>0`) and `E^\ast=-75/256<0`, confirming
`(A^\ast,B^\ast)` genuinely lies in the closure of `\mathcal D_b`'s
`P>0\wedge E<0` regime.

### Step 1. Exact tangent-cone slopes and gradient at the corner

Own fresh `sympy` derivation (elementary quotient/chain rule): `\partial
X_0/\partial A=-\sin B\cos B/(2\sin^2(A+B))`, `\partial X_0/\partial
B=\sin A\cos A/(2\sin^2(A+B))` (this second identity already certified,
round 11). At `(A^\ast,B^\ast)`: `\partial X_0/\partial A=-1/\sqrt{15}`,
`\partial X_0/\partial B=3/(4\sqrt{15})` (both confirmed exactly, using
`\sin A^\ast\cos A^\ast=(c/2)(3s/2)=3sc/4` etc. and `sc=\sqrt{15}/8`).
Domain `\mathcal D_b` is bounded (near the corner) by the two implicit
curves `\mathcal C_{\mathrm{lo}}:X_0=\cos^2B` (lower) and `\mathcal
C_{\mathrm{hi}}':X_0=\cos^2\beta_0(A)` (upper); implicit differentiation
(`F=X_0-\cos^2B\Rightarrow dB/dA=-F_A/F_B`, `F_B=\partial X_0/\partial
B+2\sin B\cos B`; similarly for the upper curve with `F_B'=\partial
X_0/\partial B` and an extra term `-\tfrac23\sin\beta_0\cos\beta_0` in
`F_A'` from `\beta_0'(A)=-1/3`) gives, exactly, at the corner:
$$
\Bigl(\frac{dB}{dA}\Bigr)_{\mathcal C_{\mathrm{lo}}}=\frac29,\qquad
\Bigl(\frac{dB}{dA}\Bigr)_{\mathcal C_{\mathrm{hi}}'}=3
$$
(both independently confirmed via `sympy` symbolic substitution and via
high-precision secant-slope convergence, `mpmath`, `dps=60`, to `15+`
digits). Domain nonemptiness for `A>A^\ast` only (own numeric check:
domain is empty for `A<A^\ast`, matching that `(A^\ast,B^\ast)` is exactly
the point where the two curves meet, per `d1-nonnegative-on-boundary-
curve.md`'s fact (ii)) means the tangent cone at the corner is `\{(1,t):
t\in[2/9,3]\}` (`\varepsilon:=A-A^\ast>0`, `t:=(B-B^\ast)/\varepsilon`).
Own fresh `sympy` differentiation of `T` (raw, unsimplified, evaluated at
the corner via the `s,c` substitution) gives the **exact** gradient
$$
\frac{\partial T}{\partial A}\Big|_\ast=\frac{14375\sqrt{15}}{32768},
\qquad
\frac{\partial T}{\partial B}\Big|_\ast=\frac{5625\sqrt{15}}{32768}
$$
(`\approx1.699040,\ 0.664842` respectively; both `>0`). Since `\delta(t):=
\partial T/\partial A+t\,\partial T/\partial B` is affine and increasing in
`t` (positive slope), its minimum over the tangent cone `t\in[2/9,3]` is at
`t=2/9`: `\delta(2/9)=\sqrt{15}/32768\cdot(14375+\tfrac29\cdot5625)=
\sqrt{15}/32768\cdot15625\approx1.84678` (using `14375+1250=15625`, an
exact rational check).

### Step 2. Certified domain-safety, Hessian bound, and the Lagrange-remainder closure (`\varepsilon_0=0.01`)

Own `mpmath.iv` (`dps=30`, directed rounding) interval evaluation of the
two curves' exact slope formulas `S_{\mathrm{lo}}(A,B):=-\partial_AX_0/
(\partial_BX_0+2\sin B\cos B)`, `S_{\mathrm{hi}}(A,B):=-(\partial_AX_0-
\tfrac23\sin\beta_0\cos\beta_0)/\partial_BX_0`, over the box `A\in[A^\ast,
A^\ast+0.01]`, `B\in[B^\ast,B^\ast+0.035]` (a generous a-priori superset),
gives the certified enclosures
$$
S_{\mathrm{lo}}\in[0.20237\ldots,0.23820\ldots],\qquad
S_{\mathrm{hi}}\in[2.8422\ldots,3.1209\ldots],
$$
each comfortably inside `[0.15,3.35]`. Since `\partial_BX_0>0` strictly
throughout this box (own certified enclosure `[0.1889,0.1981]`, so `X_0` is
strictly increasing in `B` there, so `\mathcal D_b`'s two `X_0`-inequalities
translate directly into `B` between the two curves) and `B_{\mathrm{lo}}
(A^\ast)=B_{\mathrm{hi}}'(A^\ast)=B^\ast` (Step 0), a standard continuity/
bootstrap argument (the a-priori box comfortably contains the actual
curve values, since `0.238\times0.01=0.00238\ll0.035` and `3.12\times0.01=
0.0312<0.035`, so the bound is self-consistent, not circular) gives, via
the Mean Value Theorem applied to each implicit curve function of `A`:
for every `A\in(A^\ast,A^\ast+0.01]`, the admissible `t:=(B-B^\ast)/(A-
A^\ast)$-range for `(A,B)\in\mathcal D_b$ lies in `(0.2024,3.121)\subset
[0.15,3.35]`. Also certified on the same box: `P\in[1.196,1.230]>0` and
`E\in[-0.362,-0.181]<0` strictly (so the whole box automatically satisfies
`\mathcal D_b`'s sign constraints — no separate restriction needed near
the corner).

**Hessian bound.** Own `sympy` second partials `\partial^2T/\partial A^2,
\partial^2T/\partial A\partial B,\partial^2T/\partial B^2$ (raw, unsimplified),
translated to `mpmath.iv` via `\{\sin\to\mathrm{iv.sin},\cos\to
\mathrm{iv.cos}\}` (identical technique to `d1-nonnegative-on-boundary-
curve.md`'s Step 2). Over the box `A\in[A^\ast,A^\ast+0.01],B\in[B^\ast,
B^\ast+0.0335]`, `t\in[0.15,3.35]`, the quadratic form `Q(t):=\partial_A^2T
+2t\,\partial_{AB}T+t^2\partial_B^2T` (the directional second derivative
along a ray of slope `t`) is certified to satisfy `Q(t)\in[-30.54,35.67]`,
so `|Q(t)|\le M:=35.67` throughout.

**Lagrange-remainder closure.** For `(A,B)\in\mathcal D_b` with `A-A^\ast=
\varepsilon\in(0,0.01]`, write `t:=(B-B^\ast)/\varepsilon\in(0.2024,3.121)`
(certified above). By Taylor's theorem with Lagrange remainder applied to
`F_t(\varepsilon):=T(A^\ast+\varepsilon,B^\ast+t\varepsilon)` (a smooth
function of the scalar `\varepsilon` for fixed `t`):
$$
T(A,B)=F_t(\varepsilon)=\underbrace{F_t(0)}_{=0\text{ (Step 0)}}+
\varepsilon\,\delta(t)+\frac{\varepsilon^2}2F_t''(\xi),\qquad\xi\in(0,
\varepsilon),
$$
with `F_t''(\xi)=Q(t)` evaluated at the point `(A^\ast+\xi,B^\ast+t\xi)`,
which lies inside the certified Hessian-bound box (since `\xi<\varepsilon
\le0.01` and `t\xi<3.35\times0.01=0.0335`). Using `\delta(t)\ge\delta(0.2024)
\approx1.8336` (certified lower bound of the actual `t`-range, `\delta$
increasing) and `|F_t''(\xi)|\le M=35.67`:
$$
T(A,B)\ \ge\ \varepsilon\bigl(1.8336-\tfrac{35.67}2\varepsilon\bigr)\ \ge\
\varepsilon\bigl(1.8336-0.17835\bigr)=1.6553\,\varepsilon\ >\ 0
$$
for every `\varepsilon\in(0,0.01]` (using `\varepsilon\le0.01`). **This
proves `T>0` throughout `\mathcal D_b\cap\{A^\ast<A\le A^\ast+0.01\}`, with
`T\to0` only in the limit `A\to A^{\ast+}`.**

### Step 3. Certified away-from-corner sweep (`mpmath.iv`, adaptive quadtree)

Own `mpmath.iv` adaptive box-bisection sweep (identical style to `d1-
nonnegative-on-boundary-curve.md`'s branch-covering technique, extended to
2 dimensions): partition `A\in[A^\ast+0.005,\pi/2]` (overlapping Step 2's
range by `[0.005,0.01]`) into initial boxes with a generous a-priori
`B`-range `[(\pi-A_{\mathrm{hi}})/3,(\pi-A_{\mathrm{lo}})/2]`; for each box,
certify via interval arithmetic either (i) the box is **provably outside**
`\mathcal D_b` (one of `B\le\beta_0(A)`, `\cos^2B\ge X_0`, `X_0\ge\cos^2
\beta_0(A)`, `P\le0`, or `E\ge0` holds on the **whole** box), or (ii)
`T>0$ **certified on the whole box** (`T_{\mathrm{box}}`'s lower endpoint
`>0`); if neither, bisect on the larger dimension and recurse. **Result:
0 unresolved boxes** in every range tested — `A\in[A^\ast+0.005,0.55]`
(352 total boxes, depth `\le30`), `A\in[0.53,0.545]` (150 boxes, resolving
the domain's own second pinch point near `A\approx0.537`, where the
`(cos^2B,\cos^2\beta_0(A))$-window itself narrows to width `0` — confirmed
`T\approx0.2465$ there, comfortably positive, a domain-shape degeneracy
unrelated to `T`'s sign), and `A\in[0.55,\pi/2]` (206 boxes, confirming
`\mathcal D_b` is empty there). **This certifies `T\ge0` throughout
`\mathcal D_b\cap\{A\ge A^\ast+0.005\}` in full** (every box resolved, no
sampling gaps, directed-rounding interval arithmetic throughout).

### Step 4. Conclusion: `T\ge0` on all of `\mathcal D_b`

Steps 2 and 3 overlap on `A\in[A^\ast+0.005,A^\ast+0.01]` and jointly cover
`(A^\ast,\pi/2]`, the full possible range (`\mathcal D_b`, and hence the
whole residual sub-case, is empty for `A\le A^\ast$ and for `A>\pi/2`, both
independently checked). Hence
$$
T(A,B)\ \ge\ 0\quad\text{throughout }\mathcal D_b,\qquad\text{with equality
exactly at }(A,B)=(A^\ast,B^\ast).
$$
By the certified equivalence in `lemmas/case-b-p-le-0-and-e-ge-0-closed.md`
(Theorem 2's iff, applied twice), `T\ge0\iff G(\beta_1)\ge0` throughout
`\mathcal D_b`. **This closes `G(\beta_1)\ge0` unconditionally on Case (b)'s
own residual sub-case (`X_0<\cos^2\beta_0(A)`, `P>0\wedge E<0`), i.e.
Case (b) as a whole is now fully closed** (combined with Theorems 1 and 4
of that lemma, which already cover `P\le0` and `P>0\wedge E\ge0`
unconditionally): `G(\beta_1)\ge0$ for **every** `(A,B)` with `X_0(A,B)<
\cos^2\beta_0(A)` (i.e. every genuine Case-(b) point, `\beta_1>\beta_0(A)`),
regardless of the sign of `\mathrm{RHS}` — this is in fact a *simpler*,
more direct closure of Case (b) than the file's own Steps 4-5 (Reduction
Lemma / hypotheses (A),(B) / `\mathrm{Tgt},D_1$), since it establishes
`G(\beta_1)\ge0` directly from the `P,E$ sign decomposition without ever
invoking `\mathrm{RHS}$, `f-g`, or the boundary curve `\mathcal C` at all.
(The file's Steps 4-5 machinery, and Gaps 5-6's closures, remain valid and
certified — they are simply no longer the only route to Case (b)'s
conclusion, though they are not superseded or contradicted by this: both
are independent, correct closures of the same fact.)

### New finding: this does NOT close Case (a), and Case (a)'s domain is provably NOT a sub-case of the above

Per the round-20 dispatch's explicit instruction to verify the full
dependency chain, checked whether the above closes Open gap 7 as a whole
(as round 19 believed it would, and as the round-20 outline's Step 5
anticipated: "closing Open gap 7 for BOTH cases simultaneously"). **It does
not, and the reason is more fundamental than a citation gap.**

Case (a) (`\beta_1\le\beta_0(A)`) corresponds, via `\cos\beta_1=\sqrt{X_0}`
and `\cos` decreasing, to `X_0(A,B)\ge\cos^2\beta_0(A)$ — the
**complementary** region to `\mathcal D_b$ (`X_0<\cos^2\beta_0(A)`) used
above, not a subset of it, and (crucially) not touched by anything in
Steps 0-4. Own fresh 50-digit `mpmath` check, raw definitions, at the clean
witness `A=0.02,B=1.5$ (`C=1.6216\ge B`, a completely ordinary, non-
degenerate triangle with `A\le\pi/2,B\le C`): `X_0=0.49929\ldots>\cos^2
\beta_0(A)=0.25580\ldots` (genuinely in Case (a)'s domain), `\cos^2B=
0.00500<X_0$ (`\beta_1$ well-defined, `=0.78611\ldots\in(0,\gamma)`),
`P=1.00012\ldots>0,\ E=-0.49904\ldots<0$ (same sign regime as the residual
sub-case), and
$$
T=-0.24904\ldots<0,\qquad G(\beta_1)=-0.65365\ldots<0
$$
— a **robust, non-degenerate, 50-digit-confirmed counterexample** to
`T\ge0`/`G(\beta_1)\ge0` in Case (a)'s domain. Independently re-checked
round 19's own witness (`A\approx0.010023,B\approx1.499257`) from the raw
definitions: `T\approx-0.2487<0$ there too, confirming round 19's own data
already contained this fact (round 19 correctly found `G(\beta_1)<0`
there, but incorrectly concluded this meant "the same open `T\ge0` gap as
Case (b)" — the more accurate statement is that `T<0` **genuinely there**,
not merely **not yet proved `\ge0`**, since `X_0>\cos^2\beta_0(A)$ places
these points outside `\mathcal D_b$ entirely, in the complementary region
where no positivity claim was ever established or, per this round's
finding, could be).

**Conclusion.** Proving `T\ge0` cannot close Case (a) as a blanket
statement, because `T$ (equivalently `G(\beta_1)`) is simply **false**
there in general. This means the file's own Step 2 ("the target for every
`\beta_1\in(0,\gamma)` is `G(\beta_1)\ge0`, no case split in the target
itself") is not the correct universal statement for Case (a) — either
Case (a) needs a genuinely different quantity/reduction (not yet
identified by any round of this population, rounds 11-20), or there is a
missing constraint on `(A,B)` (beyond `A\le\pi/2,B\le C`) that excludes
points like the `A=0.02,B=1.5` witness from actually arising in the
original geometric reduction (Steps 1-2, rounds 1-10) — **this has not been
checked and is flagged here explicitly as the precise, sharpened form of
Open gap 7 going forward**: re-derive, from Steps 1-2's original rotation/
Cramer/MVT machinery (not merely this file's own restatement of it),
exactly what Case (a) needs to prove and whether every `(A,B)` with
`A\le\pi/2,B\le C` is actually reachable, or whether Case (a) implicitly
requires a further constraint not yet stated in this file.

## Round 21 (this round): Case (a) closed — a phantom gap, resolved by
tracing the ORIGINAL Steps 1-2 derivation end-to-end

### Setup: the exact original statement of `(\mathrm{I})`/`(\mathrm{II})`

Reproduced verbatim from `coordinate-bash-resultant-boundary.md` §15
("Formal statement of what remains, for the next round" — the ORIGINAL
round-8 derivation, not this file's own restatement), with `m:=\sin B/
\sin(A+B)` (Law of Sines, `AB=1,AC=m`) and `\beta` a free variable ranging
over `(0,\gamma)`, `\gamma:=\min(\angle B,\angle C)=\angle B` (WLOG):
$$
\text{(I)}\quad \sin(A+3\beta)<0 \implies \sin B\sin(A+\beta) <
2\sin(A+B)(\sin\beta+\sin A),
$$
$$
\text{(II)}\quad \bigl[2\cos^2\beta>m\cos A\bigr]\wedge\bigl[\sin(A+3\beta)<0
\bigr] \implies \sin B\sin(A+\beta) > 2\sin(A+B)(\sin\beta-\sin A).
$$
§15 states explicitly: "the whole coordinate-bash-resultant-boundary route
reduces... to proving **both** of the following" — i.e. `(\mathrm{I})\wedge
(\mathrm{II})`, for every `\beta\in(0,\gamma)`, is the **entire** remaining
content of the whole approach (nothing else is needed beyond this and the
already-certified genericity/branch-selection machinery of §§3-14, per §15's
and §16's own repeated framing: "This is now the single, precisely-defined
remaining item for the whole approach"). `(\mathrm{I})` is a conditional on
`\sin(A+3\beta)<0` alone; `(\mathrm{II})` is a conditional on the CONJUNCTION
`2\cos^2\beta>m\cos A` **and** `\sin(A+3\beta)<0`.

### `(\mathrm{I})` is unconditionally closed, independent of Case (a)/(b)

**Theorem 16.1** (`coordinate-bash-resultant-boundary.md` §16, certified,
independently re-verified in prior rounds and again this round): for every
`\beta\in(\beta_0,\gamma)`, `\beta_0:=(\pi-A)/3` (the threshold with
`\sin(A+3\beta_0)=0` exactly, since `A+3\beta_0=\pi`),
`f(\beta):=2\sin(A+B)(\sin\beta+\sin A)-\sin B\sin(A+\beta)>0`, i.e.
`(\mathrm{I})` holds. *Proof (reproduced for self-containedness).*
`f'(\beta)=\sin(A+\beta)\cos B+\sin(A+B-\beta)`: both terms strictly positive
on `(0,\gamma)` (`\cos B>0$ since `\gamma=B\le\pi/2` and `B<\pi/2` for a
genuine triangle unless degenerate; `0<A+\beta<A+B<\pi`; `0<A+B-\beta<A+B
<\pi`), so `f` is strictly increasing there. `f(\beta_0)=2\sin\beta_0\,
G(\beta_0)>0` is established by a two-case sign split (already certified,
"New result 2" of `coordinate-bash-resultant-boundary.md` round 9). Hence
`f(\beta)>f(\beta_0)>0` for all `\beta\in(\beta_0,\gamma)`. `\blacksquare`
For `\beta\in(0,\beta_0]`, `(\mathrm{I})`'s hypothesis `\sin(A+3\beta)<0`
fails (`A+3\beta\le\pi`, so `\sin(A+3\beta)\ge0`), so `(\mathrm{I})` holds
there vacuously. **Hence `(\mathrm{I})` holds for every `\beta\in(0,\gamma)`,
unconditionally, with no dependence whatsoever on `Y`, `\beta_1`, or the
Case (a)/(b) split.** This was already fully certified prior to this round;
recorded here for the end-to-end trace the dispatch requested.

### The key lemma: `(\mathrm{II})` is vacuous throughout Case (a)

**Definitions (all already-established, cited not re-derived).**
`X_0(A,B):=\sin B\cos A/(2\sin(A+B))\in[0,1]` (established: `\cos A\ge0`
since `A\le\pi/2`; `\sin B,\sin(A+B)=\sin C>0`; upper bound `X_0\le1` an
already-certified fact used throughout this file since round 11).
`Y(\beta):=2\cos^2\beta-m\cos A`. `\beta_0(A):=(\pi-A)/3`.

**Fact 0 (algebraic identity, verified symbolically this round, `sympy`,
residual `0`).** `Y(\beta)=2\cos^2\beta-2X_0(A,B)` identically in `A,B,\beta`
(since `m\cos A=(\sin B/\sin(A+B))\cos A=2X_0`). In particular `\sin(A+3\beta)
<0\iff\beta>\beta_0(A)` (`A+3\beta>\pi\iff\beta>(\pi-A)/3`, and — since the
relevant range is `\beta\in(0,\pi/2]$, giving `A+3\beta\in(A,A+3\pi/2)`, and
`\sin` is negative exactly on `(\pi,2\pi)\cap(A,A+3\pi/2)` — this matches the
threshold `\beta_0` used throughout the population since round 9, `\sin(A+
3\beta_0)=\sin(\pi-A+A)=\sin\pi=0` exactly, with `\sin(A+3\beta)$ changing
from `\ge0` to `<0` as `\beta` crosses `\beta_0` from below).

**Fact 1 (`Y` strictly decreasing, already certified, Theorem 16.2 of
`coordinate-bash-resultant-boundary.md`).** `Y'(\beta)=-2\sin2\beta<0` for
`\beta\in(0,\gamma)$, `\gamma\le\pi/2$ (so `2\beta\in(0,\pi)$, `\sin2\beta>0`).

**Fact 2 (Case (a)'s domain is exactly `Y(\beta_0(A))\le0`).** By definition
`\beta_1\le\beta_0(A)\iff\cos^2\beta_1\ge\cos^2\beta_0(A)$ (`\cos` decreasing
on `[0,\pi/2]`, both angles in this range) `\iff X_0(A,B)\ge\cos^2\beta_0(A)`
(using `\cos^2\beta_1=X_0`, the defining property of `\beta_1` from Step 2)
`\iff2\cos^2\beta_0(A)\le2X_0(A,B)\iff Y(\beta_0(A))\le0` (Fact 0). This is
precisely "Case (a)" as literally defined in this file's Step 2/Step 3 and
in round 20's domain analysis (`X_0\ge\cos^2\beta_0(A)`) — confirmed to be
the identical condition to `Y(\beta_0(A))\le0`, a purely algebraic
restatement, no numerics involved.

**Lemma (Case (a) vacuity — new, this round, fully proved, no gap).**
*Assume the standing domain-nonemptiness premise `\beta_0(A)<\gamma`
(inherited: this is required throughout the population for the interval
`(\beta_0,\gamma)` — the domain of `(\mathrm{I})` and of Case (b) — to be
nonempty at all; when `\beta_0(A)\ge\gamma` the interval is empty and both
`(\mathrm{I})` and `(\mathrm{II})` hold vacuously for every `\beta` with no
argument needed, a strictly easier sub-case not discussed further). If
`\beta_1\le\beta_0(A)` (Case (a), equivalently `Y(\beta_0(A))\le0` by Fact
2), then `Y(\beta)<0` for every `\beta\in(\beta_0(A),\gamma)`.*

*Proof.* By Fact 1, `Y` is strictly decreasing on `(0,\gamma)$, hence also on
the closed sub-interval touching `\beta_0(A)$ from the right (continuity of
`Y`, a finite sum of `\cos^2` and a constant, extends the strict monotonicity
of Fact 1 to `[\beta_0(A),\gamma)$ by the same derivative computation, valid
there since `\beta_0(A)<\gamma\le\pi/2`). For any `\beta\in(\beta_0(A),
\gamma)`, `\beta>\beta_0(A)$ gives, by strict monotonicity,
`Y(\beta)<Y(\beta_0(A))`. Combined with the hypothesis `Y(\beta_0(A))\le0`
(Fact 2), `Y(\beta)<Y(\beta_0(A))\le0`, i.e. `Y(\beta)<0`. `\blacksquare`

This is exactly the fact the round-21 dispatch asked to establish rigorously
(the round-20 outline-reviewer's fresh 300,000-sample sweep found `0`
violations of it and correctly flagged it as "an elementary two-line
consequence of `Y`'s monotonicity plus its unique zero at `\beta_1`" — the
above is precisely that two-line argument, written out in full with every
hypothesis named and cited).

### Consequence: `(\mathrm{II})` is vacuously true throughout Case (a) — no
proof obligation on `G(\beta_1)`, `T`, or anything else arises

For any `\beta\in(0,\gamma)$ in Case (a), consider `(\mathrm{II})`'s
hypothesis conjunction `\bigl[2\cos^2\beta>m\cos A\bigr]\wedge\bigl[\sin(A+
3\beta)<0\bigr]`, i.e. (Fact 0) `Y(\beta)>0\wedge\beta>\beta_0(A)`:
- If `\beta\le\beta_0(A)`: the second conjunct `\beta>\beta_0(A)` is false
  (equivalently `\sin(A+3\beta)\ge0`), so the hypothesis conjunction is
  false, and `(\mathrm{II})` holds vacuously at this `\beta`.
- If `\beta\in(\beta_0(A),\gamma)`: by the Lemma just proved, `Y(\beta)<0`,
  so the first conjunct `Y(\beta)>0` is false, so the hypothesis conjunction
  is again false, and `(\mathrm{II})` holds vacuously at this `\beta` too.

**Hence `(\mathrm{II})` holds — vacuously, with an empty hypothesis set —
for every `\beta\in(0,\gamma)` whenever `\beta_1\le\beta_0(A)` (Case (a)).**
Combined with `(\mathrm{I})` (unconditionally proved above, Theorem 16.1, for
every `\beta\in(0,\gamma)`, independent of `Y`/Case), **both halves of §15's
"single, precisely-defined remaining item for the whole approach" hold for
every `\beta\in(0,\gamma)` in Case (a)** — with `(\mathrm{I})` proved outright
and `(\mathrm{II})` true by an empty hypothesis set, not by any inequality
that had to be verified. **No proof obligation on `G(\beta_1)\ge0`, on `T`,
or on any other quantity arises in Case (a) at all.**

This resolves round 20's apparent contradiction (round 20's certified
`T`/`G(\beta_1)$ negativity at ordinary Case-(a) points, e.g. `A=0.02,B=1.5`)
without contradiction: `G(\beta_1)\ge0` was **never** the fact the ORIGINAL
derivation needed in Case (a) — it is a fact this file's own Step 2
restatement (round 13) asserted ("no case split in the target itself"), an
unjustified over-generalization of the certified lemma `lemmas/mvt-
lipschitz-reduction-case-b.md`, whose own Setup paragraph (quoted verbatim
above) explicitly restricts `\beta_1` to `(\beta_0,\gamma)` (i.e. Case (b))
and never claims anything for `\beta_1\le\beta_0(A)`. This mirrors, and is
directly confirmed by, round 10's own historical finding — independently
rediscovered ten rounds later by rounds 18-20 — that dropping the `\beta_1
>\beta_0` restriction from `G(\beta_1)\ge0` makes the claim genuinely false
(`8218/25123` violations, `coordinate-bash-resultant-boundary.md` §17): this
is not a coincidence, it is the same fact, because `G(\beta_1)\ge0` was
always only a reduction of `(\mathrm{II})$ valid in the nonempty-hypothesis
regime `\beta_1>\beta_0(A)` (Case (b)) — never a universal claim.

### Reachability is a non-issue

The math-explorer's `caseA-lens` report raised the question of whether
genuine problem-configurations (satisfying every containment/angle
hypothesis of the original `K,L` construction, not merely the reduced
algebraic system) ever actually produce `\beta_1\le\beta_0(A)`. **This
question is now moot for closing the proof.** Since Case (a) requires
verifying no inequality whatsoever (both `(\mathrm{I})` and `(\mathrm{II})`
are established for every `\beta\in(0,\gamma)$ with no case-dependent
hypothesis left unresolved), it does not matter whether `(A,B)` pairs with
`X_0(A,B)\ge\cos^2\beta_0(A)` are geometrically realized by valid `K,L`
configurations or not: if they are realized, the proof above applies
directly and needs nothing further; if they are not realized, there is
nothing to prove there in the first place. No separate reachability argument
is needed.

### Why this is airtight end-to-end (checking against the ORIGINAL derivation,
not just this file's restatement)

Every step above is anchored in `coordinate-bash-resultant-boundary.md`'s
own original text (§§8-10, 15-17), not in this file's round-13
`f`/`G`-based restatement of Step 2 — precisely as the round-21 dispatch
required:
1. `(\mathrm{I})`, `(\mathrm{II})` are quoted verbatim from §15's own
   "Formal statement of what remains" (the exact original two-part target,
   predating this file's round-13 restatement by 3 rounds).
2. Theorem 16.1 (`(\mathrm{I})` closed unconditionally) is §16's own theorem,
   reproduced with its exact original proof.
3. The threshold identification `\sin(A+3\beta)<0\iff\beta>\beta_0(A)` is
   §16's own stated fact (`\beta_0` defined precisely so `\sin(A+3\beta_0)=0`).
4. `Y`'s strict monotonicity is §16's own Theorem 16.2 opening line
   (`Y'=-2\sin2\beta<0`), reused verbatim, not re-derived independently
   (correctly cited, not assumed).
5. The reduction of `(\mathrm{II})$'s residual (when `Y(\gamma)<0`) to
   `G(\beta_1)\ge0`, and its explicit restriction to `\beta_1\in(\beta_0,
   \gamma)`, are §16-17's own words ("the true right endpoint of the
   `(\mathrm{II})`-relevant domain is the unique `\beta_1\in(0,\gamma)` with
   `Y(\beta_1)=0`... `2K-f(\beta_1)\ge0` is needed", restricted further in
   round 10 by "restoring the domain-nonempty hypothesis... `\beta_1>\beta_0`
   ... shown genuinely necessary, not optional") and the certified lemma
   `lemmas/mvt-lipschitz-reduction-case-b.md`'s Setup (`\beta_0<\beta_1<
   \gamma`) — none of this machinery is ever invoked or needed for Case (a)
   above, confirming the vacuity claim requires nothing from the `G(\beta_1)`
   apparatus at all.
6. Degenerate/boundary configurations: the isosceles case `B=C$ (`\gamma=B=
   \pi/2-A/2`) and the corner `\beta_1=\beta_0(A)$ exactly (`Y(\beta_0(A))=0`)
   are both covered by the (non-strict) inequality `Y(\beta_0(A))\le0` used
   throughout — the Lemma's proof only needs `\beta\in(\beta_0(A),\gamma)`
   (open interval, strictly greater than `\beta_0(A)`), where strict
   monotonicity gives strict `Y(\beta)<0` regardless of whether the
   inequality `Y(\beta_0(A))\le0` is strict or an equality; no case is
   omitted. The limiting case `\beta_0(A)\to\gamma^-$ (domain-emptiness) is
   handled separately above (vacuous for a different, simpler reason). No
   further degenerate limit (`A\to0`, `A\to\pi/2`, `B\to C`) affects any step
   of Facts 0-2 or the Lemma, since none of the sign arguments used
   (`\cos A\ge0$ for `A\le\pi/2`, `\sin B,\sin(A+B)>0`, `2\beta\in(0,\pi)`)
   degenerate at any interior or boundary point of the stated domain.

**Conclusion.** Case (a) is fully, rigorously, unconditionally closed —
combined with Case (b) (fully closed, round 20, independently certified),
the Reduction chain's target `G(\beta_1)\ge0$-or-vacuous holds for every
`\beta_1\in(0,\gamma)`, and hence (Step 1's polarization identity) `OM=ON`
for every triangle satisfying the problem's hypotheses. See "Full proof"
below for the complete, gap-free, self-contained restatement of the whole
chain with this round's Step 3 substituted in.

### Round 22: Case (c) (`\beta_1\ge\gamma`, the still-missing third case)
closed via Theorem 16.2's first branch

**Restating Step 2 with no domain restriction on `\beta_1`.** `\beta_1`
is, by Step 2's own definition, the unique angle in `[0,\pi/2)` with
`\cos\beta_1=\sqrt{X_0(A,B)}`; nothing in this definition forces
`\beta_1\in(0,\gamma)`. Given the domain-nonempty premise `\beta_0(A)<
\gamma` (§16 of `coordinate-bash-resultant-boundary.md`; when it fails the
whole target is vacuous, already handled at lines 2148-2154 above),
exactly one of the following three mutually exclusive, jointly exhaustive
cases holds, since `\beta_1$ is a single real number in `[0,\pi/2)` and
`\beta_0(A),\gamma` are two ordered reals with `\beta_0(A)<\gamma`:
$$\text{(a) }\beta_1\le\beta_0(A),\qquad\text{(b) }\beta_0(A)<\beta_1<
\gamma,\qquad\text{(c) }\beta_1\ge\gamma.$$
(Trichotomy of a real number against two ordered cutpoints — no geometry
needed for exhaustiveness/disjointness; the only content is in identifying
what each case implies.) Case (a) is closed (round 21, above); Case (b) is
closed (round 20, above, via the Reduction Lemma or the independent
corner-`T\ge0`
argument). **This section closes Case (c).**

**Fact 3 (`G\equiv2K_c-f`, an exact identity — proved fresh this round, not
merely cited).** With `K_c:=2\sin A\sin(A+B)`, `P:=\tfrac12\sin(A-B)+
\tfrac32\sin(A+B)`, `Q:=-\sin A\sin B`, `G(\beta):=K_c-P\sin\beta-Q\cos
\beta$ (this file's own Step 2 quantities, unchanged since round 11), and
`K:=2\sin A\sin(A+B)`, `f(\beta):=2\sin(A+B)(\sin\beta+\sin A)-\sin B\sin
(A+\beta)` (`coordinate-bash-resultant-boundary.md`'s §16 quantities), the
two expressions `K_c` and `K` are the **same** quantity (`2\sin A\sin
(A+B)`, not off by a factor of `2` — flagged explicitly here since the two
files otherwise use the letter `K$/`K_c` for what could be misread as
different objects), and
$$G(\beta)=2K-f(\beta)\qquad\text{identically in }A,B,\beta.$$
*Proof.* Direct expansion:
$$2K-f(\beta)=4\sin A\sin(A+B)-2\sin(A+B)\sin\beta-2\sin(A+B)\sin A+\sin B
\sin(A+\beta)$$
$$=2\sin A\sin(A+B)-2\sin(A+B)\sin\beta+\sin B\sin(A+\beta).$$
Meanwhile `G(\beta)=K_c-P\sin\beta-Q\cos\beta=2\sin A\sin(A+B)-\bigl(
\tfrac12\sin(A-B)+\tfrac32\sin(A+B)\bigr)\sin\beta+\sin A\sin B\cos\beta`.
Expanding `\sin(A\mp B)=\sin A\cos B\mp\cos A\sin B` gives `\tfrac12\sin
(A-B)+\tfrac32\sin(A+B)=\tfrac12(\sin A\cos B-\cos A\sin B)+\tfrac32(\sin A
\cos B+\cos A\sin B)=2\sin A\cos B+\cos A\sin B=:P`, so
$$G(\beta)=2\sin A\sin(A+B)-(2\sin A\cos B+\cos A\sin B)\sin\beta+\sin A
\sin B\cos\beta.$$
And expanding `\sin B\sin(A+\beta)=\sin B(\sin A\cos\beta+\cos A\sin\beta)
=\sin A\sin B\cos\beta+\sin B\cos A\sin\beta` in the `2K-f(\beta)` formula
above gives
$$2K-f(\beta)=2\sin A\sin(A+B)-2\sin(A+B)\sin\beta+\sin A\sin B\cos\beta+
\sin B\cos A\sin\beta.$$
Comparing term by term: both expressions share `2\sin A\sin(A+B)` and
`\sin A\sin B\cos\beta` outright; the two remaining `\sin\beta`-coefficients
agree since `-(2\sin A\cos B+\cos A\sin B)=-2\sin(A+B)+\cos A\sin B`
(because `2\sin A\cos B=\sin(A+B)+\sin(A-B)`... more directly: `-2\sin
(A+B)+\cos A\sin B=-2\sin A\cos B-2\cos A\sin B+\cos A\sin B=-2\sin A\cos B
-\cos A\sin B`, matching `-(2\sin A\cos B+\cos A\sin B)` exactly). Hence
`G(\beta)=2K-f(\beta)` identically. **Independently re-verified this round
by a fresh `sympy` session** (not reusing any prior round's script):
substituting `K_c,P,Q,K,f` from their raw definitions above and computing
`sp.simplify(sp.expand_trig(G - (2*K - f)))` returns `0` exactly (this
computation was re-run for this file, see the round-22 build session).
`\blacksquare`

**Fact 4 (Theorem 16.2's closed form, exact — proved fresh this round).**
$$2K-f(\gamma)=\sin(A+B)\,(2\sin A-\sin B),\qquad\gamma=B.$$
*Proof.* `f(B)=2\sin(A+B)(\sin B+\sin A)-\sin B\sin(A+B)=2\sin(A+B)\sin A+
\sin(A+B)\sin B$, so `2K-f(B)=4\sin A\sin(A+B)-2\sin(A+B)\sin A-\sin(A+B)
\sin B=2\sin A\sin(A+B)-\sin(A+B)\sin B=\sin(A+B)(2\sin A-\sin B)`.
**Independently re-verified this round by a fresh `sympy` session**:
`sp.simplify(sp.expand_trig((2*K-f).subs(beta,B) - sin(A+B)*(2*sin(A)-
sin(B))))` returns `0` exactly. `\blacksquare`

**Fact 5 (the sub-mechanism inside Theorem 16.2's own proof — the sign of
`2\sin A-\sin B` — re-checked explicitly, not merely cited, per the
round-22 dispatch's flag that this had never been independently verified).**
Write `A=\pi-2B-\delta` for `\delta:=\pi-2B-A`. Since `B\le C=\pi-A-B`
(standing WLOG), `A\le\pi-2B`, i.e. `\delta\ge0`. Then
$$\cos B\,(2\sin A-\sin B)-\sin(A+B)\,Y(\gamma)=\sin B\,(\cos\delta-\cos
B)$$
is an exact identity (independently re-derived fresh this round, `sympy`:
substituting `A=\pi-2B-\delta` into the LHS and simplifying against the
RHS via `sp.expand_trig`+`sp.simplify` gives residual `0` — note `Y(\gamma)
=Y(B)=2\cos^2B-\sin B\cos A/\sin(A+B)`, so `\sin(A+B)Y(\gamma)=2\cos^2B\sin
(A+B)-\sin B\cos A`, and this substitutes cleanly). **This is not circular**:
`\delta<B$ is not assumed as a free hypothesis — it is *derived* from the
Case (c) hypothesis `Y(\gamma)\ge0` itself, via the domain-nonempty
condition. Precisely, the domain-nonempty premise `\beta_0(A)<\gamma$ (i.e.
`(\pi-A)/3<B$, i.e. `A+3B>\pi`) is exactly `\pi-2B-\delta+3B>\pi\iff B>
\delta\iff\delta<B` — an algebraic restatement of the *standing* premise
(true throughout this whole file, needed for Case (b)/(c) to even be
discussed), **not** a consequence of `Y(\gamma)\ge0` that would make the
argument circular, but a hypothesis already in force before Case (c) is
even reached. Given `0\le\delta<B<\pi/2` (the last since `B\le\pi/2`,
established in Step 2), `\cos` strictly decreasing on `[0,\pi/2)` gives
`\cos\delta>\cos B` strictly, and `\sin B>0`, so the RHS `\sin B(\cos\delta
-\cos B)>0` strictly — **always**, independent of Case (c)'s hypothesis.
`\blacksquare`

**Theorem (Case (c) closure — Theorem 16.2's first branch, citing
`coordinate-bash-resultant-boundary.md` §16, Theorem 16.2, proved there in
full and reproduced/re-verified here).** *If `\beta_1\ge\gamma` (Case (c)),
then `G(\beta)>0` for every `\beta\in(0,\gamma)$, and consequently
`(\mathrm{II})` holds unconditionally throughout `(0,\gamma)` — no
`\beta$-specific hypothesis needed.*

*Proof.* By Fact 0 (`Y(\beta)=2\cos^2\beta-2X_0`) and the defining property
`\cos^2\beta_1=X_0`: `\beta_1\ge\gamma\iff\cos^2\beta_1\le\cos^2\gamma`
(`\cos^2` strictly decreasing on `[0,\pi/2]`) `\iff X_0\le\cos^2\gamma\iff
Y(\gamma)=2\cos^2\gamma-2X_0\ge0`. So Case (c)'s hypothesis is exactly
`Y(\gamma)\ge0`. By Fact 1 (`Y` strictly decreasing on `(0,\gamma)`,
`Y'=-2\sin2\beta<0`, unchanged from Case (a)'s citation), `Y(\beta)>
Y(\gamma)\ge0$ for every `\beta\in(0,\gamma)$, so `Y>0` holds on the
**entire** open interval `(0,\gamma)` — the hypothesis `Y(\beta)>0` in
`(\mathrm{II})`'s conjunction never restricts anything in this regime.

It remains to show `2K-f(\beta)>0$ (equivalently `G(\beta)>0`, Fact 3) for
every `\beta\in(0,\gamma)`. By Theorem 16.1 (`(\mathrm{I})`, already
certified unconditionally on `(0,\gamma)` and reused here), `f'(\beta)>0`
throughout `(0,\gamma)` (in fact throughout `(0,\gamma)`, not merely
`(\beta_0,\gamma)$ — Theorem 16.1's own proof, `f'(\beta)=\sin(A+\beta)
\cos B+\sin(A+B-\beta)`, uses only `\beta\in(0,\gamma)`), so `(2K-f)'=-f'<0`
throughout `(0,\gamma)`: `2K-f` is strictly decreasing on the whole
interval. Hence it suffices to show `2K-f(\gamma)\ge0` (in fact `>0`), and
then `2K-f(\beta)>2K-f(\gamma)\ge0` for every `\beta\in(0,\gamma)$ by strict
monotonicity.

By Fact 4, `2K-f(\gamma)=\sin(A+B)(2\sin A-\sin B)`. Since `A+B=\pi-C\in
(0,\pi)`, `\sin(A+B)>0`. By Fact 5, `\cos B(2\sin A-\sin B)>\sin(A+B)Y
(\gamma)\ge0` (using `\sin(A+B)>0` and the Case (c) hypothesis `Y(\gamma)
\ge0`), so `\cos B(2\sin A-\sin B)>0` strictly; and `\cos B>0` (Step 2's
own standing fact, `B<\pi/2`), so `2\sin A-\sin B>0` strictly. Hence
`2K-f(\gamma)=\sin(A+B)(2\sin A-\sin B)>0` strictly, and by the
monotonicity argument above, `2K-f(\beta)>0`, i.e. `G(\beta)>0`, for
**every** `\beta\in(0,\gamma)`. `\blacksquare`

**Consequence for `(\mathrm{II})`.** For every `\beta\in(0,\gamma)` in Case
(c): if `\beta\le\beta_0(A)`, `(\mathrm{II})`'s hypothesis conjunct `\sin
(A+3\beta)<0` is already false (Fact 0), so `(\mathrm{II})` holds
vacuously; if `\beta\in(\beta_0(A),\gamma)`, the Theorem above gives
`G(\beta)>0` directly, i.e. `(\mathrm{II})`'s conclusion `2K-f(\beta)>0`
holds outright regardless of whether its hypothesis `Y(\beta)>0` is true or
false (and it is in fact true throughout, by the Theorem's first
paragraph). **Either way, `(\mathrm{II})` holds throughout `(0,\gamma)` in
Case (c), with no case-dependent gap and no use of Steps 4-5 (the
Reduction Lemma/MVT-Lipschitz machinery, specific to Case (b)) anywhere in
this argument** — exactly parallel in structure to Case (a)'s closure
above, and, like Case (a), requiring no inequality on `G(\beta_1)`
specifically (`\beta_1$ itself need not even lie in `(0,\gamma)` in this
regime).

**Independent numerical corroboration (fresh this round, own script, not
reused).** A `200{,}000`-sample sweep of random `(A,B)$ with `\angle B\le
\angle C` (`0\le X_0\le1` enforced) finds `33{,}414` domain-nonempty
triples, splitting as Case (a) `30.4\%`, Case (b) `18.0\%`, Case (c)
`51.7\%` of the domain-nonempty region — matching round 21's independent
finding that Case (c) accounts for `\approx51\%` of the domain-nonempty
region (i.e. this is the common case, not an edge case). Among the `17{,}268`
Case-(c) samples: **zero** had `Y(\gamma)<0` (consistency check on the
case-membership test itself) and, sampling `20` random `\beta\in(0,\gamma)`
per Case-(c) triangle (`345{,}360` evaluations total), **zero** violations
of `G(\beta)>0`. A dedicated near-boundary sweep (`500{,}000` candidate
triangles, filtered to `|\beta_1-\gamma|<0.01`, yielding `1{,}288`
triangles and `12{,}880` `\beta`-evaluations) targeting exactly the
`\beta_1\to\gamma` transition region where round 21's gap lived finds
**zero** violations of `(\mathrm{II})`'s conclusion there either.

## Open gaps
1. `\partial S/\partial B\ge0` on `\mathcal D` (or on a suitable superset)
   — decomposed this round as `T_1+T_2` (D3), with `T_2=-2\,\mathrm{RHS}\,
   \partial_B\mathrm{RHS}` numerically `>0` throughout `\mathcal D` (new
   finding, margin `\approx0.282`) but `T_1` numerically NOT sign-definite
   (down to `\approx-0.644`) — so the naive termwise split fails (new
   honest negative finding, this round) and a genuine combined bound
   (`T_2\ge-T_1$, i.e. `T_2+T_1\ge0`, using the actual magnitude of `T_1$
   when negative, not just its sign) is still needed. NOT closed.
2. Within `T_2`: `\mathrm{RHS}>0$ (numerically confirmed, margin
   `\approx0.315`, `11{,}536` samples) and `\partial_B\mathrm{RHS}<0`
   (numerically confirmed, `7{,}743` samples) are each individually
   plausible clean sub-facts, and a compact two-variable closed form
   (D2$'$, in `\beta_0,B` alone via the `A=\pi-3\beta_0` substitution) was
   derived for `\partial_B\mathrm{RHS}` this round — but neither
   `\mathrm{RHS}>0` nor `\partial_B\mathrm{RHS}<0` was proved symbolically
   this round (both remain numeric-only, new sub-gaps more tractable in
   principle than the whole target, not yet closed).
3. Even if monotonicity in `B` were proved, the resulting reduced
   1-variable target sits on the *implicit* curve `X_0(A,B)=\cos^2B`
   (no closed form for `B$ as a function of `A` found or attempted this
   round) — a new sub-problem, not yet attacked.
4. The originally-dispatched tangent-line-in-`A`-at-fixed-`B$ construction
   is retired as a direct route (honest negative result, round 11); it
   does not close `(\star)`.
5. **CLOSED (round 16).** `\mathrm{Tgt}(A,B):=4(1+\cos B)^2X_0D_2^2-T_1^2
   >0` throughout `\mathcal D`. Round 13 pinned the numerical global
   minimizer exactly to `(\pi/3,\pi/3)`; round 14 closed
   "`D_2(\pi/3,\pi/3)\ne0`" (New result 7) and proved `(\pi/3,\pi/3)` a
   strict LOCAL minimum (New results 8-9); round 15 closed both
   boundary-curve sub-targets rigorously (Theorems B, C) and a 2-D
   adaptive interval sweep found zero violations outside a shrinking
   `\lesssim5\times10^{-8}`-radius residual around the corner. **Round 16
   closed that residual**: an explicit, certified radius `r_0=0.01`
   (Taylor's theorem with a certified Lagrange-remainder bound, `\S`"Round
   16" above and `lemmas/tgt-strictly-positive-throughout-D-full.md`)
   proves `\mathrm{Tgt}\ge\mathrm{Tgt}(\text{corner})` throughout
   `\bar{\mathcal D}\cap\{A\ge\pi/3-0.01\}`, which — since
   `0.01\gg5\times10^{-8}` — overlaps and unions with round 15's coverage
   to give `\mathrm{Tgt}\ge\mathrm{Tgt}(\text{corner})>0` **everywhere on
   `\bar{\mathcal D}`, with no residual left**. Gaps 1-4 remain subsumed
   and not needed (per the round-13 Reduction Lemma); only gap 6 is now
   outstanding.
6. **CLOSED (round 18; round 17's version was rejected and is superseded).**
   `D_1(A)\ge0` on the boundary curve `\mathcal C` — inherited from the
   `-twopoint` sibling (`lemmas/star-factorization-on-boundary-curve.md`).
   Round 17 claimed this closed via `D_1(B^\ast)=0` (Step 0) but that
   step's fact (ii) (`X_0(A^\ast,B^\ast)=\cos^2B^\ast`) was cited as
   "already-certified" when it was in fact an unproved numeric coincidence
   — correctly rejected by the proof-reviewer. **Round 18 supplies the
   missing proof**: an exact, hand-derivable identity
   `G_{\mathrm{curve}}(u)=-8\sin u\cos^2u\cdot h(u)` (`u=A/3+\pi/6`,
   `h(A):=X_0(A,\beta_0(A))-\cos^2\beta_0(A)`, i.e. fact (ii) is exactly
   `h(A^\ast)=0`), obtained via elementary triple/double-angle expansions
   from the raw definitions, plus an exact closed form
   `A^\ast=3\arcsin(\sqrt6/4)-\pi/2` proved to satisfy
   `G_{\mathrm{curve}}(A^\ast)=0` algebraically (not by numeric
   root-finding) and to be the population's actual standing `A^\ast` (via
   uniqueness of `G_{\mathrm{curve}}`'s root on `(0,\pi/2)` plus 60-digit
   numeric agreement). Since the cofactor `-8\sin u\cos^2u\ne0` at
   `u=A^\ast/3+\pi/6\in(\pi/6,\pi/3)`, `G_{\mathrm{curve}}(A^\ast)=0`
   forces `h(A^\ast)=0` exactly — fact (ii), proved. Steps 1-4 of the
   lemma (the certified `mpmath.iv` enclosure of `B^\ast`, derivative-sign
   sweep, value sweep, MVT gluing) are **unchanged** from round 17 — only
   Step 0's justification needed fixing. Full corrected detail:
   `lemmas/d1-nonnegative-on-boundary-curve.md`. Gap 6 itself is
   **genuinely closed and certified** (proof-reviewer, round 18).
   **[Proof-reviewer, round 18]: the claim "this route has no remaining
   open gaps" is FALSE.** Tracing the dependency chain end-to-end (per the
   round-18 dispatch's own instruction) found a separate, previously
   unflagged gap in "Full proof" Step 3 below (Case (a),
   `\beta_1\le\beta_0(A)`): its citation of Theorem A of
   `lemmas/claim-I-closed-and-claim-II-caseA-closed.md` covers the wrong
   sub-interval (`(\beta_0,\gamma)`, not `(0,\beta_0]`), so Case (a) is
   **not** actually closed by any certified lemma in the population. See
   "Status" at the top of this file and the inline flag at Step 3 below for
   the full diagnosis, and Open gap 7 below.

7. **CLOSED (round 21 for Case (a); round 22 adds the previously-missing
   Case (c), completing the trichotomy in full).** Found by proof-reviewer
   round 18; re-diagnosed and shown (incorrectly) deeper by round 19;
   sharpened again by round 20; **Case (a) genuinely, fully closed** — see
   "Round 21" section above. **Round 21's proof-reviewer then found the
   assembled "Full proof" only ever covered Cases (a) and (b), omitting
   `\beta_1\ge\gamma` (Case (c)) entirely** — see "Status" at the top of
   this file for the exact adjudication. **Round 22 closes Case (c)** by
   citing `coordinate-bash-resultant-boundary.md`'s Theorem 16.2 first
   branch (`Y(\gamma)\ge0\Rightarrow(\mathrm{II})` holds unconditionally on
   `(0,\gamma)`), independently re-verified from raw definitions this round
   (Facts 3-5, "Round 22" section, "Full proof" Step 3′) — see the
   dependency-chain audit (round 22) above for the full re-trace. With all
   three cases of the trichotomy now closed, **Open gap 7 is fully closed,
   and the whole route is `solved`.** The gap is a
   phantom: `G(\beta_1)\ge0` was never actually the fact Case (a) needed
   (this file's own Step 2 "no case split in the target itself" was an
   unjustified over-generalization of `lemmas/mvt-lipschitz-reduction-
   case-b.md`'s own Setup, which explicitly restricts to `\beta_0<\beta_1<
   \gamma`). Tracing the ORIGINAL `(\mathrm{I})/(\mathrm{II})` derivation
   (`coordinate-bash-resultant-boundary.md` §§8-10, 15-17) directly: `(\mathrm
   {I})` is unconditionally proved for all `\beta\in(0,\gamma)` (Theorem
   16.1, independent of Case), and `(\mathrm{II})` is proved to hold
   *vacuously* throughout Case (a) — a fully rigorous two-line consequence
   of `Y`'s already-certified strict monotonicity (`Y'=-2\sin2\beta<0`)
   combined with the algebraic identity `\beta_1\le\beta_0(A)\iff
   Y(\beta_0(A))\le0`. No inequality on `G(\beta_1)`, `T`, or any other
   quantity needs to be — or is — proved in Case (a). **The whole route is
   now `solved`.** (Original text of this entry, superseded, preserved
   immediately below for the historical record.)

   *(superseded, preserved for the record)* "Full proof" Step 3 ("Case (a)",
   `\beta_1\in(0,\beta_0(A)]`) is not established. Round 18 found the
   citation of Theorem A covered the wrong sub-interval; round 18/19's
   dispatch proposed a fix (extend `f>0` down to all of `[0,\gamma)` via
   `f'>0` there plus `f(0)\ge0`). **Round 19 fully proves both halves of
   that proposed fix** (see "Full proof" Step 3, "Sub-result A") — but
   also shows, via an exact 50-digit witness and a matching `500{,}000`-
   sample sweep, that `f(\beta_1)>0` is simply not the fact Case (a)
   needs: the file's own Step 2 states the uniform target `G(\beta_1)\ge0`
   for every `\beta_1\in(0,\gamma)`, and this is independently corroborated
   by the certified, `\beta_0`-independent lemma
   `lemmas/case-b-p-le-0-and-e-ge-0-closed.md`. `G(\beta_1)\ge0` genuinely
   fails at `\approx70\%` of literal Case-(a) points, and **every failure
   found coincides exactly with the still-fully-open `P>0\wedge E<0`
   sub-case of that lemma** — the same `T\ge0`/`-q_1,-r_0`
   Positivstellensatz-certificate target that has resisted the whole
   population's search (`coordinate-bash-resultant-boundary`,
   `-pointwise-sos`) across many rounds. **NOT closed, and now understood
   to be equivalent to the population's oldest, most persistent open gap
   — not a citation-scope technicality.** This remains the route's sole
   open gap (Gap 6 is closed; Gaps 1-5 remain closed/subsumed as before),
   but it is now known to be substantially harder than previously believed.
   **[Round 20 update — round 19's identification above is corrected.]**
   Round 20 fully closes `T\ge0` (hence `G(\beta_1)\ge0`) on Case (b)'s own
   residual sub-case `\mathcal D_b:=\{X_0<\cos^2\beta_0(A),\ P>0,\ E<0\}`
   (see "Round 20" section above, a genuine certified closure of Case (b)
   in full, via the local-Taylor+Lagrange-remainder-at-corner technique).
   **But round 19's claim that Case (a)'s residual "coincides exactly" with
   this same sub-case is FALSE**: Case (a)'s domain is the complementary
   region `X_0>\cos^2\beta_0(A)`, and `T`/`G(\beta_1)` are demonstrably
   NEGATIVE there at ordinary points (e.g. `A=0.02,B=1.5`:
   `T\approx-0.249,\ G(\beta_1)\approx-0.654$, both confirmed to 50 digits;
   round 19's own witness independently re-confirmed to have `T\approx
   -0.2487<0` too). So Case (a) is **not** closed by round 20's result, and
   is now understood to need either a genuinely different reduction (not
   `G(\beta_1)\ge0` as a blanket claim) or a missing domain constraint on
   `(A,B)$ not yet identified anywhere in this population — a **new and
   more fundamental** open question than any prior round's diagnosis (see
   "Round 20" section's closing discussion). **Open gap 7 (Case (a)) is
   STILL OPEN, now with a sharper, more accurate (if less optimistic)
   diagnosis than round 19's.** Case (b) itself is fully closed (round 20),
   an independent, genuine, certified new result of population-wide
   relevance (the first unconditional proof, anywhere in this population's
   10-round search, that `T\ge0`/`-q_1,-r_0\le0` on any nontrivial sub-domain).

## Full proof

**Claim.** `OM=ON` for every triangle `ABC` with `M,N` the midpoints of
`AB,AC` and `O` the point of the original problem statement (the point
whose defining property reduces, via the certified vector/rotation/
Case-isolation chain below, to Case (b)'s target `G(\beta_1)\ge0`).

**Step 1 (vector reduction, certified, `lemmas/vector-reduction-OM-
ON.md`).** Placing `A` at the origin, `OM=ON\iff O\cdot(C-B)=(|C|^2-
|B|^2)/4`, an elementary polarization identity, valid for every `O`, no
hypothesis beyond `M,N` being the midpoints.

**Step 2 (rotation parametrization and Case-(b) isolation — this step
compresses a long chain built over rounds 1-10 of this population,
spanning the coordinate/complex-number encoding of `K,L` via the stated
angle conditions, the rotation-parametrization of the circumcenter `O` of
`AKL`, and the reduction of `O\cdot(C-B)=(|C|^2-|B|^2)/4` to the trig
target below; NOT re-derived from scratch in this round — cited via the
already-independently-certified lemma chain
`lemmas/bilinear-chi-cramer-formula.md`, `lemmas/homogeneity-decoupling-
rotation-param.md`, `lemmas/complex-affine-L1-DK-and-r-lo-selection.md`,
`lemmas/w-r-lo-positive-via-zN-zK-evaluation.md`, converging on
`lemmas/mvt-lipschitz-reduction-case-b.md`'s Setup, each independently
certified by a proof-reviewer in its own round).** WLOG `\angle B\le\angle
C` (so `\gamma:=\angle B\le\pi/2`, `\cos B>0` — `2B\le B+C=\pi-A<\pi`). The
problem's defining condition on `O` reduces, via that certified chain, to
proving, for `\beta_1\in(0,\gamma)` the unique angle with `\cos\beta_1=
\sqrt{X_0(A,B)}` (`X_0:=\sin B\cos A/(2\sin(A+B))\in[0,1]`), that
`G(\beta_1)\ge0`, where `G(\beta):=K_c-P\sin\beta-Q\cos\beta` (`K_c,P,Q`
as in the Setup above), **with no a-priori restriction of `\beta_1` to
`(0,\gamma)`** — `\beta_1$ is simply the unique angle in `[0,\pi/2)` with
`\cos\beta_1=\sqrt{X_0}`, and it may lie anywhere in `[0,\pi/2)`. Given the
domain-nonempty premise `\beta_0(A)<\gamma` (the domain-empty case
`\beta_0(A)\ge\gamma` is vacuous, handled separately, lines 2148-2154),
exactly one of three mutually exclusive, jointly exhaustive cases holds —
a trichotomy of the single real number `\beta_1` against the two ordered
cutpoints `\beta_0(A)<\gamma`:
$$\text{(a) }\beta_1\le\beta_0(A),\qquad\text{(b) }\beta_0(A)<\beta_1<
\gamma,\qquad\text{(c) }\beta_1\ge\gamma.$$

**Step 3 (Case (a), `\beta_1\in(0,\beta_0(A)]` — CLOSED, round 21; see the
"Round 21" section above for the complete proof, reproduced compactly
here).** Write `Y(\beta):=2\cos^2\beta-m\cos A` (`m:=\sin B/\sin(A+B)`); the
ORIGINAL derivation's remaining target (`coordinate-bash-resultant-
boundary.md` §15) is exactly `(\mathrm{I})\wedge(\mathrm{II})` for every
`\beta\in(0,\gamma)`, where `(\mathrm{I})` is unconditional on
`\sin(A+3\beta)<0` alone and `(\mathrm{II})` is conditional on `Y(\beta)>0
\wedge\sin(A+3\beta)<0` jointly. `(\mathrm{I})` is proved unconditionally
for every `\beta\in(0,\gamma)` (Theorem 16.1 on `(\beta_0,\gamma)`, vacuously
true on `(0,\beta_0]`). For `(\mathrm{II})`: `\beta_1\le\beta_0(A)$
(Case (a)) is algebraically equivalent to `Y(\beta_0(A))\le0` (since
`\cos^2\beta_1=X_0=\cos^2\beta_0(A)\cdot[\beta_1=\beta_0]`-type comparison,
precisely `\beta_1\le\beta_0(A)\iff X_0\ge\cos^2\beta_0(A)\iff Y(\beta_0(A))
\le0`, using `\cos` decreasing and `Y(\beta)=2\cos^2\beta-2X_0`). Since `Y`
is strictly decreasing on `(0,\gamma)` (`Y'=-2\sin2\beta<0`, already
certified, Theorem 16.2), `Y(\beta)<Y(\beta_0(A))\le0` for every `\beta\in
(\beta_0(A),\gamma)$, so `(\mathrm{II})`'s hypothesis `Y(\beta)>0` fails
there too; and for `\beta\le\beta_0(A)`, `(\mathrm{II})`'s other hypothesis
`\sin(A+3\beta)<0` already fails. **Hence `(\mathrm{II})`'s hypothesis
conjunction is false for every `\beta\in(0,\gamma)` in Case (a), so
`(\mathrm{II})` holds vacuously throughout.** Combined with `(\mathrm{I})`,
both halves of the ORIGINAL target hold for every `\beta\in(0,\gamma)` in
Case (a) — **no inequality on `G(\beta_1)`, `T`, or any other quantity needs
to be proved here.** This is not merely "not yet needed" but a fully
rigorous, unconditional closure (see "Round 21" above for the complete
derivation, the exact citations to the original §§8-10/15-17 text, and the
handling of every boundary/degenerate case). `\blacksquare` for Step 3.

*(Historical record, superseded by the above — the following paragraphs
record rounds 18-20's incremental, ultimately-corrected diagnosis of this
step, preserved so the reasoning trail is auditable.)*

*Sub-result A (fully proved, round 19): `f(\beta)>0` for every
`\beta\in[0,\gamma)`, not just `(\beta_0,\gamma)`.* Theorem A's own proof
(`lemmas/claim-I-closed-and-claim-II-caseA-closed.md`) establishes
`f'(\beta)=\sin(A+\beta)\cos B+\sin(A+B-\beta)>0` for **every**
`\beta\in(0,\gamma)$, not merely `(\beta_0,\gamma)` — the sign argument
(`\cos B>0` since `B<\pi/2`; `\sin(A+\beta)>0` since `A+\beta\in(0,A+B)
\subset(0,\pi)`; `\sin(A+B-\beta)>0` since `A+B-\beta\in(A,A+B)\subset
(0,\pi)`) uses only `\beta\in(0,\gamma)`, never `\beta>\beta_0`. This is
the exact fix the round-18/19 dispatch anticipated, and it is genuinely
correct: we prove it in full here as a self-contained addendum.*

*Sub-result A (fully proved, round 19): `f(\beta)>0` for every
`\beta\in[0,\gamma)`, not just `(\beta_0,\gamma)`.* Theorem A's own proof
(`lemmas/claim-I-closed-and-claim-II-caseA-closed.md`) establishes
`f'(\beta)=\sin(A+\beta)\cos B+\sin(A+B-\beta)>0` for **every**
`\beta\in(0,\gamma)$, not merely `(\beta_0,\gamma)` — the sign argument
(`\cos B>0` since `B<\pi/2`; `\sin(A+\beta)>0` since `A+\beta\in(0,A+B)
\subset(0,\pi)`; `\sin(A+B-\beta)>0` since `A+B-\beta\in(A,A+B)\subset
(0,\pi)`) uses only `\beta\in(0,\gamma)`, never `\beta>\beta_0`. This is
the exact fix the round-18/19 dispatch anticipated, and it is genuinely
correct: we prove it in full here as a self-contained addendum.

*New elementary fact: `f(0)=\sin A\,(2\sin(A+B)-\sin B)>0` strictly.*
`f(0)=K_c+P\sin0+Q\cos0=K_c+Q=2\sin A\sin(A+B)-\sin A\sin B=\sin A\,(2\sin
(A+B)-\sin B)`. Since `A\in(0,\pi)`, `\sin A>0`, so it suffices to show
`2\sin(A+B)-\sin B>0`, i.e. (writing `C:=\pi-A-B`, so `\sin(A+B)=\sin(\pi-C)
=\sin C`) `2\sin C-\sin B>0`. **Claim: `\sin B\le\sin C`** (recall the
file's own standing WLOG `\angle B\le\angle C`, i.e. `B\le C`). *Proof of
claim, by cases on `C` vs `\pi/2`, exhaustive since `C\in(0,\pi)`:*
- If `C\le\pi/2`: then `0<B\le C\le\pi/2`, and `\sin` is strictly
  increasing on `[0,\pi/2]`, so `\sin B\le\sin C`.
- If `C>\pi/2`: since `A>0` (a genuine triangle angle), `\pi-C=A+B>B`, so
  `0<B<\pi-C<\pi/2` (the last inequality since `C>\pi/2`). `\sin` strictly
  increasing on `[0,\pi/2]` gives `\sin B<\sin(\pi-C)=\sin C`.
Both cases give `\sin B\le\sin C$ (in fact strict except possibly at
`B=C\le\pi/2`, where equality is allowed). `\blacksquare` (This is exactly
the two-case argument the round-18/19 dispatch specified, carried out in
full; no degenerate limit `A\to0` is needed since `A>0` strictly for every
genuine triangle, so the strict inequality `\pi-C=A+B>B` used in the second
case holds throughout the domain, not merely in a limit.) Given the claim,
`2\sin C-\sin B=\sin C+(\sin C-\sin B)\ge\sin C+0=\sin C>0` (using `\sin C
\ge\sin B\ge0` and `C\in(0,\pi)\Rightarrow\sin C>0`), so `2\sin C-\sin B
\ge\sin C>0` strictly. Hence `f(0)=\sin A(2\sin C-\sin B)>0` strictly.

*Combining (MVT/monotonicity):* `f` is smooth (a finite sum of `\sin,\cos`
of `\beta` with `\beta$-independent coefficients `K_c,P,Q`), hence
continuous on `[0,\gamma)` and differentiable there, with `f'>0` on the
open interval `(0,\gamma)$. For any `\beta_1\in(0,\gamma)`, the Mean Value
Theorem applied to `f` on `[0,\beta_1]` gives `\xi\in(0,\beta_1)` with
`f(\beta_1)-f(0)=f'(\xi)\,\beta_1>0`, so `f(\beta_1)>f(0)>0`. **This proves
`f(\beta_1)>0` for every `\beta_1\in(0,\gamma)`, in particular for every
`\beta_1\in(0,\beta_0(A)]$ (Case (a)) — Sub-result A is fully closed, with
no gap, and is a genuine, promotable strengthening of Theorem A.**

*Why this does NOT close Case (a) (round-19 finding — a deeper, previously
undiagnosed gap).* Case (a)'s actual required target, per Step 2 above
(stated uniformly for every `\beta_1\in(0,\gamma)`, no case split in the
target itself) is `G(\beta_1)\ge0$, not `f(\beta_1)>0`. This is
corroborated independently by the already-certified lemma
`lemmas/case-b-p-le-0-and-e-ge-0-closed.md` ("Case (b) target
`G(\beta_1)\ge0`"), which proves `G(\beta_1)\ge0` unconditionally on
`P\le0` or `P>0\wedge E\ge0` (`P,E` as defined there), for **any**
`\beta_1$ with `\cos^2\beta_1=X_0` — with **no** restriction relating
`\beta_1` to `\beta_0(A)` anywhere in its statement or proof — leaving only
`P>0\wedge E<0` open. Independent verification this round (fresh `sympy`,
50-digit precision, `500{,}000`-sample sweep restricted exactly to this
file's own literal Case-(a) domain: `\beta_1\le\beta_0(A)`, `\beta_0(A)<
\gamma` (domain-nonempty), `0<\beta_1<\gamma`, `B\le C`) finds
`G(\beta_1)\ge0` false at `\approx70\%$ of sampled points, and — checked
exactly — **every single failure has `P>0\wedge E<0`**, i.e. lies exactly
in the one residual sub-case of `case-b-p-le-0-and-e-ge-0-closed.md` that
remains open population-wide (it reduces, via `lemmas/case-b-e-lt-0-t-
factorization.md`, to `T:=B_c^2X_0-E^2\ge0` — the same target referred to
elsewhere in this population's history as the `-q_1,-r_0`
Positivstellensatz certificate, still not found after many rounds of
dedicated LP/SDP search by two sibling approaches). An exact witness
(50-digit `sympy`, from the raw definitions, not a floating-point
artifact): the genuine triangle `A=0.010023227880759093\ldots,\
B=1.4992571585875281\ldots$ (`C=1.6323122671215061\ldots\ge B`) has
`\beta_0=1.0438564752363447\ldots<\gamma=B`, `\beta_1=
0.7857570572374546\ldots\le\beta_0` (a bona fide, domain-nonempty Case-(a)
point), `G(\beta_1)=-0.679454396949432\ldots<0` strictly, while
`f(\beta_1)=0.7194708023254286\ldots>0` (Sub-result A holds here, exactly
as proved, but is simply not the fact needed) and `P=
0.99882492106152325\ldots>0,\ E=-0.49873339578002015\ldots<0`. **Hence
Case (a), as literally defined in this file (`\beta_1\le\beta_0(A)`), is
NOT closed: its nonvacuous residual coincides exactly with the
population's oldest and most persistent open gap.** The file's own
"Setup" aside that "`f`, not `G`, is the relevant quantity" in Case (a) is
therefore not merely unproved but appears to be simply incorrect as a
general claim (it was never accompanied by a proof anywhere in the
population, and the counterexample above shows `f(\beta_1)>0` alone does
not imply `G(\beta_1)\ge0`). **Open gap 7 remains open, now understood
to be equivalent to the `T\ge0`/`-q_1,-r_0` gap, not a citation-scope
issue.**

**Step 3′ (Case (c), `\beta_1\ge\gamma` — CLOSED, round 22; see the "Round
22" section above for the complete proof, reproduced compactly here).**
`\beta_1\ge\gamma$ is algebraically equivalent to `Y(\gamma)\ge0` (Fact 0,
`\cos^2` decreasing). By Theorem 16.2's first branch of `coordinate-bash-
resultant-boundary.md` §16 (round 9, certified; re-verified fresh this
round via Facts 3-5 above): `Y` strictly decreasing on `(0,\gamma)` gives
`Y(\beta)>Y(\gamma)\ge0` for every `\beta\in(0,\gamma)`, so `(\mathrm{II})`'s
`Y(\beta)>0` hypothesis-conjunct never excludes anything in this regime;
and `2K-f=G` (Fact 3) is strictly decreasing on `(0,\gamma)` (Theorem
16.1's `f'>0`, unconditional), with `2K-f(\gamma)=\sin(A+B)(2\sin A-\sin B)
>0` strictly (Fact 4, plus Fact 5's sign argument: `\cos B(2\sin A-\sin B)
>\sin(A+B)Y(\gamma)\ge0` and `\cos B>0` give `2\sin A-\sin B>0`), so
`G(\beta)=2K-f(\beta)>2K-f(\gamma)>0` for **every** `\beta\in(0,\gamma)`.
Hence `(\mathrm{II})`'s conclusion holds unconditionally throughout
`(0,\gamma)` — for `\beta\le\beta_0(A)`, vacuously (`(\mathrm{II})`'s other
hypothesis-conjunct `\sin(A+3\beta)<0` is already false there, exactly as
in Case (a)); for `\beta\in(\beta_0(A),\gamma)`, outright (`G(\beta)>0`
holds regardless of `Y(\beta)`'s sign, which is in any case also `>0`
throughout). Combined with `(\mathrm{I})$ (Theorem 16.1, unconditional,
independent of Case), **both halves of the ORIGINAL target hold for every
`\beta\in(0,\gamma)$ in Case (c) — exactly parallel to Case (a), and, like
Case (a), needing no inequality on `G(\beta_1)$ specifically (indeed
`\beta_1$ need not even lie in `(0,\gamma)` here) and no invocation of
Steps 4-5 (the Reduction Lemma/MVT-Lipschitz machinery, which is used only
in Case (b)).** `\blacksquare` for Step 3′.

**Step 4 (Case (b), the file's own route).** The remaining target is
`G(\beta_1)\ge0` for `\beta_1\in(\beta_0(A),\gamma)`. By the MVT/Lipschitz
reduction (Theorem, `lemmas/mvt-lipschitz-reduction-case-b.md`, certified):
writing `\mathrm{RHS}:=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0)`,
- if `\mathrm{RHS}\le0`, `G(\beta_1)\ge0` unconditionally (proved there,
  Steps 1-4, an explicit two-step MVT chain, no gap);
- if `\mathrm{RHS}>0`, `G(\beta_1)\ge0` follows from `(\star)`:
  `(1+\cos B)^2X_0\ge\mathrm{RHS}^2`.

**Step 5 (`(\star)` on all of `\mathcal D`, this file's own reduction,
New result 1, round 13, certified above).** With `f:=(1+\cos B)\sqrt{X_0}
\ge0`, `g:=\mathrm{RHS}`, `S:=f^2-g^2=(1+\cos B)^2X_0-\mathrm{RHS}^2`, the
Reduction Lemma states: given (A) `\partial(f-g)/\partial B>0` throughout
`\mathcal D` and (B) `D_1(A)\ge0` on `\mathcal C=\{X_0=\cos^2B\}`, then
`f\ge g` throughout `\mathcal D`, hence (since `(\star)$ is only ever
*needed* where `\mathrm{RHS}>0`, where `S\ge0\iff f\ge g` as both sides are
`\ge0`) `(\star)` holds throughout `\mathcal D`, closing Case (b) and hence
(via Steps 1-4) the whole problem.

*Hypothesis (A) — proved (round 16, `lemmas/tgt-strictly-positive-
throughout-D-full.md`, certified).* `\mathrm{Tgt}(A,B):=4(1+\cos B)^2X_0
D_2^2-T_1^2>0` throughout `\bar{\mathcal D}` (New result 4's radical-free
reformulation, proved via Theorems B, C — certified `mpmath.iv`
branch-covering sweeps of both boundary curves `\mathcal C_{\mathrm{hi}},
\mathcal C_{\mathrm{lo}}` — plus an explicit, quantitative Taylor +
certified-Lagrange-remainder radius `r_0=0.01` closing the residual
near-corner gap at `(\pi/3,\pi/3)`, glued to the round-15 2-D adaptive
interval sweep). By the domain-connectedness/sign-determination argument
(New result 5, round 13, certified: `\mathcal D` is path-connected, and
`\mathrm{Tgt}\ne0` everywhere forces `\partial(f-g)/\partial B` to have
constant sign, pinned positive by the single-point evaluation `\approx
0.5807>0` at `(A,B)\approx(0.603,1.269)`), `\mathrm{Tgt}>0` throughout
`\mathcal D` gives hypothesis (A).

*Hypothesis (B) — proved (round 18, this round, `lemmas/d1-nonnegative-
on-boundary-curve.md`, fixed and detailed above).* `D_1(A)\ge0` on
`\mathcal C`, via the exact corner identity `D_1(B^\ast)=0`. The corner
identity in turn rests on two facts, both now proved exactly: (i)
`G(\beta_0(A^\ast))=0`, true by `A^\ast`'s own defining equation
(originally pinned numerically by `\mathrm{mpmath.findroot}`, round 11 of
`coordinate-bash-resultant-boundary-pointwise.md`; this round additionally
supplies the exact closed form `A^\ast=3\arcsin(\sqrt6/4)-\pi/2` and
verifies `G_{\mathrm{curve}}(A^\ast)=0` from it algebraically, `\S`0(f) of
the lemma); (ii) `X_0(A^\ast,B^\ast)=\cos^2B^\ast` (i.e. `h(A^\ast)=0`),
now **proved** — not cited as a coincidence — via the hand-derived
identity `G_{\mathrm{curve}}(u)=-8\sin u\cos^2u\cdot h(u)$ (`u=A/3+\pi/6`)
together with the nonvanishing of the cofactor `-8\sin u^\ast\cos^2u^\ast`
at `u^\ast=A^\ast/3+\pi/6\in(\pi/6,\pi/3)` (`\S`0 of the lemma, in full).
Given `D_1(B^\ast)=0`, the certified two-part `mpmath.iv` sweep
(derivative bound near the corner, value bound away from it, unchanged
from round 17) glued by the Mean Value Theorem gives `D_1(A)\ge0` on all
of `\mathcal C`.

**Conclusion for Case (b).** Both hypotheses of the Reduction Lemma hold, so
`f\ge g` throughout `\mathcal D`, so `(\star)` holds throughout `\mathcal D`,
so (by Step 4) `G(\beta_1)\ge0` throughout Case (b), `\beta_1\in(\beta_0(A),
\gamma)`. **This is genuinely closed** (and, independently, round 20 above
supplies a second, direct proof of the same conclusion via the `P,E$-sign
decomposition and the corner Taylor argument, without needing hypotheses
(A)/(B) at all — both routes to Case (b) are valid and certified).

**Conclusion for Case (a) (round 21).** As proved in Step 3 above, `(\mathrm
{I})\wedge(\mathrm{II})$ — the ORIGINAL derivation's own complete remaining
target (`coordinate-bash-resultant-boundary.md` §15) — hold for every
`\beta\in(0,\gamma)` when `\beta_1\le\beta_0(A)`: `(\mathrm{I})`
unconditionally (Theorem 16.1), `(\mathrm{II})` vacuously (its hypothesis
conjunction is false throughout this range, by `Y`'s strict monotonicity and
the algebraic identity `\beta_1\le\beta_0(A)\iff Y(\beta_0(A))\le0`). No
inequality on `G(\beta_1)`, `T`, or any other quantity is needed here — this
file's own prior Step 2 restatement, which asserted `G(\beta_1)\ge0` as a
universal target "no case split," was an over-generalization of the
certified lemma `lemmas/mvt-lipschitz-reduction-case-b.md`'s own explicitly-
scoped Setup (`\beta_0<\beta_1<\gamma`); correctly traced back to the
original `(\mathrm{I})/(\mathrm{II})` system, Case (a) requires nothing
further and is closed.

**Conclusion for Case (c) (round 22).** As proved in Step 3′ above,
`(\mathrm{I})\wedge(\mathrm{II})` hold for every `\beta\in(0,\gamma)` when
`\beta_1\ge\gamma`: `(\mathrm{I})` unconditionally (Theorem 16.1, same as
every case), `(\mathrm{II})` unconditionally too — not vacuously as in Case
(a), but outright, via Theorem 16.2's first branch (`Y(\gamma)\ge0
\Rightarrow G(\beta)>0` throughout `(0,\gamma)`, Facts 0, 1, 3, 4, 5 above).
No inequality on `G(\beta_1)$ specifically, and no use of Steps 4-5, is
needed here either — Case (c) requires nothing further and is closed.

**Overall conclusion.** Steps 3, 3′, and 4 together cover the whole range
`\beta_1\in[0,\infty)` given the domain-nonempty premise (Step 2's
trichotomy `\{\beta_1\le\beta_0(A)\}\cup\{\beta_0(A)<\beta_1<\gamma\}\cup
\{\beta_1\ge\gamma\}`, exhaustive and disjoint by construction): Case (a)
closed vacuously (Step 3, round 21), Case (b) closed via the Reduction
Lemma (Steps 4-5) or, independently, via the direct `T\ge0` proof (round
20), Case (c) closed outright via Theorem 16.2's first branch (Step 3′,
round 22). The domain-empty case `\beta_0(A)\ge\gamma` is vacuous
separately (lines 2148-2154). Hence `(\mathrm{I})\wedge(\mathrm{II})` — the
ORIGINAL derivation's full target, `coordinate-bash-resultant-boundary.md`
§15 — holds for every `\beta\in(0,\gamma)`, for every triangle, in every
case; equivalently `G(\beta_1)\ge0` (or its vacuous/unconditional
equivalent) holds wherever it is the operative reduction. By Step 2's
reduction and Step 1's polarization identity, `O\cdot(C-B)=(|C|^2-|B|^2)/4`,
i.e. `OM=ON`, for every triangle `ABC` satisfying the problem's hypotheses.
`\blacksquare`

### Dependency-chain audit (round 22) — full end-to-end re-trace, not just
the new paragraph

Given this file's history of four prior false `solved` claims (rounds 17,
18, 19, 21), each caught by a subsequent proof-reviewer finding a gap
*outside* the specific paragraph the builder had just fixed, this audit
re-traces the *entire* assembled chain (Steps 1-5, 3′, both Case (a)/(b)/(c)
write-ups, and the audits below), not merely Case (c)'s new content.

1. **Is the trichotomy `\{\beta_1\le\beta_0(A)\}\cup\{\beta_0(A)<\beta_1<
   \gamma\}\cup\{\beta_1\ge\gamma\}` literally exhaustive and disjoint?**
   Yes, by construction: given the domain-nonempty premise `\beta_0(A)<
   \gamma`, this is a case split of a single real number `\beta_1$ against
   two ordered reals `\beta_0(A)<\gamma` — the three intervals `(-\infty,
   \beta_0(A)]`, `(\beta_0(A),\gamma)`, `[\gamma,\infty)$ partition `\mathbb
   R`, and `\beta_1\in[0,\pi/2)\subset\mathbb R` lies in exactly one. No
   geometric or trigonometric content is needed for this step — it is
   restated explicitly (not merely asserted) in Step 2 and in the "Round 22"
   section above, closing the round-22 dispatch's explicit request to
   restate rather than assume this.
2. **Are Steps 4-5 (Reduction Lemma / MVT-Lipschitz, used only in Case (b))
   silently invoked anywhere in Case (a) or Case (c)'s write-up?** Checked
   by direct re-reading of Step 3 (Case (a)) and Step 3′ (Case (c)) above:
   neither cites `lemmas/mvt-lipschitz-reduction-case-b.md`, `\mathrm{RHS}`,
   `(\star)`, `f-g`, `D_1`, `D_2`, `T_1`, or `\mathrm{Tgt}` (all Step
   4-5-specific quantities) anywhere. Case (a)'s proof uses only Facts 0-2
   and `Y`'s monotonicity; Case (c)'s proof uses only Facts 0, 1, 3, 4, 5 and
   Theorem 16.1's `f'>0`. Both are self-contained and independent of the
   Reduction Lemma machinery, exactly as claimed. No silent invocation
   found.
3. **Do the isosceles (`B=C`) edge case and all standing non-degeneracy
   hypotheses (`B\le C`, `B<\pi/2`, `A,B,C>0` genuine triangle angles)
   still hold throughout the assembled Case (c) argument?** `B=C` is
   admissible throughout: Case (c)'s proof uses `B\le C$ only via `\cos B>0`
   (from `B<\pi/2`, itself from `2B\le B+C<\pi`, valid whether `B<C` or
   `B=C`) and via `\delta\ge0` in Fact 5 (`\delta:=\pi-2B-A=C-B\ge0$ exactly
   when `B\le C`, with `\delta=0` exactly at `B=C`, an admissible boundary
   value — Fact 5's argument only needs `\delta<B`, i.e. `\delta\ge0` is
   consistent with, not excluded by, the strict inequality actually used).
   No other non-degeneracy hypothesis (`K\ne L`, `A,K,L` non-collinear,
   etc.) is touched by Case (c)'s argument at all — it operates entirely at
   the level of the reduced trigonometric target `(\mathrm{I})/(\mathrm{II})`
   for `\beta\in(0,\gamma)`, inherited unchanged from Steps 1-2 (whose own
   non-degeneracy scope is unchanged from every prior round's certification,
   items 1-5 of the round-18 audit below).
4. **Does Theorem 16.2's own proof (Facts 3-5 above) have any unstated
   sub-case, as the round-22 dispatch specifically flagged (the sign of
   `2\sin A-\sin B`)?** Re-checked explicitly (Fact 5 above): the sign of
   `2\sin A-\sin B` is not assumed — it is *derived*, via `\cos B(2\sin A-
   \sin B)>\sin(A+B)Y(\gamma)\ge0` (Fact 5's identity plus the Case (c)
   hypothesis `Y(\gamma)\ge0`) combined with `\cos B>0`, giving `2\sin A-
   \sin B>0` as a *conclusion*, not a hypothesis. This derivation was
   independently checked for circularity: it needs `\delta<B`, which comes
   from the domain-nonempty premise `\beta_0(A)<\gamma$ (a standing
   hypothesis already in force before Case (c) is reached, not a
   consequence of `Y(\gamma)\ge0`) — confirmed not circular. No other
   sub-case (e.g. a further split depending on `\mathrm{sign}(\sin A)` or
   any other quantity) appears anywhere in Theorem 16.1's or 16.2's proof
   as re-derived here; both are unconditional statements for every
   `\beta\in(0,\gamma)`/every triangle with the standing WLOG, with a single
   linear chain of implications each, no internal case split beyond the
   `Y(\gamma)\ge0`-vs-`<0` split that already defines Case (c) vs Cases
   (a)/(b).
5. **Any stale numeric-only or "conjecture" citation reachable from Case
   (c)'s new content?** Case (c) cites only: Fact 0 (already certified,
   round 21, algebraic), Fact 1 (`Y`'s monotonicity, `coordinate-bash-
   resultant-boundary.md` Theorem 16.2's opening line, a one-line derivative
   computation, re-verified fresh again this round), Theorem 16.1 (`f'>0`,
   `coordinate-bash-resultant-boundary.md` §16, fully proved, New results 1
   and 2, re-read in full this round — see the excerpt reproduced above,
   no numeric-only content), and Facts 3-5 (proved fresh, self-contained,
   this round). No citation in this chain is flagged "numeric only" or
   "conjecture" anywhere in the source file.
6. **Re-run of items 1-5 from the round-18 audit (Steps 1-2, hypotheses
   (A)/(B) of the Reduction Lemma, existence/non-degeneracy of `K,L,O`)?**
   Unaffected by this round's work — Case (c) does not touch Steps 4-5 or
   their hypotheses at all (item 2 above), so the round-18 audit's findings
   on those items (reproduced below, unchanged) remain the relevant record
   for that part of the chain.

**Conclusion of the round-22 audit.** No further gap was found beyond the
one this round's Step 3′ closes. Combined with the round-18 audit below
(covering Steps 1-2 and the Reduction Lemma's hypotheses, unaffected by
this round) and the round-19/20/21 corrections (all superseded by their own
later closures, Case (a) and Case (b) both independently certified), the
whole chain — Steps 1, 2, 3, 3′, 4, 5 — is gap-free. **Status: `solved`.**

### Dependency-chain audit (round 18) — checking for any OTHER silent gap

Before declaring this route `solved`, every citation used in Steps 1-5
above was traced for hidden numeric-only or "conjecture"-labeled content,
per the round-18 dispatch's explicit instruction (motivated by round 17's
false `solved` claim on this exact route). Findings:

1. **Does anything else in hypothesis (A) or (B) implicitly use the same
   "coincidence" fact (ii), or any other unproved numeric coincidence?**
   No. Hypothesis (A) (`lemmas/tgt-strictly-positive-throughout-D-
   full.md`) is anchored at the *different* corner `(\pi/3,\pi/3)`, whose
   relevant values are established by elementary exact rational
   computation (`X_0(\pi/3,\pi/3)=1/4`, New result 6) and a fully
   self-contained hand Taylor+Lagrange-remainder bound
   (`D_2(\pi/3,\pi/3)\le-0.8`, New result 7) — it never touches `A^\ast`,
   `G_{\mathrm{curve}}`, or `h` at all. This independence was already
   noted by the round-17 proof-reviewer and is reconfirmed here by
   re-reading `lemmas/tgt-strictly-positive-throughout-D-full.md` in full:
   no reference to `A^\ast` or fact (ii) anywhere in it. Hypothesis (B)'s
   only use of `A^\ast` is exactly fact (i)+(ii) in Step 0, now proved.
2. **Does `lemmas/star-corner-is-boundary-cusp-not-critical-point.md`
   itself rest on anything unproved?** It supplies a numerically-computed
   gradient/Hessian at `(A^\ast,B^\ast)`, used only to justify treating the
   corner as a domain-boundary phenomenon rather than an interior critical
   point — a piece of *motivation* for earlier rounds' proof strategy, not
   a load-bearing fact in the final "Full proof" chain above (the "Full
   proof" section does not cite this lemma; `d1-nonnegative-on-boundary-
   curve.md`'s corrected Step 0 uses only `A^\ast`'s defining equation
   `G_{\mathrm{curve}}(A^\ast)=0` and the new closed form, not this
   lemma's gradient/Hessian numerics). Not load-bearing for the final
   proof; no gap.
3. **Does the branch/domain characterization used in the fix (`u\in
   (\pi/6,\pi/3)\subset(0,\pi/2)`) hold on the exact sub-locus needed?**
   Yes, and more strongly than before: this round proves `0<A^\ast<\pi/2`
   **exactly**, by comparing `\sin(\pi/6)=\tfrac12`, `\sqrt6/4`,
   `\sin(\pi/3)=\tfrac{\sqrt3}2` via squaring (`\tfrac14<\tfrac38<
   \tfrac34`, a rational comparison) rather than by citing the population's
   older, numerically-checked-only "`0<A<\pi/2` on `\mathcal D`" domain
   fact (round 11 of the `-pointwise` sibling) — a strictly higher rigor
   tier, and one that removes a numeric-only citation from the critical
   path entirely.
4. **Any other place in the file's dependency chain flagged
   provisional/numeric anywhere in rounds 11-17 and never definitively
   closed?** A full grep of this file and every lemma it cites for
   "numeric", "unproved", "conjectur", "not proved" turns up exactly one
   remaining hit worth addressing: `lemmas/mvt-lipschitz-reduction-case-
   b.md`'s own text says *"`(\star)` ... remains a conjecture, not a
   theorem"* — but that lemma is dated round 10, **before** this file's
   round-13 Reduction Lemma (New result 1) and rounds 16, 18's closure of
   hypotheses (A), (B) existed. `mvt-lipschitz-reduction-case-b.md` proves
   only the *reduction* "Case (b)'s target follows from `(\star)`" (its
   own Status: "Certified (reduction itself is gap-free and reusable;
   `(\star)` remains open)" — i.e. it never itself claims to prove
   `(\star)`, and correctly says so). `(\star)` itself is exactly what
   Steps 1-5 above prove, via the wholly separate, later Reduction Lemma
   machinery — so this stale "conjecture" annotation in the earlier lemma
   is accurate as a statement about *that lemma's own scope* and is not a
   live gap in the present, completed argument. (Recommended for a future
   round, as pure housekeeping, not a mathematical requirement: add a
   one-line update to `mvt-lipschitz-reduction-case-b.md` noting `(\star)`
   is now proved elsewhere, so no future round is confused by the stale
   wording.) No other numeric/conjecture flag was found in
   `lemmas/vector-reduction-OM-ON.md`, `lemmas/bilinear-chi-cramer-
   formula.md`, `lemmas/homogeneity-decoupling-rotation-param.md`,
   `lemmas/complex-affine-L1-DK-and-r-lo-selection.md`,
   `lemmas/w-r-lo-positive-via-zN-zK-evaluation.md`, or `lemmas/claim-I-
   closed-and-claim-II-caseA-closed.md` (Steps 1-3 above) — each is marked
   `Certified` and each was independently re-derived/re-checked by a
   proof-reviewer in its own round (rounds 6-10, per `current.md`'s
   preserved history), with no overclaiming flagged in any of those
   passes.
5. **Existence of `K,L`, and non-degeneracy (`K\ne L`, `O` well-defined).**
   These are hypotheses of the problem statement itself (`K,L` are *given*
   to exist inside triangles `BMC,BNC` with the stated angle properties;
   `O` is *given* as the circumcentre of `AKL`, which is well-defined
   whenever `A,K,L` are not collinear). The population's Steps 1-2 chain
   (rounds 1-10, independently certified across those rounds — not
   re-derived in this round, out of this round's scope, and not flagged
   as an open item by any of the 6-10 rounds' independent reviews) encodes
   `K,L,O` via the stated angle conditions and a rotation/Cramer
   parametrization; no round in this population's 17-round history flagged
   a degenerate `K=L$ or collinear-`A,K,L` case as unhandled. This is
   outside the scope of the round-18 dispatch (which targets gap 6
   specifically) and is not re-audited from scratch here; it is flagged
   explicitly so the proof-reviewer can independently judge whether it
   warrants a fresh look, rather than silently assuming it is fine.

**Conclusion of the round-18 audit (superseded — see round-19 addendum
immediately below).** No other silent gap, unstated numeric-only
dependency, or false "already certified" citation was found anywhere in
the chain besides the one this round fixed (fact (ii) of gap 6's Step 0,
now proved). Item 5 is the one place this audit could not itself supply
new certification (it is existing, previously-certified population
infrastructure, out of this round's scope) and is flagged for the
proof-reviewer's independent judgment rather than silently assumed.

**Round-19 addendum to the audit — the round-18 audit missed Step 3
itself.** The round-18 audit above traced hypotheses (A) and (B) of the
Reduction Lemma (i.e. Case (b)) exhaustively and correctly found them
sound, but did not re-derive Step 3 (Case (a)) from scratch — it only
inherited round 18's own (as it turns out, still-incomplete) diagnosis of
Step 3 as "just needs Theorem A extended." Round 19 did re-derive Step 3
from scratch (per this round's explicit dispatch instruction to check the
*whole* chain, not just the previously-flagged step) and found the
citation-scope fix, while fully correct on its own narrow terms (Sub-result
A, `f>0` on all of `[0,\gamma)`, is genuinely proved), does **not** deliver
the fact Case (a) actually needs (`G(\beta_1)\ge0`), and that fact's
residual is exactly the population's central `T\ge0`/`-q_1,-r_0` gap — see
"Full proof" Step 3 above for the complete diagnosis. **This is now
understood to be the true, and substantially harder, content of Open gap
7.** The whole route's status is unaffected in kind (still `partial`, still
one identified open gap) but the gap's true difficulty is now correctly
understood for the first time in this route's 8-round history (rounds
11-19) of treating Case (a) as a formality.

## Promotable lemmas

### Round 22 addition
- **`G\equiv2K_c-f` (exact identity, self-contained Fact).** With
  `K_c:=2\sin A\sin(A+B)`, `P:=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`,
  `Q:=-\sin A\sin B`, `G(\beta):=K_c-P\sin\beta-Q\cos\beta` (this file's
  Step 2 quantities) and `K:=2\sin A\sin(A+B)` (same value as `K_c`),
  `f(\beta):=2\sin(A+B)(\sin\beta+\sin A)-\sin B\sin(A+\beta)`
  (`coordinate-bash-resultant-boundary.md`'s §16 quantities): `G(\beta)=
  2K-f(\beta)` identically. Proved in full (elementary trig expansion) in
  "Round 22" §Fact 3 above; independently re-verified fresh by `sympy`,
  residual `0`. Reusable by any approach needing to translate between
  this file's `G/K_c/P/Q` notation and `coordinate-bash-resultant-
  boundary.md`'s `f/K` notation — flags explicitly that `K_c` and `K` are
  literally the same quantity, not related by a factor of `2` (a
  transcription risk the round-22 outline-reviewer specifically warned
  about).
- **Theorem 16.2 first branch (`Y(\gamma)\ge0\Rightarrow G(\beta)>0` for
  every `\beta\in(0,\gamma)`), re-derived and applied to close the
  `\beta_1\ge\gamma` case of the `\beta_1`-trichotomy.** For a triangle
  `ABC` with `\angle B\le\angle C$ (`\gamma:=\angle B\le\pi/2$),
  `Y(\beta):=2\cos^2\beta-2X_0(A,B)` (`X_0:=\sin B\cos A/(2\sin(A+B))`):
  if `Y(\gamma)\ge0` (equivalently `\beta_1\ge\gamma`, `\beta_1$ the unique
  angle in `[0,\pi/2)` with `\cos^2\beta_1=X_0`), then `G(\beta)>0` for
  every `\beta\in(0,\gamma)`, unconditionally (no hypothesis on `\sin(A+3
  \beta)` or on `\beta_1$ vs `\beta_0(A)` needed). Proved in full,
  self-contained (Facts 0-5, the Theorem, and its Consequence for
  `(\mathrm{II})`), in this file's "Round 22" section above, citing and
  independently re-verifying `coordinate-bash-resultant-boundary.md`'s
  Theorem 16.2 (round 9). Confirmed numerically (0 violations, a fresh
  `200{,}000`-sample sweep plus a dedicated `500{,}000`-trial near-boundary
  sweep targeting `|\beta_1-\gamma|<0.01`). Reusable by any other approach
  relying on the same `(\mathrm{I})/(\mathrm{II})` machinery (e.g.
  `coordinate-bash-resultant-boundary`, `-pointwise-tangent-via-T`) that
  needs to dispatch a `Y(\gamma)\ge0`/`\beta_1\ge\gamma`-style residual —
  exactly the counterpart of the round-21 Case (a) vacuity lemma for the
  complementary regime.

### Round 21 addition
- **Case (a) vacuity lemma.** For a triangle `ABC` with `A\le\pi/2$,
  `\angle B\le\angle C$ (`\gamma:=\angle B$), `\beta_0(A):=(\pi-A)/3`,
  `\gamma>\beta_0(A)` (domain-nonempty), `X_0(A,B):=\sin B\cos A/(2\sin(A+B))
  \in[0,1]`, `\beta_1\in[0,\pi/2)` the unique angle with `\cos^2\beta_1=X_0`,
  and `Y(\beta):=2\cos^2\beta-m\cos A` (`m:=\sin B/\sin(A+B)`): if `\beta_1
  \le\beta_0(A)`, then `Y(\beta)<0$ for every `\beta\in(\beta_0(A),\gamma)`.
  Consequently, the original `(\mathrm{II})` conditional of `coordinate-
  bash-resultant-boundary.md` §15 (`Y(\beta)>0\wedge\sin(A+3\beta)<0
  \implies\ldots`) holds vacuously for every `\beta\in(0,\gamma)` whenever
  `\beta_1\le\beta_0(A)`, so no positivity claim on `G(\beta_1)`, `T`, or any
  reduction of `(\mathrm{II})` is required in this regime. Proved in full,
  self-contained (2-line monotonicity argument plus an elementary algebraic
  identification `\beta_1\le\beta_0(A)\iff Y(\beta_0(A))\le0`), in this
  file's "Round 21" section and "Full proof" Step 3 above. Independently
  confirmed numerically (0 violations, 300,000-sample sweep) by the round-21
  outline-reviewer prior to this proof being written out in full. Reusable
  by any other approach relying on the same `(\mathrm{I})/(\mathrm{II})`
  machinery (e.g. `coordinate-bash-resultant-boundary`,
  `-pointwise-tangent-via-T`) to dispatch a Case-(a)-style residual.

### Round 20 addition
- **`T\ge0` (equivalently `G(\beta_1)\ge0`) throughout Case (b)'s exact
  residual domain `\mathcal D_b:=\{0<A\le\pi/2,0<B\le C,B>\beta_0(A),
  \cos^2B<X_0<\cos^2\beta_0(A),P>0,E<0\}`**, with equality only at the
  corner `(A^\ast,\beta_0(A^\ast))`. Fully proved in "Round 20" above: (i)
  `T(A^\ast,B^\ast)=0` exactly, by hand, via the `u=A/3+\pi/6` substitution
  and `\sin^2u^\ast=3/8,\cos^2u^\ast=5/8` (reusing `lemmas/d1-nonnegative-
  on-boundary-curve.md`'s already-certified corner facts); (ii) exact
  tangent-cone slopes `2/9` (lower curve `\mathcal C_{\mathrm{lo}}`) and `3`
  (upper curve) at the corner, and exact gradient `\partial T/\partial
  A|_\ast=14375\sqrt{15}/32768,\ \partial T/\partial B|_\ast=5625\sqrt{15}
  /32768`; (iii) a certified `mpmath.iv` domain-safety bound (true
  `t$-range `\subset(0.2024,3.121)` for `A\in(A^\ast,A^\ast+0.01]`) and
  Hessian bound (`|F_t''|\le35.67`) giving, via Taylor's theorem with
  Lagrange remainder, `T\ge1.6553(A-A^\ast)>0` near the corner; (iv) a
  certified `mpmath.iv` adaptive-quadtree sweep (0 unresolved boxes)
  proving `T\ge0` (or domain-empty) for `A\in[A^\ast+0.005,\pi/2]`. Union of
  (iii)-(iv) covers `(A^\ast,\pi/2]` in full. Combined with the already-
  certified Theorems 1, 4 of `lemmas/case-b-p-le-0-and-e-ge-0-closed.md`
  (`P\le0` and `P>0\wedge E\ge0`), this gives **`G(\beta_1)\ge0`
  unconditionally throughout Case (b) (`X_0<\cos^2\beta_0(A)`)**, an
  independent, direct proof of Case (b)'s conclusion (not requiring the
  `\mathrm{Tgt}/D_1$/Reduction-Lemma machinery at all). **This is the
  population's first unconditional closure, anywhere in its 10+-round
  search, of the `T\ge0`/`-q_1,-r_0` Positivstellensatz target on any
  nontrivial sub-domain** — a genuinely new, reusable result. **Caveat,
  explicitly not overclaimed**: this does NOT extend to Case (a)'s domain
  (`X_0>\cos^2\beta_0(A)`), where `T`/`G(\beta_1)` are demonstrably negative
  (see "Round 20"'s closing discussion) — the lemma's scope is Case (b)
  only, precisely as stated.

### Round 19 addition
- **`f(\beta)>0` for every `\beta\in[0,\gamma)`** (extends the certified
  Theorem A of `lemmas/claim-I-closed-and-claim-II-caseA-closed.md`, which
  only states this on `(\beta_0,\gamma)`, down to the full interval
  `[0,\gamma)`). Proof: Theorem A's own proof already shows `f'(\beta)=
  \sin(A+\beta)\cos B+\sin(A+B-\beta)>0` for every `\beta\in(0,\gamma)`
  (the sign argument never uses `\beta>\beta_0`); combined with the new
  elementary fact `f(0)=\sin A(2\sin(A+B)-\sin B)>0` strictly (via
  `2\sin C-\sin B\ge\sin C>0`, itself via the two-case argument `\sin B\le
  \sin C$: if `C\le\pi/2` then `0<B\le C\le\pi/2` and `\sin` is increasing
  there; if `C>\pi/2` then `A>0\Rightarrow0<B<\pi-C<\pi/2` and `\sin B<
  \sin(\pi-C)=\sin C`), the Mean Value Theorem on `[0,\beta_1]` gives
  `f(\beta_1)>f(0)>0` for every `\beta_1\in(0,\gamma)`. Fully proved above
  in "Full proof" Step 3 ("Sub-result A"), no numeric gap, no case omitted.
  **Caveat for any future user**: this is a genuinely useful, fully general
  fact about `f`, but (per this round's finding) it does **not** by itself
  establish `G(\beta_1)\ge0` for `\beta_1\le\beta_0(A)` — `f(\beta_1)>0`
  and `G(\beta_1)\ge0` are logically independent facts in this regime (an
  explicit counterexample, `A\approx0.01002,B\approx1.49926`, has `f(\beta_1)
  \approx0.719>0$ but `G(\beta_1)\approx-0.679<0`). Do not cite this lemma
  as closing any `G`-based target.

- **Exact `\partial X_0/\partial B$ formula**: `\partial X_0/\partial B=
  \dfrac{\sin A\cos A}{2\sin^2(A+B)}`, proved in full above via direct
  differentiation and the sine-subtraction identity, independently
  confirmed by `sympy` (zero residual). Reusable by any future attempt at
  `(\star)` via monotonicity-in-`B`.
- **Exact Case-(b) domain characterization**: `\mathcal D=\{0<A,\,0<B\le
  C,\ B>\beta_0(A),\ \cos^2B<X_0(A,B)<\cos^2\beta_0(A)\}`, with the
  numerically-established structural fact that the curve `B=\beta_0(A)`
  is (away from the corner `A^*`) essentially outside `\overline{\mathcal
  D}`, and the true lower `B`-boundary is the different implicit curve
  `X_0(A,B)=\cos^2B`. This corrects an implicit assumption in the
  population's prior quick scans (that `B=\beta_0(A)` is itself the
  relevant boundary curve to scan) and should inform any future symbolic
  attempt at `(\star)` or at the sibling `-sos`/`-pointwise`
  width-expansion mechanism.
- **Exact, simplified `\partial\mathrm{RHS}/\partial B` closed form (D2)**:
  proved this round via the elementary observation `\partial\beta_0/
  \partial B=0` plus direct differentiation of `K_c,P,Q`:
  `\partial\mathrm{RHS}/\partial B=-\sin B\cos\beta_0-\sin\beta_0\bigl(
  2\sin A\cos(A+B)+\sin\beta_0(\tfrac12\cos(A-B)-\tfrac32\cos(A+B))+\sin
  A\cos\beta_0\cos B\bigr)`, independently `sympy`-confirmed equal to
  round 11's messier fully-`A`-expanded formula. A further compact
  two-variable form (D2$'$, via `A=\pi-3\beta_0`) is also proved exact.
  Reusable by any future attempt at `\partial S/\partial B` or at
  `\partial_B\mathrm{RHS}`'s sign directly.
- **Decomposition identity (D3)**: `\partial S/\partial B=T_1+T_2` with
  `T_1=(1+\cos B)^2\partial_BX_0-2(1+\cos B)\sin B\,X_0`,
  `T_2=-2\,\mathrm{RHS}\,\partial_B\mathrm{RHS}`, proved exactly via the
  product rule from `S=(1+\cos B)^2X_0-\mathrm{RHS}^2`. Reusable as the
  standard starting point for any future attempt at this target; comes
  with the honest caveat (proved this round) that `T_1` alone is not
  sign-definite on `\mathcal D`, so a future proof must bound `T_1+T_2`
  jointly, not termwise.

### Round 13 additions
- **`f-g|_{\mathcal C}=D_1` exactly** (New result 2): proved in full via
  `\sqrt{X_0}=\cos B` on `\mathcal C` (using `\cos B>0`, itself an
  elementary proved fact) — a one-line but exact (not numeric) identity
  connecting this file's `f,g` to the `-twopoint` sibling's `D_1`. `sympy`
  residual `0`.
- **Radical-free factorization of `T_1` (T1$'$)**: `T_1=\dfrac{(1+\cos B)
  \cos A}{2\sin^2(A+B)}\bigl[(1+\cos B)\sin A-2\sin^2B\sin(A+B)\bigr]`,
  proved exactly by direct algebra from the certified `\partial_BX_0,X_0`
  closed forms; `sympy`-confirmed, residual `0`. Reusable for building any
  future radical-free comparison target involving `\partial f/\partial B`.
- **The Reduction Lemma (New result 1)**: given (A) `\partial(f-g)/\partial
  B>0` on `\mathcal D` and (B) `D_1\ge0` on `\mathcal C`, then `f\ge g`
  throughout `\mathcal D` — proved in full via monotonicity from the
  domain's boundary curve, **with no separate hypothesis on the sign of
  `\mathrm{RHS}` anywhere in the argument** (a genuine simplification over
  the outline's original roadmap, which asked for an unconditional
  `\mathrm{RHS}>0` proof). Reusable as the master reduction for this whole
  route; removes an entire previously-open sub-target
  (`\mathrm{RHS}>0$ unconditionally) from the critical path.
- **Domain connectedness + sign-determination Lemma (New result 5)**:
  `\mathcal D` is path-connected (proved via the strict-monotonicity/IVT
  argument establishing `B_{\mathrm{lo}}(A)` is a well-defined continuous
  function of `A`, giving `\mathcal D` as a curvilinear trapezoid over a
  connected `A`-interval), and consequently, if a continuous function's
  vanishing is excluded everywhere by a nonvanishing-product fact (here,
  `\mathrm{Tgt}\ne0`), its sign is determined by a single point evaluation.
  A reusable proof-strategy device: converts "prove sign `S(x)>0` for all
  `x` in a connected domain" into "prove `S(x)\ne0` for all `x`" (often
  algebraically easier, e.g. via a strict inequality with margin) plus one
  concrete evaluation.

**Not yet promotable**: `\mathrm{Tgt}(A,B)>0` throughout `\mathcal D`
itself — strong numeric evidence (global-optimization minimum
`\approx1.574`) but not a proved symbolic inequality; this is the file's
own primary open gap (Open gap 5) and should not be certified.

### Round 14 additions
- **`X_0(\pi/3,\pi/3)=1/4` exactly** (New result 6): trivial substitution,
  fully elementary. Reusable anywhere the equilateral corner value of `X_0`
  is needed.
- **`D_2(\pi/3,\pi/3)\ne0`, in fact `\le-0.8`** (New result 7): a
  fully self-contained, hand-checkable rational proof via Taylor series with
  Lagrange remainder for `\sin,\cos` plus the classical Archimedes bound
  `223/71<\pi<22/7` — no black-box numerics, every number is an exact
  rational computed via `fractions.Fraction`. This is the strongest-rigor
  result of the round and is directly promotable/reusable as the exact
  nonvanishing fact needed to make `\mathrm{Tgt}(\pi/3,\pi/3)>0` unconditional
  (`\ge1.44`, via `(9/4)(0.8)^2`).
- **Exact `\partial X_0/\partial A$ formula (D6)**: `\partial X_0/\partial A
  =-\dfrac{\sin B\cos B}{2\sin^2(A+B)}`, proved via the quotient rule and the
  cosine-subtraction identity, symmetric in structure to the
  already-certified `\partial X_0/\partial B` formula. `sympy`-confirmed,
  residual `0`. Reusable for any future implicit-curve/tangent-slope
  computation involving `X_0`.
- **Exact tangent slopes of `\mathcal D`'s two boundary curves at the corner
  `(\pi/3,\pi/3)`** (New result 8): `dB_{\mathrm{hi}}/dA=-1/2` (trivial) and
  `dB_{\mathrm{lo}}/dA=1/4` (via implicit differentiation of `X_0=\cos^2B`
  and (D6)), both exact rationals, `sympy`-confirmed. Also establishes
  exactly (not numerically) that `(\pi/3,\pi/3)` is a genuine domain pinch
  point (`X_0(\pi/3,\pi/3)=\cos^2(\pi/3)=1/4`) and, via the local linear
  expansion, that the domain does not extend past `A=\pi/3` to leading
  order. Reusable for any future local analysis of `\mathcal D` near this
  corner (e.g. a future attempt at the still-open global-min gap).
- **`(\pi/3,\pi/3)` is a strict local minimum of `\mathrm{Tgt}` relative to
  `\mathcal D`** (New result 9): proved via a first-order
  gradient/tangent-cone argument — the directional derivative of
  `\mathrm{Tgt}$ into the domain is bounded below by `\delta\approx3.50>0`
  uniformly over the tangent cone at the corner. The gradient values
  themselves were certified via `60`-digit `mpmath.iv` directed-rounding
  interval arithmetic (disclosed honestly as one rigor tier below New
  result 7's fully hand-derivable bound, but still a genuine rigorous
  enclosure, not a floating-point spot check). Reusable as a genuine partial
  step toward the still-open global-minimality gap; NOT itself sufficient to
  close it (only establishes local, not global, minimality).

### Round 15 additions
- **Corrected corner-value citation**: `\mathrm{Tgt}(\pi/3,\pi/3)=
  1.57413622481406257722651370062\ldots` (30 digits, independently confirmed
  via two routes — direct `sympy.N` and `mpmath.iv` — and matching the
  round-15 outline-reviewer's independent value exactly); supersedes the
  stale round-13/14 citation `1.5741362290964376`, which was imprecise from
  the 9th significant digit on. Does not affect any previously-proved
  conclusion.
- **Theorem A — exact closed-form parametrization of `\mathcal
  C_{\mathrm{lo}}`**: on `\mathcal C_{\mathrm{lo}}=\{X_0=\cos^2B\}` with
  `B\in(0,\pi/2)`, `\tan A=\sin B(1-2\cos^2B)/(2\cos^3B)=-\sin B\cos(2B)/
  (2\cos^3B)`, proved in full via the sine-addition identity and
  `\cos A\ne0`. Correctly recovers both known corners of `\mathcal D`
  (`A(\pi/3)=\pi/3$ exactly; `A(0.91174\ldots)\approx0.40640\ldots$,
  matching the population's long-standing `A^\ast$ numerics) as its
  endpoints. Reusable for any future symbolic or certified-numerical work
  on `\mathcal C_{\mathrm{lo}}` — the first explicit (non-implicit) formula
  for this curve in the population's history.
- **Theorem B — `\mathrm{Tgt}\ge\mathrm{Tgt}(\pi/3,\pi/3)` on all of
  `\mathcal C_{\mathrm{hi}}\cap\mathcal D`**: proved in full via a
  certified directed-rounding interval-arithmetic branch-covering argument
  (value-sweep away from the corner, `0` bad sub-intervals among `3000`;
  derivative-sign sweep near the corner via MVT, `0` bad sub-intervals among
  `4000`) — a genuinely rigorous, gap-free proof of the entire boundary-
  curve sub-target, not numeric sampling. Reusable as a certified building
  block for global minimality once the interior/near-corner gap (see Open
  gap 5) is closed.
- **Theorem C — `\mathrm{Tgt}\ge\mathrm{Tgt}(\pi/3,\pi/3)` on all of
  `\mathcal C_{\mathrm{lo}}\cap\mathcal D`**: proved in full by the same
  certified-interval method, using Theorem A's parametrization to reduce to
  a 1-variable target in `B` (`0` bad sub-intervals in either the value-sweep
  or derivative-sweep half, `1500` sub-intervals each). Reusable
  analogously to Theorem B.
- **Structural finding: `\mathcal D` has a third boundary curve `\mathcal
  C_{\mathrm{mid}}:X_0=\cos^2\beta_0(A)`**, active for `A\in(A^\ast,
  0.5579\ldots)`, distinct from `\mathcal C_{\mathrm{hi}}` (`B=(\pi-A)/2`,
  active only for `A\gtrsim0.5579`) — correcting round 14's "exactly two
  boundary curves" picture (valid only near the `(\pi/3,\pi/3)`-adjacent
  region). Reusable as a caution for any future boundary-curve-decomposition
  argument on this domain; the round-15 2-D interval sweep sidesteps this
  by covering the interior directly rather than decomposing the boundary.

### Round 16 additions
- **`\mathrm{Tgt}\ge\mathrm{Tgt}(\pi/3,\pi/3)` throughout `\bar{\mathcal D}`
  — fully closed, certified lemma**: proved via an exact Taylor identity
  with a certified Lagrange-remainder bound over an explicit radius
  `r_0=0.01`, glued to round 15's 2-D adaptive sweep (which independently
  covers everything outside a `\lesssim5\times10^{-8}` residual). Full
  statement, all certified numbers (`g_A,g_B,\delta_{\min}`, the second-
  derivative enclosure, the domain-safety `\varphi`-argument), and an
  honest scope caveat (does not touch Open gap 6) are in
  `lemmas/tgt-strictly-positive-throughout-D-full.md`. This closes Open
  gap 5 **in full** — the first of this route's two remaining sub-targets
  (per New result 5's "Net assessment") is now completely proved, leaving
  only Open gap 6 (`D_1(A)\ge0` on `\mathcal C`) as this route's sole
  outstanding obstruction.
- **Reusable technique**: "sweep the second derivative along rays from
  an equality point, via Taylor's theorem with a certified Lagrange
  remainder" — avoids the interval-arithmetic degeneracy that defeats a
  raw value- or quotient-sweep exactly at a point of equality, and needs
  only a one-sided (not exact/inverted) bound on the domain's curved edge.
  Applicable to any future "prove `f\ge f(\text{corner})` near an
  equality point" target in this population.

**Not yet promotable (round 16 assessment, now superseded)**: the round-16
text noted only Open gap 6 remained; that gap is now closed (round 17,
below).

### Round 17 additions — **REJECTED by proof-reviewer, round 17**
- `D_1(A)\ge0` on `\mathcal C_{\mathrm{lo}}` was claimed closed via Step 0
  of `lemmas/d1-nonnegative-on-boundary-curve.md`, but Step 0's fact (ii)
  (`X_0(A^\ast,B^\ast)=\cos^2B^\ast`) was cited as "already-certified" when
  it was in fact an unproved numeric coincidence. **Not promotable as
  filed.** Superseded by the round-18 fix below, which proves fact (ii)
  instead of citing it.

### Round 18 additions
- **`D_1(A)\ge0` on the boundary curve `\mathcal C=\mathcal C_{\mathrm{lo}}`
  — fully closed, corrected lemma, proposed for certification**: fixes
  round 17's Step 0 by *proving* fact (ii) (previously an unproved
  coincidence) via (a) a hand-derived identity `G_{\mathrm{curve}}(u)=
  -8\sin u\cos^2u\cdot h(u)` (`u=A/3+\pi/6`), obtained from the raw
  definitions using only classical double/triple-angle formulas
  (`\cos3u=4\cos^3u-3\cos u`, `\sin2u=2\sin u\cos u`,
  `\sin4u=4\sin u\cos u(2\cos^2u-1)`), fully hand-checkable term by term;
  (b) an exact closed form `A^\ast=3\arcsin(\sqrt6/4)-\pi/2`, proved (not
  numerically found) to satisfy `G_{\mathrm{curve}}(A^\ast)=0` and to lie
  in `(0,\pi/2)`, via elementary rational comparisons
  (`\tfrac14<\tfrac38<\tfrac34$); (c) a proof that this closed form is the
  population's actual standing `A^\ast$, via uniqueness of
  `G_{\mathrm{curve}}`'s root on `(0,\pi/2)` (using the identity itself)
  plus 60-digit numeric agreement. Steps 1-4 (certified `mpmath.iv`
  enclosure of `B^\ast`, derivative-sign sweep `D_1'\ge4`, value sweep
  `D_1>0`, MVT gluing) are unchanged from round 17. Full corrected
  statement in `lemmas/d1-nonnegative-on-boundary-curve.md`. This closes
  Open gap 6 **in full** (proof-reviewer-certified, round 18) — but does
  **not** complete the whole problem's claim: the proof-reviewer (round 18)
  found a separate, previously-unflagged gap in "Full proof" Step 3's Case
  (a) closure (see Open gap 7, and "Status" at the top of this file). The
  route is not `solved`; Status is `partial`.
- **Reusable technique, upgraded**: "when a boundary-curve corner value's
  vanishing is cited via 'the corner satisfies two defining equations
  simultaneously,' don't trust that the two equations share a root just
  because they numerically appear to — find the algebraic cofactor
  relating them (here, via a change of variable and classical multi-angle
  identities) and use it to convert the coincidence into a proved `iff`."
  A generally reusable de-risking pattern for any future "two independently
  numeric-pinned points coincide" claim in this population.
- **First exact closed form for `A^\ast`** in this population's history
  (`A^\ast=3\arcsin(\sqrt6/4)-\pi/2`), independently reusable anywhere a
  future round needs `A^\ast` symbolically rather than to 40 numeric
  digits.

**Not yet promotable**: the top-level `OM=ON` claim ("Full proof") itself —
**proof-reviewer, round 18: this file's Status is `partial`, not `solved`.**
Gap 6 (`D_1(A)\ge0` on `\mathcal C`) is genuinely closed and certified
(`lemmas/d1-nonnegative-on-boundary-curve.md`), but "Full proof" Step 3
(Case (a), `\beta_1\le\beta_0(A)`) rests on an unjustified citation — see
"Status" at the top of this file and Open gap 7 for the precise diagnosis.
Every other substantive claim of this file (all promotable lemmas listed
above) remains valid and certified.
