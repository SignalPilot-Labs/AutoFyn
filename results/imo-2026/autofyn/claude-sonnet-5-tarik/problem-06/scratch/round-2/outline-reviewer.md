## imo-2026-06 — outline-reviewer, round 2

### Headline finding (verified rigorously + numerically, not asserted): `backbone-existence-crt`'s round-2 "correction" (⋆) is ALSO FALSE — the field made the same false-formalization mistake one level down, and this round's fix accidentally landed on the wrong reformulation. `persistent-backbone-monovariant`'s canonical-minimal-witness target, by contrast, checks out empirically as the correct reformulation.

**Proof that (⋆) is false, not merely unproven.** `(⋆)` defines `B := {p prime : p ∣ a_n for infinitely many n}` and claims `B` is finite. This is false whenever the problem's own conclusion holds: fix a residue class of the eventual periodic pattern, `a_r, a_r+L, a_r+2L, \dots` (an infinite AP with common difference `L`). For **any** prime `q` with `\gcd(q,L)=1`, the congruence `a_r+kL\equiv0\pmod q` has a unique solution `k\bmod q` (since `L` is invertible mod `q`), so **every** prime coprime to `L` that ever divides *any* term of that AP divides **infinitely many** terms of it (periodically, once every `q` steps). Since `a_r+kL\to\infty` picks up unboundedly many distinct prime factors as `k\to\infty` (ordinary size growth), essentially every prime not dividing `L` eventually appears in `B`. I verified this is not just a theoretical worry but the actual state of affairs, on the already-solved `a_1=15` case (`T=8,L=30`, tail primes `\{2,3,5\}` per `current.md`): sampling one residue class alone, the count of distinct primes in `B` grows **without bound** — 24, 77, 167, 302, 429, 549 across increasing sample windows of the very same residue class (script below) — with zero sign of leveling off, exactly as the theory predicts (only primes dividing `L=30` are excluded from this mechanism, so `B` is essentially *cofinite*, the polar opposite of finite). **This is the identical bug pattern the round-2 explorer caught in `H_n`** (conflating "any prime that ever divides a term" with "the causally load-bearing/dominant prime"), just moved from "co-occurrence at a pair" to "cofinite/infinite recurrence" — both are far too weak a filter to be finite. Do not let a builder spend effort proving `(⋆)` as currently stated in `backbone-existence-crt.md` Section 3 — it cannot succeed.

```python
import math
def simulate(a1, n):
    a=[a1]; x=a1+1
    while len(a)<n:
        if all(math.gcd(x,ai)>1 for ai in a): a.append(x)
        x+=1
    return a
from sympy import factorint
seq = simulate(15, 16000); T=8
cls = seq[0::T]              # one residue class of the periodic tail
ps=set()
for i,v in enumerate(cls):
    ps |= set(factorint(v).keys())
    if (i+1) in (50,200,500,1000,1500,2000): print(i+1, len(ps))
# -> 24, 77, 167, 302, 429, 549 (unbounded growth, not stabilizing)
```

