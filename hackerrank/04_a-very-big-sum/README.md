A Very Big Sum
==============

Source
------

This document has been stolen from <https://www.hackerrank.com/challenges/a-very-big-sum>

Problem
-------

You are given an array of integers of size $N$ . You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large.

### Input Format ###

The first line of the input consists of an integer $N$. The next line contains $N$ space-separated integers contained in the array.

### Constraints ###

  * $1 \le N \le 10$, and
  * $1 \le A[i] \le 10^{10}$.

### Output Format ###

Print a single value equal to the sum of the elements in the array.

### Sample Input ###

~~~~
5
1000000001 1000000002 1000000003 1000000004 1000000005
~~~~

### Sample Output ###

~~~~
5000000015
~~~~

### Note ###

  * The range of the 32-bit integer is $(-2^{31})$ to $(2^{31} - 1)$, o $[-2147483648, 2147483647]$.

  * When we add several integer values, the resulting sum might exceed the above range. You might need to use long long int in C/C++ or long data type in Java to store such sums.
