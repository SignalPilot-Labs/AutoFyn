## imo-2026-03 (lens: front 1 / Claim B, p3-cut branch + n=3 boundary bug)

### Item 2 (cheap): rank-pigeonhole-budget's n=3 middle-band v2=p4 boundary bug — precise fix

Location: `current.md` round-19 review paragraph (lines ~1498-1522) describing
rank-pigeonhole-budget's Truncated Alternating Sum Ceiling + n=3 middle-band
closure (the underlying claim itself lives in the approach file's n=3
case-split on v2 vs p3, p4; the approach file itself does not yet show the
corrected boundary — the bug is only documented in the reviewer's current.md
paragraph, so the fix needs to be applied to the approach file's own proof).

**Exact bug.** The proof's case split treats "$v_2 \le p_4$" as one case,
computing $\tau_{>v_2} = \{p_3,p_4\}$ (claiming both pieces "exceed" $v_2$).
But $A(S_{>v})$ is defined with a **strict** inequality (rank-truncation by
value **strictly greater than** $v$, per every other lemma in the file, e.g.
`truncated-alternating-sum-floor`/`-ceiling`, Theorem 35's own $\epsilon(v)$
convention). At the single point $v_2=p_4$ exactly, $p_4$ is NOT $>v_2$, so
$p_4\notin\tau_{>v_2}$ and the correct value is $\tau_{>v_2}=\{p_3\}$, giving
$\Delta=-3f(3)$, not the stated $-f(3)$.

**Why it's non-fatal (already checked by round-19's reviewer).** The wrong
value $-f(3)$ is algebraically *larger* than the true value $-3f(3)$
(since $f(3)>0$), so the case as originally written proves the target
inequality for a value stronger than what's actually needed at that one
point — i.e. the theorem's conclusion still holds there, just via a
one-point-wrong intermediate computation. The reviewer independently
re-verified the true inequality holds exactly at $v_2=p_4$ too.

**Precise, scoped fix (should be quick, no new mechanism):**
1. Change the case split boundaries from $v_2\in[0,p_4]$ (closed) vs.
   $v_2\in(p_4,p_3)$ (open) to $v_2\in[0,p_4)$ (open on the right) vs.
   $v_2\in[p_4,p_3)$ (closed on the left) — i.e. move the single boundary
   point $v_2=p_4$ from the first case into the second case, matching the
   strict-inequality convention $\tau_{>v_2}$ uses everywhere else in the
   file.
2. Re-verify the second case's existing algebra (already written for the
   open interval $(p_4,p_3)$, where $\tau_{>v_2}=\{p_3\}$) is literally
   unchanged by including the left endpoint $v_2=p_4$ — this should be
   automatic since the case's formula for $\Delta(3,v_2)$ as a function of
   $v_2$ is a single continuous closed-form expression on the whole
   interval $[p_4,p_3)$, not something that behaves differently exactly at
   the left endpoint (the reviewer's spot check at $v_2=p_4$ already
   confirms the target inequality holds there under the corrected value).
3. Delete/replace the erroneous $v_2=p_4$ computation in the first case
   with a boundary note ("$v_2=p_4$ is handled by the next case").
No new inequality, no new induction — purely a one-point case-boundary
relabeling plus copying the adjacent case's already-correct algebra to that
point. Should not require re-deriving anything from scratch. Recommend the
builder do this fix in the approach file itself (not just current.md) since
the approach file is the source of truth the ranker reads.

### Item 1: does the p3-is-cut branch need new machinery, or does it extend?

