# Proof-outliner report — round 22

Read `current.md`, all three live approach files, and both round-22
explorer reports before writing. Wrote a "Round 22 outline (proof-outliner)"
section directly into each of the three live approach files (appended, no
prior certified content overwritten). Kept the field at 3 slugs — no new
approach opened this round; the existing scoping (greedy-halving-adversary
= lower bound Claim B, rank-pigeonhole-budget = Claim A book-of-record plus
ε-bridge addendum, lp-duality-certificate = upper bound case (b2)) already
covers genuinely different terrain, and the CLAUDE.md shared-gap-plateau
rule explicitly forbids splitting the ε-bridge target across new slugs.

## 1. `greedy-halving-adversary` (advance in place)

**Applied the Theorem 35b algebra fix directly** (not just outlined): the
explorer confirmed it is a one-line *deletion*, not a replacement — $f(n-3)$
has numerator $1$, not $2^{n-3}$, so $D_{n-3}\cdot f(n-3)=1$ identically and
the correct conclusion is simply $A(T')\ge f(n)$, with no extra factor and
no need for the `tail-self-similarity` cross-level-identity step the file
previously invoked. Fixed at the point of proof (Theorem 35b) and at both
downstream citation sites (Theorem 35a′ sub-range 2, and the "Status of Case
(a)" recap) — confirmed via grep that no other citation site relied on the
false stronger bound.

**This round's outline target: push Theorem 36's Case (b) ($p_3$-cut
branch) from $n\le4$ to $n\ge5$** via the induction-tower reframing round-20
sketched but never built (view $R'=\{a,b\}\cup T'$ as a legal response, one
level up, to a rescaled $(n-2)$-ladder, invoking the full $(\star_{n-2})$).
Wrote a 5-step skeleton identifying the two genuine risk points a builder
must check explicitly, not assume: the scale-factor/cut-budget arithmetic
(step 3) and whether the resulting bound collapses to exactly $f(n)$ or
leaves slack (step 4 — flagged explicitly as *not* analogous to the
now-fixed Theorem 35b, since this is a two-level drop, not same-level).
Also flagged a smaller, cheap secondary target (verify $\epsilon(v)\equiv0$
on Theorem 35b's own range, closing $(\Diamond')$ there for free) —
round-21 explicitly declined to rely on this unverified, so it needs a real
one-line check before use. Per the explorer's identification (§2 below),
told the builder explicitly not to duplicate `rank-pigeonhole-budget`'s
§7.6 vertex-enumeration route.

## 2. `rank-pigeonhole-budget` (advance in place, redirect scoped as
"pending," not "close now")

The explorer's central finding: §7.6 (general-$n$ cross-piece vertex gap)
and `greedy-halving-adversary`'s Theorem 35b/36 open ranges are the *same*
algebraic target — an exact substitution (Theorem 34 (corrected)'s identity
$s-p_2=-f(n)$ into this file's own $(\sharp')$) reproduces $(\Diamond')$
term for term, for every $n$, not just the already-closed $n=3$ base case.
Judged the full redirect **premature this round** since the sibling's
Theorem 36 extension to $n\ge5$ is only outlined, not yet built — closing
§7.6 as a corollary now would overclaim. Instead outlined two smaller,
actually-closable items: (1) write out the conditional corollary's exact
algebraic derivation now (§7.7 stub) so it can be certified the moment the
sibling's fix lands, without re-deriving anything; (2) an independent
numeric cross-check at $n=4$ (one level past the already-closed $n=3$ case)
comparing this file's $(\sharp')$ against the sibling's $(\Diamond')$ on
identical random configurations — cheap, and a high-value negative finding
if it disagrees. Told the builder explicitly not to re-attempt §7.6's
vertex-enumeration route itself this round (already shown weaker on this
target than the sibling's algebraic-floor route).

## 3. `lp-duality-certificate` (advance in place)

The explorer found `within-chamber-affinity-theorem` (round 20/21)
characterizes vertices in the wrong space — fragment space $\bar\Omega$ for
fixed $p$, not $p$-space itself — so case (b2) cannot yet be checked "at
chamber vertices" as the theorem's name suggests. Outlined **Target 1**: a
genuinely new, from-scratch $p$-space Chamber-Vertex Theorem, built on
R20.2's linear system ($\mathbf v(p)=M(\tau)^{-1}Np$) and the same
convex-geometry fact `vertex-minimum-theorem` already uses (extremum of a
linear functional on a polytope is at a vertex) — with the constraint set
(feasibility, order, type-optimality-vs-neighbors) spelled out explicitly,
and the type-optimality condition's own invertibility dependency on
*neighboring* types flagged as an inherited, not new, conditional
hypothesis. Outlined **Target 2**: numerically test the box-corner ×
tail-chamber-vertex decomposition the explorer observed (worst witnesses
cluster at $(p_1,p_2)\to$ box corner, with the tail carrying its own
separate local extremum) at $n=3,4$, using Target 1's characterization
restricted to tail coordinates — explicitly scoped as a numeric test of a
conjecture, not a proof, with instructions to report a negative finding
honestly if the decomposition fails rather than re-attempting it. Neither
target closes case (b2) this round; both are genuinely new infrastructure,
distinct from the 9 confirmed-dead mechanism families on file.

## Build set recommendation

build set: greedy-halving-adversary, rank-pigeonhole-budget, lp-duality-certificate
