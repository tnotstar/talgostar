#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def makeArrayConsecutive2(statues):
    result = 0
    for i in range(min(statues), max(statues)+1):
        if i not in statues:
            result += 1
    return result

if __name__ == "__main__":
    assert makeArrayConsecutive2([6, 2, 3, 8]) == 3, "Test #1"
    assert makeArrayConsecutive2([0, 3]) == 2, "Test #2"
    assert makeArrayConsecutive2([5, 4, 6]) == 0, "Test #3"
    assert makeArrayConsecutive2([6, 3]) == 2, "Test #4"
    assert makeArrayConsecutive2([1]) == 0, "Test #5"

# EOF