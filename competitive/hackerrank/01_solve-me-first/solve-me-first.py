#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve_me_first(a, b):
    return a + b

if __name__ == "__main__":
    [num1, num2] = [int(_) for _ in input().strip().split()]
    print(solve_me_first(num1, num2))

# EOF