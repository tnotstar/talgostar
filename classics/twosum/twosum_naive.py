#!/usr/bin/env python
# -*- coding: utf-8 -*-

# stolen from:
# https://www.codementor.io/@info658/classic-python-interview-question-the-two-sum-problem-1aajub9joq

from timeit import timeit

def twosum_naive(data, target):
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == target:
                return (i, j)
    return None

assert twosum_naive([1, 2, 3], 4) in [(0, 2), (2, 0)]
assert twosum_naive([1234, 5678, 9012], 14690) in [(1, 2), (2, 1)]
assert twosum_naive([2, 2, 3], 4) in [(0, 1), (1, 0)]
assert twosum_naive([2, 2], 4) in [(0, 1), (1, 0)]
assert twosum_naive([8, 7, 2, 5, 3, 1], 10) in [(0, 2), (2, 0), (1, 4), (4, 1)]

print(timeit(lambda: twosum_naive([1234, 5678, 9012], 14690), number=100000))

# EOF
