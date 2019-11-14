#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def checkio(input):
    def bits_and_parity_of(value):
        bits = parity = 0
        while value:
            bits += 1
            parity = ~parity
            value &= value - 1
        return bits, abs(parity)
    result = list()
    for v, p in [(_ >> 1, _ & 1) for _ in input]:
        bits, parity = bits_and_parity_of(v)
        if parity == p:
            result.append(chr(v))
    return "".join(result)


if __name__ == "__main__":
    assert checkio([135, 134, 124, 233, 209, 81, 42,  202, 198, 194, 229, 215,
                    230, 146, 28, 210, 145, 137, 222, 158, 49, 81, 214, 157]) == \
        "Checkio"
    assert checkio([144, 100, 200, 202, 216, 152, 164, 88,  216, 222, 65,  218,
                    175, 217, 248, 222, 171, 228, 216, 205, 254, 201, 193, 220]) == \
        "Hello World"

# EOF