# Outline review — round 130 (imo-2026-06)

## Independent verification of the descent (Crux 1)

I did NOT rubber-stamp the explorer/outliner. I re-derived the descent's load-bearing steps by hand and tested them numerically.

**Arithmetic check (step 4).** All four sub-lemmas hold:
- *Landing.* $a_n/a_1 = pc/a_1 \ge p/a_1 > a_1 \ge q$ (strict, since $p>a_1^2$). The smallest $k$ with $q^k c \ge a_1$ gives $q^k c < q\cdot a_1 < a_n$ (strict: $pc/a_1 > q \Rightarrow pc > q a_1$). So $q^k c \in [a_1,a_n)$. Sound.
- *Index descent.* $a_i < q^k c < a_n \Rightarrow i<n$ (strictly increasing). Lets the IH apply. Sound.
- *Shared prime transfer.* $r\mid\gcd(a_n,a_i)$, $r\neq p$ (IH: $p\nmid a_i$), so $r\mid c\mid q^k c$. Sound.
- *Rad divisibility.* $q\mid c \Rightarrow P(q^k c)=P(c)\subseteq P(c)\cup\{p\}=P(a_n)$, so $\mathrm{rad}(q^k c)\mid\mathrm{rad}(a_n)$. Sound.
- *IH phrasing.* "No $\prec$-minimal $a_i$ with $i<n$ is divisible by a large prime." Base $n=1$ vacuous ($a_1$'s primes are $\le a_1 < a_1^2$). Inductive step: the argument produces $a_{\mathrm{idx}(q^k c)}\prec a_n$, so if $a_n$ carried a large prime it is not $\prec$-minimal; contrapositive gives the IH extended to $i=n$. Non-circular. Sound.

**Numerical confirmation** (sympy, 7 seeds): "$\prec$-minimal terms are $a_1^2$-smooth" — 0 violations. Seeds: a1=15 (maxp 5), 30 (5), 175 (13), 429 (43), 273 (241), 210 (127), 46189 (2207). All also satisfy the tightened $\le a_1$ bound. The descent mechanism is correct.

**Circularity check (Piece A) — the one real concern, RESOLVED.** The run's certified lemmas `universal-membership-no-transient` and `transversal-residue-characterization` are **conditional on GAP** (they define $L=\prod P$, $V$, and need $\mathcal M$ finite). If the descent imported THOSE, it would be circular (using finiteness to prove finiteness). But the descent does **not** use the residue form. It uses the **unconditional elementary form**: "$x\ge a_1$ appears $\iff \gcd(x,a_i)>1$ for every $\prec$-minimal $a_i<x$." I proved this unconditionally:
- *appears $\iff$ valid against all terms $a_i<x$:* forward trivial; backward uses only "$a_n\to\infty$" (strict increase) — the smallest valid candidate above $a_n$ must be $\le$ any globally-valid $x>a_n$, else contradiction. No finiteness.
- *all terms $a_i<x$ $\iff$ $\prec$-minimal $a_i<x$:* a non-$\prec$-minimal $a_j<x$ has an earlier $\prec$-minimal $a_m<x$ with $P(a_m)\subseteq P(a_j)$, so validity against $a_m$ implies validity against $a_j$. Recursion terminates (indices decrease). No finiteness.

Numerically confirmed (0 violations across 6 seeds). **No circularity.** This is the one place the outline's citation is loose (step 3 says "import as `universal-membership-no-transient`…") and must be tightened at build time.

## Issues found (both fixable, neither fatal)

### large-prime-descent — APPROVE (with two CHANGES-REQUESTED clarifications for the builder)

The technique is the published mechanism, the skeleton is sound, end-to-end, no open conjectures, no casework, uniform across regimes. APPROVE. Two clarifications the builder must handle:

1. **Piece A must be cited in its UNCONDITIONAL elementary form** (step 3). Do NOT cite the GAP-conditional `universal-membership-no-transient` / `transversal-residue-characterization` (those need $\mathcal M$ finite to define $L,V$ — circular if used inside the descent). The elementary form "$x$ appears $\iff \gcd(x,a_i)>1$ for every $\prec$-minimal $a_i<x$" is proven by the no-skip greedy argument + $\prec$-minimal set reduction, both unconditional. Prove it inline (it is a short triviality); do not lean on the residue machinery. The $\prec$-minimal-supports$=\mathcal M$ equivalence (step 2) is NOT needed for Piece A — Piece A is phrased directly on $\prec$-minimal terms, not on $\mathcal M$.

2. **Step 2 overclaims; Direction A is FALSE.** The outline states the correspondence "$\prec$-minimal supports $=\mathcal M$" with both inclusions. I tested this: **Direction A (every $\prec$-minimal support is in $\mathcal M$) is FALSE** — violated at a1=30, 429, 273, 210, 46189, 323, 385. The failure mode is real: a later term can appear with a *strictly smaller* support (e.g. a1=273: support $\{3,5\}$ appears late, strictly below the earlier $\prec$-minimal $\{3,5,7\}$-type supports; a1=429: eight $\{3,5,p\}$ $\prec$-minimal supports are later subsumed by the appearance of $\{3,5\}$). Do NOT attempt to prove Direction A.
   - **Direction B (every $\mathcal M$ member is a $\prec$-minimal support) is TRUE** and is the *only* direction needed. Proof: for $M\in\mathcal M$, let $a_n$ be the *first* term with $P(a_n)=M$; if $a_m\prec a_n$ ($m<n$, $P(a_m)\subseteq P(a_n)=M$) then $\subseteq$-minimality of $M$ forces $P(a_m)=M=P(a_n)$, contradicting first-appearance. So $a_n$ is $\prec$-minimal.
   - The transfer to the finish needs only Direction B: descent $\Rightarrow$ $\prec$-minimal supports are $a_1^2$-smooth $\Rightarrow$ $\prec$-minimal supports form a finite subset of $2^{\{p\le a_1^2\}}$; Direction B gives $\mathcal M\subseteq\{\prec\text{-minimal supports}\}$; hence $\mathcal M$ finite; $\delta$'s `post-stabilization-theorem` finishes. Rewrite step 2 as Direction B only.

These are builder-level corrections to the prose/citation, not a flaw in the descent itself. The descent is correct.

## Diversity check (single-gap-trap guard)

NOT a single-gap trap. The descent is a **complete published end-to-end solution with no open conjectures**, not a shared-gap bet on a wall. Diversity is irrelevant when one approach is a real solution. **Do NOT re-diversify next round** — re-diversifying away from a solved problem would be malpractice. (This statement is conditional on the descent being sound, which I verified above. If the builder finds a gap I missed, then diversity resumes — but verify first.)

## Superseded wall-attackers (frozen, not built this round)

The outliner froze `density-promotion-bound` (α), `smooth-window-crash`, `pstar-core-straggler`, `bounded-gap-lcm-reduction` (γ) as wall-closers — the descent closes the wall they were attacking without their machinery (SPT/$p^*$, $W_1$/$W_2$, Cov, mtp-window, regime split). I agree: no builder on them this round. Their **certified lemmas are retained as imports** (`common-primes-bounded`, `sat-criterion`, `freeze-lock`, `singleton-freeze`, `entering-2`, `cov-monovariant`, `mtp-monovariant-and-gap-bound`, `star-straggler-self-blocking`, `two-q-gap3-obstruction`, `pairwise-intersection`, and the δ chain). Their low rank below reflects "superseded, open wall, not to be built," not a defect in their (still-valid) certified assets.

`transversal-single-cycle-finish` (δ) stays high — it is the **imported finish** (Pieces A+C) the descent composes. Verified-milestone; no builder (it is an import target, not a wall-attacker).

## Ranking

Registered `large-prime-descent` (cold-start 1500). Ranked the full field head-to-head; `large-prime-descent` beats every existing approach (it closes the wall they are stuck on, uniformly, with no open conjectures; δ is conditional-only, the descent makes the whole claim unconditional end-to-end). Stale flags on the r129 wall-attackers cleared. Post-ranking Elo: δ 1687, α 1617, **large-prime-descent 1583**, pstar 1519, smooth-window-crash 1468, γ 1394. (large-prime-descent's Elo is still climbing from cold-start 1500 — it won every head-to-head this round but has no accumulated history; it will overtake as it keeps winning. The build-set decision, not the raw Elo, is what matters this round.)

Retired `bertrand-dickson-eviction` (1421) and `omega-induction-loaded` (1310) left untouched (dead, not compared).

## Per-role rule

ALWAYS: for imo-2026-06, the large-prime descent's Piece A is the UNCONDITIONAL elementary form "$x$ appears $\iff \gcd(x,a_i)>1$ for every $\prec$-minimal $a_i<x$" (no-skip greedy + $\prec$-minimal set reduction). Do NOT cite the GAP-conditional `universal-membership-no-transient`/`transversal-residue-characterization` inside the descent — they define $L,V$ from $\mathcal M$ and would make the finiteness proof circular. (round 130)
NEVER: claim $\prec$-minimal supports $=\mathcal M$ (both inclusions) for imo-2026-06 — Direction A (every $\prec$-minimal support $\in\mathcal M$) is FALSE (a1=30,429,273,210,46189,323,385: a later term appears with a strictly smaller support, subsuming an earlier $\prec$-minimal). Only Direction B ($\mathcal M\subseteq\{\prec\text{-minimal supports}\}$) is true, and it is the only direction the descent needs to transfer the $a_1^2$-smooth bound to $\mathcal M$. (round 130)

build set: large-prime-descent
