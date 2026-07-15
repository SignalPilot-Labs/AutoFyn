# proof-builder — per-role rules

ALWAYS: grep the finished proof file for drafting artifacts ("wait", "…", "TODO", trailing "precisely:") before declaring solved — mid-sentence self-corrections leak into Write calls and an adversarial reviewer will flag them (happened twice in one build, round 1).
ALWAYS: when a proof uses gcd with 0, define gcd of a multiset by its common-divisor characterization (e | all s ⇔ e | d) up front — it makes zero-cases, the fold rule, and "zeros are inert" one-line consequences instead of scattered special cases (round 1).
ALWAYS: order lemmas by use, not by the skeleton's numbering — e.g. prove "lcm/gcd = 1 ⇔ m = n" before any case analysis that cites it; the outline-reviewer checks lemma ordering explicitly (round 1).
ALWAYS: machine-check any worked example embedded in the proof (a hand-computed play had position mixups; the multiset trace was right but only a script confirmed it, round 1).
ALWAYS: test a dispatch-flagged "this invariant might fail" worry with a 10-line script before restructuring the route — the imo-2026-01 worry (Φ({2,3})=1?) rested on confusing gcd(1,0)=1 with min(1,0)=0 and evaporated under one numeric check, saving a fallback rewrite (round 1).
