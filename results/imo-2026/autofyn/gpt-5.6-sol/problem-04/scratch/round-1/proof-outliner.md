## imo-2026-04

semigroup-crossing-binary-descent: new
Target: Prove that Mulan can guarantee finite victory exactly for theta = 180 degrees/n with an integer n >= 2.
Technique: Affine normalization, additive-semigroup invariant, pigeonhole/integer crossing, and strong descent; this adapts the local-menu-then-recursion move of crux problem aimo-0439 and the one-step label reduction of aimo-0014.
Skeleton:
  1. Normalize every angle by theta and put s=180 degrees/theta; encode a state by positive (a,b,c) with a+b+c=s — by change of variables and angle chasing.
  2. Record that a cut from the a-vertex, with 0<x<a, offers descendants (x,b,a+c-x) and (a-x,c,b+x) — by supplementary-angle identities.
  3. For necessity, suppose s is nonintegral and let Shan-Yu choose the initial equiangular state (s/3,s/3,s/3), whose coordinates are all nonintegral — since integral s/3 would make s integral.
  4. Maintain the invariant that every coordinate is outside Z: for any cut of a safe state, at least one offered child is safe — by pairing the only two possible newly integral coordinates in each child; the four pairings force respectively a, b, c, or s to be integral.
  5. Hence Shan-Yu can perpetually retain a triangle with no positive integral coordinate, excluding not only theta but every positive integral multiple of theta — by induction on moves.
  6. For sufficiency let s=n be an integer. If an angle is already an integer k, mark it. Otherwise find an orientation (a,b) and integer r with b<r<a+b, set x=r-b, and cut from the a-vertex — by the integer-crossing lemma.
  7. The two offered descendants then contain respectively r and n-r as angles, so whichever survives has a positive integral marked angle — by the transition formula and a+b+c=n.
  8. If the marked angle is k>1, cut that vertex with x=floor(k/2); the two children contain floor(k/2) and ceil(k/2), both positive and strictly below k — by the same transition formula.
  9. Iterate the integer monovariant k until k=1; then the retained triangle has angle theta and Mulan wins in finitely many steps — by strong descent.
  10. State and verify the characterization, noting n>=2 because 0<theta<180 degrees — by substitution theta=180 degrees/n.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Safe-child lemma: if a,b,c,s are nonintegral, the two children cannot both contain integral coordinates — because the possible pairs (x,a-x), (x,b+x), (a+c-x,a-x), (a+c-x,b+x) force a,b,c,s integral respectively.
  - Integer-crossing lemma: for positive nonintegral a,b,c with integer sum n, some ordered interval (b,a+b) contains an integer — because if some first coordinate a>1 the interval has length >1, while if all are <1 then n=2 and two fractional coordinates have sum >1.
  - Exact-theta descent: a marked k in Z_{>1} can be replaced, independent of Shan-Yu's branch, by a marked integer at most ceil(k/2) — because splitting the k-angle into floor(k/2) and ceil(k/2) puts one part in each child.
Open gaps: Expand Step 2's geometric realization, Step 4's exhaustive source classification, and Step 6's integer-crossing edge cases into rigorous prose; explicitly prove all cut parameters are strictly interior.
Cases to cover: s nonintegral; s=n integral with an existing integer coordinate; s=n integral with no integer coordinate; descent base k=1 and step k>1.
Watch out for: The negative invariant must exclude every positive integral multiple, not merely 1; the crossing interval is open; when a=1 or an angle is already integral, do not invoke the nonintegral crossing lemma; a finite descent to an unspecified multiple is insufficient.

backward-attractor-integer-strata: new
Target: Prove that the universal finite winning region is the whole angle simplex exactly when theta = 180 degrees/n for an integer n >= 2.
Technique: Backward reachability and finite-rank strata on the affine simplex, inspired by the state encoding of aimo-0225 and backward divisibility obstruction of aimo-0563.
Skeleton:
  1. Normalize by theta and define A_0 to be states with a coordinate 1; recursively let A_{m+1}=A_m union the states admitting a legal split for which both descendants lie in A_m — by the standard backward-attractor operator for an adversarial branch game.
  2. Prove by induction that membership in A_m gives Mulan a win in at most m further cuts, and conversely any strategy with worst-case depth at most m places the state in A_m — by induction on a finite binary decision tree.
  3. Let I be the stratum of states with at least one integral coordinate. If s is nonintegral, prove F(I) subset I: whenever both descendants contain integral coordinates, either the parent has one or s is integral — by the four affine pairings.
  4. Since A_0 subset I, induction gives every finite attractor layer A_m subset I; the safe equiangular initial state lies outside I, so no finite strategy wins from it — by predecessor closure, avoiding any unjustified uniform-bound assumption.
  5. If s=n is integral, prove every state lies either in I or in F(I): for a state outside I, an oriented interval (b,a+b) crosses an integer r, and x=r-b sends both children into I — by the integer-crossing lemma.
  6. Give I an explicit attractor rank: a state containing integer k has rank at most ceil(log_2 k) (up to a fixed indexing shift), because a balanced split sends both children to strata with a positive integer no larger than ceil(k/2) — by induction on k or dyadic blocks.
  7. Combining Steps 5 and 6, every state has finite rank bounded in terms of n, hence Mulan wins; identify theta=180 degrees/n and verify n>=2 — by the attractor equivalence.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Finite-tree equivalence: A_m is exactly the set of states winnable in at most m cuts — because Mulan chooses one split and Shan-Yu chooses one of its two children at each root.
  - Predecessor closure of I for nonintegral s — because simultaneous integral hits in the two children force an old integral coordinate or integral total through the four possible pairings.
  - One-step attraction to I for integral s — because an integer r strictly between b and a+b yields x=r-b in (0,a), while the complementary child receives n-r.
  - Dyadic rank descent — because splitting k into floor(k/2)+ceil(k/2) gives both branches a strictly smaller positive integral label.