**Diagnosis: it is a recursive re-instantiation of the SAME open Claim-B
machinery one level down (n-2), not a genuinely new type of obstruction —
same pattern as the historical "p2-cut" self-similarity finding (round 10,
rule #15: "the resulting sub-instance is literally self-similar to the
ORIGINAL problem one level down… flag it as requiring the FULL inductive
hypothesis at the smaller level, not just the branch already closed").**

Tracing through Theorem 35's own Case (b) setup (`greedy-halving-adversary.md`
lines 3950-3992): $R'=\{a,b\}\cup T'$ with $a+b=p_3$, $a\ge p_4\ge b$ (so $a$
is dominant over $T'$ too, since every element of $T'$ is $\le p_4$), and
$T'$ a legal $(n-3)$-ladder response on $\{p_4,\dots,p_{n+1}\}$ using
$\le n-4$ further cuts. By Fact 2, $A(R')=a-A(B)$, $B:=\{b\}\cup T'$, and the
open target is a **lower** bound $A(B)\ge f(n)$.

Now observe: $R'=\{a,b\}\cup T'$ is *exactly* a legal response to the
$(n-2)$-ladder $\{p_3,p_4,\dots,p_{n+1}\}$ (total $s$, this is `tail-self-
similarity` one level up from what Theorem 35a/35b already used), using
$\le n-3$ total cuts (1 to split $p_3$ into $\{a,b\}$, $\le n-4$ more for
$T'$) — i.e. it is Xiang Yu peeling a dominant fragment $a$ off the
$(n-2)$-ladder's own top piece $p_3$ and refining the rest ($b$ plus the
tail) arbitrarily. This is *literally* the same "dominant-fragment-plus-
tail-refinement" shape that Theorem 31 / Propositions 20-22 (ℓ(F)=1) and
Theorems 32/33/34 (ℓ(F)=2) already exist to handle — but now instantiated
one level down, at $n-2$ instead of $n$. The needed bound $A(B)\ge f(n)$ is
(after the appropriate `tail-self-similarity` rescaling by the constant
relating the $(n-2)$-ladder's mass to $s$) precisely an instance of **the
full Claim-B lower bound** (not just Claim A's narrow "spend the whole
budget on $p_1$, leave the rest untouched" sub-case) applied at level $n-2$.

**Why this matters for the fix strategy:** Theorem 35b's own IH step
(the "$p_3$ untouched" branch) only needed $(\star_{n-3})$ in the *general*
form (any composition, not just Claim A) — and that was already available
since the induction is on the *whole* theorem, not just Claim A. Case (b)
similarly only needs the **whole** theorem at level $n-2$ (not a genuinely
new inequality) — but critically, that "whole theorem at level $n-2$"
includes the still-partially-open **middle band** (Theorems 32-35 territory)
at level $n-2$, not just the already-fully-closed Claim A. This is legitimate
for a strong induction on $n$ (level $n-2<n$), **not circular**, but it means
Case (b) at level $n$ cannot be declared closed until the middle band is
itself closed at level $n-2$ — a genuine bootstrapping dependency, not an
independent obstruction requiring new inequality-proving technique.

**Concrete, cheap-to-check consequence — a promising near-term win:**
Since $n=1$ ($c(1)=2/3$) and $n=2$ ($c(2)=4/7$) are **both already fully,
unconditionally closed** (both directions, round 1 and round 2 milestones),
this recursion should let:
- **$n=3$'s Case (b)** close "for free" by invoking the full theorem at
  level $n-2=1$ (trivial: $n=1$ has no middle band at all, only one point),
- **$n=4$'s Case (b)** close "for free" by invoking the full theorem at
  level $n-2=2$ (already fully closed, $c(2)=4/7$).

This is a concrete, low-effort next step: check whether Theorem 35's Case
(b) argument, instantiated with the already-fully-closed $n=1$/$n=2$
theorems as the level-$(n-2)$ input, actually closes $n=3$ and $n=4$
unconditionally — before attempting a general-$n$ argument. If so, it also
sets up the correct **bootstrapping tower** for general $n$: level $n$'s
Case (b) needs level $n-2$'s full closure (middle band included), so once
$n=3$ is fully closed (pending item 2's fix + this Case-(b) check), $n=5$'s
Case (b) becomes available; once $n=4$ closes, $n=6$'s Case (b) becomes
available; etc. — an inductive tower analogous to the telescoping-threshold
mechanism already used on the upper-bound front (round 9).

**One caveat/gap not yet addressed by the approach file's own Case (b)
write-up:** it only treats the sub-case where $p_3$ is split by **exactly
one cut** into two pieces $\{a,b\}$. A legal "$p_3$ is cut" response can use
**more than one** cut on $p_3$ itself (further splitting $b$, or splitting
$p_3$ into 3+ pieces directly), which is a genuinely un-enumerated deeper
sub-branch of Case (b) — worth flagging to the outliner so it isn't silently
assumed away. This further split is itself likely reachable by repeating the
same dominant-removal peel (Fact 2) recursively — consistent with the
"same machinery one level down" diagnosis above, but needs to be stated
explicitly as its own sub-case, not glossed over.

### Cheap-kill candidates
- For item 2: none needed beyond the boundary relabel above (already a
  cheap fix).
- For item 1: before doing new algebra, cheaply check numerically (exact
  Fraction) whether Case (b)'s target $A(B)\ge f(n)$, restricted to
  $n=3,4$ with $T'$ ranging over all legal responses to the (already fully
  understood) $n-2\in\{1,2\}$-ladder, is implied *literally* by substituting
  the certified $n=1$/$n=2$ closed-form lower bounds — this is a pure
  algebra/substitution check, not a search, and should take under 10
  minutes to confirm or refute before the outliner commits to writing it up
  as a new theorem (Theorem 35c, say).

### Candidate technique(s)
- Item 1: strong induction via `tail-self-similarity` (self-similarity to
  the $(n-2)$-ladder) + Fact 2 (`sharp-dominant-removal-identity`) exactly
  as already used throughout Theorem 34/35 — no new tool needed, just
  correctly scoping which induction hypothesis level ($n-2$, full theorem,
  not just Claim A) the argument actually requires, per round-10 rule #15.
- Item 2: no technique needed, a case-boundary relabeling.

### Knowledge-base / lemma entries to use
- `lemmas/theorem-34-v1-in-s-p2-v2-lt-s-conditional-closure.md` (corrected
  $n-3$ cap; cite for the mass-conservation cut-budget accounting pattern).
- `lemmas/upper-truncation-identity.md` (parity-correction term
  $\epsilon(v)$; needed if extending the $\Delta(n,v)$ bridge to the
  $\epsilon=1$ case, still flagged open even in the already-closed Case (a)).
- `sharp-dominant-removal-identity` / `dominant-element-removal-identity`
  (Fact 2, used repeatedly for both items).
- `tail-self-similarity` (rescaling between ladder levels — the exact tool
  needed to instantiate "the whole theorem at level $n-2$" for item 1).
- Round-10 Rule #15 (in `/tmp/memory/run_state.md`) — the general
  meta-pattern this diagnosis matches; cite it explicitly in the outline so
  future rounds recognize the pattern immediately.

### Analogous past problems (cruxes)
Checked combinatorics subtopics `telescoping-and-summation`,
`induction-and-construction`, `size-bounding-and-descent` for
alternating-sum/self-similar-recursion cruxes. Two loose structural analogs,
neither a strong transplant:
- `aimo-0388` (coin-stack balancing): "split a sorted sequence into two
  stacks by pairing consecutive elements so each pair's contribution
  telescopes to a non-positive gap, leaving isolated boundary terms" — same
  flavor as our own already-in-house `odd-run-reduction-lemma`/pairing
  toolkit, not a new idea.
- `aimo-0463` (anti-Pascal pyramid): "apply the same structural chain-sum
  bound to a self-similar sub-triangle whose apex chain draws only from
  unused (hence large) values" — the self-similar-sub-instance-forces-a-
  contradiction shape is structurally similar to our own
  `tail-self-similarity` recursion, but the actual mechanism (forcing a
  permutation via a sum bound) doesn't transplant.
Neither is a genuine crux transplant; the project's own machinery
(certified lemmas above) is already the right tool. No new corpus lead
found for this lens.

### Prior progress
Theorem 35a/35b (p3-untouched branch): closed, 35a unconditional, 35b
conditional on $(\star_{n-3})$ (already-established general form of the IH).
Theorem 34 (corrected $n-3$ cap): closed. n=3 middle band
(rank-pigeonhole-budget): closed modulo item 2's cosmetic fix. Case (b)
(p3-is-cut): open, only the single-cut-on-$p_3$ sub-case even attempted, no
closure — see diagnosis above for why it should be attackable via level
$n-2$ recursion for at least $n=3,4$ immediately.

### Dead ends (do not retry)
- Do NOT re-attempt closing Case (b) via `max-domination-lemma` alone (gives
  the wrong-direction bound, upper not lower) — already tried and reported
  as failing in the approach file (round 19).
- Do NOT attempt to peel $b$ off $B=\{b\}\cup T'$ via a further
  dominant-removal step assuming $b$ dominates $T'$ — false in general ($b$
  can be close to $p_4$ with a $T'$-fragment also close to $p_4$, neither
  dominates); already reported dead in the approach file.
- Do NOT assume $B$ is a rescaled copy of a smaller *standard* ladder
  response directly (its "top" $b$ is a free real in $(0,p_4]$, not forced
  to a ladder value $p_4/2^j$) — already reported dead. The correct
  self-similar object is $R'=\{a,b\}\cup T'$ (the whole thing, before
  peeling $a$), not $B$ alone — this is the key reframing this report
  offers over the approach file's own three failed attempts.

### Small-case / intuition notes (conjecture, not proof)
- 180,000+ trial exact-Fraction search (already on file, round 19) found
  zero violations of $\Delta(n,v)\le v-f(n)$ across the *entire* $R'$ family
  (both $p_3$-touched and untouched) for $n=3,\dots,6$ — strong numeric
  support that Case (b) is true, consistent with the "same machinery, one
  level down" diagnosis (it should be true for the same structural reason
  Case (a) is true, just needing the induction to reach deep enough).
- The $n=1,2$ full closures being already unconditional (no further
  induction hypothesis needed) is exactly what should make $n=3,4$'s Case
  (b) closable immediately without waiting for a general-$n$ proof — this
  is the single highest-leverage, cheapest next check for front 1.
