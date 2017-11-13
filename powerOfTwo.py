#!/usr/bin/env python
"""
Given an integer, write a function to determine if it is a power of two.

"""


def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 1:
        return False

    while n % 2 == 0:
        n = n / 2

    return n == 1
