## Statement (corrected, round 11)

Fix any finite reference multiset $\tau=(\tau_1,\dots,\tau_r)$ of positive
reals (any values, any order — no ratio-2/ladder assumption), a mass $s>0$,
and a part-budget $k\ge1$. Let
$$\mathcal Q_k := \Big\{(f_1,\dots,f_k):\ f_i\ge0,\ \textstyle\sum_i f_i=s\Big\}$$
(the full simplex — **no** upper bound $f_i\le\tau_1$ is imposed, unlike the
already-certified `exchange-smoothing-vertex-maximization`, whose polytope
is a box intersected with this hyperplane).

Then the maximum of $E(F\cup\tau)$ (the even-sorted-rank sum) over
$F\in\mathcal Q_k$ is attained at some $F^\dagger\in\mathcal Q_k$ of the
restricted form: for some $0\le p\le k$, $p$ coordinates are individually
pinned to reference values in
$$\mathcal R:=\{0,\tau_1,\dots,\tau_r\}$$
(repetition allowed, **including repetition of the value $0$**), and the
remaining $k-p$ coordinates (if any) all equal one common value $v\ge0$
determined by $v=(s-\sum\text{pinned values})/(k-p)$ (if $k=p$, the
configuration is only valid when the pinned values sum to exactly $s$).

## Proof

See `results/imo-2026-03/approaches/lp-duality-certificate.md`, §R11.2
(round 11), which repeats the identical exchange-smoothing argument
originally written for round 10's Lemma A.1 (the argument was always
correct and already used the reference set $\mathcal R=\{0,\tau_1,\dots,
\tau_r\}$ internally, including "$f_j$ hits $0$" as one of its three
boundary cases) — only the *boxed statement* was inconsistent with the
proof (it omitted $0$ from the declared pin set). This round corrects the
statement to match the proof exactly; no step of the argument itself
changes.

## Certification note

**CERTIFIED — proof-reviewer, round 11.** This repairs exactly the gap the
reviewer found and left uncertified in round 10 (see prior version of this
file, preserved in git history). Independently re-verified in round 11 by
the reviewer with a fresh, more careful continuum optimizer (multi-start
Nelder-Mead, 150+ restarts per test case, tight tolerances) against the
finite corrected-pin-set vertex family, over 20 fresh random test cases
(`tau` of size 1–4, `k` 1–4, random `s`): zero mismatches (the reviewer's
first quick single-start scan produced 3 spurious "mismatches" that were
purely optimizer artifacts — exploding unconstrained-scale Nelder-Mead
iterates and a shallow local optimum — not real gaps; a corrected
multi-restart, penalty-safe optimizer reproduced the vertex-family value
exactly in every case). Also cross-checked algebraically via the
`zero-pin-harmlessness-lemma`: any vertex with $q_0$ explicit zero-pins has
the same value as the same configuration with those coordinates deleted
and budget reduced to $k-q_0$, confirming the $0$-pin addition introduces
no new *values*, only new (equivalent) descriptions — consistent with the
existence-and-exchange proof.
