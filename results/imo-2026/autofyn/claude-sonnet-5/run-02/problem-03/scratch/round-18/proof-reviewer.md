# Proof review — round 18 — imo-2026-03

Reviewed slugs: `greedy-halving-adversary` (Theorem 33/34) and
`lp-duality-certificate` (Tail Exchange / Danskin concavity refutation).
Both self-report Status: `partial`, consistent with what I found — no
overclaiming detected in either file.

## greedy-halving-adversary — Theorem 33, Theorem 34

**Setup checked.** Reviewed the round-17 Step-1 identity (Proposition 32)
that both theorems build on:
$$A(F\cup G')=p_2-A(R')-(v_1-v_2)+2\int_{v_2}^{v_1}u_{R'}(x)\,dx,$$
for $F=\{v_1,v_2\}\cup P$ ($\ell(F)=2$, sub-case (b): $v_2<v_1<p_2$),
$G'=\{p_2\}\cup R'$. I independently re-derived this from Lemma 25 +
Proposition 30's per-threshold formula and re-verified it numerically with
a fresh exact-`Fraction` script (20,000 trials): the identity is correct
provided $p_2$ dominates $R'$ ($p_2>\mathrm{Total}(R')$), which the ladder
always satisfies — an initial unconstrained test (no dominance enforced)
produced many spurious "mismatches" that vanished once dominance was
imposed, confirming this is a real (if implicit) hypothesis of the
identity, not a bug in the file.