**In sharp contrast**, `persistent-backbone-monovariant`'s canonical-minimal-witness reformulation `w(i,j):=\min(\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j))`, target `\bigcup_n\{w(i,n):i<n\}` finite, is **empirically exactly right**: exhaustively computing `w(i,j)` for **all** ~4.5 million pairs `1\le i<j\le3000` on `a_1=15` gives witness set **exactly `{2,3,5}`**, no exceptions. Testing `a_1\in\{247,1001,65\}` up to `n=3500` (dense, not sampled) shows the witness set stabilizes **early** (by `n\approx500$–$1000`) and stays exactly constant afterward — including for the notoriously hard `a_1=247` stress case where periodicity itself hasn't even been detected within thousands of terms. This is strong, load-bearing evidence that the *right* notion of "backbone" for this problem is the canonical-minimal-witness set, not "any co-occurring prime" (falsified round 1) and not "primes dividing infinitely many terms" (falsified above). Recommend the outliner have `backbone-existence-crt` (and `intersecting-family-covering-construction`'s Step 4) retarget onto **this** notion rather than `(\star)`/`B` as currently written.

```python
# exhaustive check, a_1=15, i<j<=3000: witness set is exactly {2,3,5}, no exceptions
# (spf = smallest prime factor of gcd(seq[i],seq[j]))
```

---

### `backbone-existence-crt` — RETHINK (Step 3 only; Sections 1/2/4 remain valid and certified)

- **Sections 1, 2, 4 (Lemma P, Lemma P′, Lemma Q, Domination Lemma) are sound**, already certified in `lemmas/`, re-spot-checked here (Domination Lemma's union-bound argument is a correct, elementary pigeonhole; Lemma Q's induction is a correct minimality argument). No issue.
- **Section 3's retargeted `(\star)` is mathematically false**, as proven above — not merely hard, actually false, for the same underlying reason (using a too-permissive notion of "which primes matter") that killed round 1's `H_n`. Steps 3a–3c/3c′ are all built on top of `(\star)`, so the entire new Step-3 skeleton this round is dead on arrival; a builder cannot productively "attempt" 3c (second-moment concentration) — there is nothing to concentrate, since `B` is (essentially) cofinite, not finite. This is a fatal flaw in the specific formalization, not in the approach's general mechanism (counting/density is still a legitimate technique for *some* correctly-posed target).
- **What to change**: retarget Step 3 onto the canonical-minimal-witness set `\bigcup_n\{w(i,n):i<n\}` (borrowed/shared with `persistent-backbone-monovariant`'s Step 3, empirically validated above) instead of `B`. The Domination Lemma and the `O(\log n)` bound (3b) may well still be adaptable to this corrected target (both are about "which prime dominates a step," which is closer in spirit to `w(i,j)` than to `B`) — but this needs to be re-derived against the *correct* target, not assumed to transfer.
- **Section 6 discussion is fine as a correction** (accurately diagnoses `aimo-0648`'s Bezout device doesn't transfer) and should be retained for the next round.
- Per CLAUDE.md's per-approach routing, this is RETHINK for the slug's current outline content: send back to the outliner with the specific fix above; do not dispatch a builder against the current Step 3 this round. The slug's already-certified content (Lemma P/P′/Q/Domination Lemma) remains in the shared lemma cache regardless.

### `persistent-backbone-monovariant` — APPROVE (strongest candidate this round)

- **Lemma C (Global Intersection Collapse) is fully sound.** I independently re-derived the "iff Case I" step: since `(C_n)` is non-increasing from `n=1` (not just from `N_0`), `C_\infty\subseteq C_n` holds for **every** `n\ge1`, so `p\in C_\infty` forces `p\in C_n=\bigcap_{i\le n}\mathrm{rad}(a_i)` for every `n`, hence `p\mid a_i` for every fixed `i` (take `n\ge i`) — this is Case I, correctly proven, not hand-waved. The stabilization argument itself (nested subsets of a finite set) is a standard, valid finite-descent argument. I also independently re-verified the round-2 self-correction (the naive bound `N_0\le|P_1|+1` is false): for `a_1=65`, `k=|P_1|=2` but `C_n` doesn't empty until `n=4>k+1=3` (confirmed by direct computation: `C_1=\{5,13\}, C_2=\{5\}, C_3=\{5\}, C_4=\emptyset`). Good — the outline's self-correction is real, not just asserted.
- **The Step 4 well-ordering mechanism is honestly disclosed as open/exploratory**, not claimed as proven ("Not completed... honestly exploratory," "Open task for the builder"). This satisfies CLAUDE.md's "distinguish proved from conjectured" rule — it is not a case of a plausible-sounding-but-unsound hand-off; the outline is explicit that this is the load-bearing open content. No violation.
- **Crucially, the *target* of Step 4 (finiteness of `\bigcup_n\{w(i,n)\}`) is the one target in the whole field I could empirically validate as plausible-and-likely-true** (see Headline Finding above) — unlike the sibling's `(\star)`, which I disproved. This makes this approach's remaining gap "hard but probably true," rather than "provably false," a meaningfully better position.
- One point to flag for the builder: the fallback sub-goal (`\mu_n:=\max\{w(i,m):i<m\le n\}` eventually constant) is weaker and may be easier to attempt first, as the outline itself suggests — good triage, keep it.
- Verdict: APPROVE. This is now the most promising live gap-target in the population; dispatch a builder to (a) certify Lemma C first (cheap, essentially done), (b) attempt the well-ordering argument on the canonical-witness target, using the fallback `\mu_n` monovariant if the full argument doesn't close.

### `intersecting-family-covering-construction` — CHANGES REQUESTED

- **Sections importing Lemma P, Q, R, S′ and Proposition D (the Case I/II dichotomy) remain sound**, already certified from round 1 (re-spot-checked: Lemma S′'s minimality argument, and the `a_1=33` trace claim — independently verified `\gcd(44,33)=11>1` but `\gcd(44,39)=1`, i.e. candidate 44 passes the `a_1` check yet is correctly rejected only via `a_3` — confirms the outline's claim that even Case I's proof implicitly needs full per-index history, not just `a_1`).
- **The new Step 5 strong-induction-from-`n=1` architecture is a real skeleton, not hand-waving.** The invariant `I(n)` is concretely specified (residue-pattern match + "every admissibility check up to `n` is witnessed by a prime in `H`"), and the inductive step is broken into two genuinely distinct, correctly-identified sub-claims: (a) the `H`-forced candidate is admissible against every earlier term (uses the inductive hypothesis correctly, not circularly — it leans on `I(n)`'s clause about *earlier* terms' covering primes, which is available by induction, not assumed for the current step), and (b) no smaller candidate is admissible (correctly flagged as needing appeal to specific earlier indices, backed by the `a_1=33` trace evidence above, not just a compressed residue state). This mirrors Lemma S′'s legitimate architecture and is a defensible generalization plan, not vague "then it follows."
- **However, Step 4's characterization of `H` inherits the same false claim as `backbone-existence-crt`**: "`H` must ultimately equal the persistent divisor set `B`... import that result once proved" — since `B` (as literally defined) is not finite (Headline Finding), this specific hand-off is broken. This does **not** invalidate Step 5's induction machinery (which only needs *some* finite `H`, however characterized, to exist and be identified early — it does not depend on `H` being literally equal to `B`), but the outline as written currently commits to importing a false result and must be corrected before/during building: `H` should be characterized via (or aligned with) the canonical-minimal-witness notion validated above, not `B`.
- **What to change**: strike the "`H` must ultimately equal `B`" claim; instead take `H := \bigcup_n\{w(i,n):i<n\}` (shared target with `persistent-backbone-monovariant`, pending that approach's proof of finiteness) or, for immediate builder progress, hand-derive `H=\{2,3,5\}` for the concrete `a_1=15` test case (as the outline's own "concrete first test case" already recommends) and attempt Step 5's induction on that concrete instance first, independent of whether general finiteness is proved yet — this is legitimate incremental progress (prove `I(n)` for one worked Case-II example) even before the general backbone-finiteness gap closes.
- Verdict: CHANGES REQUESTED — real, sound architecture with one identified, fixable mislabeling (H≠B by name; use the corrected target or a concrete worked instance). Not fatal, not RETHINK.

### `bounded-gap-density-covering` — no change (parked)

No new skeleton this round, correctly left parked per the outliner's own note; Lemma 1 remains certified and reusable (already imported by all three live approaches, including as the interval-packing input to `backbone-existence-crt`'s 3b and to `persistent-backbone-monovariant`'s Lemma C context). No action needed; do not resurrect its original Step 3 strategy (round-1 dead end, unchanged).

### Diversity check

The field's mechanisms remain genuinely distinct at the technique level (counting/density vs. explicit-construction/induction vs. well-ordering/monovariant), consistent with prior rounds' diversity push. But this round surfaces a sharper diagnosis than "distinct techniques hitting one wall": two of the three approaches were built this round on a target lemma (`(\star)`/`B`) that is **actually false**, while the third (opened specifically to diversify mechanism) *independently arrived at, and empirically validated, the correct target* (canonical-minimal-witness finiteness). This is not a coincidence to be papered over — the field should now converge its *target*, not its technique, onto the canonical-witness formulation, while keeping the three distinct mechanisms (density/counting, explicit construction, well-ordering) racing to prove finiteness of the *same, now-correct* set. Recommend next round's outliner explicitly re-point `backbone-existence-crt`'s Step 3 and `intersecting-family-covering-construction`'s Step 4 at `\bigcup_n\{w(i,n):i<n\}`.

### Lemma soundness spot-checks performed this round
- Domination Lemma (`backbone-existence-crt` Section 4): re-verified the union-bound proof is correct and elementary. Sound.
- Lemma C (`persistent-backbone-monovariant`): re-derived the "iff" step in full; sound. Re-verified the `a_1=65`, `N_0=4>k+1=3` counterexample to the naive bound by direct computation; the outline's self-correction is accurate.
- Canonical-minimal-witness target: verified exhaustively finite on `a_1=15` (all ~4.5M pairs up to `n=3000`, witness set exactly `\{2,3,5\}`) and stable-early on `a_1\in\{247,1001,65\}` up to `n=3500`. This is the round's most important new empirical fact for the field.
- `(\star)`/`B` (`backbone-existence-crt` Section 3): proved false both theoretically (AP-density argument) and numerically (unbounded, likely-cofinite growth on the already-solved `a_1=15` case).
- `a_1=33` trace (`intersecting-family-covering-construction`): re-verified `\gcd(44,33)=11`, `\gcd(44,39)=1` by direct computation; claim accurate.

build set: persistent-backbone-monovariant, intersecting-family-covering-construction
