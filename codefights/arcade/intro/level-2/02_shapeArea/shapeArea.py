#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def shapeArea(n):
    result = 1
    for i in range(2, n+1):
        result += 4*(i - 1)
    return result

if __name__ == "__main__":
    assert shapeArea(2) == 5, "Test #1"
    assert shapeArea(3) == 13, "Test #2"
    assert shapeArea(1) == 1, "Test #3"
    assert shapeArea(5) == 41, "Test #4"

# EOF