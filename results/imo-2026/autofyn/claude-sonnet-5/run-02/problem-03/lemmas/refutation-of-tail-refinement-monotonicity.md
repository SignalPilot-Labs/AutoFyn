## Statement (DEAD-END RECORD, not a positive reusable lemma)

The round-5 outline's claim (B) — "for fixed $F$ (Xiang Yu's partition of
$p_1$), spending any cut refining the tail instead of fragmenting $p_1$
further can only weakly increase $A(F\cup G')$" — is **FALSE** when $F$
ranges over arbitrary (in particular non-claim-(A)-optimal) partitions of
$p_1$.

**Counterexample.** $n=2$ ladder ($p_1=4/7,p_2=2/7,p_3=1/7$), $F=\{p_1\}$
(untouched top piece, $c=0$). Splitting the tail's last piece $p_3$ into
$f_1=1/10,\ f_2=3/70$ (any positive split works, per
`single-cut-perturbation-identity`): $A(\{p_1\}\cup\{p_2,p_3\})=3/7 \to
A(\{p_1,p_2,f_1,f_2\})=12/35=3/7-3/35$, a **strict decrease** — refining the
tail here strictly *helps* Xiang Yu.

## Verification (proof-reviewer, round 5)

Independently re-verified by exact `Fraction` arithmetic: $A(\{4/7\}\cup
\{2/7,1/7\})=3/7$ exactly; $A(\{4/7,2/7,1/10,3/70\})=12/35$ exactly (both
computed by direct sort-and-alternating-sum, matching the builder's claim
and the predicted value from `single-cut-perturbation-identity`). Confirmed
genuine and correct.

## Why this matters

This does **not** endanger the already-closed $n=2$ result (both values
$3/7,12/35$ are far above the target $a_2=1/7$). It does mean claim (B), as
literally stated for arbitrary $F$, cannot be used to finish the general
lower bound — a correct replacement must be restricted (e.g. to $F$ already
at or near its own claim-(A) optimum) or reformulated as the strictly weaker
"refining the tail cannot push $A$ below claim (A)'s value $a_n$."

## Recorded as

`results/imo-2026-03/approaches/greedy-halving-adversary.md`, Proposition 15
(round 5). Do not re-attempt claim (B) in the "weakly increases $A$, for
every $F$" form — this is refuted, not merely unproven.
