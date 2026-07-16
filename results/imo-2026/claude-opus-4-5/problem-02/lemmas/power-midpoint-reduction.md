# Power-Midpoint Reduction Lemma

## Statement

Let omega be a circle with center O and radius R. Let M = (A+B)/2 and N = (A+C)/2 be the midpoints of segments AB and AC respectively. Then:

**OM = ON** if and only if **pow(B, omega) - pow(C, omega) = (|AB|^2 - |AC|^2) / 2**

where pow(X, omega) = |XO|^2 - R^2 is the power of point X with respect to omega.

## Proof

Place A at the origin. Then M = B/2 and N = C/2.

**Step 1:** The perpendicular bisector of MN passes through the midpoint of MN and is perpendicular to M - N = (B - C)/2.

Midpoint of MN = (M + N)/2 = (B + C)/4

**Step 2:** O lies on the perpendicular bisector of MN if and only if:
(O - (B+C)/4) . (C - B) = 0

Equivalently: O . (C - B) = (B + C) . (C - B) / 4 = (|C|^2 - |B|^2) / 4

**Step 3:** Compute pow(B) - pow(C):
pow(B) - pow(C) = |BO|^2 - |CO|^2
                = |B - O|^2 - |C - O|^2
                = |B|^2 - 2 O.B + |O|^2 - |C|^2 + 2 O.C - |O|^2
                = |B|^2 - |C|^2 + 2 O.(C - B)

**Step 4:** Substitute the condition from Step 2:
If O lies on the perpendicular bisector of MN, then O.(C-B) = (|C|^2 - |B|^2)/4, so:
pow(B) - pow(C) = |B|^2 - |C|^2 + 2 * (|C|^2 - |B|^2)/4
                = |B|^2 - |C|^2 + (|C|^2 - |B|^2)/2
                = (|B|^2 - |C|^2)/2

Since A is at the origin, |B| = |AB| and |C| = |AC|, so:
pow(B) - pow(C) = (|AB|^2 - |AC|^2) / 2

**Step 5:** Conversely, if pow(B) - pow(C) = (|AB|^2 - |AC|^2)/2, then working backward through the algebra shows O.(C-B) = (|C|^2 - |B|^2)/4, so O lies on the perpendicular bisector of MN.

**Step 6:** Since M and N are symmetric with respect to the perpendicular bisector of MN, any point on this perpendicular bisector is equidistant from M and N. Therefore O on perp-bisector(MN) implies OM = ON.

QED.

## Status
Certified by proof-reviewer, Round 1.
