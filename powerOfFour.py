#!/usr/bin/env python
"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

"""


def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    if num < 1:
        return False

    while num % 4 == 0:
        num = num / 4

    return num == 1
