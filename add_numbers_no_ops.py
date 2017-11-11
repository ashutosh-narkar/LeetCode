#!/usr/bin/env python
"""
Write a function that returns sum of two integers.
The function should not use any of the arithmetic operators (+, ++, -, --, .. etc).

Solution:
Sum of two bits can be obtained by performing XOR (^) of the two bits.
Carry bit can be obtained by performing AND (&) of two bits.
"""


def add(x, y):

    # TAKE A NOTE OF THIS CONDITION. ITS NOT "y > 0"
    while y != 0:
        # carry now contains common set bits of x and y
        carry = x & y

        # Sum of bits of x and y where at least one of the bits is not set
        x = x ^ y

        # Carry is shifted by one so that adding it to x gives the required sum
        y = carry << 1

    return x

if __name__ == '__main__':
    x = 15
    y = -35
    print add(x, y)