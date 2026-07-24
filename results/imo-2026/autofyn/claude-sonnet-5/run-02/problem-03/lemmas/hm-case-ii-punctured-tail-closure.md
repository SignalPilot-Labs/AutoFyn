## Statement (CERTIFIED — round 32, proof-reviewer)

**Theorem (h(m) Vertex $c=t\in S''$, Case (ii) closure).** Let $m\ge3$ and
let $\{q_1,\dots,q_{m+1}\}$ be the unit ratio-2 ladder ($q_i=2q_{i+1}$,
$\sum_{i=1}^{m+1}q_i=1$, $f(m):=q_{m+1}=1/(2^{m+1}-1)$). Let $S''$ be any
legal $\le(m-2)$-cut refinement of the tail $\{q_2,\dots,q_{m+1}\}$ that
leaves $q_2$ untouched (i.e. $q_2\in S''$ exactly, and the remaining
$\le(m-2)$ cuts are spent refining $\{q_3,\dots,q_{m+1}\}$). Then for every
$t\in S''\setminus\{q_2\}$,
$$A\big(\{q_2\}\cup(S''\setminus\{t,q_2\})\big)\ \ge\ f(m)+t\ >\ f(m).$$

## Proof

1. **Mass conservation.** Since $S''\setminus\{q_2\}$ is a legal refinement
   of $\{q_3,\dots,q_{m+1}\}$ (cuts, which preserve total sum), $\mathrm{Total}
   (S''\setminus\{q_2\}) = \sum_{i=3}^{m+1}q_i$.
2. **Shifted telescoping identity.** $\sum_{i=3}^{m+1}q_i = q_2-f(m)$, by the
   same geometric-sum/ratio-2 argument as the certified level-1 identity
   $\sum_{i=2}^{m+1}q_i=q_1-f(m)$, shifted one index down ($q_3=q_2/2$, and
   $q_3\cdot2^{-(m-2)}=q_{m+1}=f(m)$).
3. **Remove $t>0$:** $\mathrm{Total}(S''\setminus\{t,q_2\}) = q_2-f(m)-t$.
4. **Fact 2** (`fact-2-alternating-sum-leq-total`, certified): $A(S''
   \setminus\{t,q_2\}) \le \mathrm{Total}(S''\setminus\{t,q_2\}) = q_2-f(m)-t$.
5. **Peel $q_2$ off** via `sharp-dominant-removal-identity` (every element
   of $S''\setminus\{t,q_2\}$ is a fragment of the tail from index $3$ on,
   hence $\le q_3 <q_2$, so $q_2$ strictly dominates):
   $$A\big(\{q_2\}\cup(S''\setminus\{t,q_2\})\big) = q_2-A(S''\setminus\{t,q_2\})
   \ \ge\ q_2-(q_2-f(m)-t) = f(m)+t.$$
   $\blacksquare$

## Verification

Independently re-derived by the proof-reviewer (round 32): confirmed the
telescoping identity by hand and cross-checked the full inequality with a
fresh exact-`Fraction` script (3000 random legal refinements per $m$,
$m=3,\dots,7$), zero violations, worst-case slack $\to0$ as $t\to0^+$ as
predicted by the tight bound $f(m)+t$.

## Origin / usage

Proved in `results/imo-2026-03/approaches/greedy-halving-adversary.md`,
round 32 ("Round 32: Case (ii) closed unconditionally, every $m\ge3$").
Combined with the round-31 closure of the "$t=q_2$ untouched" sub-case of
Case (i) and a direct $m=3$-specific hand enumeration of the "$q_2$ itself
split" residual (Type A), this fully closes $h(3)$'s entire
"simultaneous $q_1$-cut and tail-refinement" vertex piece (modulo the same
standing $(\star_3)$ dependency used throughout the rest of the file's
induction scaffolding — note $(\star_3)=\mathrm{MinFloor}(4)$ is itself
already fully, unconditionally certified as of round 31, so this
dependency is in fact already discharged; the approach file's own text is
conservative on this point and could be strengthened to state $h(3)$'s
closure as fully unconditional in a future round).
