#!/usr/bin/env python
"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""


def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    low = 1
    high = num

    while low <= high:
        mid = low + (high - low) / 2

        if mid * mid == num:
            return True

        elif mid * mid > num:
            high = mid - 1

        else:
            low = mid + 1

    return False