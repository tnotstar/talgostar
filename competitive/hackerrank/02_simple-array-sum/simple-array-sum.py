#!/usr/bin/env python3
# -*- coding: utf-8 -*-

simple_array_sum = sum

if __name__ == "__main__":
    N = int(input().strip())
    data = [int(_) for _ in input().strip().split()]
    print(simple_array_sum(data))

# EOF