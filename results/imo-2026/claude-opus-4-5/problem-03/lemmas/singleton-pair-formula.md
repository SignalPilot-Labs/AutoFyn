# Singleton-Pair Formula Lemma

## Statement

When XY creates exactly 2n pieces split as (n-1) equal pairs {a_k, a_k} (k = 1, ..., n-1) plus 2 singletons s_1 < s_2 (all summing to 1), then:

LB = (1 - s_1 + s_2)/2 = 1/2 + (s_2 - s_1)/2

## Proof

The 2n pieces consist of (n-1) pairs and 2 singletons.

**Step 1: Apply Pairing Cancellation (n-1) times.**

By the Pairing Cancellation Lemma, the pairs contribute exactly a_1 + a_2 + ... + a_{n-1} to LB's score.

**Step 2: Determine singleton contribution.**

With 2n pieces total, LB picks n pieces. After accounting for the pairs (LB picks one from each pair), LB has picked (n-1) pieces and must pick 1 more from the 2 singletons.

Since LB picks odd positions and pairs occupy consecutive positions with alternating parity, one singleton goes to LB and one to XY. The singletons occupy two positions whose parities differ. Since s_2 > s_1, s_2 comes before s_1 in the sorted order.

In the greedy alternating selection, the larger singleton s_2 goes to LB.

**Step 3: Compute total.**

Total sum = 2*(a_1 + ... + a_{n-1}) + s_1 + s_2 = 1.

So a_1 + ... + a_{n-1} = (1 - s_1 - s_2)/2.

LB's total = (pair contribution) + (singleton contribution)
          = (1 - s_1 - s_2)/2 + s_2
          = 1/2 - s_1/2 - s_2/2 + s_2
          = 1/2 - s_1/2 + s_2/2
          = (1 - s_1 + s_2)/2
          = 1/2 + (s_2 - s_1)/2

QED.

## Note

This formula applies even when s_2 equals one of the pair values (since ties in sorting preserve the parity structure).

## Certified

This lemma is certified by the proof-reviewer (Round 5). Independently verified computationally with multiple test cases including edge cases where s_2 equals a pair value.
