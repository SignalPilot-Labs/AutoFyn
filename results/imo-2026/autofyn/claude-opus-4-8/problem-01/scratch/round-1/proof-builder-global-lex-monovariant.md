# Build report — global-lex-monovariant (imo-2026-01), round 1

Status: **solved**. Full rigorous proof of both parts written to
`results/imo-2026-01/approaches/global-lex-monovariant.md`.

## What was closed
- **GAP A1** — Lemma 1 nails P_new = P_old/gcd(m,n): P non-increasing always, strict iff gcd>1, unchanged iff gcd=1. Lemma 3 gives the airtight lex descent with the reviewer's exact phrasing ("N non-increasing every move; if N unchanged then gcd>1 so P strictly drops"), and explicitly notes a non-coprime move may also drop N (harmless). Confirmed: no move leaves both N and P fixed.
- **GAP A2** — Lemma 4 proves well-foundedness of lex on ℤ_{≥0}×ℤ_{≥1} from scratch (first coord eventually constant ⇒ strictly decreasing positive-integer second coord, impossible), plus an explicit finite move bound.
- **GAP B1** — subtractive identity gcd(min(a,b),|a−b|)=gcd(a,b) fully case-split: a=b, a=0, b=0, a>b>0, b>a>0. Exhaustive.
- **GAP B2** — associativity/commutativity of gcd over the zero-containing multiset, isolating the changed pair.
- **GAP B3 / N=0 exclusion** — Lemma 5′ imports the g_p invariant (positivity of some initial g_p from x_1>1) to rule out the all-ones terminal state. No circularity: Lemma 6 (invariant) is proved independently of termination.
- Part (b) conclusion: v_p(M)=g_p^initial for all p ⇒ M = ∏_p p^{gcd(v_p(x_i))}, function of the initial board only.

## Verification
Random simulation (3000 boards × 4 plays each) confirms: every play ends with exactly one entry >1, and it always equals ∏_p p^{gcd_i v_p(x_i)}. (Sanity check only; the written proof is self-contained.)

## Spec concerns
None. Every case settled, every invoked fact named (Fundamental Theorem of Arithmetic / unique factorization, gcd·lcm=mn, Euclidean subtraction). No residual gaps.

## Promotable lemmas
- Lemma 6: per-prime valuation-gcd g_p invariant under the gcd/lcm move.
- Subtractive identity (B1): gcd(min(a,b),|a−b|)=gcd(a,b) for all a,b≥0.
- Lemma 1 + Lemma 3: product update and lex descent of Φ=(N,P).
