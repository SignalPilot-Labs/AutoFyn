## imo-2026-06

State of play (verified against certified files): the whole theorem is certified-equivalent to a
single magnitude bound — **every prime in a ⊆-minimal support is bounded by an a₁-only constant**
(equiv. E4 cardinality bound `sup|G|<∞`, equiv. E5″ companion-radical `∏(G∖{p_max})<a₁`). Four
framings (antichain-E5″, anchor-partition, value-stream, formation-window) all bottom out on the
same wall, and R4 certified a Collapse theorem: any lever closing via "realize a proper sub-support
`S⊊G` as a term to contradict minimality" collapses verbatim to E5. Both R5 explorers reconfirmed
the wall and found the covering/density and aimo-0421 levers vacuous or collapsing.

**Honest field assessment (do not re-seed a doomed pole).** I searched for a genuinely-different
top-level framing that does NOT route through a forbidden lever. Every candidate collapses:
- "A eventually periodic" (weaker target, memory rule 7): for the *actual* greedy sequence, A
  periodic ⟺ Π finite (the obstruction family that separates them is non-realizable, fails E2), so
  the weaker target coincides with the crux; the automaton route already attempted it and collapsed.
- density/covering on A: certified dead (monovariant obstruction, re-verified R5).
- aimo-0421 fiber dichotomy: empirically vacuous (every recruited prime has positive-density fiber).
- CRT/interval-covering on `[a₁,C·a₁]`: routes back to sub-support realization (forbidden).
So I keep the field **focused on the leader's one un-forked opening** rather than seeding a pole
proven to die. The field is deliberately small (2 real slugs) and honest.

---

realizer-index-joint-double-count: new
Target: the FULL theorem — proves the Crux (Finite Alphabet, `𝓐_∞` finite) directly via the
  magnitude bound "primes in minimal supports ≤ C(a₁)", then §4–§5 (certified) give
  `a_{n+T}=a_n+L` for all n≥1 with `T=|ρ(A)|`, `L=∏Π`. This is a RIVAL endgame to the leader:
  it bypasses E5″/E5-cardinality (companion-radical route) entirely and attacks R2's magnitude
  bound `q≤C(a₁)` through a potential on the JOINT system of first realizers — the one opening both
  R5 explorers flagged as un-forked and far from the exhausted sub-support route.
Technique: proof by contradiction + Pigeonhole/extremal on the JOINT system of all minimal
  supports + certified E1/E2(⇒)/E3/R1/Anchor/Distance-prime. Spine: E3 gives a LOWER bound
  `q ≤ |t−t'|` on the private-witness pair; supply an a₁-only UPPER bound on `|t−t'|` from a
  double-count/potential over ALL witness pairs simultaneously (not on a single G or window).
Skeleton:
  1. Assume the magnitude bound fails ⇒ (certified reduction, `enumeration-and-transversal.md` §Reduction
     + E4) `𝓐_∞` infinite with unbounded primes. — by contradiction hypothesis.
  2. Anchor collapse (certified §8.1): fix `p*∈P=primes(a₁)` and a strictly increasing sequence of
     minimal supports `G_k∈𝓐_∞` with `p*∈G_k` and `q_k:=p_max(G_k)→∞`. — Anchor (L1) + Pigeonhole
     over finite P + antichain forcing distinct large primes.
  3. Two-anchor witness scaffold (NEW, rigorous from certified lemmas): by E3 take private witness
     `H_k:=H_{q_k}∈𝓐_∞` with `G_k∩H_k={q_k}`. Since `p*∈G_k` and `p*≠q_k`, `p*∉H_k`. By Anchor
     `H_k∩P≠∅`, so `H_k` contains some `p'_k∈P∖{p*}`; Pigeonhole over finite `P∖{p*}` ⇒ fix a single
     `p**∈P∖{p*}` with `p**∈H_k` for infinitely many k. Pass to that subsequence. — Anchor +
     Pigeonhole (both certified/KB). NET: `p*∈G_k∖H_k`, `p**∈H_k∖G_k`, `q_k∈G_k∩H_k` the only shared prime.
  4. Realizer pair: `t_k:=u(G_k)` and `t'_k:=u(H_k)` are genuine terms (R1), with `p*·q_k∣t_k`,
     `p**·q_k∣t'_k`, and `gcd(t_k,t'_k)=q_k^{m}`. Distance–prime (L3) ⇒ `q_k∣(t_k−t'_k)`, so
     `|t_k−t'_k|≥q_k→∞`. — certified R1 + E3 + L3.
  5. **[GAP — Lemma J]** An a₁-only UPPER bound on the witness-pair spread:
     `|t_k−t'_k| ≤ C(a₁)` for infinitely many k. — see Key lemmas.
  6. Contradiction: steps 4 and 5 give `q_k ≤ |t_k−t'_k| ≤ C(a₁)` for all k in an infinite set,
     contradicting `q_k→∞`. Hence the magnitude bound holds ⇒ `𝓐_∞⊆2^{primes≤C(a₁)}` finite ⇒ Crux
     ⇒ theorem via §4–§5. — direct.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Two-anchor scaffold (step 3) — because a private witness of the LARGE prime `q_k` must exclude
    `G_k`'s small anchor `p*` (they share only `q_k`), yet must itself meet the finite anchor set P,
    forcing a SECOND fixed anchor `p**` by Pigeonhole; this is fully proved from certified E3+Anchor
    and is the genuinely new structural content this slug contributes (rigorous, not a gap).
  - **Lemma J (the single open gap): the first-realizer pair `(t_k,t'_k)` has a₁-only bounded
    spread.** Candidate mechanism (the thing to attempt): a JOINT potential/double-count, NOT a
    bound on either endpoint. Both `t_k,t'_k` are FIRST realizers (smallest term of their support
    `≥a₁`); with the two fixed anchors `p*,p**` and `t_k≡t'_k (mod q_k)`, count first-realizers
    against the fixed resource `Z/(p*·p**)` × value-window structure: the pairs' index-intervals
    `[i(H_k),i(G_k)]` each have length `≥q_k/M` (Distance–prime), so if the double-count forces these
    intervals to overlap / share a bounded common region (via the two anchors both being active in a
    bounded set of residues), the spread cannot grow — turning "infinitely many pairs with unbounded
    spread" into a resource-overflow contradiction.
