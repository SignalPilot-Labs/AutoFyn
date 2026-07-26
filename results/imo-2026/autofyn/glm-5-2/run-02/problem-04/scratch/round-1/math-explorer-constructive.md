## imo-2026-04 (route: Mulan's constructive/forward power — which θ are forceable, and the exact angle-triple transform)

### The exact angle-triple transform (derived, verified numerically)

Triangle `T = (X, Y, Z)`, `X+Y+Z = 180°`. Mulan chooses a vertex (call its angle `X`) and a point `P` on the opposite side; the cut from the `X`-vertex to `P` splits `X` into two parts `γ` and `X−γ` (`γ ∈ (0,X)`, Mulan's free real parameter), where `γ` is the part **adjacent to angle `Y`** (so `X−γ` is adjacent to `Z`). The two children are:

- **Child 1 (keeps `Y`):** `(Y, γ, 180−Y−γ)` — angles at the kept vertex, the new small one, and at `P`.
- **Child 2 (keeps `Z`):** `(Z, X−γ, Y+γ)` — using `180−Z−(X−γ) = Y+γ`.

**Load-bearing structural fact:** the two "third angles" `(180−Y−γ)` and `(Y+γ)` are a **supplementary pair** (sum `= 180°`), and Mulan controls where the split lands. Everything in the answer flows from this.

Mulan offers the two children; Shan-Yu discards one. So a move = pick which angle `X` to destroy, pick `γ ∈ (0,X)`; Shan-Yu then chooses whether `Y` or `Z` survives (paired with `γ` or `X−γ` respectively, plus the supplement).

### Distinguish openings (several distinct attacks the outliner could build)

1. **The supplementary-pair / midpoint opening (θ = 90°).** Setting `γ` so both third-angles equal `θ` requires `(180−Y−γ) = (Y+γ) = θ`, i.e. `2θ = 180°` ⇒ `θ = 90°`. This is the **only** value of `θ` for which Mulan can make *both* children carry `θ` in their third-angle slot in one move from an arbitrary triangle. Concretely: pick the largest angle as `X`; the two adjacent angles `Y, Z` satisfy at least one of them `< 90°` (since at most one angle `≥ 90°`); set `γ = 90−Y`. Then child1 third = child2 third = 90°. Depth 1, universal. (Verified: `θ=90` ⇒ max depth 1, all states winning.)

2. **The "create-a-multiple" opening (θ | 180°, general).** More generally Mulan can make **both** third-angles be *multiples of θ* in one move whenever `θ | 180°`: choose `γ ≡ −Y (mod θ)`, so `Y+γ ≡ 0` and `180−Y−γ ≡ 0 (mod 180) ≡ 0 (mod θ)`. Both children then contain a multiple of θ (`pθ` and `(n−p)θ` with `n = 180/θ`). This is the constructive engine for every divisor `θ ≤ 60°`; `θ = 90°` is the `n=2` special case above.

3. **The reduction / descent opening (any `kθ → θ`).** Once a triangle has an angle `= kθ` (`k ≥ 2`), Mulan splits that angle into `(θ, (k−1)θ)` via `γ = θ`. Child1 carries `θ` (Shan-Yu avoids); child2 carries `(k−1)θ`. The surviving child's "multiple-index" strictly decreases `k → k−1`. Iterate to `k = 1` ⇒ angle `= θ` ⇒ win. This is a clean monovariant descent, ≤ `n−2` steps.

4. **The obstruction opening (θ ∤ 180°) — mod-θ invariant.** Let `r = 180 mod θ ∈ (0,θ)` (nonzero by assumption). The set `S = {triangles with no angle a multiple of θ}` is **Shan-Yu-closed**: from any state in `S`, no move makes *both* children have a multiple of `θ`. Four-case mod-`θ` check (see "obstruction proof sketch" below); the fourth case yields `r ≡ 0`, contradiction. Hence Shan-Yu keeps a child in `S` forever, Mulan never even forces a *multiple* of `θ` (let alone `θ` itself). Since Shan-Yu picks the starting triangle, he picks one in `S` (always exists when `θ ∤ 180°`), and Mulan cannot guarantee victory.

### Candidate answer (CONJECTURE — strongly supported by full integer-grid attractor computation, NOT a proof in the real-angle setting yet)

**Mulan guarantees victory iff `θ = 180°/n` for some integer `n ≥ 2`** (i.e. `θ` divides `180°`): `{90°, 60°, 45°, 36°, 30°, 20°, 18°, 15°, 12°, 10°, 9°, 6°, 5°, 4°, 3°, 2°, 1°, …}`.

Evidence (conjecture, integer grid of 2700 sorted triples, γ on integer grid):
- **Every divisor of 180 is a universal win.** Full attractor (least fixpoint of "contains θ OR ∃ move with both children winning") = all 2700 states for `θ ∈ {1,2,3,4,5,6,9,10,12,15,18,20,30,36,45,60,90}`. Max depths: `θ=90→1`, `θ=60→2`, `θ=45→2`, `θ=36→3`, `θ=30→3`, `θ=20→4`, `θ=10→5`, `θ=2→7`, `θ=1→6`. Bounded ⇒ finite.
- **Every non-divisor is a loss.** For `θ ∈ {72, 100, 50, 40, 70, 91, 89, 59, 61, 7, 13, 14, 22, 55, 75, 80, 85, 95, 110, 125, 140, 160, 170, 108, 135, 150}` the winning region equals *exactly* `{states with an angle that is a positive multiple of θ in (0,180)}` (a tiny set, e.g. 72/2700 for `θ=72`), and `0` of the no-multiple states admit a move that makes both children have a multiple. So from a no-multiple start (Shan-Yu's choice) Mulan is forever stuck — confirming the mod-`θ` obstruction empirically.
- **Concrete win, `θ=60`, from the hard state `(2,89,89)`:** Mulan wins in ≤2 moves (max depth 2). Example first move from `(50,55,75)` (no multiple of 60): split `X=50` (max-angle not needed here) with `γ=5` ⇒ children `(5,55,120)` and `(45,60,75)`. Both contain a multiple of 60 (`120 = 2θ`, `60 = θ`). Whichever Shan-Yu keeps: either `60` is present (win) or `120` is present ⇒ split `120→(60,60)`, win next move.

### Candidate technique(s)
- **Invariant / monovariant** (combinatorics knowledge-base entry): the no-multiple-of-`θ` invariant for the obstruction; the `k → k−1` descent on the multiple-index for the constructive reduction.
- **Modular arithmetic over `ℝ/θℤ`** (a real-mod analog of the modular-arithmetic entry): the obstruction is a 4-case residue contradiction; the constructive step picks `γ ≡ −Y (mod θ)`.
- **Casework / exhaustion** + **induction / strong induction on `k`**: split into `θ | 180` vs `θ ∤ 180`, and within the constructive side, induction on `k` in `kθ → (k−1)θ`.
- **Constructive / incremental** (combinatorics entry): explicitly exhibit the family of moves; the answer is a characterization needing both the upper-bound (obstruction) and matching construction.

### Cheap-kill candidates
- The single most load-bearing cheap observation is that the two children's *third angles sum to 180°*. This immediately pins `θ = 90°` (the midpoint) as the unique "one-move universal" value and is the seed of both the constructive `2θ=180` case and the obstruction's case 4 (`r ≡ 0`).
- "Angle = `2θ` ⇒ one-move win by splitting into `(θ,θ)`" — a free base case for the descent.

### Knowledge-base entries to use
- **Invariants & monovariants** (the no-multiple invariant; `k`-descent).
- **Modular arithmetic, CRT** (mod-`θ` residue arithmetic over reals — the 4-case obstruction).
- **Constructive / incremental** + **Induction** (the reduction `kθ → (k−1)θ`; existence of the "create a multiple" move).
- **Casework / exhaustion** (divisor vs non-divisor; `θ ≤ 60` vs `θ = 90` in the constructive existence check).
- **General proof methods: contraposition / contradiction** for the obstruction (assume Mulan has a both-multiple move, derive `r ≡ 0`).

### Analogous past problems (cruxes)
Did not run a full crux-corpus query (time-bounded), but the relevant subtopics to filter in `combinatorics` are **`games-and-strategy`** and **`invariants-and-monovariants`** (and `induction-and-construction`). The load-bearing crux here — "find a closed invariant set for the adversary and a descending monovariant for the constructor" — is the standard skeleton of impartial-game-with-splitting problems. I did not identify a specific 1:1 analogous crux by id; flag this as a gap to fill in a later exploration pass if the outliner wants a template. (Best-guess subtopic filter: `combinatorics/games-and-strategy`.)

### Prior progress
None (round 1; approach pool empty; `current.md` status `unsolved`).

### Dead ends (do not retry)
None recorded yet. One caution from the failed first brute-force: a coarse discretized γ-grid at shallow depth (≤3) reports almost everything as "losing" — that is a discretization artifact, **not** evidence. The trustworthy computation is the **full attractor / least-fixpoint** over the complete integer state space (which I ran); shallow greedy tree search misleads.

### Small-case / intuition notes (labeled CONJECTURE unless proven above)
- The cleanest statement of the winning region, valid for **every** `θ` tested (divisor or not) on the integer grid: *a state is winning iff some angle is a positive multiple of `θ` in `(0,180)`*. When `θ | 180` this set exhausts all states (because of the constructive opening); when `θ ∤ 180` it is a tiny Shan-Yu-avoidable kernel surrounded by the closed "no-multiple" region.
- **Obstruction proof sketch (the crown; passes to outliner as the key lemma to formalize):** `r = 180 mod θ ≠ 0`. State `(X,Y,Z)` in `S` (so `X,Y,Z ≢ 0 mod θ`). For a move to make *both* children have a multiple, child1 needs `γ≡0` or `Y+γ≡r` (since `180−Y−γ ≡ r−Y−γ`); child2 needs `γ≡X` or `Y+γ≡0`. Four combinations: (1) `γ≡0 & γ≡X ⇒ X≡0` ✗; (2) `γ≡0 & Y+γ≡0 ⇒ Y≡0` ✗; (3) `Y+γ≡r & γ≡X ⇒ X+Y≡r`, but `X+Y+Z≡r ⇒ Z≡0` ✗; (4) `Y+γ≡r & Y+γ≡0 ⇒ r≡0` ✗ (this is exactly where `θ ∤ 180` is used). So no such move; Shan-Yu perpetually keeps the game in `S`. ∎ (Real-angle version: same algebra in `ℝ/θℤ`; `S` is nonempty for `θ ∤ 180` — e.g. pick angles `(60°, 60°+ε, 60°−ε)` with `ε` irrational w.r.t. `θ`, so no angle is `kθ`.)
- **Constructive existence (the hard gap for the outliner to formalize):** when `θ | 180`, pick `X` = largest angle (`X ≥ 60°`). If `X` is a multiple of `θ` we already have a multiple (go to reduction). Else pick an adjacent angle `Y` (any; all are non-multiples in `S`) and set `γ = θ − (Y mod θ) ∈ (0,θ)`. Then `Y+γ` and `180−Y−γ` are both multiples of `θ`. Validity (`γ < X`, all child angles in `(0,180)`) splits into two cases:
  - `θ ≤ 60°`: `γ < θ ≤ 60° ≤ X`, and `X` not a multiple forces `X > θ` (when `θ=60°`, `X=60°` is a multiple, skipped), so `γ < X`. Also `Y ≤ 180−X ≤ 120°` (X max) ⇒ `Y+γ < 120°+60° = 180°`. ✓
  - `θ = 90°` (only divisor `> 60°`): if obtuse, `X > 90° > γ` ✓; if acute, `γ = 90−Y`, `γ < X ⇔ X+Y > 90° ⇔ Z < 90°` ✓ (acute). ✓ (Equivalently, this is the midpoint strategy.) 
  The outliner must verify these inequalities strictly in the real-angle (not just integer) setting; the integer-grid attractor strongly confirms but is not itself a proof.
- The constructive step makes *both* children carry a multiple of `θ`; whichever Shan-Yu keeps has an angle `kθ` with `1 ≤ k ≤ n−1`. The reduction `kθ → (k−1)θ` (split `kθ` into `θ + (k−1)θ` via `γ=θ`) strictly decreases `k`; terminates at `k=1` (angle `= θ`). Total move bound `≤ n = 180/θ` (empirically much less, ≈ log-ish). Finite. ✓
- The hard step / open gap is **rigorizing the constructive existence in the continuous setting** (the inequalities above) and **uniting the `θ ≤ 60°` and `θ = 90°` sub-cases** (or giving the outliner a single unified `γ ≡ −Y mod θ` lemma plus a clean `X = max` choice lemma). The obstruction and the descent are already essentially complete.
