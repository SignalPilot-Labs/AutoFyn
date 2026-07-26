# proof-builder role rules

ALWAYS: when a reviewer flags a specific edge case (e.g. n=2 / equilateral failing a "A >= bound" argument), rewrite that sub-lemma with the direct inequality that actually holds (C < 90 < A+C) rather than patching the broken bound — the direct argument is both cleaner and correct (round 1, lattice-coset-descent).

NEVER: use "open interval of length >= theta contains a multiple" without checking strictness — an interval of length EXACTLY theta can miss all lattice points (e.g. (0,theta)); require strict length > theta OR use the ceiling trick m=ceil(C/theta) which handles the boundary cleanly (round 1).

ALWAYS: When a construction picks an element satisfying several conditions (e.g. a pairing u,v with d(u)<v AND an extra constraint like m_u<=n-1), verify computationally that the REFINED statement (with all conditions) still holds, then re-prove the lemma WITH the constraint — the unrefined lemma may hold while the refined version needs a separate case split (round 1, imo-2026-04 safe-unsafe-pairing: the bare pairing held, but the cut needed m_u<=n-1 to avoid a degenerate zero angle; the refined lemma also held but needed a separate "top angle" m=n case analysis).

ALWAYS: When a deficit/round-up function is used, fix the convention explicitly (ceil vs min{m:m*theta>=x}) and check the boundary d(x)=0 / d(x)=theta cases — they determine which angles are "already won" vs "safe" (round 1, imo-2026-04).

NEVER: assume the pairing lemma's chosen element automatically satisfies a secondary constraint needed downstream — the cut may silently produce a degenerate (zero) angle if the constraint isn't enforced (round 1, imo-2026-04: m_u=n would give (n-m_u)theta=0, a non-angle).
