## Outline review — imo-2026-06, round 3

Reviewed: `results/imo-2026-06/current.md`, all four `approaches/*.md`
(active-set-stabilization, state-compactness-pigeonhole, jacobsthal-covering-bound
revised; bounded-link-invariant new), and `/tmp/round-3/proof-outliner.md`.
Verified the revisions are actually persisted to disk (file mtimes ~23:57–00:00
match/precede the outliner report at 00:01 — no repeat of round 2's
report-vs-disk mismatch).

### Cross-cutting check: the "Self-Type-Compatibility Lemma" (shared by
active-set-stabilization and state-compactness-pigeonhole)

**Claim.** Fix finite $Q\supseteq R(a_1)$. If $R(a_i)\subseteq Q$ for some
index $i$, then $\tau_i\cap\tau_j\neq\emptyset$ for every $j\ne i$, where
$\tau_k:=R(a_k)\cap Q$.

**Verified sound.** By the certified `lemmas/pairwise-non-coprimality.md`,
$\gcd(a_i,a_j)>1$, so some prime $p\mid a_i,a_j$. Since $R(a_i)\subseteq Q$,
$p\in Q$; and since $R(a_i)\subseteq Q$ means $\tau_i=R(a_i)\cap Q=R(a_i)$,
$p\in\tau_i$; also $p\in R(a_j)\cap Q=\tau_j$. So $p\in\tau_i\cap\tau_j$. I
checked both directions of the corollary chain: (a) taking $i=1$ (valid
since $Q\supseteq R(a_1)$ is assumed), $\mathrm{Good}_Q(a_1)$ holds for
*every* admissible $Q$ — correct, and a genuinely new, non-pigeonhole fact
(no state-recurrence used at all, so it does **not** fall under the
Monotonicity Obstruction Lemma's refuted family); (b) the "propagation"
corollary (if $R(a_i)\subseteq Q$ for every $i<n$, then $\tau_n$ meets every
earlier $\tau_i$ automatically, regardless of $a_n$'s own type) follows by
applying the lemma with the roles of $i,j$ as stated. This is a real,
verifiable new tool, not a hand-wave — **approved for use**.

Both files correctly leave the remaining content (the "aimo-0680-style"
discrepancy-divisibility finish in active-set-stabilization; the
"outside-prime indices harmless" question in state-compactness-pigeonhole)
explicitly marked **open/unproven**, not asserted. No overclaiming.

### jacobsthal-covering-bound: Adjacent-Link Lemma / Λ-split

**Adjacent-Link Lemma** ($\gcd(a_n,a_{n+1})\mid a_{n+1}-a_n\le R$): correct,
elementary ($\gcd(x,x+d)=\gcd(x,d)\mid d$), combined with the already-certified
bounded-gap lemma. Sound, unconditional, no transient — approved.

**Λ-stabilization** (link-prime set $\Lambda_n$ monotone non-decreasing in
the *fixed* universe $\{p\le R\}$, so it stabilizes): this is genuinely
different from every previously-refuted pigeonhole in this population. The
file correctly distinguishes it from the fallacious "state σ(n) recurs"
family (memory rule: NEVER accept a claim that a *specific* state recurs
from mere finite-codomain pigeonhole) — here the claim is only "a monotone
subset sequence in a fixed finite set eventually stops growing," which needs
no specific-value recurrence at all. **Sound.**

The reduction "$Q=\Lambda\cup(Q\setminus\Lambda)$, so it suffices to show
$Q\setminus\Lambda$ finite" is a valid reformulation (not yet a proof — the
file is honest that this is the new open target, step 3 unsolved). The
"$\Lambda\ne\mathrm{rad}(L)$, refuted, don't retry" note is a correctly
scoped negative finding (checked via $a_1=35$: $7\in\mathrm{rad}(210)$ never
appears as an adjacent link). No fatal flaw here — legitimate incremental
narrowing of the central gap, verdict **CHANGES REQUESTED** (as before: no
monovariant yet for $Q\setminus\Lambda$'s finiteness).

### bounded-link-invariant (new): one real flaw to fix before/during build

Core ingredients are sound: the Adjacent-Link Lemma (shared, verified above)
and the finite alphabet $(d_n,\ell_n)\in\{1,\dots,R\}^2$ for every $n\ge1$
with no transient — a genuinely different primary object from the
$Q$-type framing shared by the other three, correctly targeting the
plateau-break directive (three rounds now stuck on variants of "fix $Q$
first").

**Flaw found (fix before trusting later steps).** Step 3 defines the
baseline step $b_n:=\min\{d\ge1:\gcd(a_n+d,a_1)>1\}$ and claims, citing
`lemmas/prime-factors-a1-cover-forever.md`, that "$a_n+b_n$ is always a
legal candidate" (i.e. satisfies $\gcd(\cdot,a_i)>1$ for **every** $i\le n$,
not just $i=1$). This is **false as justified**: $b_n$ is only the shift
making $a_n+b_n$ share *some single* prime with $a_1$ specifically; it does
not guarantee a shared prime with an arbitrary earlier $a_i$, which by the
Fact lemma may be covered by a *different* prime of $R(a_1)$. This is
exactly the "$H(Q)$-membership is not a safety certificate" trap that
`jacobsthal-covering-bound.md`'s own certified negative lemma
(`covering-membership-not-safety-certificate.md`) warns against — the
correctly-safe construction (used in the certified `bounded-gap-via-rad-a1`
lemma) takes $M$ = the next **multiple of the full product**
$R=\mathrm{rad}(a_1)$ exceeding $a_n$, not the next integer sharing merely
one prime of $R(a_1)$ with $a_1$. The bound $b_n\le R$ itself is still true
(trivially, the gap to the next multiple of $\min(R(a_1))$ is at most
$\min(R(a_1))\le R$), so $b_n$ remains a well-defined, bounded quantity —
but the surrounding claim that it is "always a legal candidate" must be
struck; the builder should either (a) redefine $b_n$ as the next multiple
of $\mathrm{rad}(a_1)$ (which *is* provably legal, by the certified lemma,
and still $\le R$), or (b) keep $b_n$ as defined but drop the "legal
candidate" framing and treat it purely as an arbitrary bounded comparison
statistic (in which case the intended interpretation of $\epsilon_n$ as
"true step differs from the *safe* fallback" needs re-justifying, since
$b_n$ as literally defined is not obviously the "safe" one).

This does not kill the approach — the core finite-alphabet idea and step
4/5 (bounded-order determinacy / density fallback, both explicitly
untested/open, both flagged as possibly-false) are unaffected in spirit —
but it is a concrete, load-bearing definitional bug that must be fixed
**first**, before the builder invests in the automaton-determinacy
computation, or the whole $\epsilon_n$ construction may not mean what the
outline thinks it means. Verdict: **CHANGES REQUESTED** (fix the baseline
definition, then proceed with steps 3–5 as outlined).

### Diversity check

Three approaches (active-set-stabilization, state-compactness-pigeonhole,
jacobsthal-covering-bound) still work inside the finite-prime-set-$Q$
framing, but this round they attack genuinely different sub-targets within
it (prefix-extension via propagation/divisibility vs. central
self-sufficiency via the $\Lambda$/link-prime split) rather than one shared
wall, consistent with the correctly-diagnosed 2-round plateau being broken
by division of labor. bounded-link-invariant is a genuinely different
primary object (gap/link sequence, no $Q$ at all) — good, real diversity,
matches the plateau-break directive. No approach here is a fragment of the
problem; all four target the full periodicity conclusion end-to-end, with
explicit open gaps, not a sub-lemma masquerading as the whole claim.

### Verdicts

- **active-set-stabilization** — APPROVE. Self-Type-Compatibility Lemma
  verified sound; skeleton for the aimo-0680-style finish is honestly
  incomplete (divisibility relation $L\mid e_n$ unproven, correctly flagged
  as the concrete open gap, may be false).
- **state-compactness-pigeonhole** — APPROVE. Same shared lemma verified
  sound; plan to push $n^*=1$ via Proposition B + propagation is a valid,
  distinct route from active-set-stabilization's; outside-prime-index
  harmlessness genuinely open.
- **jacobsthal-covering-bound** — APPROVE (CHANGES REQUESTED-level open
  gap, as before). Adjacent-Link Lemma and Λ-stabilization verified sound;
  $Q\setminus\Lambda$ finiteness is a real narrowing of Hypothesis SS, not
  yet closed.
- **bounded-link-invariant** — APPROVE with a required fix. Core
  finite-alphabet framing sound and genuinely diversifying; the $b_n$
  "legal candidate" justification in step 3 is unsound as written and must
  be corrected (see above) before the builder relies on it for the
  exceptional-step analysis.

No approach is RETHINK this round — no wrong technique, no circularity, no
repeat of a recorded dead end (growth-rate-contradiction's two refuted
mechanisms are correctly avoided by all four).

### Ranking

Registered `bounded-link-invariant` (new). Folded round-2's verified build
outcomes into Elo for the three previously-stale entries, and placed the
new approach relative to the established field (below the three mature
partials, above the confirmed dead-end growth-rate-contradiction), per
`update_ranking`. Resulting order (best first): state-compactness-pigeonhole
(~1566), active-set-stabilization (~1561), jacobsthal-covering-bound
(~1489), bounded-link-invariant (~1472, cold-start, not yet built),
growth-rate-contradiction (~1412, dead-end, excluded from build).

### Build set

All four sound-with-open-gaps approaches should be built this round; the
builder for bounded-link-invariant must fix the $b_n$ baseline definition
(§ above) before proceeding to steps 4–5.

build set: active-set-stabilization, state-compactness-pigeonhole, jacobsthal-covering-bound, bounded-link-invariant
