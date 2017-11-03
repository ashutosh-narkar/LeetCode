#!/usr/bin/env python
'''
Given an integer, write a function to determine if it is a power of three.

One simple way of finding out if a number n is a power of a number b is to keep dividing n by b as long as the remainder is 0 and the dividend should be 1.

Time complexity :
O(log_b(n)) In our case that is O(log_3n). The number of divisions is given by that logarithm.
'''

def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 1:
        return False

    while n % 3 == 0:
        n /= 3

    return n == 1