Open gaps: Formalize the cumulative operator indexing and prove the crossing and predecessor-closure lemmas in full; compute a clean rank bound without relying on finite-grid evidence.
Cases to cover: nonintegral s; integral s and state outside I; integral s and marked k=1; integral s and k>=2.
Watch out for: Pointwise finite victory need not imply a uniform bound in general; here necessity must start from a particular state outside every A_m, while sufficiency supplies an explicit bound. Do not infer continuum exhaustion from rational grids.

fractional-color-safe-branch: new
Target: Characterize all theta for which every infinite subdivision tree can be cut so that all Shan-Yu branches terminate at an angle theta, obtaining exactly theta=180 degrees/n for n>=2.
Technique: Fractional-part coloring of the nested subdivision tree plus a well-founded integer label; this adapts the adversarial safe-response invariant of aimo-0746 and the terminating label-reduction pattern of aimo-0014.
Skeleton:
  1. View a play as a branch in the binary tree generated by Mulan's successive cevians, and color a node safe when none of its normalized angles is 0 modulo 1 — by reformulating the geometric game as a branching process.
  2. If s is nonintegral, start at the safe equiangular node and show every cut has a safe child — by the four-pair fractional-part calculation.
  3. Shan-Yu always selects that child, producing an infinite safe branch; no node on it has normalized angle 1, so necessity follows — by dependent recursive choice at each finite stage.
  4. If s=n is integral, define a productive node to carry a positive integer label equal to one of its angles. From an unlabelled node, choose a cyclic orientation whose angular interval crosses an integer and cut there; label the two children r and n-r — by the sector-crossing pigeonhole argument.
  5. At a node labeled k>1, split the labeled sector into j=floor(k/2) and k-j sectors; label the corresponding two children by these values — by direct angle chasing.
  6. Along every branch labels strictly decrease and in fact at least halve up to rounding, so every branch reaches label 1 after finitely many further cuts; translate label 1 back to angle theta — by a well-founded monovariant.
  7. Verify all reciprocal values and exclude n=1 from the allowed interval — by checking the original angle bounds.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Branch-stable safe coloring — because if each child had a zero fractional coordinate, subtracting or adding the two relevant affine expressions forces a parent's coordinate or the total to have zero fractional part.
  - Sector-crossing lemma — because either an angle exceeds one theta-sector, or all three are below one sector and their integer total forces total 2 with a pair crossing the next grid ray.
  - Well-founded branch lemma — because every child label lies in {floor(k/2),ceil(k/2)}, so the positive integer label reaches 1 regardless of branch choices.
Open gaps: Write the fractional calculation without pictorial ambiguity; prove strict sector-crossing and legal placement of P; state the recursive strategy as a function of the currently retained triangle.
Cases to cover: safe-tree obstruction; productive-node creation; labels k=1, k=2, and k>=3; theta=90 degrees as n=2 is included without a separate exception.
Watch out for: An infinite safe branch is a counterstrategy only because it excludes all integral multiples at every node. A label may switch vertices after Shan-Yu's choice; the strategy must mark the surviving label rather than track a fixed geometric vertex.

geometric-sector-induction: new
Target: Prove directly in geometric language that the winning angles are precisely theta=180 degrees/n, n>=2.
Technique: Theta-sector decomposition, angle chasing, and strong induction on a marked sector count; this is a synthetic rival to the abstract attractor formulation and borrows only the local-enumeration philosophy of aimo-0439.
Skeleton:
  1. For theta=180 degrees/n, superimpose conceptual theta-grid rays in each angle and use floor/ceiling sector counts to select two adjacent angles whose oriented sweep crosses an integer multiple r theta — by the pigeonhole/extremal principle.
  2. Draw the cevian from the first vertex so that its angle against the chosen side is (r-b)theta; verify this lies strictly inside the vertex angle — by the crossing inequalities.
  3. Angle chasing gives an r theta angle in one child and an (n-r)theta angle in the other, so every retained triangle has a marked integral number of sectors — by supplementary angles around the cut point.
  4. Prove by strong induction on k that a triangle with a marked k theta angle can be forced to theta: for k>1 split it into floor(k/2)theta and ceil(k/2)theta, and apply induction to whichever child remains — by the inductive hypothesis with smaller marked count.
  5. For the converse, if 180 degrees/theta is nonintegral, Shan-Yu begins with an equiangular triangle and, after each cevian, keeps a child all of whose angles avoid the theta-grid — by an exhaustive four-case angle chase.
  6. Conclude and verify the full characterization — by combining necessity and sufficiency.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Geometric crossing: a theta-grid ray lies strictly in a suitable angular sweep — because the three nonintegral sector remainders sum to an integer (necessarily 1 or 2), forcing a wrap for some ordered pair.
  - Complementary-sector production: the two children receive r and n-r sectors — because their relevant new angles add to the full straight-angle total n theta.
  - Sector induction: both possible surviving sector counts are smaller than k — because floor(k/2),ceil(k/2) lie in [1,k-1] for k>1.
  - Safe-child converse — because the four possible pairs of grid hits imply a parent grid angle or that the straight angle itself is on the theta-grid.
Open gaps: Turn the ray picture into explicit normalized inequalities, prove the four converse cases, and ensure every constructed ray meets the opposite side at a nonvertex point.
Cases to cover: initial triangle already has theta; initial integer multiple k>1; no initial multiple; nonreciprocal theta; boundary n=2.
Watch out for: This route must not invoke side lengths or assume a theta-grid physically exists globally; it is shorthand for exact angle equalities. Necessity and exact descent remain mandatory, not just production of some multiple.
