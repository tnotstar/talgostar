#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def adjacentElementsProduct(inputArray):
    last = len(inputArray) - 1
    maximum = None
    for i in range(last):
        product = inputArray[i] * inputArray[i+1]
        if not maximum or product > maximum:
            maximum = product
    return maximum

if __name__ == "__main__":
    assert adjacentElementsProduct([3, 6, -2, -5, 7, 3]) == 21, "Test #1"
    assert adjacentElementsProduct([-1, -2]) == 2, "Test #2"
    assert adjacentElementsProduct([5, 1, 2, 3, 1, 4]) == 6, "Test #3"
    assert adjacentElementsProduct([1, 2, 3, 0]) == 6, "Test #4"
    assert adjacentElementsProduct([9, 5, 10, 2, 24, -1, -48]) == 50, "Test #5"
    assert adjacentElementsProduct([5, 6, -4, 2, 3, 2, -23]) == 30, "Test #6"
    assert adjacentElementsProduct([4, 1, 2, 3, 1, 5]) == 6, "Test #7"
    assert adjacentElementsProduct([-23, 4, -3, 8, -12]) == -12, "Test #8"

# EOF