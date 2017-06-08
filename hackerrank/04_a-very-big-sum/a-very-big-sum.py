#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def a_very_big_sum(A):
    return sum(A)

if __name__ == "__main__":
    N = int(input().strip())
    A = [int(_) for _ in input().strip().split()][:N]
    print(a_very_big_sum(A))

# EOF