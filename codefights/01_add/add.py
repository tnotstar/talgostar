#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(param1, param2):
    return param1 + param2

if __name__ == "__main__":
    assert add(1, 2) == 3, "Test #1"
    assert add(0, 1000) == 1000, "Test #2"

# EOF