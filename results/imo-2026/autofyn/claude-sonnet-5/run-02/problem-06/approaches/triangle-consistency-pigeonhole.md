## Status
partial

## Approaches tried

- **Round 20 (this round, per outline-reviewer's "revise" dispatch: close the
  Two-Sided Singleton Witness Theorem's existence hypothesis via the
  "Constrained Singleton Coherence" reframing — pigeonhole `gcd(a_{m_A},a_x)`
  to a fixed value `d*`, then ask whether SOME witness `m_A`'s induced class
  is always a prime power).** Result: **the reframed question is proved to be
  a genuine, correctly-scoped sharpening (Constrained Singleton Coherence
  Lemma and its two corollaries proved in full, unconditional, §6.1), but its
  own existence hypothesis (step 4 of the outline) is NOT resolved** — and,
  crucially, this round identifies and proves *why* the positive
  computational evidence gathered for it is not independent support: on both
  of the workspace's only known hard test seeds, the observed
  "always‑prime‑power" pattern is a **confound**, a downstream, fully
  explained consequence of the pair's Cofinite FAH witness prime already
  being established by the (unrelated, earlier-round) Two-Sided Singleton
  Witness Theorem itself, not new evidence toward the general conjecture
  (§6.2 — new negative/diagnostic finding, proved with full case analysis,
  in the style of the already-certified Same-Type Triangle Vacuity result).
  A further attempt to obtain a genuinely independent (non-confounded) test
  instance, by implementing a heuristic core-recruitment procedure and
  scanning ~70 fresh candidate seeds for rogue pairs with `|F'|,|F''|≥2` at a
  *recruited* core, is reported honestly as a **failed replication**: the
  heuristic does not reproduce the workspace's documented recruited cores
  for the two known hard seeds (it recruits unboundedly instead of
  stabilizing at the recorded `S_0`), so its output cannot be trusted and no
  new seed is certified (§6.3). Net honest verdict: the sharpened existence
  question is proved to be a well-posed necessary-coherence *tool*, usable
  once a global witness prime is otherwise known, but is shown **not** to
  bypass the round-19 sieve/anatomy-of-integers obstruction — closing it in
  general appears to require exactly the same kind of implicit-sequence
  density control that obstruction already identified as unavailable (§6.4).
  Status remains `partial`.

- **Round 19 (per outline-reviewer's "revise" dispatch: attempt to
  close the Two-Sided Singleton Witness Theorem's residual existence
  hypothesis via an anatomy-of-integers/density argument, starting with the
  weaker "infinitely often" sub-target).** Result: **the mechanism does not
  close, and a precise, honest obstruction is now identified and documented**
  (see `Current best` §5). Concretely: (a) proved in full, unconditionally, the
  elementary anatomy-of-integers fact the outline's Step 2 needed (the
  `O(log a_n)` bound on `ω(a_n)`, §5.1) — genuine but insufficient content;
  (b) extended this round's math-explorer's computational check (doubled the
  window on both known hard seeds, `a_1=4807` and `a_1=11305`) to test whether
  singleton-occurrence COUNTS keep growing with the window rather than
  plateauing — they do (roughly linearly, at a stable rate, on both seeds and
  both sides; full data in §5.2) — mild supporting evidence, explicitly *not*
  treated as a proof of infinitude; (c) identified and wrote out in full the
  specific reason the proposed sieve/anatomy-of-integers density mechanism
  (Step 3 of the outline) **cannot be carried out with any existing
  technique**: every sieve or normal-order result that could plausibly deliver
  "infinitely many singleton values in a sequence" (Brun/Selberg sieve
  lower bounds for almost-primes, Hardy–Ramanujan/Erdős–Kac normal order,
  or any elementary density argument of this family) requires the target
  sequence to be *explicit* — given by a closed-form expression in the index
  (e.g. a linear or polynomial form `f(n)`) with independently computable or
  boundable local densities `\{n \le N : p \mid f(n)\}/N` at each prime `p`,
  usually via congruence-class/CRT structure. The sequence actually in play
  here — the out-of-core cofactor `w_n` restricted to the persistent-type
  index set `X_A` — has **neither property**: both `X_A` (membership) and
  `w_n` (value) are defined only implicitly, via the entire history of the
  greedy legality recursion, with no closed form and no known independent
  congruence-class control at any prime outside `S_0`. This is a genuine,
  specific, technical obstruction (see §5.3), not a vague "seems hard" — it is
  the precise reason no sieve-theoretic tool in the knowledge base or crux
  corpus (confirmed empty search, per this round's math-explorer) transfers
  to this setting. The weaker "infinitely often" sub-target (the outline's
  own cheaper first goal) is therefore **not established**, and the
  outline's Step 5 "third pigeonhole layer" (forcing a shared witness prime
  across `F'` and `F''`) is consequently unreachable this round, since it is
  strictly downstream of Step 3. Reported honestly as a negative result
  (obstruction identified, not merely "insufficient time"), per the round's
  explicit instruction not to paper over a genuine gap.

- **Round 18 (new approach, build set per outline-reviewer's
  CHANGES-REQUESTED-then-build dispatch).** Built the outline's Double-Witness
  Nested Pigeonhole Lemma (steps 1–5) in full — genuine, unconditional, correct
  (see `Current best` §1). Re-scoped the outline's mandated cheap-kill to the
  actually-hard regime (properly-recruited-core rogue pairs on `a_1=4807` and
  `a_1=11305`, the only two such instances on record anywhere in the workspace
  — confirmed via a fresh literature search of the workspace's own files that
  no seed with `|F'|,|F''| ≥ 2` on **both** sides has ever been found despite
  multiple broad sweeps in prior rounds; this is itself documented explicitly
  below as a negative finding, per the dispatch's instruction to verify the
  crux is not vacuous or already known). Ran the actual triangle-consistency
  mechanism (the outline's Step 6/7, `e := gcd(a_{m_A}, a_{m_A'})`) on both
  hard seeds and **proved it structurally cannot supply the needed forcing**
  (see `Current best` §2 — a genuine, complete negative result, not a guess).
  While investigating why the two hard seeds nonetheless both empirically
  exhibit literal (zero-exception) FAH, found and fully proved a **different,
  new mechanism** — the **Two-Sided Singleton Witness Theorem** — that
  correctly explains both seeds' resolution and is a genuinely new, reusable,
  unconditional-modulo-one-existence-hypothesis result (see `Current best`
  §3). Existence of the required witnesses in general remains open; this is
  the round's honestly-reported residual gap (see `Current best` §4).

## Current best

Notation and imports (all cited, none re-derived from an open hypothesis):
`(a_n)` is the problem's sequence (`a_1>1`; `a_{n+1}` = least integer exceeding
`a_n` with `gcd(a_{n+1},a_i)>1` for every `i \le n`). `P(m)` denotes the set of
prime divisors of `m`. `Q := P(a_1)`. `S_0` denotes a fixed core with
`Q \subseteq S_0`, and for `n\ge 1`, the **extended type** at `S_0` is
`\rho(n) := P(a_n)\cap S_0`. A type `A` is `S_0`-**persistent** if
`X_A := \{n : \rho(n)=A\}` is infinite (certified,
`lemmas/persistent-type-pigeonhole.md`,
`lemmas/extended-persistent-type-pigeonhole.md`). A **rogue pair** `(A,B)` is
a pair of disjoint (`A\cap B=\emptyset`) `S_0`-persistent types at the
terminal, fully-recruited core `S_0=S^*$ of the Finite Core Theorem /
Self-Absorbing Core Theorem's construction (`lemmas/finite-core-theorem.md`,
`lemmas/self-absorbing-core-theorem.md`). This is the setting H1 (FAH) is
about, and the setting the outline-reviewer required the builder to work in
(not the easier, already-resolved raw-`Q`-level base-type setting).

**Preliminary fact (used throughout, proved once here).** *Every extended
type is nonempty.* For `n\ge 2`, Free Facts (`lemmas/free-facts-gcd.md`, part
2) gives `\gcd(a_n,a_1)>1`, so some prime `p` divides both `a_n` and `a_1`;
then `p\in Q\subseteq S_0`, so `p\in P(a_n)\cap S_0=\rho(n)`, i.e.
`\rho(n)\ne\emptyset`. For `n=1`, `\rho(1)=P(a_1)\cap S_0=Q\cap S_0=Q\ne
\emptyset` since `a_1>1`. So `\rho(n)\ne\emptyset` for every `n\ge1`; in
particular every persistent type `A` used below is nonempty.

### §1. Double-Witness Nested Pigeonhole Lemma — proved in full (promotable)

**Statement.** Fix a rogue pair `(A,B)` at core `S_0`, and fix two *distinct*
indices `m_A, m_A' \in X_A` (both exist since `X_A` is infinite). Then there
exist an integer `d_1 \mid a_{m_A}` and an infinite set
`X_B^{(1)} \subseteq X_B` with `\gcd(a_{m_A}, a_x) = d_1` for every
`x \in X_B^{(1)}`; and, restricting to `X_B^{(1)}`, there exist an integer
`d_2 \mid a_{m_A'}` and an infinite set `X_B^{(2)} \subseteq X_B^{(1)}` with
`\gcd(a_{m_A'}, a_x) = d_2` for every `x\in X_B^{(2)}`. Moreover `d_1,d_2>1`,
and every prime factor of `d_1` lies in `F'_{m_A} := P(a_{m_A})\setminus S_0`,
while every prime factor of `d_2` lies in `F'_{m_A'} := P(a_{m_A'})\setminus
S_0` — both **fixed finite sets independent of `x`**.

**Proof.** For each `x\in X_B`, `\gcd(a_{m_A},a_x)` is a positive divisor of
the *fixed* integer `a_{m_A}`, so it takes values in the finite set
`\mathrm{Div}(a_{m_A})`. Since `X_B` is infinite and `\mathrm{Div}(a_{m_A})`
is finite, by the pigeonhole principle some value `d_1\in\mathrm{Div}(a_{m_A})`
is attained by `\gcd(a_{m_A},a_x)` for infinitely many `x\in X_B`; let
`X_B^{(1)}` be the (infinite) set of such `x`. Repeating the identical
argument with `a_{m_A'}` in place of `a_{m_A}` and `X_B^{(1)}` in place of
`X_B` (still infinite, so the same pigeonhole applies) produces `d_2` and
`X_B^{(2)}\subseteq X_B^{(1)}$, infinite, with `\gcd(a_{m_A'},a_x)=d_2` for
all `x\in X_B^{(2)}`.

`d_1>1`: for any `x\in X_B^{(1)}`, `x\ne m_A` (since `\rho(x)=B\ne A=\rho(m_A)`,
as `A,B` are disjoint hence distinct, and `\rho(x)=\rho(m_A)$ would force
`x=m_A$ is not needed — simply `x\ne m_A` because one has `\rho(x)=B` and
`\rho(m_A)=A`, and $A\ne B$ since they are disjoint and nonempty), so Free
Facts gives `\gcd(a_{m_A},a_x)=d_1>1`. Identically `d_2>1`.

*Confinement.* Let `p` be a prime factor of `d_1=\gcd(a_{m_A},a_x)$ for some
(equivalently, by definition of `d_1`, for every) `x\in X_B^{(1)}`. If
`p\in S_0`, then `p\in P(a_{m_A})\cap S_0=\rho(m_A)=A` and
`p\in P(a_x)\cap S_0=\rho(x)=B`, so `p\in A\cap B=\emptyset` — contradiction
(this is the rogue-pair disjointness hypothesis). Hence `p\notin S_0`, i.e.
`p\in P(a_{m_A})\setminus S_0=F'_{m_A}`. So every prime factor of `d_1` lies
in `F'_{m_A}`, a set depending only on the fixed integer `a_{m_A}` — in
particular independent of `x`. The identical argument (with `m_A'` and `B`)
gives every prime factor of `d_2` lying in `F'_{m_A'}`. $\blacksquare$

This is a direct two-fold application of the certified Confined-GCD Lemma
(`lemmas/confined-gcd-lemma.md`) with the roles of the two types exchanged:
Confined-GCD's own statement is symmetric in which side is held fixed as
"the witness" and which side is "the variable index," so the confinement
half of this proof is precisely Confined-GCD Lemma applied twice (once with
witness `m_A`, once with witness `m_A'`), and the pigeonhole-value half is
the elementary infinite-pigeonhole-on-a-finite-target argument the outline
specified. No step here uses any open hypothesis; this Lemma is genuinely
new (no certified lemma nests two nested nested-pigeonhole nested passes on
two *different, fixed* witnesses of one type against a shrinking *shared*
subset of the other type's occurrence set) and is fully unconditional.

### §2. The outline's proposed forcing mechanism (Cross-Witness Common-Prime
Lemma via the triangle `e := gcd(a_{m_A},a_{m_A'})`) fails structurally — a
complete negative result, not merely a stall

The outline's Step 6/7 proposed deriving `\gcd(d_1,d_2)>1` (i.e. some prime
common to `F'_{m_A}` and `F'_{m_A'}` that actually realizes both `d_1` and
`d_2`) by relating `d_1,d_2` to `e:=\gcd(a_{m_A},a_{m_A'})$, which is `>1`
unconditionally by Free Facts (since `m_A\ne m_A'`).

**Claim.** `e` carries **no information** about `F'_{m_A}\cap F'_{m_A'}`, and
in particular Free Facts applied to the pair `(m_A,m_A')` cannot be used to
force `\gcd(d_1,d_2)>1`.

**Proof.** Since `\rho(m_A)=\rho(m_A')=A`, every prime `p\in A` divides both
`a_{m_A}` and `a_{m_A'}` (by definition of extended type), so
`A\subseteq P(a_{m_A})\cap P(a_{m_A'})`, hence `\prod_{p\in A}p^{\min(v_p(a_{m_A}),v_p(a_{m_A'}))}`
divides `e`. Since `A\ne\emptyset` (§ preliminary fact), this alone already
forces `e>1` — i.e. Free Facts' conclusion `e>1` is **fully explained by the
type `A`'s own in-core primes**, with no reference whatsoever to
`F'_{m_A}` or `F'_{m_A'}`. This is exactly the phenomenon flagged by the
workspace's Same-Type Free-Facts Vacuity finding
(`lemmas/same-type-free-facts-vacuity.md`): Free Facts applied to two
occurrences of the *same* persistent type gives no outside-core information,
because the in-core primes of `A` alone already certify `\gcd>1`. No
certified lemma (Confined-GCD, Generalized Bounded Witness, or any other)
relates the *outside-core* prime content of `a_{m_A}` to that of `a_{m_A'}`
— those two sets are each individually confined (by Confined-GCD, applied
with witness `m_A$ resp. `m_A'` against *disjoint*-type partners), but
Confined-GCD's confinement mechanism requires a **disjoint-type** partner to
rule out the in-core primes; it supplies no tool at all for relating two
witnesses of the *same* type to each other. Hence, from Free Facts and the
certified lemma stack alone, `e`'s out-of-core prime factors (if any) are
logically unconstrained: they need not exist at all (`e` could in principle
equal `\prod_{p\in A}p^{\min(\cdot,\cdot)}` exactly, with no outside-core
factor), and even if `e` does have an outside-core factor, no certified tool
forces it to coincide with (or even intersect) `F'_{m_A}\cap F'_{m_A'}`
specifically — as opposed to being an unrelated bystander prime dividing
both `a_{m_A}` and `a_{m_A'}` "by accident." $\blacksquare$

**Concrete confirmation this is not merely a proof-inspection worry.** I
computed `e=\gcd(a_{m_A},a_{m_A'})` for every pair of the 13 occurrences of
the rogue-pair type `A'=\{3,5,19\}` found (out of `8000` terms, trial-division
simulation) for `a_1=4807` at its properly recruited core
`S_0=\{2,3,5,11,19,23\}` (rogue partner `B'=\{2,11\}$). In every one of the
`\binom{13}{2}` pairs sampled, `e`'s out-of-core part is `\{17\}` exactly —
looking like a "hit." **But this is a confound, not a confirmation of the
triangle mechanism**: `17` was already independently established (§3 below,
via a *different*, certified mechanism) to divide **every** occurrence of
`A'` in this range; once that independent fact holds, `e`'s out-of-core part
is forced to contain `17` for a trivial reason (`17` already divides both
`a_{m_A}` and `a_{m_A'}` individually, regardless of any triangle argument).
The triangle mechanism itself supplies zero *additional* forcing beyond what
that independent mechanism already gives — exactly as the structural proof
above predicts. (Full computation: script preserved at
`/tmp/round-18/sim_crux3.py`.)

**Conclusion of §2.** The outline's Step 6/7, as literally specified
(deriving `\gcd(d_1,d_2)>1` from `e:=\gcd(a_{m_A},a_{m_A'})`), is **dead**: it
is a disguised instance of the Same-Type Free-Facts Vacuity phenomenon
(memory rule 25), now confirmed for this specific construction with a full
proof and a concrete numeric check showing the apparent "hit" on the one
seed where it looked promising is fully explained by an unrelated mechanism.
This is the workspace's newest confirmed-dead FAH mechanism variant; it
should not be re-attempted in this form.

### §3. Two-Sided Singleton Witness Theorem — a new, proved conditional
mechanism that correctly explains both available hard test seeds

While diagnosing why `17` (resp. `11`) nonetheless divides *every* tested
occurrence of *both* types in the `a_1=4807` (resp. `a_1=11305`) rogue pairs,
I found the actual explanation, and it is a genuinely new (not previously
exploited in the workspace) combination of the already-certified Singleton-
Side FAH Lemma (`lemmas/singleton-side-fah.md`).

**Key observation.** Singleton-Side FAH is stated for *any valid witness
pair* `(n_A,n_B)` of the two types (`\rho(n_A)=A$, `\rho(n_B)=B`, not
necessarily the earliest occurrences): if `F'':=P(a_{n_B})\setminus S_0` is a
singleton `\{q\}`, then `q\mid a_n` for **every** `n>n_B` with `\rho(n)=A`.
Every prior use of this Lemma in the workspace applied it only with the
*earliest* occurrence of each type. But nothing in its proof requires this —
the proof (via the Generalized Bounded Witness Lemma) only uses that `n_B`
is *some* fixed index with `\rho(n_B)=B`. This licenses searching over *all*
occurrences of `B`, not just the earliest, for one with a singleton
out-of-core signature.

**Theorem (Two-Sided Singleton Witness).** Let `(A,B)` be a rogue pair at
core `S_0`. Suppose there exist an index `x_1` with `\rho(x_1)=B` and
`P(a_{x_1})\setminus S_0=\{q\}` (singleton, for some prime `q`), and an index
`x_2` with `\rho(x_2)=A` and `P(a_{x_2})\setminus S_0=\{q\}` (the **same**
prime `q`). Then:
(a) `q\mid a_n` for every `n>x_1` with `\rho(n)=A`;
(b) `q\mid a_n` for every `n>x_2` with `\rho(n)=B`.
In particular `q` divides all but finitely many occurrences of `A` and all
but finitely many occurrences of `B` — i.e. **Cofinite FAH holds for the
pair `(A,B)`**, with witness prime `q`.

**Proof.** (a) is exactly Singleton-Side FAH applied to the witness pair
`(n_A,n_B):=(\text{any }A\text{-occurrence}, x_1)` — its hypothesis is
`F'':=P(a_{x_1})\setminus S_0=\{q\}`, which holds by assumption; its
conclusion is `q\mid a_n` for every `n>x_1` with `\rho(n)=A`, exactly as
claimed. (b) is Singleton-Side FAH's symmetric statement applied to the
witness pair `(x_2, \text{any }B\text{-occurrence})`, using the hypothesis
`F':=P(a_{x_2})\setminus S_0=\{q\}`. Both are direct, unconditional
citations of the certified Lemma; no new machinery beyond the Lemma itself
and the existence of the two singleton witnesses is used. Since `A` is
`S_0`-persistent, `X_A` is infinite, so `X_A\cap[1,x_1]` is finite (an
infinite set minus a finite initial segment is still infinite, and
conversely its intersection with any finite interval is finite), hence all
but finitely many `A`-occurrences exceed `x_1$ and so satisfy (a); similarly
for `B` and (b). Cofinite FAH (as already certified sufficient for H1's
role in the Master Conditional Theorem, via
`lemmas/cofinite-sufficiency-lemma.md`) follows directly. $\blacksquare$

**This is genuinely new, reusable content**: it is *not* Singleton-Side FAH
itself (which only resolves ONE side, using the type's *canonical* witness,
and only when that side happens to already be singleton) — it is a
**two-witness, possibly-non-canonical-witness** upgrade that resolves *both*
sides simultaneously, conditional on an existence hypothesis (a matching
pair of singleton witnesses) that is strictly *weaker* than requiring the
canonical/earliest witnesses to be singleton (any later occurrence may serve
instead). It also does **not** collapse into the outline's original,
now-confirmed-dead triangle mechanism: it uses no `e=\gcd(m_A,m_A')`
comparison at all, only two independent applications of an already-certified
Lemma at two independently-chosen witnesses.

**Concrete verification on both available hard test seeds.**

- `a_1=4807`, `S_0=\{2,3,5,11,19,23\}`, `A'=\{3,5,19\}`, `B'=\{2,11\}`. The
  canonical witness `n_A=6` already has `F'_{6}=\{17\}` singleton (this is
  the seed's known `F'` from `lemmas/reduced-alphabet-corollary.md`), so
  `x_2:=6$ works directly. For the other side: among the `B'`-occurrences
  found up to `n=8000`, index `x_1=72` (a_{72}) has
  `P(a_{72})\setminus S_0=\{17\}` exactly (found by direct scan — 20 of the
  180 sampled `B'`-occurrences below `n=8000` have this exact singleton
  signature; the earliest is `x_1=72$). Both singleton witnesses use the
  same prime `q=17`. Applying the Theorem: `17\mid a_n` for every `A'`-
  occurrence `n>72` and every `B'`-occurrence `n>6`. Direct simulation
  confirms this literally, with **zero exceptions** among all 13 sampled
  `A'`-occurrences and all 180 sampled `B'`-occurrences up to `n=8000`
  (script `/tmp/round-18/sim_crux3.py`).
- `a_1=11305`, `S_0=\{2,3,5,7,13,17,19,23,29,37,43,101\}`, `A'=\{2,5\}`
  (`n_A=7`), `B'=\{3,7\}` (`n_B=4`). Here the canonical witness `n_B=4` is
  already singleton, `F''_4=\{11\}` (matching
  `approaches/cofinite-window-capacity-bound.md`'s recorded data), giving
  `x_1:=4`. For the other side, index `x_2=103` (an `A'`-occurrence) has
  `P(a_{103})\setminus S_0=\{11\}` exactly (23 of the sampled `A'`-
  occurrences below `n=8000` have this exact singleton signature; the
  earliest is `x_2=103`). Applying the Theorem with `q=11`: `11\mid a_n` for
  every `B'`-occurrence `n>4` (already known, this is the canonical
  Singleton-Side FAH direction) **and** `11\mid a_n$ for every `A'`-
  occurrence `n>103`. Direct simulation again confirms zero exceptions among
  all 247 sampled `A'`-occurrences and all 79 sampled `B'`-occurrences up to
  `n=8000` (script `/tmp/round-18/sim_11305.py`).

Both of the workspace's only two known properly-recruited-core rogue-pair
seeds are fully explained (their FAH is literally, not just cofinitely,
resolved once the finitely many pre-`x_1`/pre-`x_2` occurrences are set
aside) by this Theorem — a positive structural finding, not previously
recorded in this form anywhere in the workspace.

### §4. What remains open (the honest residual gap)

The Two-Sided Singleton Witness Theorem is a **sufficient condition**, fully
proved, but its **hypothesis is an existence claim** — that some occurrence
of `B` and some occurrence of `A` each happen to have out-of-core signature
reduced to the *same* singleton `\{q\}` — that is **not proved in general**.
Concretely:

1. **No proof that such a matching pair of singleton witnesses always
   exists** for an arbitrary rogue pair `(A,B)`. This is a different,
   though related, question from the original FAH crux; it is a purely
   arithmetic statement about the occurrence sequence `(P(a_x)\setminus
   S_0)_{x\in X_B}` (resp. `X_A`) eventually taking the value `\{q\}` for
   some `q` shared across both sides — genuinely narrower and more concrete
   than literal FAH itself (it does not follow automatically from FAH, since
   FAH only needs `q` to *divide* each `a_x`, not to be the *only*
   out-of-core prime of `a_x`), so it is not a restatement of the original
   open problem, but it is also not established here.
2. Both computational witnesses found in §3 were located by a finite scan
   (`N\le8000`); no general mechanism (density, pigeonhole, or otherwise) is
   given here for why such an occurrence must appear, or how far out it must
   be sought, for a general rogue pair.
3. Even a complete proof of H1/FAH (whether via this Theorem or another
   mechanism) would still leave H2 (absorption-chain termination) open —
   this approach does not touch H2, consistent with its scope as declared in
   the outline.

**Honest verdict (round 18).** This round replaced one dead mechanism (the
outline's originally proposed triangle/`e`-based forcing, now proved
structurally incapable of working — §2) with a different, fully proved
*sufficient* mechanism (§3) that correctly and completely explains both of
the workspace's known hard test instances, but whose own hypothesis (matching
singleton witnesses) is a new, narrower, still-open existence question, not
yet reduced to something provable from the certified lemma stack. This is
genuine forward progress (two new certified/certifiable results, and a
sharper, more concrete open question replacing a dead one) but it does not
close H1 in general. Status remains `partial`.

### §5. Round 19: attempt to close the existence hypothesis via anatomy-of-
integers/density, and the obstruction found

**§5.1. Elementary bound on `ω(a_n)` — proved in full (the outline's Step 2).**

*Claim.* For every `n \ge 1`, `\omega(a_n) \le \log_2 a_n` (where `\omega(m)`
denotes the number of distinct prime factors of `m`), and consequently, by the
certified Bounded Gap Lemma (`a_n \le n\cdot a_1`), `\omega(a_n) \le \log_2 n +
\log_2 a_1`, i.e. `\omega(a_n)` grows at most logarithmically in `n`.

*Proof.* Write `a_n = p_1^{e_1}\cdots p_k^{e_k}` with `k=\omega(a_n)` and each
`p_i \ge 2, e_i\ge 1`. Then `a_n = \prod_i p_i^{e_i} \ge \prod_i p_i \ge
\prod_i 2 = 2^k`, using `p_i\ge 2` and `e_i \ge 1$ for the first inequality
and `p_i \ge 2$ for the second. Hence `2^k \le a_n`, i.e. `k \le \log_2 a_n`.
Substituting the certified Bounded Gap Lemma's bound `a_n\le n\cdot a_1$
(`lemmas/bounded-gap-lemma.md`) gives `\omega(a_n)\le\log_2(n\cdot a_1) =
\log_2 n+\log_2 a_1`. $\blacksquare$

This is fully elementary (no PNT, no analytic number theory needed) and
fully rigorous. It confirms the outline's Step 2 qualitatively (out-of-core
cofactors cannot have more than `O(\log n)` prime factors), but — and this
must be stated plainly — **this upper bound gives no lower bound whatsoever
on how often `\omega` of the out-of-core cofactor equals exactly 1**. A
sequence of integers each satisfying `\omega(m)=O(\log m)` can consistently
have `\omega(m)\ge 2` for every single term (e.g. `m=6,30,210,\dots$ product
of first `k` primes never has `\omega=1$ for `k\ge2`) — so this bound is
necessary-but-nowhere-near-sufficient background, not progress toward Step 3.

**§5.2. Extended computational check (mandated pre-build check, per the
outline-reviewer's gate condition) — counts keep growing, not proof of
infinitude.**

Re-simulated both known hard seeds at their properly-recruited cores (trial
division, `math.gcd`, `sympy.factorint` for the singleton test only — scripts
preserved at `/tmp/round-19/sim_growth2.py`, `/tmp/round-19/sim_growth3.py`),
doubling the window used by this round's math-explorer to check for a
plateau (a real risk flagged by the outline: "low rate but growing count is
mild evidence, not proof"):

- `a_1=4807`, `S_0=\{2,3,5,11,19,23\}`: type `A'=\{3,5,19\}` — window 6000:
  10 occurrences, 7 singleton (all `q=17`); window 12000: 19 occurrences, 9
  singleton (still all `q=17`). Type `B'=\{2,11\}` — window 6000: 136
  occurrences, 18 singleton (`q=17`); window 12000: 272 occurrences, 23
  singleton (`q=17`).
- `a_1=11305`, `S_0=\{2,3,5,7,13,17,19,23,29,37,43,101\}`: type `A'=\{2,5\}`
  — window 4500: 136 occurrences, 15 singleton (`q=11`); window 9000: 277
  occurrences, 24 singleton (`q=11`). Type `B'=\{3,7\}` — window 4500: 45
  occurrences, 8 singleton (`q=11`); window 9000: 90 occurrences, 12 singleton
  (`q=11`).

In every one of these four (seed, side) combinations, doubling the window
roughly doubled both the occurrence count and the singleton count, i.e. the
*absolute count* of singleton occurrences keeps growing with no sign of
plateauing, and the singleton *rate* (already reported by this round's
explorer as low, 6–17% in this data) stays roughly stable rather than
decaying toward zero. **This is consistent with, but does not prove,**
infinitely many singleton occurrences on each side (with the *same* prime
`q` recurring every time it was observed in this data, which is itself
notable but is only two data points' worth of `q`, not a proof that `q` must
recur or that some `q` must exist for an arbitrary rogue pair). No
counterexample (a rogue pair where singleton occurrences stop appearing
entirely past some point) was found in any window tested to date, on either
seed.

**§5.3. Why the proposed sieve/anatomy-of-integers mechanism cannot be
carried out — the precise obstruction (the round's genuine negative
finding).**

The outline's Step 3 asks for a rigorous **existence** (or, as a first goal,
**infinitely-often**) statement: for `n` ranging over the persistent-type
index set `X_A`, the out-of-core cofactor `w_n := a_n / \prod_{p\in
A}p^{v_p(a_n)}$ (a positive integer coprime to every prime of `S_0`) is prime
for infinitely many `n\in X_A`. The intended technique is a Brun/Selberg-
sieve-style (or Hardy–Ramanujan/Erdős–Kac normal-order-style) lower bound for
"almost-primes"/primes in a constrained integer sequence.

**Every sieve technique of this kind that exists in the literature (and none
were found in `knowledge_base.md` or the crux corpus applicable here — see
this round's math-explorer report) requires the target sequence to be given
explicitly**, typically as the range of a fixed polynomial or linear form
`f(n)` in the index `n` (e.g. Chen's theorem: `2n+1` has at most two prime
factors infinitely often; Brun's theorem on twin primes: `n` and `n+2`). The
reason is structural, not a matter of technique-choice: to run the
sieve's inclusion–exclusion (Legendre/Brun/Selberg combinatorial identity),
one must, for **every** prime `p` up to the sieve level `z`, compute or
tightly bound the count `\#\{n\le N : p\mid f(n)\}` — usually by an exact
residue-class count (`f(n)\equiv 0 \pmod p$ has a fixed, computable number of
solutions mod `p`, independent of `N`, giving density `\approx \rho(p)/p`)
and, crucially, these counts for **different** primes `p,p'` must combine
multiplicatively/independently (a CRT-type hypothesis: the events `p\mid
f(n)$ and `p'\mid f(n)$ are "independent" across residue classes mod
`p\cdot p'`), which again requires the explicit algebraic form of `f`.

**Neither `X_A` nor `w_n` has this structure here.** Concretely:

1. `X_A = \{n : \rho(n)=A\}` is defined only via the entire greedy legality
   history up to index `n` (the type `\rho(n)` depends on which primes of
   `S_0` happen to divide `a_n`, itself the output of the recursive
   minimality rule applied to *all* of `a_1,\dots,a_{n-1}`). There is no
   known closed-form membership test for `X_A` as a function of `n` alone
   (e.g. no arithmetic progression, no polynomial congruence) — it is only
   known to be infinite (certified, Extended Persistent-Type Pigeonhole) and
   to satisfy the Bounded Gap Lemma's linear growth ceiling, neither of which
   supplies a residue-class or CRT-independence structure.
2. Even restricting attention to a single fixed `n\in X_A`, whether a
   candidate prime `p\notin S_0` divides `w_n` (equivalently `a_n`) is not
   governed by a fixed residue-class rule in `n`: it depends on whether `p`
   was already "used up" as a legality witness for some earlier index, or
   whether a different prime supplied the required `\gcd>1$ at that step —
   an intrinsically *adaptive*, path-dependent phenomenon (this is exactly
   the mechanism behind the certified Generalized Class-Blindness Obstruction
   cited by this round's `n1-periodicity-reconciliation` approach: the
   recursion only ever consults the *Boolean* legality predicate, never a
   fixed residue class, so there is no external arithmetic-progression handle
   on divisibility by a specific outside prime). **Note carefully**: that
   Obstruction is about statistics computed from the Boolean legality
   history, and does not literally forbid asking an anatomy-of-integers
   question about the actual *value* `a_n` (this is why the outline's premise
   — that this proof style falls outside that Obstruction's scope — is
   correct, and is reaffirmed here). But the present difficulty is a
   *different*, equally fatal one: it is not that the question is
   "information-theoretically" blocked, but that **no existing sieve/
   density technique has any entry point into a sequence with no explicit
   formula and no independently verifiable local densities** — the
   machinery's own hypotheses (an explicit polynomial or linear form, or at
   minimum a sequence with provably CRT-independent local densities at each
   prime) are simply not satisfied, and nothing in this round's search (of
   `knowledge_base.md`, the crux corpus, or elementary first-principles
   attempts) produces a substitute route to the needed local-density
   estimates for an implicitly/adaptively-defined recursive sequence like
   `(a_n)`.
3. As a further, independent check: I looked for a purely *elementary*
   (non-sieve) combinatorial argument specific to this recursion's
   minimality rule that might force singleton cofactors without needing
   density/CRT machinery at all (e.g. some direct argument from "`a_n` is
   the *smallest* legal successor" that bounds `\omega(w_n)`) — the
   minimality rule only ever certifies that `a_n$ is the least integer
   `>a_{n-1}$ satisfying finitely many `\gcd>1` congruence conditions
   (against `a_1,\dots,a_{n-1}`); minimality of an integer subject to
   congruence constraints gives no control on that integer's number of
   *other* prime factors (the smallest integer satisfying a set of "must
   share a factor with X" conditions can equally well be prime, or have
   many prime factors, depending on which residues are excluded) — no such
   argument was found, and none is claimed.

**Conclusion.** The weaker "infinitely often" sub-target (let alone the
existence hypothesis in full, let alone the further "shared `q` across both
sides" third pigeonhole layer of Step 5) is **not established this round**.
The obstruction is precise and reusable for future rounds: *any* future
attempt at this Density/Occurrence Lemma must first supply an explicit
description (or at least a rigorously-derived independent local-density
estimate) of the out-of-core cofactor sequence along a persistent-type index
set — something no technique currently in the workspace, `knowledge_base.md`,
or the searched crux corpus provides, and which may be fundamentally
unavailable given the recursion's genuinely adaptive, non-explicit
definition. This should be recorded as a **confirmed obstruction** for the
sieve/anatomy-of-integers proof *style* specifically (as distinct from, and a
complement to, the already-certified Generalized Class-Blindness Obstruction
for the *statistical* proof style) — future rounds should not re-attempt a
sieve/density argument on this construction without first resolving point 1
or 2 above (an explicit reformulation of `X_A$ or `w_n`), which appears to be
a genuinely hard, possibly open, sub-problem in its own right.

**Honest verdict (round 19).** No progress toward closing the existence
hypothesis was achieved beyond (a) a correct but insufficient elementary
bound, (b) further (still finite, non-conclusive) computational support, and
(c) a precisely identified and documented reason the mandated proof style
cannot currently be carried out. This is reported as genuine negative
information, not a stall to be silently retried: the anatomy-of-integers/
sieve route, as specified by the outline, requires an ingredient (an
explicit or CRT-tractable description of the recursively-defined out-of-core
cofactor sequence) that does not exist in the current toolkit and was not
producible from first principles this round. Status remains `partial`; H1
remains open via this approach.

### §6. Round 20: the "Constrained Singleton Coherence" reframing of the
existence hypothesis — proved in full where it is unconditional, and a
precise account of why the residual existence question still does not close

**Setup recap.** Fix a rogue pair `(A,B)` at core `S_0`, a witness
`m_A\in X_A`. By §1 (Double-Witness Nested Pigeonhole, using only the first
of its two passes here) there is an infinite `X_B^{(0)}\subseteq X_B` and an
integer `d^*=\gcd(a_{m_A},a_x)` for every `x\in X_B^{(0)}$, with
`1<d^*\mid b_{m_A}:=\prod_{p\in F'_{m_A}}p^{v_p(a_{m_A})}` and every prime
factor of `d^*` confined to `F'_{m_A}:=P(a_{m_A})\setminus S_0` (Confined-GCD
Lemma, `lemmas/confined-gcd-lemma.md`). This part is already fully certified
(§1); the new content this round is entirely in §6.1–§6.4 below.

**§6.1. Constrained Singleton Coherence Lemma — proved in full (new,
unconditional).**

**Statement.** Fix `m_A\in X_A` and the induced infinite class
`(d^*,X_B^{(0)})` as above. Suppose `x\in X_B^{(0)}` is itself a *singleton*
occurrence, i.e. `P(a_x)\setminus S_0=\{q_x\}` for some prime `q_x`. Then
`d^*=q_x^{\,j}` for some `j\ge1` (in particular `d^*` is a prime power, and
its prime is `q_x`).

**Proof.** By definition `d^*=\gcd(a_{m_A},a_x)`, so `d^*\mid a_x`. Write
`a_x=\left(\prod_{p\in S_0}p^{v_p(a_x)}\right)\cdot q_x^{\,v_{q_x}(a_x)}`,
which is exactly the prime factorization of `a_x$ split into its `S_0`-part
and its outside-core part, the latter being a pure `q_x`-power because
`P(a_x)\setminus S_0=\{q_x\}` by hypothesis (i.e. `a_x` has *no* outside-core
prime other than `q_x`). Every prime factor of `d^*` lies outside `S_0` (this
is the confinement half of the Double-Witness Nested Pigeonhole Lemma, §1,
itself proved via the Confined-GCD Lemma), so every prime factor of `d^*` is
a prime factor of `a_x` lying outside `S_0`, hence equals `q_x` (the only
such prime, by the singleton hypothesis on `x`). A positive integer all of
whose prime factors equal a single fixed prime `q_x` is `q_x^{\,j}` for some
`j\ge1$ (`j\ge1$ since `d^*>1`, established in §1). `\blacksquare`

**§6.1(a). Composite-Exclusion Corollary — proved (new, unconditional,
immediate contrapositive).** If `d^*` has two or more distinct prime factors
(i.e. `d^*` is *not* a prime power), then `X_B^{(0)}` contains **zero**
singleton occurrences of `B` — no `x\in X_B^{(0)}` can satisfy
`P(a_x)\setminus S_0=\{q_x\}` for any prime `q_x`, since Constrained
Singleton Coherence would then force `d^*` to be a prime power, contradicting
the hypothesis. *Proof.* Direct contrapositive of §6.1; no further argument
needed. `\blacksquare`

**§6.1(b). Prime-Power Coherence Corollary — proved (new, unconditional,
immediate).** If `d^*=q^{k}` for a single prime `q$ and integer `k\ge1`, then
every singleton occurrence `x\in X_B^{(0)}` (if any exists) automatically has
`q_x=q` — no separate search over which prime a hypothetical singleton in
`X_B^{(0)}` might carry is needed; the class `d^*` itself already pins the
prime. *Proof.* By §6.1, `d^*=q_x^{\,j}` for the singleton's own prime `q_x`;
since also `d^*=q^k` by hypothesis and both are prime-power factorizations of
the same positive integer, unique factorization forces `q_x=q` (and `j=k`).
`\blacksquare`

These three statements are exactly the outline's Step 3, now given complete,
citation-backed proofs (the outline-reviewer had already hand-verified the
mechanism informally; this closes it to the rigor bar — every step traced to
Confined-GCD, §1, and elementary unique factorization, with no appeal to any
open hypothesis).

**§6.2. Why the round's positive computational evidence for "some `m_A`
gives a prime-power `d^*`" is a confound, not independent support — a new
diagnostic finding, proved in full for the two available test seeds.**

*Computation performed this round* (script `/tmp/round-20/analyze2.py`,
`/tmp/round-20/analyze3.py`, data cached in `/tmp/round-20/data_4807.pkl`,
`/tmp/round-20/data_11305.pkl`; re-derives the sequence and its factorizations
from scratch by direct greedy simulation, `math.gcd`, and `sympy.factorint`,
independent of any prior round's cached numbers). For the seed `a_1=4807`
(`S_0=\{2,3,5,11,19,23\}`, `A'=\{3,5,19\}`, `B'=\{2,11\}`, window `N=8000`,
`|X_{A'}|=13`, `|X_{B'}|=180`): for **every one** of the 13 choices of
`m_A\in X_{A'}` and every one of the 180 choices of `m_B\in X_{B'}` (i.e. both
the `m_A`-vs-`X_{B'}` direction and the symmetric `m_B`-vs-`X_{A'}`
direction), the dominant (largest) pigeonhole class's value `d^*` is a prime
power — in fact literally `d^*=17` (exponent 1) in every single one of the
`13+180=193` cases tested. Identically for `a_1=11305`
(`S_0=\{2,3,5,7,13,17,19,23,29,37,43,101\}`, `A'=\{2,5\}`, `B'=\{3,7\}`,
`|X_{A'}|=247`, `|X_{B'}|=80`): `d^*=11` in every one of the
`247+80=327` cases. Zero exceptions across all `193+327=520` witnesses
tested on both seeds and both directions.

**Claim.** This "always prime power" pattern on both seeds is **fully
explained by, and gives no information beyond**, the fact — already
established independently in §3 (Two-Sided Singleton Witness Theorem's
verification), via a wholly different mechanism (locating one already-
singleton occurrence on each side) — that both pairs already have a single
globally-recurring companion prime (`q=17` resp. `q=11`) known to divide
*almost every* occurrence of both types. It is **not** independent evidence
that the general existence conjecture (§4 point 1 / outline Step 4) holds
for an arbitrary rogue pair where no such global witness prime has yet been
found by any other means.

**Proof of the claim (concrete mechanism, exhibited on both seeds).** Fix a
witness `m_B\in X_{B'}` whose own outside-core set is *not* itself a
singleton (`|F'_{m_B}|\ge2$; such witnesses exist and were sampled directly —
e.g. for `a_1=4807`, `m_B=7` has `F'_7=\{17,13\}`; for `a_1=11305`,
`m_B=119` has `F'_{119}=\{11,53\}`). Computing the pigeonhole classes of
`\gcd(a_{m_B},a_x)` for `x\in X_{A'}` explicitly (data reproduced in
`/tmp/round-20/analyze4.py`'s output) gives, in every sampled case, exactly
two nonempty classes: `d^*=q` (the recurring prime alone) with a LARGE count
(11–12 out of 13 for `a_1=4807`; 241–243 out of 247 for `a_1=11305`), and
`d^{**}=q\cdot r` for the *companion* prime `r` (`13,7,29` for `4807`;
`53,59,61,67,71` for `11305`) with a SMALL count (1–2 out of 13; 4–6 out of
247). The reason is structural, not accidental: `q` (`17` resp. `11`) is
already known, by the independently-established §3 Theorem, to divide *every*
occurrence of `A'` past a fixed finite threshold — so `q\mid a_x` for
literally all but finitely many `x\in X_{A'}`, which by itself already forces
`\gcd(a_{m_B},a_x)` to be a multiple of `q` for all but finitely many `x`,
*regardless of any property of the pigeonhole mechanism proposed in this
approach*. The companion prime `r`, by contrast, is not shown (and in the
sampled data is not observed) to be a recurring feature of `A'`'s occurrence
sequence at all — it divides only the handful of `x\in X_{A'}` for which it
happens, by ordinary coincidence, to also divide `a_x` — so the composite
class `\{q\cdot r\}` stays a small, bounded (not window-growing) minority
while the singleton-prime class `\{q\}` absorbs virtually all of `X_{A'}`.
Consequently the dominant class is a prime power **because `q` was already
known, from an unrelated mechanism, to be a near-universal divisor of the
far side** — the pigeonhole/Constrained-Singleton-Coherence machinery
introduced in this approach contributes nothing to *establishing* this; it
merely re-observes it. This is the same shape of confound as the
already-certified Same-Type Triangle Vacuity finding (`lemmas/same-type-
triangle-vacuity.md`): a computation that looks like a "hit" for a proposed
new mechanism turns out, on inspection, to be fully accounted for by an
independent, previously-established fact. `\blacksquare`

**Consequence.** Because the *only* two available hard test instances both
already have their Cofinite-FAH witness prime established by an unrelated
route (§3) before this round's mechanism is ever applied to them, they
cannot serve as an unconfounded test of the general existence conjecture (the
outline's Step 4: "for SOME rogue pair with no witness prime otherwise known,
some `m_A`'s dominant class is a prime power"). A genuine test requires a
rogue pair where no such prime is already known by any other means; §6.3
reports this round's (unsuccessful) attempt to locate one.

**§6.3. Attempted construction of a genuinely independent (non-confounded)
test instance — failed, honestly reported.**

To test the sharpened conjecture without the §6.2 confound, this round
attempted to locate a **new** properly-recruited-core rogue pair (beyond the
two already on record) by implementing a heuristic core-recruitment
procedure: starting from `S=Q:=P(a_1)`, repeatedly (i) simulate the sequence
to a finite window `N`, (ii) find `S`-extended types occurring at least
`min_occ` times with last occurrence past `N\cdot\text{tail\_frac}` of the
window (a proxy for "persistent"), (iii) for each such type's earliest
occurrence `m`, add `P(a_m)\setminus S` to `S`, and (iv) iterate until `S`
stabilizes or an iteration cap is hit (script `/tmp/round-20/recruit.py`).

**Result: this heuristic fails to reproduce the workspace's own documented
recruited cores.** Run on the two known seeds (with `N=6000`, `min\_occ=8`,
`tail\_frac=0.6`, 6 iterations), it does **not** converge to the recorded
`S_0=\{2,3,5,11,19,23\}$ (`a_1=4807`) or `S_0=\{2,3,5,7,13,17,19,23,29,37,43,
101\}` (`a_1=11305`) — instead it grows unboundedly within the iteration cap,
recruiting many more primes (17 for `4807`, 41 for `11305`, both far beyond
the documented sets). This shows the heuristic's finite-window "occurs
`\ge8` times with a late last occurrence" proxy for persistence is not
faithful to the workspace's actual notion (certified via the Extended
Persistent-Type Pigeonhole threshold `N(S)`, not a heuristic frequency cutoff)
— it over-recruits, likely by treating window-boundary-truncated finite
patterns as persistent types. **Consequence.** The ~70 candidate seeds this
heuristic flagged as having `|F'|,|F''|\ge2$ at *raw* `Q`-level (found by a
broad scan over products of 2–3 primes up to `6000`, script
`/tmp/round-20/search_seeds.py` — genuinely new data, not previously recorded
in the workspace) are **not** validated as *properly-recruited-core* hard
instances, since the recruitment step used to promote a raw-`Q`-level
candidate to the "hard" regime (required by this round's dispatch, and by
the outline-reviewer's insistence in round 18/19 that raw-`Q`-level non-
singleton cases are the "easy," already-covered regime) is not faithfully
implemented here. **This is reported honestly as a failed replication, not a
new positive result**: no new independently-testable hard seed was obtained
this round, and the ~70 raw candidates should not be treated as evidence for
or against the sharpened conjecture without a correct recruitment procedure
applied to them first (left as an explicit task for a future round, distinct
from — and prerequisite to — actually testing Step 4 of the outline without
the §6.2 confound).

**§6.4. Does the sharpened existence question evade the round-19 sieve/
anatomy-of-integers obstruction? No — a precise reduction argument.**

**Claim.** Proving, for an arbitrary rogue pair `(A,B)` with no independently
known Cofinite-FAH witness, that *some* `m_A\in X_A` induces a prime-power
dominant pigeonhole class `d^*$ populated by infinitely many `x\in X_B`
sharing that exact class, is **not easier in kind** than the original
existence hypothesis of the Two-Sided Singleton Witness Theorem — it requires
the same missing ingredient identified in §5.3 (an explicit or CRT-tractable
description of the implicitly/adaptively-defined out-of-core cofactor
sequence along a persistent-type index set).

**Argument.** By §6.1(b) (Prime-Power Coherence), once *some* `m_A` is found
with prime-power dominant class `d^*=q^k`, EVERY singleton occurrence that
might exist in the induced class `X_B^{(0)}` is automatically known to carry
that same prime `q` — this is a genuine simplification of the *search*
(the outline's original motivation for the reframing: it removes the need to
separately verify prime-matching once a singleton is found). But it does
**not** remove the need to show a singleton actually occurs somewhere in
`X_B^{(0)}$ (the outline's own Step 4(ii), explicitly flagged as separate
from 4(i) and not conflated here) — and, more fundamentally, it does not
supply any new *mechanism* for locating an `m_A` whose class is a prime
power in the first place when no witness prime is already known. Concretely:
the pigeonhole class `d^*(m_A)` is, by construction (§1), an *emergent*
property of the joint occurrence pattern of `F'_{m_A}`'s primes across the
implicitly/adaptively-defined index set `X_B` — exactly the same object
(the co-occurrence statistics of out-of-core primes along a persistent-type
index set of the recursive sequence `(a_n)`) that §5.3 already proved is not
reachable by any known sieve/density/anatomy-of-integers technique, because
`X_B` and the divisibility pattern of `a_x` by primes outside `S_0` have no
closed form and no independently verifiable local density at any prime.
Asking "does `d^*(m_A)` collapse to a prime power for some `m_A`" is a
*reformulation* of "does one out-of-core prime dominate the co-occurrence
pattern," which is the same order of difficulty as (indeed, essentially
equivalent to, via §6.2's own mechanism) the original "does some prime `q`
divide cofinitely many occurrences of both types" question that Cofinite FAH
already asks — the reframing changes the *bookkeeping* (which divisor-class
lens to search through) but not the underlying missing ingredient (a way to
control which out-of-core prime, if any, ends up recurring). This is
confirmed empirically by §6.2: on the only two seeds where the sharpened
question was checkable, its truth followed immediately, for free, once the
original Cofinite FAH witness was already known by an unrelated route — and
no case is known (nor could be constructed this round, §6.3) where the
sharpened question was resolved *before*, or *independently of*, resolving
the original one.

**Honest verdict (round 20).** The Constrained Singleton Coherence Lemma and
its two corollaries (§6.1) are new, fully proved, unconditional, reusable
content — a genuine (if modest) sharpening of the search apparatus around
the Two-Sided Singleton Witness Theorem. But the round's deeper
investigation (§6.2–§6.4) shows this sharpening does **not** constitute
progress toward closing the existence hypothesis in general: the positive
computational signal it produces on the only available test data is a
confound (§6.2), a genuinely new and independent test instance could not be
constructed this round (§6.3), and a structural reduction argument (§6.4)
gives a precise reason to expect the sharpened question is no easier than
the original one, both ultimately blocked by the same implicit/adaptive-
sequence obstruction already identified and certified in round 19 (§5.3).
Status remains `partial`; H1 remains open via this approach. This should be
read as a genuine negative/diagnostic contribution (three new proved facts:
§6.1's lemma+corollaries, §6.2's confound diagnosis, §6.4's reduction
argument), not a "no progress" round, but it does not move the approach
closer to `solved`.

## Promotable lemmas

- **Double-Witness Nested Pigeonhole Lemma** (§1 above, fully proved,
  unconditional). Two sequential finite-pigeonhole passes, on two distinct
  fixed witnesses of a persistent type `A`, against a shrinking infinite
  subset of a disjoint type `B`'s occurrence set, always succeed, with both
  resulting gcd-values confined (via a two-fold application of the certified
  Confined-GCD Lemma) to the respective witness's fixed finite out-of-core
  prime set. Reusable building block for any future double- or multi-witness
  FAH attack.

- **Same-Type Triangle Vacuity** (§2 above, fully proved, unconditional
  negative result). For any two occurrences `m_A,m_A'` of the same
  persistent type `A`, `\gcd(a_{m_A},a_{m_A'})` carries no information about
  `(P(a_{m_A})\setminus S_0)\cap(P(a_{m_A'})\setminus S_0)` beyond what is
  already forced by `A`'s own in-core primes — because Free Facts' `>1`
  conclusion for this pair is already fully explained by `A\subseteq
  P(a_{m_A})\cap P(a_{m_A'})`. This forecloses, in general (not just for
  this problem's specific triangle-consistency outline), any future attempt
  to extract outside-core linking information from a same-type pair's gcd —
  a genuine, reusable negative/diagnostic result, matching the spirit of the
  workspace's other certified "obstruction" write-ups (Escape-Cost Vacuity,
  Growing-Constraint Obstruction).

- **Two-Sided Singleton Witness Theorem** (§3 above, fully proved,
  conditional on an explicit, precisely-stated existence hypothesis). If a
  rogue pair `(A,B)` has *some* occurrence of `B` and *some* occurrence of
  `A` (not necessarily the earliest of either) whose out-of-core prime sets
  both reduce to the same singleton `\{q\}`, then Cofinite FAH holds for
  `(A,B)` with witness `q`. A genuine two-witness generalization of the
  already-certified Singleton-Side FAH Lemma (which only uses the canonical
  witness on one side); reusable by any future approach that can supply or
  bound such witnesses.

- **Elementary `ω(a_n) = O(\log n)` Bound** (§5.1 above, fully proved,
  unconditional). For every `n`, `\omega(a_n)\le \log_2 a_n$, hence (via the
  certified Bounded Gap Lemma) `\omega(a_n)\le \log_2 n + \log_2 a_1`. Purely
  elementary (`m\ge 2^{\omega(m)}`, no PNT needed); reusable whenever a future
  approach needs a crude a priori cap on the number of distinct prime
  factors of a term of this sequence. Note its scope is limited — it is an
  upper bound only, and does not by itself yield any lower bound on the
  frequency of singleton (`\omega=1$-on-the-out-of-core-part) occurrences.

- **Sieve/Anatomy-of-Integers Style Obstruction for the Recursive Sequence
  `(a_n)`** (§5.3 above, a documented negative finding, not a theorem in the
  usual sense but a precisely-stated methodological obstruction). Every known
  sieve technique (Brun, Selberg) or normal-order density result requires the
  target integer sequence to be given by an explicit closed-form expression
  in the index (typically a polynomial/linear form) with independently
  computable, CRT-combinable local densities at each prime. The persistent-
  type index set `X_A` and the out-of-core cofactor `w_n` in this problem are
  defined only implicitly/adaptively via the full history of the greedy
  legality recursion, with no known closed form and no independent local-
  density control at any prime outside the core `S_0`. Hence no currently
  existing sieve/density technique has an entry point into this sequence.
  This is a genuine, reusable diagnostic for future rounds: it precisely
  explains why the "weaker infinitely-often" sub-target could not be closed
  this round, and flags that resolving it first requires either (i) an
  explicit reformulation of `X_A`/`w_n`, or (ii) a fundamentally different,
  non-sieve technique — neither of which is currently available.

- **Constrained Singleton Coherence Lemma, with Composite-Exclusion and
  Prime-Power Coherence Corollaries** (§6.1 above, fully proved,
  unconditional). Fix a rogue pair `(A,B)`, a witness `m_A\in X_A`, and the
  induced infinite constant-gcd class `(d^*,X_B^{(0)})` from the (already
  certified) Double-Witness Nested Pigeonhole Lemma's first pass. If some
  `x\in X_B^{(0)}` is a singleton occurrence (`P(a_x)\setminus S_0=\{q_x\}`),
  then `d^*=q_x^{\,j}` for some `j\ge1` — a direct consequence of Confined-
  GCD plus unique factorization. Corollaries: (a) Composite-Exclusion — a
  `d^*` with `\ge2` distinct prime factors provably contains zero singleton
  occurrences in its class; (b) Prime-Power Coherence — a prime-power `d^*=
  q^k` automatically pins any singleton in its class to prime `q`, no
  separate prime-matching search needed. Reusable as a search-pruning tool
  by any future approach that pigeonholes `\gcd` values against a fixed
  witness.

- **Dominant-Class Confound Diagnostic** (§6.2 above, fully proved for both
  available hard test seeds, a negative/diagnostic finding in the style of
  the certified Same-Type Triangle Vacuity result). If a rogue pair `(A,B)`
  already has an independently-established Cofinite-FAH witness prime `q`
  (by any mechanism, e.g. the Two-Sided Singleton Witness Theorem), then for
  ANY witness `m_B` with `q\in F'_{m_B}`, the dominant pigeonhole class of
  `\gcd(a_{m_B},a_x)` over `x` of the disjoint type is automatically a prime
  power (namely a power of `q`) for a purely downstream reason — `q` already
  divides all but finitely many `x` of that type, while any other prime of
  `F'_{m_B}` need not recur and so contributes only a bounded, non-dominant
  sub-class. Consequently, verifying "the dominant class is a prime power"
  on a rogue pair that already has a known witness prime supplies **zero**
  independent evidence toward the general (witness-prime-unknown) existence
  conjecture. Reusable as a standing screening check: before treating any
  future "dominant class is a prime power" computation as support for a
  conjecture, first verify the tested pair's Cofinite-FAH witness is not
  already independently known — otherwise the check is confounded by
  construction.
