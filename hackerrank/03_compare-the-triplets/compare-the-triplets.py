#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def compare_the_triplets(a, b):
    counters = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            counters[0] += 1
        elif a[i] < b[i]:
            counters[1] += 1
    return tuple(counters)

if __name__ == "__main__":
    a = [int(_) for _ in input().strip().split()]
    b = [int(_) for _ in input().strip().split()]
    rs = compare_the_triplets(a, b)
    print("{0} {1}".format(*rs))

# EOF