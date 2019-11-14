Compare The Triplets
====================

Source
------

This document has been stolen from <https://www.hackerrank.com/challenges/compare-the-triplets>

Problem
-------

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from $1$ to $100$ for three categories: _problem clarity_, _originality_, and _difficulty_.

We define the rating for Alice's challenge to be the triplet $A = (a_0, a_1, a_2)$, and the rating for Bob's challenge to be the triplet $B = (b_0, b_1, b_2)$.

Your task is to find their comparison points by comparing $a_0$ with $b_0$, $a_1$ with $b_1$, and $a_2$ with $b_2$.

  * If $a_i > b_i$, then Alice is awarded $1$ point.
  * If $a_i < b_i$, then Bob is awarded $1$ point.
  * If $a_i = b_i$, then neither person receives a point.

Comparison points is the total points a person earned.

Given $A$ and $B$, can you compare the two challenges and print their respective comparison points?

### Input Format ###

  * The first line contains $3$ space-separated integers, $a_0$, $a_1$, and $a_2$, describing the respective values in triplet $A$.
  * The second line contains $3$ space-separated integers, $b_0$, $b_1$, and $b_2$, describing the respective values in triplet $B$.

### Constraints ###

  * $1 \le a_i \le 100$, and
  * $1 \le b_i \le 100$.

### Output Format ###

Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

### Sample Input ###

~~~~
5 6 7
3 6 10
~~~~

### Sample Output ###

~~~~
1 1
~~~~

### Explanation ###

In this example:

  * $A = (a_0, a_1, a_2) = (5, 6, 7)$, and
  * $B = (b_0, b_1, b_2) = (3, 6, 10)$.

Now, let's compare each individual score:

  * If $a_0 > b_0$, so Alice receives $1$ point.
  * If $a_1 = b_1$, so nobody receives a point.
  * If $a_2 < b_2$, so Bob receives $1$ point.

Alice's comparison score is $1$, and Bob's comparison score is $1$. Thus, we print `1 1` (Alice's comparison score followed by Bob's comparison score) on a single line.
