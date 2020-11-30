#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def theatre_square(n, m, a):
    return ((n // a) + int(n % a > 0)) * ((m // a) + int(m % a > 0))

n, m, a = [ int(_) for _ in sys.stdin.readline().split() ]
print(theatre_square(n, m, a))

# EOF