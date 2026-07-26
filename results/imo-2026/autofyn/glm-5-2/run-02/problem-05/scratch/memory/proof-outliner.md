# proof-outliner per-role rules

ALWAYS: when the dispatch specifies the exact slugs and framings for the field, write each approach's skeleton to its own file with the file-contract sections (`## Status = partial`, `## Approaches tried`, `## Current best`, proof-plan skeleton with hard steps marked as explicit **gaps**), then write the field summary to `/tmp/round-1/proof-outliner.md` — do not put the skeletons themselves in the report file (round 1).

ALWAYS: verify the load-bearing algebra of an approach's crux instrument by hand or with a small sympy computation BEFORE writing its skeleton — the explorer reports are "verified" but the outliner is the last gate before the builder (round 1, Fact 5 `|g(z)-g(y)| <= (sqrt(f(z))-sqrt(f(y)))^2` and the partition quadratic closure were re-derived; this surfaced the large-deviation branch gap the explorer had glossed).

NEVER: accept an explorer's "inductively verify |Delta g| <= |Delta t|" hand-wave as a closed step — the induction needs a base case excluding the large-deviation branch of a self-referential quadratic bound; flag it as a gap (round 1, gm-lipschitz-partition G1).

NEVER: present a "send x->infty in (star)" uniqueness argument without checking whether the constant-c residual `(x-y-c)^2 ~ x^2` swallows the perturbation — it does for P5, and the naive aimo-0234 port is doomed until the leading term is canceled by differencing or bypassed by an extremal-value reframe (round 1, asymptotic-vanishing-coefficient G1).

ALWAYS: when an approach's hard gap has multiple candidate closures (e.g. differencing vs. extremal-value reframe), enumerate them in the skeleton so the builder has explicit targets and the reviewer can rank the approach on its best case (round 1, asymptotic-vanishing-coefficient G-1a/G-1b/G-1c).
