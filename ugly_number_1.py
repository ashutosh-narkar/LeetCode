#!/usr/bin/env python
"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""


def isUgly(num):
    """
    :type num: int
    :rtype: bool
    """

    if num == 0:
        return False

    for i in [2, 3, 5]:

        while num % i == 0:
            num = num / i

    return num == 1