Open gaps: step 5 (Lemma J). Steps 1–4 and 6 are rigorous from certified lemmas.
Cases to cover: none beyond the single contradiction line (the two-anchor scaffold already handles
  |G|≥2; the |G|=1 case `G={q}` is killed by L3 as in §8.2 — a bare-prime minimal support forces
  `q|a_n` for all n, contradicting `q≤|a_i−a_j|` bounded, so p_max sits in a support of size ≥2).
Watch out for:
  - CIRCULARITY (memory rule 11): Lemma J must bound the RELATIVE spread `|t_k−t'_k|` from a joint
    invariant, NOT bound an individual `u(G_k)` or its index — bounding a single first-realizer value
    is equivalent to bounding `∏G_k`, i.e. circular. Keep the potential relational (two anchors, the
    shared-`q_k` congruence), never per-support.
  - FORK RISK (formation-window R5): if Lemma J is attacked by "in the window between `t'_k` and
    `t_k` the greedy rule rejected a smaller candidate," it collapses to the forbidden sub-support
    lever. The scaffold is designed to avoid this: it targets the spread via the STATIC two-anchor
    counting resource, not via rejection timing. If the build finds J unavoidably needs rejection
    timing, that is a genuine RETHINK finding (records the last un-forked opening as forked) — report
    it honestly rather than forcing the forbidden move.
  - Distance–prime gives the WRONG-direction bound by itself (lower, not upper, on spread) — J must
    come from the joint count, and L3 is used only for the lower bound in step 4 and the index-length
    of intervals in the count.

---

redundant-constraint-antichain: advance
Target: the FULL theorem (unchanged) — reduced to residual E5″ (`∏(G∖{p_max})<a₁` for minimal `G`
  with `∏G≥a₁`), the small-radical regime `∏G<a₁` fully closed (Prop 12.A), pincer lower jaw R1/R2
  certified.
Technique: aimo-0447 realizer-value pincer; E4/E5/E5″ chain (all certified except E5″).
Skeleton: unchanged, complete conditional on E5″ (see approach file §12); §4–§5 endgame certified.
Open gaps: E5″ only. NOTE FOR THE REVIEWER: both R5 explorers found NO new non-forbidden lever for
  E5″ in its companion-radical form (every attempt forks to sub-support realization). This slug is
  nominated to stay LIVE as the certified furthest-forward (Elo 1607), not because a new E5″ lever
  was found this round. If a builder is spent here, the only non-forbidden micro-target is to
  certify the two-anchor scaffold (step 3 of the sibling slug) as a shared lemma for reuse — but the
  substantive new bet is `realizer-index-joint-double-count`, which should get the primary builder.
Cases to cover: none new.
Watch out for: do NOT re-attempt the sub-support-realization closure of E5″ (proven-collapse, R4);
  do NOT frame E5″ as "bound `u(G)≤U(a₁)`" (circular, memory rule 11).

---

**Field summary for the outline-reviewer.** Primary new bet: `realizer-index-joint-double-count`
(the un-forked joint-system realizer-index opening; new rigorous two-anchor scaffold + single gap
Lemma J, a RELATIONAL spread bound explicitly guarded against both circularity and the sub-support
fork). Advance: `redundant-constraint-antichain` (leader, stays live as furthest-forward; no new
E5″ lever found — nominated so the certified line is not lost). I deliberately did NOT open a
different-framing pole: every candidate provably collapses to a forbidden lever, and per the plateau
rule's contingency the responsible move is to concentrate on the one opening that is genuinely far
from the exhausted sub-support route, not to re-seed a doomed pole. Suggested build set:
`realizer-index-joint-double-count` (primary), `redundant-constraint-antichain` (advance).
