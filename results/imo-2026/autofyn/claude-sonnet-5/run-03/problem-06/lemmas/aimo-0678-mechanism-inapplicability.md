## Result (aimo-0678-mechanism inapplicability — negative, diagnostic)

The two structural ingredients that make crux problem `aimo-0678`'s
monovariant $w_n=\min\{m\ge a_n : m\nmid s_n\}$ non-increasing — (a) the
target quantity is frozen except at locally (bounded-window) identifiable
break points, and (b) at each break point the current term is
unconditionally certified (no lookahead) to enter the new failing set —
**cannot both be supplied** for any residue-pattern monovariant
$w_n(M)$/$\pi_{n+1}(M)$ built for this problem's greedy sequence.

### Why (a) fails: no bounded-window break-point classifier exists
Whether $\pi_{n+1}(M)$ changes at step $n$ is determined by the divisibility
pattern of $a_{n+1}$ relative to the *accumulated history* — the same type
of datum classified by the exceptional-step indicator $\epsilon_n$ of
`windowed-epsilon-automaton-failure.md`. That certified result shows: under
eventual constancy $(d_n,\ell_n)=(d^*,\ell^*)$ for $n\ge n_0$ with
$1\le d^*<R$, $\epsilon_n$ has exact period $R/\gcd(d^*,R)>1$, tied to the
cumulative value $a_n\bmod R$, invisible to any bounded window of recent
$(d_n,\ell_n)$-history. The identical cycling argument applies with
$\epsilon_n$ replaced by "does $\pi_{n+1}(M)$ change at step $n$": under the
same hypothesis this is determined by $a_n\bmod\mathrm{lcm}(R,M)$, cycling
through $\mathrm{lcm}(R,M)/\gcd(d^*,\mathrm{lcm}(R,M))$ values — so no
bounded-window rule on $(d_n,\ell_n)$-history can determine it either.

### Why (b)/a direct transplant fails: no recurrence-intrinsic frozen quantity
`aimo-0678`'s $s_n=a_n+b_n$ is exactly conserved by the two-term recurrence
itself, independent of the unknown target. Here, legality of $a_{n+1}$ is
tested against the **entire, variable-length prefix** $a_1,\dots,a_n$, not a
bounded companion state; the relevant datum ($S_n(p,M)$, which primes have
hit which residues so far) can only grow with $n$
(`prefix-support-stabilization.md`), never resetting to a fixed frozen
scalar via a bounded two-term update.

### Consequence
Any substitute for ingredient (a) must read the cumulative state $a_n\bmod
\mathrm{lcm}(Q,M)$ directly — but this is exactly the state
`state-compactness-pigeonhole`'s $\mathrm{Good}_Q$ framing already tracks,
so a genuine substitute here reduces to the same open central existence
question, not a strictly smaller sub-problem.

### Caveat
This rules out the *literal* `aimo-0678` two-ingredient mechanism (and both
of its natural repairs — a uniform-over-$M$ version, and an $M$-independent
frozen-scalar version) for any residue-pattern-tracking monovariant of this
shape. It does not rule out every possible monovariant construction.

### Provenance
Proved in `approaches/frozen-invariant-monovariant.md`, §3.2–3.3 and §4,
round 5. Independently reviewed by the proof-reviewer: the core "same
cycling argument transplants" step is a legitimate direct application of
the standard fact that an eventually-arithmetic-progression sequence is
periodic mod any fixed modulus with period modulus$/\gcd$(common
difference, modulus) — correct, though stated somewhat tersely in the
source file.