**Theorem 33** ($v_1\in(s,p_2)$, $v_2\ge s$, fully unconditional).
Re-derived by hand: since $\mathrm{Total}(R')=s$, $u_{R'}\equiv0$ on
$[s,\infty)\supseteq[v_2,v_1)$, so the cross term vanishes and
$A(F\cup G')=p_2-A(R')-(v_1-v_2)$. The chain $A(R')+(v_1-v_2)<s$ follows
from (a) $v_1-v_2<p_2-s=f(n)$ (strict, since $v_1<p_2$), (b)
$A(R')\le\max(R')\le p_3$ via `max-domination-lemma` (independently
re-verified this general fact, $A(S)\le\max(S)$, over 20,000 random
trials, zero violations) plus the ladder's strict decrease, and (c)
$s-p_3=f(n)(2^{n-2}-1)\ge f(n)$ for $n\ge3$. The $n=3$ boundary
(equality in (c)) is correctly handled: the file's remark that step (a)'s
strictness saves the chain there is right — I checked it by hand. Fresh
12,000-trial exact-`Fraction` script against the actual ladder ($n=3..6$):
zero violations, margins matching the file's own reported figures.
**Confirmed correct, unconditional, no gap found.**

**Theorem 34** ($v_2<s$, $v_1+v_2\le p_2$, conditional on $(\star_{n-2})$).
Re-derived by hand: splitting the interval at $s$, using the crude bound
$J_0\le v_2$, and substituting the IH fact $A(R')\ge f(n)$ (via
`tail-self-similarity` chained as in Proposition 24), the algebra reduces
exactly as claimed to $A(F\cup G')\ge p_2+f(n)-(v_1+v_2)\ge f(n)$ using
the hypothesis $v_1+v_2\le p_2$. Fresh 12,000-trial script (cut budget on
$R'$ correctly capped at $n-2$, both $v_2<s$ and $v_1+v_2\le p_2$
enforced): zero violations, minimum margin matching the file's own
(small but strictly positive, e.g. $17/15{,}000{,}000$ at $n=3$).
**Confirmed correct, conditionally on $(\star_{n-2})$ exactly as scoped
(unconditional for $n\le4$), no gap found.**

**Scope/honesty check.** The residual open band $v_2\in(p_2-v_1,s)$ is
correctly identified as non-negligible in width and honestly diagnosed
(not force-closed) as the identical round-15/16 crux — a sharp upper
bound on the truncated alternating sum $A(R'_{>v_2})$. The file's
diagnosis of *why* the outline's per-cut charging mechanism fails
(a single cut's sign contribution depends on the global parity of other
fragments exceeding the breakpoint, not a local property) is a correct,
non-hand-wavy argument, not an evasion.

**Verdict: Status `partial` confirmed correct (no downgrade, no
overclaim). Two new lemmas (Theorem 33, Theorem 34) certified into
`lemmas/theorem-33-v1-in-s-p2-v2-geq-s-closure.md` and
`lemmas/theorem-34-v1-in-s-p2-v2-lt-s-conditional-closure.md`, each with
the scope/conditioning preserved exactly as the builder stated (Theorem
34 explicitly labeled conditional, unconditional only for $n\le4$).**

**Route: CHANGES REQUESTED** — real, verified progress (narrows sub-case
(b)'s open range further, at both ends), but the residual middle band is
a genuine, non-trivial remaining gap, correctly reported as such.

## lp-duality-certificate — Danskin/concavity refutation for case (b2)

**Load-bearing claim checked independently, not the builder's own
`differential_evolution` script.** I wrote a from-scratch verification
using a structurally different method (enumerate all 35 cut-budget
compositions across the 4 pieces at $n=3$ exhaustively, run independent
multi-restart Nelder–Mead within each composition, take the min), on the
same on-file witness $(p_1,p_2)=(4468,2591)/10001$. Results at a grid of
$p_3$ values reproduced the builder's qualitative shape exactly: $g$
decreases from $p_3=0.16$ ($g\approx0.5129$) down to a clean minimum at
$p_3\approx0.1877\approx p_1-p_2$ ($g=0.5000$), then increases to a local
max near the on-file witness $p_3\approx0.2251$ ($g\approx0.5158$), then
decreases again toward the far endpoint. The slopes match too:
$g(0.17)-g(0.175)=0.0025$ and $g(0.195)-g(0.190)=0.0025$, both over
$\Delta p_3=0.005$ — the same $\mp1/2$ signature the builder reported.
A concave function on an interval cannot have a strict interior local
minimum flanked by increases on both sides; this rules out the Conjectured
Concavity premise. **Per this project's own standing rule (never trust a
single-optimizer refutation), using a genuinely different optimizer and
enumeration strategy and getting the same qualitative answer is real
corroboration, not a repeat of the builder's own numbers.**

**Overclaim check.** The file correctly does not claim any new positive
coverage of case (b2), correctly stops before attempting the (now
premise-broken) general-$n$ stationarity step per the outline's own gate
instruction, and correctly declines to submit a promotable lemma (the
finding is a refutation tied to a specific witness/mechanism, not a
general reusable statement). No overclaiming found.

**Verdict: Status `partial` confirmed correct. This is a genuine negative
result (rules out a fourth distinct mechanism family for case (b2),
after peel/bisect/recurse, weighted-combination, and naive boundary
continuity) but delivers zero new positive coverage — correctly recorded
as `dead-end` in the ranking (for this specific mechanism), not
`partial`/`advanced` progress on the target itself.**

**Route: CHANGES REQUESTED** (per CLAUDE.md's routing table: Status
`partial` with real, correctly-diagnosed progress — here the progress is
a rigorous foreclosure of one mechanism, which is legitimate content for
the next round to build on, not a fatal flaw in the approach's viability
as a slug; case (b2) remains the target, open for a chamber-by-chamber
argument or a different mechanism entirely).

## current.md

Updated `results/imo-2026-03/current.md` with a new "Round 18" entry
under "Approaches tried" summarizing both builds and this review's
independent verification, and certified the two new lemma files listed
above. Status remains `partial` (unchanged, no promotion to `solved`
possible or claimed this round — case (b2) and Open Gap 1 for the general
upper bound remain the binding open items).

## No RETHINK issued

Neither approach is fundamentally broken: `greedy-halving-adversary`
continues to make genuine, verifiable incremental progress narrowing a
precisely-scoped sub-case; `lp-duality-certificate`'s refutation is a
legitimate, correctly-executed negative result consistent with its own
stated diversification role (per the shared-gap-plateau rule), not a
sign the slug itself should be abandoned.